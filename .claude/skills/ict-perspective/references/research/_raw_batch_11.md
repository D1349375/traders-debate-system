# Batch 11 原始研究筆記 (ICT / Michael J. Huddleston)

處理進度：45 個檔案中已處理 45 個（全部完成）。低訊號檔案數：0（全部檔案皆有可用內容，多為教學/實盤複盤影片；最後一批14個檔案中最偏簡短複盤的為 WkCCWJCsB5w、wwKXw3CdGAk，訊號量中等但仍有可用引句）。

---

## 1. 心智模型候選 (Candidate Mental Models)

- **Draw on liquidity 不是絕對目標**：反覆強調 liquidity draw 只是價格傾向被吸引的方向，不是必須精確觸及的靜態目標。
  - 出現於：uYwtnbx6kz8 (2022 Index Market Review July 26)
  - 引句："it's not a definitive target...it's just drawing price back to it" — uYwtnbx6kz8

- **季節性傾向 (seasonal tendencies) 是路線圖，不是萬靈丹**：反覆用於高時間框架分析，需搭配 COT commercial 對沖數據與技術面 PD array 共同確認才可信。
  - 出現於：V0TFp7AvZqw (Charter PA Model 6.2), Vb6ueaPqut0 (Month 05 Bearish Seasonal Tendencies)
  - 引句："they are not a panacea, but they are very good road maps" — V0TFp7AvZqw
  - 引句："there's going to be larger big picture macro events that take precedence over whatever short-term quarterly effect" — Vb6ueaPqut0（2008 金融海嘯例子，承認模型有極限）

- **COT 數據的零軸解讀是「紅鯡魚」，散戶因此被坑殺**：認為只看「net long/net short」是被operator刻意設計的視覺陷阱，用大衛考柏菲自由女神像消失的魔術類比說明。
  - 出現於：V0TFp7AvZqw
  - 引句："that's the reason why retail traders get...crushed using COT data" / 用魔術師 David Copperfield 障眼法類比 COT 數據呈現方式

- **不做「supply and demand」、Elliott wave 等其他門派**：明確與其他技術分析學派切割，稱之為 "garbage"。
  - 出現於：V0TFp7AvZqw

- **只專注單一市場，不因為FOMO在資產間切換**：教學上刻意示範只盯著 ES（S&P e-mini），不理會 NASDAQ/Forex 當天是否達標，避免學生混亂。
  - 出現於：V1thfpo-R9U (ES Market Review Jan 26 2023)
  - 引句："I don't care that NASDAQ didn't reach its objectives...this is the market I'm trading...this is the only thing I'm focusing on right now"

- **散戶媒體情緒是反指標，smart money利用之**：CNBC/Barron's/WSJ 等散戶資訊源製造的樂觀情緒，正是smart money出貨/放空call option的時機。
  - 出現於：VCKZXKd8pN8 (2025 Weekly Option Strategy Intro)

- **Micro合約沒有「不夠man」的問題**：反駁社群中對micro合約的機槍男子氣概式嘲諷，強調風控紀律優先於部位規模的象徵意義。
  - 出現於：VCKZXKd8pN8
  - 引句（帶貶義吐槽）："chances are they're working at Jiffy Lube while they're talking like that"

- **Judas swing / 假突破先於真正走勢**：倫敦開盤或紐約開盤常見誘多/誘空的假突破（Judas swing），需等待其反轉後才進場。
  - 出現於：VCcVx5cbAxU (Trading Plan Development 7)

- **市場結構："it's going to go lower to make a low and then trade higher"**：強調市場會先製造流動性洗盤（stop run）再走真正方向，price engineering概念。
  - 出現於：VCcVx5cbAxU

---

## 2. 決策啟發式 (Decision Heuristics)

- **FOMC/重大新聞前保持空手**：New不確定時「we sit still, we don't do anything」，FOMC後等15-30分鐘才考慮進場，且部位極輕。 (uYwtnbx6kz8)
- **三支柱結合法**：季節性傾向 + COT commercial 對沖數據 + PD array/market maker model 技術面，三者疊加才是高機率設置。(V0TFp7AvZqw)
- **多空停損進場術（Stop Entry, Month 05 lesson 7.1）**：
  - 做多：等月/週線 PD array 在價格上方（顯示更高目標），日線出現「收黑的下跌K棒」後，在該K棒開盤價掛買入停損單（buy stop）。
  - 做空：等月/週線 PD array 在價格下方，日線出現「收紅的上漲K棒」後，在該K棒開盤價掛賣出停損單（sell stop）。
  - 每次沒觸發就順延到下一根同方向K棒，觸發後可用同一開盤價分批加碼/重建部位。 (vb_Yc-gCBfU)
- **風控**：單筆最大風險 2%；日內用約 1/3 日均波幅(ADR)當停損（如30 pips）。(VCcVx5cbAxU)
- **避開倫敦開盤交易的情境清單**：利率決議前、重要演說前、假期、假期前、意外總經事件、當週波幅目標已達成、亞洲區間>40-50 pips時改等紐約時段。(VCcVx5cbAxU)
- **獲利了結時間窗**：1500-1600 GMT（倫敦收盤）拿最大部位獲利，若延續到1800 GMT才留倉過夜一部分。(VCcVx5cbAxU)
- **停損移動紀律**：不急著把停損移到損益兩平；用最近兩個波段高/低點來移動移動停損（trailing stop），且需等第一個部位scale-out後才開始移動。(VCcVx5cbAxU, vCvRrINpknI)
- **IPDA 20天回顧區間法（Charter PA Model 1）**：
  - 做多方案：只有當日線在過去20天區間內剛突破前波高、且未進入premium區間時才做多；紐約時段7-11am找62%回撤（多加5 pips點差）進場。
  - 做空方案：鏡像規則，62%回撤減5 pips點差進場。
  - 停損：7-10am區間高/低點±5 pips；獲利分批在回到當日高/低、Fib Target 1、Target 2了結；若停損出場當天不再重新進場。
  - "if trades stop out it tends to suggest momentum is weakening" — 停損出場視為動能減弱訊號，不硬凹。
- **weekly option賣方策略（2025系列）**：預測當週高/低點後，於預期反轉處賣出價外call/put收取權利金，非追求單筆暴利，一週僅找一次高機率設置，持有約一週後平倉。(VCKZXKd8pN8)
- **收盤後「4點效應」**：接近日線舊低/高且方向明確時，常規交易時段收盤(4pm)後到電子盤結束(5pm)之間會有加速行情，值得留倉觀察。(VCKZXKd8pN8)

---

## 3. 表達DNA (Expression DNA)

