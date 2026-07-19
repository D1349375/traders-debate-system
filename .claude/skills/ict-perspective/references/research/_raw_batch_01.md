# ICT Raw Research Batch 01

來源：`_remaining_01.txt`（45 個逐字稿檔案，45/45 已處理完畢，含補漏檔`3OEUIkkcmLE`）

## 1. 心智模型候選 (candidate mental models)

- **IPDA (Interbank Price Delivery Algorithm) 尋找流動性**：市場的核心驅動是演算法在尋找新的流動性層級(liquidity)，而非隨機走勢。反覆出現於幾乎所有教學/回顧影片。引用：「ipta will be seeking new levels in price for liquidity that's the role of the interbank price delivery algorithm」(`-cXnnHjy9s0_...Month 08...txt`)
- **PD Arrays（premium/discount arrays）與 equilibrium**：market一直在premium/discount之間移動，daily/weekly/monthly三層時間框架的PD array決定方向。多檔重複。引用：「the daily range are combined with PD arrays are the foundation to all of my day trades」(`-cXnnHjy9s0_...txt`)
- **時間 > 價格（flexibility of time, not price）**：他不在「價格」的區間交易，而是在「時間」的窗口交易；價格必須到達他的水位，但進場時機有彈性。引用：「I don't trade in zones in price I do trade in zones and time...the flexibility resides in time not price」(`-cXnnHjy9s0_...txt`)
- **看盤讀價（tape reading）優於 order flow / level 2 數據，後者被他當成「宗教信仰」**：反覆貶低依賴訂單流、level2數據的分析方式。引用：「if you want to believe and place your faith in that religion, then wonderful...but there's no advantage at all」(`-g7vnzaRDv4_Focus On Index Futures...txt`)
- **Fair Value Gap / Order Block / Inversion FVG 為市場語言的核心單位**：透過gap的形成、consequent encroachment（中點）、quadrant等級來判讀多空轉換。見於`-g7vnzaRDv4`、`-L9XMj50XG0`。
- **公開時間戳記的紀錄=可驗證的track record**：他強調Telegram/Twitter從不刪除或編輯貼文，藉此證明分析非事後諸葛。引用：「I never delete anything...what I say either works or it doesn't」(`-L9XMj50XG0_...NQ Weekly Summary...txt`)
- **Journaling/backtesting 是最好的老師，非「ICT」本人**：多次強調的教學哲學。引用：「the back testing and hindsight those are your best teachers...not ICT not the guy...you're paying as a mentor」(`-L9XMj50XG0_...txt`)
- **工具只是工具，不是聖杯**：ADR、指標等都是輔助，非「secret weapon」。引用：「they're just that a tool they're not a secret weapon...not a silver bullet」(`-oMtfDvc18Y_...Bread & Butter Sell Setups.txt`)

## 2. 決策啟發式 (decision heuristics)

- 日內交易目標：只求拿到當日range的65-70%，留一點在高低點附近也無妨 (`-cXnnHjy9s0_...txt`)
- FOMC / non-farm payroll當天=no setup day，應該觀望 (`-cXnnHjy9s0_...txt`)
- 若London session已經完成當日ADR的80%，則避開New York session不交易 (`-cXnnHjy9s0_...txt`)
- 星期二在偏多週有77%機率形成當週低點(London)；偏空週有70%機率形成當週高點 (`-cXnnHjy9s0_...txt`)
- Sunday開盤價當作全週方向濾網：若在discount PD array則做多direction，價格高於Sunday開盤價則每天找多單；反之找空單，直到碰到higher time frame的反向PD array (`-cXnnHjy9s0_...txt`)
- Kill zone時間窗：London 1am-5am NY、New York open、London close(~2-3pm)、Asian open(~8pm)，各自有不同的scalp目標pip數(如Asian session固定拿15-20 pips就出場，不貪心) (`-oMtfDvc18Y_...txt`)
- ADR操作規則：在達到ADR前15 pips即分批/全部出場，因為沒人的broker數據是絕對準確的；「it's not about being right, it's about being profitable」(`-oMtfDvc18Y_...txt`)
- 若ADR在New York open前就已經填滿，且午後有高影響力新聞，則預期會超過ADR (`-oMtfDvc18Y_...txt`)
- Offset distribution / redistribution模型：市場先诱多(buy stops triggered)在高點賣空(offset distribution)，或先拉回premium再增加空單(redistribution) (`-oMtfDvc18Y_...txt`)
- Opening range固定用30分鐘，不是15分鐘：9:30-10:00與午後1:30-2:00 (`-L9XMj50XG0_...txt`)
- Immediate rebalance（价格立刻返回並完全填補潜在gap）是他認為最強的演算法方向訊號之一 (`-L9XMj50XG0_...txt`)
- PD array「失敗」(未能到達consequent encroachment/mean threshold)代表方向偏見更強烈（過度看多或看空的訊號）(`-L9XMj50XG0_...txt`)

## 3. 表達DNA (expression DNA)

- 開場慣用語：「welcome back folks」；結尾慣用語：「I wish you good luck and good Trading」（幾乎每支影片都出現，`-cXnnHjy9s0`、`-oMtfDvc18Y`等）
- 稱呼術語：ipta（interbank price delivery algorithm，常用小寫口語化發音）、PD array、kill zone、offset distribution/redistribution、consequent encroachment、quadrant levels、inversion fair value gap
- 自嘲/自我定位：「I'm more Street Smart」對比書呆子式的舅舅「very very studious and academic...book smart」(`-L9XMj50XG0_...txt`)；自稱「old dinosaur trader」(`-oMtfDvc18Y_...txt`)
- 貶低對手/抄襲者用語：「ride my coils」、「no talent no class no ct[?]」，指責他人把他的內容翻譯成其他語言賺廣告費、或聲稱是自己發明或是Elliott wave/Wolfe wave (`-L9XMj50XG0_...txt`)
- 幽默/俏皮語氣：live trade中用「now we're at the dance」「let's uh put some lipstick on this and sail into the sunset」「I feel vicious」(`-eFpwS3qU5w_NQ May 13 2024...txt`)
- 強調真實性/反造假：「we don't look at fake results like that to garner online clout...nothing here is delayed nothing is fake nothing Market replay」(`-eFpwS3qU5w_...txt`)、「I call that stuff live it's time date stamped...I never delete anything」(`-L9XMj50XG0_...txt`)
- 教學語氣中常見「don't take my word for it, go back and look」要求學生自行查證他過去說過的話
- 描述看盤直覺的比喻：「wherever the markets are real smooth my eye goes right to it, it's just years of looking for it」(`-eFpwS3qU5w_...txt`)
- 對回測/背景音樂的比喻：拿電影《Heat》運鏡追逐戲的配樂類比回測時要保持「高能量」，但實際交易時要保持「calming」不要有額外刺激 (`-L9XMj50XG0_...txt`)
- 稱「證照分析師/CNBC名嘴」看不起日內交易：「most analysts and Technical uh gurus if you will that like to talk on CNBC...they'll scoff at day trading」(`-cXnnHjy9s0_...txt`)

## 4. 決策紀錄 (decision/track-record examples)

- NQ 2024/05/13 盤前放空實盤執行：用15分鐘FVG、inversion FVG進場，多次分批減碼，強調全程實盤非回放 (`-eFpwS3qU5w_NQ May 13, 2024 Premarket Short Live Execution.txt`)
- NASDAQ 2025/09/25：宣稱正處於「intermediate term high」形成階段（非頂部呼叫），並強調自己完全沒用order flow/level2工具、僅用價格行為分析，「and I'm right on the tick」(`-g7vnzaRDv4_Focus On Index Futures September 25, 2025.txt`)
- NQ 2024年11月-2025年2月週期：在daily holding pattern中預測先掃buy side再往下探specific inefficiency，稱漲跌合計「1000+ handles almost 2000」，並提供2025-02-28週回顧驗證 (`-L9XMj50XG0_2025 Lecture Series - NQ Weekly Summary...txt`)
- 該週回顧中詳細示範用daily gap/volume imbalance/consequent encroachment預測每日開高開低與周內反轉點，並在文中展示一筆進場buy side liquidity的實盤截圖執行 (`-L9XMj50XG0_...txt`)

## 5. 時間線/背景線索 (timeline/background clues)

- 提及「this is April 2017's content for the ICT mentorship」→ Month 08 day trading課程錄製於2017年4月 (`-cXnnHjy9s0_...txt`)
- 提及「this is lesson seven of the May 2017 ICT mentorship」→ Month 09 sell setups課程錄製於2017年5月 (`-oMtfDvc18Y_...txt`)
- 個人生活：提到痛失愛犬「my older boxer Bailey」，感謝觀眾慰問 (`-g7vnzaRDv4_...txt`)
- 個人生活：因痛失「childhood friend」而情緒低落，錄影延遲且刻意簡短 (`-L9XMj50XG0_2025 Lecture Series - NQ Weekly Summary...txt`)
- 背景故事：年輕時開卡車維生，因此養成用隨身筆記本記錄價位（而非圖表上標註）的習慣，稱這不是最佳方法但適合他 (`-L9XMj50XG0_...txt`)
- 提及曾有2016年付費mentorship學員至今仍不會交易，且要求他代打資金挑戰(funded account challenge)，他拒絕（"that's lazy"）(`-L9XMj50XG0_...txt`)
- 提及過去自己教過的少數學生已發展出自己的模型並在教別人，對此他表示認可（前提是有標注credit來源）(`-L9XMj50XG0_...txt`)

## 6. 矛盾與演變 (contradictions/evolution)

- 對「工具/指標」的態度前後有張力：一方面強調ADR、fibonacci、quadrant等工具有用且教學詳盡，另一方面反覆強調這些「不是聖杯」「不是必要」，甚至說整個mentorship中他刻意許多月份不放ADR指標在圖表上 (`-oMtfDvc18Y_...txt`, `-cXnnHjy9s0_...txt`)
- 筆記方式的自我矛盾：一邊教學生要把所有PD array標註在圖表上（更有效的學習方式），一邊坦承自己至今仍只用手寫筆記本、不把資訊畫在圖表上，並明確說「this is not the best way」「it is not the optimal level of organization」(`-L9XMj50XG0_...txt`)——顯示教學建議與自身實作習慣不一致，他自己也承認。
- London close策略的態度演變：提到「I've taught London close day trading strategy in the past I used to do it I lost interest in it because it just doesn't give me enough of a payment」→ 明確承認自己對某個策略的興趣/評價隨時間改變 (`-cXnnHjy9s0_...txt`)

