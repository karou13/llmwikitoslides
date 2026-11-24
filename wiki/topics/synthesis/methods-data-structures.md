# 方法與資料結構比較：各來源用什麼資料、什麼模型、能回答什麼

## 目前綜合
- Wiki 中的來源依資料結構可分為八類：國家年度面板、國家 5 年期面板、單一國家時間序列、國家－產業橫斷面、企業層級資料、雙邊貿易資料、模型模擬、描述分析。
- 直接以「國家經濟成長」為結果的研究有國家年度面板（Duarte、Kalai、Filip）、國家 5 年期面板（Gonzales）與單一國家時間序列（Athari）；其他研究的結果是產業附加價值、生產力、創新、出口、就業或 AI 採用。
- 以「國家 + 年份固定效果」估計成長或生產力的先例有三篇：Parteka（AI 專利／出版物 → 勞動生產力成長）、Gonzales（AI 專利 → 人均 GDP 成長，含時間虛擬變數）、Filip（ICT 投資 → 人均 GDP 成長，歐洲 26–29 國）。
- 多數國家層級方法（GMM、PMG、Rajan–Zingales 交互作用）依賴「很多國家」才能識別；國家數少時，文獻中有先例的做法是單一國家時間序列。

## 依資料結構分類

| 資料結構 | 來源 | 樣本 | 方法 | 結果變數 | 模型回答的問題 |
|---|---|---|---|---|---|
| 國家年度面板 | [Duarte（2026）](../../sources/duarte-freitas-simoes-2026.md) | 34–35 個 OECD 國家，1995–2017 | Panel ARDL；Diff-GMM、Sys-GMM | 人均 GDP 成長 | AI 指標變動與成長的短期、長期關係 |
| 國家年度面板 | [Kalai（2024）](../../sources/kalai-becha-helali-2024.md) | 30 個歐洲國家，2000–2021 | PMG-ARDL、PMG-NARDL | GDP 成長率 | 同上，並區分 AI 增加與減少的不對稱效果 |
| 國家年度面板 | [Parteka（2023）](../../sources/parteka-kordalska-2023.md) | 34–63 國，1985–2017 | 國家與年份固定效果 OLS；IV-GMM | 勞動生產力成長 | AI 技術生產與生產力成長的關係 |
| 國家 5 年期面板 | [Gonzales（2023）](../../sources/gonzales-2023.md) | 最多 122 國，1970–2019，10 期 | OLS；含時間虛擬變數的固定效果；AH；GMM；FE-IV | 人均實質 GDP 成長（5 年平均） | AI 專利與長期成長；先進與較不先進經濟體是否不同 |
| 國家年度面板 | [Filip（2026）](../../sources/filip-perezgonzalez-setzer-2026-ecb.md) | EU26（+ 美英日共 29 國），1996–2021 | 國家與年份固定效果；panel local projections | 人均實質 GDP 成長 | 各類投資（含 ICT）與成長；是否因所得、人力資本而不同 |
| 國家年度面板 | [Lahmeri（2025）](../../sources/dergipark-2025-export.md) | 15 個 OECD 國家，2013–2023 | MMQR 分量迴歸 | 出口占 GDP | AI 投資效果是否隨出口表現高低而不同 |
| 單一國家時間序列 | [Athari（2026）](../../sources/athari-et-al-2026.md) | Germany，44 季 | NARDL、ARDL bounds test | GDP | AI 投資正負變動對成長的長期影響 |
| 國家－產業橫斷面 | [BIS 1321（2025）](../../sources/bis-gambacorta-et-al-2025.md) | 56 經濟體 × 16 產業，2022–2023 | OLS，國家與產業固定效果 | 產業附加價值成長 | 準備度高的國家中，高暴露產業是否相對成長較快 |
| 國家－產業橫斷面 | [Brey & van der Marel（2024）](../../sources/brey-vandermarel-2024.md) | 歐洲國家 × 9 產業，2021（88–267 筆） | OLS，國家與產業固定效果 | 企業 AI 採用率 | 人力資本是否決定 AI 採用 |
| 企業層級 | [Eurochambres（2026）](../../sources/eurochambres-2026.md) | 32 國企業格子，2020–2024 | 固定效果 OLS | 勞動生產力 | 產業 AI 採用率與企業生產力 |
| 企業層級 | [Calvino（2026）](../../sources/calvino-costa-haerle-2026-oecd.md) | 15 國企業微觀資料，2017–2023 | 線性機率模型；生產力迴歸 | AI 採用、生產力 | 誰採用 AI；採用者生產力溢價 |
| 企業層級 | [Jensen & Schneider（2026）](../../sources/jensen-schneider-2026.md) | 丹麥企業，2008–2019 | 企業固定效果；lead–lag | 生產力、就業 | AI 技能投入後的就業動態 |
| 企業層級 | [Rammer（2022）](../../sources/rammer-fernandez-czarnitzki-2022.md) | 德國企業，CIS 2018 | 加權 Probit、OLS | 產品與流程創新 | AI 使用與創新產出 |
| 企業層級 | [Wagner（2025）](../../sources/wagner-2025.md) | EU27 製造業企業，2019 | Probit、OLS | 出口 | 大數據分析與出口 |
| 企業層級 | [Licht & Wohlrabe（2026）](../../sources/licht-wohlrabe-2026.md) | 德國企業，2023–2024 | 線性機率模型 | AI 採用 | 經理人特質與 AI 採用 |
| 雙邊貿易 | [Lo & Lee（2024）](../../sources/lo-lee-2024.md) | 國家對，497,636 筆 | 重力模型（Eaton–Kortum 兩階段） | 進口占比、出口能力 | 數位化與 AI 強度對貿易的彈性 |
| 模型模擬 | [Misch（2025）](../../sources/misch-et-al-2025-imf.md)、[Danmarks Nationalbank（2026）](../../sources/danmarks-nationalbank-2026.md) | 31 個歐洲國家；Denmark | Acemoglu／Bergeaud 任務模型 | TFP（推算） | 在假設下 AI 可能帶來的 TFP 增幅 |
| 描述分析 | [Renault（2025）](../../sources/renault-2025-imf-denmark.md)、[ECB OP395](../../sources/ecb-2025-op395.md) | Denmark 勞工；歐元區 12 國企業 | 描述統計 | 暴露度、採用程度 | 現況描述 |

