# TJR Raw Research Batch 16
來源：_batch_manifest_16.txt（共 50 個逐字稿，實際處理 50/50）

## 1. 心智模型候選 (candidate mental models)

- **拼圖式執行框架 (Putting the Pieces Together)**：五大 building block（liquidity sweep、break of structure、order block、fair value gap、equilibrium）按組合疊加使用，組合越多越安全、越少越risky。引用：「liquidity sweep breaker structure order block liquidity sweep breakup structure for Value Gap...along with the confirmation of price being in a discount」(`ESsy0uoFAz4`, 2023-06-25)。此框架在 `OvmbAxG15YE`(2024-03-17)「Strategy Creation pt.2」中被逐日回測驗證，是他教學體系的骨幹，跨多支影片反覆出現。

- **SMT Divergence（跨資產背離）**：兩個正相關指數（ES/NQ）中，一個提前反轉、另一個滯後，滯後指數會追隨領先指數方向。引用：「one index forecasting what another index is going to do」(`3svETDwdFUU`, 2024-05-22)；「NASDAQ is the leading index... ES will probably more than likely want to come down」(`KxBRLErkel0`, 2026-01-27)。這是2024年後新增並反覆使用（幾乎每支live trading影片都用）的核心工具，用於「建立當日偏見」與「精確進場」。

- **Higher Time Frame Holds Higher Power（高時間框架至上）**：日內判斷必須服從4H/日線趨勢，1分鐘結構反轉不能對抗高時間框架。引用：「higher time frames hold higher power...we need to be understanding the high time frames in order to understand where price wants to go」(`Z2O1BEtw4Lc`, 2025-09-12)。這是他反覆訓誡學員最核心的糾錯話術，出現在幾乎所有 trade recap 中。

- **Daily Bias 由上而下建構法**：週線定方向→日線抓市場結構→4H/1H需與日線同向才可往下切入5分鐘/15分鐘找進場。引用：「figure out where is Price going on the weekly...then scale down to the Daily...find bullish confirmation on high time frames like the four hour or the one hour」(`sjuWqKDsQtI`, 2023 boot camp)。與 `IY9NJbaNyqA`(2023-08-28)「How to find Trade Bias」互相印證，是他教學的骨架方法論。

- **反技術指標/反主流圖表工具**：明確否定trend line、channel、support/resistance，稱其為「random ass line」、「literally just a piece of art on a canvas」。引用：「trend lines...they are so vague...everybody's trend line is different」(`5dPZEeDqpbM`, 2023-09-21)。這個立場貫穿整個語料庫（跨2023-2026年份未變）。

- **Draw on Liquidity / Low Resistance Liquidity（流動性磁鐵與低阻力流動性）**：市場傾向一次掃過多個堆疊在一起的高/低點（而非只吃一個），因為可填更多訂單。引用：「it doesn't really make too much sense. It it would ideally want to take out all of them」(`KxBRLErkel0`, 2026-01-27)。與ICT的「liquidity magnet」概念高度重疊，是他挑選日內目標價位的主要邏輯。

- **Time Theory / Manipulation-Macro 時段模型**：紐約盤9:30-9:50為「操縱期」，9:50-10:10為「進場期(macro)」，10:30後若無單則收工。引用：「manipulation time frame, which is from 9:30 to 9:50...then from 9:50 really till like 10:10...that's our typical entry」(`L4xz2o23aPQ`, 2026-01-12)。這是他把ICT時段理論簡化為固定操作窗口，供學員套用。

- **Equilibrium（均衡價/折溢價）**：從高到低量出50%當作smart money買賣分界，是所有回撤交易的必要確認之一。引用：「smart money never buys in a premium smart money never never shorts in a premium they always buy and they was short in a discount」(`-E7plUbSJUk`, 2023-06-23)。此概念是他最早期（2023）教學影片的重心，之後持續作為confluence清單一員被引用。

- **風險倍增闖關法（Funded Challenge Risk Scaling）(推斷/半推斷)**：贏了維持2%風險、輸了降到1%、再贏回升到2%，藉此在1-2天內"合規地"通過資金挑戰。引用：「first trade risk two percent...if you lose that perfect risk one percent...you'll probably have already made your loss back」(`ZSJOrOeSzM0`, 2023-07-31)。這是他明確教授的機械式resizing規則，不算純心智模型但接近決策啟發式與心智模型的交界，故列於此。

## 2. 決策啟發式 (decision heuristics)

