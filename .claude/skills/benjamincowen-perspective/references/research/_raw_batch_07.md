# Benjamin Cowen Raw Research Batch 07
來源：_batch_manifest_07.txt（共 48 個逐字稿，實際處理 48/48）

## 1. 心智模型候選 (candidate mental models)

- **量化風險帶 (0–1 Risk Metric)**：把多個 on-chain／social 指標正規化到 0–1，用來定位目前處在整個市場週期的哪個階段，而非預測單一價格。「we took a look at all these and we normalized their prior moves to between zero and one... the goal is to then get an idea of where we are within any market cycle」(`2DUCJDmTOks`)。同一套邏輯也用在 social risk（重新設計版，加入 Coinbase app 排名與 Google Trends）(`WwzQ6gjktHs`) 及 ETH 專屬風險指標 (`bYVD2U-3OlA`)。跨多檔反覆出現，是他最核心、最常掛在嘴邊的分析工具。歷史規律：風險 <0.1 是好買點，>0.8 是過熱賣點；「historically, some of the best times to buy Bitcoin are when the onchain risk drops to between zero and 0.1」(`2DUCJDmTOks`)。

- **對數迴歸帶／「回家」框架 (Logarithmic Regression / "going home")**：每個資產都有一條隨時間增長的「公允價值」對數迴歸線（下緣＝「牛市支撐帶」，上緣＝隨資產成熟而抬升的壓力帶）。當價格跌破前一輪高點支撐、進入這條迴歸帶內，他稱之為「go home」，且經驗上這是牛市延續前的必要條件而非利空。「Ethereum going home is just simply the idea that at some point ETHUSD during the ETH Bitcoin downtrend will break its support and when it does that's when it goes home」(`bYVD2U-3OlA`)。他在 2019 就建立此模型並公開追蹤紀錄（`vuwmJsNsONk`），屬於他自創且反覆驗證的招牌工具。

- **Alt 是「best-case oscillator」／BTC dominance 優先**：他認定山寨幣集體對 BTC 的估值（total3−USDT／BTC 等比率）在牛熊之間震盪於固定區間（樂觀上緣≈與 BTC 等市值，悲觀下緣≈BTC 的 1/4），不具備長期跑贏 BTC 的結構性理由；因此他長期偏好持有 BTC（或 BTC+ETH）而非分散山寨幣。「altcoins to be oscillators at best」(`4Wldu8lDIOo`)；「I still think you're going to have that that sort of that slight downturn」... 更明確：「the collective altcoin market would collectively drop to 25% of Bitcoin's market cap or 0.25」(`EEoBA2GMswo`)。跨幾乎每一支影片反覆出現，是他和「alt season」敘事對立的核心立場。

- **貨幣政策狀態機 (QT/QE、聯邦基金利率 vs. 2年期殖利率作為「中性利率」代理)**：他用聯準會資產負債表變化（QT/QE）與「聯邦基金利率是否高於2年期殖利率（視為中性利率的近似）」來解釋跨資產的風險偏好切換，而非單純用敘事/新聞解釋價格。「if the Fed funds rate is above the neutral rate, the economy slows down... if the Fed funds rate is below the neutral rate, the economy speeds up」(`E66AXmddwL0`)。他反覆用這套框架解釋 alt/BTC 比率為何遲遲不轉向、ETH 為何需要等到「QT 結束」才會有結構性反轉（`HUbjGbOju2M`, `vuwmJsNsONk`）。

- **四年週期的機率化時間框架 (cycle timing via ROI-from-low / ROI-from-having)**：他不是用價位目標，而是用「距離上次低點過了多少天」「距離減半過了多少天」等時間序列來對齊歷史高低點，據此推算topping/bottoming窗口，並明確承認這是機率不是確定性。「Bitcoin topped on day 1,062. The cycle before, it topped on day 1,059. The cycle before that... 1,068」(`rKjce1jCxSM`)。同一手法用在多支影片判斷 Q4 頂部、2 月低點等（`gkDqbvMnMHI`, `GPyKx7pthe4`）。

- **跨資產類比覆蓋法 (bar-pattern overlay across analogous assets)**：他大量把不同資產（BTC 2016-17 vs 現在、ETH vs Tesla、ETH vs Monero、Bitcoin dominance vs 鈀金 vs 恆生指數 vs 穩定幣主導率）的走勢圖案「剪貼」互相比對，尋找「同一種市場心理模式」（先前高點被掃、拉回到牛市支撐帶、再度突破）以此類推當前資產的下一步。「we've seen this pattern... Bitcoin dominance... the HSI... Palladium... and the unfortunate chart is stable coin dominance」(`ZuWWt3U3UBQ`, `rKjce1jCxSM`)。這是他非常獨特、跨批次反覆出現的方法論招牌。

