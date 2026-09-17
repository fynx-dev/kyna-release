---
title: "Anime4K Upscaling"
description: "Enable real-time Anime4K image reconstruction for anime and cartoon content."
order: 3
group: "Video, HDR & Enhancement"
---

# Anime4K Upscaling

Anime4K is a specialized real-time image enhancement pipeline designed for 2D animated content. It reconstructs sharp line art, refines flat textures, and upscales anime up to 4K resolution.

---

## 🚀 Enabling Anime4K

Open the sidebar **Video Enhance** drawer or press <kbd>Alt</kbd> + <kbd>V</kbd>:
- **Anime4K Mode A (Fast)**
  Optimized for 1080p -> 4K upscaling on integrated or laptop GPUs.
- **Anime4K Mode B (HQ)**
  High-precision line reconstruction for lower-resolution 720p anime.
- **Anime4K Mode C+A (Ultra)**
  Dual-pass de-blur and edge sharpening for maximum fidelity.

---

## 🔀 Real-Time Comparison Views

- **Split Screen (Left/Right)**
  Compares original low-res frames against enhanced results side-by-side.
- **Difference Heatmap**
  Displays high-frequency reconstructed edges.

---

## ⏱️ Dynamic Performance Budget

If GPU frame calculation exceeds the 16.6ms budget (for 60 FPS video), the player dynamically falls back to lightweight shaders to prevent frame drops.
