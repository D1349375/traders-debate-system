"""db.py 落地層測試:寫入不可覆寫、單/多人格 finalize、事後回填邊界。"""
import sqlite3

import pytest

from database.db import get_session, record_opinion, finalize, fill_outcomes, upsert_market
from database.schema import MarketData


@pytest.fixture
def session(tmp_path):
    return get_session(f"sqlite:///{tmp_path / 'test.db'}")


def rec(session, persona, round_, direction, conf, date="2026-01-01", intraday_scenario="test scenario"):
    return record_opinion(session, date=date, asset="BTC/USDT", persona=persona,
                          round_=round_, direction=direction, confidence=conf,
                          reasoning="test", intraday_scenario=intraday_scenario,
                          model_id="test-model")


class TestRecord:
    def test_duplicate_raises(self, session):
        rec(session, "ict", 1, "Bullish", 70)
        with pytest.raises(ValueError, match="不可覆寫"):
            rec(session, "ict", 1, "Bearish", 30)

    def test_intraday_scenario_required(self, session):
        with pytest.raises(ValueError, match="intraday_scenario 為必填"):
            rec(session, "ict", 1, "Bullish", 70, intraday_scenario=None)
        with pytest.raises(ValueError, match="intraday_scenario 為必填"):
            rec(session, "ict", 1, "Bullish", 70, intraday_scenario="   ")

    def test_invalid_round_raises(self, session):
        with pytest.raises(ValueError):
            rec(session, "ict", 3, "Bullish", 70)

    def test_invalid_direction_raises(self, session):
        with pytest.raises(ValueError):
            rec(session, "ict", 1, "Long", 70)


class TestFinalize:
    def test_single_persona_final_equals_r1(self, session):
        rec(session, "ict", 1, "Bullish", 70)
        r = finalize(session, date="2026-01-01", asset="BTC/USDT", protocol_version="test")
        assert r.r1_direction == "Bullish" and r.consensus_direction == "Bullish"
        assert r.n_personas == 1 and r.disagreement_ratio == 0

    def test_r2_overrides_final_but_keeps_r1_baseline(self, session):
        rec(session, "ict", 1, "Bullish", 80)
        rec(session, "tjr", 1, "Bullish", 60)
        rec(session, "ict", 2, "Bullish", 40)
        rec(session, "tjr", 2, "Bearish", 90)
        r = finalize(session, date="2026-01-01", asset="BTC/USDT", protocol_version="test")
        assert r.r1_direction == "Bullish"          # 旁路基準
        assert r.consensus_direction == "Bearish"   # 末輪信心加權
        assert r.disagreement_ratio == 0.5

    def test_no_r1_raises(self, session):
        with pytest.raises(ValueError, match="沒有任何 R1"):
            finalize(session, date="2026-01-01", asset="BTC/USDT", protocol_version="test")

    def test_duplicate_finalize_raises(self, session):
        rec(session, "ict", 1, "Bullish", 70)
        finalize(session, date="2026-01-01", asset="BTC/USDT", protocol_version="test")
        with pytest.raises(ValueError, match="不可覆寫"):
            finalize(session, date="2026-01-01", asset="BTC/USDT", protocol_version="test")

    def test_snapshot_captured_at_propagates_from_market(self, session):
        upsert_market(session, {"date": "2026-01-01", "asset": "BTC/USDT", "close": 50000.0,
                                "snapshot_captured_at": "2026-01-01T00:03:00Z"}, "summary")
        rec(session, "ict", 1, "Bullish", 70)
        r = finalize(session, date="2026-01-01", asset="BTC/USDT", protocol_version="test")
        assert r.snapshot_captured_at == "2026-01-01T00:03:00Z"

    def test_snapshot_captured_at_none_when_no_market_row(self, session):
        rec(session, "ict", 1, "Bullish", 70)
        r = finalize(session, date="2026-01-01", asset="BTC/USDT", protocol_version="test")
        assert r.snapshot_captured_at is None

    def test_price_at_bias_from_market(self, session):
        upsert_market(session, {"date": "2026-01-01", "asset": "BTC/USDT",
                                "close": 50000.0}, "summary")
        rec(session, "ict", 1, "Bullish", 70)
        r = finalize(session, date="2026-01-01", asset="BTC/USDT", protocol_version="test")
        assert r.price_at_bias == 50000.0


