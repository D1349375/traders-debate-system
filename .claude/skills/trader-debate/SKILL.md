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

1. 確認 `DebateSystem/preregistration.md` 存在且已生效。
   **若不存在或被作廢:停下來,請使用者先完成預登記,不可累積紀錄。**
2. **每次執行都重讀 preregistration.md §1 及 §8 全部增補條目,取得當下實際生效的人格清單與標的**——
   不要依賴記憶或任何舊快照,生效名單會隨增補持續變動(例如 2026-07-20 由單一 ICT 擴增為
   ICT+TJR+EmperorBTC 三人格)。人格 SKILL.md 路徑對照:
   - ICT → `.claude/skills/ict-perspective/SKILL.md`
   - TJR → `.claude/skills/tjr-perspective/SKILL.md`
   - EmperorBTC → `.claude/skills/emperorbtc-perspective/SKILL.md`
   標的:**BTC/USDT 與 ETH/USDT**(每天兩個標的都要跑,除非 preregistration 增補另有標的變更)。
3. **檢查判斷日年份是否超出 `data/ingestion.py` 的 `_FOMC_MEETINGS_2026` 已涵蓋範圍**(目前僅涵蓋2026年)。
   若判斷日已進入 2027 年或更新的年份:**照常執行今日 bias**(不因此停下),但要在 Step 5 回報使用者時
   一併提醒:「FOMC 決策週旗標已超出涵蓋範圍(僅2026年),本次判斷可能漏掉真實的 FOMC 週,需要人工
   更新 `_FOMC_MEETINGS_2026` 常數(來源建議:federalreserve.gov/monetarypolicy/fomccalendars.htm)」。
   NFP 與 8月旗標為規則計算,任何年份皆準,不受此限制。

## 流程(對每個標的獨立走完 Step 1-4)

### Step 1 — 抓行情(輸入凍結 + 資訊分流)
**資訊分流(v4/v5,見 preregistration.md §8)**:每個標的要凍結**三份**檔案,不是一份——ICT 專屬 `core` 變體(無成交量)、TJR 專屬 `tjr` 變體(core內容 + 相關資產BTC/ETH參考行情)、EmperorBTC 專屬 `emperorbtc` 變體(含成交量 + RSI + 量能比值)。三變體的差異定義在 `data/ingestion.py`,orchestrator 不需要、也不應該自己詮釋或補充指標,照抓照存即可。

**先檢查 `data/market_context/<date>_<asset代碼>_<variant>.txt` 是否已存在**(asset代碼=去掉斜線如 BTCUSDT;variant=`core`/`tjr`/`emperorbtc`,三者分開判斷):
- **已存在 → 必須直接重用該檔,不得重抓**。同一判斷日的所有 run(含 dry-run、含不同協作者)都吃同一份凍結輸入,否則跨 run 不可比。
- 不存在 → 抓行情並落檔(每個標的三條指令):
```
venv\Scripts\python.exe main.py market --asset BTC/USDT --variant core       > data\market_context\<date>_BTCUSDT_core.txt
venv\Scripts\python.exe main.py market --asset BTC/USDT --variant tjr        > data\market_context\<date>_BTCUSDT_tjr.txt
venv\Scripts\python.exe main.py market --asset BTC/USDT --variant emperorbtc > data\market_context\<date>_BTCUSDT_emperorbtc.txt
venv\Scripts\python.exe main.py market --asset ETH/USDT --variant core       > data\market_context\<date>_ETHUSDT_core.txt
venv\Scripts\python.exe main.py market --asset ETH/USDT --variant tjr        > data\market_context\<date>_ETHUSDT_tjr.txt
venv\Scripts\python.exe main.py market --asset ETH/USDT --variant emperorbtc > data\market_context\<date>_ETHUSDT_emperorbtc.txt
```
輸出第一行是 `{"date": ..., "asset": ..., "variant": ...}`,其後是行情摘要全文。記下 date/asset。
`tjr` 變體會多抓一次相關標的的行情(BTC查詢會多抓ETH,反之亦然),屬預期行為。三變體是各自獨立的即時抓取,即時價格可能有數秒級落差(遠小於 Neutral 門檻,不需處理,`snapshot_captured_at` 已誠實記錄實際抓取時間)。
凍結檔應隨 git 提交,讓協作者重跑時拿到同一份輸入。

### Step 2 — R1 獨立盲判
對**每個生效人格 × 每個標的**各開一個獨立 subagent(Agent 工具,general-purpose 即可),可全部平行:

- **prompt 必須逐字使用 `templates/r1_prompt.txt`,只填充 `{佔位符}`,不得增刪或改寫任何語句**(prompt 措辭差異會系統性平移輸出分佈,見「隨機性控制」)。人格 SKILL.md 路徑:ICT=`.claude/skills/ict-perspective/SKILL.md`,其餘同模式。
- **`{MARKET_CONTEXT_PATH}` 依人格分流填值,不是固定同一份**:ICT 填 `..._core.txt`;TJR 填 `..._tjr.txt`;EmperorBTC 填 `..._emperorbtc.txt`。填錯等於資訊分流失效,務必對照 Step 1 的檔名。
- **隔離鐵律:R1 的 prompt 中不得包含任何其他人格的輸出或存在資訊;也不得混入其他標的的摘要,也不得把某人格的變體內容用給另一人格**(逐標的、逐分流獨立判斷,歸因才乾淨)。`tjr` 變體內建的相關資產參考行情屬於 TJR 專屬設計,不算違反此鐵律。
- 輸出格式已寫死在模板內,含**必答項 `intraday_scenario`**(今日收盤前雙劇本 if-then,範圍限定判斷日當天,不得是多日/週目標;詳細規格見模板檔本身,不在此重複)。

