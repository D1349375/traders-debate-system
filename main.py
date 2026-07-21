"""DebateSystem CLI — 供 Claude Code orchestrator(trader-debate skill)呼叫的落地工具。

LLM 推理不在這裡發生:人格判斷由 Claude Code subagent 產生(C 架構),
本 CLI 只負責行情抓取與 DB 落地。協議見 README 第 3 節。

用法:
  python main.py market   [--asset BTC/USDT]         抓行情、寫入 market_data、印出摘要
  python main.py record   --json <file>              落地人格判斷(單筆物件或列表)
  python main.py finalize --date YYYY-MM-DD --asset BTC/USDT [--summary-file <file>]
  python main.py outcomes                            回填已收K線的事後價格
"""
import argparse
import json
import sys

# Windows console 預設 cp950 會把中文輸出打成亂碼;orchestrator 依賴 stdout,強制 UTF-8
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

from data.ingestion import build_market_context, fetch_close_on
from database.db import get_session, upsert_market, record_opinion, finalize, fill_outcomes

# v2-2026-07-19:摘要升級為多時間框架資訊集(週52/日90/4h42+費率+快照,見 市場摘要v2_資訊集設計.md)
# v3-2026-07-20:新增 1H/15M/5M 日內時間框架 + intraday_scenario 必填欄位(見 preregistration.md §8)
# 協議不變:兩輪固定,R1 盲判 → R2 結構化反駁;單人格只跑 R1
PROTOCOL_VERSION = "v3-2026-07-20"


def cmd_market(args):
    data, summary = build_market_context(args.asset, as_of=args.as_of)
    if not data:
        print("抓取行情失敗", file=sys.stderr)
        return 1
    session = get_session()
    upsert_market(session, data, summary)
    print(json.dumps({"date": data["date"], "asset": data["asset"]}, ensure_ascii=False))
    print(summary)
    return 0


def cmd_record(args):
    with open(args.json, 'r', encoding='utf-8') as f:
        payload = json.load(f)
    records = payload if isinstance(payload, list) else [payload]
    session = get_session()
    for rec in records:
        record_opinion(
            session,
            date=rec["date"], asset=rec["asset"], persona=rec["persona"],
            round_=int(rec["round"]), direction=rec["direction"],
            confidence=rec["confidence"], reasoning=rec["reasoning"],
            intraday_scenario=rec.get("intraday_scenario"),
            falsifier=rec.get("falsifier"), model_id=rec.get("model_id"),
        )
        print(f"✅ 落地 {rec['date']} {rec['asset']} {rec['persona']} R{rec['round']}: "
              f"{rec['direction']} ({rec['confidence']})")
    return 0


def cmd_finalize(args):
    summary_reasoning = None
    if args.summary_file:
        with open(args.summary_file, 'r', encoding='utf-8') as f:
            summary_reasoning = f.read()
    session = get_session()
    result = finalize(session, date=args.date, asset=args.asset,
                      protocol_version=PROTOCOL_VERSION,
                      summary_reasoning=summary_reasoning)
    print(json.dumps({
        "date": result.date, "asset": result.asset,
        "r1_direction": result.r1_direction, "r1_confidence": result.r1_confidence,
        "consensus_direction": result.consensus_direction,
        "confidence_score": result.confidence_score,
        "n_personas": result.n_personas,
        "disagreement_ratio": result.disagreement_ratio,
        "confidence_std": result.confidence_std,
        "price_at_bias": result.price_at_bias,
    }, ensure_ascii=False, indent=2))
    return 0


def cmd_outcomes(args):
    session = get_session()
    filled = fill_outcomes(session, fetch_close_on)
    if filled:
        for date, asset in filled:
            print(f"✅ 回填 {date} {asset}")
    else:
        print("沒有可回填的紀錄(未到期或已填齊)")
    return 0


def main():
    parser = argparse.ArgumentParser(description="DebateSystem 落地 CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("market", help="抓行情並寫入 DB")
    p.add_argument("--asset", default="BTC/USDT")
    p.add_argument("--as-of", dest="as_of", default=None,
                   help="回測模式:YYYY-MM-DD(快照=該日開盤價近似);省略=實盤模式")
    p.set_defaults(fn=cmd_market)

    p = sub.add_parser("record", help="落地人格判斷(JSON 檔)")
    p.add_argument("--json", required=True)
    p.set_defaults(fn=cmd_record)

    p = sub.add_parser("finalize", help="聚合並寫入當日最終 bias")
    p.add_argument("--date", required=True)
    p.add_argument("--asset", default="BTC/USDT")
    p.add_argument("--summary-file", default=None)
    p.set_defaults(fn=cmd_finalize)

    p = sub.add_parser("outcomes", help="回填事後價格")
    p.set_defaults(fn=cmd_outcomes)

    args = parser.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
