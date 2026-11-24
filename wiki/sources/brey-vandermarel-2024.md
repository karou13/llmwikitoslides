---
type: source
title_original: "The role of human-capital in artificial intelligence adoption"
authors: ["Björn Brey", "Erik van der Marel"]
year: 2024
source_type: 期刊論文
journal: "Economics Letters"
quartile: "SJR 2025 Q2, Finance"
doi: "10.1016/j.econlet.2024.111949"
raw_file: "RAW/1-s2.0-S0165176524004336-main.pdf"
relevance: 機制參考（H3-A：人力資本與 AI 採用）
processing_status: 已寫入
countries: ["歐洲國家（附錄圖涵蓋 32 國）"]
methods: ["跨國跨產業 OLS", "國家固定效果", "產業固定效果"]
ai_measure: "企業 AI 採用率：至少使用一種 AI 技術的企業占比（Eurostat，2021，國家 × 產業）"
outcome: "企業 AI 採用率（本文 AI 是依變數，不是解釋變數）"
---

# The role of human-capital in artificial intelligence adoption — Brey & van der Marel（2024）

> 頁碼為 PDF 頁碼（共 5 頁，含附錄）。

## 1. 來源
- **書目：** Brey, B., & van der Marel, E. (2024). The role of human-capital in artificial intelligence adoption. *Economics Letters*, 244, 111949. https://doi.org/10.1016/j.econlet.2024.111949
- **期刊：** Economics Letters（Elsevier 出版）。論文載明 2024-05-29 收稿、2024-08-23 修訂、2024-08-30 接受（p.1）。同儕審查狀態：查證中（ScienceDirect 期刊頁回傳 403，未能讀取）。分區：SJR 2025 Q2，Finance（[SCImago](https://www.scimagojr.com/journalsearch.php?q=Economics+Letters)）。

## 2. 研究目的
研究人力資本在 AI 技術早期採用與擴散中的角色（p.1）。

## 3. 研究貢獻
- 作者表示是第一篇提出「現有員工整體人力資本」影響 AI 採用的、可合理解讀為因果的證據，而不只是雇用 AI 專業人才（p.1, 4）。
- 使用 Eurostat 新釋出的國家 × 產業 AI 採用資料（p.1–2）。

## 4. 研究背景
- AI 採用速度因國家與產業差異很大（p.1）。
- 既有研究指出 AI 採用與企業主、超級明星城市、高生產力大企業、AI 人才雇用、大學 AI 系所及 ICT 基礎設施有關（McElheran et al. 2023；Calvino et al. 2022、2023；Borgonovi et al. 2023）（p.1）。
- 反方向的文獻：Aghion et al.（2017）研究 AI 採用如何促使企業投資人力資本（p.1 註 2）。

## 5. 研究問題
既有的人力資本差異，能否解釋歐洲各國、各產業的 AI 採用差異？（p.1–2）

## 6. 研究假設
原文未編號，依原文寫明的預期整理：
- **H1：** 人力資本較高的國家 × 產業，AI 採用率較高（p.1–2）。

## 7. 樣本與研究期間
- **分析單位：** 國家 × 產業格子（橫斷面）。
- **期間：** AI 採用為 2021 年；人力資本為 2012 年（大學學歷占比）或 2020 年（高學歷集中企業占比）（p.2）。
- **觀測值（表 1，p.2）：** 大學學歷指標 267 筆；高學歷集中企業指標 88 筆。附錄表 A2 為 254–265 筆（p.5）。
- **涵蓋範圍：** 附錄圖 A1 呈現 32 個歐洲國家、9 個 NACE 主要產業（p.1 註 1）：C 製造、E 公用事業、F 營建、G 批發零售、H 運輸、I 住宿餐飲、J 資訊通訊、M 專業科學技術、N 支援服務（p.4）。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| `AI_s,c,t`（AI 採用率） | 國家 c、產業 s 中，至少採用一種 AI 技術（任何業務用途）的企業占比，2021 年（p.2） | Eurostat「Community survey on ICT usage and e-commerce in enterprises」（Eurostat 2023a；原文未列資料集代碼與網址） | AI 技術包含：文字探勘、語音辨識、自然語言生成、影像辨識、機器學習、自動化決策、機器自主移動（附錄表 A1，p.4） | Eurostat |
| 大學學歷占比 `HC` | 國家 × 產業中具大學（高等）學歷的員工占比，2012 年（p.2） | Eurostat 教育與訓練統計（Eurostat 2023b；原文未列資料集代碼與網址） | 2012 年是 Eurostat 公布此資料的第一年 | Eurostat |
| 高學歷集中企業占比 | 大學學歷員工至少占 50% 的企業占比，2020 年；穩健性另用 25%、10% 門檻（p.2；表 1） | 同上 | 2020 年是此變數可取得的第一年 | Eurostat |
| 中學學歷占比（控制變數） | 2012 年（表 1，p.2） | 同上 | — | Eurostat |

## 9. 研究方法
**模型（式 1，p.2）：**
`AI_s,c,t = HC_s,c,t−i + δ_s + δ_c + ε_s,c`

| 符號 | 定義 |
|---|---|
| `AI_s,c,t` | 國家 c、產業 s 在 t 年（2021）的 AI 採用率 |
| `HC_s,c,t−i` | 早於 AI 普及的人力資本，i 為時間差 |
| `δ_s`、`δ_c` | 產業固定效果、國家固定效果 |

- **識別策略（p.2–3）：** 跨國跨產業設計（Ciccone & Papaioannou 2023）。為排除「AI 採用改變人力資本組成」的反向因果，使用 AI 開始採用之前的人力資本。國家與產業固定效果吸收各國 AI 政策（如補貼）與各產業共通的 AI 方案差異。識別假設是 AI 政策與其他技術不是針對特定國家的特定產業設計。
- **標準誤：** 穩健標準誤（表 1 註，p.2）。
- **延伸分析：** 依 AI 技術類型與用途分別估計（附錄表 A2，p.5）；檢查 AI 採用與各學歷層級就業變動的關係（p.3）。

## 10. 研究結果
**原文結果：**
- **大學學歷（表 1，p.2）：** 2012 年大學學歷占比：不含固定效果 0.185***；加入國家與產業固定效果 0.084**；再控制中學學歷 0.097**。中學學歷不顯著（0.016）。
- **高學歷集中企業（表 1，p.2）：** 大學學歷員工逾 50% 的企業占比：不含固定效果 0.103***；含固定效果 0.124*；同時放入 25%、10% 門檻時為 0.132*，25%（0.005）與 10%（0.074）門檻不顯著。
- **R²（表 1）：** 含固定效果的設定為 0.830–0.879。
- **AI 類型（表 A2，p.5）：** 人力資本只對「自動化決策」（0.089**）與「機器自主移動」（0.024**）顯著；文字探勘、語音辨識、自然語言生成、影像辨識、機器學習不顯著。
- **AI 用途（表 A2，p.5）：** 生產（0.046**）、行政（0.047*）、物流（0.029***）顯著；行銷與銷售接近 0（−0.001）。
- **就業（p.3–4）：** 截至 2021 年，未發現 AI 採用造成低、中、高技能勞工就業下降。

**作者推算：** 以大學學歷平均 26.7 個百分點、AI 採用率平均 6.5 個百分點換算，人力資本約可解釋 34.5% 的 AI 採用；以高學歷集中企業指標換算約 50.2%（p.3）。

**作者解釋：** 人力資本最密集的企業是 AI 採用的主要推動者；作者認為估計結果可合理解讀為因果（p.3–4）。

## 11. 研究限制
原文未設限制章節；依原文內容可見：
- 識別依賴「AI 政策不針對特定國家的特定產業」的假設（p.3）。
- AI 採用只有 2021 一年的橫斷面資料（p.2）。
- 就業結果只觀察到 2021 年（p.1, 4）。

## 12. 關聯
**可參考之處：**
- **H3-A 的機制依據：** 人力資本較高的地方 AI 採用率較高，支持「人力資本影響 AI 能否被用起來」。
- **人力資本指標：** 使用 Eurostat 的大學（高等）學歷占比，與本研究暫定的 Eurostat `edat_lfse_03`（高等教育）同類。
- **AI 採用率資料：** 使用 Eurostat 企業 ICT 使用調查的 AI 採用率，可作為「AI 採用」與 AI 專利（創新活動）的對照。

**不能直接套用之處：**
- 研究方向是人力資本 → AI 採用，不是 AI → 經濟成長；不能當作「AI × 人力資本放大成長效果」的實證先例。
- 國家 × 產業橫斷面，只有一年，與本研究的國家年度面板不同。

**相關頁面：** [Filip et al.（2026）](filip-perezgonzalez-setzer-2026-ecb.md)、[Duarte et al.（2026）](duarte-freitas-simoes-2026.md)、[Eurochambres（2026）](eurochambres-2026.md)、[Calvino et al.（2026）](calvino-costa-haerle-2026-oecd.md)、[產業暴露度交互作用](../topics/methods/industry-exposure-interaction.md)

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
