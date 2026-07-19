# TJR 決策啟發式、交易案例與 track record（合併自 16 批）

> 本檔案合併自 `_raw_batch_01.md` 至 `_raw_batch_16.md` 全部16份原始抽取筆記之「第2節：決策啟發式」「第4節：決策記錄與案例」以及「第5節：矛盾/立場演變」中與決策/數字相關的內容。合併原則：逐字重複規則予以合併，語意相近但情境不同者予以並列保留；具體交易案例逐筆附 videoID 與日期，數字有出入或疑似同一事件不同轉述者明確標註「衝突/待核」。

---

## 一、決策啟發式 (If-Then 格式，按主題分類)

### 1.1 進場確認條件 (Entry Confluence Rules)

- **If** 高時間框架（4H/1H/日/週）流動性被掃蕩（liquidity sweep）**AND** 低時間框架出現 break of structure 或 inverse FVG **AND** 與高時間框架趨勢同向 **then** 進場；三者缺一則等待，不進場。來源(`scI-Pp0FL2I`, 2025-08-21；`aobHuNcI1QM`；`a5PLl1uM7CQ`, 2025-03-18；`ironJFzNBic`, 2026-01-14；`It4_gJjSOyY`, 2023-07-11)。
- **If** 只有 liquidity sweep + break of structure，**没有**第三個 confluence（order block/FVG/equilibrium）**then** 不進場，繼續等待。來源(`K9Q7Xdyr_3w`, 2023-08-06："I've decided to wait for three confluences")；(`GXBFpJFfVLM`, 2024-03-22；`kBb_o34vhos`, 2023-05-19)。
- **If** 沒有liquidity sweep，即使有break of structure **then** 不進場——他公開檢討自己虧損的核心教訓。「there was a 15-minute smt Divergence and we see...it didn't sweep any liquidity and you see that's where I went wrong」(`LW-Mncm1RGo`, 2024-10-28)。
- **If** 市場形成equal highs/equal lows（等高/等低）**then** 傾向不從那裡進場，因為那只是流動性堆積尚未被清掃。「I'm never a fan of taking a trade if we end up making equal lows or equal highs...I have Trauma from equal highs and equal lows」(`fwu9FnvwnNc`, 2024-10-03)。
- **If** 高時間框架方向互相矛盾（例如日線多、週線空、4H空）**then** 不交易/按兵不動，等其中一個給出突破確認。來源(`-rYGugTIsbU`, 2023-07-17；`Z-9HuHf5egU`；`32BbWfoZDCw`, 2023-08-16"mixed bias day")。
- **If** 下降趨勢中4H/日線出現逆勢break of structure **then** 預設為「更高時間框架的回撤」而非趨勢反轉，除非更高框架也跟著破結構。來源(`bQwAlwVuPbI`, 2023-10-27)。
- **If** 4H偏多 **AND** 1H偏多 **then** 直接降到5分鐘找liquidity sweep+BOS進場；**If** 4H偏多 **BUT** 1H偏空（方向衝突）**then** 必須降到15分鐘找確認再進場。來源(`67vLAkcdPu4`, 2024-03-16)。
- **If** 開盤前（pre-market/倫敦時段）高時間框流動性已被掃且已有反應 **then** 不需等紐約開盤才進場；**If** 尚未反應 **then** 等紐約開盤後的5分鐘低時間框架操縱確認再進場（"session relay"規則）。來源(`-Tl6Dr5seeE`, 2025-10-23；`8QDDxwUV1KM`, 2025-10-06；`zSgXNr2-1Vw`)。
- **If** ES/NASDAQ兩指數在關鍵高低點出現SMT背離 **then** 交易「較弱/落後」的那個指數，因為會被領先指數牽引；**注意此規則的方向性隨時間反轉，見下方「三、矛盾與立場演變」**。來源(`SHJHpedYh6A`；`kH-rbepWkNE`, 2026-04-06；`d5uOjnuzYhE`, 2024-07-29；`7dTQA0t8SH0`, 2026-01-11)。
- **If** SMT背離出現但**沒有**明確bias **then** 不視為進場理由，SMT只用來「強化」既有偏見。來源(`TNyTn30CPVg`)。
- **If** 已經在某段趨勢中「填補imbalance並突破前高/前低」**then** 該趨勢段左側所有更早的confluence（FVG/order block/breaker）視為「已平衡」，之後不再納入考量。來源(`xcDOMKaOIsk`)。
- **If** 多個FVG疊在一起（中間沒有反色K棒回撤）**then** 只看疊層最外側（最底/最頂）的那個gap來判斷是否inverse，而非任一個。來源(`xcDOMKaOIsk`)。
- **If** 進場邏輯需要收盤突破確認（如order block）**then** 只有「body」真正吃到才算有效反應，單純wick觸碰只是測試，不算數。來源(`T-Bo-9GDi3s`)。
- **If** 某個高時間框架confluence在盤前就已被觸碰過 **then** 視為「用過的」較弱訊號，偏好只在正式開盤後才被觸及的confluence。來源(`FZGcC3m4bDk`, 2024-08-28)。
- 每個交易時段（Asian/London/New York）只挑一組最適合自己時區與商品的標的專注交易，不要同時盯多個商品。來源(`SHJHpedYh6A`；`7zAy8xbzoNo`, 2023-11-27)。

### 1.2 風險控管規則 (Risk Management)

