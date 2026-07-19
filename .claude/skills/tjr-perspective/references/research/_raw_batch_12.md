# TJR Raw Research Batch 12
來源：_batch_manifest_12.txt（共 49 個逐字稿，實際處理 49/49）

備註：manifest 最後一行為空行（共 49 條實際路徑，非題目所述約 48 條）。其中 `ytuJHNnNozI_48 Hours In Los Angeles With Sara Saffari` 為單行超長生活 vlog 逐字稿（約 28k tokens），超出單次讀取上限，改以關鍵字抽樣（grep 搜尋 trading/liquidity/market open 等詞）確認：內容幾乎全為生活/約會/名人相關 vlog，僅零星提及「market open」「day trading」「trading」等詞但無新增可用實質交易內容，故此檔不計入下方引用來源，僅記錄於此作為完整性說明。

## 1. 心智模型候選 (candidate mental models)

- **機率優先於預測 (probability over prediction)**：交易的目的不是賺錢，而是「以高機率預測價格走向」，賺錢只是副產品。引用：「What is our goal of trading? To have a high probability of predicting where price wants to go on a daily basis. That's all trading is. It's not about making money」(`-zyDnjozaMM`, 2025-11-26)。跨多檔重複（`CPPREA-6ubY` 2025-04-14 同樣強調「strategy, risk management, psychology」三技能框架）。

- **籃球類比：技能習得框架**：反覆用職業籃球員練基本功類比交易員練習核心confluence，強調天賦+苦練缺一不可。引用：「I love comparing trading to basketball because it's super similar... you just have to be insanely good at the fundamentals」(`CPPREA-6ubY`, 2025-04-14)；(`BOx7Lk8Xs3o`, 2024-07-12) 用運球過人比喻confluence疊加判斷。(推斷：這是他最穩定的教學隱喻之一，貫穿至少3年)。

- **「你很爛，不是策略爛」(You suck, your strategy doesn't)**：策略只是入場的一步，讓交易員变盈利的是紀律與風控，而非策略本身。引用：「You suck. Your strategy doesn't... it's not the strategy that is going to help you turn profitable」(`-zyDnjozaMM`, 2025-11-26)。

- **Draws on Liquidity / 五件套疊加系統**：liquidity sweep → break of structure → (fair value gap / order block / breaker block / equilibrium 三選一或多個) 疊加確認才進場，是他自稱唯一使用的完整框架。引用：「liquidity sweep break of structure fair value Gap equilibrium and Order blocks that is it... there's no extra Secret Sauce」(`AUUZ9Vk6p5E`, 2022-12-12)。此模型在幾乎所有教學/交易錄影檔（`YMqC2ZvwCJg`、`Qk-mHUlSJGU`、`ftWUenk3xrk`、`BOx7Lk8Xs3o`）反覆出現，屬最核心心智模型。

- **低阻力流動性 vs 高阻力流動性 (low/high resistance liquidity)**：把鄰近的多個session高低點視為一組，判斷是強力吸引目標還是已被掃過的弱目標。引用：「Group them all together. What is it? Low, resistance, liquidity」(`FQLzhkiUVlw`, 2025-05-09)；(`YUSmh2LtHRo`, 2024-09-12)同樣使用。

- **溢價/折價 + equilibrium 銀行類比**：用超市打折比喻機構在折價區買、溢價區賣，equilibrium 是延續性confluence而非反轉confluence。引用：「it measures premium in discount... because of this it's a continuation Confluence」(`fl9ofZ4Rtb0`, 2024-03-07)；(`Qk-mHUlSJGU`) 進一步把此概念整合進「更新版」日內偏向判斷法。

- **Seek and Destroy（獵殺回踩)**：價格掃出流動性後會回踩到近乎盈虧平衡點洗出早盤交易者，再繼續原方向。引用：「remember that Seek and Destroy method... stops the ideal am session trade out at break even or a little bit lower and then continues」(`-7-oZkdB4Vs`, 2024-11-06；`YUSmh2LtHRo`, 2024-09-12)。