- **業務週期圖表 (ITC Business Cycle Chart) 與「棋局將死」比喻**：自建公式 S&P500 ÷（失業率² × 利率 × 年增通膨）／M2，用來標定景氣循環所在階段；並用西洋棋「製造兩個弱點、對手無法同時防守」比喻聯準會同時面對通膨與失業惡化時的困境。「the Fed can defend one weakness... they cannot defend two. And that's what usually leads to the end of the business cycle」(`JGXGlgF0nMA`, `itxqiPH2vIY`)。

- **熊市三階段心理模型**：把熊市拆成三個約各四個月的階段——階段一「只有少數人相信」、階段二「約一半人相信」、階段三「多數人相信」，並主張「當所有人都相信熊市時，熊市通常已經結束」。「once everyone believes in the bear market, that's usually when the bear market ends」(`gkDqbvMnMHI`)（推斷：此為他對群眾心理逆向指標的一貫應用，可能是即興構建的框架而非長期沿用模型）。

## 2. 決策啟發式 (decision heuristics)

- 若 BTC 週線連續兩次收在 50 週均線之下 → 週期頂部大機率已確立；只收一次不足以下定論，需等第二次確認。來源(`ZuWWt3U3UBQ`, `-qmJLRKbrn4`)。
- 若「死亡交叉」（50 日均線下穿 200 日均線）出現 → 歷史上常標記局部低點而非崩盤起點；因此不要在死亡交叉當天恐慌賣出，反而是短期買點候選。來源(`V3AHyJn1c9k`, `otl3Slpfwsc`)。
- 若「黃金交叉」出現 → 有兩種歷史模式：(a) 交叉前上漲、交叉當天/後小幅回調再續漲（2021, 2019-2020風格），(b) 交叉前上漲、交叉後直接續漲不回調（2023, 2024）；他承認自己在 2023 誤判為(a) 而錯過行情，2024 改為不預設回調而站對邊。來源(`V3AHyJn1c9k`)。
- 若 on-chain/social risk 落在 0–0.1 → 歷史上是好買點；落在 >0.8 → 歷史上接近過熱賣點；用於動態 DCA（越低風險越買、越高風險越減）而非一次性全進全出。來源(`2DUCJDmTOks`)。
- 若 ETH/BTC 觸及／跌破迴歸帶下緣（「回家」）→ 往往預示 ETH/BTC 已經或接近見底，隨後 ETHUSD 有機會展開對 BTC 的相對強勢／衝擊新高。來源(`bYVD2U-3OlA`, `ZZNFVcbzUE4`)。
- 若某資產／某比率第一次觸及前高並「假突破」拉回牛市支撐帶 → 依過去多次類比（BTC dominance、鈀金、恆生指數、穩定幣主導率）判斷這通常不是頂部，而是下一波更高高點前的最後洗盤。來源(`ZuWWt3U3UBQ`, `rKjce1jCxSM`)。
- 若聯邦基金利率仍高於 2 年期公債殖利率（他視為「中性利率」代理）→ 貨幣政策仍屬緊縮，alt/BTC 比率應持續偏弱，不宜看多 alt season。來源(`E66AXmddwL0`, `d-59tV33JJ4`)。
- 若股市（S&P500）持續下跌並「停留」在低位數月 → 才會真正導致企業裁員與衰退；股市下跌是因，裁員是果，而非相反；因此觀察「停留時間」比單次跌幅更重要。來源(`itxqiPH2vIY`, `bYVD2U-3OlA`)。
- 若失業率上升僅發生在「部分州／地區」而非全國普遍 → 尚不足以構成典型衰退訊號；須看到近乎全州同時惡化（如 2008、2001）才算數。來源(`8LEFZpdL0gQ`)。
- 若 Bitcoin supply-in-profit 與 supply-in-loss 兩條線收斂交叉 → 歷史上多次對應週期底部（2014、2018、2022），但此指標「更適合抓底部、不適合抓頂部」（因牛市可在高位停留數年）。來源(`XiXsP4Ch5no`, `joW6YbFRDI0`)。
- 若某資產剛掃過前波區間低點 (range low sweep) → 傾向於視為看漲訊號（因低點被掃通常伴隨買盤湧入），但需搭配是否能站回關鍵位（如 100K）判斷是否延續。來源(`3cUr9DP1UEM`)。
- 民調／群眾偏向：60/40 或 70/30 的多數方通常仍是對的；只有當比例拉大到 75–80% 以上時，「群眾總是錯的」這種逆向思維才開始比較可靠。來源(`gkDqbvMnMHI`)。

