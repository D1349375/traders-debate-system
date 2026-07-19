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
- [ ] **累積第一筆紀錄前**：使用者確認 `preregistration_DRAFT.md`（尤其 Neutral ±0.5% 門檻與樣本數門檻）→ 改名 `preregistration.md` 簽署生效
- [ ] 開始每日累積真實 bias 紀錄（對 Claude Code 說「跑今日 bias」）
- [ ] n≥30 前實作 `bias_report_metrics.py`：方向命中率 + Brier Score/校準曲線 + MCPT,強制表+圖,附 pytest（Phase4規劃 2.1/§7.4）

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
