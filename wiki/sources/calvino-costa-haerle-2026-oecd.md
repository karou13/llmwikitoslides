---
type: source
title_original: "Digital technology diffusion in the age of AI: Cross-country evidence from microdata"
authors: ["Flavio Calvino", "Hélder Costa", "Daniel Haerle"]
year: 2026
source_type: 工作論文
journal: "OECD Science, Technology and Industry Working Papers 2026/01"
quartile: "不適用"
doi: "10.1787/ebc2debe-en"
raw_file: "RAW/OECD_2026_Digital_Technology_Diffusion_Microdata.pdf"
relevance: 方法參考
processing_status: 已寫入
countries: ["OECD (15 countries)", "Germany", "Netherlands", "Denmark"]
methods: ["線性機率模型（採用決定因素）", "企業生產力溢價迴歸", "分散式微觀資料（Digital Diffuse）"]
ai_measure: "企業是否使用 AI（官方 ICT 調查，二元變數）"
outcome: "AI 採用機率；企業勞動生產力（營業額／從業人數）"
---

# Digital technology diffusion in the age of AI: Cross-country evidence from microdata — Calvino, Costa & Haerle（2026）

> 頁碼為 PDF 頁碼（與報告內頁碼相同）。

## 1. 來源
- **書目：** Calvino, F., Costa, H., & Haerle, D. (2026). Digital technology diffusion in the age of AI: Cross-country evidence from microdata. *OECD Science, Technology and Industry Working Papers*, 2026/01. OECD Publishing. https://dx.doi.org/10.1787/ebc2debe-en
- **類型：** OECD 工作論文，非期刊論文，期刊分區不適用。原文說明 OECD 工作論文為初步結果或進行中的研究，觀點不代表 OECD 會員國官方立場（p.2）。

## 2. 研究目的
分析 15 個 OECD 國家企業對 AI、大數據分析、物聯網（IoT）、機器人與 3D 列印的使用情形，探討採用者的特徵、人力與技術資本等促進因素，以及技術使用與企業生產力的關係（p.3, 8）。

## 3. 研究貢獻
- 以官方、具代表性的企業微觀資料，在統一方法下做跨國比較（p.8, 12）。
- 相較 Calvino & Fontanelli（2023），技術範圍由 AI 擴大到五種先進數位技術，並加入更多人力資本（教育、職業）與技術資本指標、更多生產力衡量與國家（p.12）。
- 採用分散式微觀資料方法（Digital Diffuse），在保密限制下產出可比較的跨國結果（p.12, 19）。

## 4. 研究背景
- OECD 國家企業採用先進數位技術的比例近年上升，但總體趨勢掩蓋國家、產業、企業之間的大幅差異（p.11）。
- AI 可能是通用目的技術，能自動化認知任務並放大其他技術的潛力（p.11）。
- 理解 AI 擴散模式對總體成長很重要（p.12）。

## 5. 研究問題
哪些企業特徵與先進數位技術（含 AI）的採用有關？人力資本與技術資本扮演什麼角色？採用者是否比非採用者更有生產力，這個差距能否由人力與技術資本解釋？（p.8, 20）

## 6. 研究假設
原文未列研究假設；以七項「典型事實」（stylised facts）呈現結果（p.8–9）。

## 7. 樣本與研究期間
- **國家（15 國）：** Belgium、Canada、Denmark、Estonia、France、Germany、Ireland、Israel、Italy、Japan、Korea、Netherlands、Portugal、Switzerland、United Kingdom（p.8, 11）。
- **期間：** ICT 調查涵蓋 2017–2023 年，尚未完整捕捉生成式 AI 熱潮（p.8）。
- **資料結構：** 多為重複橫斷面調查，分層抽樣，通常涵蓋 10 人以上企業（p.18）。
- **三國的 AI 資料年份（附錄表 B.2，p.69–70）：**
  - Denmark：AI 2016–2018、2020。
  - Germany：AI 2018、2020。
  - Netherlands：AI 2019–2021。
- **加權：** Germany 的部分迴歸未加權（p.42）。

## 8. 資料與變數

