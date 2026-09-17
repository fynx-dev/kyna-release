#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Complete English (en) Documentation Generator for Kyna Player (All 39 Docs)"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_EN = os.path.join(BASE_DIR, 'src', 'content', 'docs', 'en')

def write(rel_path, content):
    full_path = os.path.join(DOCS_EN, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"[en] Generated {rel_path}")

# ==========================================
# 1. Getting Started & Installation
# ==========================================

write("getting-started.md", """---
title: "Getting Started with Kyna Player"
description: "Explore Kyna Player's core highlights, hardware-accelerated video decoding, Anime4K upscaling, and offline Whisper AI subtitles."
order: 1
group: "Getting Started"
---

# 🚀 Getting Started with Kyna Player

Welcome to **Kyna Player** — a modern, ultra-lightweight, and high-performance video player designed specifically for Windows 10 & 11. Powered by Direct3D 11 hardware-accelerated rendering, an offline Whisper AI subtitle transcription engine, Anime4K super-resolution upscaling, and DLSS 5 support, it delivers an unparalleled audiovisual experience.

---

## ✨ Core Highlights & Features

### 🎬 Next-Gen Direct3D 11 GPU Rendering Pipeline
- **Hardware Acceleration (DXVA2 / D3D11VA)**: Offload decoding entirely to your GPU. Seamlessly play 4K / 8K ultra-high-definition HEVC, AV1, and VP9 videos with near-zero CPU usage.
- **HDR Tone Mapping**: Built-in Reinhard & Mobius color tone mapping algorithms faithfully restore Dolby Vision and HDR10 wide color gamut on standard SDR displays without washed-out highlights.
- **Micro-Stats OSD (F12)**: Real-time overlay showing frame time budget, drop counters, and VRAM memory footprint.

### 🤖 Local Offline Whisper AI Subtitle Lab
- **100% On-Device AI Transcription**: Powered by local Whisper models (`tiny`, `base`, `small`, `medium`, `large-v3`). Transcribe speech to text with accurate timestamps completely offline.
- **Context-Aware LLM Translation**: Seamlessly integrate DeepSeek, OpenAI GPT-4o, Claude, or local Ollama instances to generate studio-quality bilingual subtitles.
- **Silero VAD Silence Filtering**: Automatically isolate vocals and suppress background music / noise to eliminate AI hallucinations.

### 🎨 Anime4K & Neural Super-Resolution (DLSS 5)
- **Real-Time Anime Upscaling**: Reconstruct crisp line-art and rich flat colors for anime content in real-time.
- **Compute Shader Fallback**: Universal compatibility across NVIDIA RTX, AMD Radeon, and Intel Arc GPUs.
- **Dynamic Performance Fallback**: Automatically adjust filter intensity during heavy GPU workloads to guarantee 60 FPS playback.

### 🎛️ Clean, Borderless UI & Extensive Shortcuts
- **Frameless Immersive Design**: Auto-hiding control bar, smooth timeline thumbnail previews, and slide-out side drawers.
- **Dual Subtitle System**: Display primary and secondary subtitles simultaneously with customizable fonts, sizes, and outlines.
- **DLNA / UPnP Screencasting**: Wirelessly cast local videos to smart TVs, projectors, or Apple TV devices on your local network.

---

## 🧭 Navigation Guide

- 📦 [Installation & System Requirements](/docs/en/installation/): Minimum hardware specs, SHA-256 verification, and setup instructions.
- 🖥️ [Interface Overview](/docs/en/getting-started/interface-overview/): Master the viewport, title bar, control dock, and side drawers.
- 📂 [Opening Media](/docs/en/getting-started/opening-media/): Drag-and-drop folders, M3U playlists, and network live streams.
- ⏯️ [Basic Playback](/docs/en/getting-started/basic-playback/): Playback controls, seeking gestures, and volume boost.
- 💬 [Subtitles & Dual Subtitles](/docs/en/subtitles/embedded-tracks/): Embedded tracks, online search, and style customization.
- 🤖 [AI Subtitle Lab](/docs/en/subtitle-ai/overview/): Whisper transcription and LLM translation setup.
""")

write("installation.md", """---
title: "Installation & System Requirements"
description: "Detailed system requirements, SHA-256 verification, installation, update, and uninstallation guide for Kyna Player on Windows."
order: 2
group: "Getting Started"
---

## System Requirements

To ensure the best 4K / HDR video playback and AI subtitle generation performance, your system should meet the following requirements:

| Component | Minimum Requirements | Recommended Specifications |
| :--- | :--- | :--- |
| **Operating System** | Windows 10 (64-bit) 1909+ | Windows 11 (22H2+) |
| **Processor (CPU)** | Intel Core i3 / AMD Ryzen 3 | Intel Core i5 / AMD Ryzen 5 or higher |
| **Graphics (GPU)** | DX11 Hardware Decoding Support | DX12 / HEVC / AV1 / VP9 Hardware Acceleration |
| **Memory (RAM)** | 4 GB | 8 GB or higher |

## Installation Steps

1. Visit the official [GitHub Releases](https://github.com/fynx-dev/kyna-release/releases/latest) page to download the latest `Kyna-Setup.exe` installer and matching `SHA256SUMS` file.
2. (Optional) Run the following PowerShell command in terminal to verify SHA-256 checksum:
   ```powershell
   Get-FileHash .\\Kyna-Setup.exe -Algorithm SHA256
   ```
   Confirm the calculated hash strictly matches the published checksum.
3. Launch `Kyna-Setup.exe`, select your desired destination folder, and complete the installation wizard.
4. Launch Kyna Player via the Start Menu or Desktop shortcut.

## First-Run Tips

- **Hardware Decoding & Tone Mapping**: On first launch, Kyna Player automatically probes GPU capabilities and enables Direct3D 11 hardware decoding along with HDR-to-SDR tone mapping.
- **Whisper AI Models**: The main installer does not bundle heavy model weights. Download or import models on-demand via the "Subtitles -> Local AI" panel.

## Updates & Uninstallation

- **Updating**: Close any running instances of Kyna Player and run the latest `Kyna-Setup.exe` to upgrade in-place. Your custom preferences, hotkeys, and AI models will be preserved.
- **Uninstallation**: Uninstall cleanly via Windows "Settings -> Installed Apps" or the Start Menu shortcut.
""")

