# 交易員人格蒸餾辯論系統 (DebateSystem)

> 蒸餾長期獲利交易員的思維框架成可運行的人格 Skill，讓多個人格 agent 對每日行情獨立判斷、結構化辯論，產出 Daily Bias，並以嚴格的統計方法長期驗證「這套判斷到底準不準」。
>
> **專案定位：輔助決策的機率參考／研究工具，不是自動交易訊號。**

---

## 1. 專案想法與整體規劃

### 1.1 核心想法

市面上的交易教學內容（YouTube、推特）大多是語言化的決策邏輯，無法直接量化回測。本專案的路徑是：

1. **蒸餾**：用女媧 skill 把一位交易員的公開語料（逐字稿、貼文）蒸餾成結構化的人格檔案（心智模型 + 決策啟發式 + 表達 DNA），存成可被 LLM 載入的 `SKILL.md`。
2. **辯論**：多個人格 agent 讀同一份市場摘要，先獨立盲判、再結構化交鋒，由裁判 agent 機械聚合出當日 bias。
3. **驗證**：每一筆 bias 落地進 SQLite，事後對齊實際價格，累積樣本後用命中率、Brier Score、校準曲線、MCPT 等指標回答「有沒有真實 alpha」——驗證方法論直接繼承自本 vault 的 `quant-strategy-dev` skill（v13）。

原始六階段規劃（完整版見 [交易員人格蒸餾辯論系統 — 技術架構與工作分解(WBS).md](交易員人格蒸餾辯論系統%20—%20技術架構與工作分解\(WBS\).md)）：

```
Phase 0 篩選交易員 → Phase 1 資料蒐集 → Phase 2 人格蒸餾
→ Phase 3 辯論機制 → Phase 4 回測系統 → Phase 5 迭代優化
```

策略：先用 1 位交易員（ICT）跑通全流程 POC，驗證蒸餾品質後再擴展多人格。

### 1.2 與原始 WBS 的偏離（實際演化）

| 項目 | WBS 原規劃 | 實際走向 |
|---|---|---|
| 語料來源 | X API v2 / Threads 貼文 | **YouTube 教學影片逐字稿**（ICT 537 支，抓取流程見 [youtube_scraper_guide.md](youtube_scraper_guide.md)，ffmpeg 在專案根目錄） |
| LLM 引擎 | Claude API orchestration | **Claude Code subagent 架構**（C 路線，2026-07-19 定案並實作）：主 agent＝裁判、人格＝subagent、Python CLI 只管落地；未來產品化再遷 Claude API（B 路線），DB／聚合／預登記全部共用。舊 Gemini 引擎封存於 `engine/legacy_gemini_runner.py` |
| 辯論流程 | 「交叉點評」一筆帶過 | 已細化為固定兩輪的結構化協議（見第 3 節） |
| 回測設計 | 4 個追蹤指標的概念清單 | 已完成完整規劃並對齊 quant skill v13（見 [Phase4_回測系統_規劃.md](Phase4_回測系統_規劃.md)） |

---

## 2. 人格蒸餾過程與建議

### 2.1 蒸餾流程（女媧 skill，ICT 為首個完成案例）

女媧 skill 安裝在專案層級 `.claude/skills/huashu-nuwa`。ICT（Inner Circle Trader）完整跑過 Phase 0.5 → 1 → 1.5 → 2 → 2.5 → 3 → 4 → 5 全流程：

```
537 支 YouTube 逐字稿
  → 多 agent 並行提取（心智模型／決策啟發式／表達 DNA）
  → 三重驗證（跨場景重複出現 + 有預測力 + 有排他性）
  → 產出 .claude/skills/ict-perspective/SKILL.md
  → 聊天 + 真實圖表測試驗證（語氣與框架皆有效）
```

