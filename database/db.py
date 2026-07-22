"""DB 落地層:所有寫入走這裡。

紀律(對齊 preregistration / 測試帳本精神):
- 判斷落地即定案:record_opinion / finalize 遇到既有紀錄一律報錯,不提供覆寫歷史的介面。
- 事後結果(fill_outcomes)只回填空欄位,不觸碰已填值。
"""
import datetime
import os

from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker

from database.schema import Base, MarketData, PersonaDebate, DailyBiasResult
from engine.aggregate import aggregate, disagreement, VALID_DIRECTIONS

_DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'debate_system.db')


def _sync_schema(engine):
    """為已存在的 DB 檔案自動補上 schema.py 之後新增的欄位(ALTER TABLE ADD COLUMN)。

    create_all() 只會建「不存在的表」,對既有表不會補新增欄位——這是 SQLAlchemy/SQLite 的既定限制,
    不是 bug。本專案至今已手動撞到三次(snapshot_captured_at/intraday_scenario/
    context_summary_emperorbtc),故改自動化,避免第四次。只新增缺的欄位,不改型別、不刪欄位、
    不搬移資料;新欄位一律 NULL,如實反映「舊紀錄當時沒有這項資訊」,與既有的手動遷移精神一致。
    """
    inspector = inspect(engine)
    existing_tables = set(inspector.get_table_names())
    with engine.begin() as conn:
        for table in Base.metadata.sorted_tables:
            if table.name not in existing_tables:
                continue  # 全新的表,create_all() 已經建出完整欄位,不需要補
            existing_cols = {c['name'] for c in inspector.get_columns(table.name)}
            for col in table.columns:
                if col.name in existing_cols:
                    continue
                col_type = col.type.compile(dialect=engine.dialect)
                conn.execute(text(f'ALTER TABLE {table.name} ADD COLUMN {col.name} {col_type}'))
                print(f"[自動遷移] {table.name} 新增欄位 {col.name} ({col_type})")


def get_session(db_url=None):
    engine = create_engine(db_url or f"sqlite:///{_DB_FILE}")
    Base.metadata.create_all(engine)
    _sync_schema(engine)
    return sessionmaker(bind=engine)()


def _now_iso():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


_VARIANT_COLUMNS = {
    "core": "context_summary",
    "emperorbtc": "context_summary_emperorbtc",
    "tjr": "context_summary_tjr",
}


def upsert_market(session, data, summary, variant="core"):
    """行情快照可重抓更新(它不是判斷,不受落地不改約束)。

    variant="core"(ICT專屬)寫入 context_summary;variant="emperorbtc" 寫入 context_summary_emperorbtc;
    variant="tjr" 寫入 context_summary_tjr。三變體分開存欄,同一 (date, asset) 多次呼叫(各一變體)
    不會互相覆蓋對方的文字內容。OHLC/資金費率等數值欄位仍為同一行情事實,每次呼叫皆會更新
    (後呼叫者的讀數為準,差異僅為多次即時抓取間的數秒級價格漂移,遠小於 Neutral 門檻,不需額外處理)。
    """
    row = session.query(MarketData).filter_by(date=data['date'], asset=data['asset']).one_or_none()
    if row is None:
        row = MarketData(date=data['date'], asset=data['asset'])
        session.add(row)
    row.open_price = data.get('open')
    row.high_price = data.get('high')
    row.low_price = data.get('low')
    row.close_price = data.get('close')
    row.volume = data.get('volume')
    row.funding_rate = data.get('funding_rate')
    row.open_interest = data.get('open_interest')
    setattr(row, _VARIANT_COLUMNS.get(variant, "context_summary"), summary)
    row.snapshot_captured_at = data.get('snapshot_captured_at')
    session.commit()
    return row


