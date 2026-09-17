---
title: "Seeking & Precision"
description: "Master timeline navigation, multi-tier seeking, hover thumbnail previews, and keyframe-accurate positioning in Kyna Player."
order: 2
group: "Playback & Seeking"
---

# Seeking & Precision

Smooth and precise timeline navigation is critical when watching long films or locating key moments. Kyna Player features multi-tiered seeking and background keyframe thumbnail rendering.

---

## 🎯 Timeline Navigation

### 1. Direct Click & Dragging
- **Click**
  Click anywhere on the progress bar to instantly jump to that timestamp.
- **Drag**
  Click and drag along the bar; a centered HUD overlay shows real-time target timestamps and frame previews.

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

- **Fast Keyframe Seeking (Default)**
  Jumps directly to the nearest I-Frame for instant, stutter-free navigation.
- **Exact Frame Seeking**
  Reconstructs intermediate P/B frames from the nearest keyframe when single-stepping while paused.