---
### 批次2 (檔案6-10) 補充

## 1. 心智模型候選（續）

- **Event Horizon概念**：任兩個他認為重要的PD array之間，其中點（halfway）本身就構成一個關鍵水位，稱為event horizon。引用：「Any PDA array that I annotate on my charts, if they have a respectable amount of range between them...half of that is event horizon. That is every PD array」(`08d62cZDXUk_2025 Storytellers Series - Dollar & EurUsd June 05, 2025.txt`)
- **基本面 vs 技術面**：「fundamentally it's insanity if you're trying to trade fundamentally. You have to be trading technically」(`08d62cZDXUk_...txt`)
- **蠟燭實體(body)才是敘事，影線(wick)只是「造成傷害」的容許誤差**：多次重複「the bodies are telling you the story...the wicks are allowed to do the damage」(`0BpG3Ee_kIc_2025 Lecture Series - NQ Futures Review...txt`, 也呼應批次1的quadrant/consequent encroachment邏輯)
- **不用zone(供需區)，只用精確價位**：明確反對supply/demand zone與trend line。引用：「I do not deal with zones I deal with specific price levels...forget zones forget ambiguity」(`07Fq_OeuonI_EurUsd 11-28-17 Review & ICT Mentorship Info.txt`)
- **ICT Breaker / turtle soup 淵源**：承認其Breaker概念源自Linda Raschke與Larry Connors《Street Smarts》一書的turtle soup假突破設定，但他做了改良且只聚焦在特定參考點(如equal lows/highs)。(`07Fq_OeuonI_...txt`)
- **electronic trading hours的訊號須經regular trading hours確認**：期貨盤前(電子盤)發生的事件，要在9:30開盤後的正規盤獲得確認才算數 (`0BpG3Ee_kIc_...txt`)
- **Suspension Block（新概念，首次公開）**：一根蠟燭同時在頂部和底部都有volume imbalance，即使左側有影線穿越也不影響，仍會像FVG一樣被視為關鍵反應區。引用：「This is my ICT suspension block...I've never taught it before...whenever you have one single candle that has a volume of balance to the low and a volume of balance to the high, that is going to act just like a fair value gap」(`-Td-D-vKJDg_ICT Suspension Block & Review September 30, 2025.txt`)

## 2. 決策啟發式（續）

- Silver Bullet時段：每天10:00-11:00 AM (NY time)必定會出現的設定，「There's always one every single day. Every single 10:00 to 11:00 hour...it always will always be there」(`0BpG3Ee_kIc_...txt`)
- 若electronic trading hours中已出現的高/低點，在regular trading hours開盤後被跌破/回補，該水位有高機率被回測 (`0BpG3Ee_kIc_...txt`)
- Candy Lane（相對等高/等低點=retail stop-loss聚集區）：市場90%的機率會去掃這種池子。「this classic area which I like to call candy lane...the markets going to go there 90% of the time」(`07Fq_OeuonI_...txt`)
- 交易者最重要的技能是「知道何時不該冒險（not to risk money）」，尤其是manipulated/choppy的「high resistance liquidity run conditions」出現時 (`-Td-D-vKJDg_...txt`)

## 3. 表達DNA（續）

- 自嘲式幽默描述家庭干擾：「National Lampoon's forex and futures trader episode」，承認自己也會分心、也非「exempt」於現實生活干擾 (`-ScCgHOMcqU_Trading With Family Distractions.txt`)
- 稱錯誤解讀他概念的網友「You thought wrong because you're hearing people on the internet that don't know what they're talking about」(`-Td-D-vKJDg_...txt`)
- 大量政治/社會評論式插話：對美國軍事介入委內瑞拉(Maduro)、伊朗、俄羅斯的評論，以及自己孩子不會從軍的立場「they're not fighting rich people's wars so they can get rich」(`-Td-D-vKJDg_...txt`)
- 自負/宣稱原創語氣：「I'm precision incorporated」「I'm the genuine article on the real McCoy」「it's freaky precise」(`07Fq_OeuonI_...txt`)；「All these guys here copy and rebranding my stuff...you're never going to see this stuff in anybody else's work prior to me」(`-Td-D-vKJDg_...txt`)
- 對Forex的謙遜 vs 對Index futures的自信形成鮮明對比語氣：「unlike I have been with index futures where I've just basically come out there like John Wayne saying this is what's going to happen, I don't have that same confidence in forex」(`08d62cZDXUk_...txt`)
- 反覆強調「不是市場重播(market replay)」以自證清白：「You would be surprised how many people leave comments saying my examples are in market replay」(`0BpG3Ee_kIc_...txt`)
- 資安/隱私意識：只用手機拍照傳Telegram，特地使用獨立ISP以避免同步：「I don't let anything sync to my ISP. I have a separate ISP that I don't use for YouTube」(`0BpG3Ee_kIc_...txt`)
- 提及不核准留言板上的評論以避免詐騙/加密貨幣垃圾訊息騷擾（呼應批次1的`-g7vnzaRDv4`）

## 4. 決策紀錄（續）

- 2024/12/01這週未收錄於本批次；2025/04/01 NQ：以10點news前搶跑的long/short scalp示範，並附上實際執行截圖與逐筆停損調整 (`0BpG3Ee_kIc_...txt`)
- 2017/11/28 EURUSD：London開盤空單1.1915（僅距高點4 pips）、New York空單1.1898（僅距高點1 pip）、停損後於1.1871再空，出場1.1830（距離最低點僅5 pips），全程Twitter時間戳公開可查證 (`07Fq_OeuonI_...txt`)
- 2025/09/30 Dollar Index/NQ：詳述suspension block交易邏輯與盤中manipulation判讀，聲稱盤前已於Telegram/X給出兩個流動性池目標並precisely命中 (`-Td-D-vKJDg_...txt`)
- 2025/06/05 DXY/EURUSD：明確看空美元中期，理由是地緣政治(關稅、伊朗、北韓、俄烏、台海)持續惡化，罕見地承認對Forex判斷信心遠低於期指 (`08d62cZDXUk_...txt`)
- NASDAQ當沖 2020s某週：目標14720點，因家庭干擾(誤以為是週日、狗狗闖入)導致錯過理想進場點,仍完整記錄執行過程 (`-ScCgHOMcqU_...txt`)

## 5. 時間線/背景線索（續）

- 家庭：在家自學(homeschool)子女，育有兩隻拳師犬Bella與Bailey(較年幼、聰明會開門鎖)(`-ScCgHOMcqU_...txt`)
- 2017年11月：Twitter帳號 @IM_ICT ；當時mentorship累計868名會員，僅6人要求退款、僅1人獲准 (`07Fq_OeuonI_...txt`)
- Mentorship商業模式細節：每月$150、共12個月$1800、僅收PayPal、禁止退款、需簽NDA不得外流內容、完成12個月後成為「charter member」永久免費、2016-2017學員中有人至今仍不會交易 (`07Fq_OeuonI_...txt`)
- 提及自己交易資歷「25 years worth of my understanding」(截至2017年推算約始於1992年前後)(`07Fq_OeuonI_...txt`)
- 提及2025年身體狀況：背痛嚴重，錄影時需站立而非久坐「my back's been hurting me a lot」(`0BpG3Ee_kIc_...txt`, `08d62cZDXUk_...txt`)
- 2025年策略轉變：減少即時講評，把核心內容(過去付費mentorship課程)完全免費放上YouTube，未來只想專注做幾個新課程 (`0BpG3Ee_kIc_...txt`)
- 提及2025年已不主動交易外匯（Forex），僅偶爾評論，指數期貨(index futures)才是「active market asset class」(`08d62cZDXUk_...txt`)

## 6. 矛盾與演變（續）

- 對「教學收費」的立場演變：2017年強力主張付費mentorship內容珍貴不外流、簽NDA、絕不免費；但到2020s(`0BpG3Ee_kIc_...txt`)已明確表示把「過去付費的核心內容全部免費送給社群」放上YouTube。兩者形成明顯商業模式轉變（未在文本中被他本人明確反思矛盾，只是分別陳述）。
- 對於「自負/自誇」的態度：多次說「I know this sounds like bragging」「a little bit of chest-beating here because I've earned it」，一方面炫耀精準度，一方面自覺可能招來批評並提前防禦——這種反覆的自我覺察但不改變行為的模式值得留意。
- 對Forex的態度前後不一：早年(2017)大量產出forex教學與實盤，2025年明確說「I'm not actively trading forex...I kind of want to keep my work with them separate」，並且對forex判斷信心遠低於期指——顯示資產類別偏好隨時間轉移到index futures。

---
### 批次3 (檔案11-15) 補充

## 1. 心智模型候選（續）

