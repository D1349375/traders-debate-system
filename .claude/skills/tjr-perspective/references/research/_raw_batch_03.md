# TJR Raw Research Batch 03
來源：_batch_manifest_03.txt（共 44 個逐字稿，實際處理 44/44；其中 `SHJHpedYh6A`「Beginners Guide To Start Day Trading In 2026 (5 hours)」因單檔逐字稿無換行、單行 30 萬字元超過工具讀取上限，改以字元切塊方式抽樣讀取約 5/7 段落（涵蓋開場動機、軟體/券商設定、K線/趨勢/BOS/流動性/FVG/order block/breaker block/equilibrium/SMT 概念講解、策略整合三步驟），未讀完最後風控與心理段落，其內容與其他已處理檔案高度重疊，故信心足夠列入分析）

## 1. 心智模型候選 (candidate mental models)

- **流動性驅動市場觀（做市商操縱敘事）**：市場由銀行/機構為填單而主動「操縱」高低點，散戶的止損與追價單就是被獵殺的流動性。引用：「liquidity is what moves the market... it's what causes the market to change direction」(`Lxnu7InGhGE`, 2023-06-02)；「the banks... are seeking liquidity so that they can move the market in the direction that they want to」(`Lxnu7InGhGE`)；把 2020 疫情崩盤直接類比成一次「高時間框架流動性清洗」("wasn't that just the best buying opportunity for the market makers", `GJbC6nO3oHQ`, 2024-02-24)。此模型貫穿幾乎全部逐字稿，是最高頻出現的核心信念。

- **高時間框架宰制低時間框架 (HTF dictates LTF)**：「higher time frames hold higher power and are going to cause the market to move in that direction」反覆出現在多支日內偏見(Daily Bias)教學與實盤（`Y1lqifylC4s`；`nfL50_uO9w8`, 2024-02-06："higher time frames hold higher power"；`__fKQR5RR08`）。他因此建立「日內偏見必須先服從週/日線，再往下找確認」的固定順序。

- **機率交易者而非預測者**：反覆強調「trading is about predicting where price wants to go with a high probability... over a long period of time」("`sBmcenZDwk4`")，虧損被視為策略內建、不代表策略失效："there's no strategy that has a 100% win rate. So when you lose, that should be accepted."（`sBmcenZDwk4`）。SHJHpedYh6A 用 LeBron James 打球比喻反覆強化這個心智模型（「even the best game of his life still has missed shots」）。

- **反技術指標 / 反傳統支撐阻力**：「I don't believe in EMAs... indicators trading bots I think they're trash」(`gqqzI7jUqE0`, 2023-04-27)；「it bounced off a floor so I'm going to buy... that makes no sense to me... that's guessing」(`Lxnu7InGhGE`, 2023-06-02)。即使測試一個「Spy AI」交易機器人證明有獲利，他仍堅持「我不會用它，我信任自己」("`gqqzI7jUqE0`")。

- **站在做市商那一邊，而非散戶那一邊**：「we want to be part of the... market makers... not the crowd」(`GJbC6nO3oHQ`)；把「盲目跟單/買訊號」定義為永遠不可能真正變得有能力的行為（`dbF3gamgcFQ`, 2024-04-09）。

- **心理優先於策略（策略只給機率，紀律與心態才是變現關鍵）**：「day trading is really only 10 to 15% of day trading, the rest is psychological」(`NK-RsDCp4Lg`, 2022-10-31)；「the strategy and the confluences really are not the things that are going to help... It's going to be our mindset」(`sBmcenZDwk4`)。

- **顯化/吸引力法則式的自我實現信念（推斷延伸至交易自信建構）**：他明確主張「your focus becomes your reality」、寫日記用現在式肯定句(I am successful/I am financially free)，並將此心法與交易心態訓練並列（`YYoghwU43Kw`；`sBmcenZDwk4`）。這不是嚴格的市場心智模型，但是他解釋「如何培養交易自信/如何撐過虧損期」的底層人格心理模型，值得記錄。

## 2. 決策啟發式 (decision heuristics)

