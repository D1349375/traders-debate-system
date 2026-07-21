"""行情抓取與摘要生成。

v2(2026-07-19,設計見 市場摘要v2_資訊集設計.md):
- 多時間框架已收盤 K 線(週52/日90/4h42)+ 資金費率 + 當下快照
- 中性資訊集:只給原始 OHLCV,不預算任何結構(FVG/壓力位/指標)
- as_of 參數:實盤傳 None(=now),回測傳歷史日期 → 實盤與回測輸入格式位元級一致
- 嚴格 walk-forward:K 線表只含 as-of 時點前已收盤者;未收盤資訊只進「當下快照」段

v3(2026-07-20,對齊 intraday_scenario 必填欄位):新增 1H(48根≈2天)/15M(96根≈1天)/
5M(48根≈4小時)三個日內時間框架,修正原本只有週/日/4H 時人格傾向給出中週期波段判斷、
缺乏日內顆粒度支撐「今日收盤前雙劇本」要求的問題。5M 刻意限縮在 4 小時(非整天),
避免與 15M 的一天覆蓋範圍大量重疊、徒增成本卻無新資訊。

v4(2026-07-21,真正的資訊分流,見 preregistration.md §8):摘要拆成兩個變體,不再是單一共用文字:
- variant="core"(ICT/TJR共用):K線CSV**不含成交量欄位**,無RSI/量能區塊——兩人SKILL.md本就明文禁止
  引用成交量與RSI,這次直接讓資料層面就不存在,而非「看得到但不准用」。
- variant="emperorbtc"(專屬):K線CSV含成交量欄位,額外附「量能與動能指標」區塊(RSI(14)、近7日均量、
  當前量/均量比值)——皆為程式碼算出的客觀公式值(非LLM生成文字),且刻意不做POC/value area:
  後者需要決定分箱粒度/lookback window等方法論參數,等於替他做了一次框架詮釋選擇,牴觸「詮釋權下放」
  原則;RSI/均量比值是無方法論爭議的單一公式,不受此限。swing high/low 未加入計算層——實測抽查(對照
  2026-07-20 凍結行情原始K線與當日報告引用價位)未發現任何計算誤差,沒有實證問題不需要預先修。
"""
import ccxt
import datetime

TIMEFRAMES_V2 = (("1w", 52), ("1d", 90), ("4h", 42), ("1h", 48), ("15m", 96), ("5m", 48))
_TF_MS = {"1w": 7 * 86400 * 1000, "1d": 86400 * 1000, "4h": 4 * 3600 * 1000,
          "1h": 3600 * 1000, "15m": 15 * 60 * 1000, "5m": 5 * 60 * 1000}
_TF_LABEL = {"1w": "週線", "1d": "日線", "4h": "4小時線", "1h": "1小時線", "15m": "15分鐘線", "5m": "5分鐘線"}


# ---------- 純函數(可測試,不碰網路) ----------

def select_closed(rows, tf_ms, as_of_ms, count):
    """從 ohlcv rows 取出 as_of 時點前已完整收盤的最後 count 根。

    K 線 [ts, o, h, l, c, v] 的收盤時刻 = ts + tf_ms;收盤時刻 <= as_of 才算已收。
    """
    closed = [r for r in rows if r[0] + tf_ms <= as_of_ms]
    return closed[-count:]


def format_candles(rows, include_volume=True):
    """OHLCV → CSV 文字表格。include_volume=False 時連欄位都不出現(不是留空),
    供 core 變體(ICT/TJR)使用——避免明文禁用成交量的人格「看得到但被要求不用」。"""
    header = "date,open,high,low,close,volume" if include_volume else "date,open,high,low,close"
    lines = [header]
    for ts, o, h, l, c, v in rows:
        d = datetime.datetime.fromtimestamp(ts / 1000, tz=datetime.timezone.utc)
        row = f"{d.strftime('%Y-%m-%d %H:%M')},{o},{h},{l},{c}"
        if include_volume:
            row += f",{v}"
        lines.append(row)
    return "\n".join(lines)


def compute_rsi(closes, period=14):
    """Wilder's RSI(業界標準公式,單一定義無方法論爭議)。

    closes 需至少 period+1 筆(依時間升冪排列);不足回 None,誠實揭露而非硬湊。
    """
    if len(closes) < period + 1:
        return None
    gains, losses = [], []
    for i in range(1, len(closes)):
        change = closes[i] - closes[i - 1]
        gains.append(max(change, 0.0))
        losses.append(max(-change, 0.0))
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 2)


