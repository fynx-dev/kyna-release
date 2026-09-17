---
title: "App Data & Logs"
description: "Locate configuration files, thumbnail caches, AI model directories, and diagnostic logs."
order: 3
group: "Settings & Troubleshooting"
---

# App Data & Logs

Kyna Player organizes all user preferences, caches, and logs cleanly in the standard Windows user directory.

---

## 📂 AppData Directory Location

```plaintext
%APPDATA%\KynaPlayer\
(Absolute path: C:\Users\<Username>\AppData\Roaming\KynaPlayer\)
```

> [!TIP]
> Click **"📂 Open AppData Directory"** in **Settings → General** to open the folder directly.

---

## 🌲 Directory Structure

```plaintext
AppData\Roaming\KynaPlayer\
├── 📄 config.json           # Preferences, keybindings & custom settings
├── 📄 history.json          # Playback history and resume timestamps
├── 📁 thumbnails\           # Cached timeline preview thumbnails
├── 📁 subtitles\            # Downloaded online subtitles
├── 📁 models\               # Local Whisper speech recognition models
└── 📁 logs\                 # Diagnostic logs (kyna_player.log)
```

---

## 🧹 Cache Cleaning & Reset

- **Clear Cache**
  Click "Clear Temporary Cache" in General settings to reclaim disk space.
- **Factory Reset**
  Delete `config.json` while the player is closed to restore all factory defaults.
