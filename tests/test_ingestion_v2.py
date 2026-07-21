"""摘要 v2/v4 純函數測試:已收盤判定邊界、CSV 格式、摘要組裝、資訊分流(core/emperorbtc)。"""
from data.ingestion import (select_closed, format_candles, compose_summary_v2,
                            compute_rsi, compute_volume_ratio, classify_macro_calendar)

DAY = 86400 * 1000


def candle(ts, price=100.0):
    return [ts, price, price + 1, price - 1, price, 10.0]


class TestSelectClosed:
    def test_excludes_unclosed_candle(self):
        # as_of 落在第二根 K 線中間:只有第一根已收
        rows = [candle(0), candle(DAY)]
        assert select_closed(rows, DAY, DAY + 1000, count=10) == [rows[0]]

    def test_close_exactly_at_as_of_counts_as_closed(self):
        rows = [candle(0)]
        assert select_closed(rows, DAY, DAY, count=10) == rows

    def test_trims_to_count_keeping_latest(self):
        rows = [candle(i * DAY) for i in range(5)]
        out = select_closed(rows, DAY, 10 * DAY, count=2)
        assert out == rows[3:]

    def test_empty_input(self):
        assert select_closed([], DAY, DAY, count=5) == []


class TestFormatCandles:
    def test_header_and_rows(self):
        text = format_candles([candle(0), candle(DAY)])
        lines = text.split("\n")
        assert lines[0] == "date,open,high,low,close,volume"
        assert len(lines) == 3
        assert lines[1].startswith("1970-01-01 00:00,")

    def test_empty_gives_header_only(self):
        assert format_candles([]) == "date,open,high,low,close,volume"

    def test_include_volume_false_omits_column_entirely(self):
        text = format_candles([candle(0)], include_volume=False)
        lines = text.split("\n")
        assert lines[0] == "date,open,high,low,close"
        assert "volume" not in text
        assert lines[1].count(",") == 4  # date + 4 數值欄位,無第5個逗號分隔的volume


class TestComputeRSI:
    def test_insufficient_data_returns_none(self):
        assert compute_rsi([100.0] * 10, period=14) is None

    def test_monotonic_increase_near_100(self):
        closes = [100.0 + i for i in range(20)]
        rsi = compute_rsi(closes, period=14)
        assert rsi > 95

    def test_monotonic_decrease_near_0(self):
        closes = [100.0 - i for i in range(20)]
        rsi = compute_rsi(closes, period=14)
        assert rsi < 5

    def test_flat_prices_no_movement(self):
        # avg_gain=avg_loss=0 → 依慣例(avg_loss==0)回 100
        rsi = compute_rsi([100.0] * 20, period=14)
        assert rsi == 100.0

    def test_exact_minimum_length_computes(self):
        closes = [100.0 + i for i in range(15)]  # period+1 = 15 筆,邊界值
        assert compute_rsi(closes, period=14) is not None


class TestClassifyMacroCalendar:
    def test_nfp_week_detected(self):
        # 2026-01-02 是 2026年1月第一個星期五(NFP發布日),2026-01-01 落在同一週
        flags, _ = classify_macro_calendar("2026-01-01")
        assert any("NFP" in f for f in flags)

    def test_fomc_week_detected(self):
        # 2026-01-27/28 為官方公布之FOMC會議日期(federalreserve.gov)
        flags, _ = classify_macro_calendar("2026-01-27")
        assert any("FOMC" in f for f in flags)

    def test_august_flag(self):
        flags, _ = classify_macro_calendar("2026-08-15")
        assert any("8月" in f for f in flags)
        assert not any("NFP" in f or "FOMC" in f for f in flags)  # 該週非NFP週也非FOMC週

    def test_ordinary_week_no_flags(self):
        flags, _ = classify_macro_calendar("2026-07-22")
        assert flags == []

    def test_coverage_note_always_present(self):
        _, note = classify_macro_calendar("2026-07-22")
        assert "CPI" in note and "未涵蓋" in note  # 誠實揭露涵蓋範圍外的項目


