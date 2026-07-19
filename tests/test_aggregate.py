"""aggregate.py 邊界案例測試(比照 quant skill v6/v7 教訓:不要只跑 smoke test)。"""
import pytest

from engine.aggregate import aggregate, disagreement


def op(d, c):
    return {"direction": d, "confidence": c}


class TestAggregate:
    def test_single_persona(self):
        assert aggregate([op("Bullish", 70)]) == ("Bullish", 100)

    def test_all_agree(self):
        d, c = aggregate([op("Bearish", 60), op("Bearish", 80), op("Bearish", 40)])
        assert d == "Bearish" and c == 100

    def test_weighted_majority_beats_headcount(self):
        # 兩個低信心多頭 vs 一個高信心空頭:信心加權讓空方勝
        d, _ = aggregate([op("Bullish", 20), op("Bullish", 20), op("Bearish", 90)])
        assert d == "Bearish"

    def test_exact_tie_returns_neutral(self):
        d, _ = aggregate([op("Bullish", 50), op("Bearish", 50)])
        assert d == "Neutral"

    def test_all_zero_confidence(self):
        assert aggregate([op("Bullish", 0), op("Bearish", 0)]) == ("Neutral", 0)

    def test_confidence_score_is_share(self):
        d, c = aggregate([op("Bullish", 60), op("Bearish", 40)])
        assert d == "Bullish" and c == 60

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            aggregate([])

    def test_invalid_direction_raises(self):
        with pytest.raises(ValueError):
            aggregate([op("Long", 50)])

    def test_out_of_range_confidence_raises(self):
        with pytest.raises(ValueError):
            aggregate([op("Bullish", 101)])
        with pytest.raises(ValueError):
            aggregate([op("Bullish", -1)])


class TestDisagreement:
    def test_single_persona_zero(self):
        assert disagreement([op("Bullish", 70)]) == (0, 0)

    def test_all_agree_same_confidence(self):
        assert disagreement([op("Bullish", 50), op("Bullish", 50)]) == (0, 0)

    def test_full_split(self):
        ratio, _ = disagreement([op("Bullish", 50), op("Bearish", 50)])
        assert ratio == 0.5

    def test_confidence_std(self):
        _, std = disagreement([op("Bullish", 40), op("Bullish", 60)])
        assert std == 10  # 母體標準差

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            disagreement([])
