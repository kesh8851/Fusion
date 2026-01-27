# MP3 Trimming Project

This project contains scripts to download and trim MP3 files based on specified timestamps.

## Files Created

1. **download_trim_mp3.py** - Original script (YouTube blocked in sandbox)
2. **trim_mp3_from_urls.py** - Enhanced script with retry logic (YouTube blocked in sandbox)
3. **trim_existing_mp3.py** - Works with pre-downloaded MP3 files ✓ RECOMMENDED
4. **download_with_cobalt.py** - Alternative downloader using Cobalt API

## Song List with Timestamps

| Song Name | Timestamps | Output Name | Tag |
|-----------|------------|-------------|-----|
| palat | 0:26-1:03 | ui.mp3 | ui |
| radhe radhe | 0:11-0:37 | admin.mp3 | admin |
| arjun valley | 0:00-0:30 | backend.mp3 | backend |
| shanaya | 0:00-0:48 | hr.mp3 | hr |
| karvaan | 1:06-1:31 | migration.mp3 | migration |
| maine tujhe dekha | 1:05-1:22 | qa.mp3 | qa |
| faasla | 0:00-0:18, 0:36-0:57 | arun.mp3 | arun |
| sauda sauda | 0:12-0:19, 0:50-1:33 | marketing.mp3 | marketing |
| galti se mistake | 0:09-0:51 | ai.mp3 | ai |
| paisa h toh | 0:46-1:19 | finance.mp3 | finance |

## Method 1: Using Pre-Downloaded Files (RECOMMENDED)

### Step 1: Download MP3 files manually

Download the following songs and save them in the `source_mp3` directory:

```bash
mkdir -p /vercel/sandbox/source_mp3
```

Required files:
- palat.mp3
- radhe_radhe.mp3
- arjun_valley.mp3
- shanaya.mp3
- karvaan.mp3
- maine_tujhe_dekha.mp3
- faasla.mp3
- sauda_sauda.mp3
- galti_se_mistake.mp3
- paisa_h_toh.mp3

### Step 2: Run the trimming script

```bash
python3 trim_existing_mp3.py
```

The trimmed files will be saved in `/vercel/sandbox/trimmed_mp3/` with names:
- ui.mp3, admin.mp3, backend.mp3, hr.mp3, migration.mp3, qa.mp3, arun.mp3, marketing.mp3, ai.mp3, finance.mp3

## Method 2: Using Cobalt API (Alternative)

```bash
python3 download_with_cobalt.py
```

This uses the Cobalt API to download from YouTube, which may work better in restricted environments.

## Method 3: Direct YouTube Download (Blocked in Sandbox)

```bash
python3 trim_mp3_from_urls.py
```

Note: This method is currently blocked due to YouTube's bot detection in the sandbox environment.

## Dependencies

All required dependencies are already installed:
- yt-dlp
- pydub
- ffmpeg

## Output

All trimmed MP3 files will be saved in:
```
/vercel/sandbox/trimmed_mp3/
```

## Troubleshooting

### YouTube Bot Detection
If you encounter "Sign in to confirm you're not a bot" errors, use Method 1 (pre-downloaded files) or Method 2 (Cobalt API).

### Missing Source Files
Make sure all MP3 files are placed in the `source_mp3` directory with the exact names listed above.

### Audio Quality
All trimmed files are exported at 192kbps MP3 quality.

## Notes

- Songs with multiple segments (faasla, sauda sauda) will have their segments combined into a single output file
- The script preserves audio quality during trimming
- Original source files are not modified
