# 🎵 MP3 Trimming Project

Automated MP3 trimming tool for 10 songs with specific timestamps.

## 🚀 Quick Start

```bash
# 1. Check project status
python3 check_status.py

# 2. Download 10 songs and place in source_mp3/
#    (See QUICK_START.md for file names)

# 3. Run trimming script
python3 trim_existing_mp3.py

# 4. Get trimmed files from trimmed_mp3/
```

## 📁 Project Structure

```
/vercel/sandbox/
├── source_mp3/              # Place downloaded MP3s here
├── trimmed_mp3/             # Trimmed files appear here
├── trim_existing_mp3.py     # Main script ⭐
├── check_status.py          # Status checker
├── QUICK_START.md           # Quick guide
├── SETUP_INSTRUCTIONS.md    # Detailed setup
├── PROJECT_SUMMARY.md       # Complete overview
└── MP3_TRIMMING_README.md   # Technical docs
```

## 📋 Song List

| # | Song | Input File | Output File | Timestamps |
|---|------|------------|-------------|------------|
| 1 | Palat | palat.mp3 | ui.mp3 | 0:26-1:03 |
| 2 | Radhe Radhe | radhe_radhe.mp3 | admin.mp3 | 0:11-0:37 |
| 3 | Arjun Valley | arjun_valley.mp3 | backend.mp3 | 0:00-0:30 |
| 4 | Shanaya | shanaya.mp3 | hr.mp3 | 0:00-0:48 |
| 5 | Karvaan | karvaan.mp3 | migration.mp3 | 1:06-1:31 |
| 6 | Maine Tujhe Dekha | maine_tujhe_dekha.mp3 | qa.mp3 | 1:05-1:22 |
| 7 | Faasla | faasla.mp3 | arun.mp3 | 0:00-0:18, 0:36-0:57 |
| 8 | Sauda Sauda | sauda_sauda.mp3 | marketing.mp3 | 0:12-0:19, 0:50-1:33 |
| 9 | Galti Se Mistake | galti_se_mistake.mp3 | ai.mp3 | 0:09-0:51 |
| 10 | Paisa Hai Toh | paisa_h_toh.mp3 | finance.mp3 | 0:46-1:19 |

## ✅ Features

- ✓ Precise timestamp trimming (millisecond accuracy)
- ✓ Multi-segment support (combines multiple clips)
- ✓ High-quality output (192kbps MP3)
- ✓ Automatic file validation
- ✓ Progress reporting
- ✓ Error handling

## 🔧 Requirements

All dependencies are pre-installed:
- Python 3.9+
- pydub
- ffmpeg
- requests

## 📖 Documentation

- **QUICK_START.md** - Get started in 5 minutes
- **SETUP_INSTRUCTIONS.md** - Detailed setup guide
- **PROJECT_SUMMARY.md** - Complete project overview
- **MP3_TRIMMING_README.md** - Technical documentation

## 🎯 Workflow

```
Download Songs → Rename Files → Place in source_mp3/ → Run Script → Get Trimmed Files
```

## 💡 Usage Example

```bash
# Check what's needed
python3 check_status.py

# After downloading and placing files
python3 trim_existing_mp3.py

# Output:
# ============================================================
# MP3 Trimming Script
# ============================================================
# 
# Processing: palat.mp3 → ui.mp3
#   Loading: palat.mp3
#   Extracting segment: 0:26 to 1:03
#   ✓ Saved: ui.mp3 (duration: 37.0s)
# 
# ... (9 more files)
# 
# ============================================================
# Summary:
#   ✓ Successfully trimmed: 10/10
#   ⊘ Skipped: 0/10
# 
# Output files saved in: /vercel/sandbox/trimmed_mp3
# ============================================================
```

## ⚠️ Important Notes

1. **File Names**: Must match exactly (case-sensitive)
2. **Format**: Only MP3 files are supported
3. **Location**: Files must be in `/vercel/sandbox/source_mp3/`
4. **Quality**: Source files should be good quality for best results

## 🔍 Troubleshooting

### No files found
```bash
# Check directory exists
ls -la /vercel/sandbox/source_mp3/

# Verify file names
ls /vercel/sandbox/source_mp3/*.mp3
```

### Script errors
```bash
# Check dependencies
python3 -c "import pydub; print('OK')"
ffmpeg -version
```

### File not trimming
- Verify file is valid MP3
- Check file isn't corrupted
- Ensure file has enough duration for the timestamps

## 📊 Expected Output

- **Total Files**: 10 trimmed MP3s
- **Total Duration**: ~5 minutes 27 seconds
- **File Size**: ~1-2 MB each
- **Quality**: 192kbps MP3
- **Processing Time**: ~30-50 seconds total

## 🎓 Help

Run the status checker anytime:
```bash
python3 check_status.py
```

For detailed help, see the documentation files listed above.

## 📝 License

This project is part of the FusionIIIT repository.

---

**Status**: ✅ Ready to use (pending manual MP3 downloads)

**Created**: January 27, 2026

**Version**: 1.0
