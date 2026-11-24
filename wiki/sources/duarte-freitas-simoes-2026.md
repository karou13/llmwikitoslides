---
type: source
title_original: "Economic Growth, AI Adoption and Human Capital Across the OECD: Evidence from a Panel ARDL Model"
authors: ["Joshua Duarte", "Carina Freitas", "Marta Simões"]
year: 2026
source_type: 期刊論文
journal: "Notas Económicas"
quartile: "SJR 2025 Q4, Economics, Econometrics and Finance (miscellaneous)"
doi: "10.14195/2183-203X_61_3"
raw_file: "RAW/Notas_Economicas_OECD_Panel_ARDL.pdf"
relevance: 核心實證
processing_status: 已寫入
countries: ["OECD"]
methods: ["Panel ARDL", "Difference-GMM", "System-GMM"]
ai_measure: "AI 專利（申請人／發明人）、AI 科學出版物，每百萬就業人口"
outcome: "實質人均 GDP"
---

# Economic Growth, AI Adoption and Human Capital Across the OECD: Evidence from a Panel ARDL Model — Duarte, Freitas & Simões（2026）

> 頁碼一律為 PDF 頁碼（期刊頁碼 = PDF 頁碼 + 54）。

## 1. 來源
- **書目：** Duarte, J., Freitas, C., & Simões, M. (2026). Economic Growth, AI Adoption and Human Capital Across the OECD: Evidence from a Panel ARDL Model. *Notas Económicas*, 61, 55–92. https://doi.org/10.14195/2183-203X_61_3
- **期刊：** Notas Económicas（Imprensa da Universidade de Coimbra 出版）。同儕審查期刊，雙盲審查，兩位外部審稿人（[期刊說明頁](https://impactum-journals.uc.pt/notaseconomicas/about)）。分區：SJR 2025 Q4，Economics, Econometrics and Finance (miscellaneous)（[SCImago](https://www.scimagojr.com/journalsearch.php?q=Notas+Economicas)）。

## 2. 研究目的
- 估計 AI 採用對 OECD 國家經濟成長與生活水準的短期及長期影響。
- 檢驗 AI 的效益是否因國家人力資本程度而不同（p.6–7）。

## 3. 研究貢獻
- 從總體層級盤點 AI 採用的經濟效果，以及哪類勞動者較受益。過去證據多來自企業層級，例如 Damioli et al. 2021、Zhai & Liu 2023（p.7）。
- 把 AI 的短期效果和長期效果分開估計，補充目前很少的總體研究（p.7）。

## 4. 研究背景
- **技術進步的效益會延遲：** 技術進步是長期成長的主要來源，但效益常因調整成本和互補性投資而延後出現（p.1, 3–4）。
- **微觀證據不一致：** Bughin（2025）認為 AI 偏向高技能；Brynjolfsson, Li & Raymond（2025）發現低技能者受益較多（p.4, 7）。
- **三篇直接相關的先行研究結論不同**（表 1，p.5–6）：
  - Gonzales（2023）：165 國，GMM，正向效果，先進經濟體較強。
  - Kalai, Becha & Helali（2024）：30 個歐洲國家，PMG-ARDL，長期正向，且效果不對稱。
  - Parteka & Kordalska（2023）：35 個 OECD 國家加 28 個非 OECD 國家，固定效果 OLS 與 IV，AI 專利存量推升生產力的證據有限。

## 5. 研究問題
- AI 採用和 OECD 國家的經濟成長、生活水準，在短期與長期各有什麼關係？
- 這個關係是否因人力資本程度而不同？（p.6–7）

## 6. 研究假設
原文未編號，以下依原文寫明的預期整理（p.9–10, 32–33）：
- **H1：** AI 採用在短期正向影響經濟成長（β₃ > 0）。
- **H2：** AI 採用在長期正向影響人均所得水準（α₃ > 0）。
- **H3：** 實體資本、人力資本和一般創新在短期與長期都有正向效果。
- **H4：** AI 的效果會隨人力資本程度改變。原文給了兩種方向：
  - **H4a：** AI 和人力資本互補，交互項為正，AI 偏向高技能。
  - **H4b：** 人力資本越低，AI 的邊際效益越大，交互項為負。

## 7. 樣本與研究期間
- **分析單位：** 國家－年，年度資料，1995–2017。
- **國家數：**
  - 正文寫 35 個 OECD 國家，排除 Colombia、Costa Rica、Lithuania；國家和期間依 AI 資料可得性選定（p.7）。
  - 基準估計表（表 5）：34 國；Diff-GMM 680 筆觀測值，Sys-GMM 714 筆（p.14）。
  - 交互作用表（表 17）：35 國；Diff-GMM 700 筆，Sys-GMM 735 筆（p.35）。
  - 存量變數模型：因沒有資料，排除 Latvia（p.27）。
  - 描述統計（表 2）：每個變數 N = 805（p.8）。
- **期間對照：** Parteka & Kordalska 的專利資料截到 2016 年（Parteka p.5 註 7），出版物資料涵蓋 1998–2017（Parteka p.5）；Duarte 的研究期間寫 1995–2017。原文沒有說明兩者如何銜接，這裡不推測。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| `y` | 實質人均 GDP（2017 年不變美元 GDP ÷ 人口），成長率取 log 一階差分（p.7） | [Penn World Table 10.01](https://www.rug.nl/ggdc/productivity/pwt/pwt-releases/pwt1001) | — | Duarte et al. |
| `k` | 人均實體資本存量，2017 年不變美元（p.8） | [PWT 10.01](https://www.rug.nl/ggdc/productivity/pwt/pwt-releases/pwt1001) | — | Duarte et al. |
| `h` | 人力資本指數，由平均受教育年數和教育報酬率組成（p.8） | [PWT 10.01](https://www.rug.nl/ggdc/productivity/pwt/pwt-releases/pwt1001) | — | Duarte et al. |
| `aiAPP`、`aiINV` | AI 專利數，分別依申請人居住國、發明人居住國歸屬，每百萬就業人口（p.7） | [OECD Science, Technology and Patents（PATS_IPC）](https://stats.oecd.org/Index.aspx?DataSetCode=PATS_IPC)（Parteka 引用網址，現轉至 OECD Data Explorer 首頁） | IP5 專利家族（至少在 EPO、JPO、KIPO、USPTO、中國 SIPO 其中兩局申請）；依優先權日計年；分數計數；以分類號加關鍵詞辨識 AI（Baruffaldi et al. 2020: 66–68）；截至 2016 年（Parteka p.5） | Parteka & Kordalska（2023）；就業人口分母取自 [PWT 10.0](https://www.rug.nl/ggdc/productivity/pwt/pwt-releases/pwt100)（Parteka p.6） |
| `aiPUB` | 經同儕審查的 AI 科學出版物數，每百萬就業人口（p.7） | Elsevier/Scopus，經 [AI Index 2021 公開資料](https://drive.google.com/drive/folders/1YY9rj8bGSJDLgIq09FwmF2y1k_FazJUm)（Parteka 引用網址） | 以論文標籤、關鍵詞、出版日期、作者所屬國辨識，約 800 個關鍵詞；1998–2017（Parteka p.5–6 註 12） | Parteka & Kordalska（2023） |
| `innAPP`、`innINV`、`innPUB` | 全部專利數／全部出版物數，每百萬就業人口，控制一般創新（p.7–8） | 同 AI 專利與 AI 出版物 | 專利口徑同 AI 專利 | Parteka & Kordalska（2023） |
| AI 存量（穩健性） | 由流量依永續盤存法累計，折舊率 15%（Parteka p.6） | 同上 | — | Parteka & Kordalska（2023） |
| `rqe`（穩健性控制） | 法規品質指數 | [World Bank Worldwide Governance Indicators](https://www.worldbank.org/en/publication/worldwide-governance-indicators) | — | Duarte 取自 Parteka & Kordalska（2023）（p.18） |
| `trade`、`inds`、`g`、`inf`、`fdi`、`urban`（穩健性控制） | 貿易開放度、製造業附加價值占 GDP %、政府消費占 GDP %、CPI 通膨率、FDI 淨流入占 GDP %、都市人口 %（p.18） | [World Bank DataBank](https://databank.worldbank.org/source/world-development-indicators)（Duarte 只寫「World Bank online Databank」，未指明資料集） | — | Duarte et al. |

- **Duarte 的 AI 變數直接來源：** [Parteka & Kordalska 資料包](https://doi.org/10.34808/rjk6-ry03)（`REPLICATION PACKAGE.zip`，Stata 格式）。
- **待使用者下載放入 `僅供參考/`：** [Parteka & Kordalska 資料包](https://doi.org/10.34808/rjk6-ry03)；[Baruffaldi et al.（2020）OECD STI WP 2020/05](https://doi.org/10.1787/5f65ff7e-en)（p.66–68 AI 專利辨識規則）；[AI Index 2018 Report](https://hai.stanford.edu/sites/default/files/2020-10/AI_Index_2018_Annual_Report.pdf)（附錄：Scopus AI 關鍵詞定義）。

## 9. 研究方法
- **長期關係式：** 原為式 (1)；單根檢定後把 `log h` 改為 `Δlog h`，成為式 (3)（p.9, 11）：
  `log y_it = α0,i + α1 log k_it + α2 Δlog h_it + α3 log ai_it + α4 log inn_it + ε_it`
- **Panel ARDL 動態式（式 4）：**
  `Δlog y_it = μ_i + β1 Δlog k + β2 Δ²log h + β3 Δlog ai + β4 Δlog inn + γ log y_i,t−1 + α1 log k_i,t−1 + α2 Δlog h_i,t−1 + α3 log ai_i,t−1 + α4 log inn_i,t−1 + ε_it`
  - β 為短期效果，α 為長期效果；γ 為誤差修正項，預期為負；μ_i 為國家固定效果。
- **交互作用（式 5）：** 在長期式加入 `log h × log ai`（p.32）。
- **估計方法：**
  - Diff-GMM（Arellano & Bond 1991）與 Sys-GMM（Arellano & Bover 1995；Blundell & Bond 1998）。
  - 落後一期所得設為前定變數；AI 與一般創新設為內生變數，用 GMM 型內部工具變數。
  - Roodman collapse，工具變數數量略低於國家數（24／30）；穩健標準誤（p.12, 14）。
  - 另估固定效果模型，未附於論文（p.12）。
- **檢定：** Pesaran（2007）CIPS 單根檢定，只有 `h` 需二次差分才平穩（p.10–11）；Westerlund（2005）共整合檢定（p.11, 33）；AR(1)、AR(2)、Hansen-J（p.14）。
- **穩健性分析**（p.14–31）：落後期數最多兩期並以 BIC 比較；額外控制變數逐一加入；改用 AI 存量變數；自 1995–2005 起逐年擴大視窗檢查係數穩定性。

## 10. 研究結果
**原文結果：**
- **Diff-GMM 基準模型**（表 5，p.13–14）：
  - AI 專利（申請人）：短期 0.0639***，長期 0.0724***。
  - AI 專利（發明人）：短期 0.0547**，長期 0.0584***。
  - AI 出版物：不顯著。
  - 落後一期所得：−0.663***（申請人）、−0.592***（發明人）。
  - AR2 與 Hansen 檢定皆未拒絕虛無假設。
- **Sys-GMM 基準模型：** 三種 AI 指標皆不顯著；AR2 p 值 0.0909、0.0726，Hansen 被拒絕或接近 10%，作者提醒審慎解讀（p.12）。
- **穩健性：**
  - 加入落後期數後顯著性下降，BIC 支持基準模型（p.14）。
  - 額外控制變數不改變主要結果；政府消費占比一致為負且顯著（p.18）。
  - 改用存量：專利短期不顯著、長期仍正向顯著；出版物短期與長期皆正向顯著（Diff-GMM，p.27）。
  - 專利係數大致穩定；流量 AI 係數略降，改用存量後下降趨勢減弱（p.30–31）。
- **交互作用**（表 17，p.33–35）：12 個交互項中 9 個不顯著；Sys-GMM 專利模型短期交互項為負（申請人 −0.393*、發明人 −0.425**）；Diff-GMM 出版物模型長期交互項為正（0.108***）。

**作者解釋：**
- 以專利資料加 Diff-GMM 為偏好結果，認為 AI 已促進短期成長，長期提升生活水準，但不是在所有設定下都成立（p.1, 36）。
- 總體資料看不出 AI 明顯有利於特定技能群體，正負效果可能在加總時抵銷（p.33, 36）。
- 估計值應視為下限（p.36）。

## 11. 研究限制
作者列出：
- 受限於目前 AI 技術發展階段與可得代理指標，結論需持續重新評估（p.2）。
- 人均 GDP 只是平均值，無法反映所得分配（p.36）。
- 總體資料會掩蓋產業與企業層級的異質效果（p.33, 36）。
- 模型假設 AI 為 Hicks 中性的 TFP 提升，平均掉偏向特定要素的效果（p.9 註 1）。
- Sys-GMM 診斷檢定不理想（p.12）。

## 12. 關聯
**可參考：**
- OECD 國家面板作為基準。
- 以 AI 專利與出版物作為國家層級指標。
- Panel ARDL 拆分短長期效果，搭配 Diff-GMM 的方法先例。
- AI × 人力資本交互作用，對應本研究人力資本的角色。

**不能直接套用：**
- GMM 工具變數數量須低於國家數，三國樣本無法照搬。
- 專利與出版物衡量 AI 創新產出，不等於企業採用率。
- 資料只到 2017 年，未涵蓋生成式 AI。

**相關頁面：** [OECD 國家頁](../topics/countries/oecd.md)、[Panel ARDL](../topics/methods/panel-ardl.md)、[動態面板 GMM](../topics/methods/dynamic-panel-gmm.md)

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
