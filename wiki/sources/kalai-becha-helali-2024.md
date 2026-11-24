---
type: source
title_original: "Effect of artificial intelligence on economic growth in European countries: a symmetric and asymmetric cointegration based on linear and non-linear ARDL approach"
authors: ["Maha Kalai", "Hamdi Becha", "Kamel Helali"]
year: 2024
source_type: 期刊論文
journal: "Journal of Economic Structures"
quartile: "SJR 2025 Q2, Economics, Econometrics and Finance (miscellaneous)"
doi: "10.1186/s40008-024-00345-y"
raw_file: "RAW/s40008-024-00345-y.pdf"
relevance: 核心實證
processing_status: 已寫入
countries: ["Europe (30 countries)", "Germany", "Netherlands", "Denmark"]
methods: ["PMG-ARDL", "PMG-NARDL", "Dumitrescu–Hurlin 因果檢定"]
ai_measure: "AI 相關技術專利（OECD）"
outcome: "實質 GDP 成長率（年 %）"
---

# Effect of artificial intelligence on economic growth in European countries: a symmetric and asymmetric cointegration based on linear and non-linear ARDL approach — Kalai, Becha & Helali（2024）

> 頁碼為 PDF 頁碼（與期刊頁碼 Page x of 37 相同）。

## 1. 來源
- **書目：** Kalai, M., Becha, H., & Helali, K. (2024). Effect of artificial intelligence on economic growth in European countries: a symmetric and asymmetric cointegration based on linear and non-linear ARDL approach. *Journal of Economic Structures*, 13, 22. https://doi.org/10.1186/s40008-024-00345-y
- **期刊：** Journal of Economic Structures（Springer Nature／SpringerOpen 出版）。同儕審查期刊（[Aims and scope](https://link.springer.com/journal/40008/aims-and-scope)）。分區：SJR 2025 Q2，Economics, Econometrics and Finance (miscellaneous)（[SCImago](https://www.scimagojr.com/journalsearch.php?q=Journal+of+Economic+Structures)）。

## 2. 研究目的
檢驗 2000–2021 年 30 個歐洲國家中，AI 對經濟成長的影響是對稱還是不對稱（p.1, 3）。

## 3. 研究貢獻
- 歐洲的 AI 與經濟成長關係較少被研究；既有研究多聚焦 G7、BRICS、大型跨國面板或中國、台灣、美國（p.3）。
- 既有研究未使用不對稱共整合模型；本文以 PMG-NARDL 分析 AI 正向與負向變動對成長的不同效果（p.3）。

## 4. 研究背景
- AI 可提升生產力、品質與流程速度，但也可能造成失業、市場集中、訓練成本上升與隱私風險（p.2）。
- AI 可能出現生產力悖論，對技術創新與製造效率的效果尚無共識（p.2–3）。
- 歐盟對 AI 的投入：Horizon 2020 在 2018–2020 年投入 15 億歐元；Digital Europe Program（2021–2027）投入 25 億歐元；EIB 設立 1.5 億歐元共同投資機制（p.3）。

## 5. 研究問題
AI 對歐洲國家經濟成長的長期與短期效果為何？此效果是對稱還是不對稱？AI 與經濟成長之間的因果方向為何？（p.3, 8）

## 6. 研究假設
原文列出兩項假設（p.7–8）：
- **H1（原文 H01）：** AI 對歐洲經濟成長的影響是對稱的。
- **H2（原文 H02）：** AI 對歐洲經濟成長的影響是不對稱的。

## 7. 樣本與研究期間
- **分析單位：** 國家－年，年度資料。
- **樣本：** 30 個歐洲國家，N = 30、T = 22，2000–2021 年（p.12）。
- **國家名單：** Germany、Austria、Belgium、Bulgaria、Cyprus、Croatia、Denmark、Spain、Estonia、Finland、France、Greece、Hungary、Ireland、Italy、Latvia、Lithuania、Luxembourg、Malta、Norway、Netherlands、Poland、Portugal、Romania、United Kingdom、Slovakia、Slovenia、Sweden、Switzerland、Czech（p.12）。
- **觀測值：** 660 筆（p.16）。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| `GDPG` | GDP 成長率（年 %）（表 1，p.12） | [World Bank World Development Indicators](https://databank.worldbank.org/source/world-development-indicators) | — | World Bank |
| `Activity` | 勞動參與率：工作人口占 15 歲以上工作年齡人口比率（表 1） | WDI | — | World Bank |
| `GFCF` | 固定資本形成毛額（占 GDP %）（表 1） | WDI | — | World Bank |
| `Inflation` | 通膨率（消費者物價指數 %）（表 1） | WDI | — | World Bank |
| `FDI` | 外人直接投資淨流入（占 GDP %）（表 1） | WDI | — | World Bank |
| `R&D` | 研發支出（占 GDP %）（表 1） | WDI | — | World Bank |
| `AI` | AI 相關技術專利（表 1，p.11–12） | OECD 專利資料集；原文未載明資料集名稱或網址 | 原文未說明 AI 專利的辨識方式、計數方式（申請人或發明人歸屬、IP5 或其他）與單位；描述統計平均 13.164、最小 0、最大 150.262（表 2，p.14） | OECD |

- **資料取得：** 作者聲明資料可向通訊作者索取（p.32）。估計使用 Stata 17.0（p.32）。

## 9. 研究方法
**基本模型（式 9，p.12）：**
`GDPG_it = β0 + β1 Activity_it + β2 GFCF_it + β3 Inflation_it + β4 FDI_it + β5 AI_it + β6 R&D_it + λ_i + µ_t + ε_it`

| 符號 | 定義 |
|---|---|
| `GDPG_it` | 國家 i 在 t 年的 GDP 成長率 |
| `AI_it` | AI 相關技術專利 |
| `λ_i`、`µ_t` | 國家效果、年份效果 |
| 其他 | 勞動參與率、資本形成、通膨、FDI、研發支出 |

**PMG-ARDL（式 10–11，p.13）：**
- 將上式改寫為誤差修正形式：差分項估計短期效果，落後水準項估計長期關係；`ρ1`（ECT）為誤差修正項，預期顯著為負，代表回到長期均衡的調整速度。
- PMG（Pooled Mean Group）：長期係數各國相同，短期係數與調整速度各國可不同（Pesaran et al. 1999）。
- 選定 ARDL(1,0,0,0,0,0,0)，無限制常數項、無趨勢（p.17）。

**PMG-NARDL（式 12–14，p.13–14）：**
- 將 AI 拆為正向累積變動 `AI+`（Σ max(ΔAI, 0)）與負向累積變動 `AI−`（Σ min(ΔAI, 0)），分別估計係數（Shin et al. 2014）。
- 以 Wald 檢定比較長期與短期的 `AI+`、`AI−` 係數是否相等（式 15，p.15）。
- 選定 NARDL(1,0,0,0,0,0,0,0)（p.19）。

**前置檢定（p.15–17）：**
- 橫斷面相依檢定（Friedman、Breusch–Pagan、Frees、Pesaran 等）：全部拒絕獨立（表 3）。
- 第二代單根檢定（Pesaran 2003、2007）與含結構斷點的 Karavias–Tzavalis（2014）：所有變數一階差分後平穩，部分變數水準值已平穩（表 4–5）。
- 共整合檢定：Kao（1999）與 Pedroni（2004）拒絕「無共整合」；Westerlund（2007）未拒絕（p = 0.373）（表 6，p.16）。

**因果檢定：** Dumitrescu–Hurlin（2012）異質面板 Granger 因果檢定（p.21）。

## 10. 研究結果
**原文結果：**
- **PMG-ARDL 短期（表 7，p.16）：** AI(t−1) 係數 0.200（p = 0.020）；ECT −0.182（p = 0.000），作者解讀為約 5 年 6 個月回到均衡（p.17）。
- **PMG-ARDL 長期（表 8，p.17）：**

| 變數 | 係數 | p 值 |
|---|---|---|
| Activity | 0.110 | 0.004 |
| GFCF | 0.122 | 0.001 |
| Inflation | −0.093 | 0.134 |
| FDI | 0.367 | 0.054 |
| AI | 0.217 | 0.000 |
| R&D | 0.325 | 0.006 |

- **PMG-NARDL 短期（表 9，p.18）：** `AI+` 0.133（p = 0.028）；`AI−` −0.185（p = 0.643）；ECT −0.175；短期不對稱檢定 7.14（p = 0.008）。
- **PMG-NARDL 長期（表 10，p.19）：** `AI+` 0.026（p = 0.004）；`AI−` −0.029（p = 0.016）；長期不對稱檢定 5.33（p = 0.021）。
- **因果檢定（表 11，p.21）：** AI → GDPG 顯著（p = 0.000），GDPG → AI 不顯著（p = 0.173）；AI+ 與 GDPG 雙向皆顯著；AI− 與 GDPG 雙向皆不顯著。

**原文內部不一致之處：**
- 表 8 的 AI 長期係數為 0.217，內文寫為 0.247%；表 8 的 R&D 為 0.325，內文寫為 0.365%（p.18）。摘要使用 0.217（p.1）。
- 內文寫「長期所有變數皆正向且顯著」，但表 8 中 Inflation 的 p 值為 0.134、FDI 為 0.054（p.17–18）。
- Westerlund（2007）檢定未拒絕無共整合，作者仍以 Kao 與 Pedroni 的結果認定存在共整合（表 6）。

**作者解釋：**
- ARDL 結果支持 H1（對稱關係），NARDL 結果支持 H2（不對稱關係）：AI 正向變動提升成長，負向變動降低成長（p.22, 25）。
- AI 對成長的因果方向為單向，由 AI 指向經濟成長（p.21–22, 30）。

## 11. 研究限制
作者列出（p.31–32）：
- 使用特定國家的總體資料，對技術發展、政策或制度不同的經濟體適用性有限。
- 未分析產業別差異（製造、醫療、金融、服務等）。
- 未使用門檻模型（PTAR、PSTAR）捕捉 AI 低、中、高發展程度下的非線性效果。

作者另指出 AI 專利的衡量問題：並非所有 AI 進展都會申請專利，專利品質不一，且從申請到經濟效益實現有時間落差（p.12）。

## 12. 關聯
**可參考之處：**
- 樣本明確包含 Germany、Netherlands、Denmark，是目前 Wiki 中唯一同時涵蓋三國並以 GDP 成長為結果的國家年度面板研究。
- 以 AI 專利為 AI 指標、GDP 成長為結果，搭配 Panel ARDL 拆分短長期，與 Duarte et al.（2026）屬同一類設計，可互相對照。Duarte 的表 1 也將本文列為先行研究。
- NARDL 的正負變動拆分提供另一種非線性設定。
- 控制變數（勞動參與、資本形成、通膨、FDI、R&D）皆來自 WDI，取得容易。

**套用此模型所需資料：**

| 資料 | 來源 | 取得狀態 |
|---|---|---|
| GDP 成長、勞動參與、資本形成、通膨、FDI、R&D | [World Bank WDI](https://databank.worldbank.org/source/world-development-indicators) | 公開 |
| AI 專利 | OECD 專利資料 | 原文未說明資料集與篩選條件，需另外決定口徑（可參考 [Parteka & Kordalska 2023](parteka-kordalska-2023.md) 的定義） |

**不能直接套用之處：**
- PMG 估計依賴多國（原文 30 國）匯集長期係數；只有三國時難以支撐。
- AI 專利的口徑不明，結果難以與其他研究比較。
- 原文表格與內文數字不一致，引用時以表格數值為準並註明。
- 專利衡量 AI 創新，不是企業採用率。

**相關頁面：** [Duarte et al.（2026）](duarte-freitas-simoes-2026.md)、[Panel ARDL](../topics/methods/panel-ardl.md)、[OECD 國家頁](../topics/countries/oecd.md)

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