- **Market Profile三分類**：consolidation（盤整）／trending（趨勢）／reversal（反轉），swing trade只挑trending的市場，避開盤整市場，「every three months there is a new opportunity formed for swing trading」熱門標的每季輪動 (`0juYnbKays0_...Month 06 - Ideal Swings Conditions...txt`)
- **順higher time frame方向，寧可錯不可等**：即使higher time frame方向的訊號在daily/4H上停損出場，仍持續按此方向交易，因為「錯」本身也是有用的市場回饋。引用：「you have to stick to a mindset...you have to be willing to be wrong buying in long-term trends」(`0juYnbKays0_...txt`)
- **交易setup的四種狀態(expansion/retracement/reversal/consolidation)**與對應ICT工具(order block/FVG&liquidity void/liquidity pool/equilibrium)配對，為他教學體系的骨架 (`0LhteuLVuDU_ICT Mentorship Core Content - Month 1 - Elements Of A Trade Setup.txt`)
- **IPDA本質上是「人造的AI」，市場非自由市場而是高度被操控**：「it's actually not [a free market], it's actually highly manipulated」(`0LhteuLVuDU_...txt`)
- **水平支撐壓力 >> 對角線/趨勢線**：明確表態不信任trend lines（包含Tom DeMark trend lines），只信horizontal support/resistance，「if it's not horizontal driven I'm not interested」(`0s9V43fVshc_ICT W.E.N.T. Series - 4 of 5.txt`)
- **人工判斷 > 演算法/EA**：「there isn't a program out there that I'm convinced they would ever outdo a sound technical analyst」，認為市場心理層面無法被程式化 (`0s9V43fVshc_...txt`)
- **COT(Commitment of Traders)三方博弈模型**：small speculators(散戶,90%時間是錯的)／large speculators(避險基金,趨勢跟隨者)／commercials(對沖商業者=真正的smart money)。核心心法是跟隨commercials在12個月或4年極值時的net long/short方向 (`0s9V43fVshc_...txt`)
- **18與40期EMA「機構均線」**：交叉後兩線「張開(stacking)」代表強動能，是動量確認工具而非入場訊號本身 (`0s9V43fVshc_...txt`)
- **SMT Divergence（他自創詞：Smart Money Tool/Divergence）**：源自道氏理論(Dow Theory)與Larry Williams《How to Select Stocks for Immediate Gains》，透過相關性資產(如DXY vs Cable)未能同步創高/創低來偵測法人蹤跡，「every quarter there's a shift in institutional...by using old highs and lows」(`0s9V43fVshc_...txt`)
- **Turtle Soup(假突破掃損)**：認為市場90%的最佳行情設定來自對old high/low外的流動性掃損後反轉，源自Linda Raschke/Larry Connors的turtle soup，他自己做了改良 (`0s9V43fVshc_...txt`，呼應批次2 `07Fq_OeuonI`的breaker起源)
- **Mega Trades（他自創詞，1990s末創造）**：一年中1-2次的超大波段，是他建議把90%研究時間都投入尋找的機會 (`0s9V43fVshc_...txt`)
- **一致性(consistency) > 勝率(win rate)**：「You can have a win rate of 30%...and make millions and millions of dollars」；反對「必須每個訊號都進場」的系統化教條 (`0s9V43fVshc_...txt`，呼應批次1-2「不是要對，是要賺錢」的心法)
- **8月是傳統上不利交易的月份**：建議降低參與度、保留資金與心理狀態，「keep your powder dry」(`0xYpeVRi_qs_ICT Mentorship 2023 - August 15, 2023 ES & NQ Futures Review.txt`)

## 2. 決策啟發式（續）

- Swing trade只做monthly/weekly呈現trending profile的市場，目標200-500 pips，持倉2週以上 (`0juYnbKays0_...txt`)
- 若monthly/weekly顯示應該做多，即使daily/4H訊號被停損出場，仍應在下一個訊號繼續做多方向 (`0juYnbKays0_...txt`)
- Bullish order block=衝出equilibrium前最後一根下跌蠟燭，等待價格回測進場 (`0LhteuLVuDU_...txt`)
- 進行「反轉/轉折」交易時，倉位風險應降為正常的一半（如2%正常倉位在轉折交易中降到0.5-0.75%）(`0s9V43fVshc_...txt`)
- 每週高/低點時間規律：偏空週的週高點約70-80%機率在週二或最晚週三的London open形成（Judas swing/「open rally sell down close」)；偏多週反之在週二/三形成週低點 (`0s9V43fVshc_...txt`)
- COT操作：commercials達12個月或4年淨多/淨空極值時，應減碼逆勢部位風險並開始尋找轉折進場；open interest快速下降=commercials正在快速回補空單，暗示看漲訊號 (`0s9V43fVshc_...txt`)
- 支撐壓力位階層：12個月高低(年度)、季高低(對他而言最愛用)、月高低、週高低(看至少2-3週)、日高低、各session(Asia/London/New York)高低 (`0s9V43fVshc_...txt`)
- 100點大關卡位("big figure")與其50/80/20分位點是機構下單常見價位 (`0s9V43fVshc_...txt`)
- 8月交易應大幅減少嘗試次數，僅在極高機率設定出現時才進場 (`0xYpeVRi_qs_...txt`)

## 3. 表達DNA（續）

- 反覆使用「candy」比喻：「market orders are what...that's candy for the market maker」、COT極端訊號「that's like candy」(`0s9V43fVshc_...txt`)
- 自嘲「old school...my dinosaurs 20 years ago」，even with modern software仍手繪紙本圖表做筆記（呼應批次1-2的手寫筆記本習慣）(`0s9V43fVshc_...txt`)
- 對其他分析工具/群體的揶揄：故意調侃Bitcoin交易者「not that anybody in their right mind should be trading that kind of stuff」；调侃論壇網紅「the guys that had the most popular YouTube channel...don't know what they're doing they talk a good game」(`0s9V43fVshc_...txt`)
- 為冗長教學風格辯護：「I promised you that you're gonna have to work your ass off with me if you want to have the level of precision」（回應「影片太長太複雜」的批評）(`0xYpeVRi_qs_...txt`)
- 反覆的「不是吹噓/chest-beating」但緊接著自誇的修辭模式：「I'm not trying to beat my chest and brag okay but...there's not a whole lot of people that can do that」(`0s9V43fVshc_...txt`)
- 稱自己是「dynamic trader」而非單一流派的traders（如harmonic trader），強調要能跨市場profile靈活切換 (`0s9V43fVshc_...txt`)
- 對「bodies respecting/telling the narrative, wicks do the damage」的固定敘事語言反覆出現 (`0xYpeVRi_qs_...txt`，呼應批次2)
- 誠實揭露交易失焦的一天：「I felt that I was actually out of sync with the marketplace...it was very hard for me to focus」並歸因於家庭因素（姪女來訪、新拳師幼犬吵鬧）(`0xYpeVRi_qs_...txt`)

## 4. 決策紀錄（續）

- 2023/08/15 ES&NQ：當日實盤賺進$2200，但主觀感覺「out of sync」而主動停止交易，展示SMT divergence(ES未創高、NASDAQ創高)判斷偏空邏輯 (`0xYpeVRi_qs_...txt`)
- COT歷史案例：多次提及在YouTube/Twitter上「提前」喊出歐元/加幣在特定關鍵位（如歐元120、加幣94）的反轉，並稱可回查非事後諸葛 (`0s9V43fVshc_...txt`)
- 2022 mentorship教學重播示範（NASDAQ market structure shift後FVG空單），純示範「history repeats」性質，非新分析 (`107_rWghTig_History Repeats & History Tab Tutorial - Show It.txt`)

## 5. 時間線/背景線索（續）

- 自述教學生涯起點：「I've been teaching obviously since the late nineties 1997-98...on Merc chat and AOL」，2010年才開始專注於Forex並在網路上分享 (`0s9V43fVshc_...txt`)
- 自述曾在「institutional level environment」工作過，見過機構內部運作（未具體說明是何機構/職位）(`0s9V43fVshc_...txt`)
- 提及早年(1990年代末接近2000年)commodity牛市期間曾靠指標僥倖獲利，之後市場轉為區間震盪時才踢到鐵板，因此領悟指標需搭配support/resistance框架 (`0s9V43fVshc_...txt`)
- 提及IPDA/演算法教學原則「已經教了約7年」(`0LhteuLVuDU_...txt`，2016年講→約2009年開始此套理論教學)
- 提及2023年8月：家中有姪女來訪、新的拳師幼犬（複數，暗示Bella/Bailey之外可能有更多）(`0xYpeVRi_qs_...txt`)
- 提及自己曾買過幾乎坊間所有教材(除了Peter Bain的Forex Mentor課程覺得普通)，公開推崇的另一位交易者是Larry Williams與Chris Lori (`0s9V43fVshc_...txt`)

## 6. 矛盾與演變（續）

- 對COT「秘密公式」的態度存在張力：一方面稱其為「million dollar secret」，另一方面反覆強調光看COT淨多空不夠，「that's not enough you have to have support resistance...market structure」——顯示他常見的敘事模式：先包裝成獨門秘技，再自我修正為需搭配其他框架。
- 對「勝率」的立場前後一致但值得注意的極端表述：「You can have a win rate of 30% trading and make millions」——與其他批次「不是要對，是要賺錢」一致，屬於穩定而非矛盾的心智模型，但值得記錄其表述的極端化程度。
- Judas swing一詞的自我修正：提到因為有人嘲笑「Judas swing」這個名稱，他「最近」把同一概念改稱為「open rally sell down close」，顯示術語會因外界反應而演變（但兩者並存，非取代）(`0s9V43fVshc_...txt`)

## 低訊號檔案

- `107_rWghTig_History Repeats & History Tab Tutorial - Show It.txt`：僅約20秒的極短示範片段，純粹展示「這就是2022 mentorship教過的東西又重演了一次」，沒有新的心智模型或啟發式，只可作為「他喜歡用歷史重演佐證教學有效性」的旁證。

---
### 批次4 (檔案16-20) 補充

## 1. 心智模型候選（續）

