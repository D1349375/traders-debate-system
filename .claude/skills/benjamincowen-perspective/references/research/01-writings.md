# Benjamin Cowen 核心框架與心智模型（合併自 8 批）

> 來源：`_raw_batch_01.md` ~ `_raw_batch_08.md`（共約 386 支逐字稿）。每條標註首次/主要出現的批次範圍（B01-B08），僅去除逐字重複的引用，不同措辭、不同影片的證據皆保留。videoID 以反引號標示。

---

## 1. Risk Metric（0–1 風險帶）

自建的核心量化框架：把資產（BTC、ETH、XRP、S&P500、gold、palladium 等）的歷史價格（及部分結合 on-chain／social 數據）正規化成 0（低風險/便宜）到 1（高風險/過熱）的顏色編碼帶，取代「看感覺」判斷貴賤。核心操作原則：低風險買、高風險賣；並統計資產「歷史上在各風險帶停留的天數比例」作為機率化判讀依據，而非直覺看圖。

- 「Now, this is basically blue is zero and red is one. and you want to be buying assets when they're at low risk levels and then selling when they're at high risk levels.」(`-kOOnpo7Bts`, B02)
- 「if you look at the time in the wristbands... you'll notice that it only spends its only spent 35 days in its entire history in that higher wristband」(`-kOOnpo7Bts`, B02)
- 「the current risk for the on-chain... is around 0.5」(`FYBIOWjRGJA`, B03)
- 「Bitcoin risk analysis using machine learning」— 明確自陳此為機器學習/數學模型，六年前就已發布 (`hx_neha7BVQ`, B03)
- 「if you look at the risk level for ethereum... we're basically knocking on that door because you can see the ethereum risk right now is .4」(`6XPb-c_8hHc`, B04)；「Bitcoin's risk right now is like between 0.4 and 0.5」(`xzFJFrqtus0`, B04)
- 「for every 100 days Ethereum is around, only one of those days it's actually in the highest wristband on average」(`kfg7dNU7TJk`, B05)——用歷史天數比例做機率判讀的典型例子
- 「if you look at the risk metric for xrp it's currently its current risk is 871」；「it's only spent 80 Days in the 08 to 0.9 wristban... only spent 35 days in the 0.9 to1 wristban」(`JsBssA7ovCE`, B06)
- 同一套邏輯也套用在黃金：「the $3,000 level was a pretty important level because that corresponded to around the .8 risk level」(`LLOL3Ku4Tpc`, B06)
- 「we took a look at all these and we normalized their prior moves to between zero and one... the goal is to then get an idea of where we are within any market cycle」(`2DUCJDmTOks`, B07)；「historically, some of the best times to buy Bitcoin are when the onchain risk drops to between zero and 0.1」(`2DUCJDmTOks`, B07)
- ETH 專屬風險指標另建 (`bYVD2U-3OlA`, B07)
- Social risk（社群關注度風險，見第10節）亦採同一 0–1 正規化邏輯，B07 描述其改版加入 Coinbase app 排名與 Google Trends (`WwzQ6gjktHs`)

**應用延伸**：動態 DCA／動態分批出場——不試圖精準抄底摸頂，而是依風險等級分級調整買賣力度（如 0.2–0.3、0.3–0.4… 分級加碼；0.6–0.7 起分批賣出 1/10、2/10…；>0.9 大量減碼）。「there is a difference between being right and making money」(`hx_neha7BVQ`, B03)；「sell a portion of it at each wristband, but you sell increasing amounts the higher the risk goes」(`kfg7dNU7TJk`, B05)。

跨 B01–B08 全部批次反覆出現，是他招牌、跨批次最高頻的分析工具之一，也是他和純技術分析/型態學派最大的區別。

---

## 2. 對數迴歸帶／「Going Home」／Power Law／不對稱尾部分位數模型

為 BTC、ETH、加密貨幣總市值畫出一條「monotonically increasing」的對數迴歸線，稱其為「fair value」（公允價值）；價格跌回下緣稱為「went home / going home」，是他判斷「合理估值」與買點的核心工具（統計迴歸而非型態學）。

