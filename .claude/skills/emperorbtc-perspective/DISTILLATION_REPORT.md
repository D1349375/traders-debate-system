# EmperorBTC 人格蒸餾報告

> 目的：完整記錄 EmperorBTC（`emperorbtc-perspective`）人格的蒸餾全過程、語料取得方式、判斷取捨、驗證結果與已知限制，供團隊審閱與後續維護。
> 蒸餾日期：2026-07-19 ／ 流程：女媧（huashu-nuwa）Skill 造人術 ／ 檔位：標準（語料較小，模型數收斂）
> 產物：[SKILL.md](SKILL.md) ＋ [references/research/](references/research/)

---

## 0. 一頁總結（TL;DR）

- 從 **81 支 EmperorBTC YouTube 教學/市場分析逐字稿**（語料涵蓋 **2025-03-04 ~ 2026-07-17**，0.67MB）蒸餾出交易人格。
- **語料由本 agent 自行抓取**（repo 既有的 `data/fetch_transcripts.py` + yt-dlp，非預先存在 repo）——見 §1。
- 走完女媧流程：Phase 1 抽取（4 批平行）→ 合併/三重驗證（主 agent 直接做，語料小）→ 組裝 → Phase 4 驗證。
- 產出 **5 個核心心智模型**（語料較小，少於 ICT 6/TJR 7）、9 條決策啟發式、完整表達 DNA、5 組核心張力、誠實邊界。
- **Phase 4 驗證 3/3 通過**。
- **兩個對辯論系統的高價值特點**：
  1. **crypto 原生**——他本來就以 BTC/加密為主，本系統標的 BTC/USDT 是他的主場（不像 ICT/TJR 做美股指數需對 crypto 降權）。
  2. **框架對立面**——他走 **Volume Profile / Auction Market Theory / 古典 TA** 路線（key S&R、POC、SFP，不用 order block/FVG），**且哲學上明確反對 ICT/TJR 的「機構獵殺止損／操縱」敘事**（稱之 victim mentality）。這給辯論帶來 README §3.4 想要的「真實框架分歧」，R2 交鋒有實質內容而非同源附和。

---

## 1. 語料取得（本次新增：實際跑了抓取流程）

與 ICT/TJR（逐字稿已在 repo）不同，EmperorBTC 的語料**不在 repo**，需自行抓取。流程：

1. **工具鏈確認**：repo 既有 [data/fetch_transcripts.py](../../../../data/fetch_transcripts.py)（通用、參數化 `python fetch_transcripts.py <name> <channelURL>`，用 yt-dlp 批次抓字幕→VTT→TXT）。本機 **ffmpeg 已在 PATH**、**yt-dlp 未裝**（裝進 venv）、**cookies.txt 無**（未阻礙）。
2. **語料可得性驗證（女媧 Phase 0.5 冷門人物 gate）**：用 yt-dlp 搜尋確認三個剩餘人格——
   - **EmperorBTC** ✅：官方頻道 `UCgo-DCE58uCSEQqfN4Gd97g`、82 支教學影片。
   - **GCR** ❌：Twitter/X 匿名交易者、已消失，**YouTube 無任何本人頻道**（搜尋只回無關的印度交易頻道與「Global Currency Reset」陰謀論內容）→ 無法用 YT 流程蒸餾。
   - **Mark Douglas** ⚠️：已故、他人轉傳講座＋書摘，無官方頻道，語料薄。
3. **抓取**：`fetch_transcripts.py EmperorBTC <channel>`，背景執行約 10 分鐘，成功下載 **81 支** `.txt`（無 cookies、無 bot 封鎖）。存於 `data/transcripts/EmperorBTC/`。
4. **語料特性**：0.67MB、中位數 7.6KB/檔（~3000 字，完整含 intro/outro）、**無逐支上傳日期**（yt-dlp flat 模式取不到；改用 2 次完整抽取取得頻道日期範圍 2025-03-04~2026-07-17）。

