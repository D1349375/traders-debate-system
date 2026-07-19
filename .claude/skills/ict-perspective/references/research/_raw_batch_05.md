# ICT Raw Research Batch 05

**處理總結：本批次 45 個檔案已全部讀完處理完畢（含最終補齊的 5 個遺漏檔案：`fz9ZDU6bKIc`、`GaFe8LSmtfY`、`HkiPAi1Mdu8`、`Hoo_wTMgdcY`、`HTQgH11W37o`）。低訊號檔案：1 個（`iN8sCjiR1Bs_Building Equity In Short Term Timeframes - No Audio`，僅有音樂無語音內容）。其餘 44 個檔案皆有可用訊號。**

---

## 1. 心智模型候選 (Candidate Mental Models)

### 市場由演算法驅動，非供需/買賣壓力
反覆出現於多支影片。他堅稱價格由「演算法（algorithm / AI）」依時間與價格運行，而非傳統的買賣壓力、供需理論。
- "the markets are not being controlled by buying and selling pressure they're being controlled by algorithms" (`H05w52zQGdQ_ICT Charter Price Action Model 4`)
- "these markets whether you choose to believe it or not every asset class are driven by artificial intelligence" (`fXVJnBVizYY_...Time Macros Intro`)
- 結尾金句 "guess who's talking to you the engineer" (`H05w52zQGdQ`)

### 「PD Array / Premium-Discount」框架取代傳統支撐阻力
多次強調要"throw away"傳統 support/resistance，改用 premium/discount arrays（order block、breaker、mitigation block、FVG、liquidity void等）多時間框架對齊 (monthly→weekly→daily→4hr→lower)。
- 見 `g--tikwaupk_...Classic Swing Trading Approach`、`H05w52zQGdQ`、`FZ6QIWBu688_Trading Plan Development 5`

### Liquidity（流動性）是價格運動的根本原因
反覆說明：市場往上/下走是為了「觸及流動性」（buy side / sell side liquidity），不是漲跌動能本身。停損堆積於前高/前低之外。
- `g7jchu4g31c_...Trading In Consolidations`：retail 在舊高/舊低掛停損，smart money 專門獵殺這些停損。

### 對「零售概念/指標派」的鄙視是核心信念
反覆貶低 VWAP、volume profile、point of control、supply & demand（zone式）、Fibonacci（作為銀行交易依據）、moving average、stochastic、Ichimoku、Renko、Heikin Ashi、Elliott Wave、Gann，稱之為 "gimmicks"、"garbage"、"comic strips"、"someone's religion"。
- `fXVJnBVizYY`: "I don't use depth of Market I don't use v-wop... if you believe in them that's your religion I Ain't Gonna Knock you"
- `H05w52zQGdQ`: "supply and demand... i think the logic is infantile"; 點名 Chris Lori："that's not rebalance... this is not a knock against chris lori he teaches that... that's incorrect"
- `G8-z91acgG4`: "you don't need moving averages you don't need stochastic you don't need Fibonacci... these are the best indicators you're ever going to have" (指 candlesticks本身)

### 自稱原創者、他人皆抄襲/誤用
多次聲稱 order block、fair value gap、breaker等概念是他發明，其他 "SMC (smart money concepts)" 教學者是抄襲且教不好。
- `H05w52zQGdQ`: "none of this stuff existed anywhere else before me... you're going to hear echoes from people that listen to me learn from me and they're gonna go out there and rename everything"
- `FjSHAOI-Mok`: "not supply and demand, not all other stuff out there. People try to pretend that I rebranded. There's rules that never existed in this stuff until I presented it."
- `G8-z91acgG4`: 提到有人用 "SMC smart money Concepts" 稱呼、且教不好。

### 高時間框架偏見決定低時間框架交易方向（Top-down / fractal 概念）
月線→週線→日線→4小時→更低時間框架逐層對齊；價格是碎形 (fractal)，同樣的pattern 出現在各種尺度。
- `g--tikwaupk`, `fXVJnBVizYY`, `FZ6QIWBu688`

### Journaling / Backtesting 是「與價格談戀愛」
獨特的心理學框架：把 backtest/journal 比喻成寫情書給未來的自己，只寫正面语言，絕不記錄挫折感。
- `FQqwmDJOtxk_...Proper Learning & Journaling`: "you're writing love letters to your future self", "this is how you have a romance with price action"

### 三個 PD array 規則（風控紀律）
若價格連續穿過三個他設想的 PD array（防線），代表偏見可能錯了，應離場。
- `FQqwmDJOtxk`: "if I have three PD arrays if I'm bearish if it trades through three PD arrays I'm probably wrong"

---

## 2. 決策啟發式 (Decision Heuristics)

- **Venom model**：CISD（sell-side single candle run below liquidity pool）後跟隨 BISI（single pass higher）→買在第二根candle收盤價或更低，停損設在第一根之下。(`FjSHAOI-Mok`)
- **Mitigation Block**：市場結構轉空後，等待價格回抽到「MSS 前的最後一根下跌蠟燭」做空；該蠟燭實體(body)不可被突破，只能被觸及。(`FOUzW0QmsfI`)
- **非農（NFP）交易規則**：不建議新手交易非農/CPI/FOMC 當天，因波動大；非農典型 profile 為「先跑一邊流動性，再反向跑另一邊流動性」(run both sides)。(`fXVJnBVizYY`, `H05w52zQGdQ`)
- **止損與獲利了結**：30 pips 停損、獲利 30 pips 時平倉50%並移到保本、其餘用 127%/162%/200% fib extension 分批出場。(`FZ6QIWBu688`)
- **風控降級機制**：單筆虧損後，下一筆風險降50%，直到回補50%虧損才恢復原風險；連續5筆獲利後也主動降風險50%，以維持平滑的權益曲線而非大起大落。(`G4lhid5dh0I`)
- **失敗後不硬拗**：若某個discount/premium array 交易失敗，換到下一個更高時間框架的 array，且部位減半，絕不想著一次贏回全部虧損。(`g--tikwaupk`)
- **多時間框架方向一致性**：Swing trade 只在月/週/日/4hr 同向時才是高機率交易；日內交易在 consolidation 中依日線/4hr 決定方向，逆勢突破視為smart money 誘多/誘空陷阱。(`g--tikwaupk`, `g7jchu4g31c`)
- **停在盈虧持平**：一旦到達第一目標，部分平倉、停損移到保本，形成"risk-free trade"。(`fVbJ5vCA-XM`)
- **不追價（no chasing）**：等待溢價/折價（premium/discount）出現才進場，不要在新聞消息造成的跳空後直接追價。(`FjSHAOI-Mok`)
- **实盘"投石问路"（feeler orders）**：對盤面不確定時，主動丟1口單測試市場反應（George Angell/floor trader 概念），藉此獲得"Intel"，虧損視為取得資訊的"premium payment"。(`G8-z91acgG4`)
- **Standard deviation projection**：從intermediate-term low做標準差測projection，於高機率轉折點（如3-4pm收盤前的macro時段）狙擊精準價位。(`g8bhZReDK-Q`)