- 若高時間框架（日/週）趨勢仍成立，但低時間框架走勢相反 → 視為「retrace」而非「reversal」，需等高時間框架真正 break of structure 才翻轉偏見。來源(`Y1lqifylC4s`；`B7aj-jNQJxA`, 2023-07-05："what could we have done better... wait for extra confirmation")。
- 若出現 break of structure 但沒有對齊的 FVG/liquidity sweep 等 confluence → 不進場；等待更多confluence 而非單一訊號進場。來源(`GXBFpJFfVLM`, 2024-03-22；`kBb_o34vhos`, 2023-05-19)。
- 若當天有高影響力新聞（CPI、FOMC、NFP）→ 減碼或直接不交易那一天。來源(`52DzoRv_KJ0`, 2023-10-31；`dy9jckID-pY`, 2024-02-01；`Jnadh0FBYGk` 週報)。
- 若情緒不穩（生病、宿醉、心情差、剛分手）→ 不交易或降風險，明確列為五種「何時不該交易」情境之一。來源(`kBb_o34vhos`, 2023-05-19；`NK-RsDCp4Lg`, 2022-10-31)。
- 進場序列固定為：等待價格觸及「關鍵位」(1H/4H 高低點、FVG、亞洲/倫敦/紐約時段高低點) → 降到5分鐘找確認型 confluence（BOS / inverse FVG / SMT）→ 等回撤進入5分鐘 FVG/order block/breaker block/equilibrium → 降到1分鐘等趨勢反轉確認 → 進場，停損放在「觀點被證偽」的位置。來源(`SHJHpedYh6A`策略整合段)。
- 兩個高相關指數（ES/NQ）在關鍵位出現 SMT 背離（一個創新高、另一個未創新高）→ 交易「落後」的那個指數，因為它會被領先指數牽引。來源(`SHJHpedYh6A`；`kH-rbepWkNE`, 2026-04-06；`x92upuz_Z0A`)。
- 若當日沒有高機率設置（no confluence / 臨近時段收尾 / 靠「賭感覺」硬凹理由）→ 寧可不交易，"a day out of the market is actually better than a day in the market"。來源(`kBb_o34vhos`)。
- 虧損後：不追加、不報復性交易；虧損被視為「付學費」("pay-to-play")，情緒反應應趨近於零。來源(`_jLR3XcB5eQ`, 2023-06-02)。（注意：第5節會記錄他多次違反此原則的實例）
- 停損只能放在「交易邏輯被證偽」的價位，不可隨意收緊/放寬去迎合帳戶波動。來源(`SHJHpedYh6A`；`nR9Iikd6V2s`)。
- 每個交易時段（Asian/London/New York）只挑一組最適合自己時區與商品的標的專注交易，不要同時盯 30 個商品。來源(`SHJHpedYh6A`)。

## 3. 表達DNA (expression DNA)

- **高頻口頭禪/自創詞**：「bankroll」被當成近乎咒語式重複強調交易的財富潛力（`SHJHpedYh6A`通篇）；「standing on my business/standing on my [ __ ]」作為自誇獲利時的口號(`B0CWi29zJKU`, 2023-10-16)；稱呼觀眾為「jits/jitterbugs」「boys」；收尾固定語「I appreciate you guys/boys」「I'll catch you guys in the next one, peace/peace out」。
- **情緒化重複詞造成的喜劇效果**：整支影片瘋狂重複「baffled」數十次來表達對行情不如預期的憤怒與荒謬感(`xTVRBgbUBDQ`)。引用：「I would genuinely be baffled if ES doesn't take out these lows」。
- **性/生殖器類比作為記憶錨點的教學手法**：把 fair value gap 比喻成陰莖（"a fair value Gap is a dick... side does not matter... all that we care about is what lies within"），刻意用低俗類比幫助記憶(`SHJHpedYh6A`)。
- **髒話高密度、自我消音（[ __ ]）**：幾乎每句話夾雜髒話，YouTube 版本消音處理，但語氣攻擊性強、直接稱觀眾「idiot/little Timmy/retards」也帶有自嘲（自稱「a [__] with one of the highest leverage skills in the world」）。
- **確定語氣起伏**：對高時間框架偏見常用斬釘截鐵語氣（"I told you guys off rip what was going to happen"，`B0CWi29zJKU`），但實盤中也頻繁自我懷疑、承認不確定（"I could be completely wrong", `sDoYq6WMXGI`）。
- **敘事節奏**：長時間即興獨白、意識流，常在盤中分析時岔題聊生活瑣事（健身、跑步、狗Boogie、賭博、飲食），呈現「邊做邊播」的真人秀感。
- **反同業話術但同時自我推銷的矛盾腔調**：一邊痛批賣訊號/賣課的同行「if you're paying you are admitting that you are unprofitable」(`B0CWi29zJKU`)，一邊持續推銷自己的 Mastermind/免費 Discord 制度，語氣上刻意用「這不是廣告，因為你現在買不到」來自我辯護(`dbF3gamgcFQ`)。
- **LeBron James/NBA 類比**是他解釋「機率思維」「技能可轉移」的固定比喻庫，在多支影片重複出現(`sBmcenZDwk4`；`SHJHpedYh6A`；`_jLR3XcB5eQ`)。
- **勵志/顯化語言**：「your focus becomes your reality」「nothing changes if nothing changes」「I am successful」式現在式肯定句書寫法(`YYoghwU43Kw`)。