產出內容：6 個核心心智模型（演算法決定論、流動性磁鐵、PD Array 多時間框架、時間優先於價格、機率優先於預測、人設即行銷引擎）、9 條決策啟發式、完整表達 DNA，另含外部他者評價與時間線調研。SKILL.md 內建自動化場景條款：被 orchestrator 直接載入為 system prompt 時，跳過觸發詞判斷直接進入角色。

### 2.2 蒸餾經驗與建議（給後續人格）

- **語料量是門檻**：ICT 的品質來自 537 支影片的深度。**TJR（765 支）與 EmperorBTC（81 支）已於 2026-07-19 完成真正蒸餾**。Mark Douglas 仍為模板版（無官方頻道、語料薄）；**GCR 無法用 YT 流程蒸餾**（Twitter/X 匿名者、已消失，YouTube 無本人頻道）。擴展任何人格前先確認有無可用語料來源（YouTube 逐字稿優先；抓取用 `data/fetch_transcripts.py`，已驗證可抓任意頻道）。
- **蒸餾品質要先驗證再上線**：比照 ICT 的做法——聊天測語氣、真實圖表測框架，通過才算蒸餾完成。WBS 2.4 的「歷史情境重放一致性 ≥60%」是更嚴格的正式驗收，有語料時間戳的人格可以做。
- **語料截止日要記錄**：這直接決定回測窗口能不能往回開（見 4.2 的洩漏風險）。ICT 語料涵蓋至 2026 年中。

---

## 3. 系統架構與各 Agent 操作流程

### 3.1 架構總覽（2026-07-19 定案的辯論協議）

```
主 agent（裁判／記帳員）
 ├─ [分發] 產生標準化市場摘要，發給各人格 subagent
 │         （未來升級：依流派給不同資料切面——資訊不對稱設計，見 3.4）
 ├─ [R1 獨立盲判] N 個人格 subagent 平行判斷，互相不可見
 │         各自輸出 direction / confidence / reasoning → 落 DB (round=1)
 ├─ [旁路聚合] 裁判對 R1 做機械聚合 → 存為「無辯論基準」
 ├─ [R2 結構化反駁] 各人格收到他人 R1 的結構化輸出（三欄，非全文過程）
 │         每人必須：(a) 正面回應最強對立論點（不准挑軟柿子）
 │                   (b) 給出 falsifier（什麼證據出現會讓自己改判）
 │                   (c) 更新後的 direction / confidence → 落 DB (round=2)
 └─ [最終聚合] 裁判對 R2 機械聚合 + 分歧度統計
           → daily_bias_results（含 R1 基準與 R2 最終，兩者並存）
```

### 3.2 各角色職責邊界

**主 agent（裁判）——職責清單刻意窄：**
- 產生／分發市場摘要、調度 subagent、收集各輪輸出、落 DB
- 機械聚合（規則預先寫死，例：信心加權多數決）
- 計算並保留分歧度（方向不一致比例、confidence 標準差）——**不做共識抹平**
- **禁止**：自己讀行情下判斷（否則它成為權力最大的第六人格，事後無法歸因命中率是誰的）；LLM 若參與總結只寫敘述性報告，不得推翻機械聚合的方向

**人格 subagent：**
- 載入各自 `SKILL.md` 作為 system prompt，內容層完全依人格框架自由發揮
- 只在協議規定的時點發言、回應協議規定的必答項（互動層受約束，思考層不受約束）
- R1 階段絕對隔離：結果出來前不能看到任何其他人格的輸出與過程

### 3.3 協議設計原則（為什麼這樣設計）

1. **強制交鋒、禁止強制共識**——LLM 多智能體辯論的已知病灶是諂媚趨同（往多數／高信心方靠攏而非往正確方靠攏）。分歧本身是 Phase 4 要測的訊號（分歧情境準確率），協議不能把它磨平。
2. **輪數固定兩輪、寫進預登記**——多輪迭代=趨同壓力遞增+信息增量遞減；「吵得精彩就多吵一輪」等於引入未登記的參數。
3. **R2 只傳結構化三欄、不傳全文**——修辭越多諂媚越強；結構化輸出讓對方被論點說服而不是被文筆說服。
4. **旁路（R1 直接聚合）必須保留**——「辯論是否加分」本身是待驗證假設，文獻無定論。兩條路並存落 DB，Phase 4 用配對比較裁決 R2 的價值；不留旁路，辯論的價值永遠是信仰而非數據。
5. **辯論機制自身也要過驗證**——不因為它是專案名字就豁免。這是 quant skill 世界觀的直接延伸。