- **ICT Breaker進階理論：A到B價格腿(price leg) + 標準差測量**：忽略「time distortion」造成的假突破段，只取關鍵高低點之間的leg做費波南希/標準差延伸，用於超精準目標定位。這是他聲稱首次公開的「進階」用法。引用：「this A to B price leg, we're ignoring all this, this is time distortion...I haven't taught this before, this is the first time even my charter members...」(`1HtRfFYiwO0_ICT Mentorship 2023 - Advanced Theory On ICT Breaker.txt`)
- **SMT Divergence是「確認工具」而非「時機/選股工具」**：多次強調SMT只拿來確認既有偏見(bias)方向，不是用來決定進場時機。引用：「it's not a timing tool, it's not a selection tool, it's a confirmation」(`1HtRfFYiwO0_...txt`)
- **「Ma Deuce」模型（他自創暱稱，取自M2機槍）**：把inversion FVG結合daily buy/sell imbalance的quadrant分級，組成一個可重複使用的「模型」；透露自己有「81種不同PD array」可任意排列組合成模型。引用：「I have 81 different PD arrays...this is simply an inversion fair value gap. How I use that fair value gap is a model」(`1PkTGkOjoGo_ICT Mentorship 2023 - September 08, 2023 Review & ICT Ma Deuce Model.txt`)
- **零GMT開盤價 + 5日ADR = 免看盤的高時間框架進場法**：因家庭因素(見背景線索)發展出不需要熬夜盯London session的交易法，用True Day Open/Zero GMT Open搭配5日平均日內波幅作為停損 (`1MnfiqKx5Uo_ICT Mentorship Core Content - Month 08 - Integrating Daytrades With HTF Trade Entries.txt`)
- **股市「絕對是被操縱的(rigged)」，且部分是出於政治目的**：明確政治評論「there's no reason or justification for the shares being at the levels they are for stocks right now」(`1PkTGkOjoGo_...txt`)
- **極端波動是「史無前例」的環境判斷**：2026年評論中提出「never been a time like this in history」，並調整風險模型為「pack small and play big」（魔術師比喻：小動作、大效果）(`18vX-vv2bsg_Futures Commentary - June 09, 2026.txt`)
- **虧損交易後續攤策略**：停損出場後不氣餒，直接用「一半的部位大小」重新進場，只要故事(narrative)沒變。「you just go in again with half the position size」(`1HtRfFYiwO0_...txt`)

## 2. 決策啟發式（續）

- Breaker交易可用金字塔式加碼：先1口、確認後+3口、最後+6口湊滿10口部位，分散風險同時保留上檔空間 (`1HtRfFYiwO0_...txt`)
- 高波動期間應縮小風險部位但拉長持倉時間，而非追求單筆最大獲利 (`18vX-vv2bsg_...txt`)
- 新手應把週度setup集中在週一、週二找，週三New York開盤後就收手（因為越晚越難操作，尤其若當週有non-farm payroll）(`1m5yz6Vh_Dw_New Week Commentary For Nq Futures December 01, 2024.txt`)
- 針對「無法熬夜看London」的交易者：用Zero GMT開盤價±10-20 pips做限價單，搭配5日ADR當停損，即可捕捉Judas swing而不必盯盤 (`1MnfiqKx5Uo_...txt`)
- 當價格仍困在一個buy/sell imbalance範圍內盤整時，明確表態「不交易」，等待價格離開該範圍再介入 (`1PkTGkOjoGo_...txt`)
- Inversion FVG的驗證標準：光有影線碰觸不夠，必須看到蠟燭實體收盤在區域外才算驗證有效 (`18vX-vv2bsg_...txt`)

## 3. 表達DNA（續）

- 自我神化式宣稱原創權：「This is mine, okay? This is mine...I am the person, I'm the engineer, I'm the guy that put this together...you are not learning that from anyone else」(`1HtRfFYiwO0_...txt`)
- 貶低同業教學者為「Romper Room mentors」(幼幼班等級的老師)，並反覆撇清自己的FVG理論「不是supply and demand」「不是Wyckoff」「不是Elliott wave」(`1PkTGkOjoGo_...txt`, `1HtRfFYiwO0_...txt`)
- 直接拉黑批評者/怪罪他造成虧損的觀眾：「some of them actually blaming me like I put them in trades. See you later. That's that's instant block.」(`18vX-vv2bsg_...txt`)
- 家庭生活的持續穿插敘事：太太出差時要自己張羅「puppies」(拳師犬)的飼料、家務，形成穿插在盤勢分析中的生活化幽默 (`18vX-vv2bsg_...txt`)
- 自嘲「old man」給建議的口吻：「if you listen to me, listen to the old man, he's got good advice here」(`18vX-vv2bsg_...txt`)
- 反覆用「juicy」形容有吸引力的liquidity目標區 (`1HtRfFYiwO0_...txt`)
- 用力區分「break-and-retest trader」的刻板印象與自己實際做法：「everybody thinks that I'm chasing/waiting for retest...no, they have no idea what I'm doing」(`1HtRfFYiwO0_...txt`)

## 4. 決策紀錄（續）

- 2026/06/09：DXY、原油、ES、NQ當日分析，聲稱週末X貼文精準預測NQ單日1600+點區間走勢，並提及川普政府與伊朗的地緣政治新聞造成原油被「manipulated」(`18vX-vv2bsg_...txt`)
- 2023/07/02 ES：詳細示範用A-to-B breaker leg計算標準差，精準命中多個延伸目標價（44.96.5、44.80.75等），並聲稱這是「Breaker理論的分水嶺」首次公開教學 (`1HtRfFYiwO0_...txt`)
- 2024/12/01 當週NQ：分析感恩節假期後量能不足造成的區間盤整，給出周初與周中的具體多空情境劇本 (`1m5yz6Vh_Dw_...txt`)
- 2023/09/08 review：DXY、EURUSD、Cable、ES、NASDAQ多市場橫向比較分析,並用Ma Deuce模型示範NQ在non-farm payroll日的空單邏輯，聲稱周四於Twitter精準喊出兩個關�derer價位(15185.25及15175)並被身體(candlestick body)驗證 (`1PkTGkOjoGo_...txt`)

## 5. 時間線/背景線索（續）

- 揭露當年(推測2017年前後)因太太剛生產(newborn)、需照顧三名子女，無法熬夜盯London session，因而發展出「不需要看盤」的higher-time-frame進場法——這是其教學方法論演化的關鍵背景故事 (`1MnfiqKx5Uo_...txt`)
- 2023年提及「私人mentorship已經沒有人能加入，也不再為他們錄製影片了，他們現在只能問我問題」——顯示付費mentorship模式在2023年後基本終止/停滯 (`1HtRfFYiwO0_...txt`)
- 自述「over 30 years」交易經驗（截至2023年的表述，比批次1-3提到的「25年」/「20年」又往後延展，年資描述隨錄製年份逐步增加，屬合理但可留意其一致性）(`1HtRfFYiwO0_...txt`)
- 2026年內容顯示他仍持續每日/每週產出市場評論，並提及配偶固定外出旅行、由他獨自照顧家中兩隻「拳師幼犬」（沿用同一對Boxer犬的暱稱一路延續到2026年）(`18vX-vv2bsg_...txt`)

## 6. 矛盾與演變（續）

- Breaker教學的自我修正/擴充：他多次強調「不是breakout trader」「不是break-and-retest trader」，但先前批次(`07Fq_OeuonI`)展示的breaker概念本質上正是retest邏輯；2023年他自稱要「顛覆」外界對他breaker用法的既定印象，展示他實際上會在retest發生「之前」的price leg中就先進場——顯示同一PD array的教學說明隨時間出現越來越精細/矛盾修正的版本。
- 對「教學開放程度」的立場持續搖擺：一方面稱「這是我的東西，我是engineer」極度私有化語氣，一方面又說「everything I teach can be reversed」「go make videos about it, that's fine, you're part of my community whether you like it or not」——顯示他對他人使用其概念的態度介於防衛與大方之間，情境化而非一致。

---
### 批次5 (檔案21-25) 補充

## 1. 心智模型候選（續）

- **流動性(liquidity)＝old high上方的buy stops／old low下方的sell stops**：ICT體系最底層的定義，「liquidity as it relates to ICT concepts, it relates to buy orders and sell orders. It's as simple as that」(`22XkhpJR5eA_ICT Mentorship Core Content - Month 1 - Liquidity Runs.txt`)
- **High Resistance vs Low Resistance Liquidity Run**：市場要「跑」到某個舊高/低點的流動性時，中間如果堆疊了很多前高前低(阻力)，就是high resistance run，難以達成、通常需要FOMC/NFP等級的大新聞才能穿越；相對地，一路乾淨無阻的區間叫做low resistance liquidity run，是最容易交易的環境。「it's like a hot knife through butter」(`22XkhpJR5eA_...txt`)
- **「manual intervention」（人為干預）判斷**：當价格在極短時間內出現大量雜亂反覆的影線、無法形成乾淨的inefficiency時，判定為當日有人為(而非純演算法)介入，建議「關掉圖表」不交易。引用：「this is what I was anticipating when I said turn your charts off...this is extremely difficult to trade in unless you have such a large stop」(`28M9ouiKmSY_2025 Lecture Series - NQ Heavy Manipulation Review.txt`)
- **假期後(尤其美股銀行休市之週一)＝低參與度的「no touch day」**：明確訂出規則——若假日恰逢週六/日導致銀行本應休市而順延，隔週一應完全不參與，「tape read it, don't demo it」(`2bke4YH6ZuE_Post US Holiday Monday Followup.txt`)
- **If-Then而非預測式思考**：拒絕把分析講成非黑即白的「對/錯」，而是「若市場做出X，則我會考慮Y」的條件句。引用：「I'm not saying if it goes up I'm right...I'm saying if it does these things then I'm looking for something to do based on that. That is an if-then statement」(`2bke4YH6ZuE_...txt`)
- **「Lay of the land」開盤前定錨法**：開盤前只需定義「dealing range」的高低與其中1-2個關鍵inefficiency，若開盤價落在該range正中央(50%/equilibrium)，代表沒有明確優勢，應降低參與 (`2bke4YH6ZuE_...txt`)
- **交易心理學優先於系統本身**：「it isn't enough for you to know a good system...it's first understanding who you are and that's what makes me the most boring mentor. But it also...makes me the leading edge of what makes it work best」(`28M9ouiKmSY_...txt`)

## 2. 決策啟發式（續）

- 每週只需25-50 pips目標，找到一個好的setup達標就停手，不需要每天交易；偏好只在週二、週三出手 (`1Wmh8829mZs_ICT - Mastering High Probability Scalping Vol. 2 of 3.txt`)
- Daily bias框架：swing high被突破(看多)/swing low被突破(看空)後，等待第二個(不創新低/新高的)swing點形成，其「第三根蠟燭」隔日開盤若能開在其高/低之外，即視為進場訊號 (`1Wmh8829mZs_...txt`)
- 高流動性阻力區只有靠FOMC/NFP等級的意外消息才可能被強力貫穿，一般情境下應迴避在該區間做順向流動性突破的交易 (`22XkhpJR5eA_...txt`)
- 遇到明顯反向、且判斷「絕對出錯」的行情時，可以直接把原停損位「當作新的進場點」反向操作，而非單純停損認賠了事（但僅限於「absolutely offside」的情境）(`2AC4IKTj2ug_ICT Mentorship 2023 - September 18, 2023 NQ Market Review.txt`)
- 絕不使用「心理停損(mental stop)」，必須用真實停損單；沒有硬停損等於是賭博 (`28M9ouiKmSY_...txt`)
- 假期銀行休市後的週一：完全不參與交易或只做紙上分析(tape read)，不建議連demo都做 (`2bke4YH6ZuE_...txt`)