- 若在做多（空）以liquidity sweep為根據，停損永遠設在sweep高/低點之外（外加點差緩衝），因為那才是「bias失效點」。若停損設在order block/fair value gap之上會被spread打掉。來源(`1FunNCUw_jM`, 2023-07-03)。
- 若當天有多筆高影響力新聞（如CPI+PPI+就業）同一天出現，直接不交易；若新聞在盤前1小時公布，仍願意等波動出來後再判斷。來源(`6IJp02ivtb4`, 2024-03-14; `9SUJfAo6Sl8`, 2023-07-09)。
- 若market已經完成當日主要move（例如已達成SMT或流動性目標），不要在低時間框架逆勢硬做，等5分鐘級別出現retrace/確認再進場，否則會被巴出場。來源(`Z2O1BEtw4Lc`, 2025-09-12)。
- 若對某個高時間框架draw on liquidity有「強烈bias」，可用「激進進場策略」半倉位提前卡位（用1分鐘break of structure/inverse FVG/79%延伸收盤確認），保留一半風險額度給稍後更安全的5分鐘進場。來源(`KxBRLErkel0`, 2025-05-26)。
- 若當天找不到滿足全部confluence的設置，寧可不交易，「a day out of the market is better than a day in」。來源(`xZ3vS4PRK0s`, 2024-01-29)。
- 若4H與1H方向矛盾（例如日線空但4H多），視為日內尚在retrace階段，只能等更低時間框架給出與高時間框架一致的確認後才進場，不可只靠低時間框架反轉訊號單獨進場。來源(`sjuWqKDsQtI`; `Z2O1BEtw4Lc`)。
- 若價格已經觸及某個高時間框架liquidity/一次性巨大imbalance且長期未回補，優先假設它會被回補（新週/新日開盤缺口視同fair value gap），並以此作為draw on liquidity。來源(`qswlc-I-DuA`)。
- 交易員的心理帳：若第一筆虧損，第二筆降低風險比例（見上方風險倍增法）；若市場給出"免費的錢"式的明顯多重堆疊流動性，會考慮全倉/加大部位（"full port"），但仍設停損。來源(`ZSJOrOeSzM0`; `cGyQRiRbi6s`)。
- 每日先在盤前用高時間框架標出多空bias與draw on liquidity，市場開盤後才依此執行，不做臨場無根據的猜測。來源（幾乎所有daily bias/trade recap影片，例如`ch9Hjb7jF40`, `M54j_OhjMTU`）。

## 3. 表達DNA (expression DNA)

- **收尾慣用語**：幾乎每支影片固定以「I appreciate you guys/y'all/boys. I'll catch you guys in the next one. Peace out.」收尾，跨2023-2026年份高度一致（如`ESsy0uoFAz4`, `KxBRLErkel0`, `L4xz2o23aPQ`, `yd3NcU3SLSo`皆同構句尾）。
- **高頻術語堆疊唸誦**：進場前會連續唸出confluence清單像咒語，例如「liquidity sweep break of structure order block」「boom boom boom」，並用「boom」作為節奏標記詞，貫穿全部交易錄影。
- **自創/慣用術語**：
  - "ATL Hood glitch"：形容賺大錢後瘋狂消費、买豪車/珠寶的行為模式，反覆出現在多支炫富vlog中(`nmjpT6Rgw8k`, `ryCp8fR0Uf0`, `h6ZoJ9bUToU`)。
  - "mama we made it"：形容業績/事業里程碑瞬間的情緒爆發時刻，見`ryCp8fR0Uf0`（2025 Kiltech drop）。
  - "the tjr special"：自稱其標誌性設置（liquidity sweep + break of structure + fair value gap/order block）。引用：「the tjr ass e special like liquidity sweep break of structure inverse for Value Gap Confluence」(`Z2O1BEtw4Lc`, 2025-09-12)。
  - "seek and destroy"：形容市場先掃流動性再反轉延伸的固定行為模式，出現於多支2024-2025交易錄影。
- **口頭禪/贅詞**：極高頻使用「bro」「dude」「dead ass」「no cap」「simple [ __ ] man」；緊張/興奮時會連續重複同一句多達10次以上（如「please」「come on」「let's go」），見`qQYICoP3AwY`即興live trading片段。
- **確定性語氣**：對自己判斷極其武斷，常用「I already know」「this is obvious」「this is free bread」「I called today out to an absolute tea」等宣示式語言，即使事後被打臉也很快合理化（見矛盾章節）。
- **幽默方式**：大量性暗示/低俗玩笑穿插在交易講解中（例如把duck、back shots、pubic hair等比喻用在解釋candlestick/fair value gap），是他區別於傳統嚴肅交易教學者的核心風格標記，見`qswlc-I-DuA`（把fair value gap比喻成「dick and balls pattern」）。
- **透明化宣稱**：反覆強調「我公布每一筆交易的進出場與盈虧」，作為對比"詐騙"、"訊號機器人"的信任建立話術。引用：「I post literally every single trade that I take from market open to entries and exits and showing you guys P&L」(`KxBRLErkel0`, 2025-05-26)。
- **對初學者說教口吻**：教學向影片中常見「don't [ __ ] trade tomorrow if you trade you're literally stupid」式的強命令句，語氣直接近乎羞辱式激勵，貫穿boot camp系列。
- **禁忌詞規避**：無明顯禁忌詞迴避，反而以粗口為賣點；但在談論心理健康時語氣會突然轉為認真、放慢速度，形成風格反差（見`XcA0GiWZp7M`）。