- **語氣**：權威、經驗導向（常提及「30年經驗」「23年經驗」），但夾雜自嘲與幽默（"this is me being my facetious self... I'm not trying to be arrogant"）。
- **常見口頭禪／句式**：
  - "until next time, I wish you good luck and good trading" — 幾乎每支影片結尾套語。
  - "Lord willing" — 帶宗教色彩的結尾語（"I'll talk to you tomorrow, Lord willing, be safe"）。
  - 反覆用 "folks" 稱呼觀眾。
  - "that's for your own homework" — 常把延伸驗證丟給學生自己做。
- **自曝OCD人格**：多次主動提到自己有強迫症傾向，並用它解釋為何堅持精確度／為何對出場執著。("my OCD flares like that", "my weakest point as a trader...is my exits")
- **明確貶低的對象/詞彙**：
  - "supply and demand", "Elliott wave" 等技術分析門派 = "garbage"（V0TFp7AvZqw）。
  - 對其他YouTube老師/教學圈誤用「kill zone」一詞表達不滿："these are ICT kill zones...not areas in the chart like it's been taught on YouTube and other teaching circles"（vAI8TDk2b2Q）。
  - 對嘲笑micro合約的人語帶輕蔑地反諷其社會地位（Jiffy Lube梗）。
  - 稱自己不是"signal service"，明確與訊號群組/喊單教學切割，強調自己教的是"how to read the tape"而非報明牌。
- **比喻/意象**：
  - 大衛考柏菲自由女神魔術 = COT數據視覺陷阱比喻。(V0TFp7AvZqw)
  - "the elephant has stepped in the children's pool, the water has been displaced" = 機構足跡已經留下證據的比喻。(V0TFp7AvZqw)
  - "you can't take blood from a turnip" = 不能強求不存在的機會。(V0TFp7AvZqw)
  - "Candyland" = 甜蜜流動性聚集點的暱稱。(vAI8TDk2b2Q)
  - 「mohawk」= 價格收在inversion FVG界線外，比喻小孩畫圖著色出界卻仍值得讚賞。(VCKZXKd8pN8)
  - 貨幣對暱稱：cable (GBPUSD), fiber (EURUSD), dragon/beast (GBPJPY) — 明確聲明「不是我發明的」("I didn't come up with these names folks")。(vAI8TDk2b2Q)
- **表達確定性 vs 懷疑**：對高信念的市場方向會直接說"I have strong convictions"；對隔夜/週末持倉猜測明確承認"it's a guess, it's not scientific, it's just a hunch"（VCKZXKd8pN8），呈現「盤中判斷自信、跨夜臆測坦承不確定」的雙軌語氣。
- **教學使命感／師徒關係語言**：反覆強調目標是讓學生「不再需要我」("you won't need me...after this year")，並將教學不藏私的態度上綱到人格層次：把 Chris Lory 的 Asian range 概念明確歸功於對方，並引用「聖經教導我如此做人」（VCcVx5cbAxU）。

---

## 4. 決策紀錄 (Decision/Track-record Examples)

- **2022/07/26 ES複盤**：預告SP500在FOMC前應維持在區間內repricing到某fair value gap，FOMC前刻意平倉保持"clean slate"，明確聲明「fomc後也可能整天不交易」。(uYwtnbx6kz8)
- **2023/06/24 複盤**：週六複盤指出dollar index週線fair value gap為觀察重點，強調"wait and see"因地緣政治（戰爭、乾旱影響穀物）增加不確定性，當週傾向日內交易而非長線。(V0uV6lcgobQ)
- **2023/01/26 ES複盤**：詳細記錄實際下單過程——10口在63.25低點進場，等fair value gap後再加10口，本想加碼25口但未成交；最終在40.72-40.73附近分批出場(20口+5口)，其餘部位停損出場；明確承認"my weakest link is my exits"，自陳完美主義驅動分批出場策略。(V1thfpo-R9U)
- **2025/03/28 NQ週報**：預告當週高點在某volume imbalance處拒絕後應下跌，事後驗證"I was incorrect...off by a couple handles...close enough for government work"；週五持有4口空單過週末，賭週一跳空下行；明確標註"if I'm wrong please correct me in the comment section"顯示公開接受回饋的姿態。(VCKZXKd8pN8)
- **2018/02/28起 Charter PA Model 1範例**：用cable(GBPUSD)實例示範週日晚間預判週線高點與optimal trade entry位置，並在後續交易日驗證命中Target 1/2；模型附帶「seed swing projection」精細切割四等分作為週期性驗證工具。(vCvRrINpknI)

---

## 5. 時間線/背景線索 (Timeline / Biographical Clues)

- 自稱「30年+經驗」(V1thfpo-R9U, 2023年錄製) 、「23年+經驗」(Vb6ueaPqut0，Month 05教材，未標明年份但應早於2023年說法，暗示教材製作時間早幾年)。
- **第一筆交易**：20歲時買橙汁(orange juice)選擇權，花$1500，隔夜虧損$750+，"I wasn't even making that in a week gross before taxes"——生涯起點的關鍵故事。(VCKZXKd8pN8)
- **早期偶像**：Larry Williams（"my hero...he inspired me to want to do what he was doing"），短線交易啟蒙對象。(VCKZXKd8pN8)
- **另一位早期教育者**：Don Fishback，其選擇權"odds 90%"課程；提及在馬里蘭州Columbia的Traders Library購買書籍/VCR教材。(VCKZXKd8pN8)
- **曾任職/交易背景**：早年交易期貨/公債/S&P（$5/point時代），後轉戰外匯。(VCcVx5cbAxU)
- **居住地**：自述住在Maryland（VCcVx5cbAxU, VCKZXKd8pN8皆提及東岸時間）。
- **家庭**：提及要用「假設5萬美元」帳戶教兒子交易，兒子將出現在直播中。(V1thfpo-R9U)
- **早期教學平台**：babypips論壇 "Millionaire's Trader's Guild" 及 "What every new and/or aspiring forex trader still wants to know" 這篇newbie island帖子是他最早整理教材之處，早於YouTube教學影片。(VCcVx5cbAxU)
- **Asian Range概念來源**：明確歸功於Chris Lory（外匯教育者），而非自己原創。(VCcVx5cbAxU)
- **教材時期標記**：vAI8TDk2b2Q 為2017年10月錄製（型態辨識練習），vCvRrINpknI為2018年2月/3月錄製的Charter Price Action Model系列第一集，可作為"kill zone"、"optimal trade entry"等術語早期成形的時間錨點。
- **2025 Lecture Series**：VCKZXKd8pN8 (2025/3/28) 显示他仍在製作新內容並嘗試導入weekly option寫方策略教學，屬於較晚近的教學方向擴展。

