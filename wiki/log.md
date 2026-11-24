# Wiki Log

依 `AGENTS.md` 追加實際完成的 ingest、query 寫回與 lint 紀錄。

## [2026-11-23] setup | 建立 Wiki 規範與範本

- 依使用者確認的需求建立 `AGENTS.md` 與 Wiki 頁面骨架。
- 建立來源、研究總覽、國家、方法、跨文獻綜合等 Markdown 範本。
- 初始骨架完成；當時尚未 ingest `RAW/` 文獻。

## [2026-11-23] ingest | 建立一篇 AI 與經濟成長來源筆記

- 寫入 Duarte, Freitas & Simões (2026) 來源筆記，保留 `RAW/` 原檔並附原文頁碼。
- 建立 OECD 基準、Panel ARDL、動態面板 GMM 主題頁。
- 更新 `index.md`、`catalog.json`、搜尋首頁及相關主題索引。
- 期刊筆記記錄 SCImago 2025 Q4；JCR 分區未填值。第二篇僅整理成待審草稿，未 ingest。

## [2026-11-23] update | 來源筆記改為 12 欄格式並重寫 Duarte 筆記

- 範本與 `AGENTS.md` 改為 12 欄：來源、研究目的、研究貢獻、研究背景、研究問題、研究假設、樣本與研究期間、資料與變數、研究方法、研究結果、研究限制、關聯。
- 依 Duarte 全文與 Parteka & Kordalska (2023) 資料章節重寫 Duarte 筆記：資料與變數改列原始資料庫、篩選條件與指標建構者；資料庫連結已實際開啟確認（PATS_IPC 舊網址已註明轉址）。
- 期刊同儕審查依期刊說明頁確認；SJR 2025 Q4 與學科類別由使用者提供之 SCImago 頁面確認；JCR 未查到，未填。
- 同步更新 `index.md` 與 `catalog.json`。

## [2026-11-23] ingest | 寫入 Gambacorta et al. (2025) BIS WP 1321 來源筆記

- 依 12 欄研究架構寫入 `sources/bis-gambacorta-et-al-2025.md`，重點整理模型符號、識別邏輯、資料來源與套用所需資料。
- 依原文更正先前草稿：約 2 個百分點的產業差距依設定 (II) 係數 2.905 計算；國家層級模擬依表 3 設定 (III)；機器人資料原文未載明來源；正文僅能確認樣本含 Denmark。
- 新增方法頁 `topics/methods/industry-exposure-interaction.md`（狀態：候選），更新 OECD 國家頁、方法索引、`index.md`、`catalog.json` 與搜尋首頁內嵌資料。
- 新增報告類來源範本 `templates/report-note.md`，並於 `AGENTS.md` 加入報告類來源規則。
- 待使用者下載放入 `僅供參考/`：Aldasoro et al. (2024) BIS WP 1179、IMF AIPINote.pdf。

## [2026-11-23] ingest | 批次寫入其餘 RAW 來源

- 依使用者指示「寫全部」，以 Duarte 與 BIS 兩篇確認的格式，批次寫入 15 篇來源筆記。研究類 11 篇採 12 欄；報告類 4 篇（Danmarks Nationalbank、TNO、ECB OP395、Licht & Wohlrabe）採 9 欄。
- 每篇的資料來源、篩選條件與結果皆對照原文 PDF；資料庫連結以瀏覽器實際開啟確認，無法確認者在筆記中註明。
- 依原文記錄各篇的內部不一致，例如 Kalai 表格與內文係數不同、Wagner 內文 0.701 與表格 0.717、Eurochambres 樣本數標籤、DergiPark 表註與變數單位。
- BIS 筆記補上 Felten AIOE（GitHub 公開）、O*NET、BLS OEWS 來源，以及 AIPINote 的方法說明（加總與平均寫法不同）。
- 新增 Germany、Netherlands、Denmark 國家頁；更新 OECD 國家頁、`index.md`、`catalog.json` 與搜尋首頁（共 17 筆）。
- 未 ingest：`RAW/Rammer_et_al_2022_German_Firm_Innovation_ZEW_DP.pdf` 實際內容為 Asatryan et al.（2021）*Favoritism and Firms*，與主題無關；需重新下載 Rammer et al.（2022）。
- 期刊分區仍待查：Technovation、Journal of Economic Structures、Economies、Research Policy、Open Economies Review、Annals of Economics and Finance、International Journal of Business & Economic Studies、Applied Economics Letters。SCImago 網站阻擋自動瀏覽。

## [2026-11-23] ingest | 寫入 Rammer, Fernández & Czarnitzki (2022)

- 使用者提供 Research Policy 原文，原檔另存為 `RAW/Rammer_Fernandez_Czarnitzki_2022_AI_Industrial_Innovation.pdf`；原本放錯的 ZEW DP 檔案保留未動。
- 依 12 欄研究架構寫入來源筆記，並更新 Germany 國家頁、`index.md`、`catalog.json` 與搜尋首頁（共 18 筆）。
- 依使用者意見，刪除各筆記中「Germany／Netherlands／Denmark 不在樣本」作為不能套用理由的寫法；其他研究不需要與本研究採用相同國家。

## [2026-11-23] update | 補上期刊 SJR 分區

