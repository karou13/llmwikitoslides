# AI 指標比較：各來源怎麼衡量 AI，結果有何不同

## 目前綜合
- Wiki 中的來源用了六類 AI 指標：AI 專利、AI 出版物、AI 投資、企業 AI 採用率、AI 暴露度／準備度、職缺 AI 技能需求。它們衡量的是不同概念，不能互相替代，也不能統稱為「AI 採用」。
- 同一篇研究內，換一種 AI 指標，結果就可能改變：[Duarte et al.（2026）](../../sources/duarte-freitas-simoes-2026.md) 專利顯著、出版物不顯著；[Parteka & Kordalska（2023）](../../sources/parteka-kordalska-2023.md) 則是專利不顯著、出版物顯著。
- 國家年度面板研究多用專利或出版物（資料年份長）；真正衡量企業採用率的資料（Eurostat、OECD ICT 調查、ECB、ifo、CIS）年份短，多用於企業層級研究。

## 各類指標與使用的來源

| 指標類型 | 衡量的概念 | 資料來源 | 使用的研究 | 分析層級 |
|---|---|---|---|---|
| AI 專利 | AI 技術的創新產出 | OECD PATS_IPC（IP5、優先權日、分數計數）；Google Patents 全文關鍵詞檢索 | [Duarte](../../sources/duarte-freitas-simoes-2026.md)、[Parteka](../../sources/parteka-kordalska-2023.md)、[Kalai](../../sources/kalai-becha-helali-2024.md)（口徑未說明）、[Gonzales](../../sources/gonzales-2023.md)（Google Patents） | 國家－年；國家－5 年期 |
| AI 出版物 | AI 研究產出 | Elsevier/Scopus（AI Index）；OECD.AI（Microsoft Academic Graph） | [Duarte](../../sources/duarte-freitas-simoes-2026.md)、[Parteka](../../sources/parteka-kordalska-2023.md)、[Lo & Lee](../../sources/lo-lee-2024.md) | 國家－年 |
| AI 投資 | 投入 AI 的金額 | OECD（資料集未載明）；Fonteneau et al. 估算 | [Athari](../../sources/athari-et-al-2026.md)、[Lahmeri](../../sources/dergipark-2025-export.md)、[Danmarks Nationalbank](../../sources/danmarks-nationalbank-2026.md) | 國家－年／季 |
| 企業 AI 採用率 | 企業是否或多深入使用 AI | Eurostat E_AI_TANY；OECD ICT 調查；ECB SAFE；ifo；德國 CIS；Statistics Denmark | [Eurochambres](../../sources/eurochambres-2026.md)、[Calvino](../../sources/calvino-costa-haerle-2026-oecd.md)、[ECB](../../sources/ecb-2025-op395.md)、[Licht & Wohlrabe](../../sources/licht-wohlrabe-2026.md)、[Rammer](../../sources/rammer-fernandez-czarnitzki-2022.md)、[Misch](../../sources/misch-et-al-2025-imf.md)（迴歸依變數）、[Brey & van der Marel](../../sources/brey-vandermarel-2024.md)（依變數，2021） | 企業、國家－產業 |
| AI 暴露度／準備度 | 工作可被 AI 影響的潛在程度；國家採用 AI 的條件 | Felten AIOE（O*NET）；IMF AIPI | [BIS 1321](../../sources/bis-gambacorta-et-al-2025.md)、[Misch](../../sources/misch-et-al-2025-imf.md)、[Renault](../../sources/renault-2025-imf-denmark.md)、[Danmarks Nationalbank](../../sources/danmarks-nationalbank-2026.md) | 職業、產業、國家 |
| 職缺 AI 技能需求 | 企業招募 AI／資料科學人才的比例 | 丹麥線上職缺（HBS Economics） | [Jensen & Schneider](../../sources/jensen-schneider-2026.md) | 企業－年 |

## 支持「AI 與經濟表現正相關」的證據

