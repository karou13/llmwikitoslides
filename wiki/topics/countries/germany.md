# Germany

## 在研究中的角色
本研究的三個比較國家之一，與 Netherlands、Denmark 並列，並以 OECD 為基準。

## AI 指標與採用現況
不同來源的 AI 定義不同，數值不能直接比較。

| 指標 | 數值 | 年份 | 定義 | 來源 |
|---|---|---|---|---|
| 主動使用 AI 的企業比例 | 5.8% | 2019 上半年 | 德國 CIS 2018，只計主動使用，5 人以上企業 | [Rammer et al.（2022）](../../sources/rammer-fernandez-czarnitzki-2022.md) |
| 同上 | 10.1% | 2021 | 德國創新調查（Rammer et al. 引述） | [Rammer et al.（2022）](../../sources/rammer-fernandez-czarnitzki-2022.md) |
| 使用 AI 的企業比例 | 13.3% → 27.0% | 2023 → 2024 | ifo Business Survey，自評「使用中」，未提供 AI 定義 | [Licht & Wohlrabe（2026）](../../sources/licht-wohlrabe-2026.md) |
| 有使用 AI 的企業比例 | 77%（中度或顯著 47%） | 2025 年 12 月 | ECB SAFE，含試驗性使用 | [ECB OP395](../../sources/ecb-2025-op395.md) |
| 製造業企業的大數據分析使用率 | 5.41% | 2020 年調查 | Flash Eurobarometer 486 | [Wagner（2025）](../../sources/wagner-2025.md) |
| 企業 AI 使用（官方 ICT 調查） | AI 資料年份為 2018、2020 | — | 是否使用 AI（二元） | [Calvino et al.（2026）](../../sources/calvino-costa-haerle-2026-oecd.md) |

- Calvino et al.（2026）指出，Germany 是 15 國中唯一 ICT 產業不是 AI 採用率最高產業的國家（p.23）。

## GDP、生產力與控制變數資料
目前 Wiki 中涵蓋 Germany 的國家層級研究使用的資料：
- [Kalai et al.（2024）](../../sources/kalai-becha-helali-2024.md)：World Bank WDI 的 GDP 成長、勞動參與、資本形成、通膨、FDI、R&D；OECD AI 專利；2000–2021。
- [Athari et al.（2026）](../../sources/athari-et-al-2026.md)：OECD AI 投資、World Bank 的 GDP、勞動力、資本形成；2012Q1–2022Q4。
- [Duarte et al.（2026）](../../sources/duarte-freitas-simoes-2026.md)、[Parteka & Kordalska（2023）](../../sources/parteka-kordalska-2023.md)：OECD 國家面板，Germany 屬於 OECD 樣本。

## 相關文獻與發現
- **Athari et al.（2026）：** AI 投資的正向與負向變動，長期係數都為正（0.034、0.036）；勞動力正向變動效果最大。
- **Kalai et al.（2024）：** 30 國面板中，AI 專利對 GDP 成長的長期係數為 0.217。
- **Rammer et al.（2022）：** 使用 AI 的企業推出全球首創產品的機率高 2.3 個百分點；與 AI 相關的全球首創產品銷售約占全德國的 18.1%（約 161 億歐元）。
- **Licht & Wohlrabe（2026）：** 德國企業預期五年生產力提升約 8%（自家企業）至 12%（整體經濟），屬主觀預期。

## 與 OECD 基準的可比性
- AI 專利與出版物：可使用與 Duarte、Parteka 相同的 OECD 專利與 Scopus 資料，與 OECD 其他國家可比。
- 企業 AI 採用率：ifo、ECB、Eurostat 的定義不同，跨國比較應使用同一調查。

## 資料缺口與限制
- 尚未取得 Germany 的 Eurostat 企業 AI 採用率年度序列（Eurochambres 圖 2 有 2021 與 2025 年數值，但正文未列出）。
- Athari et al. 的變數定義在正文與表格之間不一致，資料來源未逐一對應。

## 相關來源與方法
- 樣本含本國的國家面板：[Filip et al.（2026）](../../sources/filip-perezgonzalez-setzer-2026-ecb.md)（EU26，1996–2021；本國屬高所得組，p.19–20）
- 方法：[Panel ARDL](../methods/panel-ardl.md)
- 國家：[Netherlands](netherlands.md)、[Denmark](denmark.md)、[OECD 基準](oecd.md)
