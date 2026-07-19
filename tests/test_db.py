"""db.py 落地層測試:寫入不可覆寫、單/多人格 finalize、事後回填邊界。"""
import pytest

from database.db import get_session, record_opinion, finalize, fill_outcomes, upsert_market


@pytest.fixture
def session(tmp_path):
    return get_session(f"sqlite:///{tmp_path / 'test.db'}")


def rec(session, persona, round_, direction, conf, date="2026-01-01"):
    return record_opinion(session, date=date, asset="BTC/USDT", persona=persona,
                          round_=round_, direction=direction, confidence=conf,
                          reasoning="test", model_id="test-model")


class TestRecord:
    def test_duplicate_raises(self, session):
        rec(session, "ict", 1, "Bullish", 70)
        with pytest.raises(ValueError, match="不可覆寫"):
            rec(session, "ict", 1, "Bearish", 30)

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

    def test_price_at_bias_from_market(self, session):
        upsert_market(session, {"date": "2026-01-01", "asset": "BTC/USDT",
                                "close": 50000.0}, "summary")
        rec(session, "ict", 1, "Bullish", 70)
        r = finalize(session, date="2026-01-01", asset="BTC/USDT", protocol_version="test")
        assert r.price_at_bias == 50000.0


class TestFillOutcomes:
    import datetime as _dt

    def _setup(self, session):
        rec(session, "ict", 1, "Bullish", 70)
        finalize(session, date="2026-01-01", asset="BTC/USDT", protocol_version="test")

    def test_fills_only_closed_candles(self, session):
        self._setup(session)
        today = self._dt.date(2026, 1, 4)  # 只有 +1d(01-02)已收
        filled = fill_outcomes(session, lambda a, d: 123.0, today=today)
        assert filled
        from database.schema import DailyBiasResult
        row = session.query(DailyBiasResult).one()
        assert row.price_after_1d == 123.0
        assert row.price_after_5d is None and row.price_after_20d is None

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
