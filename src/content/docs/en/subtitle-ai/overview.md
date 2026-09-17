---
title: "AI Subtitles Overview"
description: "Explore Kyna Player's offline Whisper speech recognition and LLM-powered subtitle translation pipeline."
order: 1
group: "Subtitle AI & Translation"
---

# AI Subtitles Overview

Encountered foreign videos without subtitles? Kyna Player includes a built-in **AI Subtitle Lab**, combining local Automatic Speech Recognition (ASR) with Large Language Model (LLM) contextual translation.

---

## ⚡ Core AI Pipeline

```
+------------------+     +--------------------+     +--------------------+     +------------------+
| 🔊 Audio Extract | ──> | 🎙️ Local Whisper   | ──> | 🌐 LLM Translation | ──> | 💬 Live Dual Sub |
|  (FFmpeg Demux)  |     | (100% Offline/Priv)|     | (Context-Aware)    |     |  (Mounted & Sync)|
+------------------+     +--------------------+     +--------------------+     +------------------+
```

---

## 🌟 Highlights

1. **🔒 100% Local Offline Inference**: Whisper speech recognition runs directly on your GPU (CUDA / DirectML / Vulkan) or CPU. No audio leaves your machine.
2. **🧠 Context-Aware LLM Translation**: Connect DeepSeek, OpenAI GPT-4o, Claude, or local Ollama instances to generate nuanced, natural translations.
3. **⚡ Automatic VAD Alignment**: Silero VAD strips background noise and music, splitting natural speaking pauses into aligned subtitle segments.
