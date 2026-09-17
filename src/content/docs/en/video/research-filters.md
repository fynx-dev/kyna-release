---
title: "Advanced Filters"
description: "Explore DLSS 5 neural super-resolution, CAS adaptive sharpening, Deband dithering, and custom shader pipelines."
order: 5
group: "Video, HDR & Enhancement"
---

# Advanced Filters

In addition to Anime4K, Kyna Player integrates experimental neural upscaling and cinematic post-processing shaders for live-action films.

---

## ⚡ DLSS 5 Neural Super-Resolution

- **Auto Hardware Routing**
  Detects discrete NVIDIA GPUs and initializes specialized tensor compute pipelines.
- **Compute Shader Universal Fallback**
  Universal fallback implementation runs smoothly on AMD Radeon and Intel Arc architectures.
- **Temporal Anti-Aliasing**
  Eliminates edge shimmering and high-frequency moiré patterns.

---

## 🔬 Post-Processing Shader Suite

| Filter | Algorithm | Problem Solved |
| :--- | :--- | :--- |
| **CAS** | Contrast Adaptive Sharpening | Enhances fine details without ringing or halo artifacts. |
| **Deband** | Gradient Dithering | Eliminates step-ladder color banding in sky and dark scenes. |
| **Bilateral** | Edge-Preserving Filter | Suppresses camera sensor noise while keeping facial hair and textures sharp. |
| **Film Grain** | Gaussian Noise Synthesizer | Adds authentic cinematic texture and masks compression artifacts. |

---

## 🎛️ Chaining & Intensity Controls

- **Filter Chaining**
  Stack multiple filters in sequence (e.g. `Deband` → `CAS Sharpening`).
- **Intensity Sliders**
  Fine-tune strength from `0.0` to `1.0`.
- **One-Click Bypass**
  Hold down hotkey to instantly bypass all active shaders.