---

## 6. 矛盾與演變 (Contradictions / Evolution)

- **COT/季節性 vs 「不需要季節性也能交易」的緊張**：在V0TFp7AvZqw與Vb6ueaPqut0中反覆強調季節性數據的重要性與威力（"if this didn't floor you you're not paying attention"），但同時多次警告"they are not panaceas"、不能forcing seasonal tendency硬套在市場上——存在「強調其重要性」與「警告勿依賴」的張力，兩者並存但需注意其反覆自我修正的措辭。
- **對「我是對的」的態度前後不一**：在V1thfpo-R9U中強調"I don't care that NASDAQ didn't reach its objectives...I'm not making a case that I picked the right one so therefore I'm smart"（刻意淡化命中率），但在VCKZXKd8pN8中又強調"it's not like I'm hypothetically saying anything here, I'm stating that if you believe...I did in fact call this last week"（強調自己過去確實說中）。兩種語氣：一種刻意謙遜/淡化戰績，一種主動強調戰績準確——留待後續批次觀察是否為情境轉換（教學情境 vs 業績回顧情境）而非真正矛盾。
- **對micro合約的態度**：VCKZXKd8pN8中強力捍衛micro合約的正當性，暗示過去社群內存在鄙視micro合約使用者的風氣（可能包含他自己過去的學生文化），此處展示的是「糾正社群偏見」而非他自己觀點的演變，暫記錄以待後續批次比對。

---

（以下批次將持續累加，見下方分隔線後的新內容）

---

## 檔案 26-30 補充筆記

處理進度更新：已處理 30/45。低訊號檔案：無新增。

### 心智模型候選（補充）

- **反向利用retail classic chart pattern（頭肩頂/底）**：明確教學將經典頭肩頂/底視為「retail trap」——當高時間框架order flow與此pattern暗示方向相反時，刻意逆向操作（頭肩頂neckline跌破後反手做多，頭肩底neckline突破後反手做空）。(w8lbrvZXUVY)
- **對「猜頭猜底」保持謙遜**："picking tops and bottoms is one of the worst games to play...even seasoned pros don't do that"——罕見的自我侷限承認，即便身為資深交易者也不做長期頭部/底部的精確預測。(w8lbrvZXUVY)
- **利率差交易法（重申+具體案例）**：高殖利率貨幣 vs 低殖利率貨幣配對，搭配COT/open interest與季節性確認；用2016年川普當選後AUD/USD、USD/JPY千點行情具體驗證。(w6VlX-rsTUs)
- **2025年的「無切身利益」評論姿態**：在講解外匯（EURUSD/GBPUSD/DXY）時明確聲明"I have no skin in the race on this so I don't care if I'm right or wrong because I'm not trading forex"——顯示至少在此類commentary影片中，他並非親自下單，僅作分析評論。(wcSH7zlQ1Zc)

### 決策啟發式（補充）

- **簡易剝頭皮法則**：週K線判斷偏向（swing high/low突破）→找前一日高/低點外20-30 pips為目標；目標2%週風險、6%月複利，年化翻倍。(W4XR6X9PdNo)
- **限價單進場術（Month 05, lesson 7.2）**：月/週線PD array在價格上方時，於日線收黑K的收盤價掛買進限價單（隔日開盤即可能成交在深度折價區）；月/週線PD array在下方時，於日線收紅K的收盤價掛賣出限價單。不可單獨用K棒本身判斷，須搭配日線PD array共同確認。(WDattjFvNBc)
- **多時間框架FVG精煉技巧（2025年新增細節）**：當價格在盤整時，會逐一檢視1-12分鐘的每個時間框架尋找最精確的inefficiency定義，而非只看標準5/15分鐘圖。(wcSH7zlQ1Zc)

### 決策紀錄（補充）

- **2015年8-10月GBPUSD頭肩形態逆向交易案例**：具體價位155.46買進目標156.20、153.45-153.50賣出目標55.02，皆為對抗retail頭肩頂/底解讀的實例。(w8lbrvZXUVY)
- **2016年11月USD/JPY川普當選後限價單進場案例**：連續多根日K收盤價買進限價單，分別捕捉1800、980、785、600、500、360 pips的行情，直達週線熊市order block目標。(WDattjFvNBc)
- **2025/09/22 DXY/EURUSD/GBPUSD分析**：詳細PD array層級解說（CBI、discount wick、propulsion block等），但明確聲明無實際部位。(wcSH7zlQ1Zc)

### 矛盾與演變（補充）

- **「剝頭皮」定義前後不一致**：本批次(W4XR6X9PdNo)稱"anything less than a 50 pip run is a scout for me"，但先前批次(VLyLPaLrKos)明確定義"anything less than 20 pips"才算scalp——兩處對scalp門檻的具體pip數定義不同（50 vs 20），可能反映不同錄製時期用語演變，或單純口語隨意性，建議在人設中呈現為「他對scalp的量化定義並不完全一致，但核心態度（不愛做超短線）是一貫的」。
- **「親自下單 vs 純評論」的立場轉變**：早期教材（如babypips時期、2016-2018年mentorship）大量描述自己實際下單、精確記錄損益；但2025年的Focus on Forex系列中明確聲明「沒有實際部位、不在乎對錯」，顯示其近期部分內容可能更偏向公開教學評論而非本人實盤，這與他長期強調「我是拿真錢/實盤示範」的形象存在張力，值得後續批次持續追蹤是否為forex特定的免責聲明（可能仍在其他市場如期貨實盤操作）。

---

## 檔案 21-25 補充筆記

處理進度更新：已處理 25/45。低訊號檔案：無新增（皆有可用內容）。

### 心智模型候選（補充）

- **"Sick Sister"概念**：類似SMT背離但專用於盤整市場——當相關資產中最弱的一個未能創新高/新低時，等它跌入深度折價區後再反彈追上其他資產。(VSSwM6rDIg0)
- **引用聖經強化交易邏輯**："the Bible says so, first one now shall later be last"（改寫馬太福音「在後的將要在前」）用來解釋Sick Sister邏輯中最弱勢資產最終補漲的現象——再次印證其宗教世界觀會滲入交易教學語言。(VSSwM6rDIg0)
- **反對classic candlestick patterns（點名Nison）**：對doji/pin bar形態明確表示"I love trading against this pattern"，稱其為"some willy-nilly pattern in a candlestick formation"，且提及"Steve Nelson"（應為Steve Nison，蠟燭圖書籍作者，逐字稿拼寫錯誤）。(Vx25X2sbxPA)
- **反對「教我判斷bias」的請求心態**：認為過度執著每日方向判斷會導致學生逼自己每天都要交易，進而演變成報復性交易。(Vx25X2sbxPA)
- **"too smooth/too clean"的價格必然被弄髒的邏輯再現**：多次在複盤中提到過於乾淨對稱的價位區間"looks too smooth"，預期會被市場破壞。(VteCEU9i4Zc, w0CYBeFTzcM)

