# ICT Raw Research Batch 07

進度：45 / 45 檔案全數處理完成（含補處理3個先前遺漏書面記錄的檔案：`M27EOgtHhis`、`MdYrslpUezU`、`MPlNRxHkh_M`，這3個檔案先前已被讀取但筆記未寫入，現已補上，見「批次六」）。低訊號檔案（3個）：`lHvu1qEdFRc_1 Million Subscribers Award`（純感謝影片）、`mDk6ZBadNHk_Pattern Recognition Drill OTE Fiber`（純型態示範）、`o8snDyA6kok_Pattern Recognition Drill OTE UsdCad`（純型態示範，僅30秒等級內容）；`NUdu1n-ML98_2022 Episode 14`為單筆micro NQ執行示範，語言解釋少但仍有心法片段。**資料品質註記**：`MdYrslpUezU_2022 ICT Mentorship Episode 35`的實際轉錄內容與`mkAuOOPTEKw_ICT Emini S&P 500 AM & PM Session Review - 09/02/22`逐字相同（來源端可能重複上傳/誤標），故不重複摘錄，內容已計入`mkAuOOPTEKw`的既有筆記。其餘42個檔案皆有實質可用內容。

---

## 1. 心智模型候選 (Candidate Mental Models)

- **IPDA (Interbank Price Delivery Algorithm) 是一個非隨機、可預測的演算法，會依 20/40/60 天回看區間去獵取流動性**。這是 ICT 最核心、跨影片反覆出現的信念。
  - 出現於：`LBlK6JB0QS0`（PD array matrix應用於時間與價格）、`LRKtiysz4nA`（IPDA data ranges 整集主題）。
  - 引言："it's absolutely not random it's predetermined it's running on a script that refers to specific data points" (`LRKtiysz4nA`)
- **散戶交易者對市場毫無影響力，只是「跟著上车的跳蚤」**：市場由銀行/大機構(smart money)主導，散戶的止損/掛單才是演算法獵取的目標。
  - 出現於：`LifG37ky-Rg`（"retail traders are not going to do anything to this marketplace we are... fleas on the dog"）、`LRKtiysz4nA`（"they don't see you... you're not even a blip on the radar screen"）。
- **CFTC/COT 商業對沖者(commercial hedgers)持倉是真正的聰明錢訊號，但一般人以傳統方式(Larry Williams式)解讀COT是錯的**——ICT 宣稱自己用手繪、獨創方式重繪zero-sum line 才是正確用法。
  - 出現於：`LBlK6JB0QS0`。引言："no one else does what I do with the cot data"
- **利率(尤其10年期公債殖利率)是所有資產類別的根本驅動力**，貨幣會追逐殖利率(chase yield)。
  - 出現於：`LifG37ky-Rg`（"interest rates are the driving force whether you're a stock trader...")、`LBlK6JB0QS0`（interest rate differentials）。
- **季節性傾向 (seasonal tendency) 必須與技術面/COT對齊才有效，單獨看季節性會誤導**。
  - 出現於：`LBlK6JB0QS0`："seasonal tendency does not mean that it's going to happen... without technicals aligning... it will get you in trouble"
- **開盤/整理(consolidation)是聰明錢建倉階段，行情從盤整→擴張(range expansion)是市場真正的週期循環**，多數人只在行情已經噴出後才追價。
  - 出現於：`LifG37ky-Rg`（power of 3, daily range 收窄再噴出）、`M6kCfe5QgDg`（venom model 中的類似邏輯）。
- **市場結構轉變(market structure shift)每季(quarterly)大約發生一次**，是IPDA重新定位的錨點。
  - 出現於：`LRKtiysz4nA`（整集核心）。
- **開盤利益(open interest)的漲跌反映央行/做市商是否在提供買方/賣方流動性**，這與傳統技術分析教科書教法相反（例如盤整中OI下降=看漲而非看跌）。
  - 出現於：`LRKtiysz4nA`。
- **只有兩三個「巨額交易」(mega trade)每年值得真正大賺**，來自Larry Williams的概念，ICT用它形容比特幣、大豆等大行情。
  - 出現於：`lp9cfZrqwjA`。
- **不使用對角線趨勢線(trendline)，只信任水平支撐阻力**；不使用傳統指標(stochastic、Elliott Wave、Gartley/蝙蝠/harmonic patterns)，認為這些是「retail concepts」。
  - 出現於：`LifG37ky-Rg`（"I do not have faith in diagonal support resistance"; 嘲諷harmonic patterns "crab riding on the back of an eagle's wings"）。
- **交易紀律與個人責任(personal responsibility/self-control)是長期獲利的必要條件，若缺乏這些特質，交易不適合你**。
  - 出現於：`LBrsLPKXZ2E`（"if you can't have personal responsibility...this is absolutely the wrong career choice for you"）。
- **對加密貨幣/比特幣採取謹慎但好奇的旁觀者姿態**，反覆強調自己不持倉、無利益衝突，只是「看價格行為」。
  - 出現於：`lp9cfZrqwjA`（整集主題）。

## 2. 決策啟發式 (Decision Heuristics)

- 若10年期公債期貨下跌（=殖利率上升）→傾向做多相關貨幣(如歐元)；若殖利率下降→傾向做空貨幣。(`LifG37ky-Rg`)
- 若當週已在Sunday gap後立即上漲，且有看跌的總體條件(seasonal+COT+技術面共振)→假設Monday為週高點，小倉位試單，若Tuesday創新高則加碼但保持懷疑。(`LBlK6JB0QS0`)
- 一旦交易中開始感到不安/懷疑→減倉一部分（"take one of your contracts off"）以緩解心理壓力，而非死扛或全部離場。(`LBrsLPKXZ2E`)
- 高不確定性總體環境(如戰爭風險/PPI/CPI等新聞)下→縮小槓桿、只在關鍵位交易，不追價，且能接受長時間等待才進場。(`LifG37ky-Rg`)
- 每筆交易最大風險不超過帳戶2%（"do not risk more than the industry standard 2%"）。(`LifG37ky-Rg`)
- 非農/CPI等重大新聞週：週一、週二積極交易，週三之後轉為觀望("come off jets")，除非有明確反應。(`ley5HZs4bUM`即Asian killzone文件其實無此段，此段出自 `M6kCfe5QgDg`附近文件? 實際見於 file about cable/NFP)
- 若IPDA已經在近60天內掃過所有上下方流動性（買賣停損都被觸及），則需往60天範圍之外找下一個高/低點，預期會有大行情噴出。(`LRKtiysz4nA`)
- 不要在沒有更高時間框架(日線/4小時)支撐阻力位的情況下，在低時間框架(5分/15分/1小時)尋找型態進場；只在價格到達日線/4小時的reaction level時才考慮低時間框架的進場模式。(`LifG37ky-Rg`)
- OTE(optimal trade entry)進場：用62%、70.5%、79% fib回撤位作為進場區，只在高時間框架支撐/阻力+較大swing的背景下使用。(`LifG37ky-Rg`)
- 若目標達成(如週目標已滿足)，即使還能繼續盈利也選擇收手觀望，不貪多。(`LBrsLPKXZ2E`)
- 若模型（如Venom model）沒有給出訊號，寧可放棄該筆交易也不硬凹使用其他工具湊單；一個模型不該被期待覆蓋所有情境。(`M6kCfe5QgDg`)

## 3. 表達DNA (Expression DNA)

