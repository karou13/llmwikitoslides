# 研究總覽

> 本頁追蹤研究設計；重要變更先與使用者討論確認。標記：待確認／暫定／已確認。
> 2026-11-23 依使用者提供的研究設計寫入。

## 研究問題

狀態：暫定

- **題目：** The Impact of Artificial Intelligence Adoption on Economic Growth: A Comparative Panel Analysis of Germany, the Netherlands, Denmark, and the OECD
- **研究定位：** 不只是驗證 AI 能不能促進經濟成長，而是檢驗 AI 的經濟成長效果是否存在國家異質性（country heterogeneity）。
- **RQ1：** AI 創新活動是否與經濟成長有正向關係？
- **RQ2：** 這種關係在德國、荷蘭、丹麥之間是否不同？
- **RQ3：** 人力資本與產業結構能否解釋這些國家差異？

## 研究假設

狀態：暫定

- **H1：** AI 採納（以 AI 創新活動衡量）與經濟成長呈正向關係。理論依據：自動化提高生產效率；AI 降低部分生產成本；AI 促進知識創造與創新。
- **H2：** AI 對經濟成長的影響存在跨國差異（本研究核心假設）。理論依據：各國 AI 發展程度、生產結構、運用 AI 的能力不同。
- **H3：** 國家條件會調節 AI 對經濟成長的影響。
  - H3-A：人力資本的調節效果。
  - H3-B：產業結構的調節效果。

## 資料與資料來源

狀態：暫定

### 樣本與期間
- **樣本：** 歐洲的 OECD 國家年度面板（暫定）；Germany、Netherlands、Denmark 為重點比較國家，其他歐洲 OECD 國家作為基準。完整國家名單：待確認。
- **期間：** 待確認。暫定 2014–2024，最後依各變數實際共同可取得的年份決定；近年專利資料可能尚不完整（[Parteka & Kordalska](sources/parteka-kordalska-2023.md) 依 OECD 作法將專利截至 2016 年）。

### 變數