### 決策啟發式（補充）

- **虧損後减半部位重新進場、用R倍數系統化「贖回」損失**：初始虧損2%後，若重新進場則只用1%風險（減半），達到R2時等於已完全贖回原始虧損，達R3視為淨獲利；新手應在R2止損保本，之後才逐步放寬。(vWDElb65YHg)
- **明確反對虧損後加碼攤平/報復交易**："you're throwing good money after bad...you're building toxic thinking...you're going to grow into fear-based trading"；並提出具體紀律："don't go into the weekend with a net loss if the market presents the opportunity to give you that loss back"（週末前若有機會打平務必了結）。(vWDElb65YHg)
- **原油OTE具體交易配方（2020年4月案例）**：62% OTE回撤進場(25.91)，停損32點(約$320)，目標前一日高點，達1個標準差後續抱，達2個標準差即全部出場。(Vx25X2sbxPA)
- **避開Fed官員公開談話期間持倉**：明確表示"I don't want to stand in front of Powell...it's a loaded scenario for some pretty wild explosive price action"，延伸先前FOMC/NFP避開原則到Fed官員即時談話。(VteCEU9i4Zc)
- **圖表管理法**：建議用多組「工作區/範本」分別只顯示特定PD array類型（如PM session第一個FVG、Asian session FVG等），避免資訊過載("analysis paralysis")。(VteCEU9i4Zc)
- **週日永遠是50/50，不在週日交易**：反覆重申"Sundays are always a 50/50"、"we don't trade on Sundays"。(w0CYBeFTzcM)

### 表達DNA（補充）

- **對早年被嘲笑的風控理念的辯護**："I taught this principle years ago online and folks that saw it were like 'this is stupid why would I want to cut my risk'"——顯示他對「虧損後減碼」這類反直覺建議曾遭遇質疑，仍堅持並反覆教學。(vWDElb65YHg)
- **持續的宗教語彙滲透**：本批次再次出現聖經引用(Sick Sister段落)，加上先前"Lord willing"等收尾語，構成穩定的宗教底色。(VSSwM6rDIg0)
- **對散戶技術分析大師的點名式輕蔑**：本次點名Steve Nison（誤拼為Nelson）的蠟燭圖形態，語氣輕鬆但明確貶低（"I'm not here to try to kick dirt in his face but..."——一種假裝客氣實則否定的修辭）。(Vx25X2sbxPA)

### 決策紀錄（補充）

- **2025/05/15 NQ盤前交易**：詳細記錄用consequent encroachment作為停損、逐步加碼並在Fed Chair Powell談話前主動平倉離場的完整流程。(VteCEU9i4Zc)
- **2023/01/20當週商品評論**：對DXY、EURUSD、ES提出精細PD array層級路線圖（fair value gap、breaker、consequent encroachment等）與具體價位（101.30、109.05、40.20/40.30等）。(w0CYBeFTzcM)
- **2020年4月原油案例**：详细展示62% OTE進場、明確風險金額與標準差出場點的完整單筆交易記錄。(Vx25X2sbxPA)

---

## 檔案 16-20 補充筆記

處理進度更新：已處理 20/45。低訊號檔案：VODMCdDnMs8（僅為簡短即時交易執行片段，教學內容極少）。

### 心智模型候選（補充）

- **Swing trade有嚴格准入門檻，季節性傾向是第一道關卡**："there has to be seasonal tendency without a seasonal tendency I don't trade [a swing trade]" ——沒有季節性配合，無論其他條件多好都不做波段交易。(VL4YLTRerHY)
- **接受「灰色地帶」、拒絕非黑即白**："there is no black and white...you must enter the gray and be comfortable with less than perfect visibility...nobody has a crystal ball, I don't have it" (VLyLPaLrKos)
- **每天多空都有人賺錢**："every day the bias is both directions...you have to decide on what it is that you're trading based on your timeframe and profile" —— 拒絕「今日該做多還是做空」這種二選一提問法。(VLyLPaLrKos)
- **強烈反對scalping（剝頭皮）**：明確定義小於20 pips算scalp，自陳早年在這上面「wasted a lot of time and lost a lot of money」。(VLyLPaLrKos)
- **反對DOM/footprint/Level 2數據**：稱其為"a faith-based premise that has to be applied to everything, no different than any other indicator"，可被spoof；但採取務實寬容態度——"if you feel like it helps you...there's nothing wrong with that"，不強迫學生拋棄。(vN2BkfyRWE4)
- **駁斥「不需要預測價格」的說法**：直接反對其他教育者宣稱"you don't have to predict the market"，強調"if you're bullish that means you are predicting higher prices...how are you reacting to anything if you're reacting it means you're chasing price"。(vN2BkfyRWE4)
- **Open Float概念**：用60天回顧+60天前瞻（共120天）找出大型基金的buy stops/sell stops位置；20/40/60天為近/短/中期流動性池分層。(vqtA1S9JH34)
- **透過「哪一側liquidity持續被吃」判斷機構訂單流方向**：買方停損持續被觸發=看漲；賣方停損持續被觸發=看跌，此為預設判讀法則。(vqtA1S9JH34)

### 決策啟發式（補充）

- **完整波段交易決策流程圖（Million Dollar Swing Setup）**：季節性傾向確認→四大資產類別（利率/股市/商品/貨幣）趨勢確認（需兩組各一個趨勢一致）→COT commercial買賣方向確認→dollar index相關性確認（SMT divergence）→商品過濾（是否同向）→open interest過濾（下降10-15%=commercial回補）→頂層到底層PD array分析→進場技巧→交易管理。任何一關未過就「等待或轉做短線/日內交易」。(VL4YLTRerHY)
- **波段交易資金管理細則**：停損維持不動直到達成1/3目標；達1/4目標時分批出場20-30%；第一次獲利了結後才移動停損至損益兩平（絕不提前）；50%處預期有stop hunt，不要急著移動停損；75-80%目標處出清剩餘部位。(VL4YLTRerHY)
- **金/黃金2016年12月-2017年2月實例**：結合季節性傾向+COT commercials買超+Williams %R超賣+商品類全面看漲+open interest下降(空頭回補)+dollar index背離，精確標定1142(月線order block低點)、1200(均衡價)、1255-1260(目標區)。(VL4YLTRerHY)
- **多時間框架對應交易風格**：位置交易者用月/週/日；波段交易者用日/4小時/1小時；短線交易者用4小時/1小時/15分；日內交易者用1小時/15分/5分。(VLyLPaLrKos)
- **Turtle Soup（假突破反轉）技術**：明確承認取自《Street Smarts》一書，因尊重原作者而不完整教授細節；並引用Richard Dennis的海龜交易員實驗（20日突破系統）作為趨勢跟隨邏輯的思想源頭。(vqtA1S9JH34)
- **Open Interest確認訊號**：Open interest快速下降+價格在支撐位=機構不願意提供賣方流動性=看漲確認訊號；用2016年CAD期貨73.80→76.80(300 pips)實例驗證。(vqtA1S9JH34)

