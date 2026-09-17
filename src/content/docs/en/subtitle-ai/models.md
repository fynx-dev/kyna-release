---
title: "AI Models & Acceleration"
description: "Manage offline Whisper model weights, configure GPU compute backends, and optimize VRAM usage."
order: 4
group: "Subtitle AI & Translation"
---

# AI Models & Acceleration

Manage on-device model weights and select compute backends in **Settings → AI Models**.

---

## 📥 Model Storage & Downloads

- **One-Click Download**
  Download Whisper models directly within Kyna Player with automatic SHA-256 verification.
- **Storage Path**
  `%APPDATA%\KynaPlayer\models\`.
- **Manual Import**
  Place standard `ggml-*.bin` weights into the models directory for air-gapped offline use.

---

## ⚡ Hardware Acceleration Backends

| Backend | Hardware | Acceleration Ratio |
| :--- | :--- | :--- |
| **NVIDIA CUDA** *(Recommended)* | GeForce / RTX GPUs | 🚀 Ultra (~20x-30x) |
| **DirectML** | AMD Radeon / Intel Arc / APUs | ⚡ High (~8x-15x) |
| **Vulkan Compute** | Cross-platform GPUs | ⚡ Medium (~8x-12x) |
| **CPU AVX2 / OpenVINO** | Modern multi-core CPUs | 🔄 Standard (~2x-4x) |

---

## 🧹 Smart VRAM Scheduling

- **Lazy Loading**
  Models load into VRAM only when transcription starts.
- **Auto-Unload**
  Unloads models after 5 minutes of idle time, freeing 100% VRAM for games or 4K rendering.
