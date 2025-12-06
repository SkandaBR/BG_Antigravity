# Pre-generating Audio Files

To improve performance, run this script once to pre-generate all audio files:

```bash
python generate_audio.py
```

This will:
1. Create an `audio_files` directory
2. Generate audio for all 72 verses in both English and Kannada
3. Save them as MP3 files

The app will then load these files instantly instead of generating them on-demand.

**Note:** This process may take some time (approximately 2-3 minutes per verse due to network calls to Google TTS). You can run it in the background and the app will use whatever files are available.