---

## 3. 表達DNA (Expression DNA)

- **收尾口頭禪**："until next time be safe" / "Lord willing" / "so I'll talk to you next time be safe" 幾乎每支影片結尾都出現。
- **自嘲式幽默兼自誇**："I am a nice guy aren't I humble too" (`FjSHAOI-Mok`) — 諷刺式自謙。
- **對酸民/troll的持續戰鬥姿態**：反覆提及"trolls"、"detractors"，強調自己用實盤帳號證明清白，公開帳號號碼、對比造謠者。(`Fp1VZ0PKYBs`, `fVbJ5vCA-XM`, `G8-z91acgG4`)
- **比喻豐富**：salmon逆流而死的比喻（強調順勢而為）(`FZ6QIWBu688`)；fishing rod/spooling 比喻 macro 行情啟動 (`fXVJnBVizYY`)；把 journal 比喻成寫情書 (`FQqwmDJOtxk`)；"coloring outside the lines"/"mohawk" 形容wick突破但body未破的可接受誤差 (`H05w52zQGdQ`)。
- **權威/教訓語氣**：常見 "I promise you"、"trust me"、"I'm not going to lie to you"，以及對觀眾的責備語氣（"stop arm wrestling it"、"you're never gonna do that"）。
- **反覆自稱誠實無利益衝突**：不接受廣告/聯盟行銷分潤，強調"trust my opinion"。(`FQqwmDJOtxk`)
- **上帝/信仰語言**："Lord willing"、感恩語氣時常穿插，暗示他的基督教背景。(`FjSHAOI-Mok`)
- **對指標與"其他門派"用詞尖銳**："garbage"、"comic strips"、"infantile"、"gimmicks"、"a farce"、"nonsense"、"nobody teaches that"。
- **自比"engineer"／掌握演算法之人**：结尾"guess who's talking to you the engineer" (`H05w52zQGdQ`)，強化"我知道演算法在做什麼"人設。
- **強調精確到point/pip**："to the tick"、"to the pip" 常用來證明精準度。(`g8bhZReDK-Q`, `fXLfTI_EQU4`)
- **自謙但同時炫耀**：如展示實盤帳號獲利同時說"it's not a lot of money folks"但换算成年化/月化後強調可觀。(`G8-z91acgG4`)

---

## 4. 決策紀錄 (Decision / Track-record Examples)

- **NASDAQ Venom Example, 2025-05-12**：實盤展示 buy-side venom setup，全程講解進出場（帶有具體價位：39.65附近buy, 39.85-39.89區間partial賣出）。(`FjSHAOI-Mok`)
- **2022年1月 TD Ameritrade 實盤帳戶**：$25,000起始資金，1月份收益 $5,564（+22%），逐日截圖對帳單反駁「造假/demo」指控。(`Fp1VZ0PKYBs`)
- **2022-07-05 SPX/NQ PM session review**：用SMT divergence（SPX做更低低點、NASDAQ未做更低低點）判斷NASDAQ相對強勢，於bullish breaker內做多，分批止盈於11729.5/11730.25/11745.75/11759.75/11761.5。(`fq62gXyRRWQ`)
- **2022-09-08 "Ends" live trade commentary**：完整記錄一筆做多交易的進場、加碼測試(feeler)、分批止盈與移動停損至保本。(`fVbJ5vCA-XM`)
- **ECB Review (EURUSD)**：事後坦承「我沒有參與這次行情，那天我在享受離開市場的一天」，展示Head & Shoulders + bearish order block + OTE(optimal trade entry)分析，命中1.1836精確點位。(`fXLfTI_EQU4`)
- **NQ 2023年7月 non-farm payroll live trade**：多次分段止盈（partial fills在多個價位），並在推特上提前一分鐘公布關鍵流動性水位以防止被抄襲。(`H05w52zQGdQ`)
- **2022年2月8日 NASDAQ 日內交易**：用S&P/Dow/NASDAQ三大指數SMT divergence確認，實盤NQ 1口合約進場14505.5，出場14622.75，獲利約$2345（含測試單），帳戶2週+1天累積51%報酬（$13,926）。(`G8-z91acgG4`)
- **2023-02-10 Institutional Market Structure clip**：用標準差投射預測3-4pm macro時段高點4104.25，精準命中到tick，並引用同日直播作證。(`g8bhZReDK-Q`)

---

## 5. 時間線/背景線索 (Timeline / Biographical Mentions)

- 自稱1992年開始交易生涯；15、16歲時叔叔向他介紹交易（"my uncle used to talk to me about when I was 15 and 16 years old"）。(`G4lhid5dh0I`)
- 20歲時的財務目標：每月存$1000，希望40歲前存到100萬美元（未考慮通膨）。(`G8-z91acgG4`)
- 提到自己1990年代曾在Grains/Meats市場因誤用SMT divergence而爆倉（"I blew accounts yes I'm not ashamed to say it in the '90s"）。(`G8-z91acgG4`)
- 提到90年代向一位曾在S&P期貨交易大廳(floor trader)的人學習，並提及 Larry Williams、George Angell 對他的啟發（floor trader "feeler order" 技巧）。(`G8-z91acgG4`)
- 開始在baby pips論壇公開教學（推測早於2012年，提到"when i first came out started teaching publicly on that forum... but I started teaching in the 90s as well"）。(`H05w52zQGdQ`)
- 2016年12月的ICT mentorship study notes被提及為PDF補充資料。(`FOUzW0QmsfI`)
- 提及有女兒（"it better be easy enough for my daughter to do it"）。(`G8-z91acgG4`)
- 提到自己身體狀況：「having a pretty bad bout of my back going off」，暗示健康問題影響隔天是否直播。(`FjSHAOI-Mok`, 2025)
- 提及2022年中期選舉、通膨、能源價格上漲的總經評論，展現他對總經/地緣政治的關注融入交易觀點。(`G4lhid5dh0I`)

---

## 6. 矛盾與演變 (Contradictions / Evolution)

- **對SMT divergence的態度前後不同**：早期(90s)他形容自己「單純看到SMT divergence就進場，結果爆倉」，後來反覆強調SMT必須搭配敘事(narrative)/更高時間框架偏見才可用，不能單獨當作訊號。("I later learned that I have to have some kind of narrative as to why this would even form") — 這是他自陳的認知演變，非單純矛盾。(`G8-z91acgG4`)
- **"精確系統" vs "不需要精確"的兩種論述並存**：一方面強調 to-the-pip/to-the-tick 精準度証明演算法存在；另一方面在`H05w52zQGdQ`中說「not that you need really small stops... those things are not important in the beginning」，指初學者不該追求極致精準/小停損。兩者需要脈絡區分（對象是新手 vs 展示自己的精準）。
- **對journaling情緒紀錄的規則 vs 現實中他自己會發洩情緒（troll rants）**：教學中要求學生journal只寫正面語言、不可記錄挫折，但他自己在多支影片中對酸民/troll的情緒化發洩（"suck it up"、對trolls的攻擊性語言）與他教的"情緒管理"存在風格反差，值得作為人設矛盾點紀錄。