> ⚠️ **可重現**：要更新語料，重跑 `venv\Scripts\python.exe data/fetch_transcripts.py EmperorBTC https://www.youtube.com/channel/UCgo-DCE58uCSEQqfN4Gd97g/videos`（`_yt_archive.txt` 支援斷點續傳，只抓新片）。

---

## 2. 執行流程與模型分工

| 階段 | 做法 | 模型 | 產物 |
|---|---|---|---|
| 語料取得 | yt-dlp 抓 81 支字幕→txt | — | `data/transcripts/EmperorBTC/` |
| **Phase 1** 抽取 | 4 個平行 agent，各讀 ~20 支，抽心智模型/啟發式/表達DNA/案例/矛盾/背景（引用附 videoID，無日期） | Sonnet ×4 | `_raw_batch_01~04.md` |
| **Phase 1.5+2** 合併＋選型 | **主 agent 直接讀 4 份 raw batch（共 86KB）做合併＋三重驗證**（語料小，不另派合併 agent） | Opus（主） | 選型（見 §3） |
| **Phase 3** 組裝 | 照 ICT/TJR 模板逐節填入 | Opus（主） | `SKILL.md` |
| **Phase 4** 驗證 | 3 個獨立子 agent 扮演 EmperorBTC 回測試題 | Sonnet ×3 | 見 §5 |

**批次數**：81 支 / 0.67MB → **4 批**（各 ~20 支/171KB，size-greedy 平衡），遠少於 TJR 的 16 批，因語料量小。

---

## 3. Phase 2：三重驗證選型（5 個核心模型）

語料較小＋框架單一（拍賣理論為主軸），依女媧「語料較少→模型收斂 3-5 個」指引，選出 **5 個核心心智模型**：

| # | 核心模型 | 選入理由 |
|---|---|---|
| 1 | **拍賣市場理論（市場是拍賣不是獵殺）** | 全 4 批·他明確點名的框架·**內含反操縱哲學分歧**（victim mentality）→ 排他性＋辯論價值最高 |
| 2 | **成交量剖面與量價測謊（Volume-as-Lie-Detector）** | 全 4 批·他相對純 price-action/ICT 派的最大差異化工具（POC/naked POC、volume 確認） |
| 3 | **區間極值＋關鍵 S/R＋SFP＋Confluence** | 他的執行框架（range 極值、role reversal、逆勢 SFP、confluence 堆疊、Fib 只認 0.5/0.618/0.786） |
| 4 | **機率化·去情緒·if-then 系統化** | 他的認識論與紀律（percentage guesses、coder mentality、systematic>discretionary、小額風險） |
| 5 | **順勢優先＋交易/投資二分＋BTC 主導/現貨 DCA** | 趨勢與部位管理層（don't fight the trend、trade≠invest、BTC is king、DCA 只在 discount） |

**被降級/合併的候選**：反操縱敘事→併入模型1（拍賣的哲學核心）；價格分形、市場結構、premium/discount→併入模型1/3；RSI 是 regime filter→併入模型3/決策啟發式；Coinbase 溢價、機構強迫買盤→決策啟發式；alt 基本面篩選→模型5。

**與 ICT/TJR 的關鍵差異**：他用 auction/volume/古典 TA 詞彙，**完全不用 order block/FVG/draw on liquidity**；自承與 ICT「Power of Three」概念重疊但刻意保留自己的 AMT 詞彙，並反對操縱敘事。

---

## 4. 核心張力（5 組，人格深度來源）

1. **「不預設強偏見／level to level」vs 被批評騎牆**（他承認但不改）。
2. **「給具體進場/停損建議」vs「反覆免責不要盲目跟單」**。
3. **「加密市場已成熟不會再崩」vs 持續認真討論 60-70% 回撤**（他自己預告「可能會後悔說這句」）。
4. **總體看空 alt（多數像龐氏）vs 戰術上持續逐一分析佈局 alt**。
5. **穩健非賭徒的交易者形象 vs 業配自嘲「interns 的 gambling addiction」幽默**。

