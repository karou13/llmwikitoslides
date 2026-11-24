---
type: source
title_original: "Investment composition and growth: the role of intangible and tangible ICT capital in the EU and other economies"
authors: ["Marinela-Daniela Filip", "Diego Peréz-González", "Ralph Setzer"]
year: 2026
source_type: 工作論文
journal: "ECB Working Paper Series No 3242"
quartile: "不適用"
doi:
raw_file: "RAW/ecb.wp3242~873057c617.it.pdf"
relevance: 方法參考（雙向固定效果、國家異質性、人力資本）
processing_status: 已寫入
countries: ["EU26（不含 Ireland）", "United States", "United Kingdom", "Japan", "Germany", "Netherlands", "Denmark"]
methods: ["雙向固定效果（國家 + 年份）", "Panel local projections", "State-dependent local projections", "Split-panel jackknife"]
ai_measure: "非 AI 指標：各類投資成長（含無形與有形 ICT 投資：通訊設備、電腦設備、軟體與資料庫、R&D、其他智慧財產）"
outcome: "人均實質 GDP 年成長率（穩健性改用 TFP 成長）"
---

# Investment composition and growth: the role of intangible and tangible ICT capital in the EU and other economies — Filip, Peréz-González & Setzer（2026）

> 頁碼一律為 PDF 頁碼（論文內頁碼 = PDF 頁碼 − 1）。本文研究 ICT 投資，不是 AI；收錄原因是它的模型設定、樣本與異質性分析和本研究的 Model 1–3 最接近。

## 1. 來源
- **書目：** Filip, M.-D., Peréz-González, D., & Setzer, R. (2026). Investment composition and growth: the role of intangible and tangible ICT capital in the EU and other economies. *ECB Working Paper Series*, No 3242. European Central Bank. [ECB PDF](https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp3242~873057c617.it.pdf)
- **類型：** 歐洲中央銀行（ECB）工作論文，非期刊論文，期刊分區不適用。版權頁標示 © European Central Bank, 2026。論文聲明內容不代表 ECB 立場（p.1）。

## 2. 研究目的
檢驗投資「組成」的差異（而非投資總量）能否解釋 EU 與其他先進經濟體在 1996–2021 年的經濟成長差距，特別是無形與有形 ICT 投資的角色（p.2, 6）。

## 3. 研究貢獻
- 建構標準化的「投資效率比」（investment efficiency ratio）：把各類投資的估計成長效果除以該類投資占總投資的加權比重，以比較每單位投資的成長關聯（p.7, 15）。
- 依所得水準、人力資本與子期間分組，呈現投資與成長關係的跨國異質性；指出人力資本與技術密集投資之間的互補性（p.7）。

## 4. 研究背景
- EU 與美國的投資占 GDP 比率相近，但 EU 的投資報酬持續較低，問題可能不在投資不足，而在投資效率與組成（p.5）。
- EU 投資較少流向無形與有形 ICT，較多流向汽車等傳統中技術產業（p.5–6）。
- 文獻脈絡（p.7–9）：
  - 無形資產對產出成長的貢獻大於其投資占比（Corrado et al. 2005、2009）。
  - ICT 投資解釋美國 1990 年代後期生產力回升（Jorgenson et al. 2008）；歐洲企業從 ICT 獲益較少（Bloom et al. 2012）。
  - 生產力悖論與生產力 J 曲線（Brynjolfsson et al. 2021）。
  - 制度品質與人力資本影響投資的經濟報酬（Alvarez et al. 2026；Roth & Mitra 2025）。

## 5. 研究問題
- 哪些類型的投資與人均 GDP 成長的關聯最強？（p.6, 9）
- 投資與成長的關係是否因國家所得水準、人力資本與期間而不同？（p.7）

## 6. 研究假設
原文未編號，以下依原文寫明的檢驗方向整理：
- **H1：** 無形與有形 ICT 投資與人均 GDP 成長的關聯，高於其他有形投資（p.6–7）。
- **H2：** 投資與成長的關係在高所得、高人力資本國家較強（p.7）。

## 7. 樣本與研究期間
- **分析單位：** 國家－年，年度資料。
- **期間：** 1996–2021；子期間 1996–2007（金融海嘯前）、2008–2021（金融海嘯後）（p.9, 12）。
- **國家：**
  - EU26：EU 會員國扣除 Ireland。排除原因是跨國企業移轉智慧財產造成 GDP 失真（2015 年 GDP 成長 26%）；納入 Ireland 的結果列於附錄 A.3，主要結論不變（p.9）。
  - 擴大樣本：EU26 加 United States、United Kingdom、Japan，共 29 國（p.9–10）。
