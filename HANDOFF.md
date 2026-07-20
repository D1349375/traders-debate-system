# 交接文件 — 人格蒸餾第二批（feature/persona-distill-batch2）

**建立日期**：2026-07-20
**分支**：`feature/persona-distill-batch2`
**範圍**：Rekt Capital、Benjamin Cowen、Michaël van de Poppe 三位人格的蒸餾，以及相關文件

---

## ⚠️ 最重要的一件事：新人格暫不納入生效

**決定（2026-07-20，使用者裁示）：本批三位新人格蒸餾完成，但先不加入辯論系統生效。**

具體意義：

- **不在 `preregistration.md` §8 增補登記**——沒有登記就不得落地多人格紀錄。
- **每日 bias 維持現行設定**，不因為 SKILL 檔案存在就自動啟用。
- `.claude/skills/` 下的三個新人格資料夾**是已完成的資產，不是待上線的組態**。

**給組員**：PERSONAS.md 有一節「怎麼用」描述了啟用流程，**那是給未來決定上線時用的**。
在使用者另行裁示之前，請不要執行該流程、不要修改 preregistration.md、不要把新人格加進每日 bias。
若你需要單獨測試某個人格（對話中問它、給它看一張圖），這不影響統計，可以做。

---

## 一、已完成事項

### 1.1 三位人格蒸餾（全部走完女媧 skill 完整流程）

| 人格 | 語料 | commit | 方法論維度 |
|---|---|---|---|
| Rekt Capital | 589 支 | `dd2c87e` | 四年減半週期、鏡像原則、週月線收盤紀律 |
| Benjamin Cowen | 387 支（自 2481 抽樣） | `6dfb969` | 量化風險水位、BTC 主導率、宏觀貨幣政策 |
| Michaël van de Poppe | 400 支（取最近 400） | `a095e4d` | 宏觀流動性傳導、altcoin 輪動階梯、sigma 極值減碼 |

每位皆含：`SKILL.md`、`DISTILLATION_REPORT.md`、`references/research/` 完整調研檔（維度檔 + 原始批次素材）。
三位皆通過 3 個獨立子 agent 驗證。

### 1.2 文件

| 檔案 | 狀態 |
|---|---|
| `PERSONAS.md` | **新增**（`c95708e`）——人格總覽索引，給組員的單一入口 |
| `README.md` | 已更新（完成清單、檔案地圖） |
| `TODO.md` | 已更新（完成項、新增待辦） |
| 本檔 `HANDOFF.md` | **新增** |

### 1.3 分支改名

`feature/rektcapital-persona-distill` → **`feature/persona-distill-batch2`**（原名只提 Rekt，但分支含三位人格）。
舊遠端分支已刪除，改名前已比對兩者 tip 完全相同，**無 commit 遺失**。

本機若還有舊分支：`git fetch --prune && git checkout feature/persona-distill-batch2`

### 1.4 基礎設施

- `data/fetch_transcripts.py` 新增可選的第三個參數＝取樣上限（向後相容），用於處理超大頻道。
  用法：`python data/fetch_transcripts.py <TraderName> <ChannelVideosURL> [取樣上限]`

---

## 二、待確認 / 待決定（需使用者或團隊裁示）

### 2.1 【已裁示】新人格是否納入生效 → **暫不納入**

見本檔開頭。未來若要上線，前置條件是在 `preregistration.md` §8 增補登記（人格清單 + 各自語料截止日）。

### 2.2 【待決定】是否開 PR

兩個分支目前都未開 PR：

- `feature/persona-distill-batch2`（三位人格 + 文件）
- `feature/tjr-persona-distill`（TJR）

### 2.3 【待決定】debate JSON 是否新增 `action` 欄位

**問題**：現行 `direction` 只有 `Bullish / Bearish / Neutral` 三值。MvdP 驗證時浮現——他唯一有可稽核成功紀錄的
動作是**減碼／分批出場**，那不等於「預期下跌」，但只能被壓成 `Bearish`，會讓聚合器把「趨勢未破但過熱該減碼」
誤讀成「預期下跌」。

**建議**：新增 `action` 欄位（`Add | Hold | Trim | Exit | None`），與 direction 分離。

