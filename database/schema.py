from sqlalchemy import Column, Integer, String, Float, Text, UniqueConstraint, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MarketData(Base):
    __tablename__ = 'market_data'
    __table_args__ = (UniqueConstraint('date', 'asset', name='uq_market_date_asset'),)
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False) # e.g. YYYY-MM-DD
    asset = Column(String, nullable=False) # e.g. BTC/USDT
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    volume = Column(Float)
    # 專門為幣圈量身打造的數據
    funding_rate = Column(Float, nullable=True) # 資金費率
    open_interest = Column(Float, nullable=True) # 未平倉量
    context_summary = Column(Text, nullable=True) # 將餵給 LLM 的文字版行情摘要(core變體:ICT專屬,無成交量/RSI)
    context_summary_emperorbtc = Column(Text, nullable=True) # emperorbtc變體專屬:含成交量CSV欄位+RSI+量能比值(資訊分流,見preregistration §8)
    context_summary_tjr = Column(Text, nullable=True) # tjr變體專屬:core內容+相關資產(BTC/ETH)參考行情(v5,見preregistration §8)
    # 快照捕捉時間(ISO UTC):實盤模式=實際抓取當下的 wall-clock 時間;
    # 回測模式=as-of 日期的參考基準時點(該日 00:00 UTC,非程式實際執行時間)
    snapshot_captured_at = Column(String, nullable=True)

class PersonaDebate(Base):
    __tablename__ = 'persona_debates'
    __table_args__ = (UniqueConstraint('date', 'asset', 'persona_name', 'round', name='uq_debate_key'),)
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    asset = Column(String, nullable=False)
    persona_name = Column(String, nullable=False) # e.g. ict, tjr, gcr
    round = Column(Integer, nullable=False) # 1=獨立盲判, 2=結構化反駁後更新(協議固定兩輪)
    direction = Column(String, nullable=False) # Bullish, Bearish, Neutral
    confidence = Column(Integer) # 0-100 信心指數
    reasoning = Column(Text, nullable=False) # 判斷理由/對話內容
    falsifier = Column(Text, nullable=True) # R2 必填:什麼證據出現會讓自己改判
    intraday_scenario = Column(Text, nullable=True) # R1/R2 必填:今日收盤前的雙劇本 if-then(不得為多日/週目標)
    model_id = Column(String, nullable=True) # 跑此人格的底層模型(模型=預測者身分,必記)
    created_at = Column(String, nullable=True) # ISO timestamp,落地即寫、事後不改

class DailyBiasResult(Base):
    __tablename__ = 'daily_bias_results'
    __table_args__ = (UniqueConstraint('date', 'asset', name='uq_bias_date_asset'),)
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    asset = Column(String, nullable=False)
    # 旁路:R1 直接機械聚合(無辯論基準,供 Phase 4 消融比較)
    r1_direction = Column(String, nullable=False)
    r1_confidence = Column(Integer)
    # 最終:末輪機械聚合(單人格時 = R1)
    consensus_direction = Column(String, nullable=False)
    confidence_score = Column(Integer)
    # 分歧度(Phase 4 §2.3 的訊號,聚合時保留、不抹平)
    n_personas = Column(Integer, nullable=False)
    disagreement_ratio = Column(Float) # 1 - 眾數方向占比;單人格=0
    confidence_std = Column(Float) # 各人格 confidence 母體標準差
    protocol_version = Column(String, nullable=True) # 辯論協議版本
    summary_reasoning = Column(Text) # 敘述性總結(不得推翻機械聚合方向)
    # 事後結果欄位(Phase4 §4):只存原始事實;命中與否由分析層依預登記的命中定義計算
    price_at_bias = Column(Float) # 判斷當下收盤價
    snapshot_captured_at = Column(String, nullable=True) # 承接自 market_data,供執行時間紀律稽核(preregistration §8)
    price_after_1d = Column(Float, nullable=True)
    price_after_5d = Column(Float, nullable=True)
    price_after_20d = Column(Float, nullable=True)
    outcomes_filled_at = Column(String, nullable=True) # 最近一次回填時間

class BacktestRun(Base):
    __tablename__ = 'backtest_runs'
    id = Column(Integer, primary_key=True)
    run_at = Column(String, nullable=False) # ISO timestamp
    period_start = Column(String, nullable=False)
    period_end = Column(String, nullable=False)
    horizon = Column(String, nullable=False) # 1d / 5d / 20d
    n_samples = Column(Integer, nullable=False)
    metrics_json = Column(Text) # 命中率+CI、Brier、校準分桶、MCPT p-value 等
    notes = Column(Text, nullable=True)

def init_db(db_path='sqlite:///database/debate_system.db'):
    engine = create_engine(db_path)
    Base.metadata.create_all(engine)
    print(f"✅ SQLite Database successfully initialized at {db_path}")

if __name__ == "__main__":
    init_db()
