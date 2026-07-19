import os
import re
import subprocess
from pathlib import Path

def main():
    tjr_dir = Path(r"c:\Users\user\Desktop\yuyu\yu\Side Project\DebateSystem\data\transcripts\TJR")
    if not tjr_dir.exists():
        print(f"Directory not found: {tjr_dir}")
        return

    txt_files = list(tjr_dir.glob("*.txt"))
    print(f"Found {len(txt_files)} transcript files.")

    # 1. Extract IDs
    video_map = {}
    batch_file = tjr_dir / "_tjr_batch.txt"
    with open(batch_file, "w", encoding="utf-8") as f:
        for p in txt_files:
            # yt-dlp default format is <id>_<title>.en.txt
            # ID is usually 11 chars
            m = re.match(r"^(.{11})_", p.name)
            if m:
                vid = m.group(1)
                video_map[vid] = p
                f.write(f"{vid}\n")
            else:
                print(f"Skipping {p.name}: Cannot extract video ID.")

    print(f"Extracted {len(video_map)} unique video IDs.")

    # 2. Run yt-dlp to get upload dates
    print("Fetching upload dates via yt-dlp... (This may take a few minutes)")
    cmd = [
        "yt-dlp",
        "--batch-file", str(batch_file),
        "--print", "%(id)s|%(upload_date)s",
        "--ignore-errors",
        "--sleep-requests", "0.5" # be gentle to youtube
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    
    # Clean up batch file
    if batch_file.exists():
        batch_file.unlink()

    # 3. Parse output
    date_map = {}
    for line in result.stdout.splitlines():
        parts = line.strip().split("|")
        if len(parts) == 2:
            vid, raw_date = parts
            if raw_date and len(raw_date) == 8 and raw_date != "NA":
                # format YYYYMMDD to YYYY-MM-DD
                fmt_date = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"
                date_map[vid] = fmt_date

    print(f"Successfully retrieved dates for {len(date_map)} videos.")

    # 4. Modify files
    updated = 0
    for vid, fmt_date in date_map.items():
        if vid in video_map:
            fpath = video_map[vid]
            content = fpath.read_text(encoding="utf-8", errors="replace")
            
            # Prevent double-prepending
            if not content.startswith("Upload Date:"):
                new_content = f"Upload Date: {fmt_date}\n\n" + content
                fpath.write_text(new_content, encoding="utf-8")
                updated += 1
            else:
                # If it starts with Upload Date but maybe wrong, we can skip or replace
                # For now, just skip if it's already there
                pass

    print(f"Successfully added timestamps to {updated} files.")

if __name__ == "__main__":
    main()