**為何沒有順手改**：會動到 DB schema、聚合器與其他四個人格，不應在單一人格的蒸餾中夾帶。需獨立評估。
目前以 SKILL 內註明的方式暫時處理（`Bearish` 對 MvdP 包含「該減碼」的情形）。

### 2.4 【待決定】評估設計問題：單一 1d 主地平線對不同人格不公平

- **對高時間框架人格系統性不利**：Rekt（週/月）、Cowen（週線～宏觀）。兩者的 SKILL 已內建地平線折價
  （confidence 上限 45 / 50）作為緩解，**但那是緩解不是解法**。
- **對 MvdP 則相對有利**（其短線技術判斷命中率明顯高於中長期敘事判斷）。

**建議**：Phase 4 分析時對高時間框架人格另計 5d / 20d 探索性指標。

### 2.5 【待補】GCR 需要 Twitter/X 文字存檔才能蒸餾

已確認**無法用 YouTube 流程蒸餾**（Twitter/X 匿名者、帳號已消失、YouTube 無本人頻道）。
若要納入，需提供其 X 文字存檔以走純本地語料模式。Mark Douglas 語料同樣薄（已故、無官方頻道）。

### 2.6 【未動工】`bias_report_metrics.py`

n≥30 前應完成的分析腳本：方向命中率 + Brier Score / 校準曲線 + MCPT + Neutral 門檻敏感度附錄，
強制表 + 圖，附 pytest。分支 `feature/bias-report-metrics` 已開、venv 已備、25 baseline pytest 全過，**尚未寫任何程式碼**。

---

## 三、蒸餾過程中值得留下的方法論教訓

給後續要蒸餾人格的人。這些都是實際踩過的坑，不是理論。

1. **語料是硬性門檻，不可跳過。** 沒有足量公開語料就誠實地說蒸餾不出來，不要靠想像補完一個假人格。
   GCR 就是這樣被判定不可行的。

2. **Phase 1 抽取 agent 必須明確禁止派生子 agent。** 否則它可能只負責分派而不產出檔案，整批要重跑。
   （Rekt 蒸餾時發生過。之後所有 agent 都加上這條約束，14 個 agent 全部正常產出。）

3. **Phase 4 要有一支專門稽核「你自己寫的 SKILL」的 agent，而不是只稽核素材。**
   MvdP 那次靠它抓到兩個我自己看不見的問題：一個無出處的數字被寫進「誠實邊界」一節，
   以及一個會排除自身標誌案例的門檻。**驗證素材不夠，要驗證你的產出。**

4. **抓取紀錄要留檔**（見 `mvdp-perspective/references/research/00-corpus-provenance.md` 的格式）。
   記下抓取日、取樣參數、以及**哪些事實無法從留存證據回溯**。取樣參數會在列舉階段截斷日誌，事後補不回來。

5. **下游 agent 推翻上游宣稱是正常且應該鼓勵的。** 本批蒸餾中，合併與驗證 agent 多次駁回了主 agent 的
   任務指令假設（含「他從不設失效條件」「他總是把失敗轉為加強」「虧了才翻臉」等）。
   每份 `DISTILLATION_REPORT.md` 都有一節專門記錄被推翻或降級的宣稱。

6. **不要用網路搜尋補語料缺口。** 會混入非語料來源、破壞整條蒸餾鏈的可稽核性。
   三位人格的「外部視角」維度都偏弱（自製頻道結構上不會有第三方評價），我們的處理是**如實標注不足**，
   而不是去搜尋補齊。

---

## 四、相關文件

| 文件 | 內容 |
|---|---|
| [PERSONAS.md](PERSONAS.md) | 人格總覽：清單、方法論、辯論對立點、新增人格步驟 |
| [README.md](README.md) | 專案總覽、辯論協議、DB 架構、統計方法 |
| [TODO.md](TODO.md) | 完整待辦清單 |
| [preregistration.md](preregistration.md) | 統計預登記（**新人格上線需 §8 增補，目前不做**） |
| 各人格 `DISTILLATION_REPORT.md` | 該人格的蒸餾過程、決策取捨、驗證結果、已知限制 |
