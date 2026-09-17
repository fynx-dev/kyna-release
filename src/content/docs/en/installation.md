---
title: "Installation"
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
   Get-FileHash .\Kyna-Setup.exe -Algorithm SHA256
   ```
   Confirm the calculated hash strictly matches the published checksum.
3. Launch `Kyna-Setup.exe`, select your desired destination folder, and complete the installation wizard.
4. Launch Kyna Player via the Start Menu or Desktop shortcut.

## First-Run Tips

- **Hardware Decoding & Tone Mapping**
  On first launch, Kyna Player automatically probes GPU capabilities and enables Direct3D 11 hardware decoding along with HDR-to-SDR tone mapping.
- **Whisper AI Models**
  The main installer does not bundle heavy model weights. Download or import models on-demand via the "Subtitles -> Local AI" panel.

## Updates & Uninstallation

- **Updating**
  Close any running instances of Kyna Player and run the latest `Kyna-Setup.exe` to upgrade in-place. Your custom preferences, hotkeys, and AI models will be preserved.
- **Uninstallation**
  Uninstall cleanly via Windows "Settings -> Installed Apps" or the Start Menu shortcut.
