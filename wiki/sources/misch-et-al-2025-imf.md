---
type: source
title_original: "Artificial Intelligence and Productivity in Europe"
authors: ["Florian Misch", "Ben Park", "Carlo Pizzinelli", "Galen Sher"]
year: 2025
source_type: 工作論文
journal: "IMF Working Paper WP/25/67"
quartile: "不適用"
doi:
raw_file: "RAW/IMF_2025_AI_and_Productivity_in_Europe.pdf"
relevance: 方法參考
processing_status: 已寫入
countries: ["Europe (31 countries)", "Germany", "Netherlands", "Denmark"]
methods: ["Acemoglu (2024) 任務模型模擬", "Hulten 定理", "橫斷面 OLS（AI 採用率決定因素）"]
ai_measure: "任務／職業 AI 暴露度（多種文獻指標）× AI 採用率 × 勞動成本節省"
outcome: "中期累積 TFP 增幅（模擬值）"
---

# Artificial Intelligence and Productivity in Europe — Misch, Park, Pizzinelli & Sher（2025）

> 頁碼為 PDF 頁碼（論文內頁碼 = PDF 頁碼 − 2）。

## 1. 來源
- **書目：** Misch, F., Park, B., Pizzinelli, C., & Sher, G. (2025). Artificial Intelligence and Productivity in Europe. *IMF Working Paper*, WP/25/67. International Monetary Fund.
- **類型：** 國際貨幣基金（IMF）工作論文，非期刊論文，期刊分區不適用。原文說明 IMF Working Papers 為進行中的研究，觀點屬作者個人（p.2）。原文建議引用格式寫為 2024 年，編號為 WP/25/67（p.2）。

## 2. 研究目的
估計 AI 對 31 個歐洲國家中期 TFP 的影響規模，並檢視歐洲法規可能造成的抑制效果（p.5）。

## 3. 研究貢獻
- 國家涵蓋範圍、情境數量與法規分析都比既有研究廣（p.6）。
- 不自行假設 AI 暴露度，而是彙整文獻中多種任務層級 AI 暴露度估計，形成 44 個情境，量化不確定性（p.6）。
- AI 採用率以歐洲資料的迴歸估計校準，讓採用率依各國各產業的工資等條件變動（p.6）。
- 分析國家職業管制、EU AI Act 與資料隱私法規對生產力效果的影響（p.6）。

## 4. 研究背景
- 歐洲數十年來生產力成長疲弱，與美國存在生產力差距；普遍認為歐洲在 AI 發展與採用上落後美國與中國，部分原因是法規較嚴格（p.5）。
- 微觀研究發現 AI 對特定職業的生產力提升從 14%（低技能計程車司機）到 50% 以上（軟體工程師）（p.5）。
- 總體效果估計差距極大：McKinsey 與 Goldman Sachs 估計十年內 GDP 增加 7% 至 35% 以上；Acemoglu（2024）估計美國十年累積 TFP 增幅不到 0.7%（p.5）。
- 針對歐洲的研究較少：Bergeaud（2024）估計歐元區累積增幅 2.9%；Filippucci et al.（2024b）估計 G7 國家（p.5–6）。

## 5. 研究問題
AI 對歐洲各國中期 TFP 的影響有多大？各國差異來自何處？法規會使效果減少多少？（p.5–6）

## 6. 研究假設
原文未列研究假設。本文為模型模擬研究，以情境分析取代假設檢定。

## 7. 樣本與研究期間
- **國家：** 31 個歐洲國家：EU27、Iceland、Norway、Switzerland、United Kingdom（p.20）。
- **時間定義：** 模擬結果解讀為 5 年中期累積效果；Acemoglu（2024）原為 10 年（p.6 註 1, p.9）。
- **資料年份（p.20–21, 24）：**
  - 工時與國民帳：2023 年（UK 為 2019 年）。
  - 工資：EU-SILC；Netherlands 與 UK 用 2019 年 Structure of Earnings Survey。
  - AI 採用率：2023 年企業資料；工資迴歸使用 2016 年工資。