## 4. 決策記錄與案例 (decisions & track record)

- $176,000 單日獲利，與學員 Tim 邊喊盤邊教學（`1imPWpFwKVo`, 2026-03-03）。
- $137,872 單日獲利，標題自稱「risked entire account」（`BPQhu2L1Tzc`）。
- $103,000 單日獲利，由 ES/NQ SMT 背離空單完成（`OJXkE2h2mz4`）。
- $60,630 單一設置獲利，發生在自己生日當天直播（`kH-rbepWkNE`, 2026-04-06）。
- $150,000 單日獲利，稱「up $500K this week」（`sDoYq6WMXGI`）。
- $44,165，稱為「my best trading day all year」（`CMsuCPOwEpI`, 2024-10-02）。
- $39k Nas100 獲利（`B0CWi29zJKU`, 2023-10-16），並自稱「past three weeks... 150k」「200 bucks off月獲利300K目標」。
- 虧損案例：單日虧 $161,430，稱「down $220K/$227K this month」（`x92upuz_Z0A`）；單日虧 $75,610（`xTVRBgbUBDQ`）；單日虧 $53,934，標題「traded while hammered」（`zUAKtc8fnv0`）；$13k SPX 虧損（`B7aj-jNQJxA`, 2023-07-05）；兩次 $9k SPX 虧損（`PviUVrNVe3Y`, 2023-08-22；`__fKQR5RR08`）；$4,689 虧損（`yG5AO7G7tsQ`, 2023-07-06）。
- 初學者指南中回顧提及「made $25,000 on this trade」的 SMT 案例（`SHJHpedYh6A`）。
- 自稱身家「several millions of dollars」、23 歲買下 Koenigsegg Regera 超跑（`YYoghwU43Kw`）。

## 5. 矛盾 / 立場演變 (contradictions & evolution)