- 「All I want to know is this cadence that Bitcoin has and how historically when the Bitcoin percentage of supply in profit and loss when it crosses historically the market bottoms within about 1 to four months」(`Di8YR9nX8Q8`, B01)
- 「Ethereum going home. It's hard to know exactly when the process plays out each cycle, but it is a process that does play out each cycle」(`S-ovduNlqu0`, B01)
- 「Ethereum would go to the regression band, go home, and after that rallied to all-time highs.」(`iwurmuYjvOM`, B02)；同一邏輯套用於黃金：「if you look at the extension from the fair value in this first rally, it was about a 100% extension. But in the second rally, it was about almost a 500% extension.」(`ld_kV9AMrSE`, B02)
- 「the fair value logarithmic aggression trend line fit to all prior data」(`tlgl6cgJ-8A`, B03)；「when Ethereum goes home, it's usually a good opportunity to buy」(`dQmZiBgSOms`, B03)
- 「the fair value logarithmic aggression trend line for the entire cryptocurrency asset class is approximately 3.267 trillion, whereas the overall market cap right now is around 3.371 trillion... this still represents a slight overvaluation of about 3%」(`966xZic_g_4`, B04)——「Beauty of Mathematics」系列每月固定更新（B04: `966xZic_g_4`,`JAkNLbhTjFg`,`Vwhte0qmsS0`,`hAFvtCnrJAw`；B06: `4byEiDYDOKQ`,`E6xmZR6HRGw`,`UwH6OKKypDo`,`V3DPOp7SbTE`,`jxDDnGc1emI`,`vWLAcGD3AJc`；B08: `iXSuyuNJBqA`,`rvR8WJJoT_U`,`wUhYv3lGk_I`）
  - 固定收尾梗（近乎逐字重複）：「the asset class will eventually get to approximately 10 trillion plus or minus a few trillion... as we go to sleep at night, we cannot help but wonder what's a few trillion dollars among friends」
- 「I would defer to the regression line, right? So for me, when I think about what is the fair value, I would just say it's around that regression line」(`A1Np-NgKLCQ`, B05)
- 「the fair value logarithmic aggression trend line is at around 3.725 trillion. This represents an undervaluation of approximately 19%」(`4byEiDYDOKQ`, B06)
- 「Ethereum going home is just simply the idea that at some point ETHUSD during the ETH Bitcoin downtrend will break its support and when it does that's when it goes home」(`bYVD2U-3OlA`, B07)——他 2019 年建立此模型並公開持續追蹤紀錄 (`vuwmJsNsONk`, B07)

**蝴蝶調和形態（butterfly harmonic）與費波那契比例**：對 ETH/BTC 套用 X-A-B-C-D 蝴蝶諧波型態搭配 0.382/0.618/0.786/0.886/1.618/2.24 等 Fib 比例，且明確自陳非專家：「I am not an expert at at butterfly harmonics or Elliot waves or anything like that... feel free to point it out」(`YD4rIRCf4qk`, B04)。

**Power law 與新一代「不對稱尾部曲率」分位數模型（含自我批判）**：模型演化路徑為彩虹圖 → 對數迴歸帶 → 上下尾不對稱分位數模型（"asymmetric tail curvature"），強調上尾（euphoria）與下尾（結構支撐）曲率不同、且隨週期收斂；他公開發表數學論文《asymmetric tail curvature in Bitcoin price quantiles》於 benjamincowen.com，並致謝 power law 提出者 Giovanni 及 "The Real Plan C" 等其他模型作者 (`uFn3KUE-VTI`, B08)。

- **自我批判**：明確表示新模型（asymmetric tail curvature）**並未全面優於**舊模型（power law），僅在上尾預測上可能更有用——「展現罕見的『新模型不等於舊模型錯』的謹慎立場」，即他自陳新模型在下尾（跌幅預測）上不比舊的 power law 模型更優 (`uFn3KUE-VTI`, B08)。
- 用該模型估算：若 BTC 跌到歷史同分位數，對照現價約落在 51–58K 區間（對照 2022 熊市／疫情崩盤／2015 三次歷史極端偏離事件）(`uFn3KUE-VTI`, B08)。

跨 B01–B08 全部批次反覆出現，是他和 Rekt Capital 等單純用型態學或減半天數敘事的分析師最大的方法論分野。

---

## 3. Bull/Bear Market Support-Resistance Band（20週SMA＋21週EMA、50週MA、200日/200週MA）

由 20 週 SMA 與 21 週 EMA 構成的帶狀區間：牛市中是「Bull Market Support Band」（最重要的第一道防線），熊市/期中選舉年中同一區間角色反轉為「Bear Market Resistance Band」。金價則有月線版本（20月SMA+21月EMA）。

- 「the way it works is Bitcoin first falls through the 50, consolidates at the 100, and then goes to the 200」(`yLhApa2vv3s`, B01)
- 「we don't really have the luxury of spending a lot of time below it... a single weekly close below the bull market support band, and then it goes right back above it」(`5812UUvIZDw`, B04)
- 「You need two closes, not just one... like when we go above the bull market support band, you then need another weekly close above it for it to really mean anything」(`QhmRWzYykfE`, B04)——需要**兩次收盤**而非單一影線才算真正突破/跌破，跨批反覆強調 (B01, B02, B03, B04, B06, B08)
- 「so long as Bitcoin holds it, you could argue the integrity of the market cycle remains intact」(`QhmRWzYykfE`, B04)——50 週均線視為「牛市結構完整性」標記
- 「Bitcoin has a date with destiny... destiny is the 200 week moving average」(`kSQO_Td8xO4`, B04)——更深層的「命運之約」框架：50週→100週→200週均線依序被跌破
- 「in mid-term years Bitcoin tends to find resistance at this band... it's no longer the bull market support band」(`1E2cJu2ZjEs`, B06)；「until proven otherwise, the bull market support band is the bare market resistance band」(`BhI9mS770yA`, B06)；金價月線版本 (`sjt1LV2iDog`, B06)
- 「treating the bull market support band not as a support band but as a resistance band」(`U9MFiXzhWT8`, B08)；需要**兩根週K**收在其上才算突破確認 (`RFNt0rCbmhA`, `9Qg02JYoXB0`, B08)

