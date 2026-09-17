---
title: "Tracks & Dual Subs"
description: "Master embedded subtitle track switching, dual simultaneous subtitles, and preferred language auto-matching."
order: 1
group: "Subtitles"
---

# Tracks & Dual Subs

Modern MKV and MP4 containers frequently bundle multi-language subtitle tracks. Kyna Player features a pioneering **Dual Subtitle System**, ideal for language learning and bilingual viewing.

---

## 📑 Track Selection & Switching

- **Subtitle Drawer**
  Open via <kbd>Alt</kbd> + <kbd>S</kbd>.
- **Right-Click Menu**
  Right-click viewport → **Subtitles** → **Subtitle Track**.
- **Cycle Hotkey**
  Press <kbd>V</kbd> to cycle through all available tracks and "Off".

---

## 👥 Dual Subtitle System

Display primary and secondary subtitles simultaneously on screen:
- **Primary Subtitle**
  Select target language (larger font size).
- **Secondary Subtitle**
  Select original language (smaller font size, placed above/below).
- **Independent Layout**
  Customize independent font sizes, vertical offsets, and colors to prevent overlapping.

---

## 🎯 Preferred Language Rules

In **Settings → Subtitle Preferences**:
- **Primary Language Code**
  e.g. `en, eng`.
- **Secondary Language Code**
  e.g. `zh, chi, ja, jpn`.
- New media automatically activates matching tracks without manual selection.

---

## 📦 Supported Subtitle Formats

| Format | Type | Rendering Support |
| :--- | :--- | :--- |
| **ASS / SSA** | Advanced styling, animations, and custom placement | Full libass hardware-accelerated rendering |
| **SRT** | Plain text standard | Full customizable typography |
| **VTT** | WebVTT streaming standard | Fully supported |
| **PGS / SUP** | Blu-ray bitmap graphics | Lossless bitmap composition |