- 依使用者貼上的 SCImago 頁面補上 2025 年 SJR 分區：Technovation Q1、Research Policy Q1（Engineering (miscellaneous)）；Journal of Economic Structures Q2、Economies Q2（Economics, Econometrics and Finance (miscellaneous)）；Open Economies Review Q3、Applied Economics Letters Q3（Economics and Econometrics）；Annals of Economics and Finance Q4（Finance）。
- International Journal of Business & Economic Studies：使用者以 SCImago 搜尋查無收錄，筆記照實記錄。
- 同步更新各筆記 frontmatter、`catalog.json` 與搜尋首頁的分區欄位。JCR 未查。

## [2026-11-23] update | 移除搜尋首頁，新增跨文獻綜合頁

- 依使用者確認（Wiki 由 Agent 讀寫與查詢，不需給人瀏覽的網站），刪除 `wiki/index.html` 與 `wiki/catalog.json`，並刪除空的 `wiki/concepts/` 資料夾。
- 修改 `AGENTS.md`：刪除搜尋首頁與 catalog 規定；`index.md` 改為每頁附具體摘要；Ingest 時若新來源與既有頁面數字或結論不一致，寫入綜合頁；Lint 改為檢查索引是否涵蓋所有頁面。
- 新增綜合頁：`topics/synthesis/ai-measures.md`、`methods-data-structures.md`、`source-discrepancies.md`；各來源筆記加上綜合頁連結。
- 重寫 `index.md`，每頁附研究設計、主要結果與注意事項摘要。

## [2026-11-23] setup | 建立研究模型簡報的 loop 規格

- 依老師簡報第 41 頁 Loop 格式，建立 `.claude/skills/research-model-deck/SKILL.md`（目標、程式檢查、AI 審查、每輪修正範圍、停止條件）與程式檢查腳本 `check_deck.py`。
- 以測試用簡報驗證腳本：能抓出頁數不足、缺出處、引用頁不存在、數字在引用頁找不到。
- 產出資料夾為 `presentation/research-model/`；簡報尚未產生。`wiki/research-overview.md` 目前多為「待整理」，依停止條件，需先寫入研究設計才能執行 loop。

## [2026-11-23] update | 寫入研究總覽，研究模型簡報流程進行到大綱

- 依使用者提供的研究設計寫入 `research-overview.md`（題目、RQ1–3、H1–H3、變數與來源、Model 1–3、限制；狀態皆為暫定，樣本為歐洲 OECD 國家，期間待確認）。
- `presentation/research-model/` 產出 `sources.md`、8 張證據卡、`outline.md`；覆蓋率關卡與卡片檢查通過，大綱待人工確認。

## [2026-11-24] 簡報 | 研究模型簡報第 2、3 輪
- 第 2 輪依 review-round-1.md 修正 10 項並放大字體（12 頁）；第 3 輪依 review-round-2.md 修正 3 項。程式檢查通過；後備字型渲染無溢出。已達 3 輪上限，紀錄見 presentation/research-model/report.md。

## [2026-11-24] 更新 | 研究總覽 Model 2 加入三國之間的檢定
- 使用者確認後，Model 2 核心檢定改為兩個 Wald 檢定：β₂ = β₃ = β₄ = 0（與基準比較）、β₂ = β₃ = β₄（三國之間比較）。簡報第 9 頁同步更新，程式檢查通過。

## [2026-11-24] 修正 | 研究總覽的文獻先例說法
- 雙向固定效果改列為有先例（Parteka & Kordalska 2023，式 1，p.7）；Duarte、Kalai 補註方法；只有 AI × 個別國家虛擬變數屬本研究延伸，相近先例為 BIS 1321。簡報第 11 頁同步更新，程式檢查通過。

## [2026-11-24] ingest | Gonzales 2023、Filip et al. 2026（ECB WP 3242）、Brey & van der Marel 2024
- 使用者確認三篇為主要參考文獻，從 `僅供參考/` 移入 `RAW/`，建立三篇來源筆記（12 欄）。
- 期刊分區：Gonzales 為 Journal of Economic Structures，沿用既有 SJR 2025 Q2 紀錄；Economics Letters 待查（SCImago、ScienceDirect 本次回傳 403）；ECB 工作論文不適用。
- 更新方法與資料結構比較、AI 指標比較、來源間的數字差異三個綜合頁；新增矛盾：Gonzales 的 AI 專利顯著、Parteka 不顯著，並列可能原因。
- 更新研究總覽「文獻先例與本研究延伸」、索引，以及德、荷、丹國家頁的相關來源。
- 仍留在 `僅供參考/`：Czernich et al. 2011、Kjosevski et al.、Graetz & Michaels（IZA DP 8938）。
- 依使用者貼上的 SCImago 頁面補上 Economics Letters 分區：SJR 2025 Q2，Finance。同儕審查狀態仍待查證。

## [2026-11-24] 簡報 | KaTeX 樣式與字型改為本地檔案
- `presentation/research-model/katex/` 存放 KaTeX 0.16.9 的 CSS 與 woff2 字型，`deck.html` 改為讀取本地樣式，避免外部樣式表被阻擋。

## [2026-11-24] 流程 | 修改 research-model-deck loop
- 依實際執行發現的問題修改 loop：覆蓋率關卡加入「每個模型設定都要找得到文獻先例或標為本研究延伸」；轉引文獻規則改為通用寫法。