- **自信/挑釁交替的語氣**：常見句式「I'm not special. I don't have ESP. I'm not clairvoyant. But I'm light-years ahead」(`LBrsLPKXZ2E`)。
- **貶低競爭對手/模仿者**：稱使用他術語卻誤用概念的YouTuber為抄襲者、"buzzword" 使用者（"institutional this institutional that"）(`ley5HZs4bUM`)。批評harmonic patterns、Elliott wave、Gartley/蝙蝠形態為毫無根據的花招。
- **自嘲/幽默**：稱自己是「old guy」、「dinosaur」、用漫畫比喻（漫畫小偷雷聲 "the comic steals the thunder from the video"）(`LBrsLPKXZ2E`)；提到小時候買X光眼鏡被騙的故事(`LifG37ky-Rg`)。
- **反覆的if-then句式**：「If it does this, then I'll do that. Else, I will do this.」(`LBrsLPKXZ2E`) —— 明確的決策樹語言。
- **家庭/個人生活穿插**：常提及妻子、孫子（"pop pop my grandson"）、需要去購物/睡覺，塑造「有血有肉的老練交易者」形象。(`LBrsLPKXZ2E`)
- **免責聲明式的謙遜與傲慢並存**：對加密貨幣話題反覆聲明「這不是投資建議」「我不懂」的謙虛姿態，同時又不斷強調自己「叫頂/叫底」精準。(`lp9cfZrqwjA`)
- **對Larry Williams的反覆致敬**：多次引用其著作《How I Made One Million Dollars Trading Commodities Last Year》(1970s)，稱其為交易者必讀經典，但也說「我不是全盤照搬他的東西」。
- **重複的教學警語**："notepad moment"、"write this down and underline it several times"——用於強調重點。
- **對批評者/酸民的反擊**：「my haters」「show me where you shorted the highs... so shut up」(`LBrsLPKXZ2E`)。
- **獨創詞彙宣稱**：反覆聲明他的術語(kill zone, power of 3, OTE, venom model等)是自己原創，別人使用是誤用/抄襲。("I create these own my own names... please don't be confused if you see other people using those terms")

## 4. 決策紀錄 (Decision/Track Record Examples)

- **2017年3月 EUR/USD 一次性單發模型**：公開於Twitter預測歐元見頂於109.08，實際高點109.09（誤差1 pip）；預測週低點106.50，實際106.55（誤差5 pips）。用seasonal tendency + COT commercial selling + dollar index discount PD array三者匯合判斷。(`LBlK6JB0QS0`)
- **2026/07/15 PPI後NQ期貨即時交易**：早盤给出兩種情境(new week opening gap先觸及或sell-side先觸及)，用CPI/PPI作為Judas swing判斷，實盤金字塔式加倉放空，多次減倉，最終部分止損出場但整體獲利；影片中強調"33 years"經驗，仍常猜錯報告後方向。(`LBrsLPKXZ2E`)
- **2017年 AUD/USD**：以40天IPDA回看框架預測71.50支撐後反彈至75.70-75.80區間，並在文件中稱此為即時（非事後諸葛）預測。(`LRKtiysz4nA`)
- **比特幣時間線macro call**：2017年稱BTC會從6500漲到10000再到20000（準確）；2017年底反轉時預測「不會到20000」改稱會跌到6000（準確，之後又稱可能到3000，未精準達到但方向正確）；後於2018年喊出「會跌到100美元」的誇張說法作為修辭策略以擺脫加密貨幣追問者。2020年12月最新預測看向30000（後續是否應驗未在本檔案中確認）。也提到早於2012/2014年就有人訪談問他BTC意見，當時不感興趣。(`lp9cfZrqwjA`)
- **XRP**：在高點附近喊頂，稱之後"dead money"，形容為pump-and-dump/penny stock行為。(`lp9cfZrqwjA`)
- **Venom Model 2025示範交易**：在Asian session期間持有多單，主動減倉5口以防被套利，隨後部分停損、部分達到限價單目標，強調"content"心態（不強求每次都拿到最佳結果）。(`M6kCfe5QgDg`)

## 5. 時間線/背景線索 (Timeline/Biographical)

- 自稱交易生涯始於 **1992年**（`lp9cfZrqwjA`一處提及"since 1992"），但同影片後段又說「I started trading 1982」——**同一影片內部前後不一致**，需留意（見矛盾章節）。
- 專注外匯交易自 **2006年** 開始。(`lp9cfZrqwjA`)
- Mentorship 從 **2010年** 累積免費教材內容，Mentorship課程模組化教學延伸至2016-2017年。(`LBlK6JB0QS0`)
- 提及計畫在 **2017年冬季** 開始 signal service。(`LRKtiysz4nA`)
- Twitter帳號後來被停用/自我關閉，遷移重心至YouTube community tab；曾提及被Twitter審查凍結帳號。(`lp9cfZrqwjA`，約2020年底錄製)
- 與PayPal有合作關係處理mentorship金流。(`lp9cfZrqwjA`)
- **達成YouTube 100萬訂閱者**，收到YouTube金獎（Gold Creator Award），並提及"we're off to the Publishers for book one"——暗示當時正籌備出版第一本書。(`lHvu1qEdFRc`，低訊號檔案但含此背景線索)
- 提到自己有「obsessive compulsive disorder」，易分心，因此偏好短線/日內交易而非長期部位交易。(`lp9cfZrqwjA`)
- 提及祖母的口頭禪（"a lot of Rick morrow if you will if my grandmother"，原句有點不清楚，可能是"heartache"的替代詞或口誤）。(`LRKtiysz4nA`)

## 6. 矛盾與演變 (Contradictions/Evolution)

- **交易年資自述前後矛盾**：`lp9cfZrqwjA`中先說「i've been trading markets since 1992」，後段又說「i started trading 1982... i'm a dinosaur」。兩個數字相差10年，未在文件內部解釋或調和，僅記錄兩種說法皆存在。
- **對COT/commercial hedging數據的態度**：一方面說COT/公開的commitment of traders報告"nothing out there like what I'm showing you"、宣稱自創方法優於Larry Williams傳統教法(`LBlK6JB0QS0`)；但同時在其他地方大量引用並推崇Larry Williams的書為"essential reading"、"absolutely gold"，形容自己的方法論根基直接來自Larry Williams的公開interest/COT教學再"take it to another level"(`LRKtiysz4nA`, `lp9cfZrqwjA`)。此為「站在巨人肩膀上但又強調獨創性」的張力，兩邊都有明確措辭，暫不評斷孰真。
- **對「一天/一週不必每天交易」的態度演變**：早期教材(`LBlK6JB0QS0`, `LRKtiysz4nA`)強調精確度與高頻率規則化流程；2025年`M6kCfe5QgDg`則更強調"你的模型不需要每天都有交易"、允許自己錯過行情，語氣更寬容/佛系，可能反映後期教學風格從"精準預測"轉向"心理健康與紀律"的重心轉移。
- **對加密貨幣的立場隨時間變化**：2017年稱BTC會崩到100美元（修辭誇飾＋策略性打消追問者興趣）；到2020年底轉為"official interest"並認真討論30000美元目標，坦承此前"adversarial and kept at a distance"，本人明確承認立場轉變（非我方推論，是他自己陳述的演變）。(`lp9cfZrqwjA`)

---

## 批次二（檔案 10-25）補充

### 1. 心智模型候選（補充）