- **反技術指標/反花俏工具立場**：明確唾棄 Fibonacci circle/wedge/pitchfan/ABCD/cipher/head-and-shoulders 等工具，稱其為「無意義的視覺垃圾」，但同時大量使用 Fibonacci retracement 與 Gann box 作equilibrium/retracement工具（矛盾見第5節）。引用：「If you're putting one of these on your charts, just give up, bro... genuinely give up」(`eEg0_zc8Hxg`, 2026-07-06)。

- **人設即行銷引擎（延續既有心智模型，本批新增證據）**：極度強調「全透明」——同時公開巨額獲利與巨額虧損影片作為信任建立手段（`dIbWfM1145Q` -$76,340、`h-lq97cSJ00` -$45,679、`MKeZTAR-VK4` -$65,000/-$106,000、`FQLzhkiUVlw` +$46,180）。引用：「Documented live in front of your f-ing faces every single f-ing day」(`FQLzhkiUVlw`, 2025-05-09)。

- **「少即是多」(less is more) 交易哲學**：最頂尖交易員一個月只交易幾次，而非天天交易；過度交易=不成熟訊號。引用：「The best traders in the world are taking one to two trades per month... So why the [ ] are you taking a trade every single day」(`-zyDnjozaMM`, 2025-11-26)；(`W7izYiBHWW4`, 2024-03-05) 同樣強調「less is more」。

## 2. 決策啟發式 (decision heuristics)

- 若4小時與1小時方向一致 → 依此方向找進場；若高時間框架互相矛盾 → 當日不強行進場 (`-VR7Y2Tr_2M`, 2023-06-05)。
- 只在流動性掃蕩 + break of structure 之後才尋找confluence進場；fair value gap用於「retracement」而非「reversal」，liquidity sweep才會造成reversal，break of structure確認方向轉變 (`AUUZ9Vk6p5E`, 2022-12-12；`xX5LTSJ5wwM`)。
- 一律避開高影響力新聞日（CPI/FOMC/NFP）交易，除非有基本面研判的極少數例外（如 2025-10 FOMC「buy the rumor sell the news」逆勢交易，事前於社群媒體公開預測）(`MKeZTAR-VK4`, 2026-06-19；`syUOu_-MFNA`)。
- 進場後設定多個逐步停利點於高confluence區（draws on liquidity、order block、fair value gap），達第一停利後移動停損至盈虧平衡，「絕不把已賺到的錢還給市場」(`-Myd0b6xCh4`類似格式檔`8JyK4AC29Mg`, 2023-06-05；`ftWUenk3xrk`, 2024-05-16)。
- 若連續虧損：不改變核心策略，只微調confluence組合（例如原本只用sweep+BOS進場，改為要求額外order block或FVG確認），並降低交易頻率 (`PyCPHiO2nj0`, Boot Camp Day 41)。
- 兩指數同時設定時偏好NASDAQ而非S&P 500，理由是量能/波動度更適合其風格（多次重申）(`-7-oZkdB4Vs`；`YUSmh2LtHRo`)。
- 不追已經完成的行情（"chasing"），寧可等回撤與正式確認 (`BOx7Lk8Xs3o`)。
- 一天只用「9:50 macro之後」的時段作為主要進場窗口，開盤前1.5小時為最佳交易時段，之後傾向不交易 (`W7izYiBHWW4`, 2024-03-05；`FQLzhkiUVlw`)。
- 正常風險為0.5%~1%，但對「高信心」設置會放大部位/情緒化加碼（見矛盾章節），這與其平時教的紀律原則直接衝突。

## 3. 表達DNA (expression DNA)

