---
name: trader-debate
description: >-
  交易員人格辯論 orchestrator:跑今日 Daily Bias 完整流程(抓行情→人格 subagent 盲判→結構化反駁→機械聚合→落地 SQLite→可選產出每日報告,格式 md/html 由使用者選)。
  觸發詞:「交易員辯論」「跑今日 bias」「daily bias」「/交易員辯論」;報告相關:「產報告」「日報」「辯論報告」。
  也用於回填事後價格(「回填結果」「outcomes」)。專案位置:Side Project/DebateSystem/。
---

# 交易員辯論 Orchestrator Runbook

你(主 agent)在此流程中的身分是**裁判/記帳員**。職責邊界(嚴格遵守):

- ✅ 分發行情摘要、調度人格 subagent、收集輸出、呼叫 CLI 落地
- ❌ **禁止自己分析行情、給出方向判斷**——你不是第 N+1 個人格
- ❌ 禁止修改機械聚合的結果;敘述性總結只能描述,不得推翻聚合方向
- ❌ 禁止加開輪次:協議固定 R1 + R2 兩輪(單人格只跑 R1),吵得精彩也不加輪

所有指令在 `Side Project/DebateSystem/` 目錄下用 venv 執行:
`venv\Scripts\python.exe main.py <cmd>`

## 前置檢查

1. 確認 `DebateSystem/preregistration.md` 存在且已生效(已生效:2026-07-19 版)。
   **若不存在或被作廢:停下來,請使用者先完成預登記,不可累積紀錄。**
2. 生效人格與標的以 preregistration 為準。現行:人格=ICT;標的=**BTC/USDT 與 ETH/USDT**(每天兩個標的都要跑)。

## 流程(對每個標的獨立走完 Step 1-4)

### Step 1 — 抓行情
```
venv\Scripts\python.exe main.py market --asset BTC/USDT
venv\Scripts\python.exe main.py market --asset ETH/USDT
```
每次輸出第一行是 `{"date": ..., "asset": ...}`,其後是行情摘要全文。記下 date/asset,摘要原文傳給人格。

### Step 2 — R1 獨立盲判
對**每個生效人格 × 每個標的**各開一個獨立 subagent(Agent 工具,general-purpose 即可),可全部平行:

- prompt 組成:該人格的 SKILL.md 全文(ICT 在 `.claude/skills/ict-perspective/SKILL.md`,subagent 自行讀取)+ **該標的**的行情摘要 + 輸出格式要求
- **隔離鐵律:R1 的 prompt 中不得包含任何其他人格的輸出或存在資訊;也不得混入其他標的的摘要**(逐標的獨立判斷,歸因才乾淨)
- 要求輸出嚴格 JSON:
```json
{"direction": "Bullish|Bearish|Neutral", "confidence": 0-100, "reasoning": "以該人格口吻與框架的完整分析"}
```

收齊後寫入暫存 JSON 檔(scratchpad),每筆補上 `date`/`asset`/`persona`/`round`(=1)/`model_id`(subagent 實際使用的模型 ID),然後:
```
venv\Scripts\python.exe main.py record --json <r1檔案路徑>
```

### Step 3 — R2 結構化反駁(僅當生效人格 ≥2)
單人格直接跳到 Step 4。多人格時,對每個人格再開 subagent,prompt 包含:

1. 自己的 R1 輸出 + **其他人格的 R1 結構化三欄**(direction/confidence/reasoning,不傳過程全文)
2. 協議必答項:
   - (a) 指出**與你對立的最強論點**並正面回應(不准挑最弱的打)
   - (b) 給出 falsifier:什麼證據出現會讓你改判
   - (c) 更新後的 direction/confidence(可以不變,但要說明為何不變)
3. 輸出 JSON 加一欄 `falsifier`

record 落地(round=2)。

### Step 4 — 聚合與落地(逐標的)
```
venv\Scripts\python.exe main.py finalize --date <date> --asset <asset> [--summary-file <敘述總結檔>]
```
敘述總結(可選)由你撰寫:僅描述各方立場與分歧點,**不得下自己的方向結論**。
finalize 會自動:R1 旁路聚合(無辯論基準)+ 末輪最終聚合 + 分歧度統計 + price_at_bias。

### Step 5 — 回報使用者
逐標的回報:最終方向/信心、R1 基準(若與最終不同要點出)、各人格立場摘要、分歧度。
結尾必附一句:**「此為研究性統計工具的輸出,非投資建議。」**

### Step 6 — 產出每日報告(可選,格式由使用者選)

1. **問格式**:若使用者在觸發時已指定格式(「md 報告」「html 報告」「網頁報告」),直接採用;
   否則用 AskUserQuestion 問一次,選項:`HTML(含互動 K 線圖)` / `Markdown` / `不產報告`。
2. **版型**:照抄 `templates/` 下的參考版型結構,只換當日內容,不重新設計:
   - `templates/report_reference.html` — HTML 版。含 SVG K 線圖(60 根日線 + 量能副圖 + hover tooltip)、
     各人格關鍵價位標註(levels/zones/events 寫在 `CONF` 物件)、偏見對比卡、聚合算式、人格卡(含
     `<details>` 完整論述與 falsifier)、辯論結構盒、方法論備註、免責聲明。日線數據從 Step 1 的
     market 輸出解析成 JSON 注入 `const DATA`(參考版型內已有注入點格式)。**注意保留 `<meta charset="utf-8">`。**
   - `templates/report_reference.md` — Markdown 版。同樣結構,K 線圖以「關鍵價位表 + 事件標記」代替。
3. **報告內容鐵律**(承襲裁判邊界):兩種格式都必須同時呈現**單人格基準(生效人格 R1)**與
   **辯論後聚合**兩欄;所有敘述只描述各方立場與分歧,不得出現你自己的方向判斷;
   聚合數字直接取 finalize / aggregate 的輸出,不得改寫。
4. **落點**:寫入 `data/reports/YYYY-MM-DD.{html,md}`(同日重跑直接覆蓋)。
   HTML 版若使用者要網址,用 Artifact 工具發佈;**同一天更新請重發同一檔案路徑以沿用同一網址**。
5. dry-run(未落 DB)時報告必須帶明顯的 `DRY RUN — 不計入預登記樣本` 標示;正式跑則移除該標示,
   並把當日 `price_at_bias` 與 `protocol_version` 寫進頁首。

## 回填事後價格(獨立操作,任何時候可跑)
```
venv\Scripts\python.exe main.py outcomes
```
只回填已收 K 線且為空的欄位,冪等可重複執行。建議每次跑 daily bias 前順手執行一次。

## 落地紀律

- record/finalize 遇「已落地不可覆寫」報錯=當日已跑過,**不要試圖刪除或改寫**,向使用者回報即可
- 任何統計評估(命中率/Brier)不在本 skill 範圍——那是 Phase 4 的 `bias_report_metrics.py`(未實作),不要臨時手算了就宣稱結論