write("getting-started/interface-overview.md", """---
title: "Interface Overview"
description: "Comprehensive guide to Kyna Player's UI layout, control dock, slide-out sidebar, and gesture areas."
order: 2
group: "Getting Started & Interface"
---

# 🖥️ Interface Overview

Kyna Player adopts a modern **frameless immersive design**, eliminating visual distractions while offering fast and intuitive access to playback controls and side drawers.

---

## 📐 Layout Overview

![Interface Overview](/assets/images/docs/getting-started/openfile-playlist-settings.png)

Kyna Player is composed of four primary interface zones:

```
+-------------------------------------------------------------+
| 🏷️ Title Bar (Window controls / Always-on-Top / Media Title)  |
+-------------------------------------------------------------+
|                                                             |
|                                            +--------------+ |
|                                            |              | |
|                    📺 Video Viewport         |  📑 Sidebar  | |
|                 (Gestures / Scaling)       |   (Drawers)  | |
|                                            |              | |
|                                            +--------------+ |
+-------------------------------------------------------------+
| 🎛️ Floating Control Bar (Timeline / Controls / Volume / Hub)  |
+-------------------------------------------------------------+
```

---

## 1. 🏷️ Top Title Bar

Appears when moving the mouse to the top edge (auto-hidden in full-screen):
- **📌 Always-on-Top**: Pin the player above all other windows.
- **🎬 Media Title**: Displays the current video/audio file name.
- **⚙️ Window Controls**: Minimize, Maximize / Restore, and Close.

---

## 2. 📺 Video Viewport

The primary hardware-accelerated rendering surface, supporting direct mouse gestures:

| Action | Result |
| :--- | :--- |
| **Single Click** | Toggle Play / Pause (configurable) |
| **Double Click** | Toggle Fullscreen mode |
| **Mouse Wheel** | Adjust volume (±5% step) |
| **Seek Dragging** | Displays centered time stamp and preview HUD |
| **Drop Media** | Drag files, folders, or subtitles directly into the viewport |
| **Right Click** | Open the context menu (Tracks, Filters, Settings, etc.) |

---

## 3. 🎛️ Floating Control Bar

Houses all primary playback controls:
- **Interactive Timeline**: Hover over the progress bar to preview keyframe thumbnails.
- **Playback Controls**: Previous / Next (<kbd>PageUp</kbd>/<kbd>PageDown</kbd>), Play / Pause (<kbd>Space</kbd>), Stop (<kbd>S</kbd>), and Frame Step (<kbd>.</kbd>).
- **Volume & Boost**: Smooth slider supporting up to 200% software volume gain.
- **Speed & Modes**: Quick presets for 0.5x ~ 2.0x speeds and repeat modes (Loop, Single, Shuffle, Sequential).

---

## 4. 📑 Slide-Out Sidebar Drawers

Open via control dock icons or dedicated hotkeys:

| Panel | Description | Hotkey |
| :--- | :--- | :--- |
| 📑 **Playlist** | Manage queue, search items, import folders | `F3` / `Alt+P` |
| 💬 **Tracks & Subtitles** | Track selection, dual subtitles, styling | `Alt+S` |
| 🤖 **AI Lab** | Whisper speech transcription, LLM translation | `Alt+A` |
| ✨ **Video Enhance** | Anime4K, DLSS 5, shaders, color tuning | `Alt+V` |
| ⚙️ **Settings** | Hardware decoding, file associations, i18n | `F2` / `Ctrl+,` |
""")

write("getting-started/opening-media.md", """---
title: "Opening Media"
description: "Learn how to open local videos, scan folders, load M3U playlists, and stream online media in Kyna Player."
order: 3
group: "Getting Started & Interface"
---

# 📂 Opening Media

**Kyna Player** provides versatile ways to load media. Whether opening a single local file, batch-importing a folder, loading an M3U playlist, or streaming a live URL, playback starts instantly.

---

## 📂 1. Open Local Media Files

### Quick Access
- **Hotkey**: Press <kbd>O</kbd> to bring up the Windows file dialog.
- **UI Button**: Click the **Open File** button in the title bar menu or control bar.
- **Supported Formats**: MP4, MKV, AVI, MOV, WEBM, FLV, WMV, TS, M2TS, M4V, RMVB, 3GP, VOB, and more.

![Open File Menu](/assets/images/docs/getting-started/openfile-menu.png)

### Playlist Opening Strategy
Configure default behavior in **Settings → Playlist**:
- 🔄 **Replace & Play** (Default): Clears the current temporary queue and starts playing the new file immediately.
- ➕ **Append & Play**: Keeps existing items, adds the new file to the end, and starts playback.

![Playlist Settings](/assets/images/docs/getting-started/openfile-playlist-settings.png)

---

## 🖱️ 2. Drag & Drop Files and Folders

### Dragging Files
Drag one or more video/audio files directly from Windows Explorer into Kyna Player.

### Dragging Folders (Batch Scanning)
When dropping an entire series folder or music album, the **Folder Import** dialog appears:
- 🔍 **Recursive Scan**: Check "Scan subfolders" to traverse all nested folders.
- 📊 **Real-time Counter**: Shows scanning progress and detected media count.
- ⚡ **Natural Sorting**: Automatically sorts episodes naturally (e.g. EP01, EP02 ... EP10).

![Drag Files & Folder Scan](/assets/images/docs/getting-started/drag-files-and-folder.png)

---

## 🌐 3. Stream Network URLs

Kyna Player supports direct playback of online network streams and live broadcasts:
- **Open URL Dialog**: Press <kbd>Ctrl</kbd> + <kbd>U</kbd>.
- **Supported Protocols**: HTTP / HTTPS direct video streams, HLS (`.m3u8`), RTMP, RTSP, and WebDAV.

![Open URL Dialog](/assets/images/docs/getting-started/open-url-dialog.png)
""")

write("getting-started/basic-playback.md", """---
title: "Basic Playback & Hotkeys"
description: "Master essential playback controls, volume adjustment, speed switching, and shortcut navigation."
order: 4
group: "Getting Started & Interface"
---

# ⏯️ Basic Playback & Hotkeys

Kyna Player offers responsive controls with full keyboard shortcut and mouse gesture support.

---

## 🎮 Essential Playback Controls

| Action | Default Hotkey | Mouse Gesture | Description |
| :--- | :--- | :--- | :--- |
| **Play / Pause** | <kbd>Space</kbd> | Click viewport center | Toggle playback state |
| **Stop** | <kbd>S</kbd> / <kbd>Ctrl+S</kbd> | Control bar Stop button | Stop decoding and reset position |
| **Fullscreen** | <kbd>Enter</kbd> / <kbd>F11</kbd> | Double click viewport | Enter/exit fullscreen |
| **Frame Step Forward** | <kbd>.</kbd> / <kbd>E</kbd> | Frame step button | Advance by exactly one frame |
| **Frame Step Backward** | <kbd>,</kbd> | Frame step backward | Step backward by one frame |
| **Volume Up / Down** | <kbd>↑</kbd> / <kbd>↓</kbd> | Wheel up / down | Adjust volume by ±5% |
| **Mute Toggle** | <kbd>M</kbd> | Click speaker icon | Mute or restore sound |
| **Speed Up / Down** | <kbd>]</kbd> / <kbd>[</kbd> | Speed menu | Adjust speed by ±0.1x |
| **Reset Speed (1.0x)** | <kbd>Backspace</kbd> / <kbd>Z</kbd> | Speed menu (1.0x) | Reset speed to normal |

---

## ⏩ Seeking & Progress Navigation

- **Short Seek (±5s)**: Press <kbd>→</kbd> / <kbd>←</kbd>.
- **Medium Seek (±30s)**: Press <kbd>Ctrl</kbd> + <kbd>→</kbd> / <kbd>←</kbd>.
- **Long Seek (±60s)**: Press <kbd>Shift</kbd> + <kbd>→</kbd> / <kbd>←</kbd>.
- **Percentage Seek (0%~90%)**: Press number keys <kbd>0</kbd> ~ <kbd>9</kbd>.
""")

# ==========================================
# 2. Playback & Seeking
# ==========================================