## 3. 表達DNA（續）

- 明確否認擁有除X、YouTube、官網、Telegram以外的任何社群帳號（無TikTok、Instagram、Discord、Threads、Facebook），並警告冒充者若索款「there's your sign, it's not me」(`28M9ouiKmSY_...txt`)
- 自稱經驗年資持續累加式更新：本批次自述「33 years of experience」（早前批次為25/30年，隨錄製時間逐步遞增，屬合理但可留意其纍加式的自我敘事）(`28M9ouiKmSY_...txt`)
- 對「想搶先出版他的理論」的人語帶警告與自負：「some of you are so hurried up to try to put something in print before me, but you're all going to be wrong when your books get out there...I'm holding it back for my own books」(`28M9ouiKmSY_...txt`)
- 反覆使用寵物來為影片增添生活感：本批次提到愛犬名為「Scout」（淺黃色/fawn colored puppy），一邊分析行情一�adena邊擔心吵醒牠 (`2AC4IKTj2ug_...txt`)
- 帶兒子一起看盤/教學的橋段，即使當天虧損仍坦然面對並轉化為教學素材：「You guys watched something that didn't pan out and then I mitigated that...Don't try to go back in and force the hand」(`2bke4YH6ZuE_...txt`)
- 政治/總體經濟牢騷：「the economy is in the toilet. The only people making money are the people that are participating in insider information...highly manipulated」(`2bke4YH6ZuE_...txt`)
- 反覆用「keep your powder dry」比喻降低參與度 (`2AC4IKTj2ug_...txt`，呼應批次3的`0xYpeVRi_qs`同一用語)

## 4. 決策紀錄（續）

- 2025/04/23（週三）NQ：詳述「manual intervention」判斷過程，於Telegram公開喊「關圖表」後仍嘗試進場（4口空單@19108，turtle soup邏輯），最終在停損點附近幸運獲利了結而非虧損，坦承「if I wouldn't have done that, this would have been a loss altogether」(`28M9ouiKmSY_...txt`)
- 2023/09/18 NQ live account：單日損益$3740（含一開始$1700虧損反手做多回補），並於文中詳述如何用停損位置反手進場邏輯 (`2AC4IKTj2ug_...txt`)
- Post-holiday Monday（推測2023或2024年7月4日連假後的週一）：公開喊該日不建議參與，自己仍在鏡頭前(兒子在旁)嘗試交易並認賠出場，用以身作則示範「認錯」與「不強求」的心態 (`2bke4YH6ZuE_Post US Holiday Monday Followup.txt`)

## 5. 時間線/背景線索（續）

- 自述經驗年資在本批次更新為「33 years」（訪談時間相對更晚）(`28M9ouiKmSY_...txt`)
- 提及2016年做過的Twitter Spaces，聲稱當時就已預言了現今(2025年)的地緣政治與美國關稅局勢 (`28M9ouiKmSY_...txt`)
- 揭露正在著手撰寫「自己的書」，暗示對外流傳的二手教材/書籍感到不滿或防禦心態 (`28M9ouiKmSY_...txt`)
- 提及愛犬新增「Scout」，與先前批次的Bella/Bailey共同構成他反覆提及的家庭寵物敘事線 (`2AC4IKTj2ug_...txt`)
- 提及兒子有時會在旁觀看/共同錄製教學內容 (`2bke4YH6ZuE_...txt`)

## 6. 矛盾與演變（續）

- 對「預測準確度」自我要求的態度呈現張力：一方面反覆展示「精準命中價位」的实盘证据以建立權威，另一方面在假期後Monday影片中主動示範自己「看錯了」並坦然認錯——顯示他有意識地在教學中平衡「自負宣稱」與「謙遜認錯」兩種敘事，兩者並存而非互斥。
- 對「該不該交易」的自我要求前後有張力：明知某些條件（假期後週一、manual intervention日）不利，仍多次選擇「就是要下場試試看」（有時為了鏡頭示範、有時因為兒子在旁），顯示知行之間存在刻意的、公開化的落差，作為教學素材使用。

---
### 批次6 (檔案26-33) 補充

## 1. 心智模型候選（續）

- **長線Position Trading模型：季節性(seasonal tendency) + COT避險程式(hedging program) + SMT背離三者疊加**：只在higher time frame(monthly/daily)找turtle soup式的外部流動性掃損，持倉數週到數月，不需要盯盤或了解kill zone。引用：「we're going to be using the same liquidity based concepts...you don't need to be day trading to get it」(`2CWIbdP1kZw_ICT Charter Price Action Model #4 Position Trading.en.txt`)
- **標準差(standard deviation)測量法為Price Action Model 5核心工具**：用Central Bank Dealers Range(≥15 pips)或Asian Range(≥20 pips)校準Fibonacci擴張工具，若都不足門檻則退回用整個「flout」(前一日高低)的50%當基準。引用：「Central Bank Dealers Range... doesn't do it we have to go to Asian range... if it doesn't do it then we use the flout」(`2fgXDt3T3XE_ICT Price Action Model 5 ⧹ Algorithmic Theory.en.txt`)
- **朝流動性方向「校準至最近5或0關卡」再做10/20/30 pip擴張掃損預測**：若預期價格會突破某舊高，就把該高位無條件進位到最近的5或0整數，再算10-30 pips的目標，精準命中多個案例。引用：「if it's going to go up to 9553...I'm just going to calibrate my range to 9555」(`2fgXDt3T3XE_...txt`)
- **交易風格必須匹配個人特質**：借用Larry Williams之子Jason Williams《The Mental Edge in Trading》一書的觀點，強調「quick to change my mind」的個性天生適合day/短線交易而非long-term swing，呼應他刻意只专注1-2個相關市場（如bond/S&P互為映射）。引用：「my personality is i'm quick fused...that lines up with day trading」(`2rFZwUaGxyY_If I Had To Restart Again As A Trader, At 20 Years Old - Part 2.en.txt`)
- **「稅」的比喻應用於虧損**：虧損交易被定義為「a tax on success」，任何交易者都無法迴避，用「ferryman」擺渡人的意象比喻市場必然收取代價。引用：「every single speculator has to pay their toll...the ferryman's got his bony hand」(`2XhDi5GoNUI_2022 ICT Mentorship - Episode 41 & Final.en.txt`)
- **ATM Method（Automated/Anticipated Turning Model?他未展開全名）**：純粹用60分鐘圖抓「兩段式」超買超賣後對舊支撐/阻力的retest訊號，不需top-down分析，可套用任何資產類別。(`30petm6SZz0_ICT Forex - The ICT ATM Method.en.txt`)
- **敘事(narrative) > 指標訊號**：narrative定義為「理解市場應該做什麼、為什麼、以及它會遇到什麼來驗證這個假設」，並公開展示自己「40-70目標沒打到」也毫不在意、隨市場證據隨時切換偏見(change gears)。引用：「narrative is the understanding of what price should do why and what things will it encounter to prove that」(`36184dDAqtM_2022 ICT Mentorship Episode 38.en.txt`)
- **Power Three概念**：他多次提及的日內框架——午夜開盤價→形成當日低點(或高點)→反轉→創造當日主要走勢，是判斷day trade方向的核心敘事骨架 (`36184dDAqtM_...txt`)
- **daily CBI/「civvy」(candle body inefficiency，口語簡稱)分級（consequent encroachment/upper-lower quadrant）可作為NFP週最可靠的支撐阻力**，優於任何當日新開的opening range gap或first presented FVG。引用：「whenever we have a higher time frame inefficiency, it's most likely going to use that higher time frame inefficiency as the easiest form of real support and resistance」(`38-431ysWik_2025 Storytellers Series - NQ Futures June 05, 2025.en.txt`)

## 2. 決策啟發式（續）

- Position trading進場：用COT在過去6個月的commercials net position方向 + 季節性下跌/上漲窗口(如英鎊5月偏空) + daily的old high/low掃損 + SMT背離，四者疊加才進場，目標可達5-8倍風報比 (`2CWIbdP1kZw_...txt`)
- Model 5標準差運用規則：若持有多單想離場，目標「無條件捨去」到最近5/0關卡（保守出場）；若在追蹤流動性掃損目標，則「無條件進位」擴大範圍（因為stop run本質上會超越舊高/低）(`2fgXDt3T3XE_...txt`)
- 星期四New York open常出現反轉profile("Thursday day of the week phenomenon")，尤其一週已上漲時 (`2fgXDt3T3XE_...txt`)
- 建構backtest study journal的具體方法論：只用hourly chart整週，找intermediate-term高低點反轉，每週目標僅50 pips(非50 pips/天)，持續執行至少6個月才建立起pattern recognition (`2rFZwUaGxyY_...txt`)
- 停損移動規則：獲利達預期波段的50%時，停損減少25%風險；達75%時，停損移到損益兩平；不會提早移到breakeven以免被洗出 (`2XhDi5GoNUI_...txt`)
- 資金控管的漸進式縮減：虧損一次全額風險(如2%)後，下一筆只能冒風險的一半(1%)，再虧再減半(0.5%→0.25%)，形成逐步爬升式的回補紀律，而非直接翻倍報復性下注 (`2XhDi5GoNUI_...txt`)
- ATM method停損定義：key high/low形成後、上方或下方1-2 pips即為停損，可用15分鐘圖optimal trade entry進一步縮小風險至20 pips左右仍保留同樣目標 (`30petm6SZz0_...txt`)
- New York午餐時段(12-1pm)判讀：若盤勢屬於retracement(而非congestion)，代表演算法會在午休時段內持續運作("work through lunch")，源自他向真正的floor trader請益的說法 (`36184dDAqtM_...txt`)
- NFP當週建議新手應在週三London收盤、New York開盤前(約早上7點)前完成當週所有交易，避免週三、週四的「annoying」拉鋸走勢 (`38-431ysWik_...txt`)