收齊後寫入暫存 JSON 檔(scratchpad),每筆補上 `date`/`asset`/`persona`/`round`(=1)/`model_id`(subagent 實際使用的模型 ID),然後:
```
venv\Scripts\python.exe main.py record --json <r1檔案路徑>
```

### Step 3 — R2 結構化反駁(僅當生效人格 ≥2)
單人格直接跳到 Step 4。多人格時,對每個人格再開 subagent:

- **prompt 必須逐字使用 `templates/r2_prompt.txt`,只填充 `{佔位符}`**。R1 各家輸出先整理成單一 JSON 檔(scratchpad,含 direction/confidence/reasoning/intraday_scenario 四欄,不含過程全文),路徑填入 `{R1_JSON_PATH}`。
- `{MARKET_CONTEXT_PATH}` 分流規則與 Step 2 相同:ICT 填 `..._core.txt`,TJR 填 `..._tjr.txt`,EmperorBTC 填 `..._emperorbtc.txt`,不得填錯或混用。
- 協議必答項 (a)(b)(c)(d) 與輸出格式(JSON 加 `falsifier`、`intraday_scenario` 兩欄)已寫死在模板內。(d) = 更新後的 `intraday_scenario`,範圍限制同 Step 2,可沿用 R1 版本但須重新確認仍成立,不可留空。

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
     `<details>` 完整論述與 falsifier)、辯論結構盒、方法論備註、免責聲明。日線數據(含量能副圖需要的
     volume)從 Step 1 的 `..._emperorbtc.txt`(唯一含成交量的變體)解析成 JSON 注入 `const DATA`
     (參考版型內已有注入點格式)——**這只是報告視覺化用途,不影響任何人格的判斷輸入**,ICT/TJR 的
     R1/R2 prompt 仍只讀 `..._core.txt`。**注意保留 `<meta charset="utf-8">`。**
   - `templates/report_reference.md` — Markdown 版。同樣結構,K 線圖以「關鍵價位表 + 事件標記」代替。
   - **兩版皆含**「ICT/TJR Range 與折溢價判讀」表(2026-07-22 起,見兩份版型內範例):逐標的列出 ICT、TJR
     兩人在 R2(若只跑R1則取R1)reasoning 裡自己講的 dealing range 高低點、equilibrium、據此判定的
     premium/discount。**照抄他們原話裡的數字,裁判不得重新計算或挑一個「更合理」的 range**——這張表
     的目的是讓使用者自行檢視兩人每天選的 range 是否前後一致,純供人工複核用,不是正式命中指標,
     不影響任何聚合或判斷邏輯。EmperorBTC 用 balance/imbalance 而非 premium/discount,不列入此表。
     **必須含「時間框架層級」欄**(週線HTF/日線腿/近期擺盪/4H等,照人格自己講的名稱寫)——同一人格
     常在不同層級各給一次判讀(例如同時給「大範圍讀法」與「近期讀法」),**每個層級各自成一列**,
     不得把不同層級的數字混在同一列平均或挑一個代表,也不得因為兩列數字不同就當成矛盾標記出來:
     這正是這張表要讓使用者一眼分辨「多時間框架的正常分歧」與「同一層級內真的判斷不一致」的目的。
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

## 隨機性控制(2026-07-19 起,依兩次同日 dry-run 分歧事件納入)

**事實**:同日、同陣容、名義上同資料的兩次 dry-run 給出不同結果(EBTC Bearish 55 vs Neutral 30;聚合 67 vs 78;一次無人改信心、一次兩家下修)。差異來源分三層,對策不同:

1. **輸入漂移(可消除)**:`market` 的「當下快照」隨抓取時刻變動。→ 已由 Step 1 的凍結檔規則消除:同一判斷日一份輸入,先到先凍結,後跑者必須重用。
2. **Prompt 漂移(可消除)**:orchestrator 手寫 prompt 的措辭差異會系統性平移人格輸出。→ 已由 `templates/r{1,2}_prompt.txt` 逐字模板消除。**修改模板=修改協議**:須在報告與 DB 摘要中註明模板版本變更日期,分析時分段,不可混算(同「換模型=換預測者」原則)。
3. **LLM 抽樣隨機性(不可消除,只能量測與平均)**:同輸入同 prompt 下,人格判斷仍是分佈抽樣——包括「敘事層」隨機(如 ICT 兩次選了不同 dealing range 錨點,連帶改變 discount/premium 結論與信心)。對策:
   - **不重跑**:正式紀錄=當日第一次抽樣,「已落地不可覆寫」就是防 cherry-picking 的機制。dry-run 重跑結果不同是預期行為,不是 bug,不得挑好看的那次講故事。
   - **靠 n 平均**:預登記 n≥30/60 評估的是分佈的平均技能,單日單次(不管多漂亮)不可作準。
   - **(選項,未啟用)K 次自洽投票**:每人格×標的 R1 抽 K=3~5 次,取方向眾數+信心中位數,並記錄「人格內分歧度」作為新訊號。成本 K 倍,且**等於改協議**——啟用前須依預登記 §8 增補登記(或作廢重登),樣本自啟用日分段。未經使用者明確決定不得擅自啟用。
   - **(選項,探索性)穩定性稽核**:對同一份凍結輸入重複 N 次 dry-run,估計各人格的方向翻轉率與信心標準差。僅作探索性參考,結果標註「不計入正式樣本」;建議在考慮多人格轉正前跑一次,讓 §8 增補的決策有數據依據。