class TestUpsertMarketVariant:
    """資訊分流(v4/v5):core/emperorbtc/tjr 三變體各自獨立存欄,互不覆寫對方文字。"""

    def test_core_and_emperorbtc_write_separate_columns(self, session):
        upsert_market(session, {"date": "2026-01-01", "asset": "BTC/USDT", "close": 50000.0},
                      "core摘要文字", variant="core")
        row = upsert_market(session, {"date": "2026-01-01", "asset": "BTC/USDT", "close": 50001.0},
                            "emperorbtc摘要文字", variant="emperorbtc")
        assert row.context_summary == "core摘要文字"
        assert row.context_summary_emperorbtc == "emperorbtc摘要文字"

    def test_all_three_variants_write_separate_columns(self, session):
        upsert_market(session, {"date": "2026-01-01", "asset": "BTC/USDT"}, "core文字", variant="core")
        upsert_market(session, {"date": "2026-01-01", "asset": "BTC/USDT"}, "emp文字", variant="emperorbtc")
        row = upsert_market(session, {"date": "2026-01-01", "asset": "BTC/USDT"}, "tjr文字", variant="tjr")
        assert row.context_summary == "core文字"
        assert row.context_summary_emperorbtc == "emp文字"
        assert row.context_summary_tjr == "tjr文字"

    def test_default_variant_is_core(self, session):
        row = upsert_market(session, {"date": "2026-01-01", "asset": "BTC/USDT",
                                      "close": 50000.0}, "summary")
        assert row.context_summary == "summary"
        assert row.context_summary_emperorbtc is None


class TestSchemaAutoMigration:
    """get_session() 對已存在的舊版 DB 自動補齊 schema.py 新增的欄位,不需手動 ALTER TABLE。"""

    def test_missing_column_on_existing_table_gets_added(self, tmp_path):
        db_path = tmp_path / "legacy.db"
        con = sqlite3.connect(str(db_path))
        # 模擬缺少 context_summary_emperorbtc 的舊版 market_data 表(其餘欄位齊全)
        con.execute("""CREATE TABLE market_data (
            id INTEGER PRIMARY KEY, date VARCHAR NOT NULL, asset VARCHAR NOT NULL,
            open_price FLOAT, high_price FLOAT, low_price FLOAT, close_price FLOAT,
            volume FLOAT, funding_rate FLOAT, open_interest FLOAT,
            context_summary TEXT, snapshot_captured_at VARCHAR
        )""")
        con.commit()
        con.close()

        session = get_session(f"sqlite:///{db_path}")
        row = upsert_market(session, {"date": "2026-01-01", "asset": "BTC/USDT",
                                      "close": 50000.0}, "emperorbtc摘要", variant="emperorbtc")
        assert row.context_summary_emperorbtc == "emperorbtc摘要"

    def test_no_op_when_schema_already_complete(self, tmp_path):
        # 已是最新 schema 時重複呼叫 get_session() 不應報錯、不應遺失既有資料
        db_url = f"sqlite:///{tmp_path / 'fresh.db'}"
        session = get_session(db_url)
        upsert_market(session, {"date": "2026-01-01", "asset": "BTC/USDT",
                                "close": 50000.0}, "summary")
        session2 = get_session(db_url)
        row = session2.query(MarketData).filter_by(date="2026-01-01", asset="BTC/USDT").one()
        assert row.context_summary == "summary"


class TestFillOutcomes:
    import datetime as _dt

    def _setup(self, session):
        rec(session, "ict", 1, "Bullish", 70)
        finalize(session, date="2026-01-01", asset="BTC/USDT", protocol_version="test")

    def test_fills_only_closed_candles(self, session):
        self._setup(session)
        today = self._dt.date(2026, 1, 3)  # 判斷日 01-01 自己那根K線(1d地平線目標)01-02收盤,01-03已收
        filled = fill_outcomes(session, lambda a, d: 123.0, today=today)
        assert filled
        from database.schema import DailyBiasResult
        row = session.query(DailyBiasResult).one()
        assert row.price_after_1d == 123.0
        assert row.price_after_5d is None and row.price_after_20d is None

    def test_1d_horizon_targets_judgment_days_own_candle(self, session):
        """判斷日 D 的 price_after_1d 應該抓 D 自己那根日K的收盤(D+1 00:00 UTC),
        不是 D+1 那根日K的收盤(D+2 00:00 UTC)——後者會多算一天(2026-07-22 修正的 bug)。"""
        self._setup(session)  # date="2026-01-01"
        requested_dates = []

        def fake_fetch(asset, date_str):
            requested_dates.append(date_str)
            return 100.0

        fill_outcomes(session, fake_fetch, today=self._dt.date(2026, 2, 1))
        assert "2026-01-01" in requested_dates  # 1d → D 自己(不是 2026-01-02)
        assert "2026-01-05" in requested_dates  # 5d → D+4
        assert "2026-01-20" in requested_dates  # 20d → D+19

    def test_fills_all_when_elapsed_and_idempotent(self, session):
        self._setup(session)
        today = self._dt.date(2026, 2, 1)
        fill_outcomes(session, lambda a, d: 123.0, today=today)
        # 第二次跑:已填欄位不再觸碰(fetch 回傳不同值也不覆寫)
        filled = fill_outcomes(session, lambda a, d: 999.0, today=today)
        assert filled == []
        from database.schema import DailyBiasResult
        row = session.query(DailyBiasResult).one()
        assert row.price_after_1d == row.price_after_5d == row.price_after_20d == 123.0

    def test_fetch_none_leaves_empty(self, session):
        self._setup(session)
        filled = fill_outcomes(session, lambda a, d: None, today=self._dt.date(2026, 2, 1))
        assert filled == []
