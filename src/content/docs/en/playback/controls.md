---
title: "Playback & Stepping"
description: "Master Kyna Player's core playback controls, including play/pause, stop, frame stepping, speed control, and volume boost."
order: 1
group: "Playback & Seeking"
---

# Playback & Stepping

Kyna Player provides ultra-responsive playback controls. Whether enjoying movies or performing frame-accurate analysis, everything is easily accessible.

---

## 🎮 Basic Playback Controls

### 1. Play & Pause
- **Hotkey**
  <kbd>Space</kbd>
- **Mouse Action**
  Click the `▶ / ❚❚` button in the control bar or click the viewport center.
- **Zero Latency**
  Multi-threaded rendering ensures instantaneous pause and resume with rock-solid audio/video sync.

### 2. Stop
- **Hotkey**
  <kbd>S</kbd> or <kbd>Ctrl</kbd> + <kbd>S</kbd>
- **Behavior**
  Completely stops decoding, frees stream caches, and resets timeline to `00:00:00`.

---

## 🎞️ Frame Stepping (Forward & Backward)

Essential for inspecting high-speed action, capturing frame-perfect stills, or analyzing animation keyframes:

| Action | Hotkey | Description |
| :--- | :--- | :--- |
| **Frame Forward** | <kbd>.</kbd> / <kbd>E</kbd> | Advance exactly one frame while paused |
| **Frame Backward** | <kbd>,</kbd> | Step backward exactly one frame while paused |

> [!TIP]
> Pressing frame step keys while playing will automatically pause the video first, preventing flickering.

---

## ⏩ Speed Control with Pitch Preservation

Kyna Player uses high-fidelity time-stretching algorithms to preserve natural audio pitch across all speeds:
- **Preset Selection**
  Click the speed badge (e.g. `1.0x`) to choose `0.5x`, `0.75x`, `1.0x`, `1.25x`, `1.5x`, or `2.0x`.
- **Keyboard Tuning**
  - Speed Up: <kbd>]</kbd> or <kbd>C</kbd> (+0.1x)
  - Slow Down: <kbd>[</kbd> or <kbd>X</kbd> (-0.1x)
  - Reset: <kbd>Backspace</kbd> or <kbd>Z</kbd> (1.0x)

---

## 🔊 Volume Control & 200% Boost

- **Mouse Wheel**
  Scroll over the viewport to adjust volume in 5% increments.
- **Mute**
  Press <kbd>M</kbd> to instantly mute/unmute.
- **200% Software Boost**
  Amplify quiet movie dialogues beyond 100% up to 200% without distortion.
