#!/usr/bin/env python3
"""
Script to download and trim MP3 files based on provided timestamps.
"""

import os
import sys
from pydub import AudioSegment
import yt_dlp

# Song data with timestamps and names
SONGS = [
    {
        "name": "palat",
        "timestamps": [(26, 1, 3)],  # 0:26 to 1:03
        "tag": "ui"
    },
    {
        "name": "radhe_radhe",
        "timestamps": [(11, 37)],  # 0:11 to 0:37
        "tag": "admin"
    },
    {
        "name": "arjun_valley",
        "timestamps": [(0, 30)],  # 0:00 to 0:30
        "tag": "backend"
    },
    {
        "name": "shanaya",
        "timestamps": [(0, 48)],  # 0:00 to 0:48
        "tag": "hr"
    },
    {
        "name": "karvaan",
        "timestamps": [(1, 6, 1, 31)],  # 1:06 to 1:31
        "tag": "migration"
    },
    {
        "name": "maine_tujhe_dekha",
        "timestamps": [(1, 5, 1, 22)],  # 1:05 to 1:22
        "tag": "qa"
    },
    {
        "name": "faasla",
        "timestamps": [(0, 18), (36, 57)],  # 0:00 to 0:18 and 0:36 to 0:57
        "tag": "arun"
    },
    {
        "name": "sauda_sauda",
        "timestamps": [(12, 19), (50, 1, 33)],  # 0:12 to 0:19 and 0:50 to 1:33
        "tag": "marketing"
    },
    {
        "name": "galti_se_mistake",
        "timestamps": [(9, 51)],  # 0:09 to 0:51
        "tag": "ai"
    },
    {
        "name": "paisa_h_toh",
        "timestamps": [(46, 1, 19)],  # 0:46 to 1:19
        "tag": "finance"
    }
]


def parse_timestamp(timestamp):
    """
    Convert timestamp tuple to milliseconds.
    Handles both (seconds, seconds) and (minutes, seconds, minutes, seconds) formats.
    """
    if len(timestamp) == 2:
        # Format: (seconds, seconds) - both are in same minute (0:XX)
        start_ms = timestamp[0] * 1000
        end_ms = timestamp[1] * 1000
    elif len(timestamp) == 3:
        # Format: (minutes, seconds, minutes) - start is M:SS, end is M:SS
        start_ms = (timestamp[0] * 60 + timestamp[1]) * 1000
        end_ms = timestamp[2] * 60 * 1000
    elif len(timestamp) == 4:
        # Format: (minutes, seconds, minutes, seconds)
        start_ms = (timestamp[0] * 60 + timestamp[1]) * 1000
        end_ms = (timestamp[2] * 60 + timestamp[3]) * 1000
    else:
        raise ValueError(f"Invalid timestamp format: {timestamp}")
    
    return start_ms, end_ms


def download_audio(search_query, output_path):
    """
    Download audio from YouTube using yt-dlp.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Searching and downloading: {search_query}")
            ydl.download([f"ytsearch1:{search_query}"])
        return True
    except Exception as e:
        print(f"Error downloading {search_query}: {e}")
        return False


def trim_audio(input_file, output_file, timestamps):
    """
    Trim audio file based on timestamps and combine multiple segments if needed.
    """
    try:
        audio = AudioSegment.from_mp3(input_file)
        
        # Process all timestamp segments
        segments = []
        for timestamp in timestamps:
            start_ms, end_ms = parse_timestamp(timestamp)
            segment = audio[start_ms:end_ms]
            segments.append(segment)
        
        # Combine all segments
        if len(segments) > 1:
            combined = segments[0]
            for segment in segments[1:]:
                combined += segment
            final_audio = combined
        else:
            final_audio = segments[0]
        
        # Export trimmed audio
        final_audio.export(output_file, format="mp3")
        print(f"Trimmed audio saved to: {output_file}")
        return True
    except Exception as e:
        print(f"Error trimming audio: {e}")
        return False


def main():
    """
    Main function to download and trim all songs.
    """
    # Create output directory
    output_dir = "/vercel/sandbox/trimmed_mp3"
    os.makedirs(output_dir, exist_ok=True)
    
    temp_dir = "/vercel/sandbox/temp_downloads"
    os.makedirs(temp_dir, exist_ok=True)
    
    for song in SONGS:
        print(f"\n{'='*60}")
        print(f"Processing: {song['name']} ({song['tag']})")
        print(f"{'='*60}")
        
        # Prepare file paths
        temp_file = os.path.join(temp_dir, f"{song['name']}")
        final_output = os.path.join(output_dir, f"{song['tag']}.mp3")
        
        # Download the song
        search_query = f"{song['name']} song"
        if download_audio(search_query, temp_file):
            # Find the downloaded file (yt-dlp adds .mp3 extension)
            downloaded_file = f"{temp_file}.mp3"
            
            if os.path.exists(downloaded_file):
                # Trim the audio
                if trim_audio(downloaded_file, final_output, song['timestamps']):
                    print(f"✓ Successfully created: {final_output}")
                    # Clean up temp file
                    os.remove(downloaded_file)
                else:
                    print(f"✗ Failed to trim: {song['name']}")
            else:
                print(f"✗ Downloaded file not found: {downloaded_file}")
        else:
            print(f"✗ Failed to download: {song['name']}")
    
    # Clean up temp directory
    try:
        os.rmdir(temp_dir)
    except:
        pass
    
    print(f"\n{'='*60}")
    print(f"All processing complete!")
    print(f"Trimmed MP3 files saved in: {output_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
