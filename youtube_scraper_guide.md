# YouTube 頻道字幕批次抓取工具 (YouTube Transcript Fetcher)

這是一份專為 Agent 撰寫的技術說明文件。當你需要抓取任何 YouTube 頻道的完整歷史影片字幕（並轉換為乾淨的 `.txt` 文字檔）以供後續的 RAG (檢索增強生成) 或人格蒸餾 (Persona Distillation) 使用時，請遵循此文件的指示操作。

## 📍 腳本與相依檔案位置

所有相關腳本與依賴檔案皆位於本機專案目錄中：
* **工作目錄 (CWD)**: `C:\Users\user\Desktop\yuyu\yu\Side Project\DebateSystem`
* **主腳本位置**: `data/fetch_transcripts.py`
* **Cookies 檔**: `data/cookies.txt` (由使用者匯出，用於避免 YouTube IP 封鎖與年齡限制)
* **FFmpeg**: `ffmpeg.exe` 與 `ffprobe.exe` 必須存在於專案根目錄或 PATH 中（目前已放置於根目錄）。這是 `yt-dlp` 執行字幕格式轉換 (`--convert-subs`) 的必要依賴。

## ⚙️ 核心功能與特性

1. **單一 yt-dlp 批次呼叫**: 腳本會將整個頻道的影片 URL 傳遞給 yt-dlp，由其內部引擎自動解析播放清單並排隊下載。
2. **內建防封鎖機制 (Anti-Ban/Rate Limit)**:
   * 隨機休眠 (`--sleep-interval 4` ~ `--max-sleep-interval 8`)。
   * 自動處理 `HTTP 429 Too Many Requests`，具備指數退避重試機制。
3. **自動斷點續傳 (Resume Support)**: 
   * 依賴 `_yt_archive.txt` 紀錄已下載的 Video ID。
   * 中斷後再次執行時，會**在一秒內瞬間跳過**所有已下載的影片，完全不發送多餘請求。
4. **格式自動清洗**: 下載的 `.vtt` 字幕檔會在抓取完成後，經由 Python 正則表達式自動去除非語音標籤與時間戳，輸出成純文字 `.txt` 檔，並刪除原始 `.vtt`。

## 🚀 如何使用 (Usage)

請在專案根目錄 (`DebateSystem`) 下開啟終端機執行。腳本支援透過命令列參數傳入「交易員代號」與「頻道 Videos 網址」。

**語法**:
```powershell
python data/fetch_transcripts.py <TraderName> <ChannelVideosURL>
```

**範例 1：抓取 TJR Trades 的頻道**
```powershell
python data/fetch_transcripts.py TJR https://www.youtube.com/@TJRTrades/videos
```

**範例 2：抓取預設的 ICT 頻道（不帶參數）**
```powershell
python data/fetch_transcripts.py
```

## 📂 輸出結構 (Output Structure)

執行完畢後，所有處理好的純文字逐字稿會自動分類放置於：
`data/transcripts/<TraderName>/`

目錄結構範例：
```text
DebateSystem/
└── data/
    └── transcripts/
        ├── ICT/
        │   ├── _yt_archive.txt          # 斷點續傳紀錄檔 (勿刪)
        │   ├── video1_title.en.txt      # 清洗後的純文字逐字稿
        │   └── video2_title.en.txt
        └── TJR/
            ├── _yt_archive.txt
            └── ...
```

## ⚠️ Agent 執行注意事項 (For AI Agents)

1. **不要併發執行 (Do NOT Run Concurrently)**: 由於 YouTube 對單一 IP 的請求頻率限制極為嚴格，**絕對不要**同時啟動兩個 `fetch_transcripts.py` 進程，這會導致立即觸發 `429 Too Many Requests` 並封鎖使用者的 IP。
2. **背景監控**: 若由 Agent 代為執行此腳本（例如透過 `run_command`），由於執行時間可能長達數十分鐘至數小時，請使用 `schedule` 工具設定定時器（例如每 15 分鐘）喚醒檢查 log 檔狀態，不要使用 while loop 輪詢。
3. **關於無字幕影片**: 腳本已加上 `--ignore-no-formats-error`，遇到真正沒有英文字幕（連自動翻譯都沒有）的短片 (Shorts) 或音樂影片時，會顯示 `There are no subtitles for the requested languages` 並安全跳過，**這屬於正常現象，不需要修復**。