**50週均線 = 牛市結構完整性、週期終結判準**：連續兩根週線收在 50 週均線之下＝週期結束的關鍵訊號（唯一例外：2021 年，因該年不是 midterm year）(`QhmRWzYykfE`, `Sbw6X6aRNww`, B04)。

**移動平均序列崩潰模型**（50→100→200週/日均線依序跌破，為熊市進程的量化路徑圖，非型態辨識）：
- 「below the 50 takes you to the 100 which eventually you break and then go to the 200...same thing 50 to the 100 to the 200」(`7Zans8ehwpg`, B05)
- 「every time Bitcoin crossed below the 50-week moving average, it was always confirmation that the bull market was over」(`6RBevGGz1Pw`, B06)

跨 B01–B08 全部批次反覆出現，幾乎每月固定製作同名更新影片，是他最高頻的固定儀式性技術分析。

---

## 4. Bitcoin Dominance 與「Altcoins are Oscillators at Best」／Satoshi 本位計價

全語料庫中出現頻率最高的核心命題：山寨幣對 BTC 的估值長期而言只是在一個區間內震盪（悲觀下緣≈0.25，樂觀上緣≈與 BTC 等市值/parity），不具備長期跑贏 BTC 的結構性理由；「everything eventually bleeds back to the king」。

- 「Bitcoin dominance is the key to unlocking the secrets of the cryptoverse」(`8nBbg72z-PI`, `QMU14i4PIYk`, B01；`xNHyUX0_Zz0`, B08)
- 「altcoins are oscillators at best against Bitcoin」(`AIYS-_-BCj0`, `Vet2DnHvA7w`, B01)；「Altcoins in my opinion are oscillators at best against Bitcoin. And many of them just bleed to Bitcoin」(`ZVJ1LK_O6b8`, B04)；「there does exist a world where everything else could fail, but Bitcoin doesn't」(`ZVJ1LK_O6b8`, B04)
- 「viewing altcoins as oscillators at best is correct... they basically just range between 0.25 and one」(`nuhiHnPSvls`, B05)；「99.99% of all coins bleed to Bitcoin」(`M5d5fbiSfhc`, B05)
- 「every video I do is a Bitcoin dominance video. I just change the titles of them to make people think that I'm talking about something else」(`7Zans8ehwpg`, B05)——自陳幾乎每支影片本質都是 dominance 影片
- 「altcoins to be oscillators at best」(`4Wldu8lDIOo`, B07)；「the collective altcoin market would collectively drop to 25% of Bitcoin's market cap or 0.25」(`EEoBA2GMswo`, B07)
- 「If you value your portfolio in Satoshi's... Bitcoin dominance going up is not a bad thing.」(`Caw15TVblw4`, B08)；「everything in crypto asymptotically goes to zero against Bitcoin over a long enough period of time」(B08)
- 「Don't marry an altcoin. It will take more than half in the divorce.」(`Caw15TVblw4`, B08)

**Satoshi 本位計價（機會成本思維）**：主張投資組合應以 Satoshi（BTC 計價）而非美元計價，因為「一塊錢丟進 alt 就是一塊錢沒丟進 BTC」。
- 「the way to be successful in crypto is to value your portfolio in Satoshi's」(`QMU14i4PIYk`, B01)；「Every dollar in Ethereum is not a dollar in Bitcoin or into something else」(`S-ovduNlqu0`, B01)
- 「the Satoshi valuation of your crypto portfolio is a lot more important than the USD valuation」(`3gObVL_2eL8`, B06)
- 「if you train your mind to think in terms of Satoshi's instead of US Dollars then you'll likely be a lot more successful」(`f2EcDC5H71c`, B05)

**排除穩定幣的 dominance 計算與假性走弱辨識**：他指出 BTC dominance（含穩定幣）走平常是因 USDT+USDC dominance 上升，而非山寨幣真正走強；剔除穩定幣後 BTC dominance 其實仍創高。「there's a major issue with the way that this Bitcoin dominance metric is... it includes stablecoins」(`VdCMIWRHkTs`, B04)；同一拆解見 (`3PCBcXqTx2g`, B06)。

