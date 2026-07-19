"""摘要 v2 純函數測試:已收盤判定邊界、CSV 格式、摘要組裝。"""
from data.ingestion import select_closed, format_candles, compose_summary_v2

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
