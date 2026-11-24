# 來源間的數字差異：同一件事，不同來源寫的不一樣

## 目前綜合
本頁並列各來源對同一指標或同一篇文獻的不同數字，以及單一來源內部前後不一致之處。依 AGENTS.md 規則，只並列並說明可能原因，不合成為單一數字。引用時應註明採用哪個來源與定義。

## 一、企業 AI 採用率

### Denmark

| 年份 | 數值 | 定義 | 來源 |
|---|---|---|---|
| 2017 | 7% | 丹麥 ICT 調查 | [Calvino（2026）](../../sources/calvino-costa-haerle-2026-oecd.md) Box 4.4，引述 Warzynski |
| 2019 | 6.0% | 10 人以上企業 | [Rammer（2022）](../../sources/rammer-fernandez-czarnitzki-2022.md) p.5，引述 Montagnier et al. 2020 |
| 2021 | 23.89% | Eurostat E_AI_TANY，10 人以上企業 | [Eurochambres（2026）](../../sources/eurochambres-2026.md) p.10 |
| 2021 | 36% | 丹麥 ICT 調查 | [Calvino（2026）](../../sources/calvino-costa-haerle-2026-oecd.md) Box 4.4，引述 Warzynski |
| 2024 | 約 25% | 10 人以上企業（來源未載明） | [Renault（2025）](../../sources/renault-2025-imf-denmark.md) ¶5 |
| 2025 | 42% | Statistics Denmark，10 人以上民間非金融企業 | [Danmarks Nationalbank（2026）](../../sources/danmarks-nationalbank-2026.md) p.5 |

- **差異：** 2021 年 23.89% 與 36% 相差 12 個百分點；Calvino 引述的 2017 年 7% 高於 Rammer 引述的 2019 年 6.0%。
- **可能原因：** 調查題目、AI 技術清單、企業範圍（是否含金融業）、引用的資料版本不同。原文未說明，無法確定。

### Germany

| 年份 | 數值 | 定義 | 來源 |
|---|---|---|---|
| 2019 上半年 | 5.8% | 德國 CIS 2018，只計主動使用，5 人以上企業 | [Rammer（2022）](../../sources/rammer-fernandez-czarnitzki-2022.md) p.4 |
| 2021 | 10.1% | 德國創新調查 | [Rammer（2022）](../../sources/rammer-fernandez-czarnitzki-2022.md) p.13，引述 Rammer 2022 |
| 2023 | 13.3% | ifo Business Survey，未提供 AI 定義 | [Licht & Wohlrabe（2026）](../../sources/licht-wohlrabe-2026.md) p.3 |
| 2024 | 27.0% | 同上 | 同上 |
| 2025 年 12 月 | 77% | ECB SAFE，含試驗性使用 | [ECB OP395](../../sources/ecb-2025-op395.md) p.17 |

- **可能原因：** 定義差異極大。CIS 排除被動使用（如使用內建 AI 的軟體）；ECB 把試驗性使用也算進去；ifo 由受訪者自行判斷。數字上升同時反映 AI 擴散與定義差異，不能直接解讀為成長幅度。

## 二、同一篇文獻被引述時的差異

| 被引述的內容 | 寫法 A | 寫法 B | 說明 |
|---|---|---|---|
| Acemoglu（2024）美國 TFP 估計 | 十年累積約 0.71%（[Misch](../../sources/misch-et-al-2025-imf.md) p.9；[Eurochambres](../../sources/eurochambres-2026.md) p.8）；每年 0.07%、為期十年（[BIS 1321](../../sources/bis-gambacorta-et-al-2025.md) p.6） | 每年 0.7%（[Licht & Wohlrabe](../../sources/licht-wohlrabe-2026.md) p.4，引述 Acemoglu 2025） | 寫法 A 的三者互相一致；寫法 B 引述的是 Acemoglu 2025，可能是不同文獻或引述錯誤，需查 Acemoglu 原文 |
| Misch et al.（2025）對 Denmark 的估計 | Misch 原文定義為 5 年中期累積 TFP 增幅（p.6 註 1） | 每年增加 0.4 個百分點（[Danmarks Nationalbank](../../sources/danmarks-nationalbank-2026.md) p.18 註 17） | 時間定義不同；Misch 原文的丹麥個別數值只出現在圖中，正文未列 |
| IMF AIPI 的組成方式 | 四構面加總（[BIS 1321](../../sources/bis-gambacorta-et-al-2025.md) p.10） | 四構面簡單平均（IMF AIPINote p.2） | 以 IMF 原始說明為準 |

