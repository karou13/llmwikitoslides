---
type: source
title_original: "Artificial intelligence and growth in advanced and emerging economies: short-run impact"
authors: ["Leonardo Gambacorta", "Enisse Kharroubi", "Aaron Mehrotra", "Tommaso Oliviero"]
year: 2025
source_type: 工作論文
journal: "BIS Working Papers No. 1321"
quartile: "不適用"
doi:
raw_file: "RAW/BIS_2025_AI_and_Growth_Short_Run_Impact.pdf"
relevance: 核心實證
processing_status: 已寫入
countries: ["Global (56 economies)", "Denmark"]
methods: ["Rajan–Zingales 交互作用", "OLS 固定效果"]
ai_measure: "產業生成式 AI 暴露度（AIIE）× 國家 AI 準備度（IMF AIPI）"
outcome: "產業實質附加價值成長率（2022–2023）"
---

# Artificial intelligence and growth in advanced and emerging economies: short-run impact — Gambacorta, Kharroubi, Mehrotra & Oliviero（2025）

> 頁碼一律為 PDF 頁碼（論文內頁碼 = PDF 頁碼 − 2）。

## 1. 來源
- **書目：** Gambacorta, L., Kharroubi, E., Mehrotra, A., & Oliviero, T. (2025). Artificial intelligence and growth in advanced and emerging economies: short-run impact. *BIS Working Papers*, No. 1321. Bank for International Settlements. [BIS 論文頁](https://www.bis.org/publ/work1321.htm)
- **類型：** 國際清算銀行（BIS）工作論文，非期刊論文，期刊分區不適用。2025 年 12 月 19 日發布。

## 2. 研究目的
檢驗生成式 AI 對附加價值成長的短期效果，在先進經濟體（AEs）與新興及開發中經濟體（EMDEs）之間是否不同（p.3–4）。

## 3. 研究貢獻
- 研究範圍涵蓋先進與新興經濟體；既有的生成式 AI 總體效果研究較少處理新興經濟體（p.5）。
- 作者稱本文為最早針對生成式 AI 近期成長效果及其分配意涵的跨國評估之一（p.6）。
- 方法上有別於以暴露度或多部門模型推估的研究（Cazzaniga et al. 2024；Cerutti et al. 2025），改以 Rajan–Zingales 架構檢驗產業 AI 暴露度與國家 AI 準備度的交互作用（p.7）。

## 4. 研究背景
- 主流觀點認為生成式 AI 將提升勞工生產力，並促進企業成長與創新（p.4）。
- 效果分布不均：
  - 生成式 AI 主要強化認知與知識密集的活動，實體勞動比重高的產業受影響較小。
  - 教育程度較低與年長族群的採用率偏低（p.4）。
- 企業與產業層級的生產力提升，受採用摩擦、生產網絡與法規影響，不必然加總為等量的總體成長（p.4）。
- 先進經濟體中早期採用 AI 的產業（金融、醫療、先進製造）比重較高，預期受益較多（p.4）。
- 既有研究多集中於美國，總體生產力效果的估計差距大：Acemoglu（2024）估計 TFP 每年約增加 0.07%，其他研究估計值較高（p.6–7）。

## 5. 研究問題
生成式 AI 的短期成長效果，是否因產業 AI 暴露度與國家 AI 準備度而不同？先進經濟體與新興經濟體之間是否存在差異？（p.4–5）

## 6. 研究假設
原文明確列出一項關鍵假設（p.4）；H2 依引言寫明的預期整理。
- **H1：** 生成式 AI 的成長效果由產業 AI 暴露度與國家 AI 準備度共同決定：AI 準備度較高的國家中，AI 暴露度較高的產業成長較快，即交互項 β > 0（p.4–5, 12）。
- **H2：** 先進經濟體高暴露產業的比重較高、AI 準備度也較高，受益將多於新興經濟體（p.4）。

## 7. 樣本與研究期間
- **分析單位：** 國家－產業。
- **樣本：**
  - 56 個經濟體，其中 29 個為先進經濟體，其餘為新興與開發中經濟體，分類依 BIS 標準（p.7, 10 註 4）。
  - 16 個產業，涵蓋製造業與服務業（p.7）。
- **觀測值：** 875 筆（表 1–4）。56 個經濟體 × 16 個產業應為 896 筆，原文未說明兩者差異。
- **期間：** 依變數為 2023 年相對 2022 年的實質附加價值成長率；AI 準備度受資料可得性限制，僅使用 2023 年資料（p.10–11）。
- **資料結構：** 單一期間的橫斷面資料，非面板資料。
- **涵蓋國家：** 正文可確認的國家有 Denmark（先進經濟體中 AIPI 最高，0.78）、Croatia、Greece、Luxembourg、United States、United Kingdom、Norway、Hong Kong SAR、Singapore、Nepal、Cambodia（p.10, 17–18）。完整國家名單僅見於附錄圖表，Germany 與 Netherlands 是否在樣本中尚未確認。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| `GR_VA_cj` | 國家 c、產業 j 在 2023 年相對 2022 年的實質附加價值成長率（p.11） | [ADB Multiregional Input-Output Tables](https://www.adb.org/what-we-do/data/regional-input-output-tables)（原文未附網址，此為 ADB 官方 MRIO 頁面） | 2010 年不變價格；資料庫涵蓋 62 個經濟體及「世界其他地區」（p.8–9） | Gambacorta et al. |
| `AIIE_j` | 產業生成式 AI 暴露度，以美國產業分布作為各國共同基準（p.7–8） | [Felten et al.（2021）AIOE 資料](https://github.com/AIOE-Data/AIOE)（mTurk 調查建構的 AI 應用－工作能力關聯矩陣）；[O*NET](https://www.onetcenter.org/database.html) 的職業能力重要性；[BLS OEWS](https://www.bls.gov/oes/tables.htm) 的各產業職業就業占比（WP 1179 p.11） | Aldasoro et al.（2024）四步驟建構（WP 1179 p.11）：① 10 種 AI 應用對 52 項工作能力，由調查受訪者判斷能否使用，得 0–1 關聯度；② 能力暴露度 = 各應用關聯度加總（0–10）；③ 職業暴露度（AIOE）= 能力暴露度依 O*NET 能力重要性加權平均，標準化為 0–10；④ 產業暴露度（AIIE）= 職業 AIOE 依 BLS 產業內就業占比加權平均，標準化為最高產業 = 1，NAICS 2 位碼。BIS 1321 再將 NACE 20 個部門合併為 16 個產業（p.8 註 1） | [Aldasoro et al.（2024）BIS WP 1179](https://www.bis.org/publ/work1179.htm)，以 Felten et al.（2021）為基礎 |
| `AIPI_c` | 國家 AI 準備度指數，0–1，四個構面：數位基礎建設、人力資本與勞動市場政策、創新與經濟整合、法規與倫理；迴歸中除以標準差（p.10–12） | [IMF AI Preparedness Index](https://www.imf.org/external/datamapper/datasets/AIPI)；方法說明載明「Data available upon request」（AIPINote p.1）。子指標來自 Fraser Institute、ILO、ITU、UN、UNCTAD、UPU、World Bank、WEF（AIPINote p.1, 3–4） | 2023 年資料，涵蓋 174 國；子指標以 (x − min)/(max − min) 標準化為 0–1，構面為子指標簡單平均（AIPINote p.2）。BIS 1321 寫 AIPI 為四構面「加總」（p.10），AIPINote 寫為四構面「簡單平均」（AIPINote p.2），兩者寫法不同 | IMF（Cazzaniga et al. 2024） |
| `Lagged_Share_cj` | 2022 年產業 j 占國家 c 總附加價值的比重（p.12） | ADB MRIO | — | Gambacorta et al. |
| 機器人存量（穩健性） | 每名員工的機器人存量，再除以前一期產業實質附加價值（p.14–15） | 原文未載明資料來源 | 僅 7 個產業有資料；缺值國家以人均實質 GDP 與每人網路使用者數迴歸補值；完全無資料的產業（如政府部門）填入該國各產業最小值（p.14–15） | Gambacorta et al. |

- **參考文件（已存於 `僅供參考/`）：** Aldasoro et al.（2024）BIS WP 1179；IMF AIPINote.pdf。
- **AIIE 數值取得：** WP 1179 未附資料下載說明。Felten et al.（2021）在 [GitHub](https://github.com/AIOE-Data/AIOE) 公開職業層級 AIOE、4 位碼 NAICS 產業層級 AIIE，以及生成式 AI（影像生成、語言模型）版本的 AIOE 與 AIIE；BIS 1321 使用的 2 位碼、最高產業 = 1 版本需依 WP 1179 步驟自行彙整。

## 9. 研究方法
**模型（式 1，p.11）：**
`GR_VA_cj = β (AIPI_c × AIIE_j) + γ Lagged_Share_cj + λ_j + τ_c + ε_cj`

| 符號 | 定義 |
|---|---|
| `GR_VA_cj` | 國家 c、產業 j 在 2022–2023 年的實質附加價值成長率 |
| `AIPI_c` | 國家 c 的 AI 準備度指數，除以標準差 |
| `AIIE_j` | 產業 j 的生成式 AI 暴露度，以美國數值作為各國共同基準 |
| `Lagged_Share_cj` | 2022 年產業 j 占國家 c 總附加價值的比重 |
| `λ_j` | 產業固定效果，吸收各國共通的產業因素 |
| `τ_c` | 國家固定效果，吸收同一國家內各產業共通的因素 |
| `β` | 核心係數：國家 AI 準備度提高時，高暴露產業相對低暴露產業多出的成長 |

**識別邏輯：**
- 國家固定效果吸收 AIPI 本身，產業固定效果吸收 AIIE 本身；設定 (III) 中 AIIE 的單獨效果無法估計，只能估計交互項（p.13）。
- 模型衡量的是產業之間的相對成長差異，不是 AI 對國家總體成長的絕對效果。國家層級數值是以產業估計值依產業比重加權推算而得（p.16–17）。
- 設計來自 Rajan & Zingales（1998）：原架構以美國的產業外部融資依賴度乘上各國金融發展程度；本文改為產業 AI 暴露度乘上國家 AI 準備度（p.5）。

**估計方法：**
- OLS，標準誤在國家層級群聚（表 1 註）。
- 設定 (I) 只含國家固定效果與 AIIE；(II) 加入交互項；(III) 再加入產業固定效果。
- 延伸分析：
  - AIPI 四個構面分別估計（表 2）。
  - 加入機器人存量控制變數（表 3–4）。
  - 以表 3 設定 (III) 的估計值，模擬 AIPI 增加一個標準差的國家層級效果，結果以預測增幅最低的國家（Cambodia）為基準表示（p.16–17）。

## 10. 研究結果
**原文結果：**
- **基準模型（表 1，p.13）：**

| | (I) | (II) | (III) |
|---|---|---|---|
| AI 暴露度 | 2.519* | −13.170* | — |
| AI 暴露度 × AIPI | — | 2.905** | 3.043** |
| 2022 年附加價值占比 | −0.134** | −0.160** | −0.186* |
| 觀測值 | 875 | 875 | 875 |
| R² | 0.157 | 0.160 | 0.195 |
| 產業固定效果 | 否 | 否 | 是 |
| 國家固定效果 | 是 | 是 | 是 |

- **經濟意義：** 依設定 (II) 的係數 2.905 計算，AIPI 增加一個標準差時，AI 暴露度第 10 百分位產業的成長增幅約 16.5 個百分點，第 90 百分位約 18.5 個百分點，差距約 2 個百分點（p.12）。
- **AIPI 四個構面（表 2，p.14）：** 數位基礎建設 2.942*、創新與整合 2.541*、人力資本與勞動市場政策 2.525*、法規與倫理 3.079**。各構面係數相近，以法規與倫理的顯著性最強。
- **加入機器人存量（表 3–4，p.15–16）：**
  - 交互項仍為正且顯著，設定 (III) 為 3.140**。
  - 含產業固定效果的設定中，機器人存量本身為正且顯著，設定 (III) 為 0.304***。
  - 改變缺值補值方式後主要結果不變（p.15 註 6）。

**模型推算值（非觀察值，p.17–18）：**
- 相對於 Cambodia，先進經濟體平均高約 0.6 個百分點，新興經濟體平均高約 0.4 個百分點，兩組內部差異均大。
- 先進經濟體中 Luxembourg 推算增幅最大，與其金融業比重高有關；Norway 因採礦業比重高而較小。新興經濟體中 Hong Kong SAR 與 Singapore 較大，Hong Kong 在全樣本中僅次於 Luxembourg。

**作者解釋：**
- 各國成長效果的差異來自產業暴露度、生產結構與技術準備度的不同（p.18）。
- 短期內生成式 AI 平均而言對先進經濟體較有利，可能擴大全球所得差距（p.3, 18）。

## 11. 研究限制
作者列出：
- 以美國產業 AI 暴露模式作為所有國家的共同基準，為隱含假設（p.8）。
- 僅分析短期成長，未處理長期均衡動態（p.5）。
- 結果以總附加價值衡量；換算為 TFP 或做長期跨國預測，需另建能處理總需求效果與產業間外溢的結構模型（p.18）。
- AIPI 受資料可得性限制，僅使用 2023 年（p.10）。
- 企業與產業層級效果不必然直接加總為總體效果（p.4）。

IMF 對 AIPI 的使用提醒：指數含多項主觀認知調查指標，應視為參考性指標，不宜用於排名（AIPINote p.1）。

## 12. 關聯
**可參考之處：**
- 以「國家層級變數 × 產業層級變數」的交互作用，表達 AI 效果的國家異質性。
- AIPI 的構面之一為「人力資本與勞動市場政策」，可與本研究中人力資本的角色對照（p.10, 14）。
- Denmark 在樣本中，為先進經濟體中 AIPI 最高的國家（p.10）。

**套用此模型所需資料：**

| 資料 | 來源 | 取得狀態 |
|---|---|---|
| 國家 × 產業實質附加價值 | [ADB Multiregional Input-Output Tables](https://www.adb.org/what-we-do/data/regional-input-output-tables) | 2010 年不變價格版本的下載位置尚未確認 |
| 產業 AI 暴露度 | [Felten et al. AIOE 資料](https://github.com/AIOE-Data/AIOE)（4 位碼 NAICS AIIE 與生成式 AI 版本公開）；彙整方法見 [WP 1179](https://www.bis.org/publ/work1179.htm) p.11 | 公開；BIS 使用的 2 位碼版本需自行彙整 |
| 國家 AI 準備度 | [IMF AI Preparedness Index](https://www.imf.org/external/datamapper/datasets/AIPI) | 資料頁可瀏覽；方法說明載明完整資料依申請提供 |

**不能直接套用之處：**
- 此設計的識別依賴多國之間 AIPI 的差異，原文有 56 個經濟體。若只有 Germany、Netherlands、Denmark 三國，國家層級變異只剩三個值，也無法在國家層級群聚標準誤。
- 資料僅一期，與 Duarte et al.（2026）的「國家 × 年」面板屬不同資料結構：
  - Duarte：衡量同一國家 AI 指標隨時間變動與成長的關係。
  - 本文：衡量同一年度不同國家、不同產業之間的相對成長差異。
- AIIE 衡量潛在暴露度，不是實際採用率；國家層級結果為模型推算值，不是觀察值。

**相關頁面：** [OECD 國家頁](../topics/countries/oecd.md)、[Duarte et al.（2026）](duarte-freitas-simoes-2026.md)、[產業暴露度交互作用](../topics/methods/industry-exposure-interaction.md)

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
