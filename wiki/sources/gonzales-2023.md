---
type: source
title_original: "Implications of AI innovation on economic growth: a panel data study"
authors: ["Julius Tan Gonzales"]
year: 2023
source_type: 期刊論文
journal: "Journal of Economic Structures"
quartile: "SJR 2025 Q2, Economics, Econometrics and Finance (miscellaneous)"
doi: "10.1186/s40008-023-00307-w"
raw_file: "RAW/s40008-023-00307-w.pdf"
relevance: 核心實證
processing_status: 已寫入
countries: ["Global（最多 122 國，依設定而異）"]
methods: ["Pooled OLS", "固定效果（含時間虛擬變數）", "Anderson–Hsiao", "GMM", "FE-IV"]
ai_measure: "AI 專利數，每百萬人（Google Patents 全文關鍵詞檢索），取對數"
outcome: "人均實質 GDP 成長率（5 年平均；短期分析改用年度）"
---

# Implications of AI innovation on economic growth: a panel data study — Gonzales（2023）

> 頁碼為 PDF 頁碼（與期刊「Page x of 37」相同）。

## 1. 來源
- **書目：** Gonzales, J. T. (2023). Implications of AI innovation on economic growth: a panel data study. *Journal of Economic Structures*, 12, 13. https://doi.org/10.1186/s40008-023-00307-w
- **期刊：** Journal of Economic Structures（Springer Nature／SpringerOpen 出版）。同儕審查期刊（[Aims and scope](https://link.springer.com/journal/40008/aims-and-scope)）。分區：SJR 2025 Q2，Economics, Econometrics and Finance (miscellaneous)（[SCImago](https://www.scimagojr.com/journalsearch.php?q=Journal+of+Economic+Structures)）。開放取用，CC BY 4.0（p.1）。

## 2. 研究目的
估計 AI 對經濟的整體影響，特別是 AI 創新與長期經濟成長的關係（p.1）。

## 3. 研究貢獻
- 延續以專利、期刊論文、網路普及等衡量技術並研究成長的文獻，但聚焦於 AI 這種較新的技術（p.2）。
- 以 Google Patents 全文檢索自行辨識 AI 專利，建立 1970–2019 年的跨國 AI 專利資料（p.11）。
- 以專利引用的非專利文獻（NPL）作為 AI 專利的外部工具變數（p.20–24）。

## 4. 研究背景
- 內生成長理論把技術視為生產與知識累積的結果（Arrow 1962；Romer 1990）；Zeira（1998）指出新技術需要更多資本，不是每個國家都能跟上技術前緣（p.2）。
- Lu（2021）把 AI 視為可自行累積知識、非競爭性的獨立投入（p.8）。
- 既有 AI 與成長的實證多為中國省級資料（He 2019；Fan & Liu 2021）或企業資料（Yang 2022），國家層級研究受限於資料（p.8–9）。
- 作者說明 Oxford Insights 的 AI 準備度指數年份太短，不適合長期分析（p.8 註 24）。

## 5. 研究問題
AI 創新（以 AI 專利衡量）與長期經濟成長是否相關？這個關係在先進與較不先進經濟體、早期與近期之間是否不同？（p.1–2, 12）

## 6. 研究假設
原文寫明的預期整理如下（原文只有 H1 的意思明確寫為假設，其餘為作者寫明的預期符號）：
- **H1：** AI 與經濟成長正相關（「This study conjectures a positive relationship between AI and economic growth」，p.1）。
- **H2：** AI 專利與總專利的係數預期為正（p.12）。
- **H3：** 先進經濟體 × 專利的交互項預期為負，即專利對長期成長的影響在先進經濟體較小（p.12）。

## 7. 樣本與研究期間
- **分析單位：** 國家－期；每期 5 年，1970–2019 共 10 期（p.12–13）。不平衡面板。
- **描述統計（表 1，p.14）：** 人均實質 GDP 2,080 筆、208 國；人均 GDP 成長率 1,936 筆、208 國；AI 專利 2,165 筆、217 國；人力資本 1,387 筆、145 國。
- **估計樣本（各表不同）：**
  - 表 3（主結果，p.17–18）：AI 專利模型 616 筆、122 國；總專利模型 1,140 筆、144 國。
  - 表 4（1970–1994，p.21）：AI 專利模型 158 筆、61 國。
  - 表 5（1995–2019，p.23）：AI 專利模型 388 筆、120 國。
  - 表 6（先進經濟體，p.25）：AI 專利模型 299 筆、53 國。
  - 表 7（較不先進經濟體，p.26）：AI 專利模型 301 筆、83 國。
  - 表 8（FE-IV，p.27）：AI 專利模型 OLS、FE、GMM 欄 258 筆，FE-IV 欄 326 筆，65 國。
  - 表 9（年度資料，p.30）：AI 專利模型 2,261 筆、120 國。
  - 表 10（加入網路使用者，p.32）：AI 專利模型 463 筆、119 國。
- **先進經濟體定義：** 5 年平均人均實質 GDP 高於 10,000 美元（依 Kim & Lee 2015）（p.12–13）。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| 依變數 `Growth_it` | 5 年期間的平均人均實質 GDP 成長率：(期末 ln 人均實質 GDP − 期初 ln 人均實質 GDP) ÷ 年數；美元，2015 年不變價格（p.11） | [UN National Accounts — Analysis of Main Aggregates](https://unstats.un.org/unsd/snaama/) | — | Gonzales |
| `Growth_i,t−1` | 前一期 5 年平均人均 GDP 成長率（p.11；表 12，p.34） | 同上 | — | Gonzales |
| `GDPpc_i,t−1` | 前一期 5 年平均人均實質 GDP 的對數，代表收斂效果（p.11–12） | 同上 | — | Gonzales |
| `Patents_it`（AI 專利） | 5 年內 AI 專利總數 ÷ 5 年平均人口 × 100 萬，取對數；與 Kim & Lee（2015）的強度指標相同（p.12） | Google Patents Public Data（IFI CLAIMS Patent Services 提供；原文未附網址） | 全文檢索 AI 相關詞，例如「artificial intelligence」「face recognition」「virtual assistant」「machine learning」；以精確比對檢索，詞表限於最常見、最明確的 AI 用語（p.11 及註 30） | Gonzales |
| 總專利 | 口徑同 AI 專利，換成全部專利（p.12） | 同上 | — | Gonzales |
| 人口成長率 | 5 年平均（表 12，p.34） | [World Bank WDI](https://databank.worldbank.org/source/world-development-indicators) | — | — |
| 人均實質資本形成成長率 | 5 年平均（表 12，p.34） | [UN National Accounts](https://unstats.un.org/unsd/snaama/) | — | — |
| 人均實質政府支出成長率 | 5 年平均（表 12，p.34） | [UN National Accounts](https://unstats.un.org/unsd/snaama/) | — | — |
| 貿易開放度 | 5 年平均（出口 + 進口）÷ GDP（p.12） | [World Bank WDI](https://databank.worldbank.org/source/world-development-indicators) | — | — |
| 通膨 | 5 年平均，以 GDP 平減指數計算（p.12 註 32） | [UN National Accounts](https://unstats.un.org/unsd/snaama/) | — | — |
| 人力資本指數成長率 | 依受教育年數與教育報酬率建構的指數，取 5 年平均成長率（p.12） | [Penn World Table](https://www.rug.nl/ggdc/productivity/pwt/)（Feenstra et al. 2015） | — | PWT |
| 先進經濟體虛擬變數 | 5 年平均人均實質 GDP > 10,000 美元 = 1（表 12，p.34） | — | — | Gonzales |
| 網路使用者成長率（穩健性） | 5 年平均（表 12，p.34） | [World Bank WDI](https://databank.worldbank.org/source/world-development-indicators) | — | — |
| 工具變數：引用的非專利文獻（NPL） | 5 年內專利引用的非專利文獻總數，取對數（表 12，p.34） | Google Patents | 只用專利本身引用的 NPL，以強化外生性（p.22 註 49） | Gonzales |

## 9. 研究方法
**理論模型（式 1–8，p.9–10）：** 從 `Y = A K^α L^β H^γ` 出發，假設規模報酬固定，得到 `g_y = δR + α g_k + γ g_h`；以 AI 專利代理研發 R（作者說明專利是研發的產出，不是投入）。

**計量模型（式 9，p.11）：**
`Growth_it = φ0 + φ1 Growth_i,t−1 + φ2 GDPpc_i,t−1 + φ3 Patents_it + φ X_it + ε_it`

| 符號 | 定義 |
|---|---|
| `Growth_it` | 國家 i 在第 t 期（5 年）的平均人均實質 GDP 成長率 |
| `Growth_i,t−1` | 前一期成長率，控制遺漏變數造成的內生性 |
| `GDPpc_i,t−1` | 前一期人均實質 GDP，檢驗收斂效果 |
| `Patents_it` | AI 專利（或總專利）強度 |
| `X_it` | 控制變數、人力資本、先進經濟體虛擬變數、先進經濟體 × 專利交互項 |

- **時間效果：** 以期別虛擬變數控制（p.12）；原文：「All estimated models include time dummies」（p.16 註 41）。表 3 各欄均標示 Time dummies: Yes（p.17–18）。
- **估計方法：** Pooled OLS、固定效果、Anderson–Hsiao（AH）、GMM（p.12–13）。作者說明加入落後期成長率後，固定效果估計有 Nickell 偏誤，且專利與成長可能互為因果，因此加估 AH 與 GMM（p.12–13）。
- **標準誤：** OLS、FE、GMM 為穩健標準誤；AH 為 bootstrap 標準誤（表 3 註，p.18）。
- **GMM 工具變數：** 依 Roodman（2009），工具變數數量應少於國家數；最多用到第 5 期落後值，AI 專利模型 65 個工具變數，總專利模型 32 個（p.18 註 42）。
- **檢定：** Sargan–Hansen 過度認定檢定、Arellano–Bond AR(1)／AR(2)（p.18）；Fisher 型 ADF 單根檢定（p.18 註 43）。
- **穩健性：** 拆成 1970–1994 與 1995–2019（表 4–5）；先進與較不先進經濟體分開估計（表 6–7）；FE-IV，以引用的 NPL 為工具變數（表 8）；改用年度資料（表 9）；加入網路使用者成長率（表 10）。

## 10. 研究結果
**原文結果：**
- **主結果（表 3，p.17）：** AI 專利係數 OLS 0.178***、FE 0.264***、AH 0.246***、GMM 0.275*。總專利係數 OLS 0.172***、FE 0.131*、AH 0.124*、GMM 0.197（不顯著）。
- **其他變數（表 3，p.16–17）：** 前一期人均 GDP 在多數設定顯著為負（FE −1.865***），支持收斂效果；資本形成與政府支出成長顯著為正；人力資本與通膨在各設定皆不顯著。
- **先進經濟體交互項（表 3，p.17–18）：** 先進經濟體 × AI 專利只在 GMM 顯著（−0.227*）；先進經濟體 × 總專利只在 FE 顯著（−0.196**）。
- **GMM 檢定（p.18）：** Sargan–Hansen p 值：AI 專利模型 0.426、總專利模型 0.581，未拒絕工具變數有效。
- **期間（表 4–5，p.19–23）：** 1970–1994 AI 專利各設定皆不顯著（FE 0.151）；1995–2019 FE 0.207**、AH 0.256**、GMM 0.741**。
- **所得分組（表 6–7，p.20, 25–26）：** 先進經濟體 AI 專利顯著為正（FE 0.367***、AH 0.354***、GMM 0.299**）；較不先進經濟體各設定皆不顯著（FE 0.087）。
- **FE-IV（表 8，p.24, 27）：** AI 專利 OLS 0.222***、FE 0.668***、GMM 0.535*、FE-IV 0.499*；Kleibergen–Paap 檢定拒絕識別不足。
- **年度資料（表 9，p.30）：** AI 專利 FE 0.360***、GMM 0.426*。
- **加入網路使用者（表 10，p.32）：** AI 專利 FE 0.277***、GMM 0.769**。

**作者解釋：**
- AI 創新帶動長期成長，影響大於總專利；AI 可應用於製造、ICT、運輸、金融與醫療等多個產業（p.18–19, 29）。
- 近期效果較明顯，原因是 AI 專利自 1990 年代中期增加，品質也提升（p.19–20）。
- AI 效果只在先進經濟體顯著，顯示需要已開發國家的基礎設施與制度才能善用 AI，符合 Zeira（1998）（p.20, 29–30）。
- 人力資本不顯著，可能因為指標有限制，或 AI 替代勞動與人力資本（p.16）。

## 11. 研究限制
作者列出：
- 全文檢索辨識 AI 專利可能有準確度與衡量誤差；部分技術用語跨領域共用（p.11 註 30）。
- 加入落後期成長率的固定效果模型有 Nickell 偏誤；專利與成長可能互為因果（p.12）。
- 時間虛擬變數未必能完全捕捉 1970–2019 年間的外部事件（戰爭、石油危機、金融危機、網路普及等）（p.16 註 41）。
- 人力資本指標忽略認知技能（p.12）。
- 隨著 AI 嵌入各種發明，很難把 AI 與非 AI 的部分分開（p.19 註 46）。
- 先進經濟體的 GMM 工具變數數（42）接近國家數（53）（p.20 註 47）。
- 工具變數資料有限，FE-IV 樣本較小（p.22–24）。

## 12. 關聯
**可參考之處：**
- **H1 的直接先例：** 依變數為人均實質 GDP 成長率、AI 專利每百萬人取對數，在含時間虛擬變數的固定效果模型中顯著為正。
- **H2 的參考：** 以「先進經濟體 × AI 專利」交互項及分組估計檢驗國家差異；AI 效果在先進經濟體才顯著。
- **期間設定的參考：** 1995 年後效果才顯著，提醒研究期間會影響結果。
- **年度資料：** 附錄表 9 改用年度資料，AI 專利仍顯著；與本研究的年度面板較接近。
- **內生性處理：** NPL 工具變數與 FE-IV 可作為穩健性選項。

**不能直接套用之處：**
- 主結果用 5 年平均，不是年度資料。
- AI 專利由全文關鍵詞檢索建構，與 OECD 依 IP5 專利家族、申請人／發明人歸屬的口徑不同（見 [Parteka & Kordalska（2023）](parteka-kordalska-2023.md)）。
- 樣本以全球國家為主，包含大量開發中國家；交互項是「先進經濟體」虛擬變數，不是個別國家。
- AI 專利衡量 AI 創新活動，不是企業採用率。

**相關頁面：** [Parteka & Kordalska（2023）](parteka-kordalska-2023.md)、[Duarte et al.（2026）](duarte-freitas-simoes-2026.md)、[Kalai et al.（2024）](kalai-becha-helali-2024.md)、[Filip et al.（2026）](filip-perezgonzalez-setzer-2026-ecb.md)、[OECD 國家頁](../topics/countries/oecd.md)、[動態面板 GMM](../topics/methods/dynamic-panel-gmm.md)

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
