---
title: "Interface Overview"
description: "Comprehensive guide to Kyna Player's UI layout, control dock, slide-out sidebar, and gesture areas."
order: 2
group: "Getting Started & Interface"
---

# Interface Overview

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
- **📌 Always-on-Top**
  Pin the player above all other windows.
- **🎬 Media Title**
  Displays the current video/audio file name.
- **⚙️ Window Controls**
  Minimize, Maximize / Restore, and Close.

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
- **Interactive Timeline**
  Hover over the progress bar to preview keyframe thumbnails.
- **Playback Controls**
  Previous / Next (<kbd>PageUp</kbd>/<kbd>PageDown</kbd>), Play / Pause (<kbd>Space</kbd>), Stop (<kbd>S</kbd>), and Frame Step (<kbd>.</kbd>).
- **Volume & Boost**
  Smooth slider supporting up to 200% software volume gain.
- **Speed & Modes**
  Quick presets for 0.5x ~ 2.0x speeds and repeat modes (Loop, Single, Shuffle, Sequential).

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
