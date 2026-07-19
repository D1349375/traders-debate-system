# TJR Raw Research Batch 15
來源：_batch_manifest_15.txt（共 49 個逐字稿，實際處理 49/49）

## 1. 心智模型候選 (candidate mental models)

- **流動性=訂單填充機會 (Liquidity as order-fill opportunity)**：價格衝過前高/前低不是「趨勢確認」，而是機構在那裡填單，之後才有反轉/延續的機會。「Liquidity is step one of our strategy...price has the opportunity to fill orders above highs and below lows. It doesn't mean that price has to fill orders. It just means price has the opportunity.」(`4sRDnVmLcMk`, 2026-01-09)。這個框架在幾乎每支「daily bias」「live trading」影片中都出現，是他解讀盤面最底層的邏輯。

- **三層確認流程：Liquidity sweep → 訂單流轉變(BOS/inverse FVG) → 延續確認(FVG)**：他把交易切成「reversal confluence → confirmation confluence → continuation confluence」三段。「liquidity...that's the reversal confluence...break of structure...I call a confirmation confluence...fair value gaps [are] a continuation confluence」(`4sRDnVmLcMk`, 2026-01-09)。這套三層模型在 `xcDOMKaOIsk`（Fair Value Gaps Explained）、`PlsHO33j6B8`（Advanced Imbalance Concepts）等技術影片中反覆講解，是他核心策略骨架。

- **Inverse FVG 等同於 break of structure（不是必須要「回補」的東西）**："inverse fair value gaps are confirmation confluences and are equal to break of structure...I just use whichever comes first" (`xcDOMKaOIsk`, 無日期)。他也在別的影片中明確反對「一定要等它填回」的教條：「I'm not necessarily a huge fan of using inverse fair value gaps like getting tapped back into as like a Confluence... I am a fan of seeing fair value gaps getting invalidated and taking trades based off of that」(`rMkghkG-ZjE`, 無日期)。

- **價格是分形的 (price is fractal)**：「price moves the same way on every single time frame」，任何時間框架的邏輯可以套用到其他框架，這也是他把高時間框架偏向(HTF bias)套到低時間框架執行(LTF execution)的理論基礎。多次出現，例如 `NZqRbc_9u_I`（2025-02-12）、`kl_aMLMISdg`（2025-09-29）。

- **均衡(Equilibrium)=機構的溢價/折價分界**：「when are they buying? in a discount...when are they selling? at a premium...take it from the swing High all the way down to the swing low...this is our 50 mark」(`lyXKaPy-1SU`, 2022-11-11)。這是他早期(2022年底)就系統化教授的核心工具，之後每天的 daily bias 影片都會用。

- **PM Session = AM Session 策略的「縮時版」**：「it's exactly like my strategy we're just using lower time frames...instead of using High time frame draws on liquidity we're using lower time frame draws on liquidity」(`UR6vM7nPBeo`, 無日期)。這代表他相信策略本質不變，只是時間框架的相對縮放，是「分形」信念的延伸應用。

- **教學者/人設即事業(Teacher persona as business model, 演變中)**：他把自己定位成「填鴨式教學 + 生活風格網紅」的混合體，早期(`IfSiPGirNIY`, 2022-12-31)就明講：「I want you guys to like me for me...I want this to be a little bit different than any other just like stock or Forex trader...I want you guys to actually enjoy my personality in my life versus just enjoying the content」。這個「人比策略更重要」的行銷哲學貫穿整個研究樣本，從 vlog 到教學影片再到募資型 mentorship 都能看到。

- **反訊號商業模式的道德十字軍 (anti-signal-seller crusade)**：他把「賣訊號/直播喊單」定義為對學員有害的行為，多次以近乎懺悔的語氣宣布「戒斷」：「if you are a Trader right now and you are offering trades like live trades...you are literally putting you guys on pause for your guys's journey to profitability」(`wDH8IqakaQo`, 無日期，Trading Transformation Day 5)。同樣主題也出現在 `0vgTPBz3htk`（2023-12-18，關閉 Discord）。（見下方「矛盾」一節，此信念與後續行為有明顯落差。）

## 2. 決策啟發式 (decision heuristics)

- If 在 daily bias 中偵測到「liquidity sweep + break of structure」但**沒有**第三個確認(FVG/order block/breaker/equilibrium)，then 不進場，繼續等待。「I've decided to wait for three confluences so right we have point of Interest hit break of structure and then there has to be something else」(`K9Q7Xdyr_3w`, 2023-08-06)。

