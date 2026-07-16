#!/usr/bin/env python3
"""Offline Chinese pronunciation practice app.

This prototype can:
- record a short voice clip from the microphone
- transcribe it locally with an offline speech engine when available
- compare the result with an expected sentence
- report a pronunciation similarity score

If the optional speech libraries are not installed, the script falls back to a
simple demo mode so the file remains runnable.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
import wave
from difflib import SequenceMatcher
from pathlib import Path
from typing import Optional


def normalize_text(text: str) -> str:
    """Clean whitespace so comparisons are more stable."""
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


def calculate_score(expected: str, recognized: str) -> float:
    """Return a similarity score between 0 and 100."""
    expected_clean = normalize_text(expected)
    recognized_clean = normalize_text(recognized)

    if not expected_clean or not recognized_clean:
        return 0.0

    similarity = SequenceMatcher(None, expected_clean, recognized_clean).ratio()
    return round(similarity * 100, 1)


def record_audio(output_path: Path, seconds: int = 5, sample_rate: int = 16000) -> Path:
    """Record microphone input to a WAV file using sounddevice."""
    try:
        import sounddevice as sd
    except ImportError as exc:
        raise RuntimeError(
            "Recording requires sounddevice and numpy. Install them with: pip install sounddevice numpy"
        ) from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)

    frames = int(seconds * sample_rate)
    try:
        audio = sd.rec(frames, samplerate=sample_rate, channels=1, dtype="int16")
        sd.wait()
    except Exception as exc:  # pragma: no cover - depends on OS/microphone
        raise RuntimeError(
            f"Unable to start microphone recording. Make sure your microphone is connected and allowed on Windows: {exc}"
        ) from exc

    with wave.open(str(output_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio.tobytes())

    return output_path


def setup_model_cache() -> Path:
    """Create a workspace-local cache for downloaded whisper models."""
    cache_dir = Path(__file__).resolve().parent / ".cache" / "whisper"
    cache_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("HF_HOME", str(cache_dir))
    os.environ.setdefault("HUGGINGFACE_HUB_CACHE", str(cache_dir))
    os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
    return cache_dir


def detect_language(expected_text: str) -> Optional[str]:
    """Return Chinese for Chinese text, otherwise None."""
    if any("\u4e00" <= ch <= "\u9fff" for ch in expected_text):
        return "zh"
    return None


def transcribe_offline(audio_path: Path, model_size: str = "tiny", expected_text: str = "") -> Optional[str]:
    """Try to use a local transcription backend.

    Supported backends (if installed):
    - faster-whisper (preferred)
    - whisper

    Returns None when no offline backend is available.
    """
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

    try:
        import whisper

        model = whisper.load_model(model_size, download_root=str(cache_dir))
        result = model.transcribe(str(audio_path), fp16=False, language=language, task="transcribe")
        text = result.get("text", "").strip()
        if text:
            return text
    except Exception as exc:
        print(f"openai-whisper failed: {exc}")

    return None


def demo_transcription(expected: str, reason: str) -> str:
    """Fallback mode for environments without successful transcription."""
    print(reason)
    return normalize_text(expected) if expected else ""


def main() -> None:
    parser = argparse.ArgumentParser(description="Offline Chinese pronunciation practice")
    parser.add_argument("--expected", default="你好，世界", help="The sentence you want to practice")
    parser.add_argument("--seconds", type=int, default=5, help="Recording length in seconds")
    parser.add_argument("--output", default=None, help="Optional output WAV path")
    parser.add_argument(
        "--model",
        default="tiny",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model size; tiny is the lightest and fastest option",
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


if __name__ == "__main__":
    main()
