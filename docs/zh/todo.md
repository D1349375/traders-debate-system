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
- [x] 每日累積已啟動:首筆 2026-07-19 落地(BTC+ETH 各一筆,ICT R1)。之後每天對 Claude Code 說「跑今日 bias」
- [x] schema 補 `snapshot_captured_at`(2026-07-20):`market_data`/`daily_bias_results` 新增欄位,回測模式=as-of 日 00:00 UTC 參考點、實盤模式=真實抓取時間;既有 3 筆真實紀錄已用 ALTER TABLE 遷移(舊資料該欄位為 NULL,誠實反映當時未記錄);36 pytest 全過。搭配 preregistration §8「每日執行時間紀律(UTC 00:00-01:00)」
- [ ] n≥30 前實作 `bias_report_metrics.py`：方向命中率 + Brier Score/校準曲線 + MCPT + Neutral 門檻敏感度附錄,強制表+圖,附 pytest（Phase4規劃 2.1/§7.4、preregistration §5）。**必須包含逐人格命中率對比**(ICT/TJR/EmperorBTC 各自單獨命中率 vs 辯論後聚合命中率,Phase4規劃 §2.2 ensemble lift)——`persona_debates` 已逐人格逐輪記錄,不需新增資料收集;**但比較 3 人格+1 聚合=4 路比較,判定「誰更準」前必須套用 BH-FDR 校正(Phase4規劃 §7.5),不可挑單獨表現最好的人格就下結論**

- [x] 三人格正式生效(2026-07-20,preregistration §8 增補已寫入,ICT+TJR+EmperorBTC)
- [x] 執行時間紀律定案:UTC 00:00-01:00(台灣 08:00-09:00),窗口錯過當日盡快補跑不跳過,真死線是隔日 UTC 00:00;`snapshot_captured_at` 欄位已補(schema+db.py+ingestion.py,37 pytest 全過)
- [x] 新增必填欄位 `intraday_scenario`(2026-07-20):R1/R2 皆強制填今日收盤前雙劇本 if-then,範圍限定當天,修正 dry-run 觀察到的地平線錯配問題;schema/db.py/main.py/trader-debate SKILL.md(兩份鏡像)已同步,37 pytest 全過,preregistration §8 已記錄
- [x] 摘要 v3(2026-07-20):新增 1H(48)/15M(96)/5M(48,4小時)三個日內時間框架,配合 `intraday_scenario` 提供顆粒度支撐;K線 184→370 根,摘要 12.2KB→24.2KB,實測回測模式 6 個時間框架皆嚴格 walk-forward;`protocol_version` 升 v3-2026-07-20;preregistration §8 已記錄。維持 Binance/ccxt 開源資料庫架構
- [x] **首次三人格正式樣本落地(2026-07-20)**:BTC(Bearish 76,分歧33%)、ETH(Bearish 100,分歧0%),v3 摘要+intraday_scenario+資料使用邊界規範首次正式應用;日報見 `data/reports/2026-07-20.md`

- [ ] **考慮接入 DXY 資料,供 EmperorBTC 使用**:確認其 SKILL.md Step 2 第4維度明確以「DXY 方向(走弱利多風險資產)」判斷 BTC/ETH(風險資產)方向,屬其框架真實依賴的宏觀輸入
- [x] ICT/TJR SKILL.md 新增「資料使用邊界」規範(2026-07-20):禁止引用成交量作判斷依據,追查 dry-run 發現的「帶量」「量縮」語句屬敘事層無傷大雅描述;preregistration §8 已記錄
- [x] **摘要 v4:真正的資訊分流(2026-07-21)**:市場摘要拆成 `core`(ICT/TJR共用)/`emperorbtc`(專屬)兩變體,取代先前「看得到但不准用」的作法;`main.py market` 新增 `--variant`,`database/schema.py` 新增 `context_summary_emperorbtc`
- [x] **DB schema 自動遷移(2026-07-21)**:`database/db.py` 的 `get_session()` 新增 `_sync_schema()`,每次呼叫自動比對既有 DB 欄位與 schema.py 宣告差異,缺什麼自動 `ALTER TABLE ADD COLUMN` 補齊;54 pytest 全過
- [x] **摘要 v5:總經行事曆旗標 + TJR專屬相關資產參考行情 + ICT信心天花板修正(2026-07-22)**:
  - 三變體皆新增「總經行事曆旗標」區塊(NFP週規則計算、2026年FOMC決策週查證自 federalreserve.gov)
  - 新增 `tjr` 變體:core內容 + 相關資產(BTC↔ETH)日/4H/1H/15M參考行情
  - ICT SKILL.md 修正信心分級表:季節性判斷改依總經行事曆旗標評估
- [x] **事後結果地平線計算修正 off-by-one(2026-07-22)**:`fill_outcomes()` 的 1d/5d/20d 目標日期算錯一天已修正,查證業界方法論確認 direction accuracy 類指標標準做法為 close-to-close
- [x] **daily報告新增「ICT/TJR Range與折溢價判讀」表(2026-07-22)**:`templates/report_reference.md`/`.html` 兩份版型新增此表供使用者主觀複核
- [x] **摘要 v6:R1/R2 新增必填欄位 `trade_plan`(2026-07-23)**:新增 `trade_plan` 必填欄位(R1/R2 皆須提供,允許「現在不下單」為合法答案,避免製造假交易訊號);`database/schema.py`/`db.py`/`main.py`/prompt 模板/orchestrator SKILL.md/報告版型同步更新,`protocol_version` 升 `v6-2026-07-23`
- [ ] **2026年底前手動更新 `_FOMC_MEETINGS_2026`(2026-07-23 確認)**:`data/ingestion.py` 的 FOMC 判斷手動更新 2027 年會議日期

## 未來開源研發方向 (Open Source Roadmap)
- [ ] 將「多 Agent 辯論」流程封裝為標準化 Claude Skill / Agent Protocol (如 `/debate-consensus`)
- [ ] 開發開源社群 Web 儀表板 (`DebateSystem-Web`)：供開源使用者視覺化檢視 Brier Score 校準圖表與歷史辯論紀錄
- [ ] 消息面 Subagent 評估：研究如何引入即時消息面數據作為獨立 Agent 的輸入維度
- [ ] 發表開源 Benchmark 數據集：累積 $\ge 100$ 筆辯論紀錄後，將數據集開源於 HuggingFace 供 AI 評測社群研究使用

## 待整合的既有資源
- [x] `skills/quant skill/quant-strategy-dev` 已比對評估，結論見 `DebateSystem/Phase4_回測系統_規劃.md`