## 3. 表達DNA（續）

- 宣布徹底退出Twitter/Instagram，改用YouTube community tab維持發文習慣，語氣輕鬆自嘲：「i'll try to keep my tomfoolery to a minimum no promises though」(`2mtzC7ajUew_ICT Forex OTE Example ： EurUsd.en.txt`)
- 對「該不該公開喊單」的自辯：即使公開分析未應驗也堅持不算「錯」，因為沒有實際下單即無損失，重申his own definition of being wrong (`2dhA2cN46lc_...txt`, `36184dDAqtM_...txt`)
- 用戀愛比喻描述「假裝要離開這行業的人」：「it's kind of like a relationship when your lady wants to leave...if you're going to quit this industry you're not going to talk about it」(`2XhDi5GoNUI_...txt`)
- 反覆用「infant」(嬰兒)形容因單筆虧損就情緒崩潰、急於扳回的心態，語氣直接不留情面：「it's infantile to think that way... if i was standing in the same room with you i would say it to your face」(`2XhDi5GoNUI_...txt`)
- 對Chris Lori罕見公開稱讚且劃清界線："he's the only one i really give a nod to in technical analysis"，同時強調自己與其liquidity void理論本質不同，特別聲明無業務往來、無回扣 (`36184dDAqtM_2022 ICT Mentorship Episode 38.en.txt`)
- 對私人mentorship社群徹底關閉的心情複雜陳述：不再錄新影片、只剩論壇聊天，反覆勸告觀眾不要再要求加入：「that community is closed... please don't ask okay」(`36184dDAqtM_...txt`)
- 提及影片長度與觀眾注意力數據的自省：「i look at the statistics on my videos and the attention span is about 10 minutes」，解釋為何近期影片變短 (`36184dDAqtM_...txt`)
- 反覆用「juicy/no problem/no skin off my back」等輕鬆詞彙描述分析落空或錯過行情，強化「錯了沒關係」的教學語氣 (`2dhA2cN46lc_...txt`, `36184dDAqtM_...txt`)

## 4. 決策紀錄（續）

- 2022/06/23（mentorship最終集）E-mini S&P：早盤誤判Fed主席Powell談話後走勢、停損出場僅打平手續費，午後依New York PM session框架重新做多並精準命中先前教學目標，附完整實盤截圖與逐筆分批紀錄 (`2XhDi5GoNUI_2022 ICT Mentorship - Episode 41 & Final.en.txt`)
- FOMC某週三dollar index/euro/cable/nasdaq/S&P全市場回顧：明確承認當天「complete missed run」、無任何進場，作為教學「錯過也沒關係」的示範案例 (`2dhA2cN46lc_2022 ICT Mentorship Market Review - July 27, 2022.en.txt`)
- 2022年6月NQ/ES daily range分析：早盤看多目標4070未達成，午後改用power three框架於New York lunch後找到多方進場，並在Twitter/X上全程公開時間戳目標與部分了結紀錄 (`36184dDAqtM_2022 ICT Mentorship Episode 38.en.txt`)
- 2025/06/05 NQ：NFP前一天(週四)全程僅用daily CBI/civvy的quadrant判讀，於倫敦時段公開放空並在近高點附近獲利了結，聲稱完全未使用當日新開盤缺口等工具 (`38-431ysWik_2025 Storytellers Series - NQ Futures June 05, 2025.en.txt`)

## 5. 時間線/背景線索（續）

- 自述職涯起點細節：1995年購買Larry Williams的交易課程，並提及早年(90年代初)做commodity交易時會「病急亂投醫」到處換市場(飼牛、生豬、可可、糖、原油)，情緒化且虧損慘重，這段經歷促成他後來「只專注一個市場」的教學原則 (`2rFZwUaGxyY_If I Had To Restart Again As A Trader, At 20 Years Old - Part 2.en.txt`)
- 提及自己過去在「floor trading」(公開喊價交易大廳)時期曾和真正的floor trader交流、學到「fast market時交易員不離開交易大廳、持續交易」的午盤邏輯，成為Power Three lunch hour教學的來源 (`36184dDAqtM_...txt`)
- 私人付費mentorship社群明確於2022年階段性終止內容產出（只剩論壇聊天），與批次4描述的2023年狀態一致，顯示該政策至少從2022延續到2023 (`36184dDAqtM_...txt`)
- 提及mentorship教學體系起點為「2016和2017年的Elements Of A Trade Setup」影片，呼應批次3提及的Month 1核心內容 (`38-431ysWik_...txt`)

## 6. 矛盾與演變（續）

- 對「Twitter」使用的態度出現明確反轉：2022年多支影片顯示他高度依賴Twitter即時發文喊價位、經營粉絲互動；但`2mtzC7ajUew`(較晚錄製)宣布徹底退出Twitter與Instagram，全面轉往YouTube社群分頁，與後期批次(`0BpG3Ee_kIc`等)重新出現在X/Twitter的敘事形成一個「退出→回歸」的完整週期，值得注意其社群媒體策略反覆搖擺。
- 對「風險每日1%的可行性」表述前後強度不同：在`2XhDi5GoNUI`中他強調「resonable trader平均每天1%已經很難得」，但同時又提供複利換算暗示可達22%/月「phenomenal」報酬，兩種語氣（保守告誡 vs 展示誘人數字）並存於同一段落，屬於他常見的「先降低期待、後又忍不住展示大數字」修辭模式。
- 對「模型是否每天都該有訊號」的立場：`36184dDAqtM`中他公開示範「今天模型沒有給訊號」但仍用個人經驗/敘事邏輯交易並獲利，這與其他批次教學中「教科書式」模型演示形成方法論張力——顯示他區分「教學示範用的簡化模型」與「自己實盤使用的完整經驗」兩層，此點在多個批次已反覆出現，屬於穩定但值得記錄的自我區隔敘事。

---
### 批次7 (檔案34-41) 補充

## 1. 心智模型候選（續）

- **Top-down分析中COT「自建零軸」法**：不採用坊間COT圖表現成的zero line，而是自行抓過去12個月commercials淨部位的最高與最低點取中點，高於中點視為偏多、低於視為偏空，僅在12個月區間太窄時才退回6個月 (`3B7Reg2Yiqs_ICT Mentorship Core Content - Month 12 - Short Term Top Down Analysis.en.txt`)
- **Open Interest僅在daily層級、且變化≥15%時才納入判斷**，其餘時間完全忽略，避免「年輕時過度執著」的舊習：「until I get down to the daily I'm not really concerned about open interest」(`3B7Reg2Yiqs_...txt`)
- **Daily Breaker之間的「中段」才是最佳交易區間**：不追求抓到bullish/bearish breaker的絕對高低點，而是專注在兩者「中間地帶」找設定，因為那裡最容易形成setup (`3B7Reg2Yiqs_...txt`)
- **"Macro"時間窗口（如9:50-10:10）為進場最佳時機的具體化**：延續kill zone概念但更精細到20分鐘窗口，用於直接抓turtle soup式的buy/sell side liquidity run (`3J8drYX2zHM_ICT 2026 Asian Session Short Review ⧹ April 14, 2026.en.txt`)
- **把「wick」本身當作gap來分級(grade)並套quadrant/eighths**：影線內部一樣可切consequent encroachment、upper/lower quadrant，甚至更細的1/8分位，稱為「gradient levels」(`3J8drYX2zHM_...txt`, `486N8ow3U2A_ICT Technical Review ⧹ NQ Futures March ⧹ February 03, 2026.en.txt`)
- **「不是Plan A/Plan B」的單一偏見原則**：明確反對「兩邊都下注、事後只講對的那一半」的做法，堅持只給一個方向的偏見，即使可能出錯也要公開負責，藉此與「事後諸葛」的分析師劃清界線。引用：「it's not me picking both sides in the marketplace and then when it unfolds One Direction then I'll say see how smart I was that's what trolls will say about me」(`3TVdmXWTCTQ_ICT Market Review - July 06, 2022.en.txt`)
- **20 pip「麵包奶油(bread & butter)」scalping模型：Order Block位於FVG「內部」而非緊鄰**：與核心教學中「高機率order block=下跌蠟燭緊鄰FVG」不同，這個模型專找沒有明顯gap的order block，等待expansion swing出現後回頭在swing內部找FVG進場，藉此避免錯過原本會漏掉的機會 (`3xgtrXok-xs_ICT Charter Price Action Model 12 - Scalping Intraday Model.en.txt`)
- **前一段range的1/4作為突破後延伸目標的經驗法則**：非源自任何技術分析書籍，純粹是他多年觀察歸納的「經驗法則」("just a general rule of thumb")，用於判斷創新高後還能漲多遠 (`403Dzt_Vl5Y_NQ December 05, 2024 Seek & Destroy Review.en.txt`)
- **Silver Bullet交易的精確定義（10-11am NY窗口）首次清楚展開**：專找FVG、目標最低5個handle，是他「如果一天只能交易一次」會選的設定；PM session的2-4pm為「sweet spot」，通常延續早盤方向 (`441vklRYYR4_Emini S&P 500 Review - April 12, 2023.en.txt`)
- **高波動/地緣政治干擾期的因應心法：新手應「暫停數月」等市場恢復乾淨走勢**：明確建議經驗不足者在極端環境下直接停止交易、春天再回來，而非硬撐 (`486N8ow3U2A_...txt`)

## 2. 決策啟發式（續）

