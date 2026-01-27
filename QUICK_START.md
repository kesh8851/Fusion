# Quick Start Guide - MP3 Trimming

## 🎵 What This Does

Automatically trims 10 songs to specific timestamps and saves them with custom names.

## 🚀 Quick Steps

### 1. Download Songs
Download these 10 songs as MP3 files:
- palat
- radhe radhe  
- arjun valley
- shanaya
- karvaan
- maine tujhe dekha
- faasla
- sauda sauda
- galti se mistake
- paisa h toh

### 2. Rename Files
Rename them to:
```
palat.mp3
radhe_radhe.mp3
arjun_valley.mp3
shanaya.mp3
karvaan.mp3
maine_tujhe_dekha.mp3
faasla.mp3
sauda_sauda.mp3
galti_se_mistake.mp3
paisa_h_toh.mp3
```

### 3. Place Files
Put all files in:
```bash
/vercel/sandbox/source_mp3/
```

### 4. Run Script
```bash
python3 /vercel/sandbox/trim_existing_mp3.py
```

### 5. Get Results
Find trimmed files in:
```bash
/vercel/sandbox/trimmed_mp3/
```

Output files will be named:
- ui.mp3
- admin.mp3
- backend.mp3
- hr.mp3
- migration.mp3
- qa.mp3
- arun.mp3
- marketing.mp3
- ai.mp3
- finance.mp3

## 📋 Timestamp Reference

| Input | Output | Timestamps |
|-------|--------|------------|
| palat.mp3 | ui.mp3 | 0:26-1:03 |
| radhe_radhe.mp3 | admin.mp3 | 0:11-0:37 |
| arjun_valley.mp3 | backend.mp3 | 0:00-0:30 |
| shanaya.mp3 | hr.mp3 | 0:00-0:48 |
| karvaan.mp3 | migration.mp3 | 1:06-1:31 |
| maine_tujhe_dekha.mp3 | qa.mp3 | 1:05-1:22 |
| faasla.mp3 | arun.mp3 | 0:00-0:18, 0:36-0:57 |
| sauda_sauda.mp3 | marketing.mp3 | 0:12-0:19, 0:50-1:33 |
| galti_se_mistake.mp3 | ai.mp3 | 0:09-0:51 |
| paisa_h_toh.mp3 | finance.mp3 | 0:46-1:19 |

## ✅ That's It!

The script will automatically:
- ✓ Trim each song to the specified timestamps
- ✓ Combine multiple segments (for faasla and sauda sauda)
- ✓ Export at 192kbps quality
- ✓ Save with the correct output names

## 🔧 Requirements

Already installed:
- Python 3
- pydub
- ffmpeg

## 📁 Directory Structure

```
/vercel/sandbox/
├── source_mp3/          # Put your downloaded MP3s here
│   ├── palat.mp3
│   ├── radhe_radhe.mp3
│   └── ... (8 more files)
├── trimmed_mp3/         # Trimmed files appear here
│   ├── ui.mp3
│   ├── admin.mp3
│   └── ... (8 more files)
└── trim_existing_mp3.py # The script
```

## ❓ Need Help?

See `SETUP_INSTRUCTIONS.md` for detailed troubleshooting.