- 固定收尾語：「I love and appreciate you guys. I'll catch you guys in the next one. Peace out.」幾乎每支影片皆出現，橫跨2022-2026。
- 高頻自我指令口頭禪：「lock in」（多次連續重複自我催眠式喊話，如"lock in lock in lock in lock in"）。
- 自創術語/暱稱：NASDAQ暱稱為「gas pack」或「ass crack (Ascra)」；S&P 500暱稱「es」；社群稱呼「jits」/「Discord jits」；狗狗「Boogie」是固定登場角色，常被拿來當作交易運氣/幽默橋段。
- 音樂化口號段子：「we bring the boom」（自創饒舌式重複段，用於PPI無波動日的自娛橋段）(`YUSmh2LtHRo`, 2024-09-12)。
- 分析語氣 vs 人生說教語氣兩套截然不同的語域：圖表分析時語速快、術語密集、簡潔；勵志/心理段落則轉為冗長佈道式、大量反問句與重複強調（例如`-zyDnjozaMM`全片幾乎都是說教格式）。
- 用「boom」作為確認confluence的口頭標點：「boom, liquidity sweep, boom, break of structure」。
- 自嘲式幽默處理批評：「everybody loves saying tjr your risk rewards suck dick well guess what I'll make you nut quick」(`YUSmh2LtHRo`, 2024-09-12)。
- 宗教/信仰語彙偶爾出現：「put your faith in him... God is on your side」(`JTLwPgf1NyU`, 2024-04-20)。
- 推薦書目固定引用 Mark Douglas《Trading in the Zone》作為心理建設權威來源 (`AUUZ9Vk6p5E`)。
- 禁忌詞/嘲諷對象：技術指標買賣訊號("indicators that tell you when to buy and when to sell")、花俏Fibonacci工具、"course scammers"皆被貶為「詐騙/垃圾」。
- 確定性語氣但常自我對沖：先斷言「我知道市場要去哪」，隨後又補「for real」「not gonna cap」「no cap」等口頭確信/緩衝語混用。

## 4. 決策記錄與案例 (decisions & track record)

- 2024-11-06：川普當選當天判斷「不做空」全長倉，S&P/NASDAQ流動性掃蕩後做多，獲利約$9,928 (`-7-oZkdB4Vs`)。
- 2024-10-10：前一日NASDAQ單日獲利約$115,000（CPI日不交易，隔日補發trade recap）(`7NGsl8TWalQ`)。
- 2023-10：單月獲利+$250,000，已提領$64,956；同年1月「整月unbeaten，連勝21筆交易」(`NA2equ--jc4`)。
- 2025-05-09：單日先虧$59,000（三筆交易），第四筆情緒化加碼多單後反轉獲利，最終單日+$46,180，當週+$91,000 (`FQLzhkiUVlw`)。
- 2025-03-11：因手動計算lot size失誤（NASDAQ與ES部位大小搞混），單日虧損$45,679，稱為「my worst trading day of 2025」(`h-lq97cSJ00`)。
- 2026-03-17（`dIbWfM1145Q`檔實際上傳日期為此，記錄的是Eval帳戶交易對話錄影）：討論連兩日過早（10:30後）強行進場導致虧損，反思「10:30後如果沒有setup就該收手」。
- 2025-10-29：FOMC「buy rumor sell news」單日獲利約$400,000-$427,000，稱為近6-7天總計約$550,000獲利的起點；同影片承認同月稍早三連敗使帳戶周虧損約$100,000、月虧損約$100,000 (`MKeZTAR-VK4`)。
- 2026-06-19：法國飛邁阿密頭等艙（$41,000機票）途中交易虧損$65,000-$66,000，自嘲「lost $106,000 in one day」（含機票）(`MKeZTAR-VK4`同批次上傳，"I spent $100,000 on a random Thursday"實為此檔標題內容)。
- 早期案例（`AUUZ9Vk6p5E`, 2022-12-12）：曾把$10,000炒到$112,000（過度槓桿/過度交易），隔天因未收斂風控在數小時內全部回吐至零，作為反面教材反覆引用。
- 2025-11-12：贈送二手Dodge Challenger Hellcat及$5,000現金給陌生黑人夫妻（聲稱資金來源為賭博贏得$10,000之一部分），並自曝同月交易虧損$185,000 (`ggJVKEBIWvI`)。

## 5. 矛盾 / 立場演變 (contradictions & evolution)