- Daily bias流程完整步驟：COT commercials 12個月淨部位→open interest(僅≥15%異動時參考)→daily institutional order flow(上漲支撐在down-close蠟燭/下跌受阻在up-close蠟燭)→週度輪廓預測(用經濟日曆)→SMT背離→market structure/breaker→PD array matrix，七步驟依序疊加得出每日方向 (`3B7Reg2Yiqs_...txt`)
- 週度區間主體通常落在週二到週四；他甘願放棄「週一低點」，等週二依週一低點找optimal trade entry，若週二沒有再等週三依週二低點 (`3B7Reg2Yiqs_...txt`)
- 一週交易信心隨時間遞增：週一過後對higher time frame判斷有60%把握，週二後70%，週三到週五持續up-date (`3B7Reg2Yiqs_...txt`)
- 用weekly開盤價(Sunday)與週一午夜開盤價(New York time)兩者作為當週方向濾網，看價格是否能在其上/下方運行 (`3B7Reg2Yiqs_...txt`)
- 契約展期(rollover)規則：以barchart.com上的open interest為準，當次月合約未平倉量超過當月合約時才轉倉，而非依到期日硬性規定 (`3TVdmXWTCTQ_...txt`)
- Silver Bullet停利門檻：找到FVG後至少要有5個handle的空間才會考慮進場 (`441vklRYYR4_...txt`)
- 高波動期間縮小部位規模至最多1-3口micro，即使是教學示範也刻意展示小部位以避免帶頭示範過度槓桿 (`486N8ow3U2A_...txt`)
- 新週開盤缺口(new week opening gap)可作為當週第一個重要的liquidity draw / 支撐阻力參考點 (`486N8ow3U2A_...txt`)

## 3. 表達DNA（續）

- 直播中坦承「刻意嘗試做一筆虧損交易」以回應觀眾對回撤(drawdown)教學的請求，展現教學不怕虧損的態度：「I was actually trying to take a losing trade... I'll have to create some kind of drawdown to teach how to resolve drawdown later this year」(`3FGFEuaDSOc_ICT Mentorship 2023 - July 07, 2023 Live NQ Futures Trading.en.txt`)
- 生活化背景音干擾：太太洗衣間門沒關、烘衣機聲音入鏡，自然帶過不中斷錄影 (`3FGFEuaDSOc_...txt`)
- 反覆用「toggle market replay」實機操作證明非回放，並抱怨「還是有很多goober寄信說是market replay」(`3FGFEuaDSOc_...txt`, `3J8drYX2zHM_...txt`)
- 引用聖經措辭包裝行情邏輯：「just like it says in the Bible, first one now should lay to be last」用來描述NASDAQ與S&P強弱互換的sympathy play (`3TVdmXWTCTQ_ICT Market Review - July 06, 2022.en.txt`)
- 對「頻道會被刪除」謠言的直接闢謠開場白：「just so you guys know, Channel's not getting deleted」，顯示外界曾流傳他帳號將被移除的傳言 (`403Dzt_Vl5Y_...txt`)
- 反覆用「Bitcoin到10萬美元」等大眾話題點綴市場評論收尾的幽默方式 (`403Dzt_Vl5Y_...txt`)
- 對CPI/NFP等高風險新聞日的一貫警語：「CPI is very risky...if you're wrong it can rip your face off」，同時仍願意公開show hand讓學生知道他的方向偏見以滿足好奇心 (`441vklRYYR4_...txt`)
- 對「市場太難、太操縱」時期的溫和勸退語氣，罕見地承認「everybody's methodology right now...has caused a doubt or a concern」，並用「your head cleanly removed from your shoulders」形容高波動期裸露部位的下場 (`486N8ow3U2A_...txt`)

## 4. 決策紀錄（續）

- 2023/07/07 NQ live trading：全程實盤含刻意做一筆虧損單的心理實驗，多筆分批進出，單日損益達$26,240，並逐步公布macro教學預告(週日下午2點) (`3FGFEuaDSOc_...txt`)
- 2026/04/14 Asian session：用9:50-10:10 macro窗口配合turtle soup示範一筆完整實盤空單，並在X上全程直播（非事後剪輯）(`3J8drYX2zHM_...txt`)
- 2022/07/06 S&P/NASDAQ/Gold FOMC後分析：詳述兩指數SMT背離與sympathy play邏輯，公開展示無隱藏偏見的「單一方向」判斷 (`3TVdmXWTCTQ_...txt`)
- 2024/12/05 NQ NASDAQ：精準命中週日盤前給出的21580.25上緣目標(僅差0.25點)，隔日轉向下方21490賣方流動性池，並宣布假期後恢復每日Forex市場評論 (`403Dzt_Vl5Y_NQ December 05, 2024 Seek & Destroy Review.en.txt`)
- 2023/04/12 ES：CPI當日精準命中4180目標(僅差1 tick)，隨後用Silver Bullet與PM session框架命中最終標準差-3的41 13.5低點，形容「you can't improve on perfection」(`441vklRYYR4_Emini S&P 500 Review - April 12, 2023.en.txt`)
- 2026/02/03 NQ/ES：用daily suspension block的consequent encroachment作為當日多空分水嶺，精準預告「新週開盤缺口」會被觸及且被觸及後持續破底，SMT用NQ/ES累積高點線比對佐證 (`486N8ow3U2A_...txt`)

## 5. 時間線/背景線索（續）

- 提及自己「已不再交易S&P」，COT/institutional分析經驗主要來自過去交易債券與S&P的年代（呼應早年bond/S&P配對交易的敘事）(`3B7Reg2Yiqs_...txt`)
- 私人mentorship與YouTube mentorship同時並行錄製的證據：`3FGFEuaDSOc`開頭提及「both mentorship groups both YouTube and the private mentorship in this video」，說明至少到2023年兩軌內容仍偶有並存 (`3FGFEuaDSOc_...txt`)
- 2024年12月表示因「假期/holiday season for ICT」而暫停每日市場評論，並預告2025年將恢復每日產出Forex/商品市場評論 (`403Dzt_Vl5Y_...txt`)
- 2026年初(2-3月)市場處於高度政治/總體干擾期，他公開建議新手「休息到春天」，顯示他對市場環境难度的分级判斷會直接影響教學建議的積極度 (`486N8ow3U2A_...txt`)

## 6. 矛盾與演變（續）

- 「20 pip模型」的教學與核心理論存在方法論分歧：Price Action Model 12刻意使用「不符合他自己定義的高機率order block」(沒有緊鄰FVG的下跌蠟燭)，並坦承「會是錯的」但仍將其視為有效模型，顯示他在不同教學脈絡下對同一詞彙(order block/高機率)的定義存在情境性彈性，而非嚴格一致。
- 對「開頻道會被刪」的闢謠透露一種防禦性敘事模式的延續：與批次1-6反覆出現的「反造假」、「反抄襲」、「反詐騙帳號」等自我澄清話術屬同一系列，顯示他持續處於對外部質疑/謠言的警戒狀態。
- 對「難以交易的環境」的應對前後略有反差：早期批次(如批次3的COT「million dollar secret」)展現強烈自信與精準案例堆疊；本批次`486N8ow3U2A`則罕見大篇幅承認「這是史上最難時期之一」、鼓勵新手直接放棄交易數月，顯示他的自信表述會隨盤勢難度與觀眾組成(新手 vs 老手)動態調整，並非固定基調。

---
### 批次8 (檔案42-45，最終批次) 補充

## 1. 心智模型候選（續）

- **交易風格必須與「經驗不足者的恐懼」脫鉤——五步驟交易計畫框架**：Preparation(準備)→Opportunity Discovery(機會發現)→Trade Planning(交易規劃)→Execution(執行)→Trade Management(交易管理)，他認為任何模型都可套用此五階段骨架 (`4f1vjQMlV50_ICT Charter Price Action Model 1 ⧹ Trade Plan & Algorithmic Theory.en.txt`)
- **交易模型=演算法(if-then流程圖)**：明確用「找到一顆壞掉的燈泡」的日常生活演算法類比說明交易模型的本質——一連串條件判斷("if this condition, then...")，而非模糊的直覺 (`4f1vjQMlV50_...txt`)
- **Fibonacci本身沒有任何魔力，「nothing」使其有效**：直接反駁提問「什麼讓Fibonacci如此強大」——他認為真正核心是institutional order flow與tape reading，Fib只是輔助劃出範圍的工具，「price doesn't care about Fibonacci」(`49Nz1pPLEWI_ICT Weekly Recap & Table Talk Session - 11⧸17⧸17.en.txt`)
- **明確否定DOM/depth of market/footprint/order book等訂單流工具的有效性**：認為這些數據在外匯市場中本質上看不到央行等級的真實訂單，「brokers can't manipulate price except for just a small little sample size of a spread...it's already predetermined... at the central bank level that's where price comes from」(`49Nz1pPLEWI_...txt`)
- **Power Three起源故事：直接受Larry Williams「自曝弱點」啟發**：Larry Williams曾公開承認不理解為何有人能在開盤價之下就买进(up-close day仍能低接买入)，這句話刺激他把「弄懂開盤價下方买進的秘密」當作終身志業，耗費約10年才自認破解，即Power Three的起源 (`49Nz1pPLEWI_...txt`)
- **對White(Wyckoff)理論的態度：部分認可、部分認為不夠精確**：坦承自己的market maker buy/sell model部分受Wyckoff（春天/spring等概念）啟發，但認為Wyckoff「有時候有、有時候沒有」不夠科學，而他的模型「每次都在特定價位精準出現」("it's there every single time...to a science") (`49Nz1pPLEWI_...txt`)
- **「輸出教學是為了填補自己成長過程中的情感缺口」**：罕見自我剖析——由祖父母帶大、與父母關係疏離，用交易教學社群獲得的認可與崇拜感來填補內心缺憾，坦言帶有強迫性人格(OCD)驅使 (`49Nz1pPLEWI_...txt`)

## 2. 決策啟發式（續）

