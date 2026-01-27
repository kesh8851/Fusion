#!/usr/bin/env python3
"""
Alternative download script using Cobalt API for YouTube downloads.
This bypasses YouTube's bot detection by using a third-party service.
"""

import os
import sys
import requests
import time
from pydub import AudioSegment

# Cobalt API endpoint
COBALT_API = "https://api.cobalt.tools/api/json"

# Song data
SONGS = [
    {
        "name": "palat",
        "url": "https://www.youtube.com/watch?v=9vkcYxbGdTE",
        "segments": [("0:26", "1:03")],
        "output_name": "ui.mp3"
    },
    {
        "name": "radhe_radhe",
        "url": "https://www.youtube.com/watch?v=61EGpAy4Ids",
        "segments": [("0:11", "0:37")],
        "output_name": "admin.mp3"
    },
    {
        "name": "arjun_valley",
        "url": "https://www.youtube.com/watch?v=zqGW6x_5N0k",
        "segments": [("0:00", "0:30")],
        "output_name": "backend.mp3"
    },
    {
        "name": "shanaya",
        "url": "https://www.youtube.com/watch?v=YEGFMb3SS3E",
        "segments": [("0:00", "0:48")],
        "output_name": "hr.mp3"
    },
    {
        "name": "karvaan",
        "url": "https://www.youtube.com/watch?v=8qCVXCFREkQ",
        "segments": [("1:06", "1:31")],
        "output_name": "migration.mp3"
    },
    {
        "name": "maine_tujhe_dekha",
        "url": "https://www.youtube.com/watch?v=s0G3Lou00-c",
        "segments": [("1:05", "1:22")],
        "output_name": "qa.mp3"
    },
    {
        "name": "faasla",
        "url": "https://www.youtube.com/watch?v=AEDOoHqSfpU",
        "segments": [("0:00", "0:18"), ("0:36", "0:57")],
        "output_name": "arun.mp3"
    },
    {
        "name": "sauda_sauda",
        "url": "https://www.youtube.com/watch?v=CxAWKewvooo",
        "segments": [("0:12", "0:19"), ("0:50", "1:33")],
        "output_name": "marketing.mp3"
    },
    {
        "name": "galti_se_mistake",
        "url": "https://www.youtube.com/watch?v=05TA9jNnCdU",
        "segments": [("0:09", "0:51")],
        "output_name": "ai.mp3"
    },
    {
        "name": "paisa_h_toh",
        "url": "https://www.youtube.com/watch?v=u56vBNUoR1I",
        "segments": [("0:46", "1:19")],
        "output_name": "finance.mp3"
    }
]


def time_to_ms(time_str):
    """Convert time string (M:SS or MM:SS) to milliseconds."""
    parts = time_str.split(':')
    if len(parts) == 2:
        minutes, seconds = int(parts[0]), int(parts[1])
        return (minutes * 60 + seconds) * 1000
    return 0


def download_with_cobalt(url, output_path):
    """
    Download audio using Cobalt API.
    """
    try:
        print(f"  Requesting download link from Cobalt API...")
        
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        
        data = {
            'url': url,
            'isAudioOnly': True,
            'aFormat': 'mp3',
            'filenamePattern': 'basic'
        }
        
        response = requests.post(COBALT_API, json=data, headers=headers, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            
            if result.get('status') == 'stream' or result.get('status') == 'redirect':
                download_url = result.get('url')
                
                if download_url:
                    print(f"  Downloading audio file...")
                    audio_response = requests.get(download_url, timeout=60)
                    
                    if audio_response.status_code == 200:
                        with open(output_path, 'wb') as f:
                            f.write(audio_response.content)
                        print(f"  ✓ Downloaded successfully")
                        return True
                    else:
                        print(f"  ✗ Failed to download audio (HTTP {audio_response.status_code})")
                        return False
            else:
                print(f"  ✗ Cobalt API error: {result.get('text', 'Unknown error')}")
                return False
        else:
            print(f"  ✗ Cobalt API request failed (HTTP {response.status_code})")
            return False
            
    except requests.exceptions.Timeout:
        print(f"  ✗ Request timed out")
        return False
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def trim_audio(input_file, output_file, segments):
    """
    Trim audio file based on time segments and combine if multiple.
    """
    try:
        print(f"  Loading audio for trimming...")
        audio = AudioSegment.from_mp3(input_file)
        
        # Process all segments
        audio_segments = []
        for start_time, end_time in segments:
            start_ms = time_to_ms(start_time)
            end_ms = time_to_ms(end_time)
            print(f"  Extracting segment: {start_time} to {end_time}")
            segment = audio[start_ms:end_ms]
            audio_segments.append(segment)
        
        # Combine all segments
        if len(audio_segments) > 1:
            print(f"  Combining {len(audio_segments)} segments...")
            combined = audio_segments[0]
            for segment in audio_segments[1:]:
                combined += segment
            final_audio = combined
        else:
            final_audio = audio_segments[0]
        
        # Export trimmed audio
        final_audio.export(output_file, format="mp3", bitrate="192k")
        duration = len(final_audio) / 1000.0
        print(f"  ✓ Trimmed and saved: {os.path.basename(output_file)} (duration: {duration:.1f}s)")
        return True
    except Exception as e:
        print(f"  ✗ Error trimming: {e}")
        return False


def main():
    """
    Main function to download and trim all songs.
    """
    # Create directories
    temp_dir = "/vercel/sandbox/temp_downloads"
    output_dir = "/vercel/sandbox/trimmed_mp3"
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    print("="*60)
    print("MP3 Download and Trim Script (Cobalt API)")
    print("="*60)
    print(f"\nOutput directory: {output_dir}\n")
    
    success_count = 0
    failed_songs = []
    
    for i, song in enumerate(SONGS, 1):
        print(f"[{i}/{len(SONGS)}] Processing: {song['name']}")
        
        temp_file = os.path.join(temp_dir, f"{song['name']}.mp3")
        output_file = os.path.join(output_dir, song['output_name'])
        
        # Download the song
        if download_with_cobalt(song['url'], temp_file):
            # Trim the audio
            if trim_audio(temp_file, output_file, song['segments']):
                success_count += 1
                # Clean up temp file
                try:
                    os.remove(temp_file)
                except:
                    pass
            else:
                failed_songs.append(song['name'])
        else:
            failed_songs.append(song['name'])
        
        print()
        
        # Small delay between requests to be respectful
        if i < len(SONGS):
            time.sleep(2)
    
    # Clean up temp directory
    try:
        os.rmdir(temp_dir)
    except:
        pass
    
    print("="*60)
    print("Summary:")
    print(f"  ✓ Successfully processed: {success_count}/{len(SONGS)}")
    print(f"  ✗ Failed: {len(failed_songs)}/{len(SONGS)}")
    if failed_songs:
        print(f"  Failed songs: {', '.join(failed_songs)}")
    print(f"\nOutput files saved in: {output_dir}")
    print("="*60)


if __name__ == "__main__":
    main()