class TestComputeVolumeRatio:
    def test_insufficient_data_returns_none_triplet(self):
        assert compute_volume_ratio([10.0] * 5, window=7) == (None, None, None)

    def test_exact_minimum_length_computes(self):
        volumes = [10.0] * 7 + [20.0]  # window+1 = 8 筆,邊界值
        avg, cur, ratio = compute_volume_ratio(volumes, window=7)
        assert avg == 10.0 and cur == 20.0 and ratio == 2.0

    def test_current_excluded_from_baseline_average(self):
        # 若當前這筆(1000)被誤算進均量,比值會被嚴重低估
        volumes = [10.0] * 7 + [1000.0]
        avg, cur, ratio = compute_volume_ratio(volumes, window=7)
        assert avg == 10.0  # 不含當前這筆
        assert ratio == 100.0

    def test_zero_baseline_avg_ratio_is_none(self):
        volumes = [0.0] * 7 + [5.0]
        avg, cur, ratio = compute_volume_ratio(volumes, window=7)
        assert avg == 0.0 and ratio is None


class TestComposeSummary:
    def _snapshot(self):
        return {"price": 64500.0, "change_24h": 1.2, "high": 64900.0,
                "low": 64100.0, "note": None}

    def test_contains_all_sections(self):
        s = compose_summary_v2("BTC/USDT", "2026-07-19",
                               [("1w", [candle(0)]), ("1d", [candle(0)]), ("4h", [candle(0)])],
                               0.0001, 0.00005, self._snapshot())
        for expect in ["週線", "日線", "4小時線", "資金費率", "當下快照",
                       "判斷日: 2026-07-19", "0.000100", "Daily Bias"]:
            assert expect in s

    def test_funding_unavailable_is_honest(self):
        s = compose_summary_v2("BTC/USDT", "2026-07-19",
                               [("1d", [candle(0)])], None, None, self._snapshot())
        assert "無法取得" in s

    def test_backtest_note_shown(self):
        snap = {"price": 100.0, "change_24h": None, "high": None, "low": None,
                "note": "回測模式:以該日開盤價為判斷時點近似,無盤中資訊"}
        s = compose_summary_v2("BTC/USDT", "2026-03-01",
                               [("1d", [candle(0)])], None, None, snap)
        assert "回測模式" in s
        assert "盤中高/低" not in s  # 回測模式不得出現盤中資訊

    def test_core_variant_has_no_volume_or_indicator_section(self):
        s = compose_summary_v2("BTC/USDT", "2026-07-19",
                               [("1d", [candle(i * DAY) for i in range(20)])],
                               0.0001, 0.00005, self._snapshot(), variant="core")
        assert "volume" not in s
        assert "量能與動能指標" not in s
        assert "CSV 欄位:date,open,high,low,close" in s
        assert "close,volume" not in s

    def test_emperorbtc_variant_has_volume_and_indicator_section(self):
        s = compose_summary_v2("BTC/USDT", "2026-07-19",
                               [("1d", [candle(i * DAY) for i in range(20)])],
                               0.0001, 0.00005, self._snapshot(), variant="emperorbtc")
        assert "close,volume" in s
        assert "量能與動能指標" in s
        assert "RSI(14)" in s
        assert "均量" in s

    def test_default_variant_is_core(self):
        s_default = compose_summary_v2("BTC/USDT", "2026-07-19",
                                       [("1d", [candle(0)])], None, None, self._snapshot())
        s_core = compose_summary_v2("BTC/USDT", "2026-07-19",
                                    [("1d", [candle(0)])], None, None, self._snapshot(), variant="core")
        assert s_default == s_core

    def test_macro_calendar_section_present_in_all_variants(self):
        for variant in ("core", "emperorbtc", "tjr"):
            s = compose_summary_v2("BTC/USDT", "2026-01-27",
                                   [("1d", [candle(0)])], None, None, self._snapshot(), variant=variant)
            assert "總經行事曆旗標" in s and "FOMC" in s

    def test_tjr_variant_includes_correlated_asset_block(self):
        ref_sections = [("1d", [candle(i * DAY, price=2000.0) for i in range(3)])]
        s = compose_summary_v2("BTC/USDT", "2026-07-19",
                               [("1d", [candle(0)])], None, None, self._snapshot(),
                               variant="tjr", ref_asset="ETH/USDT", ref_sections=ref_sections)
        assert "相關資產參考行情:ETH/USDT" in s
        assert "非精算結論" in s
        assert "2000.0" in s  # 對方標的的實際價格有出現
        assert "close,volume" not in s  # 參考行情同樣不含成交量

    def test_non_tjr_variant_has_no_correlated_asset_block(self):
        s = compose_summary_v2("BTC/USDT", "2026-07-19",
                               [("1d", [candle(0)])], None, None, self._snapshot(), variant="core")
        assert "相關資產參考行情" not in s
