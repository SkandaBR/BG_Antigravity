"""
Script to pre-generate audio files for all verses in both English and Kannada.
Run this once to generate all audio files, then the app will use them directly.
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

def generate_audio_for_verse(text, output_path, lang='en'):
    """Generate audio file for a single verse."""
    try:
        print(f"  Generating {lang} audio: {output_path}")
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
        print(f"  ✓ Saved: {output_path}")
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("Pre-generating Audio Files for Bhagavad Gita Chapter 2")
    print("=" * 60)
    
    # Create audio directory
    audio_path = Path(AUDIO_DIR)
    audio_path.mkdir(exist_ok=True)
    
    # Create subdirectories for each language
    (audio_path / "en").mkdir(exist_ok=True)
    (audio_path / "kn").mkdir(exist_ok=True)
    
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
        
        # Generate English audio
        en_path = audio_path / "en" / f"verse_{verse_num}.mp3"
        if en_path.exists():
            print(f"  ⊙ English audio already exists, skipping.")
        else:
            if generate_audio_for_verse(verse['english_translation'], str(en_path), 'en'):
                success_count += 1
            else:
                error_count += 1
            time.sleep(1)  # Small delay to avoid rate limiting
        
        # Generate Kannada audio
        kn_path = audio_path / "kn" / f"verse_{verse_num}.mp3"
        if kn_path.exists():
            print(f"  ⊙ Kannada audio already exists, skipping.")
        else:
            if generate_audio_for_verse(verse['translation'], str(kn_path), 'kn'):
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
    print(f"\nAudio files saved in: {audio_path.absolute()}")
    print("=" * 60)

if __name__ == "__main__":
    main()