write("playback/controls.md", """---
title: "Playback, Pause, Stop & Frame Stepping"
description: "Master Kyna Player's core playback controls, including play/pause, stop, frame stepping, speed control, and volume boost."
order: 1
group: "Playback & Seeking"
---

# ⏯️ Playback Controls & Frame Stepping

Kyna Player provides ultra-responsive playback controls. Whether enjoying movies or performing frame-accurate analysis, everything is easily accessible.

---

## 🎮 Basic Playback Controls

### 1. Play & Pause
- **Hotkey**: <kbd>Space</kbd>
- **Mouse Action**: Click the `▶ / ❚❚` button in the control bar or click the viewport center.
- **Zero Latency**: Multi-threaded rendering ensures instantaneous pause and resume with rock-solid audio/video sync.

### 2. Stop
- **Hotkey**: <kbd>S</kbd> or <kbd>Ctrl</kbd> + <kbd>S</kbd>
- **Behavior**: Completely stops decoding, frees stream caches, and resets timeline to `00:00:00`.

---

## 🎞️ Frame Stepping (Forward & Backward)

Essential for inspecting high-speed action, capturing frame-perfect stills, or analyzing animation keyframes:

| Action | Hotkey | Description |
| :--- | :--- | :--- |
| **Frame Forward** | <kbd>.</kbd> / <kbd>E</kbd> | Advance exactly one frame while paused |
| **Frame Backward** | <kbd>,</kbd> | Step backward exactly one frame while paused |

> [!TIP]
> Pressing frame step keys while playing will automatically pause the video first, preventing flickering.

---

## ⏩ Speed Control with Pitch Preservation

Kyna Player uses high-fidelity time-stretching algorithms to preserve natural audio pitch across all speeds:
- **Preset Selection**: Click the speed badge (e.g. `1.0x`) to choose `0.5x`, `0.75x`, `1.0x`, `1.25x`, `1.5x`, or `2.0x`.
- **Keyboard Tuning**:
  - Speed Up: <kbd>]</kbd> or <kbd>C</kbd> (+0.1x)
  - Slow Down: <kbd>[</kbd> or <kbd>X</kbd> (-0.1x)
  - Reset: <kbd>Backspace</kbd> or <kbd>Z</kbd> (1.0x)

---

## 🔊 Volume Control & 200% Boost

- **Mouse Wheel**: Scroll over the viewport to adjust volume in 5% increments.
- **Mute**: Press <kbd>M</kbd> to instantly mute/unmute.
- **200% Software Boost**: Amplify quiet movie dialogues beyond 100% up to 200% without distortion.
""")

write("playback/seeking.md", """---
title: "Progress Bar, Fast Seeking & Precision"
description: "Master timeline navigation, multi-tier seeking, hover thumbnail previews, and keyframe-accurate positioning in Kyna Player."
order: 2
group: "Playback & Seeking"
---

# ⏳ Progress Bar, Fast Seeking & Precision

Smooth and precise timeline navigation is critical when watching long films or locating key moments. Kyna Player features multi-tiered seeking and background keyframe thumbnail rendering.

---

## 🎯 Timeline Navigation

### 1. Direct Click & Dragging
- **Click**: Click anywhere on the progress bar to instantly jump to that timestamp.
- **Drag**: Click and drag along the bar; a centered HUD overlay shows real-time target timestamps and frame previews.

### 2. Hover Thumbnail Previews
- Hovering over the timeline displays the timestamp (`hh:mm:ss`) alongside hardware-decoded keyframe thumbnails.

---

## ⏩ Multi-Tier Seeking Hotkeys

| Tier | Step Size | Hotkey | Recommended Use |
| :--- | :--- | :--- | :--- |
| **Short Seek** | **±5 s** | <kbd>→</kbd> / <kbd>←</kbd> | Catching missed dialogue lines |
| **Medium Seek** | **±30 s** | <kbd>Ctrl</kbd> + <kbd>→</kbd> / <kbd>←</kbd> | Skipping brief intros or silent scenes |
| **Long Seek** | **±60 s** | <kbd>Shift</kbd> + <kbd>→</kbd> / <kbd>←</kbd> | Skipping intro/outro songs (OP/ED) |
| **Percentage Seek** | **0% ~ 90%** | <kbd>0</kbd> ~ <kbd>9</kbd> | Press <kbd>5</kbd> to jump exactly to midpoint |

---

## 🔬 Keyframe Seeking vs Exact Frame Seeking

- **Fast Keyframe Seeking (Default)**: Jumps directly to the nearest I-Frame for instant, stutter-free navigation.
- **Exact Frame Seeking**: Reconstructs intermediate P/B frames from the nearest keyframe when single-stepping while paused.
""")

write("playback/fullscreen-mini-stats.md", """---
title: "Fullscreen, Mini-View & Performance Stats"
description: "Switch between fullscreen, compact mini-mode, always-on-top, and real-time performance statistics (F12)."
order: 3
group: "Playback & Seeking"
---

# 📺 Fullscreen, Mini-View & Performance Stats

Kyna Player adapts effortlessly to different viewing scenarios, whether you want an immersive 4K theater experience, a background picture-in-picture mini window, or real-time GPU diagnostics.

---

## 🖥️ 1. Fullscreen Mode

- **Toggle Hotkeys**: <kbd>Enter</kbd> / <kbd>F11</kbd> / <kbd>Alt</kbd> + <kbd>Enter</kbd>
- **Mouse Action**: Double-click anywhere on the video viewport.
- **Auto-Hide UI**: Controls fade out after 2 seconds of inactivity, leaving 100% pure video.

---

## 🪟 2. Compact Mini Mode & Always-on-Top

- **Always-on-Top Hotkey**: <kbd>Ctrl</kbd> + <kbd>T</kbd> (or click the pin icon in the title bar).
- Keep video visible in a corner while taking notes, coding, or chatting.

---

## 📊 3. Real-Time Diagnostics OSD (F12)

Press <kbd>F12</kbd> or <kbd>Shift</kbd> + <kbd>I</kbd> to toggle the live performance overlay:
- **Render FPS & Dropped Frames**: Immediate visibility into dropped frames (`0 dropped`).
- **Frame Time Budget**: Milliseconds spent per frame (e.g. `Decode: 2.1ms | Render: 4.8ms`).
- **Hardware Decoder**: Active GPU engine (e.g. `D3D11VA - NVIDIA NVDEC`).
""")

write("playback/modes.md", """---
title: "Repeat, Shuffle & Playback Modes"
description: "Master playlist playback strategies, including Sequential, Repeat All, Repeat One, Shuffle, and Auto-Play Next."
order: 4
group: "Playback & Seeking"
---

# 🔁 Repeat, Shuffle & Playback Modes

Kyna Player provides full control over playlist flow — whether binge-watching a series, looping a music video, or shuffling a music library.

---

## 🔀 Four Core Playback Modes

Click the repeat icon in the control bar or press <kbd>Ctrl</kbd> + <kbd>R</kbd> to cycle modes:

| Icon | Mode | Description | Ideal Use Case |
| :---: | :--- | :--- | :--- |
| 🔁 | **Repeat All** | Loops the entire playlist continuously. | Binge-watching series |
| 🔂 | **Repeat One** | Loops the current file indefinitely. | Tutorial videos, study loops |
| 🔀 | **Shuffle** | Plays tracks in randomized non-repeating order. | Music libraries, podcasts |
| ➡️ | **Sequential** | Plays from current item to end of list and stops. | Single movies, sleep timer |

---

## ⏭️ Previous & Next Navigation

- **Next Track**: Press <kbd>PageDown</kbd> or <kbd>N</kbd>.
- **Previous Track**: Press <kbd>PageUp</kbd> or <kbd>P</kbd>.

---

## 📺 Smart Auto-Play Next Episode

When importing multi-episode anime or TV series:
1. **Natural Sorting**: Episodes are sorted correctly (e.g., `EP01, EP02 ... EP10`).
2. **Seamless Preload**: Automatically pre-buffers the next episode near the end of the current file.
3. **Resume Memory**: Remembers last played position across all episodes.
""")

write("playback/timeline-thumbnails.md", """---
title: "Timeline Thumbnail Previews"
description: "Understand background thumbnail generation, caching, and precision preview seeking."
order: 5
group: "Playback & Seeking"
---

# 🖼️ Timeline Thumbnail Previews

Hovering over the progress bar during playback reveals real-time frame previews generated by our hardware-accelerated background decoding pipeline.

---

## ⚡ How It Works

1. **Background Keyframe Extraction**: Upon opening a local video, a background worker decodes I-frames into lightweight thumbnails.
2. **LRU Caching**: Thumbnails are cached in `%APPDATA%\\KynaPlayer\\thumbnails\\` for instant retrieval upon subsequent plays.
3. **Smooth Hover**: Hovering anywhere along the timeline instantly surfaces the nearest visual snapshot.
""")

