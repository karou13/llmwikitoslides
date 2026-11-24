---
type: source
title_original: "The Impact of Artificial Intelligence on Denmark's Labor Market"
authors: ["Théodore Renault"]
year: 2025
source_type: 機構報告
journal: "IMF Selected Issues Papers 2025, Issue 119"
quartile: "不適用"
doi: "10.5089/9798229021647.018.A001"
raw_file: "RAW/IMF_2025_Denmark_Labor_Market_FullText.txt"
relevance: 國家現況
processing_status: 已寫入
countries: ["Denmark"]
methods: ["職業暴露度與互補度描述分析"]
ai_measure: "職業 AI 暴露度（Felten et al. 2021）與互補度（Pizzinelli et al. 2023）；企業 AI 使用率"
outcome: "高暴露低互補（工作替代風險）勞工比例"
---

# The Impact of Artificial Intelligence on Denmark's Labor Market — Renault（IMF, 2025）

> RAW 原檔為網頁全文文字檔，無 PDF 頁碼；本筆記以原文段落編號（¶）與註腳編號標示位置。

## 1. 來源
- **書目：** Renault, T. (2025). The Impact of Artificial Intelligence on Denmark's Labor Market. *IMF Selected Issues Papers*, 2025(119). International Monetary Fund. https://doi.org/10.5089/9798229021647.018.A001
- **類型：** IMF 第四條款諮商的 Selected Issues 章節（機構報告），非期刊論文，期刊分區不適用。2025 年 8 月 25 日發布。作者見註 1。

## 2. 研究目的
評估 Denmark 的 AI 準備度，並將 AI 暴露度與互補度指標對應到職業微觀資料，判斷哪些勞工群體可能受益、哪些面臨工作替代風險（¶2）。

## 3. 研究貢獻
原文未明確列出研究貢獻。內容為 IMF 對丹麥的政策分析章節，將既有的暴露度與互補度指標（Cazzaniga et al. 2024 的跨國方法）套用到丹麥（註 5）。

## 4. 研究背景
- AI 與生成式 AI 由自動化例行任務進展到執行複雜認知功能，可能重塑各技能層級與產業的工作（¶1）。
- 丹麥政府 2024 年 12 月發布 *Strategic Approach to AI*，含四項措施：成立 Digital Taskforce 推動公部門 AI、設立 Center for Artificial Intelligence in Society、發展符合丹麥規範的 AI 模型，並開放丹麥文字資料供企業使用（¶3）。此策略延續 2019 年的 *National Strategy for Artificial Intelligence*（註 2）。

## 5. 研究問題
丹麥勞工有多少比例高度暴露於 AI？其中多少屬於與 AI 互補、多少面臨替代風險？不同部門、性別、教育、所得、出生地的勞工差異為何？（¶2, ¶7）

## 6. 研究假設
原文未列研究假設。本章為描述性分析。

