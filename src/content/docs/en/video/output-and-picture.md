---
title: "Video Output & Color"
description: "Configure GPU hardware-accelerated renderers, aspect ratio scaling, color calibration, and HDR tone mapping."
order: 1
group: "Video, HDR & Enhancement"
---

# Video Output & Color

Kyna Player features an advanced Direct3D hardware rendering pipeline, delivering peak GPU decode performance alongside flexible aspect ratios, color calibration, and wide color gamut HDR support.

---

## 🚀 Video Output & Hardware Acceleration

In **Settings → Video & Rendering**, choose the optimal rendering backend:

| Output Mode | Characteristics & Advantages | Target Hardware |
| :--- | :--- | :--- |
| **Direct3D 11 (D3D11)** *(Recommended)* | High compatibility and ultra-low latency; zero-copy GPU decode directly to display. | Windows 10/11 discrete & integrated GPUs |
| **Direct3D 12 (D3D12)** | Modern low-level rendering optimized for modern GPU compute pipelines. | RTX / RX series GPUs |
| **Software Decoding (CPU)** | High compatibility fallback for non-standard legacy codecs. | Failsafe fallback |

---

## 📐 Aspect Ratio & Scaling Modes

Press <kbd>A</kbd> or right-click → **Aspect Ratio**:
- **Keep Aspect Ratio (Fit)** *(Default)*: Preserves original proportions with letterboxing.
- **Stretch to Fill**
  Stretches video to fill window completely.
- **Crop to Fill**
  Zooms proportionally to eliminate black borders.
- **Fixed Presets**
  `16:9`, `4:3`, `21:9` (UltraWide), `1:1`.

---

## 🎚️ Color Calibration & Image Controls

Real-time non-destructive controls in **Video Settings**:
- **Brightness & Contrast**
  -50 to +50
- **Saturation & Hue**
  -50 to +50
- **Gamma**
  0.5 to 2.0
- **One-Click Reset**
  Restores default video color profile instantly.

---

## 🔄 Rotation & Mirror Flipping

- **Rotate 90° Clockwise**
  <kbd>Alt</kbd> + <kbd>R</kbd>
- **Horizontal Mirror Flip**
  <kbd>Alt</kbd> + <kbd>H</kbd> (Ideal for dance tutorials)
- **Vertical Flip**
  <kbd>Alt</kbd> + <kbd>V</kbd>

---

## 🌈 HDR & Tone Mapping

When playing 4K HDR10, HLG, or Dolby Vision media:
- **HDR Passthrough**
  Outputs native 10-bit BT.2020 signals to HDR displays.
- **SDR Tone Mapping**
  Automatically compresses dynamic range using Reinhard / Mobius algorithms on standard SDR screens without washed-out highlights.