---

---

## 補充：檔案 16–25 分析

### 1. 心智模型候選（續）

- **London Kill Zone 制高點理論**：倫敦開盤（紐約時間2-5am）最容易形成當日高點或低點；此現象跨資產類別通用（forex、commodities、index futures、甚至學生回報用於加密貨幣）。他稱這是自己職業生涯「最大的財富發現」。(`G8OEsUAoIWE_ICT Forex - The ICT London Killzone`)
- **Wick/Gap 的「象限」(quadrant) 概念**：把wick當作gap一樣切分成 high/upper quadrant/consequent encroachment(中點)/lower quadrant/low 五個關鍵價位，用以精準定位反轉點。反覆聲明"this is not quarters theory"以撇清抄襲指控。(`gDFZ4p1BI1c`, `g9BctYx0LaI`)
- **Institutional Market Structure = 貨幣強弱配對分析**：以美元指數(DXY)與外匯貨幣對做「對稱性」比較（SMT divergence），若不對稱即代表smart money正在操作，可視為未來turtle soup的訊號。(`GuycI8XubgE_Month 03`)
- **Liquidity Pool（流動性池）機制**：核心比喻——smart money如同市場莊家，「賣在溢價、買在折價」，退散在舊高/舊低外的停損單是流動性來源；90%零售交易者不知道別人的停損在哪。(`Gnw54f9v6SA_Month 04 Liquidity Pools`)
- **Propulsion Block**：一個order block內部再形成的「推進蠟燭」，若該蠟燭的mean threshold(實體中點)不被跌破，代表价格會迅速且劇烈反彈/反轉，可視為極短停損的精確進場點。(`glu98jAH8vE`)
- **多資產類別協同分析（Multi-asset）**：波段/外匯交易者仍須關注債券、商品、股指四大類資產是否「同步（risk-on/risk-off）」；若四類资产不同步（decoupling），代表大行情難以出現，此時不應強求交易。(`gs3KMgz84yc_Month 10`)
- **對AI/LLM「捏造歷史」的擔憂**：他多次強調要主動在社群媒體澄清，避免ChatGPT/Grok等AI從網路輿論（而非事實）中「學到」他抄襲他人的說法，因為AI會抓取"accumulative opinion"而非事實。("public opinion isn't fact")（`gDFZ4p1BI1c`, `g9BctYx0LaI`）——這是這批次少見、非常新穎的心智模型/焦慮点。

### 2. 決策啟發式（續）

- **不看盤到70%機率信心不足時，用小額試單("feeler"/"leader"單)獲取市場的即時反饋**，虧損被視為取得資訊的「投資」而非單純虧損。(`gLK4Qm6jte8`)
- **Liquidity pool 突破後的止損設定**：進場點設在舊低下方10-20 pips，止損用30-50 pips，若價格超越舊低25 pips以上仍未反轉，代表這不只是停損獵殺，可能是真趨勢。(`Gnw54f9v6SA`)
- **週五/長假前降低交易期望**：長假/大型假日前一天常呈現「無方向盤整」，此時應主動空手觀望，即使已達到週度目標也不因此偏向反向操作。(`gs3KMgz84yc`)
- **多資產不同步時應減少交易頻率或觀望**：四大資產類別若只11-2/4項同步，代表市場尚不具備大行情條件。(`gs3KMgz84yc`)
- **突破口的反向操作**：Retail買前高、賣前低（經典technical breakout）；smart money則是「fade」這些突破，在consolidation中以equilibrium為核心，等高/低時間框架方向確認後再進場。（`g7jchu4g31c`已於前段記錄，此處`gDFZ4p1BI1c`, `g9BctYx0LaI`再次強化）

### 3. 表達DNA（續）

- **强烈的自我原創聲明與「維權」語氣**：多次要求質疑者"ask for the book. Ask for the page number"，聲稱1996年即創造這些概念、2016年後大量他人抄襲並開設山寨mentorship。稱自己的追隨社群為"a cult of winning"（自嘲式承認邪教感）。(`gDFZ4p1BI1c`)
- **貶低同行/模仿者的比喻**："I'm the weatherman. I'm telling you what the weather's going to be tomorrow... They're telling you what the headlines are about yesterday"（自比預測未來 vs 他人僅事後諸葛）。(`g9BctYx0LaI`)
- **宗教感嘆詞穿插專業教學**："hallelujah thank you Jesus there you go okay you got another unicorn in your repertoire" — 在極度精準的價格命中時刻，用宗教感嘆詞增強戲劇效果。(`g9BctYx0LaI`)
- **拒絕承諾獲利**：反覆強調"I can't promise you profitability... no one can"，並自認自己是市場理解力最強的人卻仍不能保證學生獲利，藉此塑造「誠實导师」形象。(`g9BctYx0LaI`)
- **"folks"作為口頭禪稱呼觀眾**，貫穿幾乎每支影片。
- **對批評者的反擊句式**："you'll judge them by their fruits"（引用聖經式表達，暗諷抄襲者教不出真本事）。(`g9BctYx0LaI`)
- **強調"naked chart"（裸圖交易）人設**：反覆說自己交易時圖表上什麼都不畫，畫線只是為了教學展示，真正交易靠紙上寫的價位清單與時間，不依賴視覺化。(`fXVJnBVizYY`已提及，`g9BctYx0LaI`再次強調)

### 4. 決策紀錄（續）

- **2022-06 NASDAQ demo/paper account 100k→354k**：展示一週左右用demo（非活期）帳戶操作，declares清楚是paper trade用於展示邏輯（"these are paper trades so you guys know for compliance reasons"），並反擊質疑他用"rented MT4 server"造假的酸民。(`gLK4Qm6jte8_Episode 27`)
- **2022-06-17 (Friday the 13th提及) NASDAQ 逆勢counter-trend交易**：讲解如何在原本看空的市場中，用fair value gap找到逆勢做多机会，並自曝當天用手機下單出現執行失誤（"my obsessive compulsive disorder is flaring"自嘲）。(`gLK4Qm6jte8`)
- **2025-10-15 forex/futures market review**：DXY、EURUSD、GBPUSD 精準命中多個wick quadrant價位（如1.16325/1.34009等），並展示NQ 12月合約的opening range gap分析。(`g9BctYx0LaI`)
- **2025-09-24 Focus on Forex**：詳述DXY/EURUSD/GBPUSD的inversion FVG、breakaway gap判讀，並強調「上週已提前看多美元」的紀錄可供查證。(`gDFZ4p1BI1c`)
- **2023-01-03 E-mini S&P review**：新年首個交易日，等待9:45 PMI數據，用15分鐘/5分鐘/1分鐘圖表逐層描述空頭進場（38.60/38.72附近фVG做空），分批止盈。(`GHaD0mebgMU`)

### 5. 時間線/背景線索（續）