- Price Action Model 1(scalping)完整規則：用過去20個交易日(不含週日)的ipda data range抓高低點，決定bias後只在New York Kill Zone(7-10am，數據日可延至11am)5分鐘圖找optimal trade entry，目標15-20 pips，只在週一至週三交易(週四視情況、週五完全不做) (`4f1vjQMlV50_...txt`)
- 停損管理採漸進式：獲利達預期目標25%時停損減25%風險，50%時減50%風險，75%時移至損益平衡；一旦停損出場「當日不再重新進場」(one and done) (`4f1vjQMlV50_...txt`)
- 風控的對稱規則：連續5筆虧損後每筆下降50%風險直到回補50%虧損；但連續5筆獲利後同樣要主動调降風險50%，防止自滿導致大回撤，「if you take a series of five winning trades in a row drop your R percent by 50%」(`4f1vjQMlV50_...txt`)
- 部位規模計算公式：Position Size = Account Equity × R% ÷ Stop Loss(pips)，並提供具體貨幣對照範例(標準手/迷你手/微型手) (`4f1vjQMlV50_...txt`)
- 大關卡位(big figure，如128.00)向外突破後，預期會再延伸10-20 pips，作為停利/停損校準的經驗法則 (`49Nz1pPLEWI_...txt`)
- 若價格在monthly bearish order block中點附近止步未達，仍可退而求其次，改在consolidation區間底部找空單進場，並接受「沒有拿到最低點也沒關係」的心態 (`49Nz1pPLEWI_...txt`)

## 3. 表達DNA（續）

- 對Twitter刪文政策的自我修正說明：「I don't delete my Twitter tweets anymore. I used to do it and purge it」——顯示這是他多年後才建立的"從不刪文"原則，早年其實會定期清除貼文，與批次1教學中強調的「我從不刪除任何東西」構成時間軸上的演變而非恆定事實 (`49Nz1pPLEWI_...txt`)
- 公開2010年「社會實驗」自白：坦承早期經營YouTube頻道時，刻意觀察觀眾是否只是被動娛樂(entertained)而非真正學習，稱觀眾為「guinea pigs」，且「none of you knew that you were guinea pigs」(`49Nz1pPLEWI_...txt`)
- 對假造交易截圖跟風者的直接點名批評：觀察到部分粉絲偽造「假裝進場」的圖表(未顯示真實訂單線)博取認同，直言「你不需要那種吹捧」("I don't need that type of stroking")(`49Nz1pPLEWI_...txt`)
- 罕見坦承自身弱點且反覆致意「這是我一輩子的痛」：明確表示25年來始終無法設計出一套「像entry一样固定公式化」的出場策略，稱為「my masterpiece」、「a thorn in my side」，並希望學生有朝一日能替他解決 (`49Nz1pPLEWI_...txt`)
- 完整公開師承系譜：Ken Roberts(入行启蒙、首次爆倉)→Larry Williams(1995年課程，最大影響)→Chris Lori(Asian range概念來源，特別聲明無業務往來)→AOL論壇上的Wyckoff愛好者(90年代末，啟發market maker模型雛形)，並推薦書單：Larry Williams《How I Made a Million Dollars Trading Commodities Last Year》、Linda Raschke & Larry Connors《Street Smarts》、John Murphy《Intermarket Analysis》與《Technical Analysis of Financial Markets》(`49Nz1pPLEWI_...txt`)
- 對論壇/YouTube留言板搗亂者毫不留情：「you only get one chance to act stupid...BAM」，明確採取一次違規即封鎖的鐵腕態度 (`49Nz1pPLEWI_...txt`)
- 用畫家調色盤/畫筆比喻說明「不需要每個模型都用上所有工具」：「an artist...they don't use every single paintbrush every single time」(`4f1vjQMlV50_...txt`)

## 4. 決策紀錄（續）

- 2017/11月某週：EURUSD原先設定的月線bearish order block中點1.1864空單目標未達成(僅差一點點)，被迫改在consolidation低點附近進場空單，仍精準命中週線低點附近(呼應「不用追求完美」心法)；同週GBPUSD/USDCAD亦有對應進場案例，並提及找到1994年的舊交易筆記本 (`49Nz1pPLEWI_ICT Weekly Recap & Table Talk Session - 11⧸17⧸17.en.txt`)
- 示範完整的Price Action Model 1演算法規則(牛市/熊市兩版本)，作為mentorship「訓練輪」等級的基礎模型公開教學範例，未涉及當日實盤 (`4f1vjQMlV50_...txt`)

## 5. 時間線/背景線索（續）

- 詳細自曝成長背景：由祖父母撫養長大、與親生父母關係疏離，將交易教學視為填補情感缺口的途徑，自陳有OCD傾向 (`49Nz1pPLEWI_...txt`)
- 生涯起點時間軸更完整：1994年已有手寫交易筆記(GBPUSD)；1995年購入Larry Williams課程；1999-2000年間曾「過度槓桿、常不設停損」並自認高估自己能力，適逢商品牛市僥倖獲利，之後在AOL論壇上因批評Wyckoff追隨者而「自曝是酸民(troll)」，後來才反省接受部分Wyckoff概念 (`49Nz1pPLEWI_...txt`)
- 提及自己曾用最原始的「quote tracker」機器(類似隨身收音機大小的報價機)人工記錄每小時最高最低價，形成日後「日內範圍」分析方法的雛形 (`49Nz1pPLEWI_...txt`)
- 2017年11月時點：兒子已固定協助他在Twitter發布圖表/錄製教學內容的截圖 (`49Nz1pPLEWI_...txt`)
- 交易紀錄工具偏好：不使用MT4，透過ForexLTD demo(因為該券商提供dollar index數據)，交易電腦完全獨立、不上網僅接C-Signal數據，呼應後期批次(如`0BpG3Ee_kIc`)提到的隔離ISP資安習慣，顯示此原則至少從2017延續到2020年代 (`49Nz1pPLEWI_...txt`)

## 6. 矛盾與演變（續）

- 「從不刪推文」原則的時間軸矛盾：本批次`49Nz1pPLEWI`(2017年)明確說「我現在不刪了，過去我會定期清除」，而多個更晚批次(如批次1的`-L9XMj50XG0`)則將「我從未刪除任何東西」當作恆定不變的誠信象徵反覆強調——顯示這條「零刪除」原則其實是在某個時間點才建立的政策，並非他一貫的做法，是所有批次中最明確的一個「自我敘事被簡化為永恆真理」案例。
- 對「工具有效性」的態度反覆自我拉扯：`49Nz1pPLEWI`中他一方面說「Fibonacci本身没有任何力量」、贬低DOM/footprint等工具，另一方面又花大量篇幅展示如何精準使用Fibonacci retracement/extension——這與其他批次「工具只是工具，不是聖杯」的立場一致，但本檔案的表述更為激烈和絕對化("nothing makes Fibonacci powerful")，顯示他有時會用誇張化的措辭來強調同一個穩定觀點。
- 「不给学生传帮带、每個人都要靠自己」與「渴望學生教會他東西」的並存：他一方面反覆強調不做一對一手把手教學、拒絕輔導請求，另一方面又深情地表示希望某個學生能替他解決「出場策略」的終身難題並與他平起平坐討論——顯示他自認的「高高在上導師」形象與「渴望被同行認可、渴望有人能超越自己」的脆弱面同時並存，是全部45篇逐字稿中最少見的一次深度自我揭露。

---
### 補漏檔 (`3OEUIkkcmLE_ICT Forex - The ICT London Close  Killzone.en.txt`)

## 1. 心智模型候選（續）

- **Power Three為完整daily range的最終骨架**：London Close Killzone補上day range的第四個/最後一個參考點，令open/high/low/close四點齊備，構成「accumulation→manipulation→distribution」的完整敘事，「we have been able to define the four reference points that make up power three」。
- **London Close Killzone的雙重行為模式（反轉 vs 延續）**：同一時間窗口(10am-noon NY)可能製造當日高/低點反轉，也可能只是既有趨勢的continuation pattern，兩者取決於當天整體方向偏見，不是單一固定劇本。
- **Z day與Seek & Destroy day為「不宜使用本方法」的市場狀態分類**：Z day指整天橫盤震盪的安靜盤整；seek and destroy day指整天雜亂上下、直到尾盤才一次掃損噴出，兩者皆被明確標記為此類設定「不會有效」的例外情境。
- **教學內容的價值不取決於篇幅長短**：明確反思自己「一貫產出長影片」的習慣，主張這次簡短精確的教學同樣「藏有大量洞見」，暗示他對教學形式與內容深淺之間並無必然對應關係的自覺。

## 2. 決策啟發式（續）

- London Close Killzone時間窗：10:00am-12:00pm New York time，通常只值得10-20 pips的scalp，超過20 pips屬罕見情況。
- 分析London close必須用5分鐘圖，「anything higher than that you're not going to get the detail you need」，這是他對此特定killzone少見的「僅限單一時間框架」明確規定。
- 一般經驗法則：若當日為up-close（收高於開盤）的偏多日，高點多半在10am-noon窗口內形成；偏空日則低點多半在此窗口形成。
- 若London/紐約盤已朝同一方向延續（如整晚偏多），預期London close窗口會製造「當日高點」；但若窗口前已出現premium side的雙重高點(liquidity pool/double top)，則預期窗口會變成反轉點而非單純高點，之後隔日還會延續走弱。

## 3. 表達DNA（續）

- 開場沿用一貫「hey folks welcome back」句式，但結尾罕見地改用「hopefully you found this teaching insightful, you can find more at the innercircletrader.com」，而非常見的「good luck and good trading」收尾——為既有收尾語庫增添一個變體版本。
- 自我評論教學風格與慣性反差：「you're used to very long videos from me but the insights I've given you are very concise...I've given you the DNA if you will」，用DNA比喻總結整支系列教學的精華濃縮性。

## 4. 決策紀錄（續）

- 本檔案性質為純教學示範（非實盤/非特定日期交易記錄），依序展示Dollar/CAD、EUR/USD、AUD/USD、USD/JPY等多組歷史圖表案例，逐一驗證London Close Killzone對應reversal或continuation兩種型態，未提供具體下單價位或損益數字。

## 5. 時間線/背景線索（續）

- 內容延續同系列的Asian/London/New York session教學脈絡（「We went through the Asian session the London session the New York session and now we've completed the daily range with the London close killzone」），顯示與批次1提及的Month 08系列（`-cXnnHjy9s0`，2017年4月ICT mentorship）屬同一課程脈絡的補完單元，無新增獨立時間線索。

## 6. 矛盾與演變（續）

- 收尾用語出現罕見變體：多數批次影片以「I wish you good luck and good trading」收尾，本檔案改用「you can find more at the innercircletrader.com」的導流式結尾，補充其收尾語並非100%固定公式、偶有依內容性質（偏教材/工具型教學）調整的證據。