- **觀測值（表 2，p.14）：** EU26 1996–2021：593 筆、26 國；29 國 1996–2021：667 筆、29 國。表 3 為 595 筆與 669 筆（p.17）。
- **所得分組（p.19–20）：** 以 2021 年人均 GDP 是否高於 EU26 中位數分組，各 13 國。高所得組含 Austria、Belgium、Cyprus、**Germany**、**Denmark**、Spain、Finland、France、Italy、Luxembourg、Malta、**the Netherlands**、Sweden。
- **描述統計（表 1，p.10）：** 29 國，754 筆（人均 GDP），各變數 697–754 筆。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| 依變數：人均實質 GDP 成長率 | `ln RGDPpc_i,t − ln RGDPpc_i,t−1`；人均實質 GDP 單位為千歐元（式 1、表 1，p.10, 12） | [AMECO](https://economy-finance.ec.europa.eu/economic-research-and-databases/economic-databases/ameco-database_en) | — | 作者 |
| 各類投資成長 `Δln Inv_i,t,j` | 依資產類型的實質投資成長：住宅、非住宅建物、其他機器設備、運輸設備、電腦設備、通訊設備、軟體與資料庫、R&D、其他智慧財產（p.10–12） | [EUKLEMS & INTANProd](https://euklems-intanprod-llee.luiss.it/)（2025 年版，Bontadini et al. 2023） | 資產分類依 ESA 2010；排除 cultivated assets（不是每國都有資料，且占比低）（p.11） | 作者分組 |
| 投資分組 | 無形與有形 ICT：通訊設備、電腦設備、其他智慧財產、R&D、軟體與資料庫；其他有形：其他機器、住宅、非住宅建物、運輸設備（表 3 註，p.17） | 同上 | — | 作者 |
| `ln Inv_i,t−1` | 前一期總投資（GFCF）對數（p.12） | EUKLEMS（表 1 列為 Total GFCF 占附加價值 %） | — | 作者 |
| `ln RGDPpc_i,t−1` | 前一期人均實質 GDP 對數，代表收斂效果（p.12–13） | [AMECO](https://economy-finance.ec.europa.eu/economic-research-and-databases/economic-databases/ameco-database_en) | — | 作者 |
| 就業率 | 占勞動力 %（表 1，p.10） | [AMECO](https://economy-finance.ec.europa.eu/economic-research-and-databases/economic-databases/ameco-database_en) | — | AMECO |
| 政府預算餘額 | 占 GDP %（表 1，p.10） | [AMECO](https://economy-finance.ec.europa.eu/economic-research-and-databases/economic-databases/ameco-database_en) | — | AMECO |
| 制度品質 | 政府效能、法規品質、法治、貪腐控制四項的未加權平均，重新縮放為 0–1（依 Masuch et al. 2016）（表 1 註，p.10） | [World Bank Worldwide Governance Indicators](https://www.worldbank.org/en/publication/worldwide-governance-indicators) | 1997、1999、2001 年缺值以線性內插補齊 | 作者 |
| 人力資本指數 | 依受教育年數與教育報酬率建構（表 1，p.10） | [Penn World Table 11.0](https://www.rug.nl/ggdc/productivity/pwt/) | 狀態依存模型中，以每年中位數分為高、低人力資本兩組（p.26–27） | PWT |
| TFP（穩健性） | 2020 = 100（表 1，p.10） | [AMECO](https://economy-finance.ec.europa.eu/economic-research-and-databases/economic-databases/ameco-database_en) | — | AMECO |
| 匯率 | 本國貨幣／歐元（表 1，p.10） | ECB（原文未附網址） | — | ECB |

## 9. 研究方法
**模型 1：雙向固定效果（式 1，p.12–13）：**
`ln RGDPpc_i,t − ln RGDPpc_i,t−1 = Σ_j β_j Δln Inv_i,t,j + γ1 ln Inv_i,t−1 + γ2 ln RGDPpc_i,t−1 + Σ_k ψ_k X_i,t,k + θ_i + α_t + ε_i,t`

| 符號 | 定義 |
|---|---|
| `β_j` | 第 j 類投資成長與人均 GDP 成長的關係；投資成長增加 1 個百分點，人均 GDP 成長變動 β 個百分點（p.14） |
| `X_i,t,k` | 控制變數：就業率、政府預算餘額占 GDP、制度品質 |
| `θ_i`、`α_t` | 國家固定效果、年份固定效果（原文：「we control for country (θi) and time (αt) fixed effects」，p.13） |

- **標準誤：** 依國家群聚（表 2–4 註）。
- **多重共線性：** VIF 均低於 5（p.13 註 4）。
- **內生性處理（p.12）：** 投資是 GDP 的組成，且成長可能反過來帶動投資。作者認為跨國分類投資資料難找到可信的工具變數，改以落後期投資與控制變數部分緩解，並說明結果只能解讀為關聯，不是因果。

**投資效率比（式 2，p.15）：** `Efficiency_j = β̂_j / s̄_j`，`s̄_j` 為第 j 類投資在各國的加權平均占比。

**模型 2：Panel local projections（式 3，p.22–23）：** 依變數為 `ln RGDPpc_i,t+h − ln RGDPpc_i,t−1`，h = 0–4；含國家與年份固定效果。以 Dhaene & Jochmans（2015）split-panel jackknife 修正 Nickell 偏誤；作者說明不用 GMM，是因為 GMM 容易產生過多工具變數（Roodman 2009）（p.23 註 6）。

**模型 3：State-dependent local projections（式 4，p.26–27）：** 以「人力資本是否高於當年中位數」的指示變數，讓投資效果分成高、低人力資本兩組係數；作者說明這種做法不必切分樣本，適合時間維度短的資料。

**穩健性（p.28）：** 依變數改為 TFP 成長（附錄表 6）；納入 Ireland（附錄 A.3）。

## 10. 研究結果
**原文結果：**
- **各類投資（表 2，p.14）：** EU26 1996–2021：通訊設備 0.012***、R&D 0.045***、其他智慧財產 0.006***；電腦設備 0.006、軟體與資料庫 0.016，皆不顯著。前一期人均 GDP −0.098***（收斂效果）。R² = 0.740。
- **擴大到 29 國（表 2，p.14）：** 係數普遍較大，例如 R&D 0.060***、通訊設備 0.015***。
- **投資分組（表 3，p.17）：** 無形與有形 ICT 投資：EU26 0.078***；1996–2007 為 0.119***；2008–2021 為 0.060***；29 國為 0.108***。其他有形投資：EU26 0.196***。
- **所得分組（表 4，p.20）：** 無形與有形 ICT 投資：高所得組 0.078*、低所得組 0.061***；其他有形投資：高所得組 0.143**、低所得組 0.205***。
- **Local projections（p.23–24）：** ICT 相關投資與人均 GDP 成長的關聯最持久，R&D 的累積反應最大；其他有形投資的關聯約一期後消失。
- **人力資本分組（圖 12，p.27）：** 高人力資本國家中，投資成長與人均 GDP 成長的正向關係較強、較持久；原文以圖呈現，未列係數表。
- **穩健性（p.28）：** 改用 TFP 成長或納入 Ireland，主要結論不變。

**作者解釋：**
- 依效率比，通訊設備、其他智慧財產與 R&D 的效率最高（p.15）。
- 2008 年後 ICT 投資效率下降，可能反映生產力悖論、GDP 衡量問題，或勞動與產品市場的結構性障礙（p.17–18）。
- 高人力資本與高所得國家較能把 ICT 投資轉為成長，顯示人力資本與技術密集投資的互補性（p.7, 27）。

**模型推算（非實證估計）：** 情境分析假設係數固定、不含一般均衡效果；若 EU26 的 ICT 投資成長追上美國，2035 年人均 GDP 可高出 1.3%（約 €430）；完全追上美國投資水準的情境則高出 8.5%（約 €2,700）（p.21）。

## 11. 研究限制
作者列出：
- 投資是 GDP 的組成，且有反向因果；以落後期變數處理無法完全排除內生性，結果只能解讀為關聯（p.12）。
- 效率比假設線性與固定報酬，不能解讀為因果或結構性的投資效率（p.15）。
- Local projections 的有效樣本隨期數減少，因此只報告到 h = 4（p.22 註 5）。
- 情境分析為部分均衡，假設係數穩定（p.21）。

## 12. 關聯
**可參考之處：**
- **Model 1 的直接先例：** 依變數同為人均實質 GDP 年成長率，同時控制國家與年份固定效果，國家群聚標準誤，樣本為歐洲國家年度面板。
- **H2 的先例：** 以分組或狀態依存方式呈現跨國異質性；Germany、Netherlands、Denmark 都在高所得組。
- **H3-A 的先例：** 人力資本高的國家，技術密集投資與成長的關係較強；人力資本指標為 PWT 指數。
- **控制變數參考：** 前一期人均 GDP（收斂）、前一期總投資、就業率、政府預算餘額、制度品質。
- **年份短時的做法：** 狀態依存設定不必切分樣本；以 split-panel jackknife 取代 GMM。

**不能直接套用之處：**
- 解釋變數是 ICT 投資，不是 AI 專利或 AI 採用率；只能作為「技術投資 → 成長」的方法先例。
- 異質性以所得或人力資本分組，不是 AI × 個別國家虛擬變數。
- 本文為工作論文，未經期刊審查。

**相關頁面：** [Parteka & Kordalska（2023）](parteka-kordalska-2023.md)、[Gonzales（2023）](gonzales-2023.md)、[Brey & van der Marel（2024）](brey-vandermarel-2024.md)、[德國](../topics/countries/germany.md)、[荷蘭](../topics/countries/netherlands.md)、[丹麥](../topics/countries/denmark.md)、[OECD 國家頁](../topics/countries/oecd.md)

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
