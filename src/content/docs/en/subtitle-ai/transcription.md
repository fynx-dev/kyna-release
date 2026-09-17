---
title: "Whisper Transcription"
description: "Transcribe video audio into timestamped subtitles using local offline Whisper models."
order: 2
group: "Subtitle AI & Translation"
---

# Whisper Transcription

Kyna Player embeds a high-performance **Whisper offline speech recognition engine**, generating accurate timestamped subtitles (`.srt` / `.vtt`) directly from audio tracks.

---

## 🛠️ Configuration Parameters

In sidebar **AI Lab → Speech Transcription**:
- **Source Language**
  Auto-detect or specify source language code (`en`, `ja`, `ko`, `es`, etc.) for higher accuracy.
- **Audio Track Selection**
  Target specific audio commentary or dub tracks.
- **Silero VAD**
  Filters background noise, gunshots, and BGM to prevent AI hallucinations.

---

## 🧠 Model Sizes & Hardware Requirements

| Model | Parameters | VRAM | RTX 4060 Speed | Accuracy | Recommended Use |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tiny** | 39 M | ~0.8 GB | ~30x Speed | Good | Quick summaries, low-end PCs |
| **Base** | 74 M | ~1.0 GB | ~20x Speed | Very Good | Daily English/Chinese videos |
| **Small** | 244 M | ~1.8 GB | ~12x Speed | Excellent *(Recommended)* | General movies & anime series |
| **Medium** | 769 M | ~3.5 GB | ~6x Speed | High | Complex dialects & lectures |
| **Large-v3** | 1550 M | ~6.0 GB | ~3x Speed | State-of-the-Art | Noisy backgrounds, max accuracy |