---

## 5. Phase 4 驗證結果（3/3 通過）

| 測試 | 內容 | 結果 |
|---|---|---|
| **反操縱立場＋語氣** | 「這根長下影是機構 draw on liquidity 獵殺止損、該抄底」你同意嗎？ | ✅ 正確表達「no one is hunting your stop losses / victim mentality」、用拍賣＋volume 重新框架、加條件式讓步（有量站穩才算 SFP）、術語正確（ICT 詞只在複述對方時用） |
| **辯論 JSON 實戰** | 餵 BTC/USDT 部分數據 | ✅ Bullish／confidence 30（低檔 rubric 正確、明確「不因 crypto 主場調高」）、未編造缺失維度（120k 明標為框架常識非數據）、格式正確 |
| **邊緣推斷** | 沒分析過的小 alt、只給漲 5%、無 volume/無 BTC 方向 | ✅ 誠實認缺 volume＋BTC 方向是地基級缺失、拒編價位、Neutral＋信心 10-15、點出 BTC is king＋alt 雙篩、區分 trade/invest |

**人格差異驗證**：同一份 BTC 數據，TJR 給 Neutral/18、EmperorBTC 給 Bullish/30——兩者都低信心但方向不同，證明人格產出有**真實差異化**（非同源附和），正是辯論系統要的訊號。

對照女媧通過標準：5 心智模型（3-7 範圍、各含局限）✅／表達 DNA 高辨識度 ✅／誠實邊界具體 ✅／內在張力 5 組 ✅／一手來源 100%（81 逐字稿）✅。

---

## 6. 已知限制

1. **語料量較小且偏近期**：81 支、16 個月（2025-03~2026-07），頻道可能刪過更早內容→心智模型收斂為 5 個，長期思想演變覆蓋有限。
2. **EmperorBTC 為匿名/卡通形象人物**：身分、真實帳戶、績效無法驗證；「我們幾乎喊中頂/底」為其自評。
3. **語料無逐支上傳日期**：時間線僅能靠內容線索粗排。
4. **crypto 原生是優勢**：BTC/USDT 是他主場、無需降權；但缺 volume 與關鍵位數據時信心仍受限（Phase 4 已驗證他會據實壓低信心）。
5. 字幕常把「Emperor」誤植為「Ember/Amber/M4BTC」，屬轉錄誤差。
6. 無 GCR 語料（見 §1）——GCR 無法用 YT 流程蒸餾。

---

## 7. 檔案清單與後續

```
.claude/skills/emperorbtc-perspective/
├── SKILL.md                      ← 人格檔（orchestrator 直接載入，persona key = "emperorbtc"）
├── DISTILLATION_REPORT.md        ← 本報告
└── references/
    ├── research/
    │   ├── _raw_batch_01~04.md            ← 4 批原始抽取
    │   └── _batch_manifest_01~04.txt      ← 4 批分批清單
    └── sources/transcripts/       ← 空（逐字稿在 data/transcripts/EmperorBTC/）
```

**後續決策（留給團隊）**：
1. **是否納入生效人格**：EmperorBTC 是 crypto 原生、與 ICT/TJR 框架對立，非常適合 BTC 辯論。納入需在第一筆紀錄前更新 `preregistration_DRAFT.md` §1 為多人格。
2. **GCR**：YT 無語料，無法蒸餾；如要做需其 Twitter/X 文字存檔（純本地語料模式），否則維持不做。
3. **Mark Douglas**：語料薄（無官方頻道），若要做需先確認可用的講座/書籍文字來源。

---

> 本報告與 SKILL.md 由女媧流程蒸餾產出；語料以 repo 內 `data/fetch_transcripts.py`（yt-dlp）自行抓取，調研留存於 `references/research/`。
