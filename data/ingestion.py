import ccxt
import pandas as pd
import datetime

def fetch_daily_market_data(symbol='BTC/USDT', timeframe='1d'):
    """
    獲取 Binance 的每日 OHLCV 行情與基本數據
    """
    # 初始化幣安交易所 (使用現貨/U本位合約都可以，這裡示範現貨)
    exchange = ccxt.binance({
        'enableRateLimit': True,
    })
    
    # 獲取最近 2 天的日線數據 (昨天與今天)
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=2)
        
        if not ohlcv or len(ohlcv) < 2:
            raise ValueError("無法獲取足夠的 OHLCV 數據")
            
        # ohlcv 格式: [timestamp, open, high, low, close, volume]
        yesterday_data = ohlcv[0]
        today_data = ohlcv[1]
        
        # 抓取最近 24 小時的 Ticker 數據 (包含波動率等)
        ticker = exchange.fetch_ticker(symbol)
        
        data = {
            "date": datetime.datetime.fromtimestamp(today_data[0]/1000).strftime('%Y-%m-%d'),
            "asset": symbol,
            "open": today_data[1],
            "high": today_data[2],
            "low": today_data[3],
            "close": today_data[4],
            "volume": today_data[5],
            "yesterday_close": yesterday_data[4],
            "24h_change_percent": ticker.get('percentage', 0), # 24H 漲跌幅百分比
        }
        
        # U本位合約的 OI/資金費率需切換 futures API,尚未接;誠實留空而非塞字串
        data['open_interest'] = None
        data['funding_rate'] = None

        return data

    except Exception as e:
        print(f"獲取行情資料失敗: {e}")
        return None


def fetch_close_on(symbol, date_str):
    """抓指定日期(UTC)的日線收盤價,供事後結果回填用。找不到該日K線回傳 None。"""
    exchange = ccxt.binance({'enableRateLimit': True})
    since = int(datetime.datetime.fromisoformat(date_str).replace(
        tzinfo=datetime.timezone.utc).timestamp() * 1000)
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, '1d', since=since, limit=1)
        if not ohlcv:
            return None
        ts, _o, _h, _l, close, _v = ohlcv[0]
        candle_date = datetime.datetime.fromtimestamp(
            ts / 1000, tz=datetime.timezone.utc).strftime('%Y-%m-%d')
        if candle_date != date_str:
            return None
        return close
    except Exception as e:
        print(f"抓取 {symbol} {date_str} 收盤價失敗: {e}")
        return None

def generate_market_summary(data):
    """
    將數據轉換為餵給 LLM 交易員的文字摘要
    """
    if not data:
        return "無法獲取市場數據。"
        
    trend = "上漲" if data.get('24h_change_percent', 0) > 0 else "下跌"
    
    summary = f"【今日 {data['asset']} 市場摘要】\n"
    summary += f"日期: {data['date']}\n"
    summary += f"目前現貨價格: {data['close']} USDT (24H 變化: {data.get('24h_change_percent', 0)}% - {trend})\n"
    summary += f"今日最高價: {data['high']} | 最低價: {data['low']}\n"
    summary += f"昨日收盤價: {data['yesterday_close']}\n"
    summary += f"現貨 24H 成交量: {data['volume']} 顆\n"
    
    summary += "\n(這是一份由系統生成的每日行情快照。請根據以上數據與您的交易人格，給出今天的 Daily Bias [Bullish/Bearish/Neutral] 與判斷理由。)"
    
    return summary

if __name__ == "__main__":
    print("正在測試抓取 Binance 行情數據...")
    market_data = fetch_daily_market_data()
    if market_data:
        summary = generate_market_summary(market_data)
        print("\n=== 行情摘要 (將發送給各個人格) ===")
        print(summary)
        print("==================================")
