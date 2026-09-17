---
title: "Installation & System Requirements"
description: "System requirements, checksum verification, installation, updating, and uninstallation guide for Kyna Player on Windows."
order: 2
group: "Getting Started"
---

## System Requirements

| Component | Minimum | Recommended |
| :--- | :--- | :--- |
| **OS** | Windows 10 (64-bit) 1909+ | Windows 11 (22H2+) |
| **CPU** | Intel Core i3 / AMD Ryzen 3 | Intel Core i5 / AMD Ryzen 5 or higher |
| **GPU** | DX11 Hardware Decoding | DX12 / HEVC / AV1 / VP9 HW Decoding |
| **RAM** | 4 GB | 8 GB or higher |

## Installation Steps

1. Visit [GitHub Releases](https://github.com/fynx-dev/kyna-release/releases/latest) to download the latest installer `Kyna-Setup.exe` and `SHA256SUMS`.
2. (Optional) Run PowerShell to verify installer hash integrity:
   ```powershell
   Get-FileHash .\Kyna-Setup.exe -Algorithm SHA256
   ```
   Ensure the output matches `SHA256SUMS`.
3. Double click `Kyna-Setup.exe` and follow setup wizard instructions.
4. Launch Kyna Player from Start Menu or installation folder.

## First Time Configuration

- **Hardware Decoding**: Hardware Tone Mapping for Dolby Vision & HDR 10-bit to SDR is enabled by default.
- **Whisper AI Models**: Download or import Whisper models under "Subtitles -> Local AI" panel (models are saved in user data directory).

## Updating and Uninstalling

- **Updating**: Close Kyna Player and run the new setup installer to upgrade in-place.
- **Uninstalling**: Use Windows "Installed Apps" or Start Menu uninstall shortcut.