# ==========================================
# 3. Video, HDR & Enhancement
# ==========================================

write("video/output-and-picture.md", """---
title: "Video Output & Picture Adjustments"
description: "Configure GPU hardware-accelerated renderers, aspect ratio scaling, color calibration, and HDR tone mapping."
order: 1
group: "Video, HDR & Enhancement"
---

# 🎨 Video Output & Picture Adjustments

Kyna Player features an advanced Direct3D hardware rendering pipeline, delivering peak GPU decode performance alongside flexible aspect ratios, color calibration, and wide color gamut HDR support.

---

## 🚀 Video Output & Hardware Acceleration

In **Settings → Video & Rendering**, choose the optimal rendering backend:

| Output Mode | Characteristics & Advantages | Target Hardware |
| :--- | :--- | :--- |
| **Direct3D 11 (D3D11)** *(Recommended)* | High compatibility and ultra-low latency; zero-copy GPU decode directly to display. | Windows 10/11 discrete & integrated GPUs |
| **Direct3D 12 (D3D12)** | Modern low-level rendering optimized for modern GPU compute pipelines. | RTX / RX series GPUs |
| **Software Decoding (CPU)** | High compatibility fallback for non-standard legacy codecs. | Failsafe fallback |

---

## 📐 Aspect Ratio & Scaling Modes

Press <kbd>A</kbd> or right-click → **Aspect Ratio**:
- **Keep Aspect Ratio (Fit)** *(Default)*: Preserves original proportions with letterboxing.
- **Stretch to Fill**: Stretches video to fill window completely.
- **Crop to Fill**: Zooms proportionally to eliminate black borders.
- **Fixed Presets**: `16:9`, `4:3`, `21:9` (UltraWide), `1:1`.

---

## 🎚️ Color Calibration & Image Controls

Real-time non-destructive controls in **Video Settings**:
- **Brightness & Contrast**: -50 to +50
- **Saturation & Hue**: -50 to +50
- **Gamma**: 0.5 to 2.0
- **One-Click Reset**: Restores default video color profile instantly.

---

## 🔄 Rotation & Mirror Flipping

- **Rotate 90° Clockwise**: <kbd>Alt</kbd> + <kbd>R</kbd>
- **Horizontal Mirror Flip**: <kbd>Alt</kbd> + <kbd>H</kbd> (Ideal for dance tutorials)
- **Vertical Flip**: <kbd>Alt</kbd> + <kbd>V</kbd>

---

## 🌈 HDR & Tone Mapping

When playing 4K HDR10, HLG, or Dolby Vision media:
- **HDR Passthrough**: Outputs native 10-bit BT.2020 signals to HDR displays.
- **SDR Tone Mapping**: Automatically compresses dynamic range using Reinhard / Mobius algorithms on standard SDR screens without washed-out highlights.
""")

write("video/anime4k.md", """---
title: "Anime4K Upscaling & 2× Enhancement"
description: "Enable real-time Anime4K image reconstruction for anime and cartoon content."
order: 3
group: "Video, HDR & Enhancement"
---

# ✨ Anime4K Upscaling & 2× Enhancement

Anime4K is a specialized real-time image enhancement pipeline designed for 2D animated content. It reconstructs sharp line art, refines flat textures, and upscales anime up to 4K resolution.

---

## 🚀 Enabling Anime4K

Open the sidebar **Video Enhance** drawer or press <kbd>Alt</kbd> + <kbd>V</kbd>:
- **Anime4K Mode A (Fast)**: Optimized for 1080p -> 4K upscaling on integrated or laptop GPUs.
- **Anime4K Mode B (HQ)**: High-precision line reconstruction for lower-resolution 720p anime.
- **Anime4K Mode C+A (Ultra)**: Dual-pass de-blur and edge sharpening for maximum fidelity.

---

## 🔀 Real-Time Comparison Views

- **Split Screen (Left/Right)**: Compares original low-res frames against enhanced results side-by-side.
- **Difference Heatmap**: Displays high-frequency reconstructed edges.

---

## ⏱️ Dynamic Performance Budget

If GPU frame calculation exceeds the 16.6ms budget (for 60 FPS video), the player dynamically falls back to lightweight shaders to prevent frame drops.
""")

write("video/comparison-performance.md", """---
title: "Enhancement Comparison & Performance Budget"
description: "Understand split-screen comparison views, quality lock, frame time budgets, and dynamic fallback mechanisms."
order: 4
group: "Video, HDR & Enhancement"
---

# 📊 Enhancement Comparison & Performance Budget

When utilizing **Anime4K**, **DLSS 5**, or custom compute shaders, Kyna Player provides built-in comparison tools and dynamic performance budgeting to ensure stutter-free playback.

---

## 🔀 Split-Screen Comparison Views

| Comparison View | Format | Purpose |
| :--- | :--- | :--- |
| **Side-by-Side** | Left: Original, Right: Enhanced (with draggable divider line). | Inspect line sharpening and noise reduction |
| **Top-Bottom** | Top: Original, Bottom: Enhanced. | Wide landscape scene verification |
| **Difference Map** | Isolated high-frequency reconstructed pixels on black background. | Detect over-sharpening or halo artifacts |

---

## ⏱️ Frame Time Budget & Diagnostics

For 60 FPS video, each frame must decode, enhance, and present within **16.6 milliseconds**:
- Press <kbd>F12</kbd> to inspect real-time frame time metrics (`Decode ms` + `Shader ms`).

---

## 🛡️ Dynamic Fallback Strategy

1. **Performance Priority (Default)**: Automatically scales back filter intensity if frame calculation exceeds time budget for 3 consecutive frames.
2. **Quality Locked**: Enforces full shader computation regardless of GPU load (recommended for discrete high-end GPUs).
""")

write("video/research-filters.md", """---
title: "Advanced Video Enhancement & Experimental Filters"
description: "Explore DLSS 5 neural super-resolution, CAS adaptive sharpening, Deband dithering, and custom shader pipelines."
order: 5
group: "Video, HDR & Enhancement"
---

# 🧪 Advanced Video Enhancement & Experimental Filters

In addition to Anime4K, Kyna Player integrates experimental neural upscaling and cinematic post-processing shaders for live-action films.

---

## ⚡ DLSS 5 Neural Super-Resolution

- **Auto Hardware Routing**: Detects discrete NVIDIA GPUs and initializes specialized tensor compute pipelines.
- **Compute Shader Universal Fallback**: Universal fallback implementation runs smoothly on AMD Radeon and Intel Arc architectures.
- **Temporal Anti-Aliasing**: Eliminates edge shimmering and high-frequency moiré patterns.

---

## 🔬 Post-Processing Shader Suite

| Filter | Algorithm | Problem Solved |
| :--- | :--- | :--- |
| **CAS** | Contrast Adaptive Sharpening | Enhances fine details without ringing or halo artifacts. |
| **Deband** | Gradient Dithering | Eliminates step-ladder color banding in sky and dark scenes. |
| **Bilateral** | Edge-Preserving Filter | Suppresses camera sensor noise while keeping facial hair and textures sharp. |
| **Film Grain** | Gaussian Noise Synthesizer | Adds authentic cinematic texture and masks compression artifacts. |

---

## 🎛️ Chaining & Intensity Controls

- **Filter Chaining**: Stack multiple filters in sequence (e.g. `Deband` → `CAS Sharpening`).
- **Intensity Sliders**: Fine-tune strength from `0.0` to `1.0`.
- **One-Click Bypass**: Hold down hotkey to instantly bypass all active shaders.
""")