### 3.4 下一階段設計方向：資訊不對稱

現況五個人格是同一顆 LLM 讀同一份摘要——不是五個獨立觀察者，是同一顆大腦戴五個面具，辯論無法創造新資訊。更強的設計：**每個人格拿到符合其流派的資料切面**（ICT 拿價格結構／流動性位置；籌碼型拿資金費率／OI／持倉比；宏觀型拿 DXY／利率）。這讓 R2 有真實的資訊交換（「你沒看到的費率數據顯示…」），辯論從修辭遊戲變成資訊聚合。多人格上線後優先投資這裡。

### 3.5 資料落地（SQLite）

四張表（[database/schema.py](database/schema.py)）：`market_data`（行情+摘要）、`persona_debates`（逐人格逐輪，含 falsifier／model_id）、`daily_bias_results`（R1 基準＋最終聚合＋分歧度＋事後價格欄位）、`backtest_runs`（Phase 4 分析紀錄）。

落地紀律（[database/db.py](database/db.py)）：判斷落地即定案，record／finalize 不提供覆寫；事後回填只填空欄位。機械聚合在 [engine/aggregate.py](engine/aggregate.py)（信心加權投票，純函數＋pytest）。入口 CLI：[main.py](main.py)（`market`／`record`／`finalize`／`outcomes` 四指令）；orchestrator skill 在 `.claude/skills/trader-debate/SKILL.md`（觸發：「跑今日 bias」）。

---

## 4. 驗證方法論（Phase 4 摘要）

完整規劃見 [Phase4_回測系統_規劃.md](Phase4_回測系統_規劃.md)。要點：

### 4.1 核心認知

這不是「策略回測」而是「預測準確率評估」——評估對象是離散方向預測 + confidence，沒有進出場與權益曲線。從 `quant-strategy-dev` skill 搬的是**治理紀律**（預登記、測試帳本、MCPT、Bootstrap CI、CUSUM 監控、pytest 邊界案例），不是工具本身；Brier Score／校準曲線／ensemble lift 是本專案特有的新增件。

### 4.2 已對齊 skill v13 的五項機制（Phase4 §7）

1. **預登記**：第一筆 bias 落地前，先把命中定義（主地平線、Neutral 門檻、最低樣本數、通過標準）寫死進帶日期的 `preregistration.md`，之後不可改。
2. **地平線匹配**：Daily Bias 主評估地平線 = 1d；5d/20d 只作預先標註的探索性指標。
3. **重疊視窗序列相關**：5d/20d 評估用 block bootstrap 或非重疊抽樣，否則 CI 虛高。
4. **強制指標表 script**：`bias_report_metrics.py` 單一呼叫出完整表+圖，缺表缺圖=報告未完成（v10/v13「模板≠執行」病灶的直接繼承）。
5. **BH-FDR**：多人格「挑最佳」比較用現成 `multiple_testing.py`（多人格上線後適用）。

### 4.3 本專案特有的最大風險：語料洩漏

ICT 語料涵蓋至 2026 年中，且逐字稿含他對過去實際行情的評論——回測窗口若與語料期重疊，人格可能「記得」行情而非用框架推理（LLM 版 look-ahead bias）。**目前的處理方式：往前累積新資料，回測窗口落在語料截止日之後**——每日實測正好是最乾淨的解法。

---

## 5. 目前進度（2026-07-19）

### 已完成