- If 高衝擊新聞(high-impact news)即將公布，then 不在公布前進場，等新聞出後再依訂單流交易；NFP 對外匯(Forex)影響遠大於對指數(indices)的影響，因此「NFP doesn't affect indexes but it does affect Forex」(`RG0j6CpCiqo`, 無日期)。多篇 daily bias/market recap 影片重複「wait for news to come out」的規則（如 `Kmo1HraIvDA`, 2024-06-06；`r0cxo3T9yas`, 無日期）。

- Risk management：每筆交易風險帳戶的 1–3%，且每天總風險上限也是 1–3%（可以拆成多筆但總和不超過）。「risk one to three percent of your account...you're not always going to see multiple setups every day...for risk management one to three percent A DAY」(`RkMBoqbeUq8`, 無日期，Boot Camp Day 13)。

- If 第一個 take profit 命中，then 移動停損到成本價(break even)，再視情況分批出場；這個「保本後續抱」規則幾乎每支 live trading 影片都會執行（如 `1MHLqvC2fDE`, 2025-09-19；`J1vPj1m6crQ`, 2025-04-30）。

- Take profit 一律設在下一個「building block」（liquidity/FVG/order block/breaker）上，不是隨意設定；且優先看「執行時間框架高一階」的流動性目標。「when I set take profits I do it off of...the one Higher time frame draw on liquidity on whatever execution time frame I'm on」(`FjSiLFrg5fo`, 2023-07-02)。

- If 帳戶在 demo/paper trading 上**連續三個月**盈利，then 才可以投入真實資金；否則永遠留在 demo。「you guys are going to forever be on demo until you guys can prove...after three straight months of green」(`NZqRbc_9u_I`, 2025-02-12)。此規則與他自己近期「加大風險、單日虧損4.5萬~9.9萬美元」的行為有落差（見矛盾節）。

- If 多個 fair value gap 疊在一起（中間沒有反色K棒回撤），then 只看「疊層最外側（最底/最頂）」的那個 gap 來判斷是否 inverse，而非任一個。「in order for me to be able to say okay price has inversed these gaps...we have to wait for this one [the topmost/bottommost]」(`xcDOMKaOIsk`, 無日期)。

- If 已經在某段趨勢中「填補 imbalance 並突破前高/前低」，then 該趨勢段左側所有更早的 confluence（fvg/order block/breaker）視為「已平衡」，之後不再納入考量。「everything from this low and underneath we no longer care about those confluences」(`xcDOMKaOIsk`, 無日期)——這是他解釋「趨勢延續而非走回頭路」的核心篩選規則。

## 3. 表達DNA (expression DNA)

- **開場/收尾慣用語**：常用「what is good jits / boys」開場；收尾幾乎固定「I appreciate you guys, I'll catch you guys in the next one, peace out」（幾乎每支影片都出現，例如 `xcDOMKaOIsk`, `PlsHO33j6B8`, `HDxpo-Vj3JA`）。

- **敘事實況時的擬聲詞/節奏感**：進場等待時反覆用「boom」「heat heat heat」「bing bing bing」「go go go」來營造盤中緊張感，例如 `1MHLqvC2fDE`（2025-09-19）：「Bing bing bing bing bing bing... Good boy. Use that pickaxe.」把價格走勢擬人化成小遊戲（挖礦、寵物）。

- **粗口與教學內容並存，且用粗俗類比解釋概念**：用「dick size doesn't matter」類比 fair value gap 大小不影響其有效性：「fair value gaps are like dicks size does not matter...a big one we probably want that one...but also a little guy a two incher even a microen it can do the job as long as we get in there」(`xcDOMKaOIsk`，無日期)——這是他把嚴肅技術內容「娛樂化」的招牌手法。

- **絕對化確定語氣**：講解時使用「simple as that」「money made」「that's it」「boom」等詞收束論證，語氣極度自信，例如「boom simple as that guys」(`FjSiLFrg5fo`, 2023-07-02)、「that's how you take profits...really not much else to explain here」（同上）。