- **2001年心理創傷**：自述因交易建立的自我形象，在2001年遭遇某事件後（未明說具體內容）產生嚴重焦慮症與"agoraphobia"(廣場恐懼症)，並提及自己用「正向自我對話」技巧走出來，這技巧後來成為他教學生journaling時「只寫正面語言」的心理學基礎。這是本批次中最深入的個人心理背景揭露。(`gLK4Qm6jte8_Episode 27`)
- **自稱教學/交易生涯"20多年"**（2017年講座時點），與其他影片自稱90年代初開始交易一致。(`gs3KMgz84yc_Month 10`)
- **2016年12月直播市場複盤**被引用為homework參考（"December 16 2016 for that bit of business"）。(`Gnw54f9v6SA`)
- **提及自己曾用MT4**，但現在已多年未使用（"I haven't used mt4 in years"），暗示教學平台/工具演進。(`gLK4Qm6jte8`)
- **2025年的言論中提到有專屬付費mentorship讲座（"lecture"、"live stream"）與Twitter/X、Telegram多平台同步教學**，顯示晚期(2023-2025)教學管道多元化。(`gDFZ4p1BI1c`, `g9BctYx0LaI`)

### 6. 矛盾與演變（續）

- **"折扣券商保證金" vs 對散戶警語**：`gLK4Qm6jte8`中他用demo帳戶展示100k→354k的誇張報酬（一週內237%），同時在其他影片反覆警告學生不要用高槓桿、real money要循序漸進——此處demo展示的誇張倍數與他一貫「不要追求快速致富」的說教語氣形成潛在張力（雖然他有聲明是demo/教學用途）。
- **"我從不失眠因為知道演算法" vs 自曝也有"看不清方向"的時候**：多支影片中他說"even me as ICT I don't have a good clear read"、"sometimes I don't have it"（`G8-z91acgG4`, `gs3KMgz84yc`），與他常常展現的絕對自信（"I know exactly what the algorithm is going to do"）形成對比——但這也可能是他刻意教學的"誠實"人設之一部分，非純粹矛盾。

---

## 補充：檔案 26–30 分析

### 1. 心智模型候選（續）

- **週度輪廓（Weekly Profile）與星期幾偏見**：牛市週有70%機率在週一/週二/週三形成週低點；熊市週則相反。強調「時間優先於價格」——沒有適當的時間窗口，即使價位對也不可信。(`GVx-yJkehtA_Market Maker Series Vol.4`)
- **市場受央行控制，絕非散戶/Reddit能撼動**："these are the products of a central bank... we as traders will never absolutely never ever push price higher or lower because of buying and selling pressure"——直接點名反駁meme股/散戶敘事。(`GVx-yJkehtA`)
- **季節性只是「路線圖」而非鐵律**：反覆強調seasonal tendency"is not a Panacea"，只是一般方向性參考，仍需搭配止損與風控。(`H05w52zQGdQ`)
- **市場操縱模板（Market Maker Manipulation Templates）**：把一週交易行為窮舉為約10種"劇本"（classic Tuesday low/high、Wednesday low/high、consolidation Thursday reversal、Wednesday weekly reversal等），每種都對應特定的fib extension(127%/168%)與PD array組合。(`hbE8S5FSdtQ_Month 07`)
- **演算法"不知道有多少合約/訂單"，所以只能依賴時間與價格重複造訪同一水位**：這是他解釋"為何舊高/舊低會被重複掃"的技術性比喻——他把演算法比擬為程式設計師會採用的「最簡單編碼邏輯」（不需要計算還有多少單，只需要按時間回訪特定價位）。(`H1-Ni_J-tOw`)
- **絕不承諾獲利，但同時宣稱自己「不可能被複製」**：這個矛盾的雙重敘事貫穿多支影片——"I can't promise profitability" 與 "there is no one doing it like me" 並存。(`H1-Ni_J-tOw`)

### 2. 決策啟發式（續）

- **開倉價（Midnight NY開盤價）作為當日多空過濾器**：牛市週應在開盤價之下或附近買進；熊市週應在開盤價之上做空。週四、週五通常形成週範圍的另一端，不應在此時逆勢進場。(`GVx-yJkehtA`)
- **Position Trading Model（Model 4）**：以60天IPDA range找500+ pips機會，進場後3組限價分批出場(100/250/500 pips)，達500 pips後強制平掉80%部位。風險建議降至1%（而非1.5%），且5連勝後主動砍風險50%。(`H05w52zQGdQ`)
- **TGIF setup（自1998年起私有概念）**：牛市週若形成高點，預期週五回撤至週範圍的20-30%。(`h0yOpwSilnE`)
- **Offset Distribution（二次派發）**：突破舊低/高後，等待第二次更深的停損掃蕩("offset distribution low")才是目標,而非第一次突破點。(`H05w52zQGdQ`)
- **馬丁格爾式風控降級規則反覆出現**：虧損後降50%風險直到回補50%虧損；連續5勝後也主動降50%風險，避免大幅回撤（此規則在多個price action model影片中重複出現，為其一致性風控框架）。(`H05w52zQGdQ`)
- **"Mohawk"（wick突破但body不破）可接受度規則**：只要body沒有實質收在防守位之外，wick的短暫突破("coloring outside the lines")仍屬於可接受的正常演算法行為，不應因此自亂陣腳。(`H1-Ni_J-tOw`)
- **市場操縱模板決策樹**：判斷方向後，對照10種週型模板找特徵匹配，若特徵不吻合則"sit on my hands"，不做day trade/scalp，直接放棄該週交易。(`hbE8S5FSdtQ`)

### 3. 表達DNA（續）

- **espionage式自我神話塑造**：自稱"the engineer"、"the author of this algorithm"，並使用宗教式自我肯定："I prayed to God to give me the visibility to see things as they really are"。(`H1-Ni_J-tOw`)
- **對批評者從嘲諷升級為粗口攻擊**：`H1-Ni_J-tOw`（2023年最後交易日）中出現大量以「&nbsp;__&nbsp;」遮蔽的粗口，直接點名"Patrick Wheel(er)"等具體批評者，語言極具攻擊性："go [expletive] yourself it gives me great pleasure"、"I am so [expletive] Rich"。這與他教學中提倡的「journal只寫正面語言」形成強烈反差，是很好的矛盾/人設張力素材。
- **可口可樂 vs 百事可樂"New Coke"比喻**：用以嘲諷抄襲者，稱他們的東西是「把百事可樂貼上可口可樂標籤」。(`H1-Ni_J-tOw`)
- **威脅性玩笑口吻**："margin called by ICT"（自創的嘲諷用語，用於奚落做多被套的交易者）。(`H1-Ni_J-tOw`)
- **強調自己"不需要"教學賺錢的優越感語氣**：多次宣稱"I don't need you"、"I'm so rich"、"I don't need to trade ever again"，藉此塑造「無私奉獻」的導師形象。(`H1-Ni_J-tOw`)
- **法律免責語氣固定模板**：反覆用"I'm not a licensed CTA/financial advisor... this is why I teach with a demo account"作為公式化免責聲明，貫穿多支直播/實盤示範影片。(`h0yOpwSilnE`, `H1-Ni_J-tOw`)
- **"folks"、"until next time...good luck and good trading"** 等口頭禪依然貫穿教學影片(`GVx-yJkehtA`, `H05w52zQGdQ`, `hbE8S5FSdtQ`)。