- **大範圍日(large range day)後的隔日早盤是「陷阱時段」，應避免交易**：ICT反覆強調大波動日隔天早盤容易被操縱、"chopped up"，寧可等下午段。出現於：`md9rxVLjY6A`（整集主題，"kryptonite to me"比喻）、`N4am6Jsp8N8`未直接提及但概念一致。
- **恢復手感需要先用demo交易，重新與市場「同步」**：離開盤面數天後，會先用demo/極小倉位重新校準感覺，而非直接重倉。出現於：`mdYFQIEcG38`（"I go through demo trades to get myself in sync"）、`N29ZJ-o31xs`（"I don't want to do anything else so I was like ok well just watch what I do"暗示重回節奏）。
- **月/週/日蠟燭具有分形(fractal)自相似性**，monthly premium/discount→weekly→daily→4H→1H逐級對應是核心分析框架（PD array matrix的具體操作方法）。出現於：`mQA8jCem9d0`（整集）。
- **開盤區間跳空(opening range gap/new week opening gap)本身是有效的draw on liquidity和進場工具**，非ICT原創但其"用法"是原創。出現於：`MqOVbd1oqZk`、`mQsT-xux5Xk`、`muL9EoMpYTM`。
- **支撐/阻力(support/resistance)是「宗教式信仰」，ICT明確否定其存在**，改以inefficiency/fair value gap/consequent encroachment取代；買方流動性(buy-side liquidity)不是阻力而是「draw」，賣方流動性不是支撐而是「draw」。反覆且激烈地強調（"that's a religion...it's a cult"）。出現於：`N4am6Jsp8N8`（大篇幅專門駁斥support/resistance）。
- **每週交易account growth不需要高風險/高頻率，2%風控+3:1報酬比即可複利致富**：小額本金也能十年翻成百萬美元的複利敘事。出現於：`mjVHmE1gVMg`（整集，含精確數學範例）。
- **IMP24 / algorithm 存在的「公開驗證」執念**：因被網路質疑是騙子，會刻意在別人的直播聊天室即時貼出精確價位預測以「無法被刪除竄改」的方式自證。出現於：`muL9EoMpYTM`（整集核心）。
- **對「支撐阻力education界」和其他交易教育者的持續攻擊**：稱其他人是"neophyte"、抄襲者、"John Fibilotti"等被點名嘲諷對象；反覆聲明"nothing like this exists"、"there's no other person I can say I learned that from"。出現於：`mQsT-xux5Xk`、`muL9EoMpYTM`、`N4am6Jsp8N8`。
- **總體利率背離(SMT divergence)可用於總體/中期方向判斷（10年期與30年期公債殖利率背離）**，並反覆聲明"please don't make a common knowledge"式的獨門秘技語氣。出現於：`MJwWUd_FM-k`。
- **交易者性格需與交易風格匹配**（引用Larry Williams的研究：衝動型適合當沖/剝頭皮，被動型適合部位/波段交易）。出現於：`mV1y9jIYyIU`。
- **「一個模型不可能覆蓋所有情境」的心理許可(permission)概念在後期(2025)教學中更明確化**，呼應第一批次中的矛盾演變觀察。出現於：`mQsT-xux5Xk`（"my Venom model"相關）、`mV1y9jIYyIU`亦有提及。

### 2. 決策啟發式（補充）

- 大範圍日後隔天早盤：即使有清楚的技術訊號(fair value gap+新聞事件)，也不進場，只做紙上推演；規則：candle突破設定的"neutralize"價位即視同停損出場保護。(`md9rxVLjY6A`)
- 若交易中已達成當週目標，即使還可能有更多空間也主動收手（"that finishes my week for being bullish"）。(`LBrsLPKXZ2E`一致，`mQA8jCem9d0`概念呼應)
- 若某方向(如做空)已missing部分邏輯確認(如未見swing high失敗)，則寧可不做，等下一個明確setup，不勉強凑單。(`mdYFQIEcG38`)
- 非農/CPI週：週三、週四、週五最後一小時絕不交易，"final hour trading on non-farm payroll Friday final hour it's a big gamble"。(`muL9EoMpYTM`)
- 使用IPDA/monthly-weekly-daily-4H-1H逐級篩選：只在最低阻力流動性路徑(low resistance liquidity run)明確時才進場，若某級時間框架已消耗掉PD array，需等待新的array形成。(`mQA8jCem9d0`)
- 部位管理：達到第一目標可分批減倉(50%/25%等)，move stop to breakeven，剩餘部位留倉搏更大目標；即使最終沒等到最佳出場，也視為滿意結果而非失敗。(`MqOVbd1oqZk`, `mQA8jCem9d0`)
- 若交易錯過理想進場點（因為價格移動過快），寧可放棄也不追價；"if it's too fast, I can't be a part of it"。(`muL9EoMpYTM`)
- 停損位置：貼近swing low/high本身（而非額外多留5-10-20 pips），理由是如果會跌破79% fib，代表整個看漲前提已無效，應直接認賠而非硬凹更寬停損。(`N29ZJ-o31xs`)
- 60/40/20天IPDA回看區間都已被清空(即高低點都已觸及)時，需往回看範圍之外找下一個高/低點作為目標，預期會有大行情。(`LRKtiysz4nA`一致主題)
- 三年以下經驗的交易者，虧損後當天禁止立即再進場報復性交易("revenge trade")，必須先冷靜、用demo/紙上驗證想法是否依然成立。(`mV1y9jIYyIU`)

### 3. 表達DNA（補充）

- **重複的教學儀式感詞句**："notepad moment"、"write this down"仍反覆出現；新增"Old man still got it"這類自嘲老年梗、"Grandpa syndrome"、"53 year old eyes"。(`mQsT-xux5Xk`)
- **對批評者的正面迎戰而非迴避**：明確點名"a couple guys"批評他"brag too much"，回應"I'm not bragging I'm speaking facts"。(`muL9EoMpYTM`)
- **家庭生活持續穿插**：孫子Caleb在直播現場對話("Did you sleep good last night?")、提及"married men you know what I'm talking about"式的已婚男性幽默、"my wife"多次出現。(`mQsT-xux5Xk`, `LBrsLPKXZ2E`)
- **對「其他人抄襲他的術語」持續控訴**：稱他人是"neophyte"、"a fraud... they don't even know what they're teaching"；同時聲明自己也从未embarrass被抓到造假("I've never faked my p&l")。(`muL9EoMpYTM`)
- **比喻與流行文化引用**：漫威superman/kryptonite比喻交易弱點(`md9rxVLjY6A`)、《駭客任務》"there is no spoon"比喻沒有buying/selling pressure(`muL9EoMpYTM`)、Marty McFly/回到未來梗(`mQsT-xux5Xk`)。
- **強烈的「我是原創者」主張與版權焦慮**：多次警告有人想把他的概念寫成Amazon書出售，威脅要去留負評("I'll probably go into your comment section and leave a review and tell them don't look at your stuff because it's garbage")。(`mQsT-xux5Xk`)
- **教學中滲入人生哲理/心靈雞湯語氣**：如"you have to submit to time"、"toxic thinking"、"deposit vs withdrawal"比喻交易心態。(`mV1y9jIYyIU`)
- **謙遜與傲慢並存的招牌修辭**："I'm not trying to be arrogant... but"句式反覆出現於自誇段落前後。(`N4am6Jsp8N8`)

### 4. 決策紀錄（補充）

- **2026/07/15附近NQ交易**（`LBrsLPKXZ2E`已記錄）另有`mQsT-xux5Xk`(2025/04/30 NQ Review)：即時展示entry/exit，含與助理"Caleb"的對話，收到停損但整體評論"old man still got it"。
- **2025/02/05 Forex & NQ Review**：EUR/USD與GBP/USD比較（relative strength分析），聲稱只對Cable感興趣因其為upside leader，實際先觸及目標；此為明確的跨市場比較決策紀錄。(`muL9EoMpYTM`)
- **2025年於Tanya Trades直播中即時公開喊單**：在他人直播聊天室貼出精確價位(21508做多、目標21615、然後看3pm relative equal highs)，並在影片中回放驗證完全命中，作為"無法被事後編輯"的公開紀錄範例。(`muL9EoMpYTM`)——這是本批次中最具「可驗證公開紀錄」性質的段落。
- **2022/09/02 Emini S&P AM&PM Session Review**：非農週五交易，公開Twitter發文紀錄（"draw a horizontal line at 40 17.75"），且明確展示"false bull flag"辨識，最終達成目標。(`mkAuOOPTEKw`)
- **2023/07/09-07/14 Dollar Index/EUR/ES/NASDAQ 週回顧**：聲稱一週前已在Sunday review精準預告weekly volume imbalance、breaker、weekly TGIF 20%回撤位，並在此片逐一比對兌現情況（自我驗證式敘事）。(`N4am6Jsp8N8`)
- **2022年8月澳洲/初期demo重新校準交易**：離開charts一週後先用demo交易，交易反轉後被stop out，明確承認"I was wrong"、"I did not see the afternoon unfolding the way it did"。(`mdYFQIEcG38`)——罕見的公開坦承误判且未做多余辩解的例子。
- **2023/01/31 PM Session New Week Opening Gap**：即時交易展示金字塔加倉、consequent encroachment概念應用、分批減倉直到只剩尾單。(`MqOVbd1oqZk`)

### 5. 時間線/背景線索（補充）

