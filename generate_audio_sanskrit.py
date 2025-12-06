"""
Script to pre-generate audio files for original Sanskrit verses (in Kannada script).
Run this once to generate all audio files for the original shlokas.
"""

import json
import os
from gtts import gTTS
from pathlib import Path
import time

# Configuration
JSON_FILE_PATH = "bhagavadgita_Chapter_2.json"
AUDIO_DIR = "audio_files"

def load_data():
    """Load the Bhagavad Gita JSON data."""
    with open(JSON_FILE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_audio_for_verse(text, output_path, lang='sa'):
    """Generate audio file for a single verse."""
    try:
        print(f"  Generating Sanskrit audio: {output_path}")
        # Using 'hi' (Hindi) as a proxy for Sanskrit since gTTS doesn't support Sanskrit directly
        # The Kannada script text will be read with Hindi pronunciation
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
        print(f"  ✓ Saved: {output_path}")
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("Pre-generating Audio Files for Original Sanskrit Verses")
    print("=" * 60)
    
    # Create audio directory
    audio_path = Path(AUDIO_DIR)
    audio_path.mkdir(exist_ok=True)
    
    # Create subdirectory for Sanskrit
    (audio_path / "sa").mkdir(exist_ok=True)
    
    # Load data
    print("\nLoading data...")
    data = load_data()
    chapter = data['chapters'][0]
    verses = chapter['verses']
    
    print(f"Found {len(verses)} verses to process.\n")
    
    total_verses = len(verses)
    success_count = 0
    error_count = 0
    
    for idx, verse in enumerate(verses, 1):
        verse_num = verse['verse']
        print(f"\n[{idx}/{total_verses}] Processing Verse {verse_num}...")
        
        # Generate Sanskrit audio (text field contains Sanskrit in Kannada script)
        sa_path = audio_path / "sa" / f"verse_{verse_num}.mp3"
        if sa_path.exists():
            print(f"  ⊙ Sanskrit audio already exists, skipping.")
        else:
            # Try with 'hi' (Hindi) first, fallback to 'kn' (Kannada) if needed
            if generate_audio_for_verse(verse['text'], str(sa_path), 'hi'):
                success_count += 1
            else:
                # Fallback to Kannada
                print(f"  ⚠ Retrying with Kannada language...")
                if generate_audio_for_verse(verse['text'], str(sa_path), 'kn'):
                    success_count += 1
                else:
                    error_count += 1
            time.sleep(1)  # Small delay to avoid rate limiting
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total verses processed: {total_verses}")
    print(f"Audio files generated: {success_count}")
    print(f"Errors: {error_count}")
    print(f"\nAudio files saved in: {audio_path.absolute()}/sa/")
    print("=" * 60)

if __name__ == "__main__":
    main()