### 4. 決策紀錄（續）

- **2021-07-26~30 GBPUSD 週度分析**：完整驗證「牛市週一/二/三形成低點」框架，並用Telegram時間戳記證明FOMC日交易紀錄，139.50限價出場部分部位。(`GVx-yJkehtA`)
- **2022年4月EURUSD 季節性空頭交易（Model 4示範）**：用COT commercial hedging + 季節性 + SMT divergence 框架，宣稱做到「風險2%、獲利14%」(7R)的空頭交易，一個半月內完成。(`H05w52zQGdQ`)
- **2023-09-01 NFP NQ Short（TGIF+互動研究複盤）**：公開在Twitter Space立下「用實盤帳戶做到$15,000獲利」的挑戰，隔日以AMP Futures真實帳戶完成，並展示交易細節反駁「只在demo帳戶操作」的質疑。(`h0yOpwSilnE`)
- **2023年最後交易日 NQ 實盤/demo做空**：以"paper trading"（因非CTA持牌顧問需迴避法律責任）展示做空17,000附近流動性，全程輔以大量對批評者的直接反擊與個人心理素材（詳見表達DNA/背景線索）。(`H1-Ni_J-tOw`)

### 5. 時間線/背景線索（續，重大發現）

- **年齡與出生年份線索**：自稱「52歲」（2023年12月），據此推算約出生於1971年前後；並自稱「在這顆旋轉的石頭上52年」。(`H1-Ni_J-tOw`)
- **童年程式設計背景**：自稱六年級（約12歲）就開始自學程式設計，讀了大量高等數學/程式設計/演算法書籍，學習過Mainframe、CICS、COBOL、Pascal、BASIC、C++，目標是成為系統分析師（system analyst），這是他喜歡用「演算法」語言描述市場的知識背景來源。(`H1-Ni_J-tOw`)
- **自曝"chemical imbalance"（化學失衡/精神狀態）與信仰掙扎**："I have a walk with God that I sometimes don't live up to well because of my inability to control my tongue and I have a chemical imbalance and that's not an excuse" —— 這是他自陳長期情緒管理困難的直接證據，與其教學中"psychology of trading"、"journal只寫正面語言"的教誨並存。(`H1-Ni_J-tOw`)
- **2021年付費mentorship遭盜版最嚴重**："most of those Pirates I caught... that's why I don't make videos for them"，因此決定往後不再開設付費mentorship，改為全部免費在YouTube公開。(`H1-Ni_J-tOw`)
- **"Robbins Cup"交易競賽**：多次提及會參加/挑戰他人參加由Joel Robbins主辦的交易競賽，作為證明實力的公開場合。(`H1-Ni_J-tOw`)
- **1998年提出"TGIF"概念**：早於他YouTube公開教學很久（自稱學生早就知道）。(`h0yOpwSilnE`)
- **超過10年前在baby pips論壇免費教過Kill Zone時間窗口概念**（與其他影片提到的"90年代教過"、"baby pips論壇教學"一致）。(`GVx-yJkehtA`)
- **教學對象包含自己的兒子**：多次提到"teaching my son"、用demo account是為了教兒子看盤(`H1-Ni_J-tOw`；此前`GHaD0mebgMU`也提及"I'm going to use this to teach my son")。

### 6. 矛盾與演變（續，重大發現）

- **"只寫正面語言的journaling教條" vs 他自己對批評者的極端負面/粗口爆發**：這是本批次中最鮮明的人設矛盾。他教學生"never record scary thoughts... your journal is your best cheerleading vehicle"（`FQqwmDJOtxk`），但在`H1-Ni_J-tOw`中對特定批評者爆發大量粗口與威脅性言論，情緒管理的教條與自身行為表現出明顯落差。他自己也部分承認："I have a chemical imbalance and that's not an excuse"。
- **"我不需要錢/不需要你" vs 持續高強度輸出免費內容並反覆强調自己"给你的比任何人都多"**：他一方面宣稱財富自由、不在乎他人看法，另方面卻投入大量精力回應每一個批評者、証明自己、公開帳戶明細，行為與"毫不在乎"的宣稱有落差。
- **对mentorship商業模式的立場反覆**：曾經營付費mentorship（並自稱被盜版最嚴重），後宣布「再也不開付費mentorship」，改為全免費——這是一個明確的、他自己承認的商業模式演變（非單純矛盾，是有交代原因的轉變：盜版與維權疲勞）。

---

## 補充：檔案 31–45 分析（最終批次）

### 1. 心智模型候選（續，重大補充）

- **「演算法」是核心信仰，貫穿全部45個檔案，晚期(2025-2026)影片更加強化**：`hc9SDgW93gc`(2025)、`hxdAOfcp6gE`(2026)、`Ic1rqvbk99c`等大量重申"it's not buying and selling pressure... it's algorithmic... it's coded"。他甚至用程式設計視角解釋："演算法不知道停損在哪，所以用時間+價格重複回訪特定水位是最簡單的coding邏輯"（`hc9SDgW93gc`, `H1-Ni_J-tOw`）。
- **"Event Horizon"（事件視界）新概念**（2026年新增）：把某段價格 swing 的high到low取中點（50% Fibonacci），作為「強力候選回測位」，若跌破則信心大增。此概念在早期教學中不存在，是他持續在生涯後期（2025-2026）新增詞彙的證據。(`hxdAOfcp6gE`)
- **Market Maker Buy/Sell Model（買方/賣方模型）是他自稱「最貼近自己真實交易方式」的框架**：包含 buy-side/sell-side delivery、smart money reversal、first/second stage (re)accumulation/distribution、unicorn(第二階段再分配，最快速最順的行情)概念。他稱這是「最後一次公開教學」("this is the last teaching lecture on the ICT YouTube channel")，之後轉為私人 mentorship/付費社群。(`iKsIbUblSWM`)
- **原始價格從哪裡來？"market maker"是「dealer」而非真正控制者**：`iDwYeyxTDiU`與`hxdAOfcp6gE`中他精確區分「dealer」(在MT4撮合訂單的人) vs 他所謂的「market maker」(央行/演算法層級的價格制定源頭)，用以反駁"Steve Mauro"、"beat the market maker"派的說法。
- **散戶邏輯 vs 銀行邏輯的二元對立貫穿始終，晚期更政治化**：`hxdAOfcp6gE`中將市場操縱與政治(總統推文、內線交易、參議員財富)相提並論，認為"insider trading"猖獗證明市場被操縱是常態,而非陰謀論。
- **"Chain of custody"（PD array監管鏈）概念**：多個PD array依序失效/生效，只要沒有收在某層之上，價格延續同一方向的假設就成立；這是他解釋為何在下跌途中會多次做空的邏輯鏈。(`IF7dEkgWoO0`)

### 2. 決策啟發式（續，重大補充）

