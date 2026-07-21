# 交易員辯論專案 — Todolist / 未來方向

> 專案總覽、辯論協議、進度快照見 `README.md`（2026-07-19 起為主文件，本清單與其進度區同步維護）

## 已完成
- [x] README.md 總文件（2026-07-19）：專案規劃/蒸餾過程/辯論協議定案（兩輪固定、裁判職責邊界、R1旁路聚合、R2結構化反駁+falsifier）/進度快照
- [x] 女媧skill安裝（專案層級 `.claude/skills/huashu-nuwa`）
- [x] ICT人格完整蒸餾（Phase 0.5→1→1.5→2→2.5→3→4→5全跑完），產出 `.claude/skills/ict-perspective/SKILL.md`，已用聊天+真實圖表測試驗證語氣與框架皆有效
- [x] Phase 4 回測系統規劃文件：`DebateSystem/Phase4_回測系統_規劃.md`（比對並改造 Obsidian `quant-strategy-dev` skill 方法論，尚未動工實作）
- [x] Phase 4 文件對齊 skill v13（2026-07-19，見文件第 7 節）：新增預登記命中定義、1d 主地平線、重疊視窗 block bootstrap、強制指標表 script、BH-FDR 五項

## 下一步（依 Phase4規劃文件第5節建議順序）
- [x] 修 `database/schema.py` 補事後結果欄位 + `backtest_runs` 表（2026-07-19,DB 已重建;is_correct 不入庫,由分析層依預登記命中定義計算）
- [x] C 架構實作（2026-07-19）：`main.py` CLI + `database/db.py` 落地層 + `engine/aggregate.py` 機械聚合 + trader-debate orchestrator skill;25 pytest 全過;舊 Gemini 引擎封存為 `engine/legacy_gemini_runner.py`
- [x] 語料洩漏處理方式已定（2026-07-19）：走「等新資料」路線——每日前瞻累積,不回測語料涵蓋期（已寫入 preregistration 草案 §5）
- [x] 預登記生效（2026-07-19 使用者確認）：雙標的 BTC ±0.5% / ETH ±1.0%、1d 主地平線、n≥30/60 逐標的、報告必附門檻敏感度附錄與修改建議 → `preregistration.md`
- [x] 每日累積已啟動:**首筆 2026-07-19 落地**(BTC+ETH 各一筆,ICT R1)。之後每天對 Claude Code 說「跑今日 bias」
- [x] schema 補 `snapshot_captured_at`(2026-07-20):`market_data`/`daily_bias_results` 新增欄位,回測模式=as-of 日 00:00 UTC 參考點、實盤模式=真實抓取時間;既有 3 筆真實紀錄已用 ALTER TABLE 遷移(舊資料該欄位為 NULL,誠實反映當時未記錄);36 pytest 全過。搭配 preregistration §8「每日執行時間紀律(UTC 00:00-01:00)」
- [ ] n≥30 前實作 `bias_report_metrics.py`：方向命中率 + Brier Score/校準曲線 + MCPT + Neutral 門檻敏感度附錄,強制表+圖,附 pytest（Phase4規劃 2.1/§7.4、preregistration §5）。**必須包含逐人格命中率對比**(ICT/TJR/EmperorBTC 各自單獨命中率 vs 辯論後聚合命中率,Phase4規劃 §2.2 ensemble lift)——`persona_debates` 已逐人格逐輪記錄,不需新增資料收集;**但比較 3 人格+1 聚合=4 路比較,判定「誰更準」前必須套用 BH-FDR 校正(Phase4規劃 §7.5),不可挑單獨表現最好的人格就下結論**

- [x] 三人格正式生效(2026-07-20,preregistration §8 增補已寫入,ICT+TJR+EmperorBTC)
- [x] 執行時間紀律定案:UTC 00:00-01:00(台灣 08:00-09:00),窗口錯過當日盡快補跑不跳過,真死線是隔日 UTC 00:00;`snapshot_captured_at` 欄位已補(schema+db.py+ingestion.py,37 pytest 全過)
- [x] 新增必填欄位 `intraday_scenario`(2026-07-20):R1/R2 皆強制填今日收盤前雙劇本 if-then,範圍限定當天,修正 dry-run 觀察到的地平線錯配問題;schema/db.py/main.py/trader-debate SKILL.md(兩份鏡像)已同步,37 pytest 全過,preregistration §8 已記錄
- [x] 摘要 v3(2026-07-20):新增 1H(48)/15M(96)/5M(48,4小時)三個日內時間框架,配合 `intraday_scenario` 提供顆粒度支撐;K線 184→370 根,摘要 12.2KB→24.2KB,實測回測模式 6 個時間框架皆嚴格 walk-forward;`protocol_version` 升 v3-2026-07-20;preregistration §8 已記錄。TradingView 等外部資料源評估後否決(破壞回測/實盤一致性、疊加視覺判讀雜訊、無對應公開 API),維持 Binance/ccxt 架構
- [x] **首次三人格正式樣本落地(2026-07-20)**:BTC(Bearish 76,分歧33%)、ETH(Bearish 100,分歧0%),v3 摘要+intraday_scenario+資料使用邊界規範首次正式應用;日報見 `data/reports/2026-07-20.md`

