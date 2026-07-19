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
- [ ] n≥30 前實作 `bias_report_metrics.py`：方向命中率 + Brier Score/校準曲線 + MCPT + Neutral 門檻敏感度附錄,強制表+圖,附 pytest（Phase4規劃 2.1/§7.4、preregistration §5）

## 進行中討論
- [ ] **回測支線（探索性,2026-02~07-14 半乾淨區）待與使用者討論後啟動**,懸而未決:(a) 語料稽核判定標準多嚴——提到 BTC/ETH 就剔除該日,還是要具體到價位/方向才剔除;(b) pilot 30 天怎麼選——隨機抽 vs 連續段;(c) 探索性預登記是否也走使用者簽署流程。背景見 `回測污染分析_雙層記憶.md`。**有賞味期限:模型升級到更新知識截止日即失效,要做要趁早**
- [x] **市場摘要 v2 已上線(2026-07-19)**:週52/日90/4h42 已收盤 K 線 + 資金費率 + 快照,as-of 參數支援回測模式(該日開盤價近似);protocol v2 升版,07-19 兩筆為 v1 樣本依版本過濾;34 pytest 全過。設計:`市場摘要v2_資訊集設計.md`(OI 因回測不可重現排除,資訊不對稱階段再議)

## 待評估（多人格上線後才需要）
- [ ] TJR、Mark Douglas、EmperorBTC、GCR 目前都還是模板版，尚未比照ICT真正蒸餾（需先確認有無可用語料來源，如YouTube逐字稿）
- [ ] Ensemble lift（個別vs綜合命中率比較）與分歧情境表現分析——目前只有ICT一個人格，做不了

## 未來方向（待評估，尚未決定）
- [ ] 將「交易員辯論」流程本身封裝成一個 Claude Skill（比照女媧skill的模式：`/交易員辯論` 一鍵跑今日 bias）
- [ ] 將整個專案發展成完整前後端架構產品（Web 介面 / 儀表板 / 可能對外的產品）——結論是「先驗證再包裝」，Skill化是產品化的必經之路不是繞路

## 已確認可接受的變動
- [ ] 專案架構/現有程式碼允許後續大幅修改（不受目前 DebateSystem 現有實作綁死）

## 待整合的既有資源（Obsidian vault）
- [x] `skills/quant skill/quant-strategy-dev` 已比對評估，結論見 `DebateSystem/Phase4_回測系統_規劃.md`
- [ ] 參考 `Trading/Weekly bias/`、`Trading/Trading record/` 作為使用者自身交易紀錄的對照資料