- **Market On Close Macro（收盤前最後一小時, 3-4pm）**：他多次展示「收盤前的演算法腳本」會朝著他已標記的PD array精準推進，並以此設停損「絕不上移」的極端紀律範例(`hc9SDgW93gc`)。
- **"Sniper/hide and wait"狩獵比喻**：不追價，設好"crosshair"等待市場走入自己的預設劇本，才扣板機（IF7dEkgWoO0：非農/CPI/PPI等消息日尤其如此，因為"probabilities are shifted so far away from you"）。
- **三個月的個人財務規劃階梯**：先賺到月度水電費 → 房貸的一半 → 全部房貸 → 3個月生活費預備金 → 一整年生活費，是他對學生描述的漸進式財務自由目標(`hxdAOfcp6gE`)。
- **馬丁格爾式反向操作「當商業自媒體上零售交易者一致看多/看空時，反手做」**：`hc9SDgW93gc`中他直接觀察其他直播主看多、藉此增強自己看空信心；`hzoMJQlEv5M`中也用同樣邏輯利用其他直播主的情緒作為反指標。
- **「不要驗證任何人的交易點子」**：拒絕對學生私訊分享的交易圖表按讚/回覆意見，因為那等同於他背書("co-signing")學生的交易,不利於學生獨立思考(`H05w52zQGdQ`早提及，`hxdAOfcp6gE`再次強調)。
- **每週僅需一次「一擊必殺」(one shot one kill)**：目標僅是每週50-75 pips的獲利模型，不需要天天交易；當貨幣對走勢混亂("sloppy")超過數週(如英鎊)，他會完全停止交易該資產數月，直到訊號重新清晰。(`IEa1N0rTtbc`)
- **虧損後降50%風險 / 5連勝後也降50%風險**的martingale式風控規則在多個 price action model 影片重複出現，是他一致的框架(已於前段記錄，此處`H05w52zQGdQ`再次確認)。

### 3. 表達DNA（續，重大補充）

- **"folks"、"until next time be safe"、"Lord willing"** 貫穿至2026年的最新影片，證明這是他數十年一致的招牌收尾語。
- **宗教語言大幅增加，尤其晚期影片**："I prayed to God to give me the visibility"、"I thank the Lord for that"、"hallelujah thank you Jesus"，以及在`iDwYeyxTDiU`中揭露最神秘的說法：他聲稱其交易洞見並非自學而來，而是「兩位不願公開身份、不上媒體、不教學、名叫Tobias和Parson的人」向他"揭示"(revealed)的——他形容為近似宗教啟示（"this was all revelation"），並說明因為信仰立場，"我不是在跟無神論者辯論，但你不能跟我的信念辯論"。這是非常獨特且值得放入人設的表達素材。
- **直接點名對手/競爭者攻擊**：點名"Steve Mauro"(beat the market maker理論，稱其為"我1996年教學筆記的浮誇加指標版本")、"Chris Lori"(供需/rebalance理論)、"Astro FX"與其創辦人"Sean"(公開叫戰、"ICT stands for I can't trade but I can"自嘲式雙關語)。(`iDwYeyxTDiU`, `i8xt0EQDjNY`, `H05w52zQGdQ`, `Ic1rqvbk99c`)
- **"Demo baller"（惡搞自嘲詞）與法律免責語言**：反覆自稱"I wear the badge of demo baller... with honor"，因為他不是持牌顧問(CTA)，只能以demo/paper account教學（`iDwYeyxTDiU`, `H1-Ni_J-tOw`, `Ic1rqvbk99c`）。
- **"I am the author/engineer/creator of this stuff, nobody else invented it"**成為貫穿全部45部影片最強烈、最一致的身份主張，並在晚期（2025-2026）疊加"AI/chatbot會學到錯誤說法"的焦慮（擔心ChatGPT/Grok從網路輿論"污染"他的歷史定位）。
- **家庭元素頻繁出現在後期影片**：teaching his son Caleb live trading(`hxdAOfcp6gE`, `hzoMJQlEv5M`)，兒子帳戶從$6,000成長到$10,000+，以及提及"married to a woman that demands more of my personal time"作為結束公開YouTube教學的原因(`iKsIbUblSWM`, 2022最後一集)。
- **武術腰帶比喻/教學心理學**：用美式武術"belt system"比喻初學者需要漸進式的成就感獎勵，並自比"我從不放水,我不是會嬌慣孩子的母親"式的嚴父角色(`hxdAOfcp6gE`)。
- **持續的"golden goose"/"cult of winning"自我覺察式承認**：多次自嘲承認別人稱他的社群為"cult"，但辯稱他教的是"independent thinking"而非依賴(`H1-Ni_J-tOw`早提及，`gDFZ4p1BI1c`、`hxdAOfcp6gE`再次出現)。

### 4. 決策紀錄（續，重大補充）

- **2022-06-02 EURUSD 非農日直播call**：公開在Twitter標記5分鐘圖fair value gap高點，價格如期到達，用以證明「非事後諸葛」(`HuZurY0ghDI`)。
- **2026-06-07 期貨評論影片（黃金/白銀/原油/DXY/EURUSD/GBPUSD/NQ多資產分析）**：後續於2026-06-24影片中回顧驗證，白銀跌破4%（引用1980年Hunt兄弟白銀逼倉事件作類比）、原油與黃金皆命中預測目標，展示「事後驗證」影片格式(`hxdAOfcp6gE`)。
- **2026-07-15 CPI後NQ盤中分析**：完整記錄CPI當天的做空邏輯(inversion FVG, event horizon, 8:30 low)，最終部分部位在停損處出場(仍獲利$1,680)，展示「不是每次都達到最大目標，但仍對整體邏輯有信心」的務實態度(`IF7dEkgWoO0`)。
- **2021年12月31日"last teaching lecture"（英鎊做空案例）**：用完整market maker sell model框架逐層拆解GBPUSD在1個交易日內的buy-side delivery→smart money reversal→sell-side delivery全流程，作為他YouTube免費教學的收官之作。(`iKsIbUblSWM`)
- **2021-06-03 EURUSD 反嗆Astro FX案例**：公開放出交易錄影(進場、停損10 pips、分批止盈)，同步截圖對手"Sean"看多的推文，證明自己判斷相反且正確，並公開叫戰對方展示交易紀錄。(`Ic1rqvbk99c`)

### 5. 時間線/背景線索（續，重大發現）