- [ ] **考慮接入 DXY 資料,供 EmperorBTC 使用**:確認其 SKILL.md Step 2 第4維度明確以「DXY 方向(走弱利多風險資產)」判斷 BTC/ETH(風險資產)方向,屬其框架真實依賴的宏觀輸入,非其他兩人格所需——符合 README §3.4 資訊不對稱設計的觸發條件。**工程量級較高**(Binance/ccxt 無 DXY,需另接外匯/指數資料源,非現有管線可直接擴充),且他 SKILL.md 已內建資料缺口的坦白機制(缺 DXY 時明講「這是我看不到的維度」並降信心)。建議待三人格正式樣本累積一段時間、觀察到此缺口實際拖累判斷品質後再啟動,不急於現在動工
- [x] ICT/TJR SKILL.md 新增「資料使用邊界」規範(2026-07-20):禁止引用成交量作判斷依據,追查 dry-run 發現的「帶量」「量縮」語句屬敘事層無傷大雅描述(R2 反駁確認實際判斷邏輯未依賴成交量),但為避免報告可讀性混淆與未來真正污染風險,明文禁止;preregistration §8 已記錄,ICT 兩份鏡像已同步
- [x] **摘要 v4:真正的資訊分流(2026-07-21)**:市場摘要拆成 `core`(ICT/TJR共用,無成交量)/`emperorbtc`(專屬,含成交量+RSI(14)+近7日量能比值,程式碼算非LLM生成)兩變體,取代先前「看得到但不准用」的作法;明確排除 POC/value area(涉及分箱/lookback方法論選擇,等於代人格做詮釋決定)與 swing high/low 預先計算(抽查 07-20 凍結資料未發現任何 LLM 計算誤差,無實證問題不預修)。`main.py market` 新增 `--variant`,`database/schema.py` 新增 `context_summary_emperorbtc`,trader-debate SKILL.md 僅動 Step 1/2/3/6(人格 SKILL.md 三份皆未改動);`protocol_version` 升 `v4-2026-07-21`;54 pytest 全過(含真實行情 smoke test 驗證兩變體輸出正確);preregistration §8 已記錄完整決策脈絡(含與上一條「架構重寫需基準期」承諾的關係說明)
- [x] **DB schema 自動遷移(2026-07-21)**:`database/db.py` 的 `get_session()` 新增 `_sync_schema()`,每次呼叫自動比對既有 DB 欄位與 schema.py 宣告差異,缺什麼自動 `ALTER TABLE ADD COLUMN` 補齊(新欄位一律 NULL)。動機:此欄位遷移手動做過三次(`snapshot_captured_at`/`intraday_scenario`/`context_summary_emperorbtc`),協作者在其他機器 pull 新 schema 後首次執行會撞到 `no such column`,自動化後不再需要手動介入或另外寫文件提醒;54 pytest 含此機制的邊界測試(模擬舊表補欄位、schema已最新時的 no-op)

## 進行中討論
- [ ] **回測支線（探索性,2026-02~07-14 半乾淨區）待與使用者討論後啟動**,懸而未決:(a) 語料稽核判定標準多嚴——提到 BTC/ETH 就剔除該日,還是要具體到價位/方向才剔除;(b) pilot 30 天怎麼選——隨機抽 vs 連續段;(c) 探索性預登記是否也走使用者簽署流程。背景見 `回測污染分析_雙層記憶.md`。**有賞味期限:模型升級到更新知識截止日即失效,要做要趁早**
- [x] **市場摘要 v2 已上線(2026-07-19)**:週52/日90/4h42 已收盤 K 線 + 資金費率 + 快照,as-of 參數支援回測模式(該日開盤價近似);protocol v2 升版,07-19 兩筆為 v1 樣本依版本過濾;34 pytest 全過。設計:`市場摘要v2_資訊集設計.md`(OI 因回測不可重現排除,資訊不對稱階段再議)

## 待評估（多人格上線後才需要）
- [x] **TJR 已完成真正蒸餾（2026-07-19）**：765 支逐字稿走完女媧全流程，產出 `.claude/skills/tjr-perspective/SKILL.md`，3 子 agent 驗證通過
- [x] **EmperorBTC 已完成真正蒸餾（2026-07-19）**：以 `data/fetch_transcripts.py` 自抓 81 支逐字稿，走完女媧流程，產出 `.claude/skills/emperorbtc-perspective/SKILL.md`，3 子 agent 驗證通過（crypto 原生＋反 ICT 操縱敘事，辯論框架分歧）
- [x] **GCR 確認無法用 YT 流程蒸餾**：Twitter/X 匿名者、已消失、YouTube 無本人頻道（需其 X 文字存檔才能走純本地語料模式）。Mark Douglas 語料薄（無官方頻道）待確認來源
- [ ] **決定哪些人格納入生效**（ICT / TJR / EmperorBTC）→ 若多人格,需先在 `preregistration.md` §8 增補登記(人格清單+各自語料截止日),之後 R2 結構化反駁自動啟用。注意:TJR/EmperorBTC 的模型記憶/語料條件與 ICT 不同,對回測支線的影響見報告補記
- [ ] Ensemble lift（個別vs綜合命中率比較）與分歧情境表現分析——多人格生效後即可做

## 未來方向（待評估，尚未決定）
- [ ] 將「交易員辯論」流程本身封裝成一個 Claude Skill（比照女媧skill的模式：`/交易員辯論` 一鍵跑今日 bias）
- [ ] 將整個專案發展成完整前後端架構產品（Web 介面 / 儀表板 / 可能對外的產品）——結論是「先驗證再包裝」，Skill化是產品化的必經之路不是繞路

## 已確認可接受的變動
- [ ] 專案架構/現有程式碼允許後續大幅修改（不受目前 DebateSystem 現有實作綁死）

## 待整合的既有資源（Obsidian vault）
- [x] `skills/quant skill/quant-strategy-dev` 已比對評估，結論見 `DebateSystem/Phase4_回測系統_規劃.md`
- [ ] 參考 `Trading/Weekly bias/`、`Trading/Trading record/` 作為使用者自身交易紀錄的對照資料