- 每筆風險固定 1-2%（部分表述為1-3%）；同一天原則上只交易一筆（每個session最多一筆）。來源(`nQj01ZbJ6S0`, 2023-02-16；`-mJ8mww-Flw`；`AEoCaWFRXHU`)。
- 風控規則：每筆風險1-3%帳戶資金，絕不all-in／全倉（"full port"）；第一個止盈觸發後將止損移到保本點。來源(`JKx476um7B0`, 2023-11-10；`RkMBoqbeUq8`, Boot Camp Day 13)。
- **If** 使用固定手數（set lot size）**then** 先算出該商品的平均停損點數，用1%風險反推手數；之後依實際停損倍數等比例調整風險（例如停損是平均的兩倍則風險變2%）。來源(`ik3aIvZ4NrU`)。
- 每天最多1-2筆交易；若做2筆則兩筆風險加總等於1筆的預定風險額度。來源(`bEkbNGUzQME`, 2023-05-27；`065lMUrD_kg`, 2023-06-24)。
- **If** 只有一筆交易的風控預算未用完 **then** 剩餘風險額度可用於第二個高信心設置（風險預算槓桿式運用）。來源(`ss-dZPMnjeY`, Boot Camp 2.0 Day 9)。
- **If** 交易funded/prop account **then** 每日最多只能用「每日最大回撤額度」的50%（例如帳戶日回撤5%則單日風險上限2.5%），只挑「A+」設置；funded帳戶心理與live帳戶心理需分開處理。來源(`rbVc6ZFPO7s`；`tT3lUnwayb0`)。
- **If** 處於funded account評估期(evaluation) **then** 刻意拉高風險爭取快速過關；**If** 已進入可出金/qualified階段 **then** 降回正常風險，因為規則（一致性比例、daily loss guard）在此階段轉嚴。來源(`-Tl6Dr5seeE`, 2025-10-23)。
- 帳戶採漸進放大：demo（至少3個月穩定10%+/月獲利）→ 小額live帳戶($100，3個月)→ $1,000 live帳戶(3個月)→ funded account挑戰；funded與live同步交易，live帳戶規模追上funded後即可放棄funded。來源(`XwkUiHdNfsE`；`TwakmPZJGJA`；`UNT_fytJB3Y`；`r6QaBbR5mz0`)。
- **If** 帳戶在demo/paper trading上連續三個月盈利 **then** 才可投入真實資金；否則永遠留在demo。來源(`NZqRbc_9u_I`, 2025-02-12)——**注意：他自己承認早年並未遵守此規則，見矛盾章節**。
- 出金紀律：早期建議獲利後提領75%只留25%在帳戶滾存，隨信心增加逐漸調整比例到100%提領。來源(`ik3aIvZ4NrU`)。
- Prop firm出金後的資金分配規則：先扣稅金存高收益儲蓄；50%再投入新的資金帳戶（成長）；30-40%放入傳統投資組合(S&P500/國債/私募股權)；10-20%作為個人犒賞消費。來源(`JY4DK_ZLDqQ`, 2026-03-16；`eJLqMkfUHkI`)。
- **If** 若第一筆風險交易虧損 **then** 第二筆降低風險比例（例：第一筆風險2%輸了，第二筆降到1%）；藉此在1-2天內"合規地"通過資金挑戰。來源(`ZSJOrOeSzM0`, 2023-07-31)。**注**：這與他公開批評「funded challenge公司規則是設計來讓你輸」的立場並存，見矛盾章節。
- **If** 賭博意外贏得大錢 **then** 立刻花掉，否則會在下次賭博中全部虧回去（他明確的個人金錢管理規則，非交易規則）。來源(`0NfGO54E7T4`, 2026-07-03："If you make a bunch of money gambling, spend it immediately")。

### 1.3 停損 / 停利管理 (Stop Loss / Take Profit Management)

- 停損只能設在「使交易邏輯失效」的價位（如liquidity sweep點之外+點差緩衝），設定後絕不因恐懼下移；停利點也不可因貪婪延後（除非有新的高機率理由延長）。來源(`RKu5SernXY8`；`SHJHpedYh6A`；`1FunNCUw_jM`, 2023-07-03；`nR9Iikd6V2s`)。
- 若停損放在order block/FVG之上會被spread打掉，故停損永遠設在sweep高/低點之外。來源(`1FunNCUw_jM`, 2023-07-03)。
- 第一個止盈觸發後，停損移到成本價（略高於進場價以覆蓋手續費/點差），分批出場（如50/25/25）。來源(`It4_gJjSOyY`, 2023-07-11；`bQwAlwVuPbI`, 2023-10-27；多支trade recap一致操作)。
- **If** 交易的失效點（invalidation，如某根關鍵蠟燭被跌破/漲破）被觸及 **then** 立即砍倉甚至反手，不留戀原方向，不必等停損被正式打到。來源(`mV-2BI64fUQ`, 2024-01-24)。
- 低時間框架進場只能配低時間框架的止盈/止損預期，不能拿1分鐘進場去賭高時間框架的最終目標。來源(`l4BvATuiDhQ`, 2024-08-12)。
- 停利設定優先看「執行時間框架高一階」的流動性目標（例如1分鐘執行則參考5分鐘的draw on liquidity）。來源(`FjSiLFrg5fo`, 2023-07-02)。
- **If** 已達成當日目標（win for the day）**then** 即使場中還有訊號也不再加碼找更多交易。來源(`-mJ8mww-Flw`, 2025-04-16)。
- **If** 盤面已實現顯著浮盈但盤整超過約2小時仍無方向 **then** 直接出場了結（即使只是保本），寧可停在獲利盤整而非虧損盤整。來源(`-rYGugTIsbU`, 2023-07-17)。
- **If** 已經在盤中確保一定獲利（如$159,000）**then** 部分獲利落袋，不讓整筆未實現盈利在盤中隨意還給市場。來源(`WIgScRUamo0`)。

### 1.4 交易時段規則 (Session/Time Rules)

- 進場前一律等待該時段的kill zone視窗（AM 9:50–10:10、PM 13:50–14:10附近）；開盤後前20-30分鐘只用來觀察價格走向draw on liquidity，不急著進場。來源(`r-7-gWZsnZc`；`L4xz2o23aPQ`, 2026-01-12)。
- 只交易New York（或London）session，避開Asian session（波動率太低）。「Asian session... I don't like waiting a whole hour for price to move five pips」(`CZRs2NuLQIw`, 2023-07-11)。
- PM session（美股午盤後段）因量能較低，改用「降一階時間框架」的相同策略（15分鐘當4小時、5分鐘當1小時、1分鐘執行），且只設一個止盈點。來源(`i3FU-9OUU90`, Day 34；`UR6vM7nPBeo`)。
- 10:30左右若已有一筆順勢單被止損在Break-even或小虧，且高時間框偏向尚未完全達成 **then** 應視為「Seek and Destroy」洗盤而非偏見失效，等更佳的第二次進場，不急著反手。來源(`p5CKu0FNbyg`)。
- 若當天大幅單邊暴衝後長時間橫盤整理(consolidate) **then** 不交易，這是他自陳2024年11月選舉週虧損的最大教訓。來源(`VMYNNP9JszI`)。