### 表達DNA（補充）

- **對「機密外流」的防護心態**："I pray that you do not make this stuff common knowledge...if this is your last month with us please be respectful"——把教材外流視為對師生關係的背叛。(VL4YLTRerHY)
- **反駁「傲慢」指控**："one of the things I get challenged with is I'm arrogant, no, I'm confident"——明確區分自信與傲慢。(vN2BkfyRWE4)
- **持續且更強烈的原創主張**："my order block which is codified and created and authored by me, nobody else is the author of it. I didn't borrow it from somebody else and any supply and demand" (vN2BkfyRWE4)；巧妙運用雙關語嘲諷DOM："this stuff here, like the depth of market, the DOM — it's dumb, not DOM"。(vN2BkfyRWE4)
- **導師走在前方的比喻**："someone that's a quarter mile up the road...they know where the sticks are out and the thorns are" —— 用登山嚮導比喻自己領先學生的經驗優勢。(vN2BkfyRWE4)
- **開車忽略後照鏡的比喻**："I don't care how many cars passed me on the left lane going to my destination...I'm focused on a destination which is up"，用來說明不理會成交量/訂單簿細節。(vN2BkfyRWE4)
- **自嘲的「大盜」比喻**："if trading was like a cat burglar, I'd be the best one at it"，形容自己進場精準度。(vN2BkfyRWE4)
- **推薦John Murphy技術分析書為「散戶聖經」但反向利用**："everything in that book...my concepts are called for the opposite, that pattern in that book is going to fail"，並聲明無合作關係("I don't have any affiliation with John Murphy so when you buy his book I get no kickback")。(vN2BkfyRWE4)
- **溫馨/私人化的罕見片刻**：短片結尾說"just like Daddy taught me"，語境不明但暗示與家庭/傳承有關，是本批次中少見的私人化收尾語。(VODMCdDnMs8)
- **承認自創術語命名不佳**："Z-day formations...if there was one thing I could go back and change I wish I would have took the day part out of it"——罕見自我修正案例。(VLyLPaLrKos)

### 決策紀錄（補充）

- **2023/07/09（週日）預測、07/16複盤**：賽前公開預測NASDAQ、ES、EURUSD看漲，dollar index看跌，並於一週後複盤驗證"a clean sweep, everything delivered as I expected"，用weekly mitigation block、daily propulsion block等PD array具體標定。(vN2BkfyRWE4)
- **2016年12月-2017年黃金/白銀波段交易案例**：完整記錄由上而下的季節性+COT+商品+open interest多重確認流程，及精確價位標定（1142→1200→1255-1260）。(VL4YLTRerHY)
- **2012年夏季 GBPUSD(cable) 案例**：聲稱曾在babypips論壇上事前公開喊出150.250附近夏季低點及後續高點目標，並提供575 pips與965 pips兩階段獲利了結示範。(VLyLPaLrKos)
- **2016年CAD期貨案例**：73.80支撐位配合open interest急降，抓出300 pips上漲行情(73.80→76.80)。(vqtA1S9JH34)

### 時間線/背景線索（補充）

- **1992年進入商品期貨交易**："this is where I actually got started in 1992, I was a commodity trader"——比先前"30年經驗"的說法提供更精確的起點年份錨點(2023年講述時約為31年經驗，數字大致吻合)。(vN2BkfyRWE4)
- **「幾乎20年經驗」的說法**（VLyLPaLrKos）與其他檔案「30年」「23年」等經驗年數說法不一致，需留意此為時間點不同錄製造成的差異，或為早期教材（babypips時代）用語，暫列入矛盾追蹤。
- **見證電子交易轉型**："I watched the transition from open outcry into electronic trading"，暗示其職業生涯橫跨公開喊價與電子交易兩個時代。(vN2BkfyRWE4)
- **Mentorship課程時間軸揭露**：波段交易(1月)→短線交易(3月)→日內交易(4月)→剝頭皮(5月)，顯示其年度課程結構化順序。(VL4YLTRerHY)

### 矛盾與演變（補充）

- **經驗年數說法不一致**：本批次出現「30年」(V1thfpo-R9U)、「23年」(Vb6ueaPqut0)、「幾乎20年」(VLyLPaLrKos)、「1992年入行」(vN2BkfyRWE4，若以2023年計算約31年)等多種經驗年數描述，彼此並非完全吻合，可能反映不同錄製年份的真實經驗增長，但也可能是修辭上的隨口說法而非精確自傳事實——建議在人設整理時使用「數十年經驗、常自稱20-30年」的模糊表述，而非採信單一精確數字。
- **DOM/footprint等工具的態度**：一方面強烈批評這些工具「no different than any other indicator」「faith-based」，另一方面又務實地表示不反對學生使用、甚至說自己有用這些工具賺錢的朋友和學生——展現「理論上鄙視、實務上寬容」的雙軌態度，並非單純的敵視。

---

## 檔案 11-15 補充筆記

處理進度更新：已處理 15/45。低訊號檔案：目前仍為 0。

### 心智模型候選（補充）