- 自述"I've been doing this for 33 years"（`LBrsLPKXZ2E`，對應2026年）——若從33年回推約落在1993年，与第一批次"1992"說法較接近，但仍与同集"1982"說法矛盾（見矛盾章節）。
- 自述"I've been doing this for 23 plus years"于`mV1y9jIYyIU`(webinar，未標明年份但語境像2010年代早期)——若23年回推約2000年前後，与其他自述的1990年代初起點不完全一致，可能是不同起算基準（開始交易 vs. 開始盈利/開始教學）。
- 提及自己"my understanding of the marketplace is rooted on things that I've codified in 1996"——**1996年**是另一个反覆出現的關鍵年份，指其方法論成形/系統化的時間點。(`N4am6Jsp8N8`)
- 提及YouTube訂閱數"771,000 students on this YouTube channel"于2023年（`N4am6Jsp8N8`），可與批次一中100萬訂閱里程碑對照，推算訂閱成長時間軸。
- 提及"since I began online talking about trading"及在baby pips論壇任教起點，从2010年一直到"I finally left there"。(`mV1y9jIYyIU`)
- 提及2022年因背部痙攣與偏頭痛(back spasms and migraines)導致暫停更新。(`mdYFQIEcG38`)
- 提及自己在mentorship結束後("I don't have it anymore I won't do it anymore")已於2025年徹底停止付費mentorship，僅剩YouTube與Telegram頻道（近7萬人）。(`muL9EoMpYTM`)
- 提及"Middle River Maryland"為其所在地。(`N4am6Jsp8N8`)
- 提及PayPal合作處理其mentorship金流，与批次一致。(`muL9EoMpYTM`一致`lp9cfZrqwjA`)

### 6. 矛盾與演變（補充）

- **交易年資的第三個版本**：`LBrsLPKXZ2E`(2026年)稱"I've been doing this for 33 years"（約合1993年起點），`mV1y9jIYyIU`稱"23 plus years"（時間點不明但引用"back in the 90s when I first started"），`N4am6Jsp8N8`(2023年)提及方法論"codified in 1996"。三者与批次一的"1992" vs "1982"共構成至少三個不同的起始年份說法（1982、1992、1996方法論成形、"33年"推算1993年）。這些說法可能分別指「開始交易」「開始盈利穩定」「方法論系統化」三個不同里程碑，但影片中並未明確區分，呈現自述時間線的持續模糊/不一致。
- **對「support and resistance」的態度**：`N4am6Jsp8N8`中極力否定support/resistance存在（"it's a religion...it's a cult"），但在其他教學片中（如`LifG37ky-Rg`早年内容）大量使用"resistance"、"support"字眼描述PD array的行為（雖然辯稱意涵不同，是"draw on liquidity"而非傳統支撐阻力）。此為術語使用上的張力：早期教材更頻繁直接用support/resistance語言，後期教材更堅持要用其自創詞彙且明確與傳統support/resistance切割。
- **對「每天都該有交易」的態度**：`mjVHmE1gVMg`中強調小資金穩定複利，鼓勵找到3:1報酬比並執行；`md9rxVLjY6A`及`mQsT-xux5Xk`则更强调"你的模型不需要每天交易"，甚至讚賞自己"疲憊時就不執行"的節制。兩者並不直接矛盾（可視為紀律的一體兩面），但語氣重心從"如何找到更多機會執行"逐漸轉向"如何克制不做"，與批次一觀察到的演變一致。
- **對他人抄襲的憤怒 vs 自己承認受教於Larry Williams**：本批次再次出現（`N4am6Jsp8N8`："I learned that from Larry Williams and I learned that in 1995"），與同集稍早聲稱"there is not one single person on YouTube or anywhere else... I author these things no one taught me these things no one mentored me"之間的張力（同一集內部）——即同集中一方面說「沒人教過我」，另一方面又具體指名Larry Williams教了他seasonal tendency失效反轉的概念。此為同一影片內部的直接措辭矛盾，值得記錄。

---

## 批次三（檔案 26-33）補充

### 1. 心智模型候選（補充）

- **市場「100%被工程化控制」，隨機性完全不存在**：明確以「我能連續多年精準叫出pip級價位」作為證據反駁市場隨機論。出現於：`n7SPAK_tpN8`（"my belief is that the markets are 100 percent engineered...absolutely controlled to the very pip"）。
- **SMT背離(Smart Money Technique divergence)／underlying vs benchmark錯位**是判斷買賣程式(buy/sell program)的核心分析框架，透過「基準貨幣/指數 vs 交易標的」的高低點不對稱來偵測聰明錢的真實意圖（例如標的破前低但對應基準未同步破低=吸籌）。出現於：`n7SPAK_tpN8`（大篇幅系統化教學）、`N8_8tEw2_44`（結合10年期公債殖利率驗證SMT背離）。
- **支撐/阻力再次被明確定調為「宗教」「邪教」，並自嘲接受"cult of winning"稱號**：這是本批次中最戲劇化的自我定位段落，直接擁抱外界對他的"邪教"指控並反轉為正面標籤。出現於：`N3qz13Hl-gg`（"we're a cult...we're the cult of winning"）。
- **時間優先於價格(time and price theory, time first)**：算法先決定"何時"，再決定"何地"，這比單純看價位更重要，是其反覆用來否定「純價格形態分析」的立論基礎。出現於：`NkwqJBzgQwo`。
- **機構做市商在紐約午盤(New York lunch, 12-1pm)刻意製造停損獵殺(stop hunt)**，形成假支撐(relative equal lows)引誘散戶，是"macro"現象之一，反覆出現於多集。出現於：`N3qz13Hl-gg`、`NkwqJBzgQwo`。
- **"Macro"時間窗口概念**（如9:50-10:10、2:52-3:10等特定分鐘區間）是算法啟動流動性獵取的固定時間點，屬於他自創但拒絕完整公開的核心方法論之一（留給"即將出版的書"）。出現於：`NkwqJBzgQwo`。
- **對「其他人會把他的概念寫成書搶先出版」的持續焦慮與防衛**：多次聲明特意保留部分內容不教，是為了將來出版時能證明原創性("once I put it in print... I'm offended by that because you're trying to get something out ahead of me")。出現於：`N3qz13Hl-gg`（提及計畫出版四本書，三本技術+一本小說）。
- **一天只需要一次交易機會，過度交易(over-trading)是散戶通病**：Central Bank Dealers Range模型明確教導"不是每天都要進場"、只找最佳時段(2-8pm New York time)。出現於：`nI1AMOC1pro`。

### 2. 決策啟發式（補充）

- **IPDA回看只需用20天範圍即可（非20/40/60全套）**：於具體交易計畫(price action model 5)中簡化為"we don't count Sundays...20 trading days...this is the only IPDA data range you have to be concerned about"，顯示教學隨模組不同而簡化規則。(`NB7Bku099tU`)
- **明確的資金管理規則**：連續5筆獲利後主動把風險%減半（防止過度自信）；虧損後恢復到滿倉風險前，只需先追回50%虧損即可，非100%。(`NB7Bku099tU`)
- **停損位置＝該高/低點外加15 pips固定緩衝**（非隨意抓一個數字），達到25%/50%/75%預期獲利時，停損依序上移。(`NB7Bku099tU`)
- **Central Bank Dealers Range模型**：下午2點-8點(紐約時間)區間若小於40 pips（理想20-30 pips），可用標準差(standard deviation)推算後續倫敦時段高低點；若該區間大於40 pips則放棄用此模型（"we have to allow the market to do whatever it wants"）。(`nI1AMOC1pro`)
- **交易日過濾規則**：週二、三、四為主力交易日，週一、五過濾掉不做；週四是否交易取決於週二/週三的表現組合（若週二週三都已是大範圍且順向，週四不做；若週二小範圍週三大範圍，週四可做）。(`NB7Bku099tU`)
- **量化SMT背離+10年期殖利率的三重驗證(triad)**：貨幣對SMT背離+殖利率背離+開盤利益(open interest)變化三者一致時，才視為高機率設置，單一訊號不足採信。(`N8_8tEw2_44`)
- **午盤(New York lunch, 12-1pm)絕對禁止交易**，无论看起来多有吸引力。(`nI1AMOC1pro`概念一致`N29ZJ-o31xs`)
- **一次性大額交易展示（100k in 4 days, turtle soup模型）**：進場後可在特定價位金字塔加倉，但加倉必須等到隔日午夜後（跨日）才進行，且明確設定"不會追蹤全程盤面，只等特定價位觸發"。(`N9RW9v2kOoY`)

