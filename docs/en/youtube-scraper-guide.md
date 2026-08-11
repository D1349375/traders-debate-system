# Rebuilding the Transcript Corpus

> English version of [`docs/zh/youtube-scraper-guide.md`](../zh/youtube-scraper-guide.md).

The raw transcripts behind the persona distillation are **not included in this repository** —
they are third-party copyrighted material. This document explains how to rebuild the corpus
locally with `data/fetch_transcripts.py`.

## Prerequisites

Run everything from the repository root.

- `yt-dlp` and Python 3.10+
- `ffmpeg` and `ffprobe` on `PATH` (or in the repository root) — `yt-dlp` needs them for
  subtitle format conversion (`--convert-subs`)
- Optionally a cookies file, if you hit rate limiting or age-restricted videos

> **On cookies.** `fetch_transcripts.py` can read a Netscape-format cookie file exported from
> your browser. **Never commit that file.** It contains live session credentials for your
> Google account, and anyone who obtains it can sign in as you. It is listed in
> `.gitignore`; keep it there, and keep it outside the repository if you can.

## Usage

```bash
python data/fetch_transcripts.py <TraderName> <ChannelVideosURL>
```

Example:

```bash
python data/fetch_transcripts.py TJR https://www.youtube.com/@TJRTrades/videos
```

Run with no arguments to fetch the default channel.

## What the script does

1. **A single batched yt-dlp call.** The whole channel URL is handed to yt-dlp, which parses
   the playlist and queues downloads internally.
2. **Built-in rate-limit avoidance.** Randomized sleeps (`--sleep-interval 4` to
   `--max-sleep-interval 8`) and exponential backoff retry on `HTTP 429 Too Many Requests`.
3. **Resume support.** `_yt_archive.txt` records downloaded video IDs, so a re-run skips
   everything already fetched within a second, issuing no redundant requests.
4. **Automatic cleaning.** Downloaded `.vtt` subtitles are stripped of non-speech tags and
   timestamps by regex into plain `.txt`, and the `.vtt` originals are deleted.

## Output

```text
data/
└── transcripts/
    ├── ICT/
    │   ├── _yt_archive.txt          # resume ledger -- do not delete
    │   ├── video1_title.en.txt      # cleaned plain-text transcript
    │   └── video2_title.en.txt
    └── TJR/
        ├── _yt_archive.txt
        └── ...
```

## Notes for agents running this

1. **Do not run concurrently.** YouTube's per-IP rate limiting is strict, and two
   simultaneous `fetch_transcripts.py` processes will trigger `429 Too Many Requests` and get
   the IP blocked.
2. **Monitor in the background.** A full channel can take tens of minutes to hours. Use a
   scheduled wake-up (every 15 minutes, say) to check the log rather than a polling loop.
3. **Videos without subtitles are fine.** The script passes `--ignore-no-formats-error`, so
   Shorts or music videos with no English subtitles (not even auto-translated) print
   `There are no subtitles for the requested languages` and are skipped safely. **This is
   normal and needs no fix.**

## Corpus provenance

Per-persona video counts and date coverage are recorded in the
[pre-registration](preregistration.md) §8, so what each distillation was built from stays
auditable without redistributing the transcripts themselves.