# ==========================================
# 4. Subtitles & Dual Subtitle System
# ==========================================

write("subtitles/embedded-tracks.md", """---
title: "Embedded Tracks & Dual Subtitle System"
description: "Master embedded subtitle track switching, dual simultaneous subtitles, and preferred language auto-matching."
order: 1
group: "Subtitles"
---

# 💬 Embedded Tracks & Dual Subtitle System

Modern MKV and MP4 containers frequently bundle multi-language subtitle tracks. Kyna Player features a pioneering **Dual Subtitle System**, ideal for language learning and bilingual viewing.

---

## 📑 Track Selection & Switching

- **Subtitle Drawer**: Open via <kbd>Alt</kbd> + <kbd>S</kbd>.
- **Right-Click Menu**: Right-click viewport → **Subtitles** → **Subtitle Track**.
- **Cycle Hotkey**: Press <kbd>V</kbd> to cycle through all available tracks and "Off".

---

## 👥 Dual Subtitle System

Display primary and secondary subtitles simultaneously on screen:
- **Primary Subtitle**: Select target language (larger font size).
- **Secondary Subtitle**: Select original language (smaller font size, placed above/below).
- **Independent Layout**: Customize independent font sizes, vertical offsets, and colors to prevent overlapping.

---

## 🎯 Preferred Language Rules

In **Settings → Subtitle Preferences**:
- **Primary Language Code**: e.g. `en, eng`.
- **Secondary Language Code**: e.g. `zh, chi, ja, jpn`.
- New media automatically activates matching tracks without manual selection.

---

## 📦 Supported Subtitle Formats

| Format | Type | Rendering Support |
| :--- | :--- | :--- |
| **ASS / SSA** | Advanced styling, animations, and custom placement | Full libass hardware-accelerated rendering |
| **SRT** | Plain text standard | Full customizable typography |
| **VTT** | WebVTT streaming standard | Fully supported |
| **PGS / SUP** | Blu-ray bitmap graphics | Lossless bitmap composition |
""")

write("subtitles/external-files.md", """---
title: "External Subtitle Files & Auto-Matching"
description: "Load external SRT/ASS subtitle files, configure auto-loading rules, and synchronize timing."
order: 2
group: "Subtitles"
---

# 📂 External Subtitle Files & Auto-Matching

Easily load downloaded external subtitle files or let Kyna Player pair them automatically.

---

## 📥 Loading External Subtitles

1. **Drag & Drop**: Drag `.srt`, `.ass`, `.vtt`, or `.sub` files directly onto the video.
2. **Open Subtitle Dialog**: Press <kbd>Ctrl</kbd> + <kbd>L</kbd> to select files.
3. **Auto-Loading**: Automatically loads subtitle files matching `[VideoName].*.srt` in the same directory.
""")

write("subtitles/appearance.md", """---
title: "Subtitle Styling & Timing Delay"
description: "Customize subtitle fonts, sizes, colors, outlines, vertical positions, and millisecond timing offsets."
order: 3
group: "Subtitles"
---

# 🎨 Subtitle Styling & Timing Delay

Customize subtitle typography and correct audio/text timing desynchronization in real time.

---

## ✒️ Typography & Styling

Configure in **Settings → Subtitle Styling**:
- **Font Family**: Choose any installed system font (e.g. *Inter*, *Segoe UI*, *Roboto*).
- **Font Size**: Scale from `16px` to `96px` with 4K display auto-scaling.
- **High-Contrast Outline**: Add black stroke (`1px ~ 5px`) for readability on bright backgrounds.
- **Bounding Box**: Optional semi-transparent dark backdrop.
- **Vertical Offset**: Shift subtitles up or down to avoid covering hardcoded subtitles.

---

## ⏱️ Millisecond Sync Tuning

| Action | Hotkey | Description |
| :--- | :--- | :--- |
| **Subtitle Ahead 50ms** | <kbd>G</kbd> | Shift subtitle earlier (if dialogue appears before text) |
| **Subtitle Delay 50ms** | <kbd>H</kbd> | Shift subtitle later (if text appears before dialogue) |
| **Reset Delay** | <kbd>Ctrl</kbd> + <kbd>H</kbd> | Reset offset back to 0ms |

---

## 🎭 Override ASS Styling

- **Respect ASS Styles (Default)**: Renders all custom author fonts and animations.
- **Force Clean Typography**: Check **"Override ASS Styles"** in settings to standardize all subtitles into your custom clean typography.
""")

write("subtitles/online-search.md", """---
title: "Online Subtitle Search & Auto-Download"
description: "Search, hash-match, and download multi-language subtitles from OpenSubtitles and other databases."
order: 4
group: "Subtitles"
---

# 🌐 Online Subtitle Search & Download

Download and load matching subtitles in seconds without leaving Kyna Player.

---

## 🔍 Search & Download Flow

1. **Trigger Search**: Press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd> or click **"🌐 Search Online Subtitles"** in the subtitle drawer.
2. **Dual-Tier Matching**:
   - **Hash Matching**: Uses file checksum to match the exact encode release with 100% synced timing.
   - **Title Search**: Falls back to movie/episode title parsing (e.g. `S01E05`).
3. **One-Click Apply**: Click any result to download and mount the subtitle instantly.
""")

write("subtitles/troubleshooting.md", """---
title: "Subtitle Troubleshooting Guide"
description: "Fix garbled text encoding, time drift, missing font styles, and display issues."
order: 5
group: "Subtitles"
---

# 🛠️ Subtitle Troubleshooting Guide

Quick diagnostic solutions for common subtitle issues:

---

## ❓ Common Issues & Solutions

### 1. 🔤 Garbled or Missing Characters
- **Cause**: Subtitle file uses legacy `GBK`, `Big5`, or `Windows-1252` encoding instead of `UTF-8`.
- **Solution**: Open Subtitle Drawer and change **Text Encoding** dropdown to the corresponding character set.

### 2. ⏳ Progressive Desynchronization
- **Cause**: Frame rate mismatch between video (23.976 fps) and subtitle timing (25.0 fps PAL).
- **Solution**: Change **Subtitle Frame Rate** in Subtitle Settings or adjust timing with <kbd>G</kbd> / <kbd>H</kbd>.

### 3. 🎭 Missing Fonts in ASS Subtitles
- **Solution**: Install missing `.ttf` fonts in Windows or enable **"Fallback to Default Font"** in Subtitle Settings.
""")

# ==========================================
# 5. AI Subtitle Lab (Whisper & LLM)
# ==========================================

write("subtitle-ai/overview.md", """---
title: "AI Speech Transcription & Translation Overview"
description: "Explore Kyna Player's offline Whisper speech recognition and LLM-powered subtitle translation pipeline."
order: 1
group: "Subtitle AI & Translation"
---

# 🤖 AI Speech Transcription & Translation Overview

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
""")

write("subtitle-ai/transcription.md", """---
title: "Local Whisper Speech Transcription"
description: "Transcribe video audio into timestamped subtitles using local offline Whisper models."
order: 2
group: "Subtitle AI & Translation"
---

# 🎙️ Local Whisper Speech Transcription

Kyna Player embeds a high-performance **Whisper offline speech recognition engine**, generating accurate timestamped subtitles (`.srt` / `.vtt`) directly from audio tracks.

---

## 🛠️ Configuration Parameters

In sidebar **AI Lab → Speech Transcription**:
- **Source Language**: Auto-detect or specify source language code (`en`, `ja`, `ko`, `es`, etc.) for higher accuracy.
- **Audio Track Selection**: Target specific audio commentary or dub tracks.
- **Silero VAD**: Filters background noise, gunshots, and BGM to prevent AI hallucinations.

---

## 🧠 Model Sizes & Hardware Requirements

| Model | Parameters | VRAM | RTX 4060 Speed | Accuracy | Recommended Use |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tiny** | 39 M | ~0.8 GB | ~30x Speed | Good | Quick summaries, low-end PCs |
| **Base** | 74 M | ~1.0 GB | ~20x Speed | Very Good | Daily English/Chinese videos |
| **Small** | 244 M | ~1.8 GB | ~12x Speed | Excellent *(Recommended)* | General movies & anime series |
| **Medium** | 769 M | ~3.5 GB | ~6x Speed | High | Complex dialects & lectures |
| **Large-v3** | 1550 M | ~6.0 GB | ~3x Speed | State-of-the-Art | Noisy backgrounds, max accuracy |
""")