def compute_volume_ratio(volumes, window=7):
    """近 window 筆均量(不含當前這筆,避免自己除自己)、當前量、比值。

    volumes 依時間升冪排列,最後一筆為當前。不足 window+1 筆回 (None, None, None)。
    """
    if len(volumes) < window + 1:
        return None, None, None
    current = volumes[-1]
    baseline = volumes[-(window + 1):-1]
    avg = sum(baseline) / window
    ratio = round(current / avg, 3) if avg else None
    return round(avg, 2), round(current, 2), ratio


def compose_summary_v2(asset, judgment_date, sections, funding_now, funding_avg7, snapshot, variant="core"):
    """組裝 v2/v3 摘要全文,依 variant 決定資訊分流內容(v4,見模組docstring)。

    sections: list of (timeframe, rows);snapshot: dict(price, change_24h, high, low, note)
    variant="core"(預設,ICT/TJR共用):不含成交量、無量能/RSI區塊。
    variant="emperorbtc":含成交量CSV欄位 + 額外「量能與動能指標」區塊。
    """
    include_volume = (variant == "emperorbtc")
    vol_note = "date,open,high,low,close,volume" if include_volume else "date,open,high,low,close"
    parts = [
        f"【{asset} 市場多時間框架摘要 | 判斷日: {judgment_date}】",
        f"以下 K 線均為判斷時點前已完整收盤的數據(UTC)。CSV 欄位:{vol_note}",
        "",
    ]
    for tf, rows in sections:
        parts.append(f"=== {_TF_LABEL[tf]}(最近 {len(rows)} 根已收盤)===")
        parts.append(format_candles(rows, include_volume=include_volume))
        parts.append("")
    parts.append("=== 永續合約資金費率 ===")
    if funding_now is None:
        parts.append("無法取得(本次省略,不影響其他數據)")
    else:
        avg_txt = f",近 7 日均值 {funding_avg7:.6f}" if funding_avg7 is not None else ""
        parts.append(f"當期 {funding_now:.6f}{avg_txt}(正=多方付費)")
    parts.append("")
    if variant == "emperorbtc":
        daily_rows = next((rows for tf, rows in sections if tf == "1d"), [])
        closes = [r[4] for r in daily_rows]
        volumes = [r[5] for r in daily_rows]
        rsi = compute_rsi(closes, period=14)
        avg_vol, cur_vol, vol_ratio = compute_volume_ratio(volumes, window=7)
        parts.append("=== 量能與動能指標(程式碼計算,非LLM生成文字;僅本變體提供) ===")
        parts.append(f"日線 RSI(14): {rsi if rsi is not None else '資料不足,無法計算'}")
        if avg_vol is not None:
            trend = "高於均量" if vol_ratio > 1 else ("低於均量" if vol_ratio < 1 else "與均量持平")
            parts.append(f"日線近 7 日均量: {avg_vol},當前日量: {cur_vol},比值: {vol_ratio}({trend})")
        else:
            parts.append("日線量能比值: 資料不足,無法計算")
        parts.append("")
    parts.append("=== 當下快照 ===")
    parts.append(f"價格: {snapshot['price']}")
    if snapshot.get("change_24h") is not None:
        parts.append(f"24H 變化: {snapshot['change_24h']}%")
    if snapshot.get("high") is not None:
        parts.append(f"今日盤中高/低(未收盤): {snapshot['high']} / {snapshot['low']}")
    if snapshot.get("note"):
        parts.append(f"備註: {snapshot['note']}")
    parts.append("")
    parts.append("(請根據以上數據與您的交易人格,給出該判斷日的 Daily Bias [Bullish/Bearish/Neutral] 與判斷理由。)")
    return "\n".join(parts)


# ---------- 抓取層 ----------

def _fetch_tf(exchange, symbol, timeframe, count, as_of_ms):
    tf_ms = _TF_MS[timeframe]
    since = as_of_ms - (count + 3) * tf_ms
    rows = exchange.fetch_ohlcv(symbol, timeframe, since=since, limit=count + 3)
    return select_closed(rows, tf_ms, as_of_ms, count)


def _fetch_funding(symbol, as_of_ms, live):
    """回傳 (當期費率, 近7日均值);任何失敗回 (None, None),摘要誠實標示。"""
    try:
        fut = ccxt.binanceusdm({"enableRateLimit": True})
        swap = symbol  # binanceusdm 直接用 BTC/USDT
        since = as_of_ms - 7 * 86400 * 1000
        hist = fut.fetch_funding_rate_history(swap, since=since, limit=100)
        rates = [h["fundingRate"] for h in hist
                 if h.get("fundingRate") is not None and h["timestamp"] <= as_of_ms]
        avg7 = sum(rates) / len(rates) if rates else None
        if live:
            cur = fut.fetch_funding_rate(swap).get("fundingRate")
            if cur is None and rates:
                cur = rates[-1]
        else:
            cur = rates[-1] if rates else None
        return cur, avg7
    except Exception as e:
        print(f"資金費率取得失敗(省略): {e}")
        return None, None


