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
- [x] **摘要 v5:總經行事曆旗標 + TJR專屬相關資產參考行情 + ICT信心天花板修正(2026-07-22)**:
  - 三變體皆新增「總經行事曆旗標」區塊(NFP週規則計算、2026年FOMC決策週查證自 federalreserve.gov、8月旗標),程式碼純日期規則,誠實揭露不涵蓋CPI/假期行事曆
  - 新增 `tjr` 變體(取代原本ICT/TJR共用的`core`):core內容 + 相關資產(BTC↔ETH)日/4H/1H/15M參考行情(不含成交量、不精算divergence結論)——動機:TJR SKILL.md Step2第4維度明文要查「BTC vs ETH有無SMT背離」,但先前架構下他從未拿到過對方標的的任何資料,三天報告他自己都在講「無ETH對照」。ICT刻意不給同等資料:他語料裡SMT只舉ES/NASDAQ,從未提過BTC/ETH,給了他也未必會用,主動提示又等於替他發明語料沒有的框架連結
  - ICT SKILL.md 修正信心分級表:COT與跨資產SMT在本系統結構性永久缺席,不再因此判定「維度4無數據」而把信心永久鎖死在45-70區間(75-95的頂格區間先前實質上永遠打不開);季節性判斷改依總經行事曆旗標評估,不受COT/SMT缺席影響
- [x] **事後結果地平線計算修正 off-by-one(2026-07-22)**:`fill_outcomes()` 的 1d/5d/20d 目標日期算錯一天(實際量測1d地平線約42-48小時非24小時),已修正程式碼(`D+N`→`D+N-1`)並回溯校正 4 筆已回填的舊紀錄(新增 `outcomes_correction_note` 欄位存校正說明),補回歸測試鎖定正確目標日期;不改變命中定義本身,詳見 preregistration §8。同批討論並明確排除「touch-based(盤中觸及門檻)命中定義」——查證業界方法論確認 direction accuracy 類指標標準做法就是 close-to-close,touch-based 屬於不同性質的 trading profitability 評估,兩者不相容,維持 close-to-close;查證結果已 ingest 進知識庫 [[quant-strategy-dev skill]] 頁
- [x] **daily報告新增「ICT/TJR Range與折溢價判讀」表(2026-07-22)**:討論 dry-run 追問挖出 TJR 一次 premium/discount range 選錯的計算錯誤,評估後判定不修 SKILL.md(唯一證據來源是帶引導性問句施壓下的對話,無法排除是提問方式造成而非常態問題;range選擇本身可能是活的框架判斷而非可機械化的規則),改採低成本監控:`templates/report_reference.md`/`.html` 兩份版型新增此表,逐日列出 ICT/TJR 自己在R2 reasoning講的dealing range/equilibrium/premium-discount判定,供使用者主觀複核是否前後一致;純報告呈現層變更,不影響命中定義或聚合邏輯,不觸發protocol_version
  - `database/schema.py` 新增 `context_summary_tjr`;`main.py --variant` 新增 `tjr` 選項;`protocol_version` 升 `v5-2026-07-22`;trader-debate SKILL.md Step1改凍結三份檔案、Step2/3三方路由
  - 63 pytest 全過(9個新增:總經行事曆旗標邊界案例、tjr變體輸出、DB三欄寫入);真實行情smoke test驗證三變體皆正確(tjr變體35.4KB,含ETH日/4H/1H/15M參考資料且不含成交量)
  - preregistration §8 已記錄完整脈絡
- [x] **摘要 v6:R1/R2 新增必填欄位 `trade_plan`(2026-07-23)**:使用者回顧近日報告後指出三人格輸出從未具體講「若本人真的要下這筆單會怎麼做」(進場觸發/停損/目標/部位大小),只有盤面解讀與今日劇本;三人格 SKILL.md 早已蒸餾出具體風控規則(ICT/TJR 1-3%、EmperorBTC 0.25-1%),缺的只是 prompt 沒要求套用。新增 `trade_plan` 必填欄位(R1/R2 皆須提供,允許「現在不下單」為合法答案,避免製造假交易訊號);`database/schema.py`/`db.py`/`main.py`/prompt 模板/orchestrator SKILL.md/報告版型同步更新,`protocol_version` 升 `v6-2026-07-23`;65 pytest 全過(1個新增);preregistration §8、市場摘要協議版本演進紀錄.md 已記錄。實際輸出品質待下次真實跑 bias 驗證。
- [ ] **2026年底前手動更新 `_FOMC_MEETINGS_2026`(2026-07-23 確認)**:`data/ingestion.py` 的 FOMC 判斷目前寫死 2026 年會議日期表,無跨年自動提醒機制——過了 2026 年,FOMC 那段迴圈不會報錯也不會標記任何一週,`coverage_note` 仍會印同一句「僅2026年,需逐年更新」靜態文字,不會變得更醒目。需在 2026 年底前手動查證 2027 FOMC 會議日期(來源:federalreserve.gov/monetarypolicy/fomccalendars.htm)並更新該表,否則 2027 年起 FOMC 決策週旗標會靜默完全失效(NFP 規則計算不受影響)

## 進行中討論
- [ ] **回測支線（探索性,2026-02~07-14 半乾淨區）待與使用者討論後啟動**,懸而未決:(a) 語料稽核判定標準多嚴——提到 BTC/ETH 就剔除該日,還是要具體到價位/方向才剔除;(b) pilot 30 天怎麼選——隨機抽 vs 連續段;(c) 探索性預登記是否也走使用者簽署流程。背景見 `回測污染分析_雙層記憶.md`。**有賞味期限:模型升級到更新知識截止日即失效,要做要趁早**
- [x] **市場摘要 v2 已上線(2026-07-19)**:週52/日90/4h42 已收盤 K 線 + 資金費率 + 快照,as-of 參數支援回測模式(該日開盤價近似);protocol v2 升版,07-19 兩筆為 v1 樣本依版本過濾;34 pytest 全過。設計:`市場摘要v2_資訊集設計.md`(OI 因回測不可重現排除,資訊不對稱階段再議)