- **對「初學者/散戶」的雙重語氣**：一方面極度勵志打氣（"you can do this", "I am no different than y'all"，`-sE6O1YWgMc`, 2023-06-22），另一方面對「伸手黨/不認真學習者」極度不留情面：「if you don't take trading serious leave I don't want you there」(`0vgTPBz3htk`, 2023-12-18)。

- **自創/慣用術語**：「full port(ing)」（全倉重壓）、「dub」（贏）、「L」（輸）、「bands / racks / K」（千元單位）、「draws on liquidity」「low resistance liquidity」「building blocks」；「kill zone」borrowed from ICT 但融入自己敘事。也常說「that's how the game goes」、「we cooked / we're cooking」表示交易順利。

- **口頭禪/填充語**：極高頻率使用「bro」「dude」「like」「literally」「[ __ ]」（審查掉的髒話）；直播時常穿插與觀眾/聊天室互動的吐槽（如嘲諷 kick 聊天室的「competition」）。

- **禁忌/敏感詞使用**：對聊天室酸民極度直接開嗆，甚至人身攻擊式反諷（如 `zkspNT72GP4` 樣本中對 kick 聊天室網友的「if you're profitable, you wouldn't be watching this」系列嗆聲）。

- **幽默方式**：自嘲式的、誇張式的、常把嚴肅財務數字與荒謬玩笑並置（例如一邊講「made $317,572 today」一邊唱歌、講機場憋尿糗事）。

## 4. 決策記錄與案例 (decisions & track record)

- 單日最佳交易日：「$317,572.90」，稱為「MY BEST TRADING DAY ALL YEAR」(`IeFZ43LvjcU`, 2025-11-17)。
- 「I AM UP 431K THIS MONTH」，同週淨賺 $427,224.90（`1MHLqvC2fDE`, 2025-09-19）。
- 單日虧損 $45,000（因主動提高風險）：「lost $45,000 today...I've been so risk off due to crypto. But now I'm looking to be more risk」(`NLRBtK0jnxQ`, 2025-03-15，同日簽約買下 Puerto Rico $2M 現金屋)。
- 單日虧損 $99,000（隔週提到），隨後單日 $317K 大反彈補回（見上）。
- 一週內從虧損 $10,523 三倍賺回：「How I Lost $10,523 from One Trade Then Made It Back 3x」影片全程覆盤自己一週的錯誤決策(`RG0j6CpCiqo`, 無日期)，包含承認自己「試圖接住下墜的刀子(catching a falling knife)」是錯誤。
- 三筆 SPX 交易一週賺 $50k（`K9Q7Xdyr_3w`, 2023-08-06）。
- 直播交易日 $65,800（扣除手續費後 $57K）(`WnrKJs8ePB0`, 2026-01-20)；同集透露「funded/prop account」交易只是為了「證明一個觀點(prove a point)」，本身零意義（"Zero point"）。
- $67,680 交易日，標題自稱「I FULLPORTED NEWS」(`vIjIitndRXQ`, 無日期)。
- 場外賭博/投機：在 NBA Finals（尼克 vs 馬刺）上下注 4萬~ 4.1萬美元，透過 Polymarket 現場加倉，單場獲利 $160,000（`CZMC3UNVuNs`, 2026-06-12）；提及「crypto」持倉大幅波動、之前在 Turks and Caicos 遭搶劫並「almost killed someone」。
- 現金買下 $2,000,000 波多黎各豪宅，時年 22 歲，因無法在波多黎各取得房貸融資（缺乏當地信用史/穩定收入證明），改用出售加密貨幣部位支付（`NLRBtK0jnxQ`, 2025-03-15）。
- 2023-12-18 正式宣布關閉 Discord 訂閱制信號房，轉型「one-on-one mentorship」，附贈 $100,000 funded account（`0vgTPBz3htk`）。

## 5. 矛盾 / 立場演變 (contradictions & evolution)

- **「永遠不再發即時交易信號」vs 持續直播即時進出場**：2023-12-18 宣稱「we're done with signals...I'm no longer going to be giving signals」(`0vgTPBz3htk`)；`wDH8IqakaQo`（無日期，Trading Transformation Day 5）更完整闡述「giving live trades hurts your students...stop posting live trades today」。但 2024–2026 年份的多支影片（`Fb2P0Qu-fXo` 2024-06-25、`Kmo1HraIvDA` 2024-06-06、`1MHLqvC2fDE` 2025-09-19、`WnrKJs8ePB0` 2026-01-20 等）他持續每天在 Kick 直播並公開具體進場點、停損、停利，且鼓勵觀眾「follow me on Kick every single morning」。這是研究樣本中最明顯、跨最多影片的立場與行為落差。

