# 人格 Skill 總覽（給組員的快速索引）

> 這份文件回答三個問題：**現在有哪些人格可用**、**每位的方法論是什麼**、**要怎麼用／怎麼再加一位**。
> 蒸餾方法論細節見各人格資料夾內的 `DISTILLATION_REPORT.md`；辯論協議與統計驗證見 [README.md](README.md)。

## 分支資訊

- **本批人格（Rekt Capital／Benjamin Cowen／MvdP）在分支 `feature/persona-distill-batch2`**。此分支原名 `feature/rektcapital-persona-distill`，因為後來不只放 Rekt 一位人格而改名；舊分支名已從遠端刪除，兩者 tip 完全相同，沒有任何 commit 遺失。
- 若你本機還有舊分支：`git fetch --prune && git checkout feature/persona-distill-batch2`
- TJR 在 `feature/tjr-persona-distill`；ICT 已在 `main`。

## 已完成蒸餾的人格

| 人格 | Skill 路徑 | persona key | 語料 | 核心方法論 | 主要時間框架 |
|---|---|---|---|---|---|
| **ICT** | `.claude/skills/ict-perspective/` | `ict` | 537 支 | 演算法決定論、流動性磁鐵、PD Array 多時間框架 | 日內 |
| **TJR** | `.claude/skills/tjr-perspective/` | `tjr` | 765 支 | SMC 結構＋交易心理／系統化紀律 | 日內～日線 |
| **EmperorBTC** | `.claude/skills/emperorbtc-perspective/` | `emperorbtc` | 81 支 | 拍賣市場理論、成交量測謊、區間極值／SFP | 日線～週線 |
| **Rekt Capital** | `.claude/skills/rektcapital-perspective/` | `rektcapital` | 589 支 | 四年減半週期、鏡像原則、週月線收盤紀律 | 週／月線 |
| **Benjamin Cowen** | `.claude/skills/benjamincowen-perspective/` | `benjamincowen` | 387 支（自 2481 抽樣） | 量化風險水位、BTC 主導率、宏觀貨幣政策 | 週線～宏觀 |
| **Michaël van de Poppe** | 蒸餾中 | `mvdp` | 抓取中（1275 抽樣近 400） | crypto TA＋altcoin 輪動 | 日～週線 |

無法蒸餾／暫緩：**GCR**（Twitter/X 匿名者、帳號已消失、YouTube 無本人頻道，需其 X 文字存檔才能走純本地語料模式）、**Mark Douglas**（已故、無官方頻道、語料薄）。

## 各人格在辯論中扮演什麼角色

這批人格不是「同一顆大腦戴五個面具」的湊數，選人標準是**方法論正交**——彼此在同一份行情上會因為框架不同而得出不同結論。目前存在三組真實對立：

**1. 操縱派 vs 反操縱派**
- ICT／TJR：價格被機構演算法驅動，行情在獵殺散戶止損。
- EmperorBTC：這是拍賣過程與多空 PVP，不需要陰謀論。
- Cowen：「narrative follows price」——獵殺敘事是站錯邊之後的事後歸因。

**2. 減半驅動 vs 流動性驅動**
- Rekt Capital：四年減半週期是主因，週期位置決定一切。
- Cowen：貨幣政策才是因，並以標普 500 沒有減半卻同樣有四年低點作為反例。

**3. 日內結構 vs 週期位置**
- ICT／TJR 看今天的流動性與 PD Array；Rekt／Cowen 看我們在週期的第幾個月。這是最容易在 R2 產生「你們看的根本不是同一個問題」的交鋒點。

## 兩項為了誠實而內建的特殊設計

**地平線折價（Rekt、Cowen）**
高時間框架人格被拉來回答「今天／明日方向」時，SKILL 內建 confidence 上限（Rekt ≈45、Cowen ≈50）。理由：讓人格對自己不擅長的地平線自動示弱，避免在 1d 評估上用滿分信心污染聚合結果。**但這只是緩解，不是解法**——單一 1d 主地平線評估所有人格對高時間框架者仍系統性不利，Phase 4 分析時應對這類人格另計 5d／20d 探索性指標（已記在 TODO）。

**反向誠實條款（Rekt、Cowen）**
每位「懷疑論者」人格都有一個自己不可證偽的核心信念（Rekt 護四年週期、Cowen 護反 altcoin 立場）。SKILL 明文要求：被質疑框架不可證偽時**必須據實承認、不得用 ad hoc 機制硬拗**。驗證顯示兩者都做得到。目的是讓 R2 收斂到問題本身，而不是互相表演。

## 怎麼用

**在辯論中啟用**：orchestrator skill 會把 `SKILL.md` 整份載入為人格 subagent 的 system prompt。每份 SKILL 都有自動化場景條款——被直接載入時跳過觸發詞判斷、直接進入角色。

**⚠️ 上線前必須做的事**：預登記已於 2026-07-19 生效。**納入新人格屬於受測系統的重大變更**，必須先在 [preregistration.md](preregistration.md) 以 §8 增補條目登記（載明人格清單與各自語料截止日），之後多人格紀錄才可以落地。多人格一旦生效，R2 結構化反駁自動啟用（協議與 DB 皆已支援）。

**單獨測試某個人格**：在對話中用該 SKILL 的觸發詞，或直接請 Claude 以該人格身分看一張圖／一份摘要。

## 怎麼再加一位人格

1. **先確認語料**（硬性門檻，不可跳過）。沒有足量公開語料就不要開始——寧可誠實地說「蒸餾不出來」，也不要靠想像補完一個假人格。YouTube 逐字稿優先。
2. **抓取**：`python data/fetch_transcripts.py <TraderName> <ChannelVideosURL> [取樣上限]`
   第三個參數可選，用來處理超大頻道（例如 Cowen 的 2481 支只抽最近 387 支）。腳本有防封鎖 sleep 與 `--download-archive` 續傳，中斷後重跑會接續。
3. **走女媧 skill 全流程**：Phase 0.5 建目錄 → Phase 1 平行多 agent 抽取 → Phase 1.5 合併成維度檔 → Phase 2 三重驗證（跨語境重現／生成性／排他性）→ Phase 3 依模板組裝 SKILL.md → Phase 4 獨立子 agent 驗證。
4. **一個實作上的坑**：Phase 1 抽取 agent 要明確加上「必須自己完成，絕對不要派生任何子 agent」的約束，否則它可能只負責分派而不產出檔案。
5. 完成後寫 `DISTILLATION_REPORT.md`、更新 README／TODO／本文件。

## 相關文件

| 文件 | 內容 |
|---|---|
| [README.md](README.md) | 專案總覽、辯論協議、DB 架構、統計方法、進度快照 |
| [TODO.md](TODO.md) | 待辦與未來方向 |
| [preregistration.md](preregistration.md) | 統計預登記（多人格上線需 §8 增補） |
| 各人格 `DISTILLATION_REPORT.md` | 該人格的完整蒸餾過程、決策取捨、驗證結果 |
| 各人格 `references/research/` | 原始調研維度檔（表達 DNA、外部評價、判斷紀錄等） |