### 1.5 新聞規則 (News Rules)

- 若當日有CPI/PPI/NFP/FOMC等高影響力新聞 **then** 直接避開不交易或大幅降低倉位；PPI/中等新聞給市場消化1小時後仍可交易。來源(`fwu9FnvwnNc`, 2024-10-03；`w5sUCqFH3Lg`, Boot Camp Day 19；`6GNy02w2WIo`, 2023-10-17)。
- 若聯準會主席（Powell）當天有演講 **then** 整天不交易。來源(`ik3aIvZ4NrU`："if Powell was speaking that day I don't [f-ing] trade")。
- NFP對外匯（Forex）影響遠大於對指數（indices）的影響，可依商品類型調整是否避開。來源(`RG0j6CpCiqo`)。
- 若市場已對某新聞結果做高機率定價（如Polymarket顯示98%機率）**then** 預期新聞公布時「無大波動」（已price in）；若實際結果與市場共識相反 **then** 預期出現劇烈行情（flash crash）。來源(`7a8tAGkVJac`, 2025-10-30)。
- 「Buy the rumor, sell the news」邏輯：市場已提前反映幾乎確定的利多消息（如FOMC降息預期），消息公布當下反而容易成為賣點/流動性頂部。來源(`egQLtQLmauk`, 2025-09-17；`zSgXNr2-1Vw`)。
- 若一定要在新聞後交易，等「操縱蠟燭」走完並出現低時間框架break of structure再進場，不要在新聞爆量的第一根大K線上追價。來源(`mV-2BI64fUQ`, 2024-01-24)。

### 1.6 交易頻率規則 (Trade Frequency)

- 每天只做1-2筆交易，理想是開盤後第一筆（機率最高，因新資金入場、流動性被清掃）；之後的交易只是在「追」殘餘的回撤，風險報酬變差。來源(`4moWbfm6smw`, 2023-06-21)。
- 「少即是多」：最頂尖交易員一個月只交易幾次，而非天天交易；過度交易=不成熟訊號。「The best traders in the world are taking one to two trades per month」(`-zyDnjozaMM`, 2025-11-26)。
- 若沒有滿足全部confluence **then** 寧可不交易，"a day out of the market is better than a day in the market"。來源(`kBb_o34vhos`；`OyA49XKIK7w`；`xZ3vS4PRK0s`, 2024-01-29；`VTwmHVAX29o`；`hA9I8KsMC_U`, 2024-01-30)。
- 若某天沒有給出符合策略的訊號 **then** 完全不交易，並將「今天沒交易」視為「贏的一天」。來源(`ojErKB8wA30`："today was a great trading day if you ask me. I took zero trades")。

### 1.7 情緒/心理紀律規則

