"""機械聚合與分歧度統計(裁判層的計算核心)。

規則預先寫死(見 preregistration):
- 信心加權投票:direction_score[d] = Σ confidence,取最高分方向;平手 → Neutral
- confidence_score = 勝方得分占總信心的比例(0-100);總信心為 0 → Neutral / 0
- 分歧度:disagreement_ratio = 1 - 眾數方向占比;confidence_std = 母體標準差
純函數、不碰 DB、不呼叫 LLM——裁判的聚合不允許被語言模型推翻。
"""
import math

VALID_DIRECTIONS = ("Bullish", "Bearish", "Neutral")


def aggregate(opinions):
    """opinions: list of {"direction": str, "confidence": int} → (direction, confidence_score)"""
    if not opinions:
        raise ValueError("opinions 不可為空")
    scores = {d: 0 for d in VALID_DIRECTIONS}
    total = 0
    for op in opinions:
        d = op["direction"]
        if d not in VALID_DIRECTIONS:
            raise ValueError(f"非法方向: {d}")
        c = int(op["confidence"])
        if not (0 <= c <= 100):
            raise ValueError(f"confidence 超出 0-100: {c}")
        scores[d] += c
        total += c
    if total == 0:
        return "Neutral", 0
    best = max(scores.values())
    winners = [d for d, s in scores.items() if s == best]
    if len(winners) > 1:
        return "Neutral", round(best / total * 100)
    return winners[0], round(best / total * 100)


def disagreement(opinions):
    """→ (disagreement_ratio, confidence_std)。單人格時皆為 0。"""
    if not opinions:
        raise ValueError("opinions 不可為空")
    n = len(opinions)
    counts = {}
    for op in opinions:
        counts[op["direction"]] = counts.get(op["direction"], 0) + 1
    ratio = 1 - max(counts.values()) / n
    confs = [int(op["confidence"]) for op in opinions]
    mean = sum(confs) / n
    std = math.sqrt(sum((c - mean) ** 2 for c in confs) / n)
    return round(ratio, 4), round(std, 4)