def build_market_context(symbol="BTC/USDT", as_of=None, variant="core"):
    """產生 v2/v3 摘要與 DB 落地資料。

    as_of=None → 實盤模式(判斷日=今日 UTC,快照=即時價)
    as_of="YYYY-MM-DD" → 回測模式(快照=該日開盤價近似,見設計文件 §3)
    variant="core"|"emperorbtc" → 資訊分流(v4,見模組docstring),決定文字摘要內容;
    不影響落地的 OHLC 事實(data_dict 兩變體皆相同,只是各自獨立抓取的即時讀數)。
    回傳 (data_dict, summary_text);失敗回 (None, None)。
    """
    exchange = ccxt.binance({"enableRateLimit": True})
    live = as_of is None
    try:
        if live:
            now = datetime.datetime.now(datetime.timezone.utc)
            judgment_date = now.strftime("%Y-%m-%d")
            as_of_ms = int(now.timestamp() * 1000)
        else:
            judgment_date = as_of
            as_of_ms = int(datetime.datetime.fromisoformat(as_of).replace(
                tzinfo=datetime.timezone.utc).timestamp() * 1000)  # 該日 00:00 UTC

        sections = [(tf, _fetch_tf(exchange, symbol, tf, count, as_of_ms))
                    for tf, count in TIMEFRAMES_V2]
        if not sections[1][1]:
            raise ValueError("日線資料為空")

        funding_now, funding_avg7 = _fetch_funding(symbol, as_of_ms, live)
        # 快照捕捉時間:實盤=抓取當下的真實 wall-clock;回測=as-of 參考基準點(該日 00:00 UTC)。
        # 兩者用同一個 as_of_ms 換算,語意天然正確,不必分支處理。
        snapshot_captured_at = datetime.datetime.fromtimestamp(
            as_of_ms / 1000, tz=datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        if live:
            ticker = exchange.fetch_ticker(symbol)
            today = exchange.fetch_ohlcv(symbol, "1d", limit=1)[-1]
            snapshot = {"price": ticker["last"], "change_24h": ticker.get("percentage"),
                        "high": today[2], "low": today[3], "note": None}
            data = {"date": judgment_date, "asset": symbol,
                    "open": today[1], "high": today[2], "low": today[3],
                    "close": ticker["last"], "volume": today[5],
                    "funding_rate": funding_now, "snapshot_captured_at": snapshot_captured_at}
        else:
            day = exchange.fetch_ohlcv(symbol, "1d", since=as_of_ms, limit=1)[0]
            day_date = datetime.datetime.fromtimestamp(
                day[0] / 1000, tz=datetime.timezone.utc).strftime("%Y-%m-%d")
            if day_date != as_of:
                raise ValueError(f"找不到 {as_of} 的日 K(取得 {day_date})")
            snapshot = {"price": day[1], "change_24h": None, "high": None, "low": None,
                        "note": "回測模式:以該日開盤價為判斷時點近似,無盤中資訊"}
            data = {"date": judgment_date, "asset": symbol,
                    "open": day[1], "high": None, "low": None,
                    "close": day[1], "volume": None,
                    "funding_rate": funding_now, "snapshot_captured_at": snapshot_captured_at}

        summary = compose_summary_v2(symbol, judgment_date, sections,
                                     funding_now, funding_avg7, snapshot, variant=variant)
        return data, summary
    except Exception as e:
        print(f"抓取 {symbol} 行情失敗: {e}")
        return None, None


def fetch_close_on(symbol, date_str):
    """抓指定日期(UTC)的日線收盤價,供事後結果回填用。找不到該日K線回傳 None。"""
    exchange = ccxt.binance({"enableRateLimit": True})
    since = int(datetime.datetime.fromisoformat(date_str).replace(
        tzinfo=datetime.timezone.utc).timestamp() * 1000)
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, "1d", since=since, limit=1)
        if not ohlcv:
            return None
        ts, _o, _h, _l, close, _v = ohlcv[0]
        candle_date = datetime.datetime.fromtimestamp(
            ts / 1000, tz=datetime.timezone.utc).strftime("%Y-%m-%d")
        if candle_date != date_str:
            return None
        return close
    except Exception as e:
        print(f"抓取 {symbol} {date_str} 收盤價失敗: {e}")
        return None


if __name__ == "__main__":
    data, summary = build_market_context("BTC/USDT")
    if data:
        print(summary[:2000])