## 3. 表達DNA (expression DNA)

- **固定開場**：「Hey everyone and thanks for jumping back into the cryptoverse/macroverse/equityverse/heavy metal verse.」依主題切換「verse」後綴（crypto/宏觀/股市/金屬），是他標誌性且極高頻的開場句式，出現在幾乎每支影片。
- **固定收尾**：「If you guys like the content, make sure you subscribe to the channel, give the video a thumbs up, and check out the sale on Into the Cryptoverse Premium at intothecryptoverse.com. I'll see you guys next time. Bye.」高度公式化，帶產品導流（ITC Premium訂閱、benjamincowen.com報告）。
- **招牌口頭禪／格言**：
  - 「All models are wrong, some are useful.」(`HUbjGbOju2M`, `XiXsP4Ch5no`, `joW6YbFRDI0`) — 每次介紹自製指標都會加這句自我提醒式免責聲明。
  - 「Trade the market that you have, not the market that you want.」(`3cUr9DP1UEM`, `-qmJLRKbrn4`) — 反覆用於提醒讀者不要用一廂情願取代客觀數據。
  - 「Bears sound smart, bulls make money.」(`3dSPMPi0XjI`, `itxqiPH2vIY`) — 描述多空辯論中長期而言看多方賺錢、看空方顯得聰明的矛盾。
  - 「No one has a crystal ball.」／「I don't have a crystal ball.」極高頻（幾乎每支影片出現1次以上），用來為預測加上不確定性但又緊接著給出具體機率或情境。
  - 「Markets don't need a reason to go up, they need a reason to go down.」(`8LEFZpdL0gQ`, `qrlOI5XlKR0` — 「climbing the wall of worry」概念)。
  - 「Bear markets make fools of both bulls and bears.」(`mUEsVBXxmUc`)。
  - 「Topping is a process, bottoms are events.」(`qrlOI5XlKR0`)。
  - 「Don't marry an asset class, go where the bull market is.」(`Ed9h6x9nhCU`)。
  - 「I don't control the market/rules of the cryptoverse, I just enforce them.」(`3cUr9DP1UEM`, `CBwvg-Vust8`) — 用來撇清他不是在「操控敘事」而只是陳述客觀規律。
  - 「Dubious speculation」作為系列影片標題本身即是一種語言標記：承認自己接下來要說的是帶不確定性的推測，反覆用在 BTC/ETH 週報式影片標題（`otl3Slpfwsc`, `TWax8cGppRQ`, `GPyKx7pthe4`, `CBwvg-Vust8`, `J-QHMNnRK-Q`, `cykp__hdCgk`等）。
- **高頻專屬術語**：risk metric／risk band、logarithmic regression trend line、fair value、bull market support band／bear market resistance band、going home、Satoshi-denominated portfolio、dominance（Bitcoin dominance、ETH dominance、stablecoin dominance）、total3 minus USDT divided by Bitcoin（alt/BTC 比率）、ROI from the low/having、running one-year ROI、death cross／golden cross、QT/QE、neutral rate、diminishing returns（報酬遞減）、oscillator（形容 alt）、butterfly harmonic（形容潛在的假突破後更深回檔）。
- **確定性語氣的特殊操作**：他常先鋪陳「我不是有水晶球」，再明確給出百分比機率（如「60 to 70% chance the top is already in」`9g1QsTVizyQ`），呈現「科學式的機率語言」而非武斷斷言；且會清楚劃分「這是我推斷的 base case」vs「這是既定事實」。
- **對炒作/敘事的態度**：明顯敵視「alt season」呼喊者、「super cycle」論者、被付費宣傳山寨幣的 KOL；反覆諷刺「for the 30,000th 74th time」(`d-59tV33JJ4`)、稱他們「shilling garbage altcoins/memecoins」、「getting paid to promote garbage」(`d-59tV33JJ4`, `ZuWWt3U3UBQ`)。同時也反擊「permabull/permabear」，主張兩者都會在某個時點顯得愚蠢。
- **自我修正／透明度**：主動公開過去判斷錯誤的例子（2023 年黃金交叉後預期回調卻沒發生；ETHUSD 路徑判斷錯誤但 ETH/BTC 判斷正確），並用「own it」「lick my wounds」等措辭承認錯誤，強調「我不是要騙你們，寧可告訴你們不中聽的真相」（"I'd rather tell you an inconvenient truth than feed you a lie" `ZuWWt3U3UBQ`）。
- **擬人化比喻／輕鬆語氣調劑嚴肅內容**：把 ETH 比擬成一個「回家喝一杯、看超級盃、去地下室找點心」的人物（`ZZNFVcbzUE4`），用西洋棋比喻聯準會的政策困境，用「we are living in a simulation」形容歷史重演感（`mUEsVBXxmUc`）。
- **收尾常見詩意句**：「Eventually the entire asset class will go to $10 trillion plus or minus a few trillion. And as we go to sleep at night, we cannot help but wonder what's a few trillion dollars among friends.」在多支「Beauty of Mathematics」系列影片重複出現，是他固定的詩意收尾梗(`IqADDSGQDdo`, `uoF9yzXHmt4`)。