## 7. 樣本與研究期間
- **勞動市場分析：** 2023 年 EU Labour Force Survey 的丹麥職業微觀資料，涵蓋 119 種職業、19 個經濟活動、3 個年齡組、性別、3 個教育程度、3 個所得組、2 個出生地分組；並與其他歐洲國家比較（¶7）。
- **企業 AI 使用：** 2024 年丹麥 10 人以上企業（¶5）。原文圖 2 的資料來源未在文字檔中呈現。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| 職業 AI 暴露度 | 10 種 AI 應用對應 52 項職業能力，依各職業能力的重要性與複雜度加權（附錄 I-1） | [Felten et al.（2021）AIOE 資料](https://github.com/AIOE-Data/AIOE)，以美國 O*NET 職業特徵建構 | 「高暴露」= 暴露分數高於所有職業的中位數，屬相對而非絕對概念（註 6） | Felten et al.（2021） |
| AI 互補度 | 以 O*NET 的工作情境與 job zones，歸為溝通、責任、物理條件、關鍵性、例行性、技能六個構面（附錄 I-2） | O*NET | 以中位數為門檻分高低 | Pizzinelli et al.（2023），IMF WP 2023/216 |
| 職業分類 | 三類：高暴露高互補（HEHC）、高暴露低互補（HELC，視為較高替代風險）、低暴露（LE）（附錄 I-3） | — | — | 本章作者 |
| 職業、產業與人口特徵 | 勞工的職業、產業、年齡、性別、教育、所得、出生地（¶7） | [EU Labour Force Survey](https://ec.europa.eu/eurostat/web/microdata/european-union-labour-force-survey) 微觀資料，2023 | — | Eurostat |
| AI 準備度 | IMF AI Preparedness Index（¶4，註 3） | [IMF AIPI](https://www.imf.org/external/datamapper/datasets/AIPI) | 2023 年，174 國 | IMF（Cazzaniga et al. 2024） |
| 企業 AI 使用率 | 使用至少一種 AI 技術的 10 人以上企業比例（¶5） | 原文文字未載明來源 | 2024 年 | — |

## 9. 研究方法
- **描述性對應分析：** 將職業層級的暴露度與互補度指標對應到 EU-LFS 的丹麥勞工，計算各群體落在 HEHC、HELC、LE 三類的比例，並與北歐及其他歐洲國家比較（¶7–10，附錄 I）。
- **分類規則：** 暴露度與互補度都以所有職業的中位數為門檻（附錄 I-3）。
- 無迴歸模型或因果識別設計。

## 10. 研究結果
**AI 準備度與企業使用（¶4–6）：**
- AIPI 將 Denmark 排名全球第二（¶4）。
- 民調：78% 的受訪者認為 AI 有利於企業、55% 認為有利於社會，但只有 45% 認為有利於丹麥員工（¶4）。
- 2024 年約 25% 的 10 人以上企業使用至少一種 AI 技術，約為一年前的兩倍；主要用途為自然語言生成（18%）與文字探勘（17%）（¶5）。
- 產業：資訊通訊 70%、專業科學技術活動 45%、製造 22%、運輸 21%（¶5）。
- 企業規模：250 人以上超過 60%，50–249 人約 40%，50 人以下約 20%（¶6）。

**勞動市場暴露度（¶8–10）：**
- 超過 60% 的丹麥勞工高度暴露於 AI，與北歐國家相近，比其他歐洲國家高 9 個百分點（¶8）。
- 高暴露者中三分之二屬高互補（教學、科學工程、醫療）；三分之一屬低互補，主要為商業與行政專業人員（¶8）。
- 約 20% 的勞工屬高暴露低互補，面臨替代風險，與其他歐洲國家相近；36% 不太會受 AI 影響（¶8）。
- 民間部門約 25% 面臨替代風險，公部門約 13%（¶9）。
- 近 75% 的女性勞工高度暴露，但多數屬高互補；男性超過 50% 為低暴露（¶10）。
- 高教育與高所得者最可能受益，但其中分別約 20% 與 25% 面臨替代風險；不同年齡組差異不大；本地出生者比移民更可能受益（¶10）。

**作者解釋與政策建議（¶11–14）：**
- Denmark 已有充分準備從 AI 獲益，但仍約五分之一勞工面臨替代風險。
- 建議加速公部門 AI 採用以釋出人力、持續增加相關技能人才供給、支持中小企業數位化（SME:Digital 方案）、簡化法規負擔。

## 11. 研究限制
- 「高暴露」為相對於其他職業的概念，不是絕對暴露程度（註 6）。
- AIPI 含主觀認知指標，應視為參考性指標（註 3）。
- 作者提醒 AI 快速採用可能造成比預期更快、更大的工作替代（¶13）。
- **Wiki 註記：** 暴露度與互補度指標以美國 O*NET 職業特徵建構，套用到丹麥時假設同一職業的任務內容相同；本章為描述性分析，不估計 AI 對就業或生產力的實際影響。

## 12. 關聯
**可參考之處：**
- 提供 Denmark 的企業 AI 使用率（2024 年約 25%，依產業與規模分列）與 AIPI 排名，可放入丹麥國家頁的 AI 指標。
- 說明丹麥勞工的 AI 暴露與互補結構，可作為丹麥與其他歐洲國家差異的背景。
- 與 Danmarks Nationalbank（2026）報告的 2025 年 42% 企業採用率，可並列呈現不同年份的數字。

**不能直接套用之處：**
- 無迴歸模型，不能作為 AI 影響經濟成長的實證證據。
- 企業 AI 使用率的原始資料來源未在文字檔中載明，引用前需確認。

**相關頁面：** [BIS 1321（Gambacorta et al. 2025）](bis-gambacorta-et-al-2025.md)（同樣使用 IMF AIPI）、[Jensen & Schneider（2026）](jensen-schneider-2026.md)（丹麥企業層級研究）、[Misch et al.（2025）](misch-et-al-2025-imf.md)

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