- [x] 女媧 skill 安裝（專案層級 `.claude/skills/huashu-nuwa`）
- [x] **ICT 人格完整蒸餾**（全 Phase 跑完），產出 `.claude/skills/ict-perspective/SKILL.md`，聊天+真實圖表測試通過
- [x] **TJR 人格完整蒸餾（2026-07-19）**：765 支 YouTube 逐字稿（語料 2022-09~2026-07）走完女媧全流程（16 批平行抽取→7 維度合併→三重驗證→組裝），產出 `.claude/skills/tjr-perspective/SKILL.md`，3 子 agent 驗證通過（已知立場／辯論 JSON／邊緣推斷，全程守語言紅線）。研究過程完整留存於 `references/research/`，另附 `DISTILLATION_REPORT.md`
- [x] **EmperorBTC 人格完整蒸餾（2026-07-19）**：以 `data/fetch_transcripts.py` 自行抓取官方頻道 81 支逐字稿（語料 2025-03~2026-07），走完女媧流程（4 批抽取→合併/三重驗證→組裝），產出 `.claude/skills/emperorbtc-perspective/SKILL.md`，3 子 agent 驗證通過。**crypto 原生（BTC 主場）＋走 Volume/Auction Market Theory 路線、哲學上反對 ICT/TJR 的「操縱獵殺」敘事**——為辯論系統提供真實框架分歧（呼應 §3.4）。附 `DISTILLATION_REPORT.md`
- [x] Phase 4 回測規劃文件完成，並已對齊 quant skill v13（§7 增補）
- [x] 辯論協議設計定案（本 README 第 3 節：兩輪固定、裁判職責邊界、旁路設計）
- [x] **C 架構實作完成（2026-07-19）**：
  - [database/schema.py](database/schema.py) 四張表（含事後價格欄位、falsifier、model_id、`backtest_runs`），DB 已重建
  - [database/db.py](database/db.py) 落地層（寫入即定案不可覆寫）＋ [engine/aggregate.py](engine/aggregate.py) 機械聚合／分歧度
  - [main.py](main.py) 改為 CLI（`market`／`record`／`finalize`／`outcomes`），stdout 強制 UTF-8
  - `.claude/skills/trader-debate/SKILL.md` orchestrator skill（「跑今日 bias」即觸發）——原「未來方向」的 Skill 化提前完成
  - [tests/](tests/) 25 個 pytest 全過（聚合邊界案例＋落地紀律＋回填冪等）；`market` 指令實測通過
  - 舊 Gemini 引擎封存為 [engine/legacy_gemini_runner.py](engine/legacy_gemini_runner.py)
- [x] 預登記草案 [preregistration_DRAFT.md](preregistration_DRAFT.md)（**尚未生效，待使用者確認**）

### 目前缺口

1. **預登記未生效**：`preregistration_DRAFT.md` 需使用者逐項確認（尤其 Neutral 門檻 ±0.5%、n≥30/60 門檻）後改名 `preregistration.md` 簽署——**第一筆紀錄落地前必須完成**，trader-debate skill 會擋。
2. **`bias_report_metrics.py` 未實作**：Phase 4 的強制指標表 script（命中率＋CI、Brier、校準、MCPT），等樣本開始累積後、首次報告（n≥30）前完成即可。

### 下一步（依序）

1. 使用者確認預登記草案 → 生效
2. 開始每日累積：對 Claude Code 說「跑今日 bias」即可（trader-debate skill 全自動：抓行情→ICT subagent 盲判→落地→聚合）
3. 平日不定期跑 `python main.py outcomes` 回填事後價格（或每次跑 bias 時 skill 自動順跑）
4. n≥30 前實作 `bias_report_metrics.py`（含 pytest 邊界案例）

### 待評估（多人格上線後）

