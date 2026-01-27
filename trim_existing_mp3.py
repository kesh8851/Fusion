#!/usr/bin/env python3
"""
Script to trim existing MP3 files based on provided timestamps.
Place your MP3 files in the 'source_mp3' directory with the correct names.
"""

import os
import sys
from pydub import AudioSegment

# Song data with timestamps and output names
SONGS = [
    {
        "source_name": "palat.mp3",
        "segments": [("0:26", "1:03")],
        "output_name": "ui.mp3"
    },
    {
        "source_name": "radhe_radhe.mp3",
        "segments": [("0:11", "0:37")],
        "output_name": "admin.mp3"
    },
    {
        "source_name": "arjun_valley.mp3",
        "segments": [("0:00", "0:30")],
        "output_name": "backend.mp3"
    },
    {
        "source_name": "shanaya.mp3",
        "segments": [("0:00", "0:48")],
        "output_name": "hr.mp3"
    },
    {
        "source_name": "karvaan.mp3",
        "segments": [("1:06", "1:31")],
        "output_name": "migration.mp3"
    },
    {
        "source_name": "maine_tujhe_dekha.mp3",
        "segments": [("1:05", "1:22")],
        "output_name": "qa.mp3"
    },
    {
        "source_name": "faasla.mp3",
        "segments": [("0:00", "0:18"), ("0:36", "0:57")],
        "output_name": "arun.mp3"
    },
    {
        "source_name": "sauda_sauda.mp3",
        "segments": [("0:12", "0:19"), ("0:50", "1:33")],
        "output_name": "marketing.mp3"
    },
    {
        "source_name": "galti_se_mistake.mp3",
        "segments": [("0:09", "0:51")],
        "output_name": "ai.mp3"
    },
    {
        "source_name": "paisa_h_toh.mp3",
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


def trim_audio(input_file, output_file, segments):
    """
    Trim audio file based on time segments and combine if multiple.
    """
    try:
        print(f"  Loading: {os.path.basename(input_file)}")
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
        print(f"  ✓ Saved: {os.path.basename(output_file)} (duration: {duration:.1f}s)")
        return True
    except FileNotFoundError:
        print(f"  ✗ Source file not found: {os.path.basename(input_file)}")
        return False
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def main():
    """
    Main function to trim all songs.
    """
    # Define directories
    source_dir = "/vercel/sandbox/source_mp3"
    output_dir = "/vercel/sandbox/trimmed_mp3"
    
    # Create directories
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    print("="*60)
    print("MP3 Trimming Script")
    print("="*60)
    print(f"\nSource directory: {source_dir}")
    print(f"Output directory: {output_dir}\n")
    
    # Check if source directory has files
    source_files = [f for f in os.listdir(source_dir) if f.endswith('.mp3')]
    if not source_files:
        print("⚠ No MP3 files found in source directory!")
        print(f"\nPlease place your MP3 files in: {source_dir}")
        print("\nExpected file names:")
        for song in SONGS:
            print(f"  - {song['source_name']}")
        print("\n" + "="*60)
        return
    
    print(f"Found {len(source_files)} MP3 file(s) in source directory\n")
    
    success_count = 0
    skipped_count = 0
    
    for song in SONGS:
        print(f"Processing: {song['source_name']} → {song['output_name']}")
        
        source_path = os.path.join(source_dir, song['source_name'])
        output_path = os.path.join(output_dir, song['output_name'])
        
        if not os.path.exists(source_path):
            print(f"  ⊘ Skipped (source file not found)")
            skipped_count += 1
        elif trim_audio(source_path, output_path, song['segments']):
            success_count += 1
        
        print()
    
    print("="*60)
    print("Summary:")
    print(f"  ✓ Successfully trimmed: {success_count}/{len(SONGS)}")
    print(f"  ⊘ Skipped: {skipped_count}/{len(SONGS)}")
    print(f"\nOutput files saved in: {output_dir}")
    print("="*60)


if __name__ == "__main__":
    main()
