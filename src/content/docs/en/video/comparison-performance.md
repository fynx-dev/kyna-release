---
title: "Comparison & Budget"
description: "Understand split-screen comparison views, quality lock, frame time budgets, and dynamic fallback mechanisms."
order: 4
group: "Video, HDR & Enhancement"
---

# Comparison & Budget

When utilizing **Anime4K**, **DLSS 5**, or custom compute shaders, Kyna Player provides built-in comparison tools and dynamic performance budgeting to ensure stutter-free playback.

---

## 🔀 Split-Screen Comparison Views

| Comparison View | Format | Purpose |
| :--- | :--- | :--- |
| **Side-by-Side** | Left: Original, Right: Enhanced (with draggable divider line). | Inspect line sharpening and noise reduction |
| **Top-Bottom** | Top: Original, Bottom: Enhanced. | Wide landscape scene verification |
| **Difference Map** | Isolated high-frequency reconstructed pixels on black background. | Detect over-sharpening or halo artifacts |

---

## ⏱️ Frame Time Budget & Diagnostics

For 60 FPS video, each frame must decode, enhance, and present within **16.6 milliseconds**:
- Press <kbd>F12</kbd> to inspect real-time frame time metrics (`Decode ms` + `Shader ms`).

---

## 🛡️ Dynamic Fallback Strategy

1. **Performance Priority (Default)**: Automatically scales back filter intensity if frame calculation exceeds time budget for 3 consecutive frames.
2. **Quality Locked**: Enforces full shader computation regardless of GPU load (recommended for discrete high-end GPUs).