- **"Tobias and Parson"神秘啟蒙者**：`iDwYeyxTDiU`中他首次（在本批次範圍內）提及有兩位真實姓名為Tobias和Parson的人，不公開露面、不教學、不上CNBC，是他們向他「揭示」了市場運作的核心秘密，且暗示這兩人「並不總是和善」，他作為「一家之主/父親/丈夫」必須謹慎拿捏能公開多少。這是一個此前未見、極不尋常的傳承敘事，值得作為人設素材的重點記錄（可能是宗教啟示的隱喻表達，也可能實指真人）。
- **1996年是反覆出現的關鍵年份**：多次提到「1996年我就創造了這些概念的講義」、「1996年之前是我發明這些的」，並以此反駁"rebrand"指控。(`iDwYeyxTDiU`, `gDFZ4p1BI1c`)
- **1990年代提供"$20,000一對一課程"**：`iDwYeyxTDiU`中他自曝這是"Steve Mauro"故事中被誤傳為"$25,000"、「已故鄰居飛行員」的真實原型來源，暗指對手編造師承故事影射他。
- **2021年宣布永久停止付費mentorship招生**（"my final mentorship for 2021"），此後转向"private community"與免費YouTube雙軌並行，2022年起大量透過YouTube重新教學核心內容。(`iDwYeyxTDiU`, `IEa1N0rTtbc`)
- **教導兩個兒子交易（Caleb之外至少還有其他兒子被提及"my sons"）**，並使用自己的MT4/AMP帳戶讓兒子練習，此前因對交易帳戶所有權的爭議被OANDA關閉帳戶。(`iDwYeyxTDiU`)
- **明確使用ChatGPT/Grok等生成式AI是他近期(2025-2026)公開發言的新焦慮來源**，顯示他因應時代變化持續調整"維權"策略（見前段AI相關記錄）。
- **2026年6月數個影片顯示他仍活躍公開教學**（`hc9SDgW93gc`, `hxdAOfcp6gE`, `IF7dEkgWoO0`），顯示儘管他曾多次聲稱"最後教學"、"要退休"，實際上仍持續高頻率產出內容直到系統當前日期(2026-07-16)前一天。

### 6. 矛盾與演變（續，重大發現）

- **「這是最後一次公開教學」(2021年底) vs 持續至2026年仍在製作大量教學影片**：`iKsIbUblSWM`明確宣稱是"the last teaching lecture on the inner circle Trader YouTube channel"，但manifest中有多支2025-2026年份的影片（`hc9SDgW93gc`, `hj48OuvouBM`, `g9BctYx0LaI`, `gDFZ4p1BI1c`, `hxdAOfcp6gE`, `IF7dEkgWoO0`），顯示他反覆「宣布停止」又持續復出的模式，這是一個明顯、可驗證的行為矛盾（不只是言語矛盾）。
- **「我不需要吹噓」vs 反覆展示帳戶餘額、獲利數字、追隨者數量(2.5百萬)、金錢炫耀式反問句（"look at my house, my car"）**：`iDwYeyxTDiU`與`hxdAOfcp6gE`中皆有大量篇幅炫富反擊酸民，與他"我不在乎錢/名"的自我敘述形成張力。
- **神秘啟示來源(Tobias and Parson / 向神禱告獲得洞見) vs 反覆強調1996年"自己創造"這些概念**：一方面說是他人啟示或神所賜予，另一方面又堅稱"I am the author, I created it, no one taught me"——這兩種敘事（外部啟示 vs 自我原創）在邏輯上略有張力，值得作為矛盾記錄，但也可解讀為信仰語言（感謝神賜予他發現的能力）與人類作者權（他組織/命名系統）兩個不同層次，並非嚴格互斥。

---

## 補充：遺漏的 5 個檔案分析

### 1. 心智模型候選（續）

- **Wick = Gap 的「consequent encroachment」vs order block 的「mean threshold」是兩套不同術語**：他明確澄清"wick theory"與"order block theory"雖類似但不同——wick(視為gap)的中點稱"consequent encroachment"，order block的中點稱"mean threshold"，兩者不可混用。(`GaFe8LSmtfY_2023 Preview... Precision Inc.`)
- **Mitigation 是交易者的行為，不是PD array本身的行為**：糾正普遍誤用——"order blocks and candles are not mitigating anything, price is allowing the trader to mitigate their offside position"，mitigation指的是逆勢交易者藉由價格回測來減損/出場，而非PD array"在mitigate"。(`GaFe8LSmtfY`)
- **Premium/Discount 可以「反轉」(inversion)**：在高時間框架失衡(imbalance)的上半部（premium）若被跌破，會變成新的discount，反之亦然；他坦言"that part is extremely confusing"，屬於2023年教學中逐步展開的進階概念。(`GaFe8LSmtfY`)
- **真正的支撐阻力來自「未成交的價格缺口」(real gap/liquidity void)，而非傳統技術分析畫線**：日線圖上「完全無成交紀錄」的缺口比order block、fair value gap更具權威性，演算法會反覆精確回測到這類缺口的高低點。(`fz9ZDU6bKIc_2022 ICT Mentorship Market Review`)
- **Liquidity Void（流動性缺口）機制詳解**：單邊、長實體K棒形成的價格區間視為"缺乏對向流動性"，市場終將回補；缺口能開多久沒有時間上限，取決於當下價格行為；並區分「liquidity void」與「common gap」（K棒開盤/收盤之間真正未交易的空隙）兩種不同缺口，common gap可作為精確限價進場點。(`HTQgH11W37o_ICT Mentorship Core Content - Month 04 - Liquidity Voids`, 2016年12月)
- **Swing Trade「八大要素」框架（explosive move的判斷條件）**：多重時間框架/多資產類別綜合分析法——(1)四大資產類別(利率、股市、商品、外匯)至少兩類呈趨勢環境 (2)跨資產intermarket confluence (3)COT commercial hedging對齊(以過去12個月高低點自訂新的0軸，而非官方0軸) (4)open interest變化驗證smart money倉位 (5)季節性傾向 (6)波動率收縮filter(inside bar/inside candle，過去3天或7天最小範圍) (7)反向利用主流財經頭條情緒 (8)市場情緒指標。(`Hoo_wTMgdcY_ICT Mentorship Core Content - Month 06`)

### 2. 決策啟發式（續）

- **反指標式利用其他直播主的情緒**：觀察到其他live streamer對某方向過度亢奮/啦啦隊式喊多時，视为反向訊號，藉此增強自己相反方向的信心並加碼部位。("the more they did that, the more I felt confident it was going to sell off")(`fz9ZDU6bKIc`)
- **不建議新手交易非農/FOMC，但自己仍會用demo帳戶實盤示範該日交易邏輯**：明確聲明"I don't advocate trading with live funds if you're a developing student"，但同日仍完整示範NFP當天的做空邏輯與分批出場(8口/4口/2口)。(`fz9ZDU6bKIc`)
- **分批止盈並非隨意，而是對應具體PD array層級**：強調"my partials are not random"，每次減倉都對應特定的imbalance/order block高低點，並非因價格波動而臨場反應。(`fz9ZDU6bKIc`)
- **COT持倉背離官方0軸的「自訂中性軸」方法**：用過去12個月commercial持倉的最高與最低點取中點，作為自己判斷偏多/偏空的基準，而非市場公認的官方零軸淨倉位。(`Hoo_wTMgdcY`)
- **利用財經頭條的反向情緒作為進場確認**：若已看多某資產，卻看到財經媒體/名嘴發布利空頭條，視為「錦上添花」的進場加強訊號，因為"anything a talking head would have in their headline...that to me is fuel in the fire"。(`Hoo_wTMgdcY`)
- **波動率收縮(inside bar/inside candle)作為「引爆前兆」**：月/週/日K棒實體範圍較前一根收縮，視為即將出現大範圍(explosive)行情的訊號，但不提供時間點，只提供「即將發生」的階段確認。(`Hoo_wTMgdcY`)
- **市場情緒過濾器：15週期Williams %R，50為分界**：50以下視為oversold(偏多濾網)，50以上視為overbought(偏空濾網)；若剛離開超買/超賣區並回到50附近，仍沿用剛離開的那個情緒方向做為偏向。(`Hoo_wTMgdcY`)
- **Liquidity void回補的限價進場法**：在缺口(common gap)價位直接掛限價單進場，利用「只有實體回補、不需完全回補」的特性作為精準進場點，回撤極小即恢復原方向。(`HTQgH11W37o`)