## 待評估（多人格上線後才需要）
- [x] **TJR 已完成真正蒸餾（2026-07-19）**：765 支逐字稿走完女媧全流程，產出 `.claude/skills/tjr-perspective/SKILL.md`，3 子 agent 驗證通過
- [x] **EmperorBTC 已完成真正蒸餾（2026-07-19）**：以 `data/fetch_transcripts.py` 自抓 81 支逐字稿，走完女媧流程，產出 `.claude/skills/emperorbtc-perspective/SKILL.md`，3 子 agent 驗證通過（crypto 原生＋反 ICT 操縱敘事，辯論框架分歧）
- [x] **GCR 確認無法用 YT 流程蒸餾**：Twitter/X 匿名者、已消失、YouTube 無本人頻道（需其 X 文字存檔才能走純本地語料模式）。Mark Douglas 語料薄（無官方頻道）待確認來源
- [x] **決定哪些人格納入生效**（ICT / TJR / EmperorBTC）→ 三人格已於 2026-07-20 正式生效(見上「已完成」區第21行),`preregistration.md` §8 已增補登記,R2 結構化反駁已啟用
- [ ] Ensemble lift（個別vs綜合命中率比較）與分歧情境表現分析——多人格生效後即可做

## 未來方向（待評估，尚未決定）
- [ ] 將「交易員辯論」流程本身封裝成一個 Claude Skill（比照女媧skill的模式：`/交易員辯論` 一鍵跑今日 bias）
- [ ] 將整個專案發展成完整前後端架構產品（Web 介面 / 儀表板 / 可能對外的產品）——結論是「先驗證再包裝」，Skill化是產品化的必經之路不是繞路
- [ ] **消息面 compiler agent(2026-07-22 討論,非必須,有隱藏成本)**:討論脈絡見 preregistration §8——三人格 SKILL.md 都提到需要判斷「今天是不是重大消息日」(CPI/FOMC/NFP/Powell講話),已知行事曆部分(FOMC/NFP)已用純日期規則解決(見摘要 v5),但**真正不可預期的即時消息(突發新聞、非排定的 Fed 談話、地緣政治事件)** 目前完全沒有涵蓋,任何人格都拿不到。若要解決,需要開一個獨立的消息面 subagent(可能要用 WebSearch),整理後依資訊分流原則發給各自會用到的人格(例如 EmperorBTC 需要 DXY,這點也跟上面「待接入 DXY」的 TODO 項目相關)。**標記為非必須,原因**:(1) 隱藏成本高——WebSearch 的查詢延遲、token 成本、查到內容的可靠性/來源驗證、要不要在 dry-run 先測過再上線,是一整套新的架構決定,不是小補丁;(2) 已知行事曆(FOMC/NFP)已經解掉多數已被 SKILL.md 明確提及的用例,真正的增量價值只剩「突發消息」這一小塊,價值/成本比不明朗;(3) 沒有證據顯示現有樣本因為缺這塊而判斷失準——目前優先要務仍是 `bias_report_metrics.py` 跟累積樣本,不要在還沒量出問題規模前就動這個更大的工。若未來想啟動,建議先用分歧度診斷腳本類似的手法,看有沒有實際證據支持,而非直接動工。
- [ ] **交易訊號延伸(2026-07-22 討論,明確定位為專題延伸,非本專題範圍)**:使用者觀察到三份人格 SKILL.md 的決策啟發式本來就含具體風控邏輯(ICT/TJR 單筆風險1-3%、EmperorBTC 部位0.25-1%,皆蒸餾自語料非捏造),認為人格已具備「基礎交易能力」,討論能否延伸成真正的交易訊號產品。**結論:技術上可行,但要當成獨立子專題,不是 DebateSystem 本體的功能擴充**,呼應 README 已有的定位紅線(「confidence 轉部位建議=跨入自動交易訊號,需使用者明確決定」)。
  - **真正困難的地方**:不是信心加權聚合(現有機械聚合已解決,純量好平均),是**三人格對同一方向給出的進場價/停損價/目標價通常不同**(各自框架算出的關鍵位不會剛好重合)——這是全新的、比方向聚合難的設計問題,現有機制沒有對應的聚合規則。
  - **建議先後順序**:參照使用者自己 `xs-momentum-bot` 專案的先例——那個機器人是等策略先過 PBO/WF/保留區驗證、**確認有真實 edge 之後**才建執行層,不是驗證前就做。DebateSystem 目前 `bias_report_metrics.py` 未實作、n=0,**此延伸應等 Phase4 產出正的命中率/Brier score 驗證之後才啟動**,現階段不展開細部設計,優先要務仍是樣本累積與 `bias_report_metrics.py`。

## 已確認可接受的變動
- [ ] 專案架構/現有程式碼允許後續大幅修改（不受目前 DebateSystem 現有實作綁死）

## 待整合的既有資源（Obsidian vault）
- [x] `skills/quant skill/quant-strategy-dev` 已比對評估，結論見 `DebateSystem/Phase4_回測系統_規劃.md`
- [ ] 參考 `Trading/Weekly bias/`、`Trading/Trading record/` 作為使用者自身交易紀錄的對照資料