| 主張 | 來源與位置 | 層級／指標 |
|---|---|---|
| AI 專利與人均 GDP 成長短期、長期正相關（Diff-GMM） | Duarte 表 5，p.13–14 | 國家－年；專利 |
| AI 專利對 GDP 成長長期係數 0.217 | Kalai 表 8，p.17 | 國家－年；專利 |
| AI 專利與 5 年平均人均 GDP 成長正相關（FE 0.264***；只在 1995–2019 與先進經濟體顯著） | Gonzales 表 3、5–6，p.17–25 | 國家－5 年期；專利 |
| 2012 年人力資本較高的國家 × 產業，2021 年 AI 採用率較高（含固定效果 0.084**） | Brey & van der Marel 表 1，p.2 | 國家－產業；Eurostat 採用率（依變數） |
| AI 出版物（存量）與勞動生產力成長正相關 | Parteka 表 6–7，p.8–9 | 國家－年；出版物 |
| 準備度較高的國家，高暴露產業成長較快 | BIS 表 1，p.13 | 國家－產業；暴露度 × 準備度 |
| 產業 AI 採用率增加 1 個百分點，勞動生產力約增 0.33% | Eurochambres 表 1，p.16 | 企業格子；Eurostat 採用率 |
| 使用 AI 的企業較可能推出全球首創產品 | Rammer 表 6，p.8 | 企業；CIS |
| Data science & AI 職缺占比與企業生產力、TFP 正相關 | Jensen & Schneider 表 4–5，p.9 | 企業；職缺技能 |

## 相反或不一致的證據

| 差異 | 來源 | 可能的解釋（測量、樣本、期間、方法） |
|---|---|---|
| AI 專利：Duarte 顯著、Parteka 不顯著 | [Duarte](../../sources/duarte-freitas-simoes-2026.md) vs [Parteka](../../sources/parteka-kordalska-2023.md) | 結果變數不同（人均 GDP 成長 vs 勞動生產力成長）；方法不同（Panel ARDL + GMM vs 固定效果 OLS／IV）；樣本不同（34–35 個 OECD 國家 vs 含非 OECD 國家） |
| AI 出版物：Duarte 基準不顯著、Parteka 顯著 | 同上 | 同上；Duarte 改用存量後出版物轉為顯著（p.27），與 Parteka 存量結果方向一致 |
| AI 專利：Gonzales 顯著、Parteka 不顯著（兩者都用含時間效果的固定效果） | [Gonzales](../../sources/gonzales-2023.md) vs [Parteka](../../sources/parteka-kordalska-2023.md) | 專利口徑不同（Google Patents 全文檢索 vs OECD IP5）；5 年平均 vs 年度；122 國 vs 34 個 OECD 國家；人均 GDP 成長 vs 勞動生產力成長。詳見[方法與資料結構比較](methods-data-structures.md) |
| Duarte 內部：Diff-GMM 顯著、Sys-GMM 不顯著 | [Duarte](../../sources/duarte-freitas-simoes-2026.md) p.12–14 | 估計方法不同；作者指出 Sys-GMM 診斷檢定不理想 |
| 企業 AI 採用者的生產力溢價，控制人力與技術資本後多數國家消失 | [Calvino](../../sources/calvino-costa-haerle-2026-oecd.md) p.9 | 溢價部分反映互補資本，而非 AI 本身 |
| 歐元區 AI 使用者與非使用者生產力整體無顯著差異 | [ECB OP395](../../sources/ecb-2025-op395.md) p.5 | 調查代理指標；只有 ICT 與研發產業顯著 |
| AI 投資：對 GDP 正向（Athari），對出口負向（Lahmeri） | [Athari](../../sources/athari-et-al-2026.md) vs [Lahmeri](../../sources/dergipark-2025-export.md) | 結果變數不同（GDP vs 出口）；單一國家季資料 vs 15 國年資料；AI 投資資料集兩篇都未載明 |

## 尚未解決的問題
- Kalai 的 AI 專利口徑未說明，無法判斷與 Duarte、Parteka 的專利指標是否相同。
- 兩篇使用 OECD AI 投資的研究都沒有載明資料集，無法確認是否為同一序列。
- 企業 AI 採用率的各來源定義差異大（只計主動使用、含試驗性使用、自行判斷），目前沒有一個三國都有、年份夠長的一致序列。

## 對本研究的意涵
- **文獻先例：** 以 AI 專利或出版物作為國家層級 AI 指標，有 Duarte、Parteka、Kalai 等先例，資料可由 [Parteka 資料包](https://doi.org/10.34808/rjk6-ry03) 與 OECD 取得。
- **測量提醒：** 若研究題目使用「AI 採納」，專利與出版物只能作為創新面的代理指標；若要衡量企業採用，需使用 Eurostat 或 OECD ICT 調查等資料，但可用年份較短。
- 選用哪一種指標由使用者決定；本頁只整理各指標的文獻先例與限制。

## 相關 Wiki 頁面
- [方法與資料結構比較](methods-data-structures.md)
- [來源間的數字差異](source-discrepancies.md)
- 國家頁：[Germany](../countries/germany.md)、[Netherlands](../countries/netherlands.md)、[Denmark](../countries/denmark.md)、[OECD](../countries/oecd.md)