| 變數 | 定義／衡量方式 | 原始資料庫 | 篩選條件 | 指標建構者 |
|---|---|---|---|---|
| 技術使用 | 企業是否使用 AI、大數據、IoT、機器人、3D 列印（二元變數）（p.18） | 各國統計機關的官方 ICT 企業調查微觀資料；彙總統計見 [OECD ICT Access and Usage by Businesses database](https://data-explorer.oecd.org/s/3il)（p.11 圖 1.1 註） | 各國定義與年份不同，需注意可比性（p.18） | 各國統計機關；Netherlands 由 Statistics Netherlands（CBS）人員執行（p.69） |
| 勞動生產力 | 營業額 ÷ 從業人數，取對數；穩健性改用附加價值 ÷ 從業人數（p.39） | ICT 調查；附加價值來自可合併的資產負債表資料 | — | 同上 |
| 人力資本 | 是否有 ICT 專業人員、是否對非 ICT 人員提供 ICT 訓練（ICT 調查）；大專學歷比例、技術職業比例等（LEED）（p.19, 32） | ICT 調查；雇主－員工連結資料（LEED） | LEED 僅部分國家可合併，含 Denmark、Netherlands、Portugal（p.35） | 各國統計機關 |
| 技術資本 | 是否使用 100 Mbit/s 以上寬頻；企業已採用的其他數位技術比例（p.32） | ICT 調查 | — | Calvino et al. |
| 企業特徵 | 規模級距、年齡級距、2 位碼 NACE 產業、年份 | ICT 調查、企業登記 | — | 各國統計機關 |

- **資料取得：** 微觀資料不公開，由各國專家以 OECD 共同 Stata 程式分散執行，只把彙總結果傳回 OECD（p.19）。

## 9. 研究方法
**採用迴歸：線性機率模型（Box 4.1，p.32）：**
`Technology use_it = β0 + β1 SizeClass_it + β2 AgeClass_it + β3 X′_it + δ_s + γ_t + ε_it`

| 符號 | 定義 |
|---|---|
| `Technology use_it` | 企業 i 在 t 年是否使用某項技術（每項技術分別估計） |
| `SizeClass`、`AgeClass` | 規模與年齡級距固定效果 |
| `X′_it` | 人力資本與技術資本：ICT 專業人員、ICT 訓練、高速寬頻、其他數位技術採用比例（延伸設定才放入） |
| `δ_s`、`γ_t` | 產業、年份固定效果 |

**生產力迴歸（p.39）：**
`log(Productivity)_it = β0 + β1 Technology use_it + β2 SizeClass_it + β3 AgeClass_it + β4 X′_it + δ_s + γ_t + ε_it`
- `β1`：採用者相對於非採用者的生產力溢價。
- 先不放 `X′` 估計，再加入人力與技術資本，看溢價縮小多少。
- 作者強調結果只是條件相關，不能做因果解讀（p.38, 41）。

**其他分析：** 技術共同出現網絡分析（p.20–）；穩健性另以 probit 估計（p.64）。

## 10. 研究結果
原文以七項典型事實呈現（p.8–9）：
1. **技術間相互依賴：** 先進技術常建立在雲端、CRM、ERP 與高速寬頻等基礎技術上。
2. **產業差異大：** AI 與大數據在 ICT 與專業科學服務較普遍；IoT 分布較廣；機器人與 3D 列印集中在製造業與公用事業。Germany 是 ICT 產業不是 AI 採用最高產業的唯一國家；Denmark 多個產業的 AI 採用率相對較高（p.23）。
3. **大企業較常採用：** 控制產業後，大企業採用 AI 的機率平均比小企業高 20 個百分點，各國介於 5 到 37 個百分點。
4. **人力與技術資本：** AI 採用與 ICT 技能正相關（6 國中 5 國）、與 ICT 訓練正相關（5 國中 2 國）、與技術資本正相關（9 國全部）。
5. **教育與技術職業：** 大專學歷員工比例增加 1 個百分點，AI 採用機率在 Denmark 增加 0.53、Netherlands 0.24、Portugal 0.15 個百分點。
6. **生產力溢價：** AI 採用者的生產力溢價從 France 7.7% 到 Belgium 31%（p.40）；大企業的溢價較大。
7. **溢價部分來自互補資本：** 控制人力與技術資本後，10 國中只有 2 國仍有顯著的 AI 生產力溢價。

**近期採用率：** AI 與 3D 列印約 4%–10%，大數據與 IoT 約 25%（p.8）。

**Denmark 補充（Box 4.4，p.43；引述 Warzynski，即將出版）：**
- Denmark 企業 AI 使用率由 2017 年 7% 升至 2021 年 36%。
- 早期採用者兩年內每員工附加價值成長高 3.7%，技術人員比例增加 7.1%。
- 生產函數估計中 AI 的直接效果約 3%，與技術及非技術勞動有互補。

**作者解釋：** 單靠 AI 採用不保證生產力提升，效果取決於人力資本與組織變革等互補投資（p.9, 43）。

## 11. 研究限制
作者列出：
- ICT 調查多為重複橫斷面，且多問「是否使用」而非首次採用時間，難以分析採用行為的變化（p.18）。
- 各國定義、年份、產業與規模涵蓋不同，跨國比較需謹慎（p.18, 20）。
- 人力資本資料在 ICT 調查中不一致，LEED 只有部分國家可用（p.35）。
- 生產力結果為條件相關，不是因果效果（p.38, 41）。
- 調查期間 2017–2023，未完整涵蓋生成式 AI（p.8）。

## 12. 關聯
**可參考之處：**
- 三國（Germany、Netherlands、Denmark）都在樣本中，且使用官方企業調查衡量 AI 採用，可作為三國「企業 AI 採用」的可比資料來源。
- 提供 OECD 層級的 AI 採用彙總資料庫入口（OECD ICT Access and Usage by Businesses），可用於國家年度層級的 AI 採用變數。
- 說明人力資本是 AI 採用與生產力溢價的關鍵互補因素，與本研究人力資本的角色相關。
- 文獻蒐集總覽提醒：此處的 AI 為生成式 AI 普及前的 AI。

**套用此模型所需資料：**

| 資料 | 來源 | 取得狀態 |
|---|---|---|
| 國家層級企業 AI 使用率 | [OECD ICT Access and Usage by Businesses](https://data-explorer.oecd.org/s/3il) | 公開彙總資料 |
| 企業層級 ICT 調查微觀資料 | 各國統計機關 | 不公開，需透過各國統計機關申請 |

**不能直接套用之處：**
- 分析單位是企業，結果是企業生產力溢價，不是國家經濟成長。
- 三國 AI 資料只有 2–4 個年份，且年份不同。
- 生產力關係不能做因果解讀。

**相關頁面：** [Eurochambres（2026）](eurochambres-2026.md)、[Jensen & Schneider（2026）](jensen-schneider-2026.md)、[Renault（2025）](renault-2025-imf-denmark.md)

**綜合頁：** [AI 指標比較](../topics/synthesis/ai-measures.md)、[方法與資料結構比較](../topics/synthesis/methods-data-structures.md)、[來源間的數字差異](../topics/synthesis/source-discrepancies.md)
