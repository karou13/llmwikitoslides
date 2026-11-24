# LLM Wiki 索引

Agent 的內容索引。Query 時先讀本頁，依摘要判斷要打開哪些頁面；必要時再回查 `RAW/`。

## 研究總覽
- [research-overview.md](research-overview.md)：研究問題、假設、資料、模型、結果、限制六節；目前內容待使用者確認。

## 跨文獻綜合（先讀這裡）
- [AI 指標比較](topics/synthesis/ai-measures.md)：六類 AI 指標（專利、出版物、投資、企業採用率、暴露度／準備度、職缺技能）各自衡量什麼、誰用過、結果為何不同；Duarte 與 Parteka 在專利／出版物上結果相反。
- [方法與資料結構比較](topics/synthesis/methods-data-structures.md)：21 篇來源依資料結構分八類，列出樣本、方法、結果變數；各方法對國家數的要求；三國設計的文獻先例與需使用者決定的部分。
- [來源間的數字差異](topics/synthesis/source-discrepancies.md)：丹麥與德國企業 AI 採用率的各來源數字；Acemoglu、Misch、AIPI 被引述時的不同寫法；各篇內部表格與內文不一致之處。

## 來源筆記：研究類（12 欄）

**國家層級：AI 與經濟成長**
- [Duarte, Freitas & Simões (2026)](sources/duarte-freitas-simoes-2026.md)：Notas Económicas（SJR Q4）。34–35 個 OECD 國家 1995–2017；Panel ARDL + Diff／Sys-GMM；AI 專利 Diff-GMM 短長期皆正向顯著、出版物不顯著；AI × 人力資本交互項多不顯著。AI 變數取自 Parteka 資料包。
- [Kalai, Becha & Helali (2024)](sources/kalai-becha-helali-2024.md)：Journal of Economic Structures（SJR Q2）。30 個歐洲國家（含德荷丹）2000–2021；PMG-ARDL／NARDL；AI 專利對 GDP 成長長期係數 0.217，正負變動效果不對稱。AI 專利口徑未說明；表格與內文數字不一致。
- [Athari et al. (2026)](sources/athari-et-al-2026.md)：Economies（SJR Q2）。德國 2012Q1–2022Q4 單一國家時間序列；NARDL；AI 投資正負變動長期係數皆為正。變數定義前後不一致，資料集未載明。
- [Gambacorta et al. (2025) BIS WP 1321](sources/bis-gambacorta-et-al-2025.md)：工作論文。56 經濟體 × 16 產業，2022–2023 橫斷面；產業 AI 暴露度 × 國家 AIPI 交互項 3.043**；只能回答產業間相對差異。
- [Parteka & Kordalska (2023)](sources/parteka-kordalska-2023.md)：Technovation（SJR Q1）。34–63 國；固定效果 OLS、IV-GMM；AI 專利與勞動生產力成長不顯著，AI 出版物顯著。公開資料包含 AI 專利與出版物指標。
- [Gonzales (2023)](sources/gonzales-2023.md)：Journal of Economic Structures（SJR Q2）。最多 122 國，1970–2019 共 10 個 5 年期；OLS、含時間虛擬變數的固定效果、AH、GMM、FE-IV；AI 專利（Google Patents 全文檢索）對人均 GDP 成長 FE 0.264***；只在 1995–2019 與先進經濟體顯著；人力資本不顯著。
- [Filip, Peréz-González & Setzer (2026) ECB WP 3242](sources/filip-perezgonzalez-setzer-2026-ecb.md)：工作論文。EU26 加美英日，1996–2021 年度；國家 + 年份固定效果、local projections；ICT 投資（非 AI）與人均 GDP 成長正相關（EU26 0.078***）；高所得、高人力資本國家關係較強；德荷丹皆在高所得組。

**國家－產業：人力資本與 AI 採用**
- [Brey & van der Marel (2024)](sources/brey-vandermarel-2024.md)：Economics Letters（SJR Q2）。歐洲國家 × 9 產業，2021 橫斷面；國家與產業固定效果；2012 年大學學歷占比對 2021 年 AI 採用率 0.084**；人力資本約解釋 34.5% 的 AI 採用（作者推算）。

**模擬與情境**
- [Misch et al. (2025) IMF](sources/misch-et-al-2025-imf.md)：工作論文。31 個歐洲國家；Acemoglu 任務模型；偏好情境 5 年累積 TFP 約 1.1%；工資驅動 AI 採用率；法規可使增幅減少 30% 以上。結果為模擬值。

