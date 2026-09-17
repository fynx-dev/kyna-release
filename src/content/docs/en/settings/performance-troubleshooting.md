---
title: "Performance Tuning"
description: "Resolve dropped frames, black/green screens, audio desync, and HDR color issues."
order: 4
group: "Settings & Troubleshooting"
---

# Performance Tuning

Quick diagnostic steps for resolving playback anomalies:

---

## 🛠️ Common Issues & Fixes

### 1. 📺 4K/8K Dropped Frames or Stutter
- **GPU Scheduling (Dual-GPU Laptops)**
  In Windows Settings → Display → Graphics, assign `Kyna Player` to **"High Performance (Discrete GPU)"**.
- **Hardware Acceleration**
  Ensure **"Direct3D 11 (D3D11VA)"** is active in Video Settings.
- **Shader Load**
  Switch Anime4K to *Mode Fast* or temporarily disable heavy post-processing.

### 2. 🟢 Black or Green Screen with Normal Audio
- **Fix**
  Right-click viewport → **Video** → Switch to **"Software Decoding (CPU)"**, then update GPU drivers to the latest WHQL release.

### 3. 🌈 Washed-Out HDR Colors on SDR Screens
- **Fix**
  Enable **"SDR Tone Mapping"** in Video Settings and select `Reinhard` or `Mobius` tone mapping.
