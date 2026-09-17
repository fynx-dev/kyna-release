---
title: "Subtitle Troubleshooting"
description: "Fix garbled text encoding, time drift, missing font styles, and display issues."
order: 5
group: "Subtitles"
---

# Subtitle Troubleshooting

Quick diagnostic solutions for common subtitle issues:

---

## ❓ Common Issues & Solutions

### 1. 🔤 Garbled or Missing Characters
- **Cause**
  Subtitle file uses legacy `GBK`, `Big5`, or `Windows-1252` encoding instead of `UTF-8`.
- **Solution**
  Open Subtitle Drawer and change **Text Encoding** dropdown to the corresponding character set.

### 2. ⏳ Progressive Desynchronization
- **Cause**
  Frame rate mismatch between video (23.976 fps) and subtitle timing (25.0 fps PAL).
- **Solution**
  Change **Subtitle Frame Rate** in Subtitle Settings or adjust timing with <kbd>G</kbd> / <kbd>H</kbd>.

### 3. 🎭 Missing Fonts in ASS Subtitles
- **Solution**
  Install missing `.ttf` fonts in Windows or enable **"Fallback to Default Font"** in Subtitle Settings.