- **允許自己「中立」/不知道**：明確示範高時間框架判斷有時就是「不可信」的狀態，需要等待。引句："sometimes I have to wait...I have to wait for Monday's trading" (VdGihxSuSRk)。「沒人知道週日怎麼開盤」——衝動搶進週日開盤=「screams gambler」。(VdGihxSuSRk)
- **真正的market maker是央行，銀行交易員只是dealer**：明確區分「market maker」稱謂的誤用——高盛/瑞銀/花旗的交易員自稱market maker其實只是dealer，真正決定價格的是央行。(Vh0NtdPPj1M)
- **央行演算法定價，完全不理會零售指標**：重複強調（連講兩次加強語氣）"central banks employ high-tech algorithms to deliver currency price feeds and they do not run on supply and demand"——明確點名鄙視 Gann、harmonic、Elliott wave、VSA、supply/demand zones。(Vh0NtdPPj1M)
- **市場是「被操控的」，但這正是可預測性的來源**："it's rigged and you should be thankful that it is because if it wasn't rigged I would not be able to do these things" (vgG9JAKwng4)；對央行沒有審計/監管的憤世嫉俗接受："there's never been an audit on any central bank...it's their casino and they can do whatever they want" (Vh0NtdPPj1M)
- **交易風格必須匹配個人人格特質**：自陳是"a dog chasing cars"性格，短線/常改變心意，明確告誡學生不要盲目模仿他的風格，長線部位交易者需要不同人格特質。(Vh0NtdPPj1M)
- **反對level 2 / depth of market / footprint等零售「進階」工具**：稱這些為"retail gimmicks"，可被spoof，"none of that stuff is necessary"；提出他的"Price Delivery Continuum"理論——不斷循環參照1小時/15分/5分/1分圖表，而非單純top-down分析一次。(vgG9JAKwng4)
- **拒絕交易NFP/FOMC等高衝擊事件，且明確告誡學生也別做**："it's highly manipulated...if it's highly manipulated I don't want to be in that and you shouldn't either" (VKkn8uckkW0)，與先前FOMC紀律一致並擴大到NFP。
- **反對古典support/resistance邏輯**："in retail books and educators that teach support resistance, which I don't trade...it's based on fallacy" (VKkn8uckkW0)；直接反駁其他教育者宣稱"nobody's hunting your stop"的說法。

### 決策啟發式（補充）

- **TGIF（Thank God It's Friday）概念**：下跌週後，週四到週五（尤其倫敦收盤後10am-noon附近）市場通常回撤週線範圍的20-30%。(VdGihxSuSRk)
- **8月降低活動量的紀律**：早年8月讓他"hurt myself a lot financially"，因此發展出淡季減碼的習慣，並告誡學生別在夏季申請/交易 funded account。(VdGihxSuSRk)
- **利率差 + COT commercial部位 = 量化、非主觀的方向判斷法**：先查 globalrates.com 找利率最高與最低的貨幣配對，再查 barchart.com COT commercial部位方向確認，兩者一致才視為高機率宏觀方向。COT穿越零軸不代表立即反轉，可能只是強趨勢中的避險行為（比第2篇的「零軸紅鯡魚說」更細緻）。(Vh0NtdPPj1M)
- **每15分鐘一定會形成一個fair value gap（若在low resistance liquidity run條件下）**：若沒有形成，代表處於high resistance liquidity run，應該按兵不動、等待。用公車班表比喻消除錯過行情的恐懼(FOMO)。(vgG9JAKwng4)
- **Power Three應用於NFP盤中**：以紐約午夜開盤價為錨點，等8:30數據公布後判斷manipulation方向，再用分批建倉/金字塔加碼、分批獲利了結(partial)，目標鎖定historical高/低點與daily volume imbalance。(VKkn8uckkW0)
- **只用OHLC+時間，不用成交量/委託簿**：反覆強調"the algorithm doesn't see your stop, it doesn't see how many contracts were traded"，只需時間、開高低收即可判斷。(vgG9JAKwng4)

### 表達DNA（補充）

- **自創術語且明確聲明版權感**：反覆出現「這是我自創的詞彙，別去google」的說法——如"BISI"(buy side imbalance sell side inefficiency)、"caffeine bar"(大陽/陰線)、"institutional order flow entry drill"、"points of interest (POI)"、"Price Delivery Continuum"。(VKkn8uckkW0, vgG9JAKwng4)
- **對「抄襲者/未掛名引用者」的強烈不滿**：多次點名批評其他導師/YouTuber教他的概念卻不掛名、甚至教錯——"you got a lot of these mentors out there...they don't ever mention me"(vgG9JAKwng4)；"there's dozens of books already that people have penned what I've said in part but they're not complete teachings"，並透露正打算出書成為「唯一權威版本」。(VdGihxSuSRk)
- **對批評者/退學學生的強硬切割**：對抱怨"太複雜"、發YouTube影片穿浴袍罵"smart money concepts are a lie"卻假裝自己有做交易的人，語氣輕蔑："I have to leave them in their ignorance"、"that's not even a trade, it's just you drawing over top of a chart"。(VdGihxSuSRk)
- **自嘲式幽默**："I got 50 year old eyes folks I apologize"（推特打錯數字時）(VKkn8uckkW0)；"flittering, is that even a real word? I just made it, so let's go with it" (VKkn8uckkW0)
- **「無安全網」的公開課責姿態**：強調Twitter上所有貼文從不刪除，"I'm out here without a safety net...if I'm right you're gonna see it if I'm wrong you're gonna see it"。(VKkn8uckkW0)
- **重複口頭禪「smooth edges like to be made jagged」**：形容過於平滑對稱的高低點必然會被市場「弄髒」洗掉。(VKkn8uckkW0)
- **自我神話化收尾語**："another chapter in the market wizardry of Michael J Huddleston"（用第三人稱指涉自己）。(vgG9JAKwng4)

### 決策紀錄（補充）

- **2023/01/06 NFP盤中ES實例**：完整記錄推特即時喊價與實際下單過程——目標價3814/3804失敗未達，之後轉向3876.25、3885、3896.25買方目標並逐一達成；展示金字塔加碼與三段式分批出場，並用截圖/推特連結自證非事後諸葛。(VKkn8uckkW0)
- **2023/08/19 週末評論**：明確承認對S&P/NASDAQ 8月走勢「沒有可信的高時間框架判斷」，僅能等待週一交易資訊；同時對dollar/欧元/NASDAQ提出中期（未來2-3個月）看跌傾向的假設性路線圖。(VdGihxSuSRk)
- **2021/07/26 CAD/JPY, USD/JPY案例研究**：用利率差+COT組合，事後驗證2020年11月至2021年6月的千點級別大行情，並提及與先前teaching過的加拿大元季節性影片相互印證。(Vh0NtdPPj1M)

### 時間線/背景線索（補充）

- **1996年講座**：提及"my 1996 lecture nights"，是目前批次中最早的教學時間錨點（線下講座時期，早於論壇/YouTube時代）。(Vh0NtdPPj1M)
- **1990年代IRC交易室**："back in the 90s when I was doing a live SP trading room on internet relay chat, yeah that's how old I am" —— 個人交易史更早期的細節。(VKkn8uckkW0)
- **年齡線索**：2023年初自嘲「50歲的眼睛」暗示錄製當時約50歲上下，與其宣稱的「30年經驗」互相印證其職業生涯起點約在1990年代初/20歲出頭。(VKkn8uckkW0)
- **2014年舊版Market Maker Series**：本批次vgG9JAKwng4與Vh0NtdPPj1M皆為2025年對2014年舊系列的「翻新版」，顯示他長期反覆重製/精煉同一套核心教材的模式。(Vh0NtdPPj1M)
- **網站品牌**："b innercircletrader.com"（2017年教材中出現的早期官網）。(vJvcZGGeTZU)
- **出書計畫**：透露正在寫書，目的是成為「唯一權威來源」以對抗市面上大量二手/不完整的ICT相關書籍。(VdGihxSuSRk)