write("subtitle-ai/translation.md", """---
title: "LLM & Multi-Engine Subtitle Translation"
description: "Translate subtitles with natural nuance using DeepSeek, OpenAI, Claude, or local Ollama models."
order: 3
group: "Subtitle AI & Translation"
---

# 🌐 LLM & Multi-Engine Subtitle Translation

Unlike traditional word-by-word machine translation, Kyna Player uses **sliding context windows** to provide LLMs with preceding and subsequent dialogue lines for natural, idiom-aware translations.

---

## 🔌 Supported Translation Engines

| Engine | Models | Features |
| :--- | :--- | :--- |
| **DeepSeek** *(Recommended)* | `deepseek-chat`, `deepseek-reasoner` | Exceptional value, localized phrasing |
| **OpenAI** | `gpt-4o`, `gpt-4o-mini` | Strong multi-language reasoning |
| **Anthropic Claude** | `claude-3-5-sonnet` | Natural literary flair & dialogue flow |
| **Ollama (Local)** | `qwen2.5`, `llama3.1`, `gemma2` | 100% offline, free, private |
| **Custom Endpoint** | Any OpenAI-compatible API | Reverse proxies and enterprise gateways |

---

## 💬 Bilingual Layout Options

- **Bilingual Top/Bottom**: Target translation on top, original speech on bottom.
- **Target Translation Only**: Clean single-language experience.
- **Export Standards**: Export directly as `.srt` or `.ass` subtitle files.
""")

write("subtitle-ai/models.md", """---
title: "AI Model Management & Hardware Acceleration"
description: "Manage offline Whisper model weights, configure GPU compute backends, and optimize VRAM usage."
order: 4
group: "Subtitle AI & Translation"
---

# 📦 AI Model Management & Hardware Acceleration

Manage on-device model weights and select compute backends in **Settings → AI Models**.

---

## 📥 Model Storage & Downloads

- **One-Click Download**: Download Whisper models directly within Kyna Player with automatic SHA-256 verification.
- **Storage Path**: `%APPDATA%\\KynaPlayer\\models\\`.
- **Manual Import**: Place standard `ggml-*.bin` weights into the models directory for air-gapped offline use.

---

## ⚡ Hardware Acceleration Backends

| Backend | Hardware | Acceleration Ratio |
| :--- | :--- | :--- |
| **NVIDIA CUDA** *(Recommended)* | GeForce / RTX GPUs | 🚀 Ultra (~20x-30x) |
| **DirectML** | AMD Radeon / Intel Arc / APUs | ⚡ High (~8x-15x) |
| **Vulkan Compute** | Cross-platform GPUs | ⚡ Medium (~8x-12x) |
| **CPU AVX2 / OpenVINO** | Modern multi-core CPUs | 🔄 Standard (~2x-4x) |

---

## 🧹 Smart VRAM Scheduling

- **Lazy Loading**: Models load into VRAM only when transcription starts.
- **Auto-Unload**: Unloads models after 5 minutes of idle time, freeing 100% VRAM for games or 4K rendering.
""")

write("subtitle-ai/results.md", """---
title: "Subtitle Results Editing, Export & Mounting"
description: "Preview AI-generated subtitles, adjust timing timestamps inline, and export to SRT/ASS formats."
order: 5
group: "Subtitle AI & Translation"
---

# 📝 Subtitle Results Editing, Export & Mounting

Review, edit, and export AI-generated subtitles with Kyna Player's built-in subtitle editor.

---

## 🔍 Interactive Timeline Navigation

- **Click to Seek**: Click any subtitle row in the AI results drawer to jump straight to that timestamp.
- **Active Line Highlight**: Automatically highlights the current spoken dialogue line as playback advances.

---

## ✏️ Inline Editing & Timing Adjustments

- **Edit Text**: Double-click any line to edit text; press <kbd>Enter</kbd> to save.
- **Timestamp Fine-Tuning**: Adjust start/end millisecond values or click "Sync with Current Playhead".
- **Split & Merge**: Split long sentences or merge adjacent lines with one click.

---

## 💾 Export Formats

- **SRT (.srt)**: Universal format compatible with all TVs, players, and cloud drives.
- **ASS (.ass)**: Rich formatting preserving bilingual vertical stacking and custom colors.
- **Plain Text (.txt)**: Meeting transcripts and article summaries.
""")

# ==========================================
# 6. Audio, Screenshots & Casting
# ==========================================

write("audio-and-tools/audio.md", """---
title: "Audio Tracks, Output Devices & Sync"
description: "Manage audio track switching, output device routing, multi-channel downmixing, and audio delay synchronization."
order: 1
group: "Audio, Screenshots & Casting"
---

# 🔊 Audio Tracks, Output Devices & Sync

Kyna Player features a high-fidelity audio pipeline with surround sound passthrough, multi-track selection, and millisecond sync compensation.

---

## 🎧 Audio Tracks Selection

- **Cycle Hotkey**: Press <kbd>A</kbd> or <kbd>Ctrl</kbd> + <kbd>A</kbd> to cycle audio tracks.
- **Detailed Metadata**: Displays track language, channel layout (`5.1`, `7.1`, `Stereo`), and codec (`DTS-HD MA`, `TrueHD Atmos`, `FLAC`, `AAC`).

---

## 🎛️ Audio Output Routing & Downmixing

- **Independent Output Device**: Route player audio exclusively to headphones or USB DAC without affecting system sound.
- **HRTF Spatial Downmix**: Downmixes 5.1/7.1 surround sound to stereo headphones while preserving crisp center-channel dialogue.
- **Bitstream Passthrough**: Passthrough raw Dolby/DTS bitstreams via S/PDIF or HDMI to AV receivers.

---

## ⏱️ Audio Delay Sync

| Action | Hotkey | Description |
| :--- | :--- | :--- |
| **Audio Delay +100ms** | <kbd>Ctrl</kbd> + <kbd>]</kbd> | Delay audio (if sound precedes video) |
| **Audio Advance -100ms** | <kbd>Ctrl</kbd> + <kbd>[</kbd> | Advance audio (if video precedes sound) |
| **Reset Delay** | <kbd>Ctrl</kbd> + <kbd>\\</kbd> | Reset audio offset to 0ms |
""")

write("audio-and-tools/audio-enhancement.md", """---
title: "Night Mode, Voice Boost & Audio Visualizer"
description: "Master Dynamic Range Compression (Night Mode), dialogue clarity boost, 10-band equalizer, and live audio spectrums."
order: 2
group: "Audio, Screenshots & Casting"
---

# 🎚️ Night Mode, Voice Boost & Audio Visualizer

Kyna Player's DSP suite tackles the classic movie issue of quiet dialogues and deafening action explosions.

---

## 🌙 Night Mode & Dynamic Range Compression (DRC)

- **DRC Compression**: Tames loud explosions while boosting whisper-quiet dialogue, maintaining an even volume level throughout movies without disturbing others late at night.

---

## 🗣️ Voice Clarity Boost

- **Mid-Frequency Vocal Boost**: Selectively amplifies human vocal ranges (300Hz ~ 3.5kHz) and cleans up muddy background rumble.

---

## 🎛️ 10-Band Graphic Equalizer

- **Presets**: *Pop*, *Rock*, *Bass Boost*, *Vocal*, *EDM*.
- **Custom Sliders**: Tune ±12dB across `31Hz` to `16kHz`.

---

## 📊 Live Audio Spectrum & Waveform

- **Dynamic Bar Spectrum**: Neon rhythm bars reacting in real-time to music playback.
- **Smooth Waveform**: Oscilloscope-style visualization with near-zero CPU usage.
""")