## 各方法對國家數與期間的要求

| 方法 | 文獻中的國家數與期間 | 國家數少時的問題 | 來源 |
|---|---|---|---|
| Diff-GMM／Sys-GMM | 34 國 × 23 年 | 工具變數數量須低於國家數（原文 24／30 個工具變數） | [Duarte](../../sources/duarte-freitas-simoes-2026.md) p.12 |
| PMG-ARDL／NARDL | 30 國 × 22 年 | 長期係數由多國匯集估計 | [Kalai](../../sources/kalai-becha-helali-2024.md) |
| 國家與年份固定效果 | 34 國以上（Parteka）；26–29 國 × 26 年（Filip）；122 國 × 10 期（Gonzales） | 國家數少時固定效果吸收大部分變異；加入落後期依變數時有 Nickell 偏誤（Gonzales p.12） | [Parteka](../../sources/parteka-kordalska-2023.md)、[Filip](../../sources/filip-perezgonzalez-setzer-2026-ecb.md) p.12–14、[Gonzales](../../sources/gonzales-2023.md) p.12–17 |
| 狀態依存 local projections | 29 國 × 26 年 | Filip 說明不必切分樣本，適合時間維度短的資料；以 split-panel jackknife 取代 GMM | [Filip](../../sources/filip-perezgonzalez-setzer-2026-ecb.md) p.23, 26 |
| Rajan–Zingales 交互作用 | 56 經濟體 | 國家層級變異來自國家數；標準誤在國家層級群聚 | [BIS 1321](../../sources/bis-gambacorta-et-al-2025.md) |
| NARDL 時間序列 | 單一國家 44 季 | 自由度有限；只能分析單一國家 | [Athari](../../sources/athari-et-al-2026.md) |

## 不一致之處與可能原因
- 國家層級研究多發現 AI 指標與成長或生產力正相關，但 Parteka 的專利結果不顯著；Calvino 與 ECB 在企業層級控制互補因素後，生產力溢價多半消失或不顯著。差異可能來自分析層級（國家 vs 企業）、AI 指標（創新產出 vs 採用）、控制變數（是否控制人力與技術資本）。
- Gonzales 的 AI 專利在含時間虛擬變數的固定效果中顯著為正（0.264***），Parteka 的 AI 專利在國家與年份固定效果 OLS 中不顯著。可能原因：專利口徑（Google Patents 全文檢索 vs OECD IP5 專利家族）、期間結構（5 年平均 vs 年度）、樣本（含大量開發中國家的 122 國 vs 34 個 OECD 國家）、結果變數（人均 GDP 成長 vs 勞動生產力成長）。Gonzales 在先進經濟體中仍顯著（表 6），因此樣本含開發中國家不能完全解釋差異；原因尚無法確定。
- 幾乎所有作者都聲明結果是相關而非因果；Parteka 以 IV 處理反向因果，但部分工具變數未通過識別檢定（p.9 註 18）。

## 尚未解決的問題
- 尚無任何來源同時以國家年度資料、企業 AI 採用率、GDP 成長三者估計模型。
- Kalai 與 Duarte 同屬 Panel ARDL，但使用的估計器（PMG vs GMM）與 AI 專利口徑不同，結果無法直接比較。

## 對本研究的意涵
- **文獻先例：**
  - 國家年度面板 + AI 專利或出版物 + GDP 成長：Duarte、Kalai（Panel ARDL／GMM）；Gonzales（5 年期面板，含時間虛擬變數的固定效果）。
  - 國家 + 年份固定效果 + 成長率：Parteka（AI，生產力成長）、Filip（ICT 投資，人均 GDP 成長）。
  - 技術效果的跨國異質性：Gonzales 的先進經濟體 × AI 專利、分組估計；Filip 的所得分組與人力資本狀態依存模型。
  - 單一國家時間序列：Athari（德國）。
  - 人力資本交互作用：Duarte 的 AI × 人力資本（p.32）；BIS 的 AIPI 含人力資本構面；Filip 的高、低人力資本狀態依存模型（ICT 投資）。
  - 人力資本影響 AI 採用的機制：Brey & van der Marel（國家 × 產業，2021）。
- **需由使用者決定、屬本研究延伸的部分：** 若以三國為主要比較對象，是採用 OECD 面板並另外比較三國，或對三國分別做時間序列，目前 Wiki 中沒有直接相同設計的先例。
- 方法狀態皆為「候選」，見各方法頁。

## 相關 Wiki 頁面
- [AI 指標比較](ai-measures.md)
- [來源間的數字差異](source-discrepancies.md)
- 方法頁：[Panel ARDL](../methods/panel-ardl.md)、[動態面板 GMM](../methods/dynamic-panel-gmm.md)、[產業暴露度交互作用](../methods/industry-exposure-interaction.md)