- **風控哲學（1-3%/日）vs 近期主動加碼冒險**：2023 年 Boot Camp 明確教「risk one to three percent of your account per day」(`RkMBoqbeUq8`)；但 2025 年多支影片他自陳「I've been trading a little bit more aggressive...I've been so risk off due to crypto. But now I'm looking to be more risk」並在同一天虧損 $45,000（`NLRBtK0jnxQ`, 2025-03-15），另一集也提到單筆風險達 $40,000（`kl_aMLMISdg`, 2025-09-29）。他自己也承認這與「新手不該追求快錢」的教條矛盾，但用「這是我贏得的自由/我已經證明過自己」來合理化。

- **對「三個月demo才可上真倉」的規則 vs 自身早期經歷**：他在教學影片一貫要求學生先在demo證明三個月盈利才能上真倉(`NZqRbc_9u_I`, 2025-02-12)，但自述式回顧影片中承認自己當年「would trade on demo...then after like two green days...I would jump over to a live account and then lose all my money」(`cXlVBiwIlbI`, 2025-09-04)，屬於他親口承認的「早年犯過的錯誤」，用以警示觀眾——這裡不是矛盾而是刻意的「反面教材」敘事。

- **手錶「不是好投資」vs 大量炫耀手錶收藏**：在 Q&A 中明確說「I think watches are a really stupid investment...I don't even consider them Investments」(`V4Zw-xE6x94`, 無日期)，但同一批樣本中多支 vlog（`CZMC3UNVuNs` 2026-06-12、`HB6Z-jHW5Tk` 2023-08-18）大量展示、更換、討論名錶（Richard Mille、Audemars Piguet 等）作為身份/生活風格展示的核心道具。（推斷：他區分「投資」與「消費/身份認同」兩個帳本，但對外呈現的內容仍以炫耀消費品為主。）

- **「不希望走紅／想保持地下(underground)」vs 積極衝訂閱數KPI**：2023-12-18 說「I wish I could have stayed underground for as long as possible」(`0vgTPBz3htk`)，但同一支影片和多支其他影片都在追逐具體訂閱數字目標（100k→250k→500k→400k 等），並公開喊話催更、設定明確衝量計畫，顯示「反主流化」修辭與實際成長企圖之間的張力。

- **保健品/自我藥療的立場**：他大力推薦一個未受規管、單價高昂（單包 $250、單次採購達 $5,000-$8,600）的「Interstellar Blends」保健品品牌，聲稱其協助他停用抗憂鬱藥物(SSRI)、戒除尼古丁與大麻依賴、治療「the c word」（暗指癌症或COVID，語意含糊）(`uTJBy34bLKY`, 無日期)。這與他一貫「no cap, 100% transparent, 不騙你錢」的人設形成潛在張力：他強調「no referral, no sponsorship」，但同時做出近乎醫療等級的療效宣稱，屬於（推斷）高風險的信任轉嫁行為，值得存疑處理。

## 6. 時間線 / 背景事實 (timeline & bio)

- 2022-12-31（`IfSiPGirNIY`）：頻道仍屬早期草根階段——影片中提到「we hit 20K on Tick Tock」「we're at like 2.5k Subs」，內容包含開箱 PS5、打籃球、日常 vlog，尚未大量產出交易教學內容；本人透露曾在大學期間只去上期中考，其餘課全翹。

- 2022-11-11（`lyXKaPy-1SU`，Equilibrium 教學）：頻道仍未開通YouTube營利（「we are still not monetized on YouTube」），屬於教學系列建置初期。

- 2023-03-02 / 03-03 / 03-16（`I0_gEOkHz4A`, `BmyfIFwfmp8`, `0BhgyVX_Z6w`）：早期「Live Trading with Discord」系列，尚在經營付費Discord訂閱模式，教學風格已定型（daily bias→liquidity sweep→BOS）。

- 2023-05-30（`N7so8LEHmLA`，Boot Camp Day 5）／2023-06-03（`-ga9oK2bClQ`，Day 9）／2023-07-02（`FjSiLFrg5fo`，Day 37）：「Boot Camp」系列（免費教學課程），本人提到計畫「連續兩個月每天上傳」，目標是打造「day trading community」；同期提到正在等新電腦、設備升級中。