### 3. 表達DNA（補充）

- **正式擁抱「邪教」("cult")標籤並反轉為榮譽勳章**："everybody likes to say we're a cult and I've gladly accepted that and we're the cult of winning"。(`N3qz13Hl-gg`)
- **對「支撐阻力」的攻擊持續升級，帶有濃厚的宗教/信仰隱喻**（"it's a religion... you have to have more faith in that"）。(`N4am6Jsp8N8`延續, `NkwqJBzgQwo`, `N3qz13Hl-gg`)
- **反覆使用肢體/生活化比喻解釋機構思維**：如"who benefits the most"式的換位思考句式，教學生從smart money角度反問自己。(`N3qz13Hl-gg`)
- **對自己「經驗豐富但仍保留exit時機作為弱點」的罕見自我坦承**："I'm never really satisfied with my exit...that's been a way for me to really nail down a specific criteria"。(`nBschaCBNLU`)——這是少見的具體弱點自曝，而非泛泛謙虛。
- **明確自稱寫書計畫**：四本書（三本技術理論+一本小說），並以「達成YouTube百萬訂閱」作為出版觸發條件，呼應批次一`lHvu1qEdFRc`的"we're off to the publishers for book one"。(`N3qz13Hl-gg`)
- **持續的"institutional order flow entry drill"（IOFED）等自創縮寫詞彙堆疊**，並主動嘲笑自己造的詞拗口（"that's a tongue twister"）。(`N3qz13Hl-gg`)
- **對批評者的「挑戰證明」語氣**：反覆用"don't take my word for it, go measure it yourself"、"I can't edit it, it's already uploaded on YouTube, time and date stamped"作為自證話術。(`NeZlyG8FZLQ`)

### 4. 決策紀錄（補充）

- **2024/09/06 NQ Live Execution「OSOK」100k交易**：18小時盤面壓縮成9分鐘影片，展示turtle soup空單、金字塔加倉、目標打到10萬美元獲利，並主動吐槽網路酸民「4天賺10萬，我的問題是你怎麼花這麼久？」("what took you so long")。(`N9RW9v2kOoY`)
- **2017年10月 USD/CAD Demo交易**：展示OTE進場、日內20 pip目標推算、大數字關卡(big figure)概念的實戰應用，坦承"my weakness as a trader is exits"。(`nBschaCBNLU`)
- **2023年ES(E-mini S&P)週回顧「Precision Results」**：聲稱前一晚已在錄影中預告當週weekly volume imbalance、buy-side、daily fair value gap會被觸及，並用未剪輯、已上傳YouTube的影片作為「無法竄改」的自證。(`NeZlyG8FZLQ`)
- **2023/03/27 ES Review**：詳細逐分鐘展示9:30開盤後的macro時間窗口(9:50-10:10)、午盤停損獵殺、PM session silver bullet、最後15分鐘市場收盤前(market-on-close macro)交易邏輯，並多次在Twitter即時公開喊價位（4034 buy side、4018 sell side、4027.75目標，皆宣稱precisely delivered）。(`NkwqJBzgQwo`)
- **2016年12月-2017年1月 Dollar Index/EUR quarterly shift分析**：以2015年12月1日為錨點的60/40/20天回看框架，回溯驗證美元指數與歐元的quarterly shift precision（"the 60 day IPDA data range nails it on the very high"）。(`n7SPAK_tpN8`)

### 5. 時間線/背景線索（補充）

- **明確提及計畫出版四本書**：三本技術/演算法理論、一本小說(fiction)，以達成100萬YouTube訂閱作為觸發承諾。(`N3qz13Hl-gg`)——與批次一`lHvu1qEdFRc`（"we're off to the Publishers for book one"）構成完整時間線佐證。
- **"my studies over the last two decades"**（`nI1AMOC1pro`，該片為2017年4月mentorship內容）→ 推算約1997年前後開始系統化研究，與先前批次"1996年codified"說法時間點高度吻合，是本次最能相互印証的時間錨點。
- 提及"seven years teaching Forex online"于`nI1AMOC1pro`(2017年)——回推約2010年開始網路教學，與"baby pips"起點(`mV1y9jIYyIU`)一致。

### 6. 矛盾與演變（補充）

- **"1996年方法論codified" vs "過去二十年的研究(over the last two decades，於2017年發表)"**：後者回推約1997年，兩者高度吻合，屬於本批次中少見的**時間線自洽**案例，值得放入最終時間軸作為相對可信的錨點（區別於1982/1992/33年等互相矛盾的「開始交易」年份）。
- **對「支撐阻力」的態度貫穿多集且語氣逐漸激化**：從早期教材中頻繁直接使用"resistance"、"support"描述PD array行為（如批次一`LifG37ky-Rg`），到本批次多集（`N4am6Jsp8N8`、`NkwqJBzgQwo`、`N3qz13Hl-gg`）用近乎宗教批判的語言全面否定"support and resistance"概念存在。此為用詞立場隨時間顯著強化/激化的演變模式，而非單純矛盾。
- **保留核心內容不公開教學 vs 免費教學者形象**：`N3qz13Hl-gg`中明確表示「有些東西留給書」「不會公開最好的東西」，与其一貫「completely free, I don't sell anything, I don't need your money」的形象論述之間存在張力——一邊強調完全免費無私分享，一邊承認策略性保留關鍵細節以防止他人搶先出版/抄襲。兩種說法在同一批次不同影片中並存，未見自我調和。

---

## 批次四（檔案 34-39）補充

### 1. 心智模型候選（補充）

- **Breaker(斷路器)型態是判斷市場結構(market structure)最強工具之一**：低點被跌破後smart money累積sell stops，行情回到前高即轉為看漲訊號（反之亦然），是反覆用於「趨勢反轉判讀」的核心工具。出現於：`Nl-eKxgPWI4`（整集主題）。
- **外部區間流動性(external range liquidity) vs 內部區間流動性(internal range liquidity)**：在區間內買賣(internal)、在區間外停損出場(external)是其個人偏好的「進出場配對邏輯」，並反覆強調"my entries are internal range liquidity entries with exits at external range liquidity"。出現於：`npL3ZXJ5zOU`（整集）。
- **低阻力流動性路徑(low resistance liquidity run) vs 高阻力流動性路徑(high resistance liquidity run)**：判斷交易是否該做的核心過濾器——若與更高時間框架(月/週)方向一致，回撤買入後上方基本無阻力；若逆勢，則屬高阻力應避開。出現於：`npL3ZXJ5zOU`。
- **訂單塊(order block)定義的「唯一標準答案」**：他明確聲稱"only my students and mentorship know what an order block is"，並定義為"a change in the state of delivery"，藉此否定其他教育者對這個詞的用法。出現於：`nQfHZ2DEJ8c`。
- **高頻演算法(high frequency trading algorithms)在1-3分鐘圖上留下的「簽名」是可辨識、可回測的**，且反覆宣稱這是他「原創」於2010年baby pips、更早於1996年一對一教學。出現於：`nQfHZ2DEJ8c`。
- **完全否定「買賣壓力(buying/selling pressure)」作為價格驅動力**，改以"the algorithm constantly offering price at a higher/lower price"取代，滑點(slippage)只是执行細節而非驅動力證據。出現於：`nQfHZ2DEJ8c`。
- **個人責任(personal responsibility)是他長年拒絕開放付費會員/拒絕直播實盤喊單的核心理由**：明確以他人在留言區聲稱「照著做虧損1000美元」為例，強調這正是他多年不願意做直播交易教學的原因。出現於：`nv0ey5UyOmY`（大篇幅論述）。
- **模型驗證的「反向邏輯」：沒有形成預期型態=模型有效，而非模型失敗**——若市場沒有走出他預告的劇本，代表過濾機制正確發揮作用避免了一筆爛單，而非代表分析錯誤。出現於：`nv0ey5UyOmY`（"it doesn't mean that the models broke...it just means the market did not provide the structure"）。