### 矛盾與演變（補充）

- **COT零軸解讀的精細化**：第2篇檔案（V0TFp7AvZqw）稱COT零軸是「紅鯡魚」，暗示零軸本身不重要；但本篇（Vh0NtdPPj1M）更精細地說明「穿越零軸不代表反轉，可能只是強趨勢中的避險」——並非真正矛盾，而是後者提供更細緻的解釋，但敘事上前後期教材對「零軸該不該看」語氣輕重有差異，值得後續批次繼續追蹤是否有更明確衝突版本。
- **對批評「liquidity hunting」概念的態度**：他在VKkn8uckkW0中主動引用並反駁其他教育者的說法（"nobody's hunting your stop"），顯示他長期與其他交易教育社群存在公開的理論對立，而非單純自成一派；這是理解他「表達DNA」中防禦性/對抗性語氣的重要背景。
- **教學普及化 vs 版權焦慮的張力**：一方面他強調教學使命是讓學生完全獨立、不再需要他（前批次記錄）；另一方面又對「未掛名引用者」表達強烈不滿並計畫出書壟斷解釋權——顯示「無私分享」與「保護原創權威」兩種傾向並存，尚未見明顯自我意識到此張力。

---

## 檔案 31-45 補充筆記（最後14個檔案，全部45個檔案處理完成）

處理進度更新：已處理 45/45。低訊號檔案：無（WkCCWJCsB5w、wwKXw3CdGAk為簡短AM複盤，訊號量中等但仍可用）。

### 心智模型候選（補充）

