---
type: source
title_original: "Nonlinear Dynamics of AI Investment and Economic Growth in Germany: Evidence from a NARDL Approach"
authors: ["Seyed Alireza Athari", "Mario Edmond Sassine", "Eric Tieku Agyemang", "Dervis Kirikkaleli", "Chafic Saliba"]
year: 2026
source_type: 期刊論文
journal: "Economies"
quartile: "SJR 2025 Q2, Economics, Econometrics and Finance (miscellaneous)"
doi: "10.3390/economies14010031"
raw_file: "RAW/economies-14-00031.pdf"
relevance: 核心實證
processing_status: 已寫入
countries: ["Germany"]
methods: ["NARDL", "ARDL bounds test"]
ai_measure: "AI 投資（百萬美元，OECD AI）"
outcome: "GDP（取對數；表 2 標為 2015 年不變美元人均 GDP）"
---

# Nonlinear Dynamics of AI Investment and Economic Growth in Germany: Evidence from a NARDL Approach — Athari, Sassine, Agyemang, Kirikkaleli & Saliba（2026）

> 頁碼為 PDF 頁碼（與期刊頁碼 x of 28 相同）。

## 1. 來源
- **書目：** Athari, S. A., Sassine, M. E., Agyemang, E. T., Kirikkaleli, D., & Saliba, C. (2026). Nonlinear Dynamics of AI Investment and Economic Growth in Germany: Evidence from a NARDL Approach. *Economies*, 14(1), 31. https://doi.org/10.3390/economies14010031
- **期刊：** Economies（MDPI 出版）。同儕審查期刊（[Aims & Scope](https://www.mdpi.com/journal/economies/about)）。分區：SJR 2025 Q2，Economics, Econometrics and Finance (miscellaneous)（[SCImago](https://www.scimagojr.com/journalsearch.php?q=Economies)）。

## 2. 研究目的
在控制勞動力與固定資本形成後，檢驗德國 AI 投資對經濟成長的影響，並區分正向與負向變動的不對稱效果（p.1, 11–12）。

## 3. 研究貢獻
- 補足 AI 投資影響德國經濟成長的具體機制缺乏實證的缺口（p.10）。
- 將資本形成、勞動力與 AI 投資放在同一系統中分析，而非個別研究各變數（p.10）。

## 4. 研究背景
- 德國經濟成長放緩：2023 年實質 GDP 下降，面臨能源價格與出口競爭力問題（p.2）。
- 聯邦政府計畫至 2025 年投入 50 億歐元於 AI，其中 20 億歐元用於經濟刺激與新興技術方案（p.2）。
- 德國 Industry 4.0（2011 年起）已將 AI 與機器學習整合至製造流程，Siemens、Bosch、SAP 等企業在 2012–2017 年持續投資 AI（p.2）。
- 德國 AI 市場預估 2024–2030 年複合年成長率 28.41%，2030 年達 351.9 億美元（Statista 2024，p.3）。

## 5. 研究問題
德國 AI 投資、勞動力與固定資本形成的正向與負向變動，對經濟成長的長期影響是否不同？（p.11–12）

## 6. 研究假設
原文列出六項假設（p.11）：
- **H1a：** 固定資本形成的正向衝擊顯著提升經濟成長。
- **H1b：** 固定資本形成的負向衝擊降低經濟成長。
- **H2a：** 勞動參與的正向衝擊有利於經濟成長。
- **H2b：** 勞動參與的負向衝擊不利於經濟成長。
- **H3a：** AI 投資的正向衝擊促進經濟成長。
- **H3b：** AI 投資的負向衝擊降低經濟成長。

## 7. 樣本與研究期間
- **分析單位：** 單一國家（Germany）時間序列。
- **期間：** 2012 年第一季至 2022 年第四季，季資料（p.1, 12）。
- **期間選擇理由：** 作者稱可涵蓋景氣擴張（2009–2019 年金融危機後復甦）與危機（COVID-19、2007–2009 全球金融危機）時期（p.12）；但兩次危機中的 2007–2009 年不在 2012–2022 的樣本期間內。
- **頻率轉換：** 原文未說明各變數由年資料轉為季資料的方式。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| `LGDP` | 正文稱以 GDP 衡量經濟成長（p.12）；表 2 標為「GDP（2015 年不變美元）per capita」，取對數（p.15） | 原文寫「OECD AI 與 World Bank database」，未逐一對應各變數來源或資料集名稱（p.12） | — | Athari et al. |
| `LAI` | AI 投資，百萬美元，取對數（表 2，p.15）。作者引述 OECD 的 AI 投資定義與四類別：技能、研發、資料與設備、其他智慧財產；並寫「本研究採用教育與訓練方面的 AI 投資」（p.12） | OECD（原文寫「Organization for Economic Co-operation and Development」，未載明資料集名稱或網址）（p.12） | 原文未說明使用 OECD.AI 何項 AI 投資序列（如創投或其他）、涵蓋範圍或季化方式 | OECD |
| `LLF` | 正文定義為 15 歲以上提供勞動的人口（World Bank 定義，p.13）；表 2 標為「Labor Force（Number）」；摘要與假設寫為勞動參與（p.1, 11） | World Bank（p.12–13） | — | World Bank |
| `LGFCF` | 正文定義為固定資本形成占 GDP 百分比（p.13）；表 2 標為「Gross Fixed Capital Formation（Current USD）」（p.15） | World Bank（p.12–13） | — | World Bank |

- **原文變數定義的不一致：** GDP（總量或人均）、勞動力（人數或參與率）、固定資本形成（占 GDP % 或現值美元）在正文與表 2 的寫法不同，筆記照原文並列。
- **資料取得：** 作者聲明研究內容已包含於文章，進一步詢問可聯絡通訊作者（p.27）。

## 9. 研究方法
**NARDL 模型（式 6，p.14）：**
`ΔLGDP_t = α0 + ρ LGDP_t−1 + β1⁺ LAI⁺_t−1 + β1⁻ LAI⁻_t−1 + β2⁺ LLF⁺_t−1 + β2⁻ LLF⁻_t−1 + β3⁺ LGFCF⁺_t−1 + β3⁻ LGFCF⁻_t−1 + Σ 短期差分項 + ε_t`

| 符號 | 定義 |
|---|---|
| `LAI⁺_t`、`LAI⁻_t` | AI 投資對數值的正向累積變動 Σ max(ΔLAI, 0) 與負向累積變動 Σ min(ΔLAI, 0)（式 7–8） |
| `LLF⁺`、`LLF⁻`、`LGFCF⁺`、`LGFCF⁻` | 勞動力與固定資本形成的正負累積變動（式 9–12） |
| `β⁺`、`β⁻` | 正向與負向變動的長期係數；兩者不同即代表不對稱 |
| `ρ` | 落後一期 GDP 水準的係數，對應誤差修正 |

**分析步驟（p.12–14）：**
1. BDS 檢定：檢查序列是否獨立同分布，或存在非線性結構（表 3）。
2. 含結構斷點的 ADF 單根檢定（表 4）。
3. ARDL bounds test 檢定共整合。
4. 估計 NARDL 長期係數。
5. 殘差與穩定性檢定：Breusch–Pagan–Godfrey 異質變異、Breusch–Godfrey 序列相關、Ramsey RESET、CUSUM 與 CUSUM of squares。

**單一國家時間序列：** 無國家固定效果或面板結構；識別完全依賴德國 44 季的時間變異。

## 10. 研究結果
**原文結果：**
- **單根檢定（表 4，p.18）：** 水準值中僅 LGFCF 顯著（−7.24***，斷點 2018Q4）；LAI、LLF、LGDP 水準值不顯著，一階差分後顯著。斷點：LAI 2021Q4、LLF 2018Q3、LGDP 2019Q4。
- **Bounds test（表 5，p.20）：** F = 28.454，K = 6。
- **NARDL 長期結果（表 5，p.20）：**

| 變數 | 係數 | p 值 |
|---|---|---|
| LLF_POS | 3.987 | 0.0003 |
| LLF_NEG | −3.890 | 0.0948 |
| LGFCF_POS | 0.089 | 0.4573 |
| LGFCF_NEG | 3.484 | 0.0741 |
| LAI_POS | 0.034 | 0.0001 |
| LAI_NEG | 0.036 | 0.0006 |

- **診斷：** Breusch–Pagan–Godfrey F = 2.074（p = 0.141）；Breusch–Godfrey LM F = 2.186（p = 0.183）（表 5）。

**作者解釋：**
- AI 投資增加 1% 時，GDP 成長增加約 0.034（作者寫為「百萬美元」）；AI 投資減少的係數也為正，作者解讀為資源轉向較有效的 AI 應用或互補投資（p.20–21）。
- 正向固定資本形成變動不顯著，作者認為德國需重新定義生產性投資（p.1, 21）。
- 勞動力正向變動的效果最大，可能反映人口老化下勞動力成長的價值（p.20）。
- **Wiki 註記：** 作者以「百萬美元」解讀係數，但模型變數皆取對數，係數一般解讀為彈性；筆記照原文記錄作者的解讀。

## 11. 研究限制
作者列出（p.27）：
- AI 投資可能被低估：無形與企業內部自行開發的 AI 資產難以在國民帳中衡量，係數可能向下偏誤。
- 單一總體勞動參與率掩蓋德國勞動市場的技能差異。
- 只納入 AI、勞動力與固定資本形成，未納入數位基礎建設品質、研發支出等其他成長因素。

## 12. 關聯
**可參考之處：**
- 唯一聚焦 Germany 單一國家、以 AI 投資（而非專利）為 AI 指標的研究，可作為德國國家頁的文獻。
- 示範在國家數很少時，可改用單一國家時間序列（NARDL／ARDL bounds test）分析。
- AI 投資與專利屬不同概念，可與 Duarte、Kalai 的專利指標對照。

**套用此模型所需資料：**

| 資料 | 來源 | 取得狀態 |
|---|---|---|
| AI 投資 | OECD.AI | 原文未載明資料集，需確認是哪項 AI 投資序列、是否有季資料 |
| GDP、勞動力、固定資本形成 | [World Bank WDI](https://databank.worldbank.org/source/world-development-indicators) | 公開（年資料）；季資料來源原文未說明 |

**不能直接套用之處：**
- 樣本只有 44 季、6 個長期係數，自由度有限。
- 變數定義在正文與表格之間不一致，資料來源未逐一對應，難以重現。
- 季資料的來源與轉換方式未說明。

**相關頁面：** [Kalai et al.（2024）](kalai-becha-helali-2024.md)、[Panel ARDL](../topics/methods/panel-ardl.md)

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
