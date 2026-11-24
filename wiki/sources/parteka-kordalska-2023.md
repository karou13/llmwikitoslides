---
type: source
title_original: "Artificial intelligence and productivity: global evidence from AI patent and bibliometric data"
authors: ["Aleksandra Parteka", "Aleksandra Kordalska"]
year: 2023
source_type: 期刊論文
journal: "Technovation"
quartile: "SJR 2025 Q1, Engineering (miscellaneous)"
doi: "10.1016/j.technovation.2023.102764"
raw_file: "RAW/Parteka_Kordalska_2023_Technovation_AI_Patents_Productivity.pdf"
relevance: 核心實證
processing_status: 已寫入
countries: ["OECD", "non-OECD"]
methods: ["固定效果 OLS", "IV-GMM", "Lewbel 異質變異工具變數"]
ai_measure: "AI 專利（流量、存量）、AI 科學出版物（流量、存量），每百萬就業人口"
outcome: "勞動生產力成長率（每工時產出；穩健性改用每就業人口產出）"
---

# Artificial intelligence and productivity: global evidence from AI patent and bibliometric data — Parteka & Kordalska（2023）

> 頁碼為 PDF 頁碼（與期刊內頁相同）。

## 1. 來源
- **書目：** Parteka, A., & Kordalska, A. (2023). Artificial intelligence and productivity: global evidence from AI patent and bibliometric data. *Technovation*, 125, 102764. https://doi.org/10.1016/j.technovation.2023.102764
- **期刊：** Technovation（Elsevier 出版）。同儕審查期刊，雙盲審查（[Guide for authors](https://www.sciencedirect.com/journal/technovation/publish/guide-for-authors)）。分區：SJR 2025 Q1，Engineering (miscellaneous)（[SCImago](https://www.scimagojr.com/journalsearch.php?q=Technovation)）。

## 2. 研究目的
評估 AI 領域的技術創新（以 AI 專利與 AI 科學出版物衡量）在總體勞動生產力成長中的角色，並比較 OECD 與非 OECD 國家（p.1–2）。

## 3. 研究貢獻
- 明確聚焦 AI 技術，而非過去跨國生產力悖論文獻多用的 ICT 或機器人資料（p.2, 9）。
- 同時使用 AI 專利與 AI 文獻計量資料衡量高度無形的 AI 技術（p.2, 9）。
- 自 1980 年代中期起，比較 OECD 與非 OECD 國家，補足既有文獻多限於單一國家或工業化國家的缺口（p.2, 9）。

## 4. 研究背景
- 全球生產力成長在數位技術快速發展的同時放緩，即「現代生產力悖論」（p.1–2）。
- 文獻提出的解釋包括：
  - 衡量誤差假說：無形資產難以納入國民帳，導致產出與生產力被低估（p.4）。
  - J 曲線假說：通用目的技術需要互補投資與時間落差，生產力效果延後出現（p.4）。
  - 新點子愈來愈難找到（p.4）。
- 數位技術與生產力的既有研究多使用 ICT 或機器人資料；以 AI 為對象的研究受限於衡量困難，仍在起步（p.2, 4–5）。
- 企業層級研究發現 AI 專利與勞動生產力正相關（Damioli et al. 2021；Benassi et al. 2022）；Venturini（2022）發現 4IR 技術專利存量可解釋 32 個工業化國家 3%–8% 的生產力變動（p.5）。

## 5. 研究問題
AI 技術生產（AI 專利、AI 科學出版物）是否與國家層級的勞動生產力成長相關？OECD 與非 OECD 國家之間是否不同？（p.1–2, 7）

## 6. 研究假設
原文未編號，以下依原文檢驗的觀點整理（p.7, 9）：
- **H1：** AI 技術生產（AI 專利或 AI 專利存量）與勞動生產力成長正相關。
- **H2：** 以 AI 科學出版物衡量的 AI 技術生產，與勞動生產力成長正相關。
- **H3：** 上述關係在 OECD 國家與擴大樣本（含非 OECD 國家）中一致。

## 7. 樣本與研究期間
- **分析單位：** 國家－年。
- **資料集 1（專利）：** 35 個 OECD 國家與 23 個非 OECD 經濟體，1985–2016 年（p.5）。
- **資料集 2（出版物）：** 35 個 OECD 國家與 28 個非 OECD 國家，1998–2017 年（p.5）。
- **專利資料截止：** 專利資料可取得至 2017 年，但依 OECD 作法截至 2016 年，因 2017 年資料因公開延遲而不完整（p.5 註 7）。
- **估計樣本（各表不同）：**
  - 表 3（OECD，專利）：OLS 736 筆、34 國；IV-GMM 746 筆、33 國；專利存量外部工具變數 260 筆、16 國（p.5）。
  - 表 4（全樣本，專利）：OLS 1,046 筆、57 國（p.6）。
  - 表 6（OECD，出版物）：OLS 560 筆、35 國（p.8）。
  - 表 7（全樣本，出版物）：OLS 969 筆、63 國（p.9）。
- **平滑處理：** 以專利數或出版物數為解釋變數的迴歸，資料以 5 期移動平均平滑（p.8）。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| `Δln(Y/L)` | 勞動生產力成長率。Y 為 GDP（chained PPPs，2017 年百萬美元）；基準為每工時產出，穩健性改用每就業人口產出（p.6, 8） | [Penn World Table 10.0](https://www.rug.nl/ggdc/productivity/pwt/pwt-releases/pwt100) | — | Parteka & Kordalska |
| `Δln(K/L)` | 資本深化：資本存量（2017 年不變價格，百萬美元）對勞動的比率成長（p.6） | [PWT 10.0](https://www.rug.nl/ggdc/productivity/pwt/pwt-releases/pwt100) | — | Parteka & Kordalska |
| `ln(AI Pat/L)` | AI 專利申請數，每百萬就業人口（p.8） | [OECD Science, Technology and Patents（PATS_IPC）](https://stats.oecd.org/Index.aspx?DataSetCode=PATS_IPC)（原文引用網址，現轉至 OECD Data Explorer 首頁） | 以專利分類號加關鍵詞辨識 AI（Baruffaldi et al. 2020: 66–68）；IP5 專利家族（至少在 EPO、JPO、KIPO、USPTO、中國 SIPO 其中兩局申請）；依優先權日計年；基準依申請人居住國，穩健性依發明人居住國；分數計數；截至 2016 年（p.5） | Parteka & Kordalska |
| `ln(AIST Pat/L)` | AI 專利存量，每百萬就業人口（p.6, 8） | 同 AI 專利 | 永續盤存法：AIST_t = AI_t + (1 − δ) AIST_{t−1}；初始值 AI_t0 / (g + δ)，g 為期間平均成長率；δ = 15%（Schankerman & Pakes 1986）（p.6） | Parteka & Kordalska |
| `ln(AI Pub/L)`、`ln(AIST Pub/L)` | 經同儕審查的 AI 科學出版物數與存量，每百萬就業人口（p.6, 8） | Elsevier/Scopus，經 [AI Index 2021 公開資料](https://drive.google.com/drive/folders/1YY9rj8bGSJDLgIq09FwmF2y1k_FazJUm)（原文引用網址） | 以論文標籤、關鍵詞、出版日期、作者所屬國辨識，約 800 個 AI 關鍵詞；定義見 AI Index 2018 附錄；1998–2017（p.6 註 12） | Parteka & Kordalska |
| `ln(GI)` | 一般創新：全部專利或全部出版物，每百萬就業人口（p.8） | OECD PATS_IPC；AI Index 2021 公開資料 | 專利口徑同 AI 專利 | Parteka & Kordalska |
| `HC` | 人力資本：平均受教育年數（Barro & Lee 2013）結合教育報酬率（p.6） | [PWT 10.0](https://www.rug.nl/ggdc/productivity/pwt/pwt-releases/pwt100) | — | PWT |
| `Trade` | 貿易開放度：商品與服務進出口合計占 GDP（p.6） | [World Bank World Development Indicators](https://databank.worldbank.org/source/world-development-indicators) | — | Parteka & Kordalska |
| `RQ` | 法規品質指數（p.6） | [World Bank Worldwide Governance Indicators](https://www.worldbank.org/en/publication/worldwide-governance-indicators) | — | World Bank |
| 外部工具變數（IV ii） | 工程與技術領域 R&D 支出占比，乘上 R&D 總支出占 GDP（p.8） | OECD PATS_IPC；[OECD Main Science and Technology Indicators（MSTI）](https://stats.oecd.org/Index.aspx?DataSetCode=MSTI_PUB)（原文引用網址） | 依領域的 R&D 資料有限，樣本大幅縮小（p.8） | Parteka & Kordalska |

- **作者公開資料與程式：** [Parteka & Kordalska 資料包](https://doi.org/10.34808/rjk6-ry03)（`REPLICATION PACKAGE.zip`，Stata 格式；p.10 Data availability）。Duarte et al.（2026）的 AI 與一般創新變數即取自此資料包。

## 9. 研究方法
**模型（式 1，p.7）：**
`Δln(Y/L)_it = β0 + β1 ln(Y/L)_i,t−1 + β2 Δln(K/L)_it + β3 ln(AI/L)_it + β4 ln Z_it + μ_i + υ_t + ε_it`

| 符號 | 定義 |
|---|---|
| `Δln(Y/L)_it` | 國家 i 在 t 年的勞動生產力成長率 |
| `ln(Y/L)_i,t−1` | 前一期勞動生產力水準，代表 β 收斂機制 |
| `Δln(K/L)_it` | 資本深化 |
| `ln(AI/L)_it` | AI 技術生產：AI 專利、AI 專利存量、AI 出版物或 AI 出版物存量，每百萬就業人口，四者擇一放入 |
| `Z_it` | 控制變數：一般創新（GI）、人力資本（HC）、貿易開放度（Trade）、法規品質（RQ） |
| `μ_i`、`υ_t` | 國家固定效果、年份固定效果 |
| `β3` | 核心係數：AI 技術生產與生產力成長的關係 |

**理論基礎：** 從加總生產函數 Y = A·F(K, L) 出發，加入無形投入 U（AI 知識生產），即 Y′ = A′·F′(K, U, L)；兩邊除以 L、取對數線性化，並假設生產力成長取決於過去生產力水準（β 收斂）而得（p.7）。

**AI 變數不加落後期：** 作者說明專利與出版物本身已有公開延遲，t 期觀察到的資料實際反映較早的 AI 技術生產（p.8）。

**估計方法（p.8）：**
- 基準為固定效果 OLS，穩健標準誤（表 3 註）。
- 為處理反向因果，改用工具變數估計：
  - (i) 專利或出版物的第一期落後值（依 Damioli et al. 2021）。
  - (ii) 外部工具變數：工程與技術領域 R&D 支出占比 × R&D 總支出占 GDP。
  - (iii) 同所得組其他國家的平均專利申請數（排除本國）。
  - (iv) Lewbel（2012）異質變異工具變數。
  - (v) Lewbel 工具變數加上第一期落後值。
  - (vi) Lewbel 工具變數加上 (iii)。
- 方法 (iii)、(iv) 與 (vi) 的事後檢定未能拒絕識別不足與弱識別的虛無假設；(vi) 的結果僅列於附錄作為穩健性檢查（p.9 註 18）。
- **穩健性（p.9）：** 改用發明人歸屬的專利（表 B1–B2）；改用每就業人口生產力（表 B3）；拆成 1985–2000 與 2001–2016 兩期（表 B4）；統一為 1996–2016（表 B5）；出版物改用其他工具變數（表 B6）。

## 10. 研究結果
> 原文表註寫「*、**、*** 分別代表 1%、5%、10% 顯著水準」（表 3、表 6 註），與一般慣例相反；本筆記照原文記錄星號，不換算。

**原文結果：**
- **AI 專利，OECD（表 3，p.5）：** OLS 與 IV-GMM 估計中，AI 專利與 AI 專利存量的係數均不顯著。前一期生產力水準與生產力成長負相關（符合 β 收斂），資本深化正相關（p.8–9）。
- **AI 專利，全樣本（表 4，p.6）：** 結論與 OECD 相同。
- **加入控制變數（表 5，p.7）：** AI 專利係數仍不顯著；一般創新（GI）在 OECD 與全樣本各設定中為正且顯著。
- **AI 出版物，OECD（表 6，p.8）：** AI 出版物流量 OLS 為 0.007***；AI 出版物存量在 OLS 為 0.024***、IV-GMM 為 0.026***、外部工具變數設定為 0.024***。加入 GI 後部分設定仍顯著（0.014*、0.020**）。
- **AI 出版物，全樣本（表 7，p.9）：** AI 出版物存量在各設定中為正且顯著，例如 OLS 0.020***、IV-GMM 0.019***。
- **穩健性（p.9）：** 改變生產力衡量、專利歸屬方式、期間切分與工具變數，皆不改變主要結論。

**作者解釋：**
- AI 技術生產（尤其是專利所反映的部分）對總體生產力成長的效果微小，AI 仍屬「利基」創新現象，支持現代生產力悖論（p.1, 10）。
- 文獻計量資料可能比專利捕捉到更廣的 AI 創新類型（p.9）。
- 生產力效果可能出現在企業與產業層級，但尚未反映在總體生產力紀錄中（p.9–10）。

## 11. 研究限制
作者列出：
- AI 技術的衡量方式仍不完善，可能低估全球數位經濟（p.10）。
- 研究衡量的是 AI 技術「生產」效果，未研究以機器人安裝數或資本財貿易衡量的「採用」效果（p.2 註 5）。
- 結果須與企業層級證據合併解讀；總體分析可能看不到企業內部的生產力與學習效果（p.10）。
- 依領域的 R&D 資料有限，外部工具變數使樣本大幅縮小（p.8）。
- 部分工具變數設定未通過識別檢定（p.9 註 18）。

## 12. 關聯
**可參考之處：**
- 資料結構為「國家 × 年」面板，與本研究以國家年度資料為主的方向相同。
- 提供 AI 專利與 AI 出版物指標的完整建構方式與公開資料包，Duarte et al.（2026）即使用此資料。
- 同時呈現專利與出版物兩種代理指標結果不同：專利不顯著、出版物顯著。選擇 AI 指標會影響結論。
- 以人力資本（HC）作為控制變數，並在 IV 估計中處理反向因果。

**套用此模型所需資料：**

| 資料 | 來源 | 取得狀態 |
|---|---|---|
| AI 專利、AI 出版物、一般創新、法規品質 | [Parteka & Kordalska 資料包](https://doi.org/10.34808/rjk6-ry03) | 公開下載，涵蓋至 2016／2017 年 |
| 更新年份的 AI 專利 | OECD Data Explorer（PATS_IPC 已轉移） | 新版資料集的欄位與篩選條件尚待對照 |
| 勞動生產力、資本、人力資本 | [PWT 10.0](https://www.rug.nl/ggdc/productivity/pwt/pwt-releases/pwt100) | 公開 |
| 貿易開放度 | [World Bank WDI](https://databank.worldbank.org/source/world-development-indicators) | 公開 |

**不能直接套用之處：**
- 結果變數是勞動生產力成長，不是經濟成長或人均 GDP。
- 原文樣本為 34–63 國；若只有 Germany、Netherlands、Denmark 三國，國家與年份固定效果會吸收大部分變異，無法沿用相同估計。
- AI 專利與出版物衡量 AI 創新產出，不是企業採用率。

**相關頁面：** [Duarte et al.（2026）](duarte-freitas-simoes-2026.md)、[OECD 國家頁](../topics/countries/oecd.md)、[Panel ARDL](../topics/methods/panel-ardl.md)

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