- **TJR、EmperorBTC 已完成蒸餾（見「已完成」區）**；Mark Douglas 語料薄待確認、**GCR 無 YT 語料無法用此流程蒸餾**（需其 Twitter/X 文字存檔才能走純本地語料模式）。**哪些人格納入生效由使用者在預登記決定**——一旦多人格生效，R2 結構化反駁流程自動啟用（協議與 DB 已支援），且 `preregistration_DRAFT.md` §1 需從單一 ICT 改為多人格，ensemble lift 與 BH-FDR 隨之適用（第一筆紀錄落地前完成）。EmperorBTC 因 crypto 原生＋框架對立，特別適合納入 BTC 辯論
- Ensemble lift 與分歧情境表現分析
- 資訊不對稱資料切面（3.4）
- 產品化（B 路線：Claude API 化＋Web 介面）——「先驗證再包裝」，DB／聚合／預登記層可直接沿用

---

## 6. 已知風險與限制

1. **樣本累積慢**：Daily bias 一年約 250 筆，統計顯著性需長期累積或多標的並行。
2. **語料洩漏**（4.3）：語料截止日前的回測結果可能因語料記憶而虛高；目前無自動化稽核工具。
3. **敘事→訊號失真**：蒸餾出的是語言化決策邏輯，轉成方向判斷的過程可能失真。
4. **相關性錯誤**：多人格同源於一顆 LLM，人格間的「獨立性」是設計出來的，不是天然的——這是資訊不對稱設計要解的問題。
5. **定位紅線**：本專案是研究工具；若未來把 confidence 轉成部位建議，等於跨入自動交易訊號，需使用者明確決定（Phase4 §3 有記錄此觸發條件）。

---

## 附錄：專案檔案地圖

| 檔案 | 用途 |
|---|---|
| [README.md](README.md) | 本文件：專案總覽＋協議＋進度 |
| [TODO.md](TODO.md) | 工作清單（與本文件進度區同步維護） |
| [交易員人格蒸餾辯論系統 — 技術架構與工作分解(WBS).md](交易員人格蒸餾辯論系統%20—%20技術架構與工作分解\(WBS\).md) | 原始規劃（歷史文件，部分已演化） |
| [Phase4_回測系統_規劃.md](Phase4_回測系統_規劃.md) | 回測系統完整規劃（含 v13 對齊 §7） |
| [preregistration_DRAFT.md](preregistration_DRAFT.md) | 命中定義預登記（草案，待確認生效） |
| [youtube_scraper_guide.md](youtube_scraper_guide.md) | 語料抓取流程 |
| [main.py](main.py) | 落地 CLI：`market`／`record`／`finalize`／`outcomes` |
| [database/schema.py](database/schema.py) | SQLite schema（四張表，含事後價格欄位） |
| [database/db.py](database/db.py) | 落地層（寫入即定案、回填冪等） |
| [engine/aggregate.py](engine/aggregate.py) | 機械聚合＋分歧度（裁判的計算核心，純函數） |
| [engine/legacy_gemini_runner.py](engine/legacy_gemini_runner.py) | 舊 Gemini 引擎（已封存，僅供歷史參考） |
| [data/ingestion.py](data/ingestion.py) | Binance 行情抓取、摘要生成、事後收盤價回補 |
| [tests/](tests/) | pytest（聚合邊界＋落地紀律，25 個） |
| `.claude/skills/ict-perspective/SKILL.md` | ICT 人格 Skill（537 逐字稿蒸餾） |
| `.claude/skills/tjr-perspective/SKILL.md` | TJR 人格 Skill（2026-07-19 蒸餾，765 逐字稿；`references/research/` 存完整調研） |
| `.claude/skills/emperorbtc-perspective/SKILL.md` | EmperorBTC 人格 Skill（2026-07-19 蒸餾，81 逐字稿；crypto 原生、Volume/Auction Market Theory 路線） |
| `../.claude/skills/trader-debate/SKILL.md` | Orchestrator skill（辯論協議 runbook） |

相關知識庫頁（vault `知識庫/`）：[[專案總覽]]、[[quant-strategy-dev skill]]、[[多重測試與測試帳本]]、[[倖存者偏差]]