## 4. 市場判斷案例 (analysis cases)

- **BTC 50週均線攻防與 2019 類比**：反覆將本輪週期（2025年10月見頂、非歐福里亞式）與 2019 年（同樣非歐福里亞頂、QT 結束前見頂）類比，預期 2026 迎來約 50–70% 的中期熊市、目標區 60–70K（200週均線）。「my guess is that Bitcoin will have its date with destiny at the 200E moving average in 2026... somewhere between 60 and 70K」(`3dSPMPi0XjI`)。
- **ETH「回家」後衝擊新高再回檔**：長期主張 ETH 需先跌回對數迴歸帶下緣（約1500-1600）才能真正展開牛市；2025年4月「Welcome Home, Ethereum」(`bYVD2U-3OlA`)，隨後2025年8月衝上新高(`0mY0CglvElA`)，並精準預期9月回檔、10月再衝高的路徑（`0mY0CglvElA`）。之後又在另一輪週期二度提出「Welcome Back Home, Ethereum!」(`ZZNFVcbzUE4`)，預期2026整年在迴歸帶內盤整，目標公允價值約2000。
- **Solana/BTC 比率看空**：延續 ETH/BTC 見頂的分析框架，主張 SOL/BTC 只是「重演 ETH 走過的路」——四重頂、跌破higher-low結構、進入二次派發階段，目標看向更低位；並批評「memecoin 超級週期」敘事其實是掩護派發。「the very thing that people think was helping salana was is actually the thing hurting it」(`4Wldu8lDIOo`)。
- **Bitcoin Dominance 長期看多／alt 持續失血**：從 2021-2022 起長期看多 BTC 主導率，目標曾設 60%，後續逐步上修至 66%、70%+；反覆用 Fib 回撤位與 alt/BTC 比率解釋為何每次「alt season」呼聲響起後都以失敗告終。「altcoins have been bleeding to Bitcoin for years... alts are oscillators at best」(`ASASjr93enU`, `d-59tV33JJ4`)。
- **鈀金 (Palladium) 結構性看多**：自 2025年9月約1080-1090起持續看多鈀金，並用「先前假突破再真突破」的相同套路做目標推演（目標區約2150-2350），同時提醒鈀金波動性大於黃金/白銀，不宜過度自滿。(`Ed9h6x9nhCU`, `ZuWWt3U3UBQ`)。
- **DXY（美元指數）判斷**：預期美元在降息後反彈到約110後於選後年崩跌，並在低點附近（`wdPiMb2xJqY`）主張已跌足、可能接近階段性低點，較同業更早看到反轉跡象。
- **S&P500 中期年（midterm year）季節性劇本**：反覆用1969/1981/1998/2018/2022的歷史案例類比，預期淺回檔（6月）後夏季反彈，再於8-9月出現較深回檔（10-20%），並以此推演對 Bitcoin 見底時點的連動影響。(`DInEqYCj04A`, `Wef7vP6ffBM`, `qrlOI5XlKR0`)。
- **鮑爾遭刑事調查事件的宏觀解讀**：將川普政府對聯準會主席 Powell 的刑事調查框架化為「聯準會獨立性遭跨越的紅線」，並連結到殖利率曲線去反轉後歷史上必然衰退的觀察，強調不確定性升高但避免對時點下determinstic賭注。(`qzWWMQaI6Vk`)。
- **通膨數據與 Bitcoin 中期年季節性吻合**：CPI 降溫後 BTC 反彈，並將此走勢與 2018 年中期年 6-7 月路徑（低點-反彈-回檔-8月再度轉弱）逐月比對，強調不需要敘事也能預測到這個路徑。(`rWfLRMiyQVY`)。