- **紀律 vs 情緒化交易的自我矛盾**：反覆教導「stop being an emotional trader」，但在 `FQLzhkiUVlw`（2025-05-09）多次公開承認「Call me an emotional trader... I don't give a [ ] when I know where market wants to go, I put money on it」，並在虧損$59,000後加碼賭氣式做多，事後仍將此包裝為「knowing where market wants to go」的自信展示而非違反紀律。
- **反技術指標 vs 實際使用類技術工具**：在TradingView教學影片(`eEg0_zc8Hxg`, 2026-07-06)嚴厲抨擊Fibonacci circle/wedge/ABCD/cipher/pitchfork等「垃圾」，卻同時承認自己核心使用Fibonacci retracement與Gann box（equilibrium工具），存在定義上的雙重標準：「這些是輔助我的，不是花俏視覺垃圾」。
- **策略演變但否認改變**：2022年教學(`AUUZ9Vk6p5E`)聲稱其五件套（sweep/BOS/FVG/OB/equilibrium）「this is all you need... there's no extra Secret Sauce」；但2024年中(`BOx7Lk8Xs3o`, `CPPREA-6ubY`)引入London/Asia/NY session高低點的「session fakeout」全新框架，並明確說「this isn't necessarily how I trade」「my current strategy is a little bit different」。同時堅持辯護：「strategies don't expire... just because I made a YouTube video on it doesn't mean I'm going to use it every day」(`ftWUenk3xrk`, 2024-05-16)。
- **每日偏向判斷法「更新」**：2026年新影片(`Qk-mHUlSJGU`)明確表示這是「updated」版本，加入premium/discount，並隱含修正舊版策略邏輯（舊版偏向僅看4H/1H順勢找單邊，現在也接受逆勢方向的premium/discount交易）——本人未直接承認舊方法有誤，僅稱「it still [ ] works if you use it and it works for you」。
- **行銷急迫感重複使用**：「這是最後一次開設Mastermind」在2024-10 (`-7-oZkdB4Vs`)與2024-11-06附近的另一段落中皆重複聲稱，形成典型的稀缺性行銷話術重複套用而非真的最後一次。
- **「我不需要你的錢」vs 龐大付費漏斗**：2022年強調「I don't need your guys's money... I'm not here to scam you」(`AUUZ9Vk6p5E`)，但同期已在建構Discord付費頻道、5天Zoom課程；後續數年逐步擴張為 Mastermind 1.0-5.0、Trading Blueprint mentorship、Trade Wars競賽等多層付費產品線。

## 6. 時間線 / 背景事實 (timeline & bio)

- 14-16歲開始接觸外匯/交易（自述時間點在不同影片略有出入，`JTLwPgf1NyU`, 2024-04-20 稱「14和15或16歲」）。
- 花費2年才轉為穩定獲利；截至2025年底累積約6年交易資歷 (`-zyDnjozaMM`, 2025-11-26)。
- 曾就讀猶他大學（University of Utah），兩年後輟學；輟學前曾在猶他州經歷憂鬱/低潮期，稱搬到波多黎各後心理狀態與交易績效大幅改善（"went from doing like a th000 5,000 sometimes $10,000 days to moving out here...upwards of 90k days"）(`JTLwPgf1NyU`)。
- 定居波多黎各，理由包含日照/氣候對心理健康的影響、稅務考量（未直接明說但反覆強調生活品質提升）。
- 事業版圖：擁有prop firm（自述"I own a prop firm"）、加密貨幣市場研究公司、服飾品牌 Killtech（Capsule 1/2/3陸續發售）、"1800 Bankroll"（自創鏈飾/品牌名稱，非單純潮牌）。
- 固定登場人物：愛犬Boogie（自2022年起持續出現）、好友兼經理人Carson。
- 2025年11月：以賭博（非交易）獲利購入二手Dodge Challenger Hellcat並贈與陌生人，同時進行交易（FOMC）獲利$400k+單日紀錄，同月稱交易虧損$185,000（提及於贈車影片中，屬於自曝矛盾業績的例子）。
- 2026年：出席Waste Management高爾夫球賽（與家人）；提及即將進行「手術」(`qYxm2BkD-v0`同批次其他檔案未直接說明手術類型，`isetVuqlSLo`批次外的其他影片有提及安排medical appointment)；搭乘法航La Première頭等艙（$41,000/座）飛往邁阿密 (`MKeZTAR-VK4`, 2026-06-19)；對SpaceX IPO與Hyperliquid持長期看多立場並自曝為Hyperliquid長期持有者兼「不是理財顧問」的免責聲明使用者。
- 每日固定於Kick平台上午9:00 ET開盤前開始直播（pre-market分析），為其反覆引導觀眾的固定行銷渠道。
- 「22歲百萬富翁」人設隨年齡增長而預告「退場」：多次自嘲「22歲後我就不能再打這個標籤了」，透露其個人品牌高度依賴年齡稀缺性敘事。