### 3. 表達DNA（續）

- **"sneaky ICT"自嘲式坦承**：直播/複盤影片中坦承自己在陪伴家人時偷看手機、偷發推特分析市場，用"I was in the stealth mood"、"sneaky ICT"自嘲，展現輕鬆幽默的一面。(`fz9ZDU6bKIc`)
- **對模仿者的用詞更新**："dollar menu mentorships"(廉價山寨導師)、"yahoos on instagram and facebook and youtube"，持續攻擊自稱教他理論卻教不好的人。(`fz9ZDU6bKIc`)
- **嚴厲糾錯語氣升級**："stop spreading misinformation and stop perpetuating ignorance"，針對誤解他"shift in market structure"定義（不需收盤突破）的人直接開罵。(`fz9ZDU6bKIc`)
- **自謙但暗藏優越感的措辭**："I'm probably one of those boring person on the planet to learn from and that's what you want"、"I'm not a 20 year old hot shot that's trying to make everybody love me because of image"。(`fz9ZDU6bKIc`)
- **提及"我50歲的眼睛不像以前那麼好了"**：邊用手機看盤邊自嘲視力衰退。(`fz9ZDU6bKIc`)
- **對兒子的情緒外露**：直播中提及"if especially if my son does something right I'm gonna be like cheerleading him"，顯示家庭元素很早（2022-2023）就已融入教學風格，並非僅晚期才出現。(`fz9ZDU6bKIc`)
- **持續使用宗教/道別語尾**："until then be safe"、"good luck good trading"依然貫穿教學內容影片(`Hoo_wTMgdcY`)。
- **教學中坦承使用指標的罕見自我調侃**："and yes I heard that right I use an indicator"——難得打破"我不用任何指標"的一貫人設,語氣帶著自嘲式驚訝。(`Hoo_wTMgdcY`)

### 4. 決策紀錄（續）

- **2022-07-08 NFP當週市場複盤（DXY/EURUSD/GBPUSD/NASDAQ/ES）**：完整展示SMT divergence（dollar未創新低 vs EURUSD創新高）判斷dollar看漲、指數看漲的複合偏見；ES非農實盤demo交易於38.75附近做空，分批出場(8口進場，4口/2口/2口分批平倉於38.75附近)，並在推特於8:29(NFP公布前一分鐘)公開流動性水位以防抄襲。(`fz9ZDU6bKIc`)
- **2023年「Precision Inc.」示範片段**：用2022年模型示範bullish breaker + fair value gap的做空進場與金字塔加碼，停損刻意設在遠離市場處，展示「極致精準卻又不需要靠近停損」的教學片段。(`GaFe8LSmtfY`)
- **2023-01-25 Mentorship Analysis複盤（DXY/EURUSD/GBPUSD/NASDAQ/ES）**：多時間框架(日/時/15分/2分)逐層拆解，NASDAQ在12339高點consequent encroachment、ES在4117.75/4072.75一線精準延遲進場,並描述觀察其他直播主看多情緒後反手做空的實戰心理紀錄。(`HkiPAi1Mdu8`)

### 5. 時間線/背景線索（續）

- **"我50歲的眼睛"**：2022年7月自述年齡線索(50歲)，與2023年12月自述"52歲"的時間線吻合，可交叉驗證其出生年份約1971-1972年。(`fz9ZDU6bKIc`)
- **提及剛搬新家、太太、家中還在拆箱整理、有一份禮物要掛在交易室牆上**：罕見的即時家庭生活片段，顯示他將個人生活細節帶入教學開場白。(`fz9ZDU6bKIc`)
- **2016年12月教學系列時間點確認**："this teaching number five of eight for the ICT mentorship content for December 2016"，明確標示Month 04 Liquidity Voids屬於2016年12月付費mentorship課程第5/8課，聖誕週停止交易但持續補充每日教材。(`HTQgH11W37o`)
- **兒子在直播現場會被他當場稱讚、產生情緒外露**：顯示"教兒子交易"與家庭元素融入教學的模式其實早於2022年就已存在，並非僅是2025-2026年才出現的新現象。(`fz9ZDU6bKIc`)
- **提及訂閱Futures雜誌，長期關注COT/commercial hedging數據**，作為他總經/機構持倉分析知識來源之一。(`Hoo_wTMgdcY`)

### 6. 矛盾與演變（續）

- **"零指標裸圖交易"人設 vs 公開承認使用Williams %R指標**：他反覆宣稱"you don't need moving averages... these are the best indicators you're ever going to have"（指燭台本身），但在`Hoo_wTMgdcY`中明確說明自己用15週期Williams %R作為市場情緒過濾器，並自嘲"yes I heard that right I use an indicator"——這是目前收集到最直接、他本人也承認的一次自我矛盾。
- **警告學生不要交易非農 vs 自己於非農當天全程示範交易邏輯**：`fz9ZDU6bKIc`中他強調不建議developing trader於非農/FOMC當日交易（"that's stupid... poor mentor"），但同一支影片中緊接著完整示範自己當天的非農demo交易，用「demo帳戶、非實盤」作為兩者之間的緩衝解釋，但語氣張力仍值得記錄。
- **"我不評論/按讚學生交易點子" vs 實際上透露自己私下按讚過學生貼文**：`fz9ZDU6bKIc`中他先說"I don't like it because that's me co-signing your trade"，隨後又承認"I knew that this was going to be a turning point, the gentleman on twitter knows that I liked his post"——說法前後有些微不一致（先說不按讚，又說有按讚），可能是語境切換（不主動評論 vs 私下按讚以示認可）造成的模糊地帶。

---

## 低訊號檔案 (Low-signal files)

1. `iN8sCjiR1Bs_Building Equity In Short Term Timeframes - No Audio.en.txt` — 逐字稿僅顯示 "[Music] ah Oh than"，無任何語音教學內容，完全無法萃取訊號。

（其餘44個檔案皆含充足心智模型/決策啟發式/表達風格/背景線索/矛盾素材）

---

*（本批次45個檔案分析完畢，含最終補齊的5個遺漏檔案：fz9ZDU6bKIc、GaFe8LSmtfY、HkiPAi1Mdu8、Hoo_wTMgdcY、HTQgH11W37o）*