**企業層級**
- [Eurochambres (2026)](sources/eurochambres-2026.md)：工作論文。Eurostat 企業 AI 採用率（E_AI_TANY）× Orbis；產業採用率增 1 個百分點，勞動生產力約增 0.33%；EU 平均採用率 2021 年 7.65% → 2025 年 19.95%。
- [Calvino, Costa & Haerle (2026) OECD](sources/calvino-costa-haerle-2026-oecd.md)：工作論文。15 國官方 ICT 企業調查；AI 採用者生產力溢價 7.7%–31%，控制人力與技術資本後多數國家消失；OECD ICT 彙總資料庫入口。
- [Rammer, Fernández & Czarnitzki (2022)](sources/rammer-fernandez-czarnitzki-2022.md)：Research Policy（SJR Q1）。德國 CIS 2018；2019 年 5.8% 企業主動使用 AI；使用 AI 的企業較可能推出全球首創產品；全經濟推估。
- [Jensen & Schneider (2026)](sources/jensen-schneider-2026.md)：Research Policy（SJR Q1）。丹麥職缺文字 BERT 分類；Data science & AI 職缺占比與生產力、TFP 正相關；數位技能投入後就業增加。資料保密。
- [Renault (2025) IMF](sources/renault-2025-imf-denmark.md)：Selected Issues。丹麥 60% 以上勞工高度暴露於 AI，約 20% 有替代風險；2024 年約 25% 企業使用 AI。

**貿易管道**
- [Lo & Lee (2024)](sources/lo-lee-2024.md)：Annals of Economics and Finance（SJR Q4）。重力模型；AI 出版物強度的貿易彈性 1.01–1.33。
- [Lahmeri (2025)](sources/dergipark-2025-export.md)：SCImago 查無收錄。15 個 OECD 國家 2013–2023；MMQR；AI 投資對出口為負。變數單位不清。
- [Wagner (2025)](sources/wagner-2025.md)：Open Economies Review（SJR Q3）。EU27 製造業企業；大數據分析與出口正相關；德荷丹使用率 5.41%、16.36%、21.33%。

## 來源筆記：報告類（9 欄）
- [Danmarks Nationalbank (2026)](sources/danmarks-nationalbank-2026.md)：丹麥 2025 年 42% 企業使用 AI；AI 投資約占 GDP 2%（2023）；TFP 情境每年 +0.1–1.0 個百分點。
- [TNO (2023)](sources/tno-2023-netherlands-ai-strategy.md)：荷蘭 AI 政策時間軸與經費：SAPAI、NL AIC、AiNed（2.76 億歐元）。
- [ECB OP395](sources/ecb-2025-op395.md)：歐元區 12 國 SAFE 調查；2025 年荷蘭 85%、德國 77% 企業有使用 AI（含試驗性）。
- [Licht & Wohlrabe (2026)](sources/licht-wohlrabe-2026.md)：Applied Economics Letters（SJR Q3）。ifo 調查，德國企業 AI 使用率 2023 年 13.3% → 2024 年 27%。

## 國家
- [Germany](topics/countries/germany.md)：各來源的企業 AI 採用率、國家層級研究、資料缺口。
- [Netherlands](topics/countries/netherlands.md)：企業 AI 採用率、AI 政策時間軸、資料缺口。
- [Denmark](topics/countries/denmark.md)：企業 AI 採用率（多來源並列）、AIPI、AI 投資、生產力趨勢。
- [OECD 基準](topics/countries/oecd.md)：以 OECD 為樣本或基準的來源。

## 方法（狀態皆為候選）
- [Panel ARDL](topics/methods/panel-ardl.md)：短期與長期關係；先例 Duarte、Kalai。
- [Difference-GMM 與 System-GMM](topics/methods/dynamic-panel-gmm.md)：動態面板內生性；先例 Duarte。
- [產業暴露度 × 國家條件交互作用](topics/methods/industry-exposure-interaction.md)：Rajan–Zingales 設計；先例 BIS 1321；需要多國資料。

## 待處理
- `RAW/Rammer_et_al_2022_German_Firm_Innovation_ZEW_DP.pdf` 的內容是 Asatryan et al.（2021）*Favoritism and Firms*，與主題無關，未 ingest；正確原文已另存為 `RAW/Rammer_Fernandez_Czarnitzki_2022_AI_Industrial_Innovation.pdf`。
- `RAW/文獻蒐集總覽.pdf` 為使用者整理筆記，不 ingest。
- JCR 分區全部未查。
