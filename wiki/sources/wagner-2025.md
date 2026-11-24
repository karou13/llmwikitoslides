---
type: source
title_original: "Big Data Analytics and Exports—Evidence for Manufacturing Firms from 27 EU Countries"
authors: ["Joachim Wagner"]
year: 2025
source_type: 期刊論文
journal: "Open Economies Review"
quartile: "SJR 2025 Q3, Economics and Econometrics"
doi: "10.1007/s11079-024-09777-2"
raw_file: "RAW/s11079-024-09777-2.pdf"
relevance: 背景資料
processing_status: 已寫入
countries: ["EU27", "Germany", "Netherlands", "Denmark"]
methods: ["Probit（平均邊際效果）", "OLS"]
ai_measure: "企業是否導入大數據分析（含資料探勘、預測分析）"
outcome: "是否出口、出口目的地、出口目的地數量"
---

# Big Data Analytics and Exports—Evidence for Manufacturing Firms from 27 EU Countries — Wagner（2025）

> 頁碼為 PDF 頁碼（期刊頁碼 = PDF 頁碼 + 824）。

## 1. 來源
- **書目：** Wagner, J. (2025). Big Data Analytics and Exports—Evidence for Manufacturing Firms from 27 EU Countries. *Open Economies Review*, 36, 825–834. https://doi.org/10.1007/s11079-024-09777-2（2024 年 6 月 22 日線上發表）
- **期刊：** Open Economies Review（Springer 出版）。期刊說明頁未查到同儕審查的明文；論文致謝兩位匿名審稿人（p.10），標示為 Original Research（p.1）。分區：SJR 2025 Q3，Economics and Econometrics（[SCImago](https://www.scimagojr.com/journalsearch.php?q=Open+Economies+Review)）。

## 2. 研究目的
檢驗 EU27 製造業企業使用大數據分析與出口活動之間的關係（p.1–2）。

## 3. 研究貢獻
- 作者以 Google Scholar 檢索確認，Flash Eurobarometer 486 資料過去未被用來研究出口與大數據分析的關係（p.3 註 2）。
- 回應 Goldfarb & Trefler（2018）指出 AI 的國際面向仍少有研究的缺口（p.1–2）。

## 4. 研究背景
- AI、雲端運算、機器人與大數據分析等數位技術日益普及，但對企業績效各面向的實證證據仍不足（p.1）。
- 作者預期大數據分析透過兩個管道與出口正相關（p.2）：
  - 降低生產成本、提高生產力；文獻顯示生產力與出口正相關。
  - 降低貿易成本，例如以資料探勘與預測分析更快、更便宜地研究國外市場。

## 5. 研究問題
使用大數據分析的製造業企業，是否更常出口、更常出口到各區域，且出口到更多目的地？（p.2, 5）

## 6. 研究假設
原文未編號，以下依作者寫明的預期整理（p.2）：
- **H1：** 使用大數據分析的企業與出口活動正相關。

## 7. 樣本與研究期間
- **分析單位：** 企業，單一橫斷面。
- **調查時間：** 2020 年 2–5 月；出口資料指 2019 年（p.3）。
- **樣本：** EU27 國家的製造業（NACE C）企業 2,355 家；不含 UK（p.3）。
- **各國樣本數（附錄，p.9）：** Germany 74 家、Denmark 75 家、Netherlands 55 家。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| Big Data Analytics | 企業是否導入大數據分析（如資料探勘、預測分析），問卷 Q23_5（p.3） | Flash Eurobarometer 486，可於 [GESIS Eurobarometer Data Service](https://www.gesis.org/en/eurobarometer-data-service) 註冊後免費下載（p.10；原文網址寫為 www.gesis/eurobarometer） | 製造業企業 | European Commission |
| Exporter | 2019 年是否出口商品，Q11_1（p.3） | 同上 | — | — |
| 出口目的地 | 是否出口到 EU、其他歐洲、北美、拉美、中國、其他亞太、中東與非洲，Q11_2–Q11_8（p.4） | 同上 | — | — |
| 出口目的地數量 | 上述七個目的地的出口數（0–7）（p.4） | 同上 | — | Wagner |
| 控制變數 | 企業年齡（Q1）、員工數（不含業主，Q2A）、是否有專利或專利申請中（Q9_6）、國家虛擬變數（p.4–5） | 同上 | 資料無細產業分類，無法控制產業（p.5 註 4） | — |

- 作者表示 Stata 程式可向作者索取（p.10）。

## 9. 研究方法
**模型（p.5–6）：**
- 出口與否、各目的地出口（二元）：Probit
  `Indicator_i = a + β BigDataAnalytics_i + c Control_i + e_i`（式 2）
  大數據分析溢價 = 大數據分析虛擬變數的平均邊際效果。
- 出口目的地數量：OLS
  `number_i = a + β BigDataAnalytics_i + c Control_i + e_i`（式 3）
  標準誤在 27 國層級群聚（表 5 註）。
- 方法改編自 Bernard & Jensen（1995, 1999）的「出口商溢價」設計，改為比較使用與不使用大數據分析的企業（p.5）。

## 10. 研究結果
- **描述統計（表 1，p.3）：** 13.8% 的企業使用大數據分析；64.5% 為出口商；平均出口目的地 1.544 個。
- **各國大數據分析使用率（附錄，p.9）：** Germany 5.41%、Netherlands 16.36%、Denmark 21.33%；最低 Italy 4.70%，最高 Belgium 25.92%。
- **出口與否（表 3，p.6）：** 大數據分析 Probit 係數 0.386，平均邊際效果 0.122（t = 4.52）。
- **各目的地（表 4，p.7）：** 平均邊際效果介於 0.095（北美）到 0.163（其他歐洲）。
- **出口目的地數量（表 5，p.8）：** OLS 係數 0.717（t = 5.69），R² = 0.278。
- **原文數字不一致：** 內文寫目的地數量差異為 +0.701（p.6），表 5 為 0.717（p.8）。

**作者解釋：** 大數據分析與出口的各項指標皆有大且顯著的正相關，但無法判斷是出口企業自我選擇使用大數據分析，還是大數據分析造成出口增加（p.8–9）。

## 11. 研究限制
作者列出（p.8–9）：
- 橫斷面資料無法區分自我選擇與因果效果；需要多年、且有足夠企業轉換使用狀態的追蹤資料，作者表示目前沒有這類資料。
- 只衡量出口的廣延邊際（是否出口、出口到哪裡），沒有出口占營收比重等密集邊際資料（p.3 註 2）。
- 資料無細產業分類，無法控制製造業內部的產業差異（p.5 註 4）。

## 12. 關聯
**可參考之處：**
- 提供 Germany、Netherlands、Denmark 製造業企業的大數據分析使用率（2020 年調查），三國差異明顯（5.41%、16.36%、21.33%）。
- 文獻蒐集總覽將此篇列為出口與數位技術的參考，可作為 AI／數位技術影響國際貿易管道的背景。

**不能直接套用之處：**
- 技術是大數據分析，不是 AI；結果是出口，不是經濟成長。
- 單一年度橫斷面、企業層級，各國樣本只有 55–75 家，國別比率的精確度有限。
- 不能做因果解讀。

**相關頁面：** [Lo & Lee（2024）](lo-lee-2024.md)、[DergiPark（2025）](dergipark-2025-export.md)（同屬 AI／數位技術與貿易）

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