## 4. 決策記錄與案例 (decisions & track record)

- 聲稱單月獲利 $291,456，使用新的「aggressive scalping strategy」，並反覆強調此策略「不是取代」原有5分鐘高時間框架策略，而是疊加用法。來源(`KxBRLErkel0`, 2025-05-26)。
- 單月獲利宣稱 $629K（當月仍在虧損 $133,760 的那天之後）。來源(`KKUc45lLXT4`, 2025-03-17)。
- 單月獲利 $269K（2023年10月），期間提及計畫月底提領並買錶（Rolex Daytona）。來源(`RI1ANCNy2OY`, 2023-10-24)。
- 單日虧損 $97,220：在獲利高點（帳面浮盈約$130,000+）時選擇不將停損移至保本，結果從獲利轉為大虧；他事後坦承「這無論如何都是一次失誤(L)」。來源(`cGyQRiRbi6s`, 2025-05-15)。
- 單週首次出現虧損週（4個月來首次），單日虧$52,360，最終當月僅剩獲利$4,000；強調對虧損週「不必太在意」。來源(`MpC4Kj_zIJU`, 2023-04-19，日期為影片標題語境，內容顯示為近期交易)。
- 單日獲利多筆展示：$21,094（「今天太簡單了」)(`Z2O1BEtw4Lc`)、$89,705(`ZX8bcxk5ZEE`)、$42,510（"如何在1分鐘圖上scalp"）(`ZioWcbxSuIw`)、$11,969(`wCJytpDXO2E`)、$11,000 vs 原損失$9,000後回補至僅虧$750的「trade recap」(`h2mMazT1kLk`似乎為另一次；獨立小片段記錄類似結果)。
- 教學案例：詳解如何用風險管理在1-2天內"合規通過"資金挑戰帳戶(prop firm funded challenge)，並批評資金挑戰公司「rules are built for you to lose」「they make no money off live account traders」。來源(`ZSJOrOeSzM0`, 2023-07-31)。
- Kiltech服飾品牌（與好友Carson共同創立）首發（Capsule 1）：friends & family預售 $14,000＋Kick直播销售 $26,000，正式上線後12分鐘內接單225筆，一小時累積營收 $86,295，用此筆收入租/買了一台Dodge Hellcat（後段揭露其實是租車搞笑橋段，但他仍實際擁有勞斯萊斯等豪車）。來源(`ryCp8fR0Uf0`, 2025)。
- 出售Ferrari 488 Pista打平出場（未虧損），但事後得知若多持有2個月可多賺約$150,000，稱「that one hurt a little bit」，並強調「I'm not here trading cars. I'm trading other [ __ ]」。來源(`IY9NJbaNyqA`, 2023-08-28)。
- 拉斯維加斯與朋友Togei賭博：帶$25,000本金，一度輸到只剩約$3,000-4,000，靠21點/輪盤翻本至最終盈利約$40,000，用以購買Chrome Hearts配件。來源(`h6ZoJ9bUToU`, 2025-05-20)。
- 擁有一台Koenigsegg（約$350萬美元），日常存放在專門的豪車倉儲，並提及過去也擁有Aventador等超跑。來源(`-NI5Gz3QZy0`, 2026-04-18)。

## 5. 矛盾 / 立場演變 (contradictions & evolution)

