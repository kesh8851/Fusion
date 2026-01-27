# MP3 Trimming Setup Instructions

## Current Status

Due to YouTube's bot detection and API restrictions in the sandbox environment, automatic downloads are blocked. However, the trimming functionality works perfectly!

## ✅ WORKING SOLUTION: Manual Download + Automated Trimming

### Step 1: Create Source Directory

```bash
mkdir -p /vercel/sandbox/source_mp3
```

### Step 2: Download Songs Manually

You need to download the following 10 songs as MP3 files and place them in `/vercel/sandbox/source_mp3/`:

| # | File Name | Song to Download | YouTube Search |
|---|-----------|------------------|----------------|
| 1 | `palat.mp3` | Palat (Bollywood song) | Search: "palat song" |
| 2 | `radhe_radhe.mp3` | Radhe Radhe | Search: "radhe radhe song" |
| 3 | `arjun_valley.mp3` | Arjun Valley | Search: "arjun valley song" |
| 4 | `shanaya.mp3` | Shanaya | Search: "shanaya song" |
| 5 | `karvaan.mp3` | Karvaan | Search: "karvaan song" |
| 6 | `maine_tujhe_dekha.mp3` | Maine Tujhe Dekha | Search: "maine tujhe dekha song" |
| 7 | `faasla.mp3` | Faasla | Search: "faasla song" |
| 8 | `sauda_sauda.mp3` | Sauda Sauda | Search: "sauda sauda song" |
| 9 | `galti_se_mistake.mp3` | Galti Se Mistake | Search: "galti se mistake song" |
| 10 | `paisa_h_toh.mp3` | Paisa Hai Toh | Search: "paisa hai toh song" |

**How to download:**
- Use any YouTube to MP3 converter website (e.g., y2mate.com, ytmp3.cc, etc.)
- Or use a local tool like `youtube-dl` or `yt-dlp` on your personal computer
- Save each file with the exact name shown above
- Transfer files to `/vercel/sandbox/source_mp3/`

### Step 3: Run the Trimming Script

Once all MP3 files are in place, run:

```bash
python3 /vercel/sandbox/trim_existing_mp3.py
```

### Step 4: Get Your Trimmed Files

The trimmed files will be in `/vercel/sandbox/trimmed_mp3/` with these names:

| Output File | Original Song | Trimmed Segments | Duration |
|-------------|---------------|------------------|----------|
| `ui.mp3` | palat | 0:26-1:03 | 37s |
| `admin.mp3` | radhe radhe | 0:11-0:37 | 26s |
| `backend.mp3` | arjun valley | 0:00-0:30 | 30s |
| `hr.mp3` | shanaya | 0:00-0:48 | 48s |
| `migration.mp3` | karvaan | 1:06-1:31 | 25s |
| `qa.mp3` | maine tujhe dekha | 1:05-1:22 | 17s |
| `arun.mp3` | faasla | 0:00-0:18 + 0:36-0:57 | 39s |
| `marketing.mp3` | sauda sauda | 0:12-0:19 + 0:50-1:33 | 50s |
| `ai.mp3` | galti se mistake | 0:09-0:51 | 42s |
| `finance.mp3` | paisa h toh | 0:46-1:19 | 33s |

## Alternative: Use yt-dlp on Your Local Machine

If you have access to a local machine without restrictions:

```bash
# Install dependencies
pip install yt-dlp pydub

# Copy the script to your local machine
# Then run it there
python3 trim_mp3_from_urls.py
```

## Verification

To check if your source files are ready:

```bash
ls -lh /vercel/sandbox/source_mp3/
```

You should see 10 MP3 files with the exact names listed above.

## Troubleshooting

### "No MP3 files found in source directory"
- Make sure files are in `/vercel/sandbox/source_mp3/`
- Check that file names match exactly (case-sensitive)
- Ensure files have `.mp3` extension

### "Source file not found"
- Verify the file name matches exactly
- Check for extra spaces or characters in the filename

### "Error trimming audio"
- Ensure the MP3 file is not corrupted
- Try re-downloading the file
- Check that ffmpeg is installed (it should be)

## Technical Details

- **Trimming Tool**: pydub with ffmpeg backend
- **Output Quality**: 192kbps MP3
- **Multi-segment Support**: Songs with multiple segments are automatically combined
- **Precision**: Millisecond-level accuracy for timestamps

## Files in This Project

- `trim_existing_mp3.py` - Main trimming script (RECOMMENDED)
- `download_trim_mp3.py` - Auto-download script (blocked by YouTube)
- `trim_mp3_from_urls.py` - Enhanced download script (blocked by YouTube)
- `download_with_cobalt.py` - Cobalt API script (API restrictions)
- `MP3_TRIMMING_README.md` - Detailed documentation
- `SETUP_INSTRUCTIONS.md` - This file

## Support

If you encounter any issues, check:
1. File names are exactly as specified
2. Files are valid MP3 format
3. ffmpeg is installed (`ffmpeg -version`)
4. pydub is installed (`pip list | grep pydub`)
