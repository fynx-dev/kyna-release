---
title: "Installation & Requirements"
description: "System requirements, installation, updates, and app data directory management."
order: 2
group: "Getting Started"
---

# 📦 Installation & System Requirements

## 💻 System Requirements

| Specification | Minimum | Recommended |
| :--- | :--- | :--- |
| **Operating System** | Windows 10 (64-bit) 1909+ | Windows 11 (22H2+) |
| **Processor (CPU)** | Intel Core i3 / AMD Ryzen 3 | Intel Core i5 / AMD Ryzen 5 or higher |
| **Graphics (GPU)** | Direct3D 11 hardware decoding | DX12 / HEVC / AV1 / VP9 hardware acceleration |
| **Memory (RAM)** | 4 GB | 8 GB or higher |

---

## 🚀 Installation & Updating

1. **Download Installer**
   Visit [GitHub Releases](https://github.com/fynx-dev/kyna-release/releases/latest) to download `Kyna-Setup.exe`.
2. **Run Setup Wizard**
   Launch the setup program and follow the on-screen steps to install.
3. **Upgrading**
   Close the player and run the latest installer directly to overwrite. Your custom settings and downloaded AI models will be preserved.

---

## 🗄️ App Data & Cache Directory

User configurations and caches are securely stored in the standard AppData folder:
- **Directory Path**: `%APPDATA%\KynaPlayer\` (accessible with one click in **Settings → General**).
- **Structure**:
  - `config.json`: Preferences, configurations, and custom keybindings.
  - `history.json`: Playback history and resume positions.
  - `thumbnails\`: Cached timeline hover thumbnail previews.
  - `models\`: Local offline Whisper AI models.