**9月季節性反轉規律**：「every single time... Bitcoin dominance has reversed course in the month of September」(`1cKJWyUQKR0`, B04；同框架見 `fkXRo-28qv0`,`nmdSKv5TqYI`, B04)。

**費波那契階梯式上升模型**：dominance 依序在 0.382/0.5/0.618/0.786 費波那契關卡遇阻回檔再突破，目標 60%→66%→（討論中）82%（含穩定幣主導率合計）。60% 目標最初部分源於「confirmation bias」（湊巧對應上輪 0.618 回撤位），事後才追加更嚴謹理由 (`8nBbg72z-PI`, B01)；精準命中 60%、66.9% 等關卡 (`-ULNlneh-SA`,`AXcB5Nzym7U`,`7R0ZPddqcTI`,`f2EcDC5H71c`, B05；`sNzpCZDPVjc`,`nrjQUkOmgbg`, B03；`muNTKBPSgsA`,`r3b2gWvHEhU`, B02；`Caw15TVblw4`,`51eFi9k02as`,`xNHyUX0_Zz0`,`q6WNUuy950U`, B08)。

跨 B01–B08 全部批次反覆出現，是他和「alt season」敘事對立的核心立場，也是全語料庫最高頻的心智模型。

---

## 5. 貨幣政策決定論（QT/QE 狀態機、Fed funds vs 2Y 殖利率、Neutral Rate / R-star）

一切風險資產／alt 幣表現的根本解釋變數是聯準會貨幣政策，而非敘事或炒作。核心 if-then：QT（量化緊縮）期間高風險資產（alt）向低風險資產（BTC）撤退，只有 QE 開始才會逆轉。

- 「when liquidity is very tight...markets...are characterized by a flight to quality within the asset class」(`rDYzbxeMWdY`, B01)；「Bitcoin dominance topped when QT ended and QE began」(`QMU14i4PIYk`, `sQPJCZuI3Nc`, B01)
- 「until quantitative tightening is over there's always a chance dominance goes higher... that should be lesson number one」(`muNTKBPSgsA`, B02)
- 「2019 is the only time in history where Bitcoin topped on apathy rather than euphoria... there was also no rotation into altcoins」(`pxFxcr11dMI`, B02)
- 「the 2-year yield tells the Fed what to do... not the other way around」(`chjQo996XvM`, `kZGHzEGRyAM`, B03)
- 「until the Fed funds rate gets a lot lower, you're still likely going to eventually see those altcoins roll over against Bitcoin」(`nmdSKv5TqYI`,`px1Inquiceg`, B04)——聯邦基金利率 > 2年期公債殖利率（他用以近似「中性利率 R*」）＝環境仍屬緊縮
- 「if the Fed funds rate is above the neutral rate, the economy slows down... if the Fed funds rate is below the neutral rate, the economy speeds up」(`E66AXmddwL0`, B07)
- 「the market tells the Fed what they need to do. The Fed doesn't tell the market what to do.」(`Caw15TVblw4`, B08)
- **QT 結束時間點的持續落空**：他在多支不同時期的影片中反覆預期 QT「未來幾個月內」結束（2024年中、2025年年中、2025年底等），但每次都被推遲；本人主動承認：「had you told me QT was still going on I would have absolutely believed it. I just don't think a lot of people assumed that quantitative tightening would have ended already especially back in 2021, 2022」(`muNTKBPSgsA`, B02)——詳見決策紀錄檔第4節「落空案例」
- **QT 敘事的工具性使用（自承）**：「quantitative tightening has just been a convenient narrative for me...I don't think you needed to know anything about monetary policy to figure out that altcoins were likely going to bleed against Bitcoin」(`QMU14i4PIYk`, B01)——他承認圖表訊號才是主因，總經敘事是「事後合理化」的工具

**QT 結束後 alt season 未如期出現，因果關係修正為「必要非充分條件」**：他長年宣稱「alt season 需等 QT 結束」，但 QT 於 2025 年 12 月結束後，Bitcoin 頂部已過（apathy top），alt season 仍未出現；事後修正說法為「all-Bitcoin-pairs 到 0.25 是必要非充分條件」，公開承認原先隱含的因果關係不夠精確 (`rt4cLrhLbZQ`, B08)。

跨 B01–B08 全部批次反覆出現，是他解釋「為何本輪沒有 alt season」的方法論主軸。

---

## 6. ITC 景氣循環方程式與 Business Cycle Chart

自建公式：**S&P500 ÷（失業率² × 通膨率YoY × 聯邦基金/利率）÷ M2 貨幣供給**，用以視覺化景氣循環階段、判斷是否進入「晚期商業週期環境 (late business cycle environment)」，其終點歷史上必然是衰退。

