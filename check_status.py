#!/usr/bin/env python3
"""
Status checker for MP3 trimming project.
Shows what files are present and what's missing.
"""

import os
import sys

# Expected files
EXPECTED_FILES = [
    "palat.mp3",
    "radhe_radhe.mp3",
    "arjun_valley.mp3",
    "shanaya.mp3",
    "karvaan.mp3",
    "maine_tujhe_dekha.mp3",
    "faasla.mp3",
    "sauda_sauda.mp3",
    "galti_se_mistake.mp3",
    "paisa_h_toh.mp3"
]

OUTPUT_FILES = [
    "ui.mp3",
    "admin.mp3",
    "backend.mp3",
    "hr.mp3",
    "migration.mp3",
    "qa.mp3",
    "arun.mp3",
    "marketing.mp3",
    "ai.mp3",
    "finance.mp3"
]


def check_dependencies():
    """Check if required dependencies are installed."""
    print("Checking Dependencies...")
    print("-" * 60)
    
    # Check Python
    print(f"✓ Python: {sys.version.split()[0]}")
    
    # Check pydub
    try:
        import pydub
        print(f"✓ pydub: installed")
    except ImportError:
        print(f"✗ pydub: NOT installed")
        return False
    
    # Check ffmpeg
    if os.system("ffmpeg -version > /dev/null 2>&1") == 0:
        print(f"✓ ffmpeg: installed")
    else:
        print(f"✗ ffmpeg: NOT installed")
        return False
    
    print()
    return True


def check_source_files():
    """Check which source files are present."""
    source_dir = "/vercel/sandbox/source_mp3"
    
    print("Checking Source Files...")
    print("-" * 60)
    print(f"Directory: {source_dir}")
    
    if not os.path.exists(source_dir):
        print(f"✗ Directory does not exist!")
        print(f"  Run: mkdir -p {source_dir}")
        print()
        return 0
    
    present = []
    missing = []
    
    for filename in EXPECTED_FILES:
        filepath = os.path.join(source_dir, filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            size_mb = size / (1024 * 1024)
            present.append((filename, size_mb))
        else:
            missing.append(filename)
    
    if present:
        print(f"\n✓ Found {len(present)} file(s):")
        for filename, size in present:
            print(f"  • {filename} ({size:.2f} MB)")
    
    if missing:
        print(f"\n✗ Missing {len(missing)} file(s):")
        for filename in missing:
            print(f"  • {filename}")
    
    print()
    return len(present)


def check_output_files():
    """Check which output files exist."""
    output_dir = "/vercel/sandbox/trimmed_mp3"
    
    print("Checking Output Files...")
    print("-" * 60)
    print(f"Directory: {output_dir}")
    
    if not os.path.exists(output_dir):
        print(f"✗ Directory does not exist (will be created when script runs)")
        print()
        return 0
    
    present = []
    
    for filename in OUTPUT_FILES:
        filepath = os.path.join(output_dir, filename)
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            size_mb = size / (1024 * 1024)
            present.append((filename, size_mb))
    
    if present:
        print(f"\n✓ Found {len(present)} trimmed file(s):")
        for filename, size in present:
            print(f"  • {filename} ({size:.2f} MB)")
    else:
        print(f"\n⊘ No trimmed files yet")
    
    print()
    return len(present)


def show_next_steps(source_count, output_count):
    """Show what to do next."""
    print("Next Steps...")
    print("-" * 60)
    
    if source_count == 0:
        print("1. Download the 10 songs manually")
        print("2. Rename them according to QUICK_START.md")
        print("3. Place them in /vercel/sandbox/source_mp3/")
        print("4. Run this script again to check status")
    elif source_count < len(EXPECTED_FILES):
        print(f"1. Download the remaining {len(EXPECTED_FILES) - source_count} song(s)")
        print("2. Place them in /vercel/sandbox/source_mp3/")
        print("3. Run this script again to check status")
    elif output_count == 0:
        print("✓ All source files ready!")
        print("\nRun the trimming script:")
        print("  python3 /vercel/sandbox/trim_existing_mp3.py")
    elif output_count < len(OUTPUT_FILES):
        print(f"⚠ Only {output_count}/{len(OUTPUT_FILES)} files were trimmed")
        print("\nRe-run the trimming script:")
        print("  python3 /vercel/sandbox/trim_existing_mp3.py")
    else:
        print("✓ All done! All files have been trimmed successfully!")
        print(f"\nTrimmed files are in: /vercel/sandbox/trimmed_mp3/")
    
    print()


def main():
    """Main function."""
    print("=" * 60)
    print("MP3 Trimming Project - Status Check")
    print("=" * 60)
    print()
    
    # Check dependencies
    if not check_dependencies():
        print("⚠ Please install missing dependencies first!")
        return
    
    # Check source files
    source_count = check_source_files()
    
    # Check output files
    output_count = check_output_files()
    
    # Show summary
    print("Summary...")
    print("-" * 60)
    print(f"Source files: {source_count}/{len(EXPECTED_FILES)}")
    print(f"Trimmed files: {output_count}/{len(OUTPUT_FILES)}")
    print()
    
    # Show next steps
    show_next_steps(source_count, output_count)
    
    print("=" * 60)
    print("For detailed instructions, see:")
    print("  • QUICK_START.md (quick guide)")
    print("  • SETUP_INSTRUCTIONS.md (detailed guide)")
    print("  • PROJECT_SUMMARY.md (complete overview)")
    print("=" * 60)


if __name__ == "__main__":
    main()