| 角色 | 變數 | 定義 | 來源 | 狀態 |
|---|---|---|---|---|
| 依變數 | 人均實質 GDP 成長率 | 每年人均實質 GDP 相較前一年的百分比變化 | 使用者整理的 [Google 試算表](https://docs.google.com/spreadsheets/d/10nCfJxmAy1kntUsHU-x00dasZnpemV4-/edit?gid=214935724#gid=214935724) | 原始來源待確認 |
| 主要 AI 指標 | AI 專利（申請人） | 依申請人所在國歸屬，分數計數；1985–2024 | [OECD Patents 資料庫](https://data-explorer.oecd.org/vis?df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_PATENTS%40DF_PATENTS_OECDSPECIFIC&df[ag]=OECD.STI.PIE&lc=en&dq=.A...PRIORITY...INVENTOR...AI&pd=2012,2024&to[TIME_PERIOD]=false&vw=tb) | 待確認：使用者提供的申請人與發明人連結相同，網址篩選條件皆為 `INVENTOR` |
| 穩健性 | AI 專利（發明人） | 依發明人所在國歸屬，分數計數；1985–2024 | 同上 | 暫定 |
| 穩健性 | AI 學術論文 | 以約 800 個 AI 關鍵字辨識，依作者機構國家歸屬；2000–2025 | [OECD.AI（Elsevier/Scopus）](https://oecd.ai/en/data?selectedTab=AIResearch)；[資料說明](https://oecd.ai/en/elsevier) | 暫定 |
| 待確認 | OECD.AI 的 AI 專利資料 | 五類核心 AI 的 CPC 分類；依發明人分數計數；1995–2024 | [OECD.AI AI patents](https://oecd.ai/en/data?selectedArea=ai-patents) | 待確認是否與上述專利資料重複 |
| 調節（H3-A） | 人力資本 | 25–64 歲人口中受過高等教育的比例 | [Eurostat edat_lfse_03](https://ec.europa.eu/eurostat/databrowser/view/edat_lfse_03/default/table?lang=en) | 暫定；為人力資本的代理指標 |
| 調節（H3-B） | 產業結構 | 各產業占總附加價值比例，先用製造業占比 | [Eurostat nama_10_a10](https://ec.europa.eu/eurostat/databrowser/view/nama_10_a10/default/table?lang=en) | 暫定 |
| 控制 | 固定資本形成毛額 | 占 GDP 百分比 | [World Bank NE.GDI.FTOT.ZS](https://data.worldbank.org/indicator/NE.GDI.FTOT.ZS) | 暫定；為投資流量，非資本存量 |
| 控制 | 貿易開放度、通膨、人口成長、一般創新（非 AI 專利） | — | — | 待確認是否採用 |
| 標準化 | 就業人口 | 用於計算每百萬就業人口的 AI 專利數 | — | 來源待確認 |

## 研究模型

狀態：暫定

| 模型 | 對應假設 | 設定 | 核心檢定 |
|---|---|---|---|
| Model 1 | H1 | 雙向固定效果：`Growth_it = α + β₁AI_it + γ′X_it + μ_i + λ_t + ε_it` | β₁ > 0 |
| Model 2 | H2 | 加入 AI × 國家交互作用（DE、NL、DK），以其他歐洲 OECD 國家為基準 | Wald 檢定 1：β₂ = β₃ = β₄ = 0（三國是否與基準不同）；Wald 檢定 2：β₂ = β₃ = β₄（三國之間是否不同） |
| Model 3-A | H3-A | 加入人力資本與 AI × 人力資本 | 交互項係數 |
| Model 3-B | H3-B | 加入產業結構與 AI × 產業結構（與 3-A 分開估計） | 交互項係數 |
| 穩健性 | — | 改用發明人專利、AI 學術論文、專利存量、落後一期 AI 指標 | — |

**文獻先例與本研究延伸：**
- 國家面板 + AI 專利 + 經濟成長：有先例（[Duarte et al. 2026](sources/duarte-freitas-simoes-2026.md)：Panel ARDL、GMM；[Kalai et al. 2024](sources/kalai-becha-helali-2024.md)：PMG-ARDL）。
- 雙向固定效果（國家 + 年份固定效果）+ AI 專利／出版物：有先例（[Parteka & Kordalska 2023](sources/parteka-kordalska-2023.md)，式 1，p.7；依變數為勞動生產力成長，基準為固定效果 OLS）。
- 固定效果 + 時間效果 + AI 專利 → 人均 GDP 成長：有先例（[Gonzales 2023](sources/gonzales-2023.md)，表 3，p.17；5 年平均資料，122 國；附錄表 9 改用年度資料）。
- 國家 + 年份固定效果 → 人均 GDP 年成長率，歐洲國家年度面板：有先例，但解釋變數是 ICT 投資而非 AI（[Filip et al. 2026](sources/filip-perezgonzalez-setzer-2026-ecb.md)，式 1，p.12–13；EU26 加美英日，1996–2021，國家群聚標準誤）。
- AI × 人力資本交互作用：有先例（Duarte et al. 2026，交互項多不顯著）。
- 人力資本放大技術投資的成長效果：相近先例（[Filip et al. 2026](sources/filip-perezgonzalez-setzer-2026-ecb.md)：高人力資本國家中 ICT 投資與成長的關係較強，p.27；指標為 PWT 人力資本指數）。
- 人力資本影響 AI 採用的機制：[Brey & van der Marel 2024](sources/brey-vandermarel-2024.md)（2012 年大學學歷占比較高的國家 × 產業，2021 年 AI 採用率較高，p.2）；研究方向是人力資本 → AI 採用，不是 AI → 成長。
- 研究國家異質性的動機：有先例（[BIS 1321](sources/bis-gambacorta-et-al-2025.md)、[Misch et al. 2025](sources/misch-et-al-2025-imf.md)；[Gonzales 2023](sources/gonzales-2023.md)：AI 專利只在先進經濟體顯著，表 6–7）。
- 以交互作用表達 AI 效果的國家差異：相近先例為 [BIS 1321](sources/bis-gambacorta-et-al-2025.md)（國家 AI 準備度 × 產業 AI 暴露度，連續變數，國家－產業資料）。
- AI × 個別國家虛擬變數（DE、NL、DK）：本研究延伸，wiki 中沒有相同設計（見 [方法與資料結構比較](topics/synthesis/methods-data-structures.md)）。

## 研究結果

### 文獻發現
見 [AI 指標比較](topics/synthesis/ai-measures.md)、[方法與資料結構比較](topics/synthesis/methods-data-structures.md)、[來源間的數字差異](topics/synthesis/source-discrepancies.md)。

### 本研究實證結果
待實際估計後更新；不得以文獻結果代填。

## 研究限制

狀態：暫定

- AI 專利與學術論文衡量 AI 創新活動，不等於企業 AI 採用率；題目使用 Adoption，需說明為代理指標（見 [AI 指標比較](topics/synthesis/ai-measures.md)）。
- 高等教育人口比例只是人力資本的代理指標，不涵蓋技能、經驗與教育品質。
- 固定資本形成是投資流量，也可能受經濟成長影響，無法排除內生性。
- 研究期間短、交互作用項多，估計可能不穩定。
- 結果為相關，不是因果。