- 「S&P 500 divided by the unemployment rate squared... multiply by the inflation rate... multiplying by [interest rates]」(`Kx7F_EL9ocI`, B04；同公式見 `efzBx985xbU`,`oWV5iW3glao`,`rmpIOnNUwII`,`yBJDk4a0e24`, B04；`2ehTz4A5yJQ`,`4rkqfmzKFpU`,`sKK9yzBhTmI`, B03；`bB6oo3oJc0k`, B05；`FiztJuyl7p4`,`boZbiynTEQ0`,`w1dJjaF1g9g`, B06；`JGXGlgF0nMA`,`itxqiPH2vIY`, B07）
- 核心推論鏈：晚期商業週期 → 油價飆升（供給面而非需求面）→ 通膨與失業率同時惡化 →「Fed 被將死 (checkmate)」→ 風險資產（尤其風險曲線末端的迷因幣/山寨幣）率先下跌 → 最終衰退重置整個週期。「risk rolls down the curve rather than up the curve」(`oWV5iW3glao`, B04)
- **西洋棋比喻**：「the Fed can defend one weakness... they cannot defend two. And that's what usually leads to the end of the business cycle」(`JGXGlgF0nMA`,`itxqiPH2vIY`, B07)——聯準會同時面對通膨與失業惡化時的困境
- 「every time this metric basically goes off of this level down here, we eventually return to it... the way in which we eventually get it down there, historically, is a recession」(`FiztJuyl7p4`, B06)
- 拒絕給出精確衰退時間表：「It could be as early as this year. It could take as long as until 2028」(`efzBx985xbU`,`oWV5iW3glao`, B04)

跨 B03–B08 反覆出現，是他總經分析的骨幹公式，橫跨加密貨幣、股市、貴金屬三大資產類別的討論。

---

## 7. 「敘事跟隨價格」認識論 與 反駁「M2 領先 BTC」

明確的認識論立場：市場先動，敘事才被發明來解釋它，因此不該用敘事去預測價格；反過來說，用新聞/媒體解釋漲跌是他認為散戶最大的認知謬誤之一。

- 「I do not believe that price follows narrative. In fact, it's the other way around. Narrative follows price」(`AXcB5Nzym7U`, B05)
- 「narrative follows price... the news cycle is noise」(`4rkqfmzKFpU`,`PdWvxD7-Di8`,`fV6NzO02KH4`, B03)
- 「Bitcoin normally corrects at January in January of post having years... so why do we need to go find a narrative to support that outcome because we already knew that was a likely outcome」(`boZbiynTEQ0`, B06)
- 「price leads the narrative... narrative lags price」(`Caw15TVblw4`, B08)

**反駁「M2 領先 BTC」，主張「Bitcoin 領先流動性」**：他反駁社群普遍流行的「BTC 落後 M2 三到四個月」模型，提出反向假說。
- 首次提出（明確標註為探索性假說，非定論）：「What if Bitcoin is not lagging the global money supply? What if it's not lagging it? What if it's leading it?」(`wWLGTouVRWk`, B02)——「just something to think about」，他明確承認這只是推測
- 後續強化並轉為更確定的立場：「Bitcoin leads liquidity, Bitcoin is a leading indicator for M2, not the other way around」(`rt4cLrhLbZQ`, B08)——並自我評論「一年前這麼說沒人信，現在可能比較可信」，顯示他隨時間強化並公開修正這個原本邊緣的立場（詳見決策紀錄檔第5節「認錯模式」，此為挑戰社群主流模型而非自身模型的案例）

跨 B01–B08 全部批次反覆出現，是他對抗市場共識敘事的招牌立場之一。

---

## 8. 反駁「減半驅動四年週期」——改以貨幣政策/景氣循環解釋

明確反駁「halving causes the 4-year cycle」的通俗說法（含他自己早期也曾隱含使用此敘事），改以「M2/貨幣政策/商業週期」作為更根本的解釋。

- 「I don't think the reason for Bitcoin's cycles, 4-year cycles, is not because of the halving」(`FgxAe_NAh5c`, B04)
- **反證**：舉標普 500 在**沒有減半機制**下也呈現約四年一次的低點作為反證，說明四年週期是更普遍的商業週期現象而非 Bitcoin 特有。「Bitcoin does not have a monopoly on the four-year cycle.」(`rt4cLrhLbZQ`,`sy6AxBbgico`, B08)
- 頂/底發生時間點由總體經濟（通膨-失業率是否「良好行為」）決定，而非單純套用減半模型：右翻轉週期（peak 在 bear market low 前一年，通常伴隨一年熊市）vs 左翻轉週期（因通膨/失業率同時惡化而延後，通常兩年熊市）——見第9節
- 這與坊間（包含他自己早期）「減半驅動論」的樸素敘事有明顯區別；值得注意 Rekt Capital 等分析師常用的減半天數敘事，在 Cowen 這裡被明確降級為次要或非因果關係。與此並存的統計事實描述：頂部固定發生在減半後年份 Q4，熊市通常持續約一年，低點落在期中選舉年 (`s_SJS5EdwP8`,`pkDDBb1EYwg`,`prz4p7r45vU`, B08)——他強調這是**統計規律**而非**減半天數的因果敘事**本身。

跨 B04, B08 主要出現，是他方法論上與純減半敘事派（如 Rekt Capital）的核心分野。

---

## 9. 報酬遞減與 ROI-from-low 疊圖；右翻轉 vs 左翻轉週期

用「從低點起算天數」「從減半起算天數」「從峰值起算天數」三種方式衡量目前處於週期第幾天，並與前兩個週期逐日比對，推論報酬遞減（diminishing returns），而非用型態學或減半敘事。

- 「last cycle, market cycle 4... ended on day 1059. The cycle before that ended on day 1067. Currently, we are on day 1016.」(`k7F7P0uqUuA`, B02)；「if you just measure it from the low, you can see that we are looking more than likely at diminishing returns」(`k7F7P0uqUuA`, B02)
- 「this cycle lasted, it topped on day 1,062... The cycle before this one topped on day 1,059... The cycle before that one topped on day 1,068」(`CJCyxfuo73o`, B06；同手法見 `rKjce1jCxSM`, B07)
- 報酬倍數遞減量化：92x→30x→8x→<2x，並批評每輪都有人聲稱「這次不一樣」。「diminishing returns unfortunately is a thing... it's not a popular theory, but all Bitcoin pairs bleeding was not a popular theory」(`ZeO0sahwPsc`, B05)
- 「the current cycle is actually still outperforming the 2016 to 2017 cycle... when measured from Peak to Peak」(`2j8fbCW4GpU`, B03)

**右翻轉 vs 左翻轉週期 (Right-translated vs. Left-translated cycles)**：
- 「you basically have two types of cycles you have right translated where you get a one-year bear market and then you have left translated where you get a two-year bear market」(`29nSJuyPrP0`, B02)
- 「right translated cycle is where the peak is one year before the bare Market low... left translated Cycles is when the labor market and inflation is not well behaved」(`gdVN_7aktHI`, B03)——整支影片圍繞此模型展開，是他少見的「風險情境樹」思考方式，明確分配 20%/60%/20% 等機率（見決策紀錄檔第2節「機率化情境樹」）

跨 B02, B03, B05, B06, B07 反覆出現，是他量化週期定位而非套用固定型態或敘事的方法論骨幹。

---

## 10. Apathetic Top vs Euphoric Top（社群關注度指標）

用社群關注度（Social Risk / Social Interest 指標：YouTube 訂閱/觀看數、Twitter/X 分析師/交易所/Layer1 追蹤者數、後期加入 Coinbase app 排名與 Google Trends）給價格上色，區分「在狂熱情緒中見頂」（2017、2021，快速崩跌）vs「在冷漠中見頂」（2019、2025-2026，緩慢陰跌，即 time-based capitulation）。

- 「when you top on apathy rather than euphoria, you do not get a rotation into higher risk assets」(`W_YasiLxgJ4`, B01)
- 「The social risk is a way that we use to measure social interest in crypto... made up of five different risk metrics」(`16l2PcW3Z4g`, B03)
- 「we topped on apathy rather than euphoria. If you go look at the social interest of Bitcoin, what you'll see is that it's most similar to 2019」(`WUJwW3mf6to`, B04)；「social risk is about 0.25. This is actually where it was in 2018」(`DHnqpPWJDn0`, B04)——他明確標示這是「這次真的不一樣」的少數承認之一，但強調機制（四年週期）本身沒變，只是狂熱與否不同
- 「in order to get the alt season that people want, you need to see retail return」(`nuhiHnPSvls`, B05)；自嘲式量化散戶稀缺：「there's literally dozens of us left right, 0.06」(`f2EcDC5H71c`, B05)
- 「there's dozens of us left」反覆自嘲用語 (`jQ8xEnReO0M`,`YA-7M-01d84`,`rt4cLrhLbZQ`, B08)，用此指標解釋「為何這輪 topped on apathy not euphoria」，並主張唯有社會利益回升才可能有真正 alt season

**必要條件邏輯**：社會關注度回流（social risk 持續突破並站穩 0.4 之上、打出更高低點）是 alt season 發生的必要條件；本輪循環一直未出現此訊號 (`MeRKLQij0xo`,`nuhiHnPSvls`,`wJTg1wlEpnQ`,`f2EcDC5H71c`,`jus1K0YHE3A`, B05)。

跨 B01, B03, B04, B05, B08 反覆出現，是他解釋本輪週期「與過去不同」但「機制未變」的核心工具。

---

## 11. 跨資產類比覆蓋法（Cross-Asset Analogical / Fractal Overlay）

大量把不同資產、不同年代的走勢圖案「剪貼」互相比對，尋找「同一種市場心理模式」（先前高點被掃、拉回到牛市支撐帶、再度突破），以此類推當前資產下一步；同時反覆公開懷疑類比方法本身的可靠性。

- 1970s S&P、1973/2008 S&P against gold breakdown、1989-1990 衰退、dot-com bubble、2019 ETH bear market、Tesla 股價 vs Ethereum 走勢：「Ethereum would likely follow Tesla's move... the low for Ethereum was 1380... the low for Tesla approximately... 139」(`KWWoGH-KpKY`, B04)
- 自嘲式承認方法的爭議性：「I know a lot of people compare it to that... I don't really think anyone here is willing to accept that it's different」(`-2ZIAvw9Wgc`, B04)
- Bitcoin dominance vs 鈀金 vs 恆生指數 vs 穩定幣主導率的圖形疊圖：「we've seen this pattern... Bitcoin dominance... the HSI... Palladium... and the unfortunate chart is stable coin dominance」(`ZuWWt3U3UBQ`,`rKjce1jCxSM`, B07)
- **保持保留的態度**：明確反覆強調「analogies almost never play out how you think」、「fractals almost never work」，只作為情境推演工具而非預測 (`WFRKEDi6vNg`,`TGCR40obh8I`,`Va4uxOptS4c`, B08)——「使用類比但公開懷疑類比」是他表達風格的核心特徵之一
- 其他跨資產類比：QQQ 於 BTC ETF 上市後 54 週見頂、S&P/M2 對照 1996-2000 dot-com bubble、S&P/gold 對照 1973、2008 (B08)

跨 B04, B07, B08 反覆出現，是他非常獨特的方法論招牌，但也是他自我懷疑最頻繁的工具之一。

---

## 12. 比率分析（Ratio Analysis：ETH/BTC、S&P/M2、S&P/gold 等）

透過資產間比率而非美元價格判斷資金流向與相對強弱，貫穿加密貨幣與宏觀資產（黃金/白銀/股市），是他最重要的方法論支柱之一。

- 「alt season doesn't occur historically until all Bitcoin pairs go to 0.25」(`sNzpCZDPVjc`,`lIMT_CwWAc0`,`nrjQUkOmgbg`, B03)
- 「when you get these levels going back all the way to the 1980s, that is when the ratio of gold against silver starts to bounce」(`ZTRxoRs3VM8`, B03)——金/銀比模型：金銀比觸及歷史低點區（1987、1998、2006同樣位階）→ 之後銀相對金會走弱數十個月（30–107個月不等）
- 「always the Bitcoin valuation over the USD valuation」(`AHco65OpeZo`, B04)——ETH/BTC、SOL/BTC、TOTAL3/BTC、TOTAL3/gold、TOTAL3/silver、S&P/gold、Bitcoin/gold 等比率鏈分析
- S&P500/黃金比值月收盤跌破 1.4 → 大幅提高衰退機率：「if this starts closing below 1.4... I think you have to start seriously considering a recession at that point」(`k7F7P0uqUuA`, B02)
- 若 S&P/gold breakdown（突破前高，即金相對股市走強）→ 歷史上（1973、2008）隨後風險資產修正幅度大於黃金本身，因此金銀回檔不代表資金會輪動回加密貨幣，反而常是加密貨幣跌更深的前兆 (`-2ZIAvw9Wgc`,`WeRACbnZH0E`, B04)
- 「one of the ways to defeat inflation... is lower asset prices」——S&P/M2、S&P/gold、Bitcoin/gold、ETH/BTC、all-Bitcoin-pairs 等比率突破/跌破歷史關鍵位（如1998、1973、2008）(`3p8qHHgcIqc`,`WFRKEDi6vNg`,`hMkHnOuVLIw`, B08)

跨 B01–B08 全部批次反覆出現，是他宏觀分析（股市/黃金/比特幣三大類資產）的核心方法論骨幹。

---

## 13. 鏈上估值三線：Realized Price / Balance Price / Terminal Price

熊市底部歷史規律：先跌破 realized price，再跌破 balance price 才真正見底；本輪（因是冷漠頂）未觸及 terminal price。

- 「every after every euphoric top... Bitcoin first goes below the realized price and then later it goes below the balance price. And when Bitcoin goes below the balance price, that is normally when Bitcoin bottoms」(`WUJwW3mf6to`, B04；同框架見 `sigSZCnSa6M`,`yBJDk4a0e24`, B04)
- 亦用「supply in profit / supply in loss」交叉驗證是否已觸底：兩線收斂交叉歷史上多次對應週期底部（2014、2018、2022），但此指標「更適合抓底部、不適合抓頂部」（因牛市可在高位停留數年）(`XiXsP4Ch5no`,`joW6YbFRDI0`, B07)

跨 B03, B04, B07 出現，是他判斷熊市底部是否已到位的鏈上估值錨點。

---

## 14. 季節性統計基準（YTD ROI ±1σ、弱勢窗口）

用同期歷史年份的 year-to-date ROI、月報酬率平均值±1個標準差來設定「最可能情境」，而非用型態辨識；他明確排斥 head-and-shoulders 等古典 TA。

- 「I don't believe in a lot of forms of TA, like heads and shoulders, knees and toes, right? That stuff doesn't really mean a whole lot to me. But, momentum means a lot」(`vxnpP3EOl-8`, B01)
- 「if you look at the year-to-date ROI...and overlay the historical average...we are generally tracking prior midterm years」(`Y2b3oTZg2AQ`, B01)
- 「windows of weakness are early February, early April. Then June. If not June, the next one's October」(`6RBevGGz1Pw`, B06)；「Bitcoin is green in both July and August, right?... September was red」(`EnnKjDHiqyI`,`G5IEOvGueGU`,`il089bNt-4g`, B06)
- 季節性只有約70%命中率，不應被視為必然發生的規則：「seasonality only works about 70% of the time」(`UB3O2T0HElw`,`e211pOyTVyI`,`hMStACy4ou4`, B03)
- 「With technical analysis, a lot of it is handwavy, right? I don't believe in most technical analysis to be completely honest. But one of the things that I think does make sense to believe in is momentum.」(`6BfEEwrHJH4`, B06)——明確將自己的方法論與純粹型態學/ICT/SMC式技術分析區隔開

**期中選舉年 (midterm year) 策略**：上半年忽略/淡出 BTC，下半年開始定期定額買進；歷史上低點多落在 6 月與 Q4。「the strategy for midterm years for Bitcoin... is to DCA Bitcoin throughout the second half of the midterm year」(`8TmOvGK235I`, B02)。

跨 B01, B02, B03, B06 反覆出現，是他判斷「短期最可能路徑」的統計錨點，明確與古典型態學/ICT/SMC技術分析區隔。

---

## 15. 現代投資組合理論（Sharpe / Sortino Ratio / 效率前緣）

用歷史報酬與波動度，透過 Sharpe ratio、Sortino ratio、efficient frontier、Monte Carlo/quadratic programming 計算 BTC/ETH/XRP 的最佳配置權重，每約 6 個月更新一次；主張「drop the bias at the door. No one cares about it. Stick to the data.」

- 「the sharp ratio is maximized at.703 volatility which would give you 81% Bitcoin and 19% Ethereum」(`fFaDfy1scWU`, B02)；「the sortino ratio does not punish positive volatility」(`fFaDfy1scWU`, B02)
- 「if you run a Monte Carlo simulation of Bitcoin and eth portfolios and try to figure out what portfolio percentage maximizes your Sharpe ratio or your Sortino ratio... 83% Bitcoin and 17% eth」(`qYd9edAe0iE`, B04)
- 資產配置延伸：面對潛在左翻轉週期風險時，依現代投資組合理論保留約 1/3 現金，以便在下跌時加碼、同時降低曝險 (`9Qg02JYoXB0`, B08)

跨 B02, B04, B08 出現，是他將「不憑感覺、只憑數據」原則延伸到資產配置決策的具體工具。

---

## 補充：與本框架密切相關但未獨立成節的次要模型

- **死亡交叉反彈 / 黃金交叉回調模式**：Golden cross 後常見「golden cross dump」（10-15%拉回）；Death cross 後常見「death cross rally」（局部低點）——不要在死亡交叉當天恐慌賣出，不要在黃金交叉當天追高。跨 B01–B08 反覆出現（如 `Yc4epD9pZNI`,`QMU14i4PIYk`, B01；`e211pOyTVyI`,`nrjQUkOmgbg`,`iD_vlVaPHLU`, B03；`x4ptTIHciXI`,`YwNA4wHZLPg`,`M5d5fbiSfhc`, B05；`DeFbx6cCHro`, B06；`V3AHyJn1c9k`,`otl3Slpfwsc`, B07）。此模式本身在 2023 年一度失準，詳見決策紀錄檔。
- **熊市三階段心理模型**：階段一「只有少數人相信」、階段二「約一半人相信」、階段三「多數人相信」；「once everyone believes in the bear market, that's usually when the bear market ends」(`gkDqbvMnMHI`, B07)（推斷：即興構建框架，非長期沿用模型）。
- **「賣強不賣弱」原則**：反對「賣贏家買輸家」的行為偏誤，正確做法是讓贏家繼續跑、逐步止盈。「one of the biggest mistakes that traders often make is they sell their winners to go buy the losers」(`FUig3U0PelQ`, B04)。