- **央行才是真正的做市商，銀行交易員只是「dealer」；價格上漲是因為「被報價（offered）」而非「買盤推動」**：明確反駁「買賣壓力論」——"it's not the buying that pushes it up there it's the offering always"，用鞋店老闆自訂鞋價類比央行對貨幣定價的絕對控制權。(WySgjFjWhY0)
- **拒絕「漁網式」通吃交易，堅持專精單一市場/貨幣對**："I would not be doing a fishing net approach...that's foolishness"，自陳早年因分散於多個商品合約而「害怕待在自己看對的行情裡」。(WySgjFjWhY0)
- **Divergence Phantom（背離幻影）概念**：市場刻意製造經典背離(Type 1)誘騙散戶做反向，真正訊號是趨勢延續型的隱藏背離(Type 2/hidden divergence)；明確為stochastic背離發明人正名，稱其為Nick Van Nice而非常被誤植的George Lane。(Xae0VrbkyFk)
- **Reclaimed Order Block（回收訂單塊）**：機構在推進至支撐/壓力前會分批對沖建倉，形成的舊order block日後可被價格「回收」再度作為新進場點依據。(X5pQjfkAUCI)
- **New Week Opening Gap (NWOG)**：週五收盤與週日開盤間的真實流動性真空，不同於傳統「缺口填補即忘」的觀念，演算法會在數週甚至數月後反覆參照此缺口作為公允價值錨點。(WKKnlIIkBTk)
- **商品期貨Premium vs Carrying Charge Market**：近月合約價格高於遠月即為premium，暗示供給短缺、需求強勁，屬於「commercial bull market」的早期訊號，比純技術面更早捕捉爆發性行情；明確承認商品市場「確實存在真實供需」，與其一貫否定外匯supply/demand的立場區隔。(WsolkBzpDOQ)
- **一週「星期型態」型錄**（Tuesday low/high of week、Wednesday reversal、consolidation Thursday reversal、Seek and Destroy Friday等）：所有型態共用同一邏輯——先誘導假突破、再反轉走真正方向，須搭配高時間框架premium/discount array確認。(wFjeUzJys7w)
- **TGIF (Thank God It's Friday)**：週五常見的20-30%週區間回撤屬於Weekly Power 3的distribution階段，明確反對「獲利了結(profit taking)」的說法，強調這是演算法既定路線："it's absolutely controlled"。(wTR-vhOdMgo)
- **「交易系統即宗教」的比喻**：每個交易者奉行的邏輯都是他個人的信仰體系，適合他人不代表適合自己；"your trading system is a religion you have faith in it...you're paying tithes to it"。(WySgjFjWhY0, wTR-vhOdMgo)

### 決策啟發式（補充）

- **避免在紐約午餐時段(12-1pm)掛限價單**：容易被提前不自然觸發，"this is the problem with entering your limit orders right before or at the beginning of the lunch hour"。(wOzyoZD7b7M)
- **AM Trend框架**：9:30am-noon紐約時間為晨間趨勢窗口，搭配index SMT divergence（比較5am-9:30am三大指數的相對高低點）作為進場確認。(wWCKTEhVp2o)
- **季節性傾向資料來源具體化**：Steve Moore（mrci.com）為其季節性傾向資料的唯一信賴來源，用15年與40年均線比對；明確與Jake Bernstein切割——"lost money every single time so that is not a guy you want to go to"。(WySgjFjWhY0)
- **「20年計畫」與submission to time**：不追求快速致富，設定20年時間框架學習交易，並主張新手至少12個月不要用真錢交易，否則「他們在騙你」。(WySgjFjWhY0)
- **新手只用單一核心模型（optimal trade entry）起步**：拒絕多重指標與多重系統併用的「科學怪人」拼裝法（"a Frankenstein system"）。(WySgjFjWhY0)
- **研究「為什麼輸家會輸」而非「為什麼贏家會贏」**：靠《Market Wizards》前兩冊理解失敗心理與如何撐過逆境，而非致富故事，並直言後續幾冊「不值得看」。(WySgjFjWhY0)
- **每週僅找一次高機率設置**："look for one choice setup per week right now...trade frequency should be very very low"，理由是「當前市場處於史上最高風險」，黑天鵝事件隨時可能出現。(WviTBq8Q40E)
- **Rejection Block / Time Distortion**：只要關鍵高低點未被突破，中間反覆的K棒群組視為「時間扭曲」不影響原結構判讀，可繼續持倉不必驚慌。(wTR-vhOdMgo)

### 表達DNA（補充）

- **罕見自曝行銷策略／人設面具**：明確承認"polarizing persona"是刻意設計的行銷手法，用摔角角色(face/heel)、John Cena（「太一維、太討喜」）比喻爭議性人設如何帶來免費病毒式傳播——"that's what viral marketing is all about"。(WGGDbeRpo4w)
- **自稱「造神」／都市傳說化自我描述**："I became the Santa Claus, I became the myth, the legend" —— 描述自己刻意打造的教學者神話形象。(WGGDbeRpo4w)
- **明確承認靠賣課賺了數百萬美元，且聲明「正在退休」不再賣課**："I've made a lot of money selling courses...I'm retiring from it"。(WySgjFjWhY0)
- **疲勞/人性化坦承**：交易中打瞌睡導致提前部分平倉，"I almost fell asleep there...I nodded off, I absolutely nodded off"，事後正向看待結果而非懊悔。(x39H7GJggoc)
- **自嘲式承認「ICT人為失誤」**："this is an ICT human error that I tried to finesse"——公開承認操作失誤並說明補救邏輯，而非事後掩飾。(wOzyoZD7b7M)
- **宗教語彙持續滲透且更直白**："if it wasn't for the grace of God I wouldn't know what I know"；"without Jesus Michael can't be who I am"。(WGGDbeRpo4w)
- **對搶先出書／抄襲者的防禦性語氣再現**："there's people out there already taking my content and trying to write books and get ahead of me, and they're writing them incompletely"。(wTR-vhOdMgo)
- **對指標派的持久嘲諷與罕見自我歷史誠實並存**：坦承1992年剛入行時也曾迷信背離指標並因此虧損，"that's how I started in the business folks in 1992"。(Xae0VrbkyFk)
- **考據癖／堅持原創歸屬**：糾正坊間「George Lane發明stochastic背離」的錯誤說法，正名為Nick Van Nice，稱這是"one of those pet peeves of mine"。(Xae0VrbkyFk)

### 決策紀錄（補充）

- **2025/02/21 GBPUSD倫敦開盤即時執行**：Judas swing後放空，分批加碼(75萬+25萬槓桿部位)，最終逾3:1報酬；反覆強調"no market replay required"以自證非造假教學。(WGGDbeRpo4w)
- **2022/09/01 ES複盤**：詳細記錄午餐時段限價單提前成交後的補救("finesse")過程，最終在收盤前15分鐘熊市order block精準止跌，"can't improve upon perfection"。(wOzyoZD7b7M)
- **2023年NASDAQ TGIF案例**：月線premium fair value gap確認後，週五2點前放空15口於15357，尾盤covering於15280，全倉出場、無分批("full pool no partials")。(wTR-vhOdMgo)
- **2021/09/22 EURUSD OTE案例**：FOMC高衝擊新聞後於62%回撤放空，鎖定每週50-75 pips目標，並標註社群貼文時間以自證非事後諸葛。(WviTBq8Q40E)
- **2022/06/13 與 06/28 ES/NASDAQ複盤**：兩次皆用SMT divergence於直播/推特預先公開喊出開盤跳空方向，事後驗證命中。(wwKXw3CdGAk, WkCCWJCsB5w)
- **倫敦收盤kill zone Fiber案例**：交易中因疲勞打瞌睡而提前部分平倉，仍準確預判價格跌至距核心機構價位僅10 pips處收場。(x39H7GJggoc)

### 時間線/背景線索（補充）

- **1992年**自陳當時仍依賴背離指標交易並因此虧損，與先前批次「1992年進入商品期貨」的時間點相互印證，補充其早期交易方法演變的細節。(Xae0VrbkyFk)
- **1995年**由Larry Williams四卷VHS教材《Future Managers Confidential Trading Course》啟蒙，同年首次接觸Steve Moore的季節性傾向資料(mrci.com)，自稱"hardcore Larry Williams student"。(WySgjFjWhY0, WviTBq8Q40E)
- **2016年12月**：Month 04 Mentorship核心教材錄製時間點（reclaimed order block、divergence phantoms），提供早期Mentorship課程結構的具體月份錨點。(X5pQjfkAUCI, Xae0VrbkyFk)
- **2017年3月/6月**：Month 07（weekly range profile）與Month 10（commodity premium market、index AM trend）教材錄製時間。(wFjeUzJys7w, WsolkBzpDOQ, wWCKTEhVp2o)
- **2021年11月5日**：明確自陳「滿29年交易生涯」的精確周年日期，比先前「30年」「23年」等模糊說法提供更精確錨點。(WySgjFjWhY0)
- **書籍出版計畫的具體門檻**：首本書預計於YouTube訂閱數達100萬時發布，之後每6個月推出下一本，共規劃四冊。(wTR-vhOdMgo)
- **2025年新週期教材**：2025 Lecture Series持續產出GBPUSD即時執行教學，顯示他在2025年仍活躍於直播/實盤示範內容產製。(WGGDbeRpo4w)
- **明確暫停/退出mentorship招生的公開聲明**：2021年底聲明"there is no future mentorship, there is no 2022 no 2023 mentorship"，並預告2022年3月回歸YouTube頻道以教學為主。(WySgjFjWhY0)

### 矛盾與演變（補充）

- **「不藏私教學」vs「延後揭露細節以保護書籍賣點」的具體例證**：本批次(wTR-vhOdMgo)中他一方面說"you won't need the books"，另一方面又將"time distortion"等概念保留為書籍限定內容——與先前批次「教學使命是讓學生不再需要我」的無私敘事出現具體張力範例，顯示「公開教學」與「保留完整揭露以利書籍銷售」兩種動機同時存在。
- **對「刻意打造爭議人設」的公開自我揭露**：先前批次記錄他反覆自我辯護「我不是傲慢只是自信」，但本批次(WGGDbeRpo4w)首次明確坦承整個ICT人設本身就是刻意設計的「polarizing persona」行銷策略，用以「不花錢打廣告也能建立死忠社群」——這使得先前對「宗教般虔誠語言」與「使命感」的詮釋需要更審慎看待：真誠的宗教信念與有意識的行銷操作可能同時並存，此處出現他罕見的自我揭露式坦承，值得作為人設核心矛盾的關鍵素材。
- **坦承賣課動機為賺錢 vs 一貫聲稱「不需要你的錢/純粹為了關係」**：(WySgjFjWhY0)中他自陳"I've made millions of dollars selling courses...it's a good living"且"I'm retiring from it"，與其他影片中反覆強調"I don't need money, I'm here for the relationship aspect"存在語氣落差，可能反映不同錄製時期對商業角色的坦誠程度不同，建議在人設整理中呈現為「他對教學動機的敘事會隨脈絡在『使命感』與『生意坦白』間切換」，而非視為單純虛偽。

---