### 2. 決策啟發式（補充）

- 判斷交易是否「太晚進場」的量化標準：只要價格仍低於（若做多）先前定義的swing high（尚未失效的錨點），即使錯過最佳進場點仍可追價進場，只是風險報酬比變差。出現於：`ntqw8rgXUss`。
- 週線目標設定法：用多組不同幅度的價格擺動(price swing)分別做Fibonacci extension，尋找多組延伸位「群聚重疊(confluence)」的區域作為目標，取最接近機構整數關卡(5或0結尾)的價位。出現於：`nNEt9QTCTtk`。
- 出場時故意「提前一點」離場（不試圖抓到最低點/最高點），理由是不同券商報價有落差，早出場能確保成交。出現於：`nNEt9QTCTtk`（"I always leave a little bit on that's why I see most of my exits I always have that little bit of a tail"）。
- 交易篩選的pip數門檻：15分鐘/1小時圖上，回撤幅度需達40 pips以上才值得進場，理由是若只有20 pips無法覆蓋點差和目標利潤。出現於：`npL3ZXJ5zOU`。
- 市場結構轉變(market structure shift)確認需要「兩步驗證」：1) 假突破前高/前低(stop run)；2) 隨後出現位移(displacement)並跌破/突破前一個短期高低點，兩者缺一不可，否則不算有效訊號。出現於：`nQfHZ2DEJ8c`、`nv0ey5UyOmY`。
- Central Bank Dealers Range模型的具體交易規則另有版本：進場只在特定fair value gap／displacement／entry drill三重確認下才做，若當日邏輯未成形，寧可整天不交易也不勉強找替代訊號。出現於：`nv0ey5UyOmY`（NFP前一天的空手案例）。
- 微型合約(micro contracts)分批加減倉並在到達目标价位前就主動獲利了結部分部位（"take six off to fund the position roll the stops to even"），用「先落袋為安」降低心理壓力。出現於：`NUdu1n-ML98`。

### 3. 表達DNA（補充）

- **對留言區「聲稱因為聽他的話虧錢」的網友進行公開駁斥與威脅封鎖**：明確表示會直接刪除/封鎖任何暗示他該為他人虧損負責的留言，並反覆用「我不是伸手進螢幕幫你按下單按鈕的人」之類的具體畫面比喻撇清責任。出現於：`nv0ey5UyOmY`。
- **"practice this speech, write it down in your journal"式的呼籲**：要求觀眾在交易日誌上手寫承諾"I promise that as long as I'm doing this I'm going to endure losses"，帶有類似宗教式的儀式感語言。出現於：`nv0ey5UyOmY`。
- **對「其他人教錯我的概念」的攻擊持續且更具體**：直接批評有人在教order block卻用錯誤定義，"you're actually teaching it incorrectly and without the real context"。出現於：`nQfHZ2DEJ8c`。
- **自稱即將滿30年交易生涯（"November 5th"）成為反覆強調的資歷錨點**：多次以「今年是我交易第30年」作為權威來源，用來對抗批評者。出現於：`nQfHZ2DEJ8c`（"my 30th anniversary november 5th... 30 years"）。
- **警告付費mentorship不會再開放的持續聲明，與「我不需要你的錢」的姿態並存**：反覆聲明2018年之後決定用"rolling enrollment"模式重開mentorship（每月$150 x 12個月），但同時強調錢不是重點，是為了補償他投入的時間與"post-mentorship access"。出現於：`ntqw8rgXUss`。
- **自嘲式坦承「我的弱點是出場」**：與批次三`nBschaCBNLU`一致的自我認知重複出現："I've made it very candid about my weaknesses as a trader it's the exits"。出現於：`ntqw8rgXUss`。

### 4. 決策紀錄（補充）

- **2017/11/10週 USD/CAD市場回顧**：公開展示故意「先在最佳進場點平倉出場」再重新示範「即使錯過最佳進場仍可追價進場」的教學實驗，明確承認"I opened the invitation for your mind to go to work...I was measuring your level of conviction"，屬於刻意設計的教學操縱（自曝的心理測試）。並在此片中宣布即將於2018年重開mentorship，訂價每月150美元。(`ntqw8rgXUss`)
- **2022/05/05（週四，NFP前一天）NQ/ES分析未觸發交易**：於YouTube community頁面公開貼出「觀察中」的價位與情境，最終市場未走出預期劇本，坦承「今天沒有交易」並用此作為「模型具備有效性（因為沒有勉強進場）」的正面案例。(`nv0ey5UyOmY`)
- **micro NASDAQ執行範例（未標明日期）**：金字塔式加倉、部分提前減倉，展示entry price around 14160-14220區間的目標推算與實際成交。(`NUdu1n-ML98`)
- **Dollar Yen月度低阻力流動性路徑分析（回溯至2016年美國大選前後）**：詳細展示月線fair value gap如何在數週內逐步被價格"efficiently delivered"，並提及"in that area many times average around 113.50 to 113.25"作為機構建倉均價的具體描述。(`npL3ZXJ5zOU`)

### 5. 時間線/背景線索（補充）

- **"my 30th anniversary november 5th... this november 5th 30 years"**（`nQfHZ2DEJ8c`，2022年1月25日錄製）——回推至**1992年11月5日**為其交易生涯的具體起點日期。這是本研究批次中最精確的單一日期自述，可作為與先前"1982/1992/33年/1996codified"等說法比對的關鍵錨點：1992年11月起點與批次一"33年"(推算至2026年約1993年)、批次二"since 1992"高度吻合，但仍與"1982"及"since 1996 codified"（可能指方法論成熟年份而非交易起點）存在差異。
- **提及"probably sound like a young guy but I'm actually getting turned 50"**於`nQfHZ2DEJ8c`（2022年1月），與1992年11月交易起點推算（30年資歷）大致自洽，暗示出生年約1972年前後。
- **明確提及664人完成mentorship、867人報名過**的具體數字，用以說明「完成課程≠達到他的能力」。(`ntqw8rgXUss`)
- **2022年五月提及正處於mentorship早期發展階段（development stage）**，並多次表示會員區留言板"community tab"取代了他過去在論壇/Twitter上的即時互動模式。(`nv0ey5UyOmY`)

### 6. 矛盾與演變（補充）

- **交易起點年份再添新證據**：本批次`nQfHZ2DEJ8c`給出最精確的說法——"1992年11月5日"，且與"33年"(批次一，2026年)、"since 1992"(批次二`lp9cfZrqwjA`)高度吻合。這強化了一個假設：**1992年11月可能是相對可信的「開始交易」錨點**，而先前出現的"1982"（`lp9cfZrqwjA`同集內部矛盾）可能是口誤或指涉其他里程碑（如最早接觸/學習交易的年份，而非正式開始交易）。建議在最終人物側寫中，將1992年11月作為主要採用版本，1982年/1996年視為需要進一步排查的旁支說法。
- **對於「完全免費、不需要你的錢」vs「即將重新開放付費mentorship」的表態**：`ntqw8rgXUss`中一方面說"I don't need your money"，另一方面詳細規劃了每月150美元、滾動式招生的付費方案，並解釋這是「補償他的時間」而非追求利潤——此為一貫的立場，非全新矛盾，但值得記錄其「免費／收費」自我定位始終伴隨著防禦性解釋。
- **對「該不該直播實盤喊單」的立場**：`nv0ey5UyOmY`中強調多年來因為「他人責任感缺失」而堅持不做即時實盤買賣指令；但同一批次中`ntqw8rgXUss`、批次三的多支影片、以及批次二的`muL9EoMpYTM`（在Tanya Trades直播間即時喊價）都顯示他其實一直有在做類似「即時公開喊價」的行為（只是包裝成「觀察」「demo」而非「指令」）。這反映一種修辭策略上的區隔：他嚴格區分「這是我的觀察/demo」與「這是買賣建議」，但外部行為（即時公開精確價位）在兩種情境下高度相似，本質差異更多在於法律免責語言而非行為本身。