def record_opinion(session, *, date, asset, persona, round_, direction, confidence,
                   reasoning, intraday_scenario, trade_plan, falsifier=None, model_id=None):
    if direction not in VALID_DIRECTIONS:
        raise ValueError(f"非法方向: {direction}")
    confidence = int(confidence)
    if not (0 <= confidence <= 100):
        raise ValueError(f"confidence 超出 0-100: {confidence}")
    if round_ not in (1, 2):
        raise ValueError("round 只能是 1 或 2(協議固定兩輪)")
    if not intraday_scenario or not intraday_scenario.strip():
        raise ValueError("intraday_scenario 為必填(R1/R2 皆須提供今日收盤前的雙劇本 if-then)")
    if not trade_plan or not trade_plan.strip():
        raise ValueError("trade_plan 為必填(R1/R2 皆須提供若本人真的要下單的具體計畫,或明講不下單及原因)")
    exists = session.query(PersonaDebate).filter_by(
        date=date, asset=asset, persona_name=persona, round=round_).one_or_none()
    if exists is not None:
        raise ValueError(f"{date} {asset} {persona} R{round_} 已落地,不可覆寫")
    row = PersonaDebate(date=date, asset=asset, persona_name=persona, round=round_,
                        direction=direction, confidence=confidence, reasoning=reasoning,
                        intraday_scenario=intraday_scenario, trade_plan=trade_plan,
                        falsifier=falsifier, model_id=model_id, created_at=_now_iso())
    session.add(row)
    session.commit()
    return row


def finalize(session, *, date, asset, protocol_version, summary_reasoning=None):
    """R1 旁路聚合 + 末輪最終聚合 + 分歧度,寫入 daily_bias_results。"""
    if session.query(DailyBiasResult).filter_by(date=date, asset=asset).one_or_none():
        raise ValueError(f"{date} {asset} 已 finalize,不可覆寫")
    rows = session.query(PersonaDebate).filter_by(date=date, asset=asset).all()
    r1 = [r for r in rows if r.round == 1]
    r2 = [r for r in rows if r.round == 2]
    if not r1:
        raise ValueError(f"{date} {asset} 沒有任何 R1 紀錄")

    def ops(rs):
        return [{"direction": r.direction, "confidence": r.confidence} for r in rs]

    r1_dir, r1_conf = aggregate(ops(r1))
    final_rows = r2 if r2 else r1  # 單人格或未跑 R2 → 最終 = R1
    cons_dir, cons_conf = aggregate(ops(final_rows))
    ratio, std = disagreement(ops(final_rows))

    market = session.query(MarketData).filter_by(date=date, asset=asset).one_or_none()
    result = DailyBiasResult(
        date=date, asset=asset,
        r1_direction=r1_dir, r1_confidence=r1_conf,
        consensus_direction=cons_dir, confidence_score=cons_conf,
        n_personas=len({r.persona_name for r in final_rows}),
        disagreement_ratio=ratio, confidence_std=std,
        protocol_version=protocol_version,
        summary_reasoning=summary_reasoning,
        price_at_bias=market.close_price if market else None,
        snapshot_captured_at=market.snapshot_captured_at if market else None,
    )
    session.add(result)
    session.commit()
    return result


def fill_outcomes(session, fetch_close_fn, today=None):
    """回填事後價格。只填「該日 K 線已收」且目前為空的欄位。

    fetch_close_fn(asset, date_str) -> float | None
    地平線為日曆日(幣圈全年交易),定義見 preregistration:「判斷日 UTC 收盤 → N 日後 UTC 收盤」。
    price_at_bias 是判斷日 D 開盤附近抓的快照(執行窗口 UTC 00:00-01:00),D 自己這根日K的收盤
    (發生在 D+1 00:00 UTC)才是真正的「+1 天」參考點,故 Nd 地平線抓的是 (D + N - 1) 那根日K的收盤,
    不是 (D + N)——後者會多算一天(2026-07-22 修正,見 preregistration §8;修正前已回填的少量舊紀錄
    已用同一份修正邏輯手動重算,見 outcomes_correction_note)。
    """
    today = today or datetime.datetime.now(datetime.timezone.utc).date()
    horizons = {'price_after_1d': 1, 'price_after_5d': 5, 'price_after_20d': 20}
    filled = []
    for row in session.query(DailyBiasResult).all():
        base = datetime.date.fromisoformat(row.date)
        touched = False
        for col, days in horizons.items():
            if getattr(row, col) is not None:
                continue
            target = base + datetime.timedelta(days=days - 1)
            if target >= today:  # 該日 K 線尚未收
                continue
            price = fetch_close_fn(row.asset, target.isoformat())
            if price is not None:
                setattr(row, col, price)
                touched = True
        if touched:
            row.outcomes_filled_at = _now_iso()
            filled.append((row.date, row.asset))
    session.commit()
    return filled
