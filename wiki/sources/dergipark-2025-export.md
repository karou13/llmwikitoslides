---
type: source
title_original: "Artificial Intelligence and Export Performance: Insights from OECD Countries"
authors: ["Hafidha Lahmeri"]
year: 2025
source_type: 期刊論文
journal: "International Journal of Business & Economic Studies"
quartile: "SCImago 查無收錄"
doi: "10.54821/uiecd.1786964"
raw_file: "RAW/DergiPark_2025_OECD_Export_Performance.pdf"
relevance: 背景資料
processing_status: 已寫入
countries: ["OECD (15 countries)", "Germany"]
methods: ["MMQR（動差法分量迴歸）", "Westerlund 共整合"]
ai_measure: "AI 與資料新創投資（OECD）"
outcome: "商品與服務出口（占 GDP %）"
---

# Artificial Intelligence and Export Performance: Insights from OECD Countries — Lahmeri（2025）

> 頁碼為 PDF 頁碼（期刊頁碼 = PDF 頁碼 + 257）。RAW 檔名寫為 DergiPark，DergiPark 是刊登平台，作者為 Hafidha Lahmeri。

## 1. 來源
- **書目：** Lahmeri, H. (2025). Artificial intelligence and export performance: Insights from OECD countries. *International Journal of Business and Economic Studies*, 7(4), 258–271. https://doi.org/10.54821/uiecd.1786964
- **期刊：** International Journal of Business & Economic Studies（DergiPark 平台）。論文載明 2025-09-19 收稿、2025-12-26 修訂、2025-12-29 接受，類型為研究論文（p.1）；期刊同儕審查制度：查證中。分區：使用者以 SCImago 搜尋（[連結](https://www.scimagojr.com/journalsearch.php?q=International+Journal+of+Business+and+Economic+Studies)），2026-11-23 查無收錄；JCR 未查。

## 2. 研究目的
檢驗 15 個 OECD 國家中，AI 投資與 R&D 支出對出口表現的影響，以及影響是否隨出口表現高低而不同（p.1–2）。

## 3. 研究貢獻
- 文獻較少討論 AI 與 R&D 對出口的效果在高出口與中低出口國家之間是否不同（p.3）。
- 使用 MMQR 分量迴歸，檢視條件分配不同位置的效果，而非只看平均效果（p.2）。

## 4. 研究背景
- 出口表現愈來愈取決於數位化與知識型生產（p.2）。
- AI 採用需要高固定成本與組織轉型，對各國與各企業的效果可能不同（p.2）。
- R&D 投資可協助產品差異化與技術優勢（p.2）。

## 5. 研究問題
AI 投資與 R&D 支出對出口表現的影響，在出口表現低、中、高的國家之間是否不同？（p.2）

## 6. 研究假設
原文未列研究假設。

## 7. 樣本與研究期間
- **分析單位：** 國家－年。
- **國家（15 國）：** France、Greece、Spain、Germany、Italy、United Kingdom、Sweden、Norway、Canada、Belgium、Luxembourg、Portugal、Türkiye、Poland、United States（p.4）。
- **期間：** 2013–2023 年（p.4）。
- **觀測值：** 165 筆（表 6–7，p.7–8）。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| `I_Expo` | 商品與服務出口（占 GDP %）（p.5） | World Bank（原文未載明資料集） | — | World Bank |
| `AI_inv` | AI 與資料新創企業投資（p.5） | OECD（原文寫「衡量 AI 與資料生態系的投資」，未載明資料集名稱或網址） | 原文未說明是否為創投、單位或幣別 | OECD |
| `R_D` | R&D 支出（占 GDP %）（p.5） | World Bank | — | World Bank |
| `GDP` | GDP 成長（p.5） | World Bank | — | World Bank |
| `Inf` | 年通膨率（p.5） | World Bank | — | World Bank |

- **描述統計（表 1，p.5）：** I_Expo 平均 1.603（最小 1.003、最大 2.328）；AI_inv 平均 2.317；R_D 平均 3.027；GDP 平均 28.259（最大 226.0）；Inf 平均 5.471（最大 74.30）。原文未說明各變數是否取對數或其他轉換。
- **Wiki 註記：** 若 GDP 為成長率（%），平均 28.259、最大 226.0 的數值與一般 GDP 成長率範圍不符；原文未說明單位，引用前需確認。

## 9. 研究方法
**模型（式 1–2，p.4）：**
- 模型 1：`I_Expo_it = β0 + β1 AI_inv_it + β2 R_D_it + ε_it`
- 模型 2：`I_Expo_it = β0 + β1 AI_inv_it + β2 R_D_it + β3 GDP_it + β4 Inf_it + ε_it`

**MMQR（式 3，p.5）：** `Q(τ | X_it) = X_it β(τ) + δ_i + ε_it(τ)`
- Machado & Silva（2019）的動差法分量迴歸：先估計位置（location，平均效果）與尺度（scale，對波動的效果），再組合出各分量 τ 的係數。
- 估計 25、50、75、90 分位（p.5）。

**前置檢定（p.5–6）：**
- 橫斷面相依：Pesaran（2015）CD 與 CDw+，全部顯著（表 2）。
- 斜率異質性：Pesaran & Yamagata（2008），顯著（表 3）。
- 單根：Pesaran（2007）CIPS，所有變數 I(1)（表 4）。
- 共整合：Westerlund（2007）（表 5）。

## 10. 研究結果
**模型 1（表 6，p.7）：**

| | 0.25 | 0.50 | 0.75 | 0.90 |
|---|---|---|---|---|
| AI_inv（分量係數） | −0.124* | −0.168*** | −0.210*** | −0.294*** |
| R_D（分量係數） | 0.062** | 0.053 | 0.044 | 0.027 |

- 位置效果：AI_inv −0.158***；R_D 0.055（不顯著）。
- 尺度效果：AI_inv −0.060**，作者解讀為降低出口波動。

**模型 2（表 7，p.8）：**
- 位置效果：AI_inv −0.156*（10% 顯著）；R_D、GDP、Inf 不顯著。
- 尺度效果：AI_inv −0.060，不再顯著。
- 分量係數：AI_inv 在 0.25 分位為 −0.122***，0.50 為 −0.164*，0.75 為 −0.211*，0.90 為 −0.289（不顯著）。

**原文表格與文字的不一致：**
- 表 6 中 AI_inv 0.25 分位的 t 值為 −5.62，卻只標一顆星（p.7）。
- 共整合表只列統計值與 Z 值，未列 p 值（表 5，p.6）。
- 橫斷面相依的說明段落提到「SDG indicators, green bond activity」，與本文變數無關（p.5）。

**作者解釋：**
- AI 投資在短期壓抑出口表現，同時降低出口波動，具穩定作用（p.1, 7）。
- R&D 對中低出口表現國家的效果較明顯（p.1, 7）。
- 建議依各國出口表現水準設計差異化的 AI 與 R&D 政策（p.1）。

## 11. 研究限制
作者列出（p.11）：
- 只涵蓋少數 OECD 國家與 2013–2023 年，難以推論到開發中國家。
- AI 投資變數可能無法捕捉產業使用強度、企業採用速度、技術勞工等面向。
- R&D 支出無法反映創新的品質與成效。
- 國家層級資料會忽略企業與產業差異。
- 未納入匯率波動、貿易政策、全球價值鏈整合、地緣政治風險等因素。

## 12. 關聯
**可參考之處：**
- 以 OECD 的 AI 投資作為國家層級 AI 指標，與專利、出版物、企業採用率等指標不同。
- 示範在國家數少（15 國）、期間短（11 年）時，以分量迴歸檢視效果異質性。

**不能直接套用之處：**
- 結果變數是出口，不是經濟成長。
- AI 投資資料集未載明，變數單位不清楚，難以重現。

**相關頁面：** [Wagner（2025）](wagner-2025.md)、[Lo & Lee（2024）](lo-lee-2024.md)、[Athari et al.（2026）](athari-et-al-2026.md)（同樣使用 OECD AI 投資）

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