- 若當天贏錢 **then** 關掉圖表走人，研究這筆贏單為什麼贏；若輸錢 **then** 絕不追單報復性交易(revenge trade)。來源(`vlnNPFu4rEQ`, Rule #1)。
- 虧損被視為「付學費」("pay-to-play")，情緒反應應趨近於零，不追加、不報復性交易。來源(`_jLR3XcB5eQ`, 2023-06-02)。
- 若出現「想凹單/貪心/等更多確認又追進」的衝動 **then** 屬於需要事後檢討的錯誤模式。來源(`RcapWZ9xtPw`；`ppKIDXlZ4ow`)。
- 若情緒不穩（生病、宿醉、心情差、剛分手）**then** 不交易或降風險，明確列為「何時不該交易」的情境之一。來源(`kBb_o34vhos`, 2023-05-19；`NK-RsDCp4Lg`, 2022-10-31)。
- 若出現同一個錯誤第二次（over-leverage、revenge trade、移動停損）**then** 視為絕對禁止再犯的紅線。來源(`1fWcEeYpSXk`, 2024-05-22："if you over leverage once you get the consequences of it, never do it again")。
- 若剛經歷連勝週/連勝月 **then** 主動降低風險（因為預期「市場遲早會打臉」），不因近期順風而加碼。來源(`ssPMxVk6B9Y`)。
- 若已連續看對高時間框架偏見但下一筆止損被掃出 **then** 不重新追單、下車觀察，避免把風險再度攤在桌上。來源(`7We6u-TW3z4`, 2025-11-13)。
- 每筆交易（不論輸贏）都要journal記錄：pair/session/confluences/risk/是否守計畫/情緒/如何改進；贏的交易也要分析「為什麼贏」而非只慶祝。來源(`CZRs2NuLQIw`, 2023-07-11；`z9p7OThLkr4`)。

---

## 二、具體交易案例與 Track Record

> 說明：以下數字均為 TJR 本人在影片中的自我陳述（部分附Tradezella/broker截圖佐證），未經第三方驗證。日期依原始逐字稿標註的Upload Date；「無日期」代表原始批次筆記未能取得明確上傳日期。**同一事件在不同批次被不同方式轉述、或金額有出入者，已於條目中以「衝突/待核」標註，不強行統一數字。**

### 2.1 起源故事 / 核心創傷敘事（跨批反覆講述，版本略有差異）

- 核心敘事：把 $10,000 帳戶在兩天內做到 $112,000（部分版本描述為「隔天」），因未設風控/貪婪加槓桿，隨後全部虧光，觸發margin call歸零。此故事在**至少10個批次**中以幾乎相同的結構反覆出現，作為其「起源創傷」核心故事：(`AEoCaWFRXHU`；`Xq6-oO2n6-U`；`yK2tYsDZlj4`；`v_K8fOJYMt8`；`JKx476um7B0`, 2023-11-10；`7C1FxfjIC54`, 2023-02-05；`FDkqslOPL9A`, 2023-03-27；`qJap-CZoV6g`；`Q-tqgxE6Ntk`；`AUUZ9Vk6p5E`, 2022-12-12；`0J-3HBxVL08`, 2025-07-17)。
  - 版本差異：部分敘述稱資金來源是「加密貨幣部位」（`Q-tqgxE6Ntk`稱2020年COVID期間、以太坊/Solana生態相關），部分敘述未指明資金類別（外匯或指數帳戶）；發生時間點也隨影片年份推移而模糊（早期稱「幾年前」，未給精確年份）。
  - 後續影響：三個月重度憂鬱、部分版本提及「多次企圖自殺」（`Q-tqgxE6Ntk`；`5bkbEA5NxfE`, 2026-01-20首度公開約5年前有過自殺未遂經歷；`FDkqslOPL9A`, 2023-03-27，當時本人20歲）；靠DoorDash送餐維生3-4個月還債，銀行帳戶一度負$2,000。

### 2.2 按批次列出的具體損益案例（含日期與videoID）

**2023年：**
- 2023-01-06：自述曾在GBP/JPY轉為獲利，先於SPX(`WFA8zc1tJ9w`)。
- 2023-01-21：「7-1 on the week」，自稱2023年至今S&P 500日內交易未曾虧損("we have not lost a intraday S&P 500 day trade")(`OCjU-7NKaL8`)。
- 2023-01-30：整月S&P 500日內交易「undefeated」；因無學歷/收入不穩定被銀行拒發賓士車貸，需父親共同簽署(`HW6YoCcev9U`)。
- 2023-02-05：自稱1月S&P 500戰績「23 and 1」/「22-1」(`7C1FxfjIC54`)。
- 2023-02-23：單日gold+SPX+AUDUSD累積獲利約$11K+；自稱「first 100K month像一年半前一樣」(`EM7xm4YeTFc`)。
- 2023-04-19：4個月來首次虧損週，單日虧$52,360，當月僅剩獲利$4,000(`MpC4Kj_zIJU`)。
- 2023-04-20：直播虧損$3,000，宣布給Discord發$5,000等值補償空投(`YJ7YQp4Q7Gs`)。
- 2023-05：連續6.5個月無虧損週，直到某週因兩筆逆勢交易首度出現虧損週(-3.5%)(`pybufNiEg9k`)。
- 2023-05-01：GBP/JPY單筆獲利，標題「$37,000 in one trade」但內文口述「38,000」**（衝突/待核，數字未強行統一）**(`ErC2X1ZW78g`)。
- 2023-05-09：正式搬遷至波多黎各(`d2fEp015VKU`回顧)。
- 2023-05-30：GBPUSD交易獲利$26,788.86，同時宣布Discord從24/7開放改為稀缺制(`FtiU1uushnI`)。
- 2023-06-15：黃金空單原本止損位提前上移導致多損失約$4,000，最終虧損$14,197(`MP7_aNVjpUo`)。
- 2023-07-02：週交易獲利$50k案例(`FjSiLFrg5fo`)。
- 2023-07-11：SPX交易鎖定獲利$13,601，歸因於「等待第二個confluence」的紀律改善(`It4_gJjSOyY`)。
- 2023-07-28：$60,000週獲利回顧，逐筆拆解5筆交易(3勝2負)，宣布之後只做高機率交易(`ecQBZXdZOwk`)；同影片自述某筆意外冒進風險至$122,000。
- 2023-08-06：三筆SPX交易一週賺$50k(`K9Q7Xdyr_3w`)。
- 2023-08-16：兩日內合計虧損$26,000（GBPUSD+SPX），皆為「逆日線偏見交易」的檢討案例(`32BbWfoZDCw`)。
- 2023-08-25/26：GJ交易虧損$26K，另有$7.8K同日雙重虧損稱「my biggest loss」(`A9wbU6V_5g4`, 2023-05-25，日期先後略有出入)。
- 2023-10：單月獲利+$250,000，已提領$64,956；同年1月稱「整月unbeaten，連勝21筆」(`NA2equ--jc4`)。
- 2023-10-16：稱「past three weeks... 150k」，「$200 bucks off月獲利300K目標」；單日獲利$39k Nas100(`B0CWi29zJKU`)。
- 2023-10-17：正面自稱「業界第一個公開曬虧損的交易網紅」(`72w_QM9wmgg`)。
- 2023-10-24：單月獲利$269K，計畫買錶(Rolex Daytona)(`RI1ANCNy2OY`)。
- 2023-10-27：SPX交易獲利約$26K(`bQwAlwVuPbI`)。

**2024年：**
- 2024-05-17：Trading Transformation Day36系統性回測「五件套」confluence框架(`60H1AumgjG8`)。
- 2024-05-24：三筆ES空單全數獲利(3 for 3)，以5分鐘SMT背離+FVG失效為進場理由(`acZT9JP-c18`)。
- 2024-06-04：偏多但未實現，最終停損出場，仍維持週線3R正報酬(`LS-ZCr8RMDg`)。
- 2024-06-17：因未等待HTF回撤至equilibrium就在流動性掃蕩後做空NASDAQ/ES，被停損(`2VwFclgFiWs`)。
- 2024-06-24：「1K→10K一週挑戰」：頭兩次嘗試失敗（先虧約$250、再全倉虧$1,000），第三次靠一次算錯帳的烏龍加碼才驚險達標，最終週獲利$99,000+；他明確表示「不是我平常帳戶會做的事」(`72zjckQddOI`)。
- 2024-07-16：學員Josh（Mastermind 1.0畢業生）於2個月內獲利約$93,500（帳戶起始資金約$300,000）(`cX4yh9YmZqw`)。
- 2024-07-17：判斷錯誤「catch a falling knife」，NASDAQ因科技股拖累單日下跌約300點，虧損收場(`cojmRHLg0_Y`)。
- 2024-08-24：單日獲利$8,546(`OyKvg2JxdLs`)。
- 2024-08-28：另一筆單日獲利$11,209附近(`IzI10fsgx8k`)。
- 2024-09-05：單日虧損-$33,814(`-vdu9qqQfaI`)。
- 2024-09-06：標題$12,713但內文口述$112,000 **（衝突/待核，疑似轉錄錯誤）**(`BH-ALgKOf5U`)。
- 2024-09-25：單日獲利$2,211(`A3MoOMtJI_4`)。
- 2024-10-02：$44,165，稱為「my best trading day all year」(`CMsuCPOwEpI`)。
- 2024-10-10：前一日NASDAQ單日獲利約$115,000(`7NGsl8TWalQ`)。
- 2024-10-22：用$70,000一週獲利款項全額支付Mansory widebody Koenigsegg頭期款(`d07uY_sAR9c`)。
- 2024-10-28：公開檢討0-2虧損週後仍嘗試報復性交易，虧損約$2,000(`LW-Mncm1RGo`)。
- 2024-11-06：川普當選當天判斷不做空、全長倉，獲利約$9,928(`-7-oZkdB4Vs`)。
- 2024-11-19：equilibrium教學相關批次(`n97MKj6wGFk`)。

**2025年：**
- 2025-01-07：當年最大單筆交易+$56,590，過程中先在NASDAQ虧損約$9,600，隨後在S&P500以1:9風險報酬獲利(`DHQNZg3SLXg`)。
- 2025-02-04：宣稱當日交易S&P500賺得可觀利潤（標題$16,320，內文口誤提及$116,000，**衝突/待核，疑似腳本誤植**）(`-RAJEWMl-F0`)。
- 2025-02-06：因誤將4口單看成8口單，實際承擔兩倍預期風險，導致當日虧損約$112,000（標題另提及更高總損失$155,000，**衝突/待核，可能涵蓋前後兩筆**）(`57EEbYz_mcU`)。
- 2025-02-27：NASDAQ交易獲利約$5,000，公開反轉自己長期看多alt season的立場(`B5Psl0B6le0`)。
- 2025-03-04：單日獲利$25,000，週獲利$40,000，資金帳戶+$3,400(`Prxf0YiqaSI`)。
- 2025-03-10：兩筆交易，第一筆因「marrying bias」虧損約$5,000，第二筆反手做空獲利約$122,000（+$113K NASDAQ，**淨獲利敘述前後數字略有出入**）(`MzJK2-NDOhk`)。
- 2025-03-11：因NASDAQ與ES部位大小手動計算失誤，單日虧損$45,679，稱「my worst trading day of 2025」(`h-lq97cSJ00`)。
- 2025-03-15：22歲現金買下$2,000,000波多黎各豪宅；同日交易虧損$45,000(`NLRBtK0jnxQ`)。
- 2025-03-17：單月獲利宣稱$629K（當月仍在虧損$133,760的那天之後）(`KKUc45lLXT4`)。
- 2025-04-02：Miami vlog 中同一支影片內先稱「不想要物質」，後立刻反悔「Actually no. I do [bleep] with the cars and watches」(`d2fEp015VKU`)。
- 2025-04-08：提出複利試算範例（初始$5,000+每月$500，10年約$88K；初始$5,000+每月$2,000，10年約$325K）(`e4v45zQAX5c`)。
- 2025-04-10：「craziest win of the year」+$163,020，源於高波動關稅新聞行情(`Qr6nzziTQPU`)。
- 2025-04-16：單筆設置獲利$48,305(`-mJ8mww-Flw`)。
- 2025-05-09：單日先虧$59,000（三筆交易），第四筆情緒化加碼多單後反轉，最終單日+$46,180，當週+$91,000(`FQLzhkiUVlw`)。
- 2025-05-15：單日虧損$97,220：帳面浮盈約$130,000+時未移停損至保本，結果轉為大虧，事後坦承「這無論如何都是一次失誤」(`cGyQRiRbi6s`)。
- 2025-05-20：拉斯維加斯賭博：帶$25,000本金一度輸到剩約$3,000-4,000，靠21點/輪盤翻本至約$40,000盈利(`h6ZoJ9bUToU`)。
- 2025-05-26：聲稱單月獲利$291,456，使用新的「aggressive scalping strategy」(`KxBRLErkel0`)。
- 2025-06-02：黃金/等多商品「we came up and we swept out draws and liquidity to the upside」相關交易錄影(`2K8gXiyR3Jg`)。
- 2025-07-01：歐洲旅行(倫敦/巴塞隆納/伊維薩/聖特羅佩/阿姆斯特丹)，自述本趟旅行預算約$250,000(`iViDzDNnuY0`)；單日獲利$34,655。
- 2025-07-10：Tradezella儀表板顯示4-9月各月獲利$53K、$116K、$140K、(7月未詳)、$247K、$491K(`xRuMUvW3T7Q`)。
- 2025-07-17：自述從負債到23歲身家超過$2000萬(`0J-3HBxVL08`)。
- 2025-07-28：歐洲度假近一個月後首日交易即獲利逾5萬美元(`ccmUYoyzDlw`)。
- 2025-08-01：單週獲利$135,925（含單日$77,720）(`FBW9r6PeRGU`)。
- 2025-08-18：NASDAQ/ES做多，實現$22,730獲利，直接與Koenigsegg Regera（$3.5M）購車掛鉤(`nKbIHyY_iZc`)。
- 2025-08-21：單日+$153,775，明確承認「移除停損」、「revenge/impulsive」進場；前一週虧損$40,790(`scI-Pp0FL2I`)。
- 2025-09-04：自陳「been in this space for 6 years now」(`cXlVBiwIlbI`)。
- 2025-09-09：無新聞日仍實現$32,455日內獲利，月獲利宣稱達$57,827.50(`6gFHpsLlHzk`)。
- 2025-09-15：當月已虧損$25,765(`4eT-GMJ7ypc`)。
- 2025-09-17：FOMC交易日單日獲利$99,676.90，展示週獲利$349,000、月獲利$353,000(`hN_l4V6l2-s`)；同名事件另一批次記錄「stupid simple strategy」獲利$156,943.50，trade locker當月獲利$56,375(`BMyeYQIj_vU`)。
- 2025-09-18：（見上，日期相近的同一FOMC獲利事件在不同批次記錄略有差異）。
- 2025-09-19：「I AM UP 431K THIS MONTH」，同週淨賺$427,224.90(`1MHLqvC2fDE`)。
- 2025-09-22：單月獲利$446K(`NrkrUvFwTDg`)。
- 2025-09-26：單日+$47,723，月獲利宣稱$519K(`hmwTdRMUq0A`)。
- 2025-10-06：聲稱6個月內交易獲利$1,047,984（2025年4月-10月，附Tradezella核對）(`8QDDxwUV1KM`)。
- 2025-10-07：+$45,180「Max Prestige Goon」(`5RWTzr1D994`)；+$35,827「continuation trade」(`YfS5yBQgubI`)。
- 2025-10-20：全透明信任行銷影片中提及P&L公開紀錄(`2zmmjQovPdg`)。
- 2025-10-29/30：FOMC「buy rumor sell news」單日獲利約$400,000-$427,000，稱為近6-7天總計約$550,000獲利的起點；同月稍早三連敗使週虧損約$100,000、月虧損約$100,000(`MKeZTAR-VK4`；`7a8tAGkVJac`)。
- 2025-11-07：單筆虧損約$150,000(`jN7PWOEo2Rk`回顧)。
- 2025-11-10：單日獲利$133,900，「sizing up for November」(`jN7PWOEo2Rk`)。
- 2025-11-12：贈送二手Dodge Challenger Hellcat及$5,000現金給陌生夫妻（資金來源稱為賭博贏得的$10,000之一部分），同月自曝交易虧損$185,000(`ggJVKEBIWvI`)。
- 2025-11-13：前一日逆勢做多虧損約$20,000；同影片內另一日虧損$128,680(`7We6u-TW3z4`；`DieihNTCfBQ`)。
- 2025-11-17：單日最佳交易日「$317,572.90」，稱「MY BEST TRADING DAY ALL YEAR」(`IeFZ43LvjcU`)。
- 2025-11-19：Miami訪談自述，以太坊槓桿倉位因下跌約25%被強制平倉，損失逾$1,000,000(`3_mFgnF9Fok`)。
- 2025-11-20：單日虧損-$151,780，明確承認「I need to size down. It's definitely been affecting my mental」(`av3QLilFxek`)。**（衝突/待核：Batch05另記錄一支無日期影片標題「Live Day Trading Losing $152,060 (I MARRIED MR BIAS)」`xxJyvmHROb4`，因用2倍常規倉位+2倍止損（等於4倍正常風險）導致單筆巨虧，歸因為「married my bias」；此二事件金額極為接近（$151,780 vs $152,060）但videoID不同、日期歸屬不同（一為2025-11-20，一為無日期）、歸因敘事也不同（「size down」vs「married my bias」）。無法確認是否為同一事件的不同轉述、或恰好是兩次相近金額的獨立巨額虧損，故並列存查，不強行合併。）**
- 2025-12-25：自述「23 years old」，聖誕節前經歷一次「shook me up」的驚險事件(`HKuB2MT5bRM`)。
- 2025-12-27：Jake Paul vs Anthony Joshua拳賽Polymarket下注$2,000+$2,000，兩筆注皆輸(`oaWbzNRTOVk`)。

**2026年：**
- 2026-01-05：新年首筆交易，NASDAQ/S&P SMT背離+5分鐘結構破壞的「教科書級」設定進場做空，卻因委內瑞拉地緣新聞與ISM PMI意外走高導致虧損$99,500(`3o0Jf_s-06M`)。
- 2026-01-08：單日虧損$93,000，週虧損$122,000（此前還有週虧$174,000的紀錄，隨後單週反彈獲利約$130,000）(`MiaTd3hh47I`)。
- 2026-01-09：技術教學系列「Path to Profitability」發布(`4sRDnVmLcMk`)。
- 2026-01-11：SMT divergence教學影片中坦言不確定SMT縮寫全名(`7dTQA0t8SH0`)。
- 2026-01-16：直播坦承當月已虧損$220,000（交易），同一天賭博輸掉$200,000，合計「down a cumulative $400,000」；觀眾起鬨要他all-in報復，他拒絕，尾盤靠一筆空單拉回+$73,000(`7We6u-TW3z4`)。
- 2026-01-20：首度公開約5年前有過自殺未遂經歷(`5bkbEA5NxfE`)；同名批次另一影片記錄直播交易日$65,800（扣除手續費後$57K）(`WnrKJs8ePB0`)。
- 2026-01-23：直播交易，單筆停損損失$59,390，月度一度回落至下跌$50K，靠一週3勝1敗拉回月度+$15,000；同影片自曝前一年11月整月獲利$475,000，但同月內仍有單週虧$174K、單日虧$40K/$132K/$216K的紀錄(`CQg4ZVZ5Yos`)。
- 2026-01-27：單日獲利多筆展示，含$21,094(`Z2O1BEtw4Lc`, 2025-09-12另記錄相似框架)。
- 2026-02-24：自曝租借Bugatti製造假象，24歲(`gb5FPKtSNW8`, 2026-05-22另記錄)。
- 2026-03-02：直播中承認學員Tim「this is now like the third time」爆倉/違規交易(`9ar85Y6-5P4`)。
- 2026-03-13：直播記錄輔導學員Timmy的多個funded evaluation帳戶進度，臨場加碼15口合約押注剩餘evaluation帳戶。
- 2026-03-16：出金複利/資金分配教學(`JY4DK_ZLDqQ`)。
- 2026-03-17：直播片段，自稱月獲利$143K(`Prxf0YiqaSI`同批次呼應)。
- 2026-03-25：Vegas賭場輸掉約$600,000+(`juq3vRBZ_5s`)。
- 2026-04-06：$60,630單一設置獲利，發生在自己生日當天直播(`kH-rbepWkNE`)。
- 2026-04-17：單日獲利$75,210(`3SygD-YgZuQ`)。
- 2026-04-18：巴黎vlog同段內先說「美國很爛」後立刻改口「以身為美國公民為榮」(`-NI5Gz3QZy0`)。
- 2026-04-22：單日虧損$29,830，花大篇幅自證帳戶非demo(`0ic4VBvCjsM`)。
- 2026-04-23：反常人格/擁抱怪異特質心理內容(`BKEi-Jy5FbY`)。
- 2026-05-06：單週獲利$131,000、單日$63,632(`-2Mec02Mong`)。
- 2026-05-07：對酸民反擊「if you want to make money, do the opposite of TJR」(`tMFmR6UjHRk`)。
- 2026-05-22：以$30,000租24小時的Bugatti拍片(`gb5FPKtSNW8`)。
- 2026-05-29：Polymarket UFC賽事下注$10,000x2，一場贏$25,000，另一場放大押注贏$50,000，總計$75,000；宣布「TJR Island」真人秀交易競賽(`c7IYwQhZbIE`)。
- 2026-06-05：2026年1-5月合計獲利$874,782（含手續費前）；win rate 64.29%，平均賺賠比1:1.33；1月$41k、2月$148k、3月$293k、4月$230k、5月$34k（最差月），全年至今無虧損月份(`8PYgFVB0GHE`)。
- 2026-06-11：加密貨幣2025年6月投入$150萬（Hyperliquid/Zcash/Harmonic各$50萬），Zcash因協議漏洞暴跌逾60%，整體淨虧約$225,000(`MA2poJtIBZA`)。
- 2026-06-12：NBA Finals（尼克vs馬刺）Polymarket下注$40,000~$41,000，現場加倉，單場獲利$160,000(`CZMC3UNVuNs`)。
- 2026-06-19：法國飛邁阿密頭等艙（$41,000機票）途中交易虧損$65,000-$66,000，自嘲「lost $106,000 in one day」（含機票）(`MKeZTAR-VK4`)。
- 2026-07-03：St Barths度假期間邊度假邊交易，單日+$65K、+$60K、+$83K；賭場（Shuffle）單次贏得$1.6-1.7M，隨後2天內在Chrome Hearts花費約$400-500K(`0NfGO54E7T4`)。
- 2026-07-06：TradingView教學影片中痛批Fibonacci花俏工具，但承認自己使用Fibonacci retracement/Gann box(`eEg0_zc8Hxg`)。
- 2026-07-13：「You suck. Your strategy doesn't」心理教學影片(`88tyzO9CxGA`)。

### 2.2 學員/教練案例（旁證性track record）

- 學員Josh（Mastermind 1.0畢業生）：結束後2個月內獲利約$93,500，帳戶起始資金約$300,000(`cX4yh9YmZqw`, 2024-07-16)。
- 「Broke to Rich in 30 Days」真人秀式教學案例（學員Timmy）：從虧損兩年、負債$6,000到通過funded account challenge並嘗試首次payout(`TNyTn30CPVg`)。
- 學員Tim（30天訓練從虧損到拿到funded account出金的旗艦教學案例）：同一直播中承認Tim在他親自指導下仍多次爆倉/違規交易「this is now like the third time」(`9ar85Y6-5P4`, 2026-03-02；`_rUMSqAtppo`)。
- 直播中輔導學員「Timmy」的多個funded evaluation帳戶進度，"we're two good trades away from a payout"，當日Timmy遭遇兩次意外停損，最終臨場加碼15口合約押注剩餘evaluation帳戶(`kH-rbepWkNE`關聯批次, 2026-03-13附近)。

### 2.3 商業/生活方式相關的具體數字（與交易策略無直接關係，但反映其風險/金錢決策模式）

- 服飾品牌Kiltech首發（Capsule 1）：friends & family預售$14,000+Kick直播銷售$26,000，正式上線12分鐘內接單225筆，一小時累積營收$86,295(`ryCp8fR0Uf0`, 2025)。
- Kiltech另一批次：一小時內接單超過200筆，營收逾$86,000（與上條為同一或相近事件的不同轉述，數字接近但表述細節略有差異）。
- Kiltech單場快閃15分鐘內售罄，單日銷售額提及$600,000（Dubai影片）(`QWVzaGRo20w`)。
- 出售Ferrari 488 Pista打平出場（未虧損），但事後得知若多持有2個月可多賺約$150,000(`IY9NJbaNyqA`, 2023-08-28)。
- 花$500,000購買Rolls-Royce，2025年出售，理由是「危機時需要流動資金」，之後升級購入約$500-530k的Ferrari Pista，23歲(`oOIcbRDE6FU`, 2025-06-04)。
- 現金購買波多黎各$200萬房產、Brabis GLE($300k現金)、Can-Am($70k現金)、後院改裝$700k現金(`0J-3HBxVL08`)。
- 每月花費$50,000-$70,000在自我教練/課程/心態指導上(`5bkbEA5NxfE`, 2026-01-20)。
- TJR Island：2026年7月籌辦真人秀式交易競賽，10名參賽者飛到波多黎各比賽，獎金$25,000(`c7IYwQhZbIE`)。
- Trade Wars比賽：自製16人交易對抗錦標賽，每人用$11,000模擬帳戶，冠軍獎金$5,000(`xE6m4UvuT5s`)。

---

## 三、矛盾 / 立場演變（與決策規則直接相關者，按主題彙整）

> 完整的「表達DNA」「人設」相關矛盾請見 `01-writings.md` 附註；此處僅彙整與交易決策規則本身相關的立場演變，供辯論系統判斷「TJR現在的真實決策規則」時參考時序。

### 3.1 SMT背離：交易領先指數 vs 落後指數（明確反轉）
- 早期（多支2023-2024批次）：偏好交易「落後指數(lagging index)」，因其會被領先指數牽引。
- 2025-04起：「I've been favoring the non-lagging index... I changed that around... two and a half to three months ago」(`Qr6nzziTQPU`, 2025-04-10)——明確自陳策略調整，時間點約2025年初。
- 2025-09後多支批次（`4eT-GMJ7ypc`, 2025-09-15；`Q3c5E653bi8`）持續採用「favor leading/non-lagging index」的新規則。
- **結論：此為明確承認的策略轉向，非單純矛盾，判斷TJR當前決策規則時應以2025年後「偏好領先指數」為準。**

### 3.2 Order Block / Breaker Block：從必修到棄用
- 2023年Boot Camp系列（`bEkbNGUzQME`, `KtC2SbemF6w`, `ESsy0uoFAz4`）將order block、breaker block列為策略必修building block，逐一單獨教學。
- 2024-2025年多支批次（`wzq2AMsoJKY`；`_rUMSqAtppo`；`BMyeYQIj_vU`, 2025-09-17）明確棄用："Order blocks are completely useless, respectfully"；他將此包裝為「越練越簡化」的自然進化而非推翻。
- **結論：策略工具箱已瘦身，當前（2025年後）核心confluence為liquidity sweep+BOS+equilibrium/FVG，order block/breaker block已非必要。**

### 3.3 新聞日交易：從「絕對避開」到「精選介入」
- 2023-2024：「best traders in the world are avoiding days where...trade bias isn't completely set up」，CPI/PPI/NFP/FOMC一律避開(`6GNy02w2WIo`, 2023-10-17；`iolJOwIaKxQ`, 2024-03-08)。
- 2025年（尤其關稅/波動劇烈期）：「there is no better time to be a day trader than in the current market conditions... I've been upping my risk」(`Qr6nzziTQPU`, 2025-04-10)，並引入Polymarket預測市場作為輔助判斷工具，主動交易FOMC等事件（`hN_l4V6l2-s`, 2025-09-18；`n7R0zazt2Ao`, 2026-02-06）。
- **結論：新聞日規則從「一律避開」演變為「用預測市場/price-in邏輯篩選後有限度介入」，但「新聞公布當下那一刻」仍多半暫停操作。**

### 3.4 風控原則 vs 實際執行的持續落差（非單一事件，跨批反覆出現）
- 教學原則：每筆風險1-3%、絕不all-in、停損只能因交易邏輯失效而移動。
- 反覆出現的違反案例：多次「full port」(全倉不設停損)、單日虧損$151,780/$152,060等級的2倍倉位+2倍止損事件、$112,000（4口變8口計算失誤）、$97,220（浮盈未移保本後回吐）等。他在多支影片中主動承認「這是情緒化決定」("this was an emotional trading day...not something that I'm proud of")，但同類錯誤跨年份反覆出現，顯示知行落差是持續存在的模式而非單次失誤。
- **結論：教學規則本身穩定未變，但實盤執行的合規度隨帳戶規模擴大而波動，不能假設他嚴格遵守自己公開的風控規則。**

### 3.5 反訊號立場 vs 持續直播喊單
- 2023-2024年多次宣布「永久關閉Discord訊號」「re never give out signals again」(`dbF3gamgcFQ`, 2024-04-09；`0vgTPBz3htk`, 2023-12-18；`Zdk7Da8VxhA`, 2026-04-27)。
- 但同時期及其後持續每日在Kick平台直播並公開具體進場點/停損/停利，鼓勵觀眾「follow me on Kick every single morning」。
- **結論：「不再提供訊號」的宣示主要針對「付費Discord訊號房」商業模式，不代表他停止公開直播交易決策；判斷其行為模式時兩者需分開看待。**

### 3.6 demo三個月規則 vs 自身經歷
- 教學規則：demo至少3個月穩定獲利才可上真倉。
- 自述早年經歷：「would trade on demo...then after like two green days...I would jump over to a live account and then lose all my money」(`cXlVBiwIlbI`, 2025-09-04)——他自己將此列為早年犯過的錯誤，作為警示教材，而非用以反駁教學規則。

---

## 四、資料品質問題彙整（供下游Phase 2參考）

1. **大量交易案例缺乏明確上傳日期**：原始16批筆記中有相當比例的videoID標註「無日期」，尤其Batch05、06、11、15較多，導致track record時間序列有缺口，建議下游若需嚴格時間排序，優先使用有明確日期的條目。
2. **金額數字的內部衝突**：除本檔已標註的「$151,780 vs $152,060」外，另有「$37,000 vs $38,000」(`ErC2X1ZW78g`)、「標題$16,320 vs 內文口誤$116,000」(`-RAJEWMl-F0`)、「標題$12,713 vs 內文口述$112,000」(`BH-ALgKOf5U`)等口語轉錄與標題不一致的案例，均為TJR本人口播與影片標題間的落差，非研究者誤植，已在條目中並列標註。
3. **同一起源故事（$10,000→$112,000→歸零）版本細節不穩定**：資金類別（加密貨幣/外匯/指數）、具體年份、是否明確為「兩天內」翻倍等細節，在不同批次的轉述中略有出入，反映這是他反覆講述、隨時間被戲劇化調整的「品牌故事」而非精確歷史紀錄。
4. **交易資歷/年齡的自述數字持續上修**：例如「5 years trading」(2023) → 「7 years」(2024) → 「6 years」(2025-09)等，與其實際入行時間線大致吻合但精確度不足，可能是隨影片年份口語化估算而非精確計算。
5. **部分逐字稿因檔案過大無法完整讀取**（詳見各批manifest備註，如Batch01/03/06/11/12的個別超長vlog檔案），這些檔案多為純生活風格內容，對心智模型/決策啟發式的邊際貢獻經抽樣確認有限，但無法完全排除遺漏個別交易決策細節的可能性。
