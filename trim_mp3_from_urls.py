#!/usr/bin/env python3
"""
Script to download and trim MP3 files from direct URLs.
This version uses alternative methods to bypass YouTube restrictions.
"""

import os
import sys
from pydub import AudioSegment
import yt_dlp
import time

# Song data with timestamps and names
SONGS = [
    {
        "name": "palat",
        "url": "https://www.youtube.com/watch?v=9vkcYxbGdTE",
        "start": "0:26",
        "end": "1:03",
        "tag": "ui"
    },
    {
        "name": "radhe_radhe",
        "url": "https://www.youtube.com/watch?v=61EGpAy4Ids",
        "start": "0:11",
        "end": "0:37",
        "tag": "admin"
    },
    {
        "name": "arjun_valley",
        "url": "https://www.youtube.com/watch?v=zqGW6x_5N0k",
        "start": "0:00",
        "end": "0:30",
        "tag": "backend"
    },
    {
        "name": "shanaya",
        "url": "https://www.youtube.com/watch?v=YEGFMb3SS3E",
        "start": "0:00",
        "end": "0:48",
        "tag": "hr"
    },
    {
        "name": "karvaan",
        "url": "https://www.youtube.com/watch?v=8qCVXCFREkQ",
        "start": "1:06",
        "end": "1:31",
        "tag": "migration"
    },
    {
        "name": "maine_tujhe_dekha",
        "url": "https://www.youtube.com/watch?v=s0G3Lou00-c",
        "start": "1:05",
        "end": "1:22",
        "tag": "qa"
    },
    {
        "name": "faasla",
        "url": "https://www.youtube.com/watch?v=AEDOoHqSfpU",
        "segments": [("0:00", "0:18"), ("0:36", "0:57")],
        "tag": "arun"
    },
    {
        "name": "sauda_sauda",
        "url": "https://www.youtube.com/watch?v=CxAWKewvooo",
        "segments": [("0:12", "0:19"), ("0:50", "1:33")],
        "tag": "marketing"
    },
    {
        "name": "galti_se_mistake",
        "url": "https://www.youtube.com/watch?v=05TA9jNnCdU",
        "start": "0:09",
        "end": "0:51",
        "tag": "ai"
    },
    {
        "name": "paisa_h_toh",
        "url": "https://www.youtube.com/watch?v=u56vBNUoR1I",
        "start": "0:46",
        "end": "1:19",
        "tag": "finance"
    }
]


def time_to_ms(time_str):
    """Convert time string (M:SS or MM:SS) to milliseconds."""
    parts = time_str.split(':')
    if len(parts) == 2:
        minutes, seconds = int(parts[0]), int(parts[1])
        return (minutes * 60 + seconds) * 1000
    return 0


def download_audio_with_retry(url, output_path, max_retries=3):
    """
    Download audio from YouTube with retry logic and bot bypass techniques.
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
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'web'],
                'player_skip': ['webpage', 'configs'],
            }
        },
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-us,en;q=0.5',
            'Sec-Fetch-Mode': 'navigate',
        }
    }
    
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1}/{max_retries} to download from: {url}")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            return True
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 5
                print(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
            else:
                print(f"All attempts failed for {url}")
                return False
    
    return False


def trim_audio(input_file, output_file, segments):
    """
    Trim audio file based on time segments and combine if multiple.
    """
    try:
        audio = AudioSegment.from_mp3(input_file)
        
        # Process all segments
        audio_segments = []
        for start_time, end_time in segments:
            start_ms = time_to_ms(start_time)
            end_ms = time_to_ms(end_time)
            segment = audio[start_ms:end_ms]
            audio_segments.append(segment)
        
        # Combine all segments
        if len(audio_segments) > 1:
            combined = audio_segments[0]
            for segment in audio_segments[1:]:
                combined += segment
            final_audio = combined
        else:
            final_audio = audio_segments[0]
        
        # Export trimmed audio
        final_audio.export(output_file, format="mp3")
        print(f"✓ Trimmed audio saved to: {output_file}")
        return True
    except Exception as e:
        print(f"✗ Error trimming audio: {e}")
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
    
    success_count = 0
    failed_songs = []
    
    for song in SONGS:
        print(f"\n{'='*60}")
        print(f"Processing: {song['name']} ({song['tag']})")
        print(f"{'='*60}")
        
        # Prepare file paths
        temp_file = os.path.join(temp_dir, f"{song['name']}")
        final_output = os.path.join(output_dir, f"{song['tag']}.mp3")
        
        # Download the song
        if download_audio_with_retry(song['url'], temp_file):
            # Find the downloaded file (yt-dlp adds .mp3 extension)
            downloaded_file = f"{temp_file}.mp3"
            
            if os.path.exists(downloaded_file):
                # Prepare segments
                if 'segments' in song:
                    segments = song['segments']
                else:
                    segments = [(song['start'], song['end'])]
                
                # Trim the audio
                if trim_audio(downloaded_file, final_output, segments):
                    success_count += 1
                    print(f"✓ Successfully created: {final_output}")
                    # Clean up temp file
                    try:
                        os.remove(downloaded_file)
                    except:
                        pass
                else:
                    failed_songs.append(song['name'])
            else:
                print(f"✗ Downloaded file not found: {downloaded_file}")
                failed_songs.append(song['name'])
        else:
            print(f"✗ Failed to download: {song['name']}")
            failed_songs.append(song['name'])
    
    # Clean up temp directory
    try:
        os.rmdir(temp_dir)
    except:
        pass
    
    print(f"\n{'='*60}")
    print(f"Processing Summary:")
    print(f"  Successful: {success_count}/{len(SONGS)}")
    print(f"  Failed: {len(failed_songs)}/{len(SONGS)}")
    if failed_songs:
        print(f"  Failed songs: {', '.join(failed_songs)}")
    print(f"\nTrimmed MP3 files saved in: {output_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
