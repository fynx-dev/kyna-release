---
title: "Getting Started"
description: "Explore Kyna Player's core highlights, hardware-accelerated video decoding, Anime4K upscaling, and offline Whisper AI subtitles."
order: 1
group: "Getting Started"
---

# Getting Started

Welcome to **Kyna Player** — a modern, ultra-lightweight, and high-performance video player designed specifically for Windows 10 & 11. Powered by Direct3D 11 hardware-accelerated rendering, an offline Whisper AI subtitle transcription engine, Anime4K super-resolution upscaling, and DLSS 5 support, it delivers an unparalleled audiovisual experience.

---

## ✨ Core Highlights & Features

### 🎬 Next-Gen Direct3D 11 GPU Rendering Pipeline
- **Hardware Acceleration (DXVA2 / D3D11VA)**
  Offload decoding entirely to your GPU. Seamlessly play 4K / 8K ultra-high-definition HEVC, AV1, and VP9 videos with near-zero CPU usage.
- **HDR Tone Mapping**
  Built-in Reinhard & Mobius color tone mapping algorithms faithfully restore Dolby Vision and HDR10 wide color gamut on standard SDR displays without washed-out highlights.
- **Micro-Stats OSD (F12)**
  Real-time overlay showing frame time budget, drop counters, and VRAM memory footprint.

### 🤖 Local Offline Whisper AI Subtitle Lab
- **100% On-Device AI Transcription**
  Powered by local Whisper models (`tiny`, `base`, `small`, `medium`, `large-v3`). Transcribe speech to text with accurate timestamps completely offline.
- **Context-Aware LLM Translation**
  Seamlessly integrate DeepSeek, OpenAI GPT-4o, Claude, or local Ollama instances to generate studio-quality bilingual subtitles.
- **Silero VAD Silence Filtering**
  Automatically isolate vocals and suppress background music / noise to eliminate AI hallucinations.

### 🎨 Anime4K & Neural Super-Resolution (DLSS 5)
- **Real-Time Anime Upscaling**
  Reconstruct crisp line-art and rich flat colors for anime content in real-time.
- **Compute Shader Fallback**
  Universal compatibility across NVIDIA RTX, AMD Radeon, and Intel Arc GPUs.
- **Dynamic Performance Fallback**
  Automatically adjust filter intensity during heavy GPU workloads to guarantee 60 FPS playback.

### 🎛️ Clean, Borderless UI & Extensive Shortcuts
- **Frameless Immersive Design**
  Auto-hiding control bar, smooth timeline thumbnail previews, and slide-out side drawers.
- **Dual Subtitle System**
  Display primary and secondary subtitles simultaneously with customizable fonts, sizes, and outlines.
- **DLNA / UPnP Screencasting**
  Wirelessly cast local videos to smart TVs, projectors, or Apple TV devices on your local network.

---

## 🧭 Navigation Guide

- 📦 [Installation & System Requirements](/docs/en/installation/): Minimum hardware specs, SHA-256 verification, and setup instructions.
- 🖥️ [Interface Overview](/docs/en/getting-started/interface-overview/): Master the viewport, title bar, control dock, and side drawers.
- 📂 [Opening Media](/docs/en/getting-started/opening-media/): Drag-and-drop folders, M3U playlists, and network live streams.
- ⏯️ [Basic Playback](/docs/en/getting-started/basic-playback/): Playback controls, seeking gestures, and volume boost.
- 💬 [Subtitles & Dual Subtitles](/docs/en/subtitles/embedded-tracks/): Embedded tracks, online search, and style customization.
- 🤖 [AI Subtitle Lab](/docs/en/subtitle-ai/overview/): Whisper transcription and LLM translation setup.
