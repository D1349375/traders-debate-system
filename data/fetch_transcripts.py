"""
ICT YouTube Transcript Downloader - Batch Mode
================================================
Passes the ENTIRE channel URL to yt-dlp in ONE call.
yt-dlp handles rate limiting, retries, and resume internally.

After download, converts all .vtt files to .txt.

Usage:
    python data/fetch_transcripts.py
"""

import sys
import re
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# ── CONFIG ───────────────────────────────────────────────────────────────────
# Defaults (can be overridden by command line arguments)
DEFAULT_TRADER_NAME = "ICT"
DEFAULT_CHANNEL_URL = "https://www.youtube.com/@InnerCircleTrader/videos"

COOKIE_FILE   = Path(__file__).parent / "cookies.txt"
LANGUAGE_PREF = "en"
# ─────────────────────────────────────────────────────────────────────────────

# These will be set in main()
CHANNEL_URL = ""
OUTPUT_DIR = Path()
ARCHIVE_FILE = Path()


def download_all_subtitles():
    """
    Single yt-dlp call to download ALL subtitles from the channel.
    yt-dlp handles: rate limiting, retries, sleep intervals, and resume.
    """
    print("[INFO] Starting batch subtitle download for entire channel...")
    print(f"[INFO] Output: {OUTPUT_DIR}")
    print(f"[INFO] Archive (resume file): {ARCHIVE_FILE}\n")

    cmd = [
        "yt-dlp",
        "--write-auto-subs",           # auto-generated captions
        "--write-subs",                # manual captions if available
        "--skip-download",             # subtitles only, no video
        "--ignore-no-formats-error",   # skip videos with no subtitles silently
        "--ignore-errors",             # don't stop on individual video errors
        "--sub-langs", LANGUAGE_PREF,
        "--convert-subs", "vtt",
        # Rate limiting - slower but much safer for 600+ videos
        "--sleep-interval", "4",       # min 4s between videos
        "--max-sleep-interval", "8",   # max 8s (randomized to look human)
        "--sleep-requests", "1",       # 1s between HTTP requests within a video
        "--sleep-subtitles", "2",      # sleep before subtitle download
        "--retries", "5",
        "--fragment-retries", "5",
        # Resume support - skip already-downloaded videos
        "--download-archive", str(ARCHIVE_FILE),
        # Output filename
        "-o", str(OUTPUT_DIR / "%(id)s_%(title)s.%(ext)s"),
        CHANNEL_URL,
    ]
    if COOKIE_FILE.exists():
        cmd += ["--cookies", str(COOKIE_FILE)]
        print(f"[OK] Using cookies: {COOKIE_FILE}\n")
    else:
        print("[WARN] No cookies.txt found\n")

    # Run yt-dlp (streaming output so user sees progress live)
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    for line in process.stdout:
        print(line, end="", flush=True)
    process.wait()

    if process.returncode == 0:
        print("\n[OK] yt-dlp finished successfully")
    else:
        print(f"\n[WARN] yt-dlp exited with code {process.returncode} (some videos may have failed)")


def vtt_to_text(vtt_path: Path) -> str:
    """Parse a .vtt subtitle file and return clean plain text."""
    text_lines = []
    seen = set()
    for line in vtt_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("WEBVTT") or line.startswith("NOTE"):
            continue
        if "-->" in line:
            continue
        line = re.sub(r"<[^>]+>", "", line).strip()
        if not line or line in seen:
            continue
        seen.add(line)
        text_lines.append(line)
    return " ".join(text_lines)


def sanitize(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "_", name)[:120]


def convert_vtt_to_txt():
    """Convert all .vtt files in OUTPUT_DIR to .txt files, then delete .vtt."""
    vtt_files = list(OUTPUT_DIR.glob("*.vtt"))
    if not vtt_files:
        print("[INFO] No .vtt files to convert.")
        return

    print(f"\n[INFO] Converting {len(vtt_files)} .vtt files to .txt...")
    converted = 0
    for vtt_path in vtt_files:
        # Output txt path: same name but .txt extension
        txt_path = vtt_path.with_suffix(".txt")
        if txt_path.exists():
            vtt_path.unlink()  # clean up vtt, txt already exists
            continue

        text = vtt_to_text(vtt_path)
        if text:
            txt_path.write_text(text, encoding="utf-8")
            converted += 1
        vtt_path.unlink()  # remove vtt regardless

    print(f"[OK] Converted {converted} files.")


def main():
    global CHANNEL_URL, OUTPUT_DIR, ARCHIVE_FILE

    # Parse command line arguments
    if len(sys.argv) >= 3:
        trader_name = sys.argv[1]
        CHANNEL_URL = sys.argv[2]
    else:
        trader_name = DEFAULT_TRADER_NAME
        CHANNEL_URL = DEFAULT_CHANNEL_URL
        print(f"[INFO] No arguments provided. Using defaults.")
        print(f"       Usage: python fetch_transcripts.py <TraderName> <ChannelVideosURL>\n")

    OUTPUT_DIR = Path(__file__).parent / "transcripts" / trader_name
    ARCHIVE_FILE = OUTPUT_DIR / "_yt_archive.txt"
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1: Download all subtitles via single yt-dlp call
    download_all_subtitles()

    # Step 2: Convert .vtt -> .txt
    convert_vtt_to_txt()

    # Summary
    txt_files = list(OUTPUT_DIR.glob("*.txt"))
    total_size = sum(f.stat().st_size for f in txt_files)
    print(f"\n{'='*60}")
    print(f"[DONE] Total .txt files : {len(txt_files)}")
    print(f"       Total size       : {total_size/1024/1024:.1f} MB")
    print(f"       Output dir       : {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