---

## 批次五（檔案 40-45，最終批次）補充

### 1. 心智模型候選（補充）

- **理想季節性(ideal seasonal tendency)＝兩個相關市場的季節性圖必須「完全鏡射對立」才算高機率**：不是單看一個市場的季節性，而是要同時比對「基準美元指數」與「目標貨幣」兩條季節性曲線是否方向相反，才視為ideal。並反覆強調此為40年vs15年雙重數據對照更具信心。出現於：`O2Sio7opKxo`（整集）。
- **趨勢線(trend line/對角線支撐阻力)被完整定調為「零統計優勢」的散戶陷阱**，並提出具體反向交易法：當看到經典上升趨勢線第三次觸碰時，反而預期該處是做市商設置的「賣出陷阱(bearish order block/turtle soup)」。出現於：`o8NfSK-pUlE`（整集核心）。
- **「精確度不是重點，責任感才是重點」的教育哲學**：多次強調他教學生"study/watch/observe"而非"buy/sell"，藉此在法律與心理上與學生的實際交易結果切割。出現於：`nv0ey5UyOmY`。
- **模型「未觸發」＝模型驗證成功**的邏輯再度出現（與批次三`N3qz13Hl-gg`、批次四`nv0ey5UyOmY`一致）——若當日沒有形成預期的位移(displacement)確認，代表過濾機制正確運作，而非策略失效。
- **四小時圖(4-hour chart)是his "one shot one kill"短線交易的最愛時間框架**，理由是能同時看到monthly/weekly/daily PD array匯聚，且用control+Y可疊加週分界線做每週高低點預判練習。出現於：`O69iFqP1j7o`。
- **週線範圍30-50%通常在週三倫敦收盤前就完成**：是他教學生"不要在週四五還死抱著追逐整週波段"的具體量化依據。出現於：`O69iFqP1j7o`。

### 2. 決策啟發式（補充）

- **趨勢線交易的具體反向邏輯**：上升趨勢線第三次觸碰的高點，若高時間框架顯示看跌，則在該高點做空（抓turtle soup/bearish order block）；下降趨勢線第三次觸碰的低點，若高時間框架看漲，則在該低點做多。出現於：`o8NfSK-pUlE`。
- **虧損後若原始邏輯依然成立，可以直接重新進場（不因自尊/恐懼而卻步）**：EUR/USD交易中止損位設太緊被掃出後，判斷邏輯仍有效，立刻用同等（甚至更小）槓桿重新進場。出現於：`nz7Y5lrAqgM`。
- **明確的部位風控規則**：单笔最大风险原则上2%，若某日已有一筆滿倉虧損，重新進場只能用剩餘風險額度（如虧損後只剩不到0.5%可用），不能同等重新加碼到滿倉。出現於：`nz7Y5lrAqgM`。
- **主動「見好就收」以滿足自我要求（OCD傾向）**：明確自述因強迫症傾向，即使技術上還能抱更多利潤，也會提前於預期目標方向部分出場以「安撫自己的完美主義」，屬於針對自身心理弱點設計的具體因應策略（非泛泛而談）。出現於：`nz7Y5lrAqgM`（"I struggle with obsessive-compulsive disorder...I've given myself permission to exit in the direction of my expected targets"）。
- **判斷「錯過的移動是否該追」的量化界線**：只要當前價位仍低於（做多情境）先前定義的關鍵swing high，且下方無失效訊號，即可接受非最佳進場點追價，屬於可接受風險範圍。出現於：`nz7Y5lrAqgM`（與批次四`ntqw8rgXUss`一致主題）。

### 3. 表達DNA（補充）

- **"ICT unicorn"自嘲式標題梗**：刻意將展示虧損交易的影片稱為「獨角獸」，反諷網路上「ICT從不展示虧損」的批評指控，並在影片中完整播出停損過程。出現於：`nz7Y5lrAqgM`。
- **持續強調「我不是伸手進你的手機幫你按下單」的畫面化撇清責任語言**（"I didn't reach through the screen...I didn't meet you at your job and press your cell phone"），與批次四`nv0ey5UyOmY`用語高度一致，屬其反覆使用的招牌修辭。
- **自嘲強迫症(OCD)影響交易與生活**：提及"my home is like that everything in my house is exactly where I want it"，將個人生活習慣與交易心理連結，是少見的具體人格自剖。出現於：`nz7Y5lrAqgM`。
- **「射擊教練/狙擊訓練生」比喻**：把自己定位為「指向目標的教官」，學生是「持槍瞄準扣扳機的狙擊手」，強調他只指方向、學生要自己執行與承擔後果。出現於：`nz7Y5lrAqgM`。
- **持續使用「電影般精準」的自我形容**：如"ICT symmetrical price swing you can actually see...perfectly to the pip"，強調技術展示的絕對精準度作為權威證明。出現於：`o8snDyA6kok`（低訊號檔案但仍可見此語言模式）。

### 4. 決策紀錄（補充）

- **EUR/USD實盤損益公開示範（"ICT unicorn"）**：第一次進場因停損設太緊被掃出（虧損200美元），判斷邏輯依然有效後立即以相同小槓桿重新進場並最終達成85%左右預期目標，明確自曝「本該多減倉一次卻忘記做」的操作疏漏。(`nz7Y5lrAqgM`)
- **2022/05/05 NFP前一日NQ/ES「未觸發交易」案例**：在YouTube community頁面公開貼出觀察區間，最終市場未形成位移確認，全程未下單，並用此作為模型有效性佐證（與批次四已記錄的同一事件對應同一集`nv0ey5UyOmY`，此處為完整內容確認）。
- **2016年11月 GBP/USD 趨勢線陷阱案例**：具體展示"52.34"、"150.60"等機構參考價位，如何在趨勢線散戶陷阱中被"turtle soup"式邏輯正確預判。(`o8NfSK-pUlE`)

### 5. 時間線/背景線索（補充）

- **"I've been doing this for 24 years coming up...just about the end of the month we're actually producing this video"**（`o8NfSK-pUlE`，2016年11月教材）——回推至**1992年11-12月**為交易起點，與批次四`nQfHZ2DEJ8c`「1992年11月5日滿30年」的說法（2022年1月）高度吻合！兩個獨立時間點（2016年11月 vs 2022年1月）的「回推起點」計算結果幾乎一致（均指向1992年秋末），是本研究中最強的時間線交叉驗證證據，建議在最終人物側寫中確立**1992年11月**為其自稱交易生涯起點的主要版本。

### 6. 矛盾與演變（補充）

- **趨勢線態度的早期版本**：本檔案（`o8NfSK-pUlE`，2016年11月）是批次中「趨勢線無效論」最早的教材來源之一，且語氣相對溫和剋制（"it's my perspective...I believe it's basically an opinion"），對比批次三`N4am6Jsp8N8`（2023年）「it's a religion...it's a cult」的激烈措辭，進一步印證先前已記錄的「支撐阻力/趨勢線否定語氣隨時間顯著激化」演變模式，且首次提供了明確的「起點對照」：2016年較溫和學術化的懷疑論，到2023年演變為近乎宗教審判式的全盤否定。
- **"study/watch/observe不是交易建議" vs 大量即時公開精確價位喊單行為**：`nv0ey5UyOmY`與`nz7Y5lrAqgM`中反覆強調自己從不直接下達買賣指令、只給邏輯與觀察方向；但同時他公開發布的社群貼文與Twitter內容包含高度具體的價位（如"4303"目標、"one 1685 area"停利位），與「純觀察無建議」的自我定位存在論述與實際行為之間的持續張力（與批次四已記錄的類似矛盾一致，此處為第三次獨立佐證，顯示這是貫穿其整個教學生涯的固定修辭策略而非單一矛盾事件）。

---

## 總結：跨批次確立的關鍵時間錨點

