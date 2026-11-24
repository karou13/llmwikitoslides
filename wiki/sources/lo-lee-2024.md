---
type: source
title_original: "Digitalization, AI Intensity, and International Trade"
authors: ["Chu Ping Lo", "Yi Lee"]
year: 2024
source_type: 期刊論文
journal: "Annals of Economics and Finance"
quartile: "SJR 2025 Q4, Finance"
doi:
raw_file: "RAW/Lo_Lee_2024_Digitalization_AI_Intensity_Trade.pdf"
relevance: 背景資料
processing_status: 已寫入
countries: ["Global (cross-country)", "Germany", "Netherlands", "Denmark"]
methods: ["重力模型（Eaton–Kortum 兩階段）", "工具變數"]
ai_measure: "AI 強度：每人 AI 科學出版物（OECD.AI，Microsoft Academic Graph）"
outcome: "雙邊進口占比；出口能力"
---

# Digitalization, AI Intensity, and International Trade — Lo & Lee（2024）

> 頁碼為 PDF 頁碼（期刊頁碼 = PDF 頁碼 + 250）。

## 1. 來源
- **書目：** Lo, C. P., & Lee, Y. (2024). Digitalization, AI Intensity, and International Trade. *Annals of Economics and Finance*, 25(1), 251–273. [RePEc 頁面](https://ideas.repec.org/a/cuf/journl/y2024v25i1lolee.html)（文獻蒐集總覽所列網址）
- **期刊：** Annals of Economics and Finance。同儕審查狀態：查證中。分區：SJR 2025 Q4，Finance（[SCImago](https://www.scimagojr.com/journalsearch.php?q=Annals+of+Economics+and+Finance)）。
- **作者：** Lo 為國立臺灣大學農業經濟學系；Lee 為國立清華大學經濟學系（p.1）。

## 2. 研究目的
建立把資料視為生產要素的理論模型，並以實證估計數位化強度與 AI 強度對國際貿易的貢獻（p.1–3）。

## 3. 研究貢獻
- 在 Eaton–Kortum 貿易模型中加入「資料要素」，資料的處理成本取決於一國的數位化強度與 AI 強度（p.2–3, 7）。
- 拆解出口能力中生產技術、工資、數位化與 AI 各自的貢獻（p.18–19）。

## 4. 研究背景
- 既有實證研究多以頻寬、網路或手機普及作為數位化指標，研究其對貿易的影響（p.1–2）。
- 作者主張：數位基礎建設讓企業取得原始資料，AI 把原始資料轉為可用的資料要素，兩者共同降低資料處理成本（p.2, 7）。

## 5. 研究問題
一國的數位化強度與 AI 強度如何影響其出口？兩者對各國出口能力差異的解釋力有多大？（p.1, 3）

## 6. 研究假設
原文未編號，以下依理論模型的預測整理（p.7）：
- **H1：** 數位化強度越高，資料處理成本越低，出口越多。
- **H2：** AI 強度越高，資料處理成本越低，出口越多。

## 7. 樣本與研究期間
- **分析單位：** 第一階段為國家對（出口國 × 進口國 × 年）；第二階段為出口國 × 年。
- **觀測值：** 第一階段 497,636 筆（表 2，p.12）；第二階段 826 筆（未納入數位化與 AI）與 732 筆（表 3，p.16）。
- **期間與國家數：** 原文正文未明確寫出樣本年份與國家總數；圖 1 列出的國家包含 DEU、DNK、NLD（p.13）。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| 雙邊貿易流量與重力變數 | 進口值、距離、共同語言、共同宗教、WTO、兄弟國、殖民關係（p.9, 12） | CEPII 資料庫（原文未載明資料集名稱或網址） | — | CEPII |
| 數位化強度 `k_it` | 上網人口比例；替代指標為每百人行動電話訂閱數、固定寬頻訂閱數（p.9） | World Bank（原文未載明資料集） | — | World Bank |
| AI 強度 `ria_it` | 每人 AI 科學出版物數（p.9–10） | OECD.AI Policy Observatory，底層為 Microsoft Academic Graph（MAG） | MAG 分類為「artificial intelligence」或「machine learning」的論文；依作者機構歸屬國家；多位作者時平均分配（p.9） | OECD.AI |
| 生產技術控制 | R&D 支出／GDP、專利數對數、人力資本指數（p.15） | 原文未逐一載明資料庫 | — | — |
| 工資的工具變數 | 人口、勞動力、失業率（p.15） | 原文未載明資料庫 | — | — |

## 9. 研究方法
**兩階段估計（依 Eaton & Kortum 2002，p.10–15）：**

**第一階段：重力方程（式 9，p.11）：**
`ln(X_int / Y_nt) = C_it − θ ln τ_int − ln Φ_nt`

| 符號 | 定義 |
|---|---|
| `X_int / Y_nt` | 進口國 n 自出口國 i 的進口值占 n 國 GDP 的比例 |
| `C_it` | 出口國 × 年固定效果，代表出口能力 |
| `τ_int` | 貿易成本（距離、語言、WTO 等） |
| `Φ_nt` | 多邊阻力項：以距離倒數加權的來源國 GDP（依 Baldwin & Harrigan 2011） |

**第二階段：出口能力分解（式 10，p.15）：**
`C_it = α Z_it − θ ln w_it + θϕ(1 − γ) ln k_it + θϕγ ln ria_it + y_t + ε_it`
- `θ`：生產力分散參數；`ϕ`、`γ`：資料要素在生產中的參數。
- 數位化的貿易彈性 = ϕθ(1 − γ)；AI 的貿易彈性 = θϕγ。
- `Z_it`：R&D／GDP、專利、人力資本；`y_t`：年份固定效果。
- 工資以人口、勞動力、失業率作為工具變數（p.15）。

**分解（式 12，p.19）：** 依 Hottman et al.（2016），把出口能力拆為 Eaton–Kortum 部分（技術與工資）、數位化、AI 三部分的變異貢獻。

## 10. 研究結果
- **重力方程（表 2，p.12）：** 距離 −1.276***；共同語言 0.577***；WTO 0.316***；R² = 0.676。
- **出口能力（表 3，p.16）：**

| | (1) 未含數位與 AI | (2) 上網比例 | (3) 行動電話 | (4) 固定寬頻 |
|---|---|---|---|---|
| θ | 2.002*** | 4.371*** | 6.024*** | 6.724*** |
| 數位化貿易彈性 | — | 0.85 | 2.03 | 0.97 |
| AI 貿易彈性 | — | 1.01 | 1.33 | 1.30 |
| 觀測值 | 826 | 732 | 732 | 732 |

- AI 強度增加 1%，出口增加約 1.01%–1.30%（摘要，p.1）。數位化與 AI 合計彈性 1.86，約為貿易成本彈性（θ = 4.37）的 43%（p.16–17）。
- **原文數字不一致：** 摘要寫 AI 彈性 1.01%–1.30%，表 3 第 (3) 欄為 1.33（p.1, 16）。
- **出口能力分解（表 6，p.19）：** 生產技術與工資 47%、AI 強度 44%、數位化 9%。
- 三種數位化指標高度相關（0.986–0.995，表 4，p.17）。

**作者解釋：** 改善數位基礎建設與提高 AI 強度，對提升出口的重要性與技術升級相當（p.20）。

## 11. 研究限制
原文未列研究限制專節。
- **Wiki 註記：** AI 強度以 AI 學術出版物衡量，屬研究產出而非企業採用；三種數位化指標相關係數超過 0.98，難以區分各自效果。

## 12. 關聯
**可參考之處：**
- 以 OECD.AI 的 AI 出版物作為國家層級 AI 指標，與 Duarte、Parteka 的 AI 出版物指標屬同類，但資料來源不同（MAG 對 Scopus）。
- 提供 AI 影響經濟的貿易管道，文獻蒐集總覽註記作者為國內學者。

**不能直接套用之處：**
- 結果變數是貿易，不是經濟成長。
- 樣本年份與國家數未明確寫出，難以重現。
- AI 出版物不是企業採用率。

**相關頁面：** [Wagner（2025）](wagner-2025.md)、[DergiPark（2025）](dergipark-2025-export.md)、[Parteka & Kordalska（2023）](parteka-kordalska-2023.md)

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