- **內容重心轉移**：2023年內容幾乎全是逐日拆解的boot camp教學（Building blocks、equilibrium、candle anatomy），語氣是嚴肅系統化的導師角色；到2025-2026年，內容比例明顯轉向奢侈生活/旅遊/賭博vlog（巴黎、杜拜、拉斯維加斯、邁阿密派對），交易內容比重下降，多以trade recap短片段穿插在vlog中出現。日期跨度顯示教學深度隨時間降低、娛樂化程度上升。
- **「透明」與「付費資訊」之間的自我辯護**：他公開承認「YouTube免費影片和付費課程內容其實沒有差別，付費只是讓你更願意遵守規則」("there's no difference in the information that's on YouTube compared to the information in the course... you contributed money... you're going to actually follow the rules")(`nmjpT6Rgw8k`, 2024-02-12)，但同時仍持續銷售Mastermind/Blueprint課程與付費Discord，形成"免費夠用但你應該付費"的自相矛盾商業話術。
- **批評資金挑戰(prop firm)產業「是設計來讓你輸的騙局」，卻同時大力教學生如何"擊敗"它並鼓勵購買挑戰**：「these funded account challenges...are built for you to lose...that's how these funded account funded account companies get so freaking rich」，但影片標題與內容本身就是教你買funded account並用他的策略闖關(`ZSJOrOeSzM0`, 2023-07-31)。
- **紀律教學 vs 自身違紀行為**：他反覆教導"贏了要移停損保本、按計畫執行"，但在$97,220虧損案例中，自己因為情緒("emotional")決定不移停損、放任浮盈回吐為大虧，事後坦承「Obviously it would be pretty easy for me to...say that oh I moved stops to break even, only lost $38,000. But I am not that type of person」——他用"我夠透明所以誠實揭露錯誤"為自己開脫，但錯誤本質牴觸他一貫的紀律論述(`cGyQRiRbi6s`, 2025-05-15)。
- **對美國/居住地立場出現同段內自相矛盾**：在同一支巴黎vlog中先說「the United States sucks, guys...everything there sucks」，隨後立刻改口「I'm proud to be a US citizen. However, everything else in all the other countries are just better」，顯示為修辭效果服務而非穩定立場(`-NI5Gz3QZy0`, 2026-04-18)。
- **對新策略推出時的防禦性措辭反覆出現**：每次推出「新」概念（SMT divergence、aggressive entry strategy、time theory）都會強調「這不是取代舊策略，舊的仍然有效」，顯示他察覺到觀眾/粉絲可能質疑其策略一致性、以此預先消解「又換一套說法」的批評(`KxBRLErkel0`, 2025-05-26；`3svETDwdFUU`, 2024-05-22)。

## 6. 時間線 / 背景事實 (timeline & bio)

- 2024年1月影片自述21歲(`qRRe6tj7AZI`, 2024-01-31拍攝於年初)，故推估出生年約2002-2003。
- 自述交易生涯：先經歷一輪加密貨幣週期賺錢又虧光，之後轉入日內交易，「suck ass」了約兩年才轉為穩定獲利，整體早期奮鬥期約3年（`Z2O1BEtw4Lc`, 2025-09-12回顧）。
- 曾就讀University of Utah，中途輟學；輟學前曾對高中好友Eric承諾「等特斯拉Roadster交車時要拍第一支YouTube影片」，該車最終未能如期交付，YouTube頻道延後約2.5年才正式啟動，第一支由Eric剪輯的影片內容是「在飛機上尿褲子」(`yd3NcU3SLSo`, 拉斯維加斯後續大學畢業典禮篇)。
- 自曝大學第一年（第一次獨自生活、每天只交易倫敦盤、日夜顛倒）為心理健康最低潮期，「曾多次嘗試輕生」，靠冥想與獨處學習走出低潮，此後常在影片中提倡每日30分鐘靜坐冥想作業給訂閱者(`XcA0GiWZp7M`, Boot Camp Day 51 Sunday Motivation)。
- 定居波多黎各以享受Act 60租稅優惠，同時在邁阿密保留公寓/工作室，2025年後多次考慮遷往Dorado Beach社區(`nmjpT6Rgw8k`, 2024-02-12)。
- 2025年與最好的朋友Carson共同創立服飾品牌「Kiltech」，首發（Capsule 1）銷售火爆，一小時內接單超過200筆、營收逾$8.6萬美元，此後持續推出後續系列(Capsule 2)(`ryCp8fR0Uf0`, 2025)。
- 自2024-2025年起，開始在直播平台Kick（頻道名"tjr trading"）於美股開盤前後(約8:30-9:00 am Eastern)固定直播交易與心得，作為YouTube教學內容之外的常態化管道(`3svETDwdFUU`, 2024-05-22；`L4xz2o23aPQ`, 2026-01-12)。
- 養有一隻愛犬Boogie，長期出現於vlog與交易直播背景中，是其個人品牌/形象的固定元素。
- 擁有多輛豪車包括Koenigsegg（約$350萬美元）、Rolls-Royce、曾持有並賣出Ferrari 488 Pista；2026年初vlog顯示他計畫展開歐洲行程（巴黎、倫敦等）並持續全球旅遊型內容創作。
