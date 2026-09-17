---
title: "Subtitle Styling & Sync"
description: "Customize subtitle fonts, sizes, colors, outlines, vertical positions, and millisecond timing offsets."
order: 3
group: "Subtitles"
---

# Subtitle Styling & Sync

Customize subtitle typography and correct audio/text timing desynchronization in real time.

---

## ✒️ Typography & Styling

Configure in **Settings → Subtitle Styling**:
- **Font Family**
  Choose any installed system font (e.g. *Inter*, *Segoe UI*, *Roboto*).
- **Font Size**
  Scale from `16px` to `96px` with 4K display auto-scaling.
- **High-Contrast Outline**
  Add black stroke (`1px ~ 5px`) for readability on bright backgrounds.
- **Bounding Box**
  Optional semi-transparent dark backdrop.
- **Vertical Offset**
  Shift subtitles up or down to avoid covering hardcoded subtitles.

---

## ⏱️ Millisecond Sync Tuning

| Action | Hotkey | Description |
| :--- | :--- | :--- |
| **Subtitle Ahead 50ms** | <kbd>G</kbd> | Shift subtitle earlier (if dialogue appears before text) |
| **Subtitle Delay 50ms** | <kbd>H</kbd> | Shift subtitle later (if text appears before dialogue) |
| **Reset Delay** | <kbd>Ctrl</kbd> + <kbd>H</kbd> | Reset offset back to 0ms |

---

## 🎭 Override ASS Styling

- **Respect ASS Styles (Default)**
  Renders all custom author fonts and animations.
- **Force Clean Typography**
  Check **"Override ASS Styles"** in settings to standardize all subtitles into your custom clean typography.