- 2023-06-18／06-22（`6M6FJtrOhoE`, `-sE6O1YWgMc`）：搬家至波多黎各（Puerto Rico），購入 Ram TRX 卡車（因缺乏波多黎各信用史/穩定收入證明，銀行拒絕貸款，最後找父親作共同簽署人/或現金支付）；帶著寵物狗 Boogie 一起搬遷。

- 2023-08-06 / 08-18（`K9Q7Xdyr_3w`, `HB6Z-jHW5Tk`）：週交易獲利 $50k 案例；紐約週末旅行 vlog，提及當週交易「undefeated」。

- 2023-12-18（`0vgTPBz3htk`）：正式宣布 Discord 於 2024-01-01 起停止新用戶加入（既有月費/終身會員維持），轉型「one-on-one mentorship」（月費制→高單價教練制），宣稱要「clean up」交易產業、淘汰只想「full port 跟單」的伸手黨；同時提到 YouTube 訂閱數目標「250k→500k」。

- 2024（`NFl7lg-wV-k` 2024-02-01、`Fb2P0Qu-fXo` 2024-06-25、`Kmo1HraIvDA` 2024-06-06、`m3Jit86SyO8` 2024-06-03、`2rKRtWI3QVE` 2024-05-29、`0tJk_41xbAM` 2024-05-07）：進入固定產出「Trade Recap」「Market Recap」「Daily Bias」系列高峰期，教學內容細緻化（inverse FVG、SMT divergence、BPR 等進階概念系統化）；提及「Mastermind 3.0」學員課程與持續在 Kick 每天早上 9am 直播。

- 2025-02-12（`NZqRbc_9u_I`）：發布「How To Start Day Trading With $0」，回顧自己曾靠 DoorDash/Uber Eats 兼職籌措交易本金，「negative $2,000 in bank account」的低谷經歷。

- 2025-03-15（`NLRBtK0jnxQ`）：22 歲，現金買下 $2,000,000 波多黎各豪宅；同日交易虧損 $45,000；提及「blueprint」學員課程持續產出多筆 funded account pass 與 payout。

- 2025-09-04（`cXlVBiwIlbI`）：自陳「been in this space for 6 years now」，回顧自己從高中階段開始交易生涯的心路歷程。

- 2025-09-19 / 09-29 / 11-17（`1MHLqvC2fDE`, `kl_aMLMISdg`, `IeFZ43LvjcU`）：連續高獲利/高波動交易月份，多次提到「super locked in going into this week」「chipping away at that ugly monthly balance」等語，顯示某段時間曾處於全月虧損狀態後逐步扳平。

- 2026-01-09 / 01-20 / 03-02（`4sRDnVmLcMk`, `WnrKJs8ePB0`, `BdBxXKGWVjk`）：技術教學系列（"Path to Profitability"）持續產出；`BdBxXKGWVjk` 自稱「made seven figures just last year alone with trading in inverse fair value gaps」。

- 2026-06-12（`CZMC3UNVuNs`，「My Regular Day As A 24 Year Old Millionaire」）：24 歲；持續住在波多黎各；經營服飾品牌「Killtech」；正在籌辦「TJR Island」旅遊/篩選學員活動（面試申請者、贊助商洽談）；TikTok 主帳號一度被封鎖一個半月、掉粉 10 萬（1.9M→回復）；後院裝修花費約 $600,000（三溫暖、冷水池、按摩浴缸）；在紐約尼克 vs 馬刺 NBA 總冠軍賽現場下注並即時加倉。

備註：manifest 中部分逐字稿（如 `PlsHO33j6B8`、`QRoLG0QRiNM`、`RG0j6CpCiqo`、`RkMBoqbeUq8`、`UR6vM7nPBeo`、`V4Zw-xE6x94`、`_V9T1FDPtAs`、`rVioajyWsFQ`、`uOp1jdHGtos`、`uTJBy34bLKY`、`vIjIitndRXQ`、`vieka41svDA`、`wDH8IqakaQo`、`wqxyMao1gxE`、`xcDOMKaOIsk`、`zkspNT72GP4`）逐字稿第一行沒有明確的 Upload Date 標記，因此上述引用僅標註 videoID，日期欄位留白或以「無日期」註記，未強行推測。
