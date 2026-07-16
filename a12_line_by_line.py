"""
Simple line-by-line explanation of ai2.py.
This version uses very easy English for a beginner.
"""

# 1. This line says this file is a Python script.
#!/usr/bin/env python3

# 2. This is a docstring. It explains what the file does.
"""Offline Chinese pronunciation practice app."""

# 3. This line lets us use future Python features.
from __future__ import annotations

# 4. This imports tools for reading command-line arguments.
import argparse

# 5. This imports tools for working with the operating system.
import os

# 6. This imports tools for using regular expressions.
import re

# 7. This imports tools for working with temporary files.
import tempfile

# 8. This imports tools for saving audio in WAV format.
import wave

# 9. This imports a tool for comparing strings.
from difflib import SequenceMatcher

# 10. This imports tools for working with file paths.
from pathlib import Path

# 11. This imports a tool for optional values.
from typing import Optional


# 12. This function cleans extra spaces from text.
def normalize_text(text: str) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


# 13. This function gives a score from 0 to 100.
def calculate_score(expected: str, recognized: str) -> float:
    expected_clean = normalize_text(expected)
    recognized_clean = normalize_text(recognized)

    if not expected_clean or not recognized_clean:
        return 0.0

    similarity = SequenceMatcher(None, expected_clean, recognized_clean).ratio()
    return round(similarity * 100, 1)


# 14. This function records your voice.
def record_audio(output_path: Path, seconds: int = 5, sample_rate: int = 16000) -> Path:
    try:
        import sounddevice as sd
    except ImportError as exc:
        raise RuntimeError("Recording needs sounddevice and numpy") from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)

    frames = int(seconds * sample_rate)
    try:
        audio = sd.rec(frames, samplerate=sample_rate, channels=1, dtype="int16")
        sd.wait()
    except Exception as exc:
        raise RuntimeError("Microphone did not work") from exc

    with wave.open(str(output_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio.tobytes())

    return output_path


# 15. This function creates a folder for downloaded model files.
def setup_model_cache() -> Path:
    cache_dir = Path(__file__).resolve().parent / ".cache" / "whisper"
    cache_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("HF_HOME", str(cache_dir))
    os.environ.setdefault("HUGGINGFACE_HUB_CACHE", str(cache_dir))
    os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
    return cache_dir


# 16. This function checks if the text is Chinese.
def detect_language(expected_text: str) -> Optional[str]:
    if any("\u4e00" <= ch <= "\u9fff" for ch in expected_text):
        return "zh"
    return None


# 17. This function tries to understand the recorded voice.
def transcribe_offline(audio_path: Path, model_size: str = "tiny", expected_text: str = "") -> Optional[str]:
    cache_dir = setup_model_cache()
    language = detect_language(expected_text)

    try:
        from faster_whisper import WhisperModel

        model = WhisperModel(
            model_size,
            device="cpu",
            compute_type="int8",
            download_root=str(cache_dir),
        )
        segments, _ = model.transcribe(
            str(audio_path),
            beam_size=1,
            vad_filter=True,
            language=language,
            task="transcribe",
        )
        text = " ".join(segment.text for segment in segments).strip()
        if text:
            return text
    except Exception as exc:
        print(f"faster-whisper failed: {exc}")

    return None


# 18. This function gives a simple fallback answer.
def demo_transcription(expected: str, reason: str) -> str:
    print(reason)
    return normalize_text(expected) if expected else ""


# 19. This is the main part of the program.
def main() -> None:
    parser = argparse.ArgumentParser(description="Offline Chinese pronunciation practice")
    parser.add_argument("--expected", default="你好，世界", help="The sentence you want to practice")
    parser.add_argument("--seconds", type=int, default=5, help="Recording length in seconds")
    parser.add_argument("--output", default=None, help="Optional output WAV path")
    parser.add_argument(
        "--model",
        default="tiny",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model size",
    )
    args = parser.parse_args()

    expected = normalize_text(args.expected)
    output_path = Path(args.output) if args.output else Path(tempfile.gettempdir()) / "pronunciation_demo.wav"

    print(f"Practicing: {expected}")
    print(f"Using Whisper model: {args.model}")
    print("Recording your voice...")

    try:
        record_audio(output_path, seconds=args.seconds)
        print(f"Saved audio to: {output_path}")
    except RuntimeError as exc:
        print(f"Recording unavailable: {exc}")
        audio_path = None
    else:
        audio_path = output_path

    if audio_path is not None:
        recognized = transcribe_offline(audio_path, model_size=args.model, expected_text=expected)
    else:
        recognized = None

    if not recognized:
        recognized = demo_transcription(
            expected,
            "Offline transcription did not return a result; using the expected sentence as a placeholder.",
        )

    score = calculate_score(expected, recognized)

    print("\nResults")
    print("-" * 30)
    print(f"Expected : {expected}")
    print(f"Recognized: {recognized}")
    print(f"Score: {score:.1f}/100")

    if score >= 85:
        print("Excellent pronunciation!")
    elif score >= 60:
        print("Good effort. Try a little slower and clearer.")
    else:
        print("Keep practicing. Focus on clearer pronunciation and pacing.")


# 20. This line starts the program.
if __name__ == "__main__":
    main()