- **Netherlands 的特殊處理：** 向 Eurostat 申請荷蘭微觀資料未獲核准，改用 Eurostat 公開的 1 位碼 ISCO-08 與 NACE Rev.2 資料（p.20 註 5）。
- **AI 採用率迴歸樣本：** 30 國、11 個產業、265 筆國家－產業觀測值（表 A2 第 1 欄，p.25）。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| 職業 AI 暴露度 | 各職業中 AI 能執行的任務比例；共 44 個情境，基準為 Eloundou et al.（2024）的任務層級指標，另含 Felten et al.（2021）AIOE 第 50 與第 75 百分位門檻、Acemoglu（2025）等（附錄 2，p.21–23） | 各文獻公開指標；以美國勞工統計局（BLS）的對照表將 O*NET SOC 轉為 ISCO-08（p.21） | 3 位碼 ISCO-08；Malta、Luxembourg、Netherlands 為 1 位碼 | 各原始文獻；IMF 作者轉換 |
| 各職業工時 | 各國各產業各職業的工時（p.20） | [EU Labour Force Survey（EU-LFS）](https://ec.europa.eu/eurostat/web/microdata/european-union-labour-force-survey) 微觀資料 | 2023 年；排除農業、家戶雇主、境外組織 | Eurostat |
| 各職業工資 | 平均時薪 = 年勞動所得 ÷（週工時 × 52）（p.20） | [EU-SILC](https://ec.europa.eu/eurostat/web/microdata/european-union-statistics-on-income-and-living-conditions) 微觀資料；Netherlands 與 UK 用 Eurostat Structure of Earnings Survey 公開表（2019） | 多數國家為 2 位碼 ISCO-08 | Eurostat |
| 產業附加價值、勞動份額 | 1 位碼 NACE Rev.2 產業的附加價值與勞動報酬份額（p.20–21） | Eurostat 國民帳公開資料（原文未附資料集代碼） | 2023 年（UK 為 2019 年） | Eurostat |
| AI 採用率（迴歸依變數） | 至少使用一種 AI 技術的企業比例：文字探勘、語音辨識、自然語言生成、影像辨識、機器學習、軟體流程自動化或決策、自主機器（p.24） | Eurostat 企業 AI 使用統計（原文未附資料集代碼） | 2023 年；各國 2 位碼 NACE 產業（不含農業）；約 8% 的歐洲企業使用至少一種 AI（p.24） | Eurostat |
| 工資、勞動成本、資本成本、企業集中度、電腦使用、能源成本、人力資本（迴歸解釋變數） | 時薪（歐元）、勞動成本、5 年以上銀行放款利率、250 人以上企業比例、使用電腦企業比例、企業電價、大專學歷員工比例（表 A2 註，p.25） | 原文未逐一載明資料庫 | 工資基準為 2016 年，另以 2021 年檢查 | — |
| 受管制職業 | 各國受執照或訓練要求管制的職業（p.17） | [European Commission Regulated Professions Database](https://ec.europa.eu/growth/tools-databases/regprof/) | — | European Commission |

- 美歐工資差距（約 50%）以 OECD 資料計算（p.26 註 10），原文未載明資料集。

## 9. 研究方法
**模擬架構：Acemoglu（2024）任務模型（p.8–9）：**
- 最終財由一組固定任務生產，任務可由資本或勞動執行；AI 透過自動化與任務互補兩個管道提升生產力。
- 依 Hulten 定理，個別職業的小幅生產力提升按其占產出比重加總為總體 TFP 增幅；不捕捉創造新產業等長期結構轉變（p.8–9）。

**TFP 增幅 = 三個參數相乘（p.9）：**

| 參數 | 意義 | Acemoglu（2024）美國值 | 本文歐洲作法 |
|---|---|---|---|
| AI 暴露任務占比 | AI 能執行的任務占比（以工資總額加權） | 19.9% | 各國依職業暴露度 × 產業內各職業工資總額加權計算 |
| AI 採用率 | 暴露任務中，採用 AI 有利可圖的比例 | 23% | 以歐洲資料迴歸估計，依各國各產業工資調整 |
| 成本節省 | 採用 AI 後的總成本節省 | 勞動成本節省 27% × 勞動份額 0.535 ≈ 15% | 與 Acemoglu 相同 |

美國結果：19.9% × 23% × 15% ≈ 0.71% 中期累積 TFP 增幅（p.9）。

**AI 採用率迴歸（附錄 3 式 1，p.24）：**
`y_ij = α_i + γ_j + x_ij β + e_ij`
- `y_ij`：國家 i、產業 j 使用 AI 的企業比例（2023）；`x_ij`：工資、資本成本、集中度、數位化等；`α_i`、`γ_j`：國家、產業固定效果；OLS，標準誤依國家與產業群聚。
- 以工資係數換算：美國工資約高 50%，對應歐洲採用率低約 5 個百分點，因此歐洲平均採用率設為 18%（p.26）。

**偏好情境（p.14–15）：** 暴露度採 Eloundou et al.（2024）基準任務指標；採用率依各國各產業工資估計後整體上移，使歐洲平均為 18%（「adjusted country-sector 1」）。

**法規情境（p.17–18）：** 假設受管制職業、EU AI Act 涵蓋的「困難」與「高風險」任務、資料密集產業（NACE J、K、Q）的 AI 暴露度減半。

## 10. 研究結果
> 以下皆為模型模擬值，不是實際觀察到的生產力成長。

- **Acemoglu 基準套用至歐洲：** 歐洲約 0.8%，略高於美國；各國從約 0.5%（Romania）到接近 1%（p.10）。
- **偏好情境：** 歐洲平均中期累積 TFP 增幅約 1.1%，比 Acemoglu 美國估計高約 60%，差異幾乎全部來自較樂觀的 AI 能力假設（p.6, 15）。
- **國家差異：** 高所得國家增幅較大；Luxembourg 約 2%，接近歐洲平均兩倍、Romania 的四倍以上（p.7）。跨國差異主要來自 AI 採用率（工資）差異，其次為產業結構，職業結構影響極小（p.15–16）。
- **AI 採用率決定因素（表 A2，p.25）：** 時薪每增加 1 歐元，使用 AI 的企業比例增加 0.75 個百分點（第 1 欄）；資本成本、集中度、電腦使用、能源成本、人力資本多不顯著或不穩定。
- **法規效果（p.17–18）：** 資料隱私法規使增幅減少約 10%；EU AI Act 與國家職業管制各減少約 15%；三者合計減少超過 30%。
- **Germany、Netherlands、Denmark 的個別數值：** 只出現在圖 2–7 的圖形中，正文未列數值；正文提到 Switzerland、Norway、Denmark 的工資約為 EU 平均的兩倍（p.26）。

**作者解釋：**
- 中期而言，AI 不是提振歐洲生產力或縮小與美國差距的萬靈丹（p.7）。
- AI 效益在高所得國家較大，可能減緩歐洲內部的所得收斂（p.7, 18–19）。

## 11. 研究限制
作者列出（p.9, 19）：
- 模型只捕捉漸進式生產力變化，不含新產業、加速科研等長期結構轉變；長期效果可能更大。
- 若 AI 部署成本下降更快，採用率可能遠高於假設（Svanberg et al. 估計美國可達約 80%）。
- 勞動成本節省可能大於假設。
- 部分暴露度指標假設 AI 能力會進步，效果可能需要更久才實現。
- 不區分自動化與互補對就業與勞動生產力的不同影響，留待後續研究（p.9 註 3）。
- 假設各國同一職業的 AI 暴露度相同（p.15）。
- 法規情境為假設性，並非所有法規已在所有國家完全實施（p.18）。

## 12. 關聯
**可參考之處：**
- 樣本包含 Germany、Netherlands、Denmark，提供三國在同一框架下的模擬比較。
- 說明國家間 AI 效果差異的機制：工資驅動的採用率與產業結構。
- AI 採用率迴歸使用 Eurostat 企業 AI 使用率，是「企業 AI 採用率」的實際資料來源，可與專利、投資等指標對照。

**套用此方法所需資料：**

| 資料 | 來源 | 取得狀態 |
|---|---|---|
| 企業 AI 使用率（國家 × 產業） | Eurostat 企業 AI 使用統計 | 公開；資料集代碼待確認 |
| 職業工時與工資 | [EU-LFS](https://ec.europa.eu/eurostat/web/microdata/european-union-labour-force-survey)、[EU-SILC](https://ec.europa.eu/eurostat/web/microdata/european-union-statistics-on-income-and-living-conditions) | 微觀資料需申請；Netherlands 申請未獲核准 |
| 職業 AI 暴露度 | Eloundou et al.（2024）、[Felten et al. AIOE](https://github.com/AIOE-Data/AIOE) 等 | 公開 |

**不能直接套用之處：**
- 結果是模擬值，不是迴歸估計的實際效果，不能作為 AI 影響成長的實證證據。
- 結果變數為 TFP，不是 GDP 成長。
- Netherlands 使用較粗的 1 位碼資料，三國之間的精細程度不同。

**相關頁面：** [BIS 1321（Gambacorta et al. 2025）](bis-gambacorta-et-al-2025.md)（同樣強調產業結構與準備度造成國家差異）、[OECD 國家頁](../topics/countries/oecd.md)

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