綜合五個批次的交叉比對，交易生涯起點最一致收斂於 **1992年11月**（`o8NfSK-pUlE` 2016年"24 years"回推 vs `nQfHZ2DEJ8c` 2022年"30 years, November 5th"回推，兩者高度吻合）；"1982"（`lp9cfZrqwjA`同集內部矛盾說法）與"1996年codified"（`N4am6Jsp8N8`, `nI1AMOC1pro`則指向"over the last two decades"研究，回推約1997年）應視為分別指涉「更早的雛形接觸」與「方法論系統化完成」的不同里程碑，而非與1992年矛盾的交易起點聲稱。

*(本文件記錄至此，45個檔案已全數處理完畢——見下方「批次六」補上先前遺漏書面記錄的3個檔案)*

---

## 批次六（補處理：M27EOgtHhis、MdYrslpUezU、MPlNRxHkh_M）

說明：這3個檔案在先前處理過程中已被讀取，但因中途中斷，書面筆記未及寫入文件。現重新讀取並補上正式記錄。

### 1. 心智模型候選（補充）

- **「知道價格最可能去哪」比「進場點位是否完美」更重要**：OTE (optimal trade entry) 只是版本工具，真正核心是draw on liquidity的方向判斷，進場精準度是次要的。出現於：`M27EOgtHhis`（"the entry is not the most important thing knowing where the price is most likely trying to go to is what's most significant"）。
- **「利潤目標是不完美的，滿足即可」**：目標是抓住移動中的「肉」而非精確的最高/最低點，出場位設在預期日內波段的50%或以下即視為個人滿意的模型。出現於：`M27EOgtHhis`。
- **獨創詞彙的持續宣稱與對「盜用者」的提醒**：反覆聲明kill zone、power of 3等詞彙是自己原創，"I create these own my own names...please don't be confused if you see other people using those terms"，並指控他人使用"institutional this institutional that"的buzzword包裝。出現於：`M27EOgtHhis`（與批次一`ley5HZs4bUM`的相同措辭幾乎逐字重複，屬於他反覆使用的固定話術段落）。
- **交易紀錄應以「日誌回測(back-testing/backlog study)」為核心養成方法，而非直接進場**：明確教導以「假想的自己」對話形式，強調前3年應該把重心放在demo回測與建立setup資料庫，而非追求真實損益。出現於：`MPlNRxHkh_M`（整集核心，"if I could go back and tell myself"的虛構自我對話框架）。
- **圖表極簡主義的養成過程**：坦承自己最初也依賴stochastic、MACD等指標，是「後來才」演化到裸K線(open/high/low/close)+前日/前週/前月高低點的純淨圖表。出現於：`MPlNRxHkh_M`（"you like stochastic right now it's not going to ever appear in your chart anymore Michael"）——此為第一人稱明確承認自己方法論的「演化史」而非一開始就如此。

### 2. 決策啟發式（補充）

- 非農週交易節奏：週一週二積極、週三後轉保守（"come off jets as we get closer to Wednesday's New York open"），並明確聲明此為個人偏好非鐵律，避免讀者將其奉為教條。出現於：`M27EOgtHhis`。
- Power of 3做空模型的具體數字：以30 pips波幅計算開盤價上方停損位置（約30-62 pips），在Asian range先行小倉位建倉，目標鎖定倫敦開盤前的sell-side liquidity。出現於：`M27EOgtHhis`。
- **回測(back-testing)的具體量化紀錄項目**：每個setup都要記錄「進場後多少pips回撤(drawdown)」「花多久時間到達目標」「若不設停損原本會怎樣」三項數據，累積成「backlog」，作為建立正確心理預期的資料庫。出現於：`MPlNRxHkh_M`（"how many pips did it take from entry to scaling...how much time did it take...how much drawdown"）。
- **62% Fibonacci回撤為預設保守進場位，70.5%/79%為進階版本**：建議新手優先只用62%關卡，不要一開始就追求70.5或79%的「更完美進場」，避免因等待完美進場而錯過整體趨勢。出現於：`MPlNRxHkh_M`（"just simply used a 62% tracing level and defer the insatiable desire for you to find the perfect entry"）。
- **8:30-11:00（紐約時段）為日內OTE型態的主要觀察窗口**，每天在此區間找5分鐘圖的swing-low OTE進場，目標打前一日高點+標準差延伸位。出現於：`MPlNRxHkh_M`。

### 3. 表達DNA（補充）

- **虛構「與年輕時的自己對話」框架**：整支影片以第二人稱"Michael"稱呼年輕時期的自己進行假想教學對話，是批次中少見、情感濃度較高的敘事手法，帶有懺悔/勸誡語氣（"I don't want you to go through all that"）。出現於：`MPlNRxHkh_M`。
- **自曝年齡與生理狀態作為權威/滄桑感佐證**："at 47 turning 48 soon these problems...are still going to be painful to relive"，將自身年齡與教訓的痛苦程度掛鉤，強化「過來人」形象。出現於：`MPlNRxHkh_M`。
- **重複警告「不要在交易日誌寫負面情緒化字眼」**：明確要求日誌要"positive constructive not negative criticism"、"there's no emotions whatsoever none"，將交易日誌書寫規範上升為紀律訓練的一部分。出現於：`MPlNRxHkh_M`。
- **Twitter帳號自我認證提醒再度出現**："i am the ict"帳號格式提醒＋"a lot of people over there pretending to be me"的防偽聲明，與其他檔案（如批次三`NkwqJBzgQwo`）的類似段落構成反覆出現的固定話術模組。出現於：`M27EOgtHhis`未出现此段但`MdYrslpUezU`重複段落與`mkAuOOPTEKw`一致（因二者為同一內容，見上方資料品質註記）。

### 4. 決策紀錄（補充）

- **GBP/USD（cable）非農週做空demo交易**：於Asian range以1標準手小倉位進場做空，隔夜停損被觸及("got stopped out right there")，事後坦承"I've been hurt many times trying to get the absolute best exit"，屬於誠實展示未達目標／小額停損的案例。出現於：`M27EOgtHhis`。
- **虛構「回到過去」教學情境下引用的具體歷史案例**：以2020年7月10日EUR/USD的62%/70.5% Fibonacci回撤位教學為例，說明"最高點是114.52，目標114.46多一點點"的精準度展示，但明確定位為「回測練習範例」而非即時實盤紀錄。出現於：`MPlNRxHkh_M`。

### 5. 時間線/背景線索（補充）

- **明確自述年齡「47歲即將滿48歲」**：出現於`MPlNRxHkh_M`（該系列影片應為2020年前後製作，因為片中引用"the 10th of July 2020"作為近期案例）。若47/48歲對應2020年，回推出生年約1972-1973年，與批次四`nQfHZ2DEJ8c`（2022年初"getting turned 50"）高度吻合，進一步鞏固「出生年約1972年前後」的交叉驗證。
- **"Trading View今日才存在，但你（年輕時的自己）當年用的是MetaStock、Supercharts、TradeStation"**：暗示其職業生涯早期（推測1990年代）所使用的技術分析平台，為其技術背景提供具體工具時間線佐證。出現於：`MPlNRxHkh_M`。

### 6. 矛盾與演變（補充）

- **圖表工具使用的自我承認演變**：`MPlNRxHkh_M`中第一人稱明確承認自己"當年"（年輕時）曾使用stochastic、MACD等技術指標，之後才"strip all the indicators off"改用純K線+高低點分析。這與其他多數影片中「我從來不用任何指標、只看open/high/low/close」的一貫敘事（如批次一`LifG37ky-Rg`的"I do not have faith in diagonal support resistance"等）形成一個**自我承認的演變軌跡**，而非外部矛盾——這裡是他自己主動說明了「怎麼從用指標演變到不用指標」的過程，補足了先前批次中「他宣稱從不用指標」說法背後的實際養成史。
- **「不要把我的個人偏好當福音」的自我修正**：`M27EOgtHhis`中明確舉例說有讀者誤把他過去「不要在週一交易」的評論當成教條，並在社群上曬單反駁，他因此澄清這只是個人偏好非鐵律。這與其他批次中他強勢、絕對化的教學語氣（如"there's no other way"、"I promise you"）形成語氣上的反差，顯示其論述中同時存在「絕對權威宣稱」與「這只是我個人看法」的雙軌語言策略，視語境交替使用。

---
*(全部45個檔案的書面記錄至此完整齊全)*