- **訊號/付費社群立場反覆搖擺**：2023-10-16（`B0CWi29zJKU`）他仍在營運付費 Discord、直播帶單教學並賣課。2024-04-09（`dbF3gamgcFQ`）他宣布「The Discord is closed forever...I'll never give out signals again... I don't know why I even gave out signals in the first place」，並批判賣訊號的商業模式「that's literally just placing a pause on our students profitability」。但同一支影片他仍在賣「Mastermind」；到 2025 年之後的影片（`zXQ7ig-TWqI`）又出現「Discord is closed until the first through the 7th of every month」的固定重開機制，顯示「永久關閉」承諾並未真正兌現，而是演變成規律性重開放的商業模式。
- **反同行 vs 自我商業化的張力**：他嚴厲批評其他交易導師/網紅靠「賣課/賣訊號/秀生活方式」割韭菜（例如公開點名批評 Wes Watson 的投資課程「it doesn't really sit right with me」，`tJ_1tLe0jvE`），但他自己同樣經營高單價 Mastermind、放出「funded account 抽獎」導流，他試圖用「我的 YouTube 是免費的」「Mastermind 是直播互動不是預錄課程」來自圓其說，但界線其實模糊。
- **「情緒歸零、機械式執行」的教條 vs 實際直播行為的落差**：他反覆教學「不該對輸贏有情緒反應」「像機器人一樣執行」（`_jLR3XcB5eQ`, 2023-06-02；`kBb_o34vhos`, 2023-05-19），但在多支實盤直播中明顯情緒失控：飆罵、崩潰、承認「revenge trading」（"I'm completely flipping bias. I'm shorting NASDAQ here... Revenge trading final boss"，`x92upuz_Z0A`），與其教條直接衝突。
- **社群管理態度的驟變**：2024-02-06（`nfL50_uO9w8`）他在直播中對付費會員爆怒，威脅「kicking out and removing a lot of people」，語氣與他平常「I love you guys」「we build a great community」的溫情敘事形成明顯反差，顯示他的耐心/親和力人設在壓力下會迅速切換成嚴厲甚至羞辱式管教。
- **交易年資說法**：2023-10-16 明確宣稱「I've been trading for 5 years now, 5 years of trading experience」（`B0CWi29zJKU`）；`SHJHpedYh6A`（未標日期，內容提及"2025"「making generational wealth in 2025」等，推測拍攝於2025年初）敘述創業歷程時間軸（高中加密貨幣→轉賣鞋→短暫嘗試多種副業→回到交易）並未給出精確年資數字，兩者無法直接互相印證，但年資敘述隨時間持續往上抬升，屬於典型「經驗值不斷升級」的敘事演變（推斷）。

## 6. 時間線 / 背景事實 (timeline & bio)

- 本名 Tyler（姓氏 Riches，`sBmcenZDwk4` 影片中自稱「Tyler, Tyler Riches」）。
- 高中時期就開始碰加密貨幣，賺到錢又全部虧光，之後嘗試球鞋轉賣/Supreme代購機器人、Snapchat Creator 變現法（賺約$3,000）、短暫考慮 Dropshipping/房地產/Section 8 房產/文案代寫，最終才又回到交易（`SHJHpedYh6A`）。
- 曾經濟拮据到「literally stealing [食物] orders」「go up to the doors individually and personally ask the people for cash so that I could... fuel my car up with gas」以維持送 DoorDash 外送（`sBmcenZDwk4`；`SHJHpedYh6A`重複敘述同一段故事）。
- 2023-10-16 自稱交易資歷 5 年（`B0CWi29zJKU`）。
- 23 歲時購入 Koenigsegg Regera 超跑，並將此事件作為「顯化法則」教學案例（`YYoghwU43Kw`）。
- 常駐地點在波多黎各（稅務考量 Act 60）與邁阿密之間移動；養狗 Boogie；有女友；朋友圈刻意維持極小（自稱僅兩位摯友），自我定位為 introvert（`dbF3gamgcFQ`, 2024-04-09）。
- 經營自營資金挑戰（funded account）相關業務/合作（如 Alpha Futures 帳戶交易、與 Lucid 資助商合作贈送 funded 帳戶）（`OJXkE2h2mz4`；`1imPWpFwKVo`）。
- 「Trading Transformation」與「Boot Camp」為其編號式教學影片系列（Day 8、11、36、42、49、50 等），顯示 2023 年中至 2024 年間有系統性課程規劃（`Lxnu7InGhGE`、`_jLR3XcB5eQ`、`Y1lqifylC4s`、`NPG_BZ_83fo`、`__fKQR5RR08`、`QRvZgj3k8pk`）。
- 2026 年的直播中，開始固定與學員/朋友「Tim」「Isaac」互動教學，Tim 被描繪為財務衝動示例（提領 $25,000 資金去買車）以對照 TJR 的自律形象（`kH-rbepWkNE`, 2026-04-06）。
- 付費 Discord/Mastermind 政策隨時間變化：2023 年為常態開放付費社群 → 2024 年宣布永久關閉不再帶單 → 後期演變為每月 1 日至 7 日固定重新開放的訂閱制（`zXQ7ig-TWqI`）。