write("audio-and-tools/screenshots.md", """---
title: "High-Resolution Screenshots & Output Management"
description: "Capture native resolution stills, choose between with/without subtitles, and customize file naming templates."
order: 3
group: "Audio, Screenshots & Casting"
---

# 📸 High-Resolution Screenshots & Management

Capture crisp, uncompressed movie stills and wallpapers instantly.

---

## ⚡ Capture Modes & Hotkeys

| Action | Hotkey | Description |
| :--- | :--- | :--- |
| **Native Clean Still** *(Recommended)* | <kbd>Ctrl</kbd> + <kbd>S</kbd> / <kbd>F5</kbd> | Captures pure video frame **without subtitles** at native resolution. |
| **Capture with Subtitles** | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>S</kbd> | Captures video frame together with visible subtitle overlays. |
| **Copy to Clipboard** | <kbd>Ctrl</kbd> + <kbd>C</kbd> | Copies screenshot directly to clipboard for quick pasting. |

---

## 📂 Formats & Naming Templates

- **Image Formats**: Lossless PNG, high-quality JPEG, or WebP.
- **Naming Pattern**: `{title}_{time}_{index}.png` (e.g. `Inception_01-24-36_001.png`).
- **Save Location**: Default to `%USERPROFILE%\\Pictures\\KynaPlayer\\`. Click the toast notification to open the folder directly.
""")

write("audio-and-tools/media-information.md", """---
title: "Media Properties, Codecs & Diagnostics"
description: "Inspect container formats, video codecs, color primaries, HDR metadata, and live playback statistics."
order: 4
group: "Audio, Screenshots & Casting"
---

# ℹ️ Media Properties & Diagnostics

Inspect detailed container metadata and live hardware decoding status.

---

## 🔍 Opening Media Info

- **Hotkey**: <kbd>Ctrl</kbd> + <kbd>I</kbd> or <kbd>Shift</kbd> + <kbd>I</kbd>.
- **Menu**: Right-click → **Tools** → **Media Info**.

---

## 📊 Full Spectrum Diagnostics

- **Container Info**: Format (`.mkv`, `.mp4`), size, bitrate.
- **Video Stream**: Codec (`HEVC`, `AV1`, `H.264`), resolution (`3840x2160`), FPS, color space (`BT.2020 10-bit`), HDR standard (`HDR10`, `Dolby Vision`).
- **Audio & Subtitle Streams**: Channel layout, sample rate, language tags.
- **Live Pipeline Stats**: Active hardware decoder (`D3D11VA - NVIDIA NVDEC`), real-time bitrate graph, and frame drop counter.
""")

write("audio-and-tools/dlna.md", """---
title: "DLNA Wireless Casting & Remote Control"
description: "Wirelessly cast local media to smart TVs, projectors, and streaming boxes over DLNA / UPnP."
order: 5
group: "Audio, Screenshots & Casting"
---

# 📺 DLNA Wireless Casting

Cast local 4K movies and series directly to living room smart TVs, Apple TV, or projectors over your local Wi-Fi network.

---

## 📡 Quick Casting Guide

1. **Discover Devices**: Open sidebar **Tools → DLNA Casting** or click the `📺 Cast` icon in the control bar.
2. **Connect & Cast**: Select your TV (e.g. `Living Room TV`) to start big-screen playback.
3. **Synchronized Remote**: Seek, pause, and adjust volume on your PC; the TV follows in real-time.

---

## 🛠️ Requirements & Troubleshooting

- **Same Local Network**: Ensure PC and TV connect to the same router / subnet (5GHz Wi-Fi recommended).
- **Windows Firewall**: Allow Kyna Player access through Windows Firewall when prompted.
""")

# ==========================================
# 7. Playlist & Media Management
# ==========================================

write("playlist/overview.md", """---
title: "Playlist Overview"
description: "Learn how Kyna Player manages playback queues, recent media history, and natural sorting."
order: 1
group: "Playlist & Media Management"
---

# 📑 Playlist Overview

Kyna Player's playlist system handles large video queues, episode binge-watching, and music library playback smoothly.

---

## 🚪 Accessing the Playlist

- **Hotkey**: <kbd>F3</kbd> or <kbd>Alt</kbd> + <kbd>P</kbd>.
- **Dock Button**: Click the `📑 Playlist` icon in the bottom right control dock.

---

## ⚡ Core Features

- **Multi-File Drag & Drop**: Drag entire folders or multiple files directly into the list.
- **Drag-to-Reorder**: Reorder items by dragging and dropping within the list.
- **Recent History**: Keep track of playback progress and resume points.
- **M3U8 Support**: Import and export universal UTF-8 playlist files.
""")

write("playlist/create-save-load.md", """---
title: "Creating, Saving & Loading Playlists"
description: "Create custom media queues, export M3U/M3U8 playlists, and migrate lists across devices."
order: 2
group: "Playlist & Media Management"
---

# 📑 Creating, Saving & Loading Playlists

Manage and persist your media collections using universal playlist formats.

---

## ➕ Creating & Managing Queues

1. **New Queue**: Click `➕ New` in the playlist header to start a fresh list.
2. **Add Files**: Click "Add Files" or drag media directly from Windows Explorer.
3. **Reorder Items**: Drag items up or down to set custom playback sequences.

---

## 💾 Saving & Exporting (M3U8)

- **Save Playlist**: Click **"💾 Save / Export"**.
- **M3U8 (UTF-8)** *(Recommended)*: Preserves multi-language titles and special characters without encoding corruption.
- **Relative Paths**: Uses relative file paths so playlists remain functional when moved to external hard drives.
""")

write("playlist/import-folder.md", """---
title: "Importing Folders & Batch Addition"
description: "Batch import entire TV seasons and music albums with recursive directory scanning and automatic file filtering."
order: 3
group: "Playlist & Media Management"
---

# 📁 Importing Folders & Batch Addition

Import entire anime seasons or music discographies in a single action.

---

## 🚀 Import Methods

1. **Drag & Drop**: Drag one or multiple folders directly into the player window.
2. **Menu Import**: Select **File → Open Folder...** (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>O</kbd>).

---

## 🔍 Recursive Scanning & Filtering

- **Media Filtering**: Automatically imports supported video and audio files while ignoring images, `.nfo`, `.torrent`, and log files.
- **Recursive Scanning**: Scans nested subdirectories (e.g. `Season 1/`, `Season 2/`).
- **Auto Subtitle Pairing**: Automatically pairs matching `.srt` / `.ass` subtitle files found in the same directory.
""")