## 三、單一來源內部的不一致

| 來源 | 位置 A | 位置 B |
|---|---|---|
| [Duarte（2026）](../../sources/duarte-freitas-simoes-2026.md) | 正文 35 國（p.7） | 基準估計表 34 國（p.14）；交互作用表 35 國（p.35） |
| [BIS 1321](../../sources/bis-gambacorta-et-al-2025.md) | 56 經濟體 × 16 產業 = 896 | 迴歸觀測值 875（表 1） |
| [Kalai（2024）](../../sources/kalai-becha-helali-2024.md) | 表 8：AI 長期係數 0.217、R&D 0.325 | 內文 0.247%、0.365%（p.18） |
| [Kalai（2024）](../../sources/kalai-becha-helali-2024.md) | 內文：長期所有變數皆顯著 | 表 8：Inflation p = 0.134、FDI p = 0.054 |
| [Wagner（2025）](../../sources/wagner-2025.md) | 內文：目的地數量差異 +0.701（p.6） | 表 5：0.717（p.8） |
| [Lo & Lee（2024）](../../sources/lo-lee-2024.md) | 摘要：AI 彈性 1.01%–1.30% | 表 3 第 (3) 欄 1.33 |
| [Eurochambres（2026）](../../sources/eurochambres-2026.md) | 內文：影像辨識 n = 11,852 | 圖 5 標籤：n = 11652 |
| [Rammer（2022）](../../sources/rammer-fernandez-czarnitzki-2022.md) | 流程創新成本節省 €11.4 billion（p.2） | €11.3 billion（p.13） |
| [Athari（2026）](../../sources/athari-et-al-2026.md) | 正文：GDP、勞動參與、GFCF 占 GDP % | 表 2：人均 GDP、勞動力人數、GFCF 現值美元 |
| [Parteka（2023）](../../sources/parteka-kordalska-2023.md) | 表註：*、**、*** = 1%、5%、10% | 與一般慣例相反 |
| [Gonzales（2023）](../../sources/gonzales-2023.md) | 表 3：AI 專利模型 616 筆、122 國；總專利模型 1,140 筆、144 國 | 表 1 描述統計：人均 GDP 成長率 1,936 筆、208 國（各表樣本依變數可得性不同，原文未逐一說明） |
| [Filip（2026）](../../sources/filip-perezgonzalez-setzer-2026-ecb.md) | 表 2：EU26 593 筆、29 國 667 筆 | 表 3：595 筆、669 筆；表 1 描述統計 697–754 筆（原文未說明差異） |

## 尚未解決的問題
- 丹麥 2021 年企業 AI 採用率的兩個數字（23.89% 與 36%）來源不同，需查 Eurostat 與 Statistics Denmark 原始資料確認。
- Licht & Wohlrabe 引述的 Acemoglu（2025）需查原文。

## 對本研究的意涵
- 若以企業 AI 採用率作為變數，三國必須使用同一調查、同一定義的序列；不同來源的數字不能拼接。
- 引用單一數字時，應同時寫出年份、定義與來源。

## 相關 Wiki 頁面
- [AI 指標比較](ai-measures.md)
- [方法與資料結構比較](methods-data-structures.md)
- 國家頁：[Germany](../countries/germany.md)、[Denmark](../countries/denmark.md)