## 5. 矛盾 / 立場演變 (contradictions & evolution)

- **黃金交叉後的操作**：2023年他預期黃金交叉後會有回調（依循2019模式）結果錯了；2024年他因此改為不預設回調、選擇不淡出行情而站對邊；他自己明確承認並反思這個轉變（`V3AHyJn1c9k`）。
- **ETH/BTC 判斷 vs ETHUSD 判斷的落差**：他多次強調自己「ETH/BTC 判斷一直是對的（alts 遲早回吐給 BTC）」，但坦承「ETHUSD 這條路徑我判斷錯了很多次」，尤其低估了 ETHUSD 本輪能衝到接近5000的力度（`vuwmJsNsONk`）。這是他反覆自我揭露的核心矛盾點，顯示他更信任比率分析、對絕對美元價格的短期路徑判斷相對較弱。
- **熊市深度預期反覆調整**：一方面基於「報酬遞減／連續熊市跌幅遞減」（94%→87%→84%→77%）外推下一輪熊市約70%跌幅；另一方面又因本輪「無歐福里亞頂」而屢次調低預期至僅約50%跌幅（`3dSPMPi0XjI`），兩種估計並存、依影片而異，他自己也承認「either everyone's right or everyone's wrong」。
- **Alt Season/ETH 見底時點屢次延後**：多支影片中反覆給出「這次真的快到了」的時間預測（如「by late August」、「by November」、「this summer」、「by early December」），但實際延後多次，他本人也在片中自嘲「I've done my best... you can't say I didn't try」(`lu5uyrIeu98`)，屬於他公開承認的長期未兌現預測模式。
- **對「四年週期是否仍然完好」的立場鬆動**：早期堅持「Q4 post-halving year 必然見頂」的高度確定性語氣，但在多支「Bulls vs Bears」類影片中（`3dSPMPi0XjI`, `9g1QsTVizyQ`）改為機率化語言（如「60-70% chance the top is already in」），並開放討論「兩派都可能同時是對的」的調和情境，顯示語氣從早期較剛性逐漸轉為更強調機率分佈與情境並存。

## 6. 背景/自我定位 (bio & positioning)

- **頻道起源**：2019年夏天創立YouTube頻道「Into The Cryptoverse」，多次提及當時的宏觀環境（QT尾聲、非歐福里亞式頂部）與現在相似，並以此強化自己「活過那個環境、有第一手經驗」的可信度。「I started my YouTube channel back in in the summer of 2019... it's actually kind of similar market conditions to when I started my YouTube channel」(`2DUCJDmTOks`, `3dSPMPi0XjI`)。
- **商業模式**：Into The Cryptoverse (ITC) Premium 訂閱制平台（intothecryptoverse.com），提供更多圖表存取、每週額外影片、Telegram貼文；另設個人品牌網站 benjaminc.com/benjaminc owen.com 提供「direct access」付費諮詢、免費季度總體/加密風險備忘錄報告（crypto macro risk memo）、以及會議合作邀約入口。多次在片尾導流訂閱折扣碼（ITC50）。
- **會議曝光**：受邀在 Bitcoin Amsterdam、Bitcoin Las Vegas 等會議演講，並自辦「Investing Through the Cycles (ITC) Conference」（首屆於邁阿密，11月20-22日）。
- **自我定位為「量化、去偏見的分析者」**：多次強調自己「不是要給投資建議」，個人股票配置僅是低費率指數基金定期定額（DCA），與他頻道上對加密貨幣週期的深入量化分析明確切割，藉此強調客觀性優先於自身部位偏誤。「my investment strategy for stocks is actually relatively boring, right? I just... DCA low expense ratio index funds」(`itxqiPH2vIY`, `Wef7vP6ffBM`)。
- **與其他分析流派的關係**：明確與「supercycle」論者、「alt season」KOL、被項目方付費的網紅劃清界線，強調自己「不靠敘事、只靠圖表與數據」；也與純技術分析/型態學分析者不同，他的核心武器是自建的迴歸模型、風險指標與跨資產類比，而非古典 K 線型態或 ICT/SMC 術語（本語料庫全程未出現 order block、FVG 等詞彙，印證他是「數據驅動宏觀週期」路線而非 SMC/ICT 路線）。
- **世代/人格定位**：自稱「millennial」「90s boy」，強調長期（跨十年）投資視角，多次以「we all pay tuition into the cryptoverse」等語言把虧損正常化為學習過程，塑造一種冷靜、學術、略帶反炒作說教氣質的公眾形象。