write("playlist/search-sort.md", """---
title: "Search, Natural Sorting & Clean Titles"
description: "Filter long playlists in real time, sort naturally by episode number, and clean up release group tags."
order: 4
group: "Playlist & Media Management"
---

# 🔍 Search, Natural Sorting & Clean Titles

Effortlessly organize hundreds of files and maintain correct chronological playback order.

---

## ⚡ Instant Search & Filtering

- Type any keyword in the search bar to filter entries in real time.
- Press <kbd>Esc</kbd> to clear search and restore full queue.

---

## 🔢 Natural Order Sorting

Eliminates the common `1, 10, 2` ASCII ordering issue:
- Correct Natural Sorting: `Episode 1` → `Episode 2` → `Episode 10`.
- Sort by Filename, Date Modified, File Size, or Shuffle.

---

## ✨ Clean Title Formatting

Toggle **"Clean Title"** to automatically strip release group tags (e.g. `[1080p][x265][AAC]`), presenting clean, readable episode titles.
""")

write("playlist/recent-and-files.md", """---
title: "Recent History & File Operations"
description: "Review watch history, resume playback from bookmarks, locate files in Explorer, and delete media safely."
order: 5
group: "Playlist & Media Management"
---

# 🕒 Recent History & File Operations

Track viewing history and manage local files directly from the player.

---

## 📜 Recent Play History

- **Resume Bookmarks**: Shows exact playback timestamp (e.g. `Resumed at 45:12 (68%)`).
- **One-Click Resume**: Double-click any item to continue watching right where you left off.
- **Privacy Clear**: Click "Clear History" to wipe all playback records instantly.

---

## 🗂️ Context Menu File Actions

Right-click any playlist item:
- **Show in Explorer**: <kbd>Ctrl</kbd> + <kbd>E</kbd>
- **Remove from Playlist**: <kbd>Delete</kbd> (Keeps physical file on disk)
- **Send to Recycle Bin**: <kbd>Shift</kbd> + <kbd>Delete</kbd> (Deletes physical file to Windows Recycle Bin)
- **Copy File Path**: <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd>
""")

# ==========================================
# 8. Settings & Troubleshooting
# ==========================================

write("settings/overview.md", """---
title: "Settings Center Overview"
description: "Comprehensive overview of Kyna Player's preferences, including General, Playback, Video, Audio, Subtitles, AI, Hotkeys, and File Associations."
order: 1
group: "Settings & Troubleshooting"
---

# ⚙️ Settings Center Overview

Customize every aspect of Kyna Player to match your hardware configuration and viewing preferences.

---

## 🚪 Opening Settings

- **Hotkey**: <kbd>F2</kbd> or <kbd>Ctrl</kbd> + <kbd>,</kbd>.
- **Access**: Click the `⚙️ Settings` button in the control dock or select **Preferences** from the context menu.

---

## 📑 Settings Categories

- 🏠 **General**: UI language, single-instance mode, AppData folder access.
- ⏯️ **Playback**: Default speed, auto-play next, seek step sizes.
- 📺 **Video & Rendering**: Direct3D 11/12 GPU acceleration, HDR tone mapping, Anime4K presets.
- 🔊 **Audio**: Output device routing, multi-channel downmixing, Dynamic Range Compression.
- 💬 **Subtitles**: Preferred languages, fonts, outline stroke, online subtitle providers.
- 🤖 **AI Lab**: Whisper models, LLM API keys, VRAM auto-unload rules.
- ⌨️ **Hotkeys**: Custom keyboard and mouse gesture bindings.
- 🔗 **File Associations**: Register default video player extensions and Windows context menu entries.
""")

write("settings/file-associations.md", """---
title: "File Associations & Windows Integration"
description: "Set Kyna Player as default player in Windows and manage file extensions."
order: 2
group: "Settings & Troubleshooting"
---

# 🔗 File Associations & Windows Integration

Associate video and audio extensions with Kyna Player for seamless double-click playback.

---

## ⚡ One-Click Association

In **Settings → File Associations**:
- Click **"Associate All Video Formats"** to register MP4, MKV, AVI, MOV, TS, WEBM, and more.
- Shows up as **"Kyna Player"** in the Windows "Open with" context menu.
""")

write("settings/app-data-and-logs.md", """---
title: "App Data, Cache & Log Management"
description: "Locate configuration files, thumbnail caches, AI model directories, and diagnostic logs."
order: 3
group: "Settings & Troubleshooting"
---

# 🗄️ App Data, Cache & Log Management

Kyna Player organizes all user preferences, caches, and logs cleanly in the standard Windows user directory.

---

## 📂 AppData Directory Location

```plaintext
%APPDATA%\\KynaPlayer\\
(Absolute path: C:\\Users\\<Username>\\AppData\\Roaming\\KynaPlayer\\)
```

> [!TIP]
> Click **"📂 Open AppData Directory"** in **Settings → General** to open the folder directly.

---

## 🌲 Directory Structure

```plaintext
AppData\\Roaming\\KynaPlayer\\
├── 📄 config.json           # Preferences, keybindings & custom settings
├── 📄 history.json          # Playback history and resume timestamps
├── 📁 thumbnails\\           # Cached timeline preview thumbnails
├── 📁 subtitles\\            # Downloaded online subtitles
├── 📁 models\\               # Local Whisper speech recognition models
└── 📁 logs\\                 # Diagnostic logs (kyna_player.log)
```

---

## 🧹 Cache Cleaning & Reset

- **Clear Cache**: Click "Clear Temporary Cache" in General settings to reclaim disk space.
- **Factory Reset**: Delete `config.json` while the player is closed to restore all factory defaults.
""")

write("settings/performance-troubleshooting.md", """---
title: "Performance Tuning & Hardware Troubleshooting"
description: "Resolve dropped frames, black/green screens, audio desync, and HDR color issues."
order: 4
group: "Settings & Troubleshooting"
---

# 🚀 Performance Tuning & Hardware Troubleshooting

Quick diagnostic steps for resolving playback anomalies:

---

## 🛠️ Common Issues & Fixes

### 1. 📺 4K/8K Dropped Frames or Stutter
- **GPU Scheduling (Dual-GPU Laptops)**: In Windows Settings → Display → Graphics, assign `Kyna Player` to **"High Performance (Discrete GPU)"**.
- **Hardware Acceleration**: Ensure **"Direct3D 11 (D3D11VA)"** is active in Video Settings.
- **Shader Load**: Switch Anime4K to *Mode Fast* or temporarily disable heavy post-processing.

### 2. 🟢 Black or Green Screen with Normal Audio
- **Fix**: Right-click viewport → **Video** → Switch to **"Software Decoding (CPU)"**, then update GPU drivers to the latest WHQL release.

### 3. 🌈 Washed-Out HDR Colors on SDR Screens
- **Fix**: Enable **"SDR Tone Mapping"** in Video Settings and select `Reinhard` or `Mobius` tone mapping.
""")

write("settings/feedback.md", """---
title: "Feedback & Submitting Diagnostics"
description: "Export diagnostic logs, report bugs on GitHub, and suggest new features."
order: 5
group: "Settings & Troubleshooting"
---

# 💬 Feedback & Submitting Diagnostics

Encountered an issue or have a feature idea? We welcome your feedback!

---

## 📮 Official Support Channels

- **GitHub Issues**: [GitHub Repository](https://github.com/fynx-dev/kyna-release/issues) *(Recommended for bug reports & feature requests)*
- **Community Forum**: Discuss playback tips and custom shader configurations.

---

## 📋 Reporting a Bug

Please include the following in your bug report:
1. **App Version**: e.g. `Kyna Player v0.1.0 (x64)`
2. **OS & GPU**: Windows 11 23H2 / RTX 4070 (Driver: 560.xx)
3. **Reproduction Steps**: Step-by-step description of how the bug occurs.
4. **Attachments**: Media properties text (<kbd>Ctrl</kbd> + <kbd>I</kbd>) and `kyna_player.log`.

> [!NOTE]
> **🔒 Privacy Assurance**: Logs contain only codec metrics and shader compile logs. **No personal data or video frames are ever recorded or uploaded.**
""")

print("All 39 English (en) docs generated successfully!")
