#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Flat Multilingual (en, ja, ko) Docs for Kyna Player aligned with zh-CN"""

import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_ROOT = os.path.join(BASE_DIR, 'src', 'content', 'docs')

def clean_and_prepare(lang):
    target_dir = os.path.join(DOCS_ROOT, lang)
    if os.path.exists(target_dir):
        for item in os.listdir(target_dir):
            p = os.path.join(target_dir, item)
            if os.path.isdir(p):
                shutil.rmtree(p)
            elif os.path.isfile(p):
                os.remove(p)
    os.makedirs(target_dir, exist_ok=True)
    return target_dir

def write_doc(target_dir, filename, content):
    full_path = os.path.join(target_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# ==============================================================================
# ENGLISH (en)
# ==============================================================================
def gen_en():
    d = clean_and_prepare('en')

    write_doc(d, "getting-started.md", """---
title: "Quick Start"
description: "Discover Kyna Player's core features, interface layout, and media opening methods."
order: 1
group: "Getting Started"
---

# 🚀 Quick Start

**Kyna Player** is a modern, lightweight video player built specifically for Windows. Combining GPU hardware-accelerated rendering, local offline Whisper AI subtitles, and Anime4K upscaling technology, it delivers a pure and immersive viewing experience.

---

## ✨ Core Features

- **GPU Hardware Acceleration**
  Direct3D 11 hardware decoding and zero-copy rendering allow silky-smooth 4K/8K playback with minimal CPU usage.
- **HDR Tone Mapping**
  Naturally reproduces Dolby Vision and HDR10 rich dynamic colors on standard SDR monitors.
- **Offline AI Subtitles**
  Built-in local Whisper transcription and LLM translation with 100% offline privacy protection.
- **Anime4K Super-Resolution**
  Reconstructs sharp line art and vibrant colors in real time—the ultimate companion for anime enthusiasts.
- **Immersive Distraction-Free UI**
  Minimalist interface with auto-hiding controls, supporting rich keyboard shortcuts and smooth mouse interactions.

---

## 🖥️ Interface & Interaction Overview

![Interface Overview](/assets/images/docs/main-ui.png)

- **Top Title Bar**
  Appears when hovering near the top; supports Window Pinning 📌, Minimize, Fullscreen, and Close.
- **Video Viewport**
  Single-click to Play/Pause, double-click for Fullscreen, scroll wheel to adjust volume, and drag-and-drop to open files.
- **Floating Control Bar**
  Integrates progress bar, hover thumbnail previews, playback speed, loop modes, and quick tool shortcuts.
- **Right Sidebar**
  Quickly toggle Playlist, Subtitle tracks, Audio enhancements, and Video filters.

---

## 📂 Opening Media

![Open File Menu](/assets/images/docs/openfile-menu.png)

- **Drag and Drop**
  Simply drag video files, audio tracks, or entire TV season folders directly into the player window.
- **Keyboard Shortcut**
  Press <kbd>O</kbd> to bring up the Windows file dialog to select media files.
- **Network Stream URL**
  Select "Open URL" from the menu to play HTTP/HTTPS direct links, HLS (`.m3u8`), or RTMP live streams.
""")

    write_doc(d, "installation.md", """---
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
- **Directory Path**: `%APPDATA%\\KynaPlayer\\` (accessible with one click in **Settings → General**).
- **Structure**:
  - `config.json`: Preferences, configurations, and custom keybindings.
  - `history.json`: Playback history and resume positions.
  - `thumbnails\\`: Cached timeline hover thumbnail previews.
  - `models\\`: Local offline Whisper AI models.
""")

    write_doc(d, "playback.md", """---
title: "Playback & Navigation"
description: "Core playback controls, precision seeking, speed & loop modes, and hotkeys."
order: 1
group: "Playback & Video"
---

# ⏯️ Playback & Navigation

Kyna Player features an ultra-responsive playback engine with sub-frame seek precision and full keyboard controllability.

---

## 🎮 Shortcut Keys Cheatsheet

| Action | Default Shortcut | Mouse Action | Description |
| :--- | :--- | :--- | :--- |
| **Play / Pause** | <kbd>Space</kbd> | Click viewport center | Toggle playback and pause state |
| **Stop** | <kbd>S</kbd> | Stop button on control bar | Stop decoding and reset progress to beginning |
| **Toggle Fullscreen** | <kbd>F</kbd> | Double-click viewport | Enter / Exit fullscreen mode |
| **Exit Fullscreen / Layer** | <kbd>Escape</kbd> | - | Exit fullscreen or dismiss active modal overlay |
| **Frame Step Forward** | <kbd>.</kbd> | - | Step forward exactly one frame while paused |
| **Volume Control** | <kbd>↑</kbd> / <kbd>↓</kbd> | Scroll mouse wheel | Increase / decrease audio volume |
| **Mute / Unmute** | <kbd>M</kbd> | Click volume icon | Toggle audio mute |
| **Open File** | <kbd>O</kbd> | Click open button | Open system file picker dialog |
| **Performance OSD** | <kbd>Tab</kbd> | - | Toggle realtime FPS, dropped frames, bitrate & render latency |

---

## ⏳ Progress Bar & Hover Thumbnails

![Timeline Thumbnail Preview](/assets/images/features/thumbnails.webp)

- **Hover Thumbnails**
  Hover anywhere across the timeline to instantly preview keyframe scenes and timestamps.
- **Precision Stepping**
  Press arrow keys <kbd>→</kbd> / <kbd>←</kbd> to jump forward or backward smoothly.

---

## 🔁 Loop & Playback Modes

Click the loop icon on the right side of the control bar to cycle modes:
- 🔁 **Loop All**: Cycles the playlist continuously—perfect for binge-watching.
- 🔂 **Repeat Single**: Repeats the current video endlessly for dance/skills practice.
- 🔀 **Shuffle**: Plays list items in random order for music libraries.
- ➡️ **Sequential**: Plays sequentially and stops at the end of the list.
""")

    write_doc(d, "video-enhance.md", """---
title: "Video Enhancement & Settings"
description: "Direct3D 11 hardware acceleration, adaptive detail enhancement, Anime4K upscaling & filters."
order: 2
group: "Playback & Video"
---

# 🎨 Video Enhancement & Settings

Built on a dedicated Direct3D hardware pipeline, Kyna Player provides rich picture controls and AI upscaling algorithms.

---

## 🚀 Video Rendering & Hardware Acceleration

- **Direct3D 11 Accelerated Pipeline**
  Leverages GPU hardware decoding with zero-copy presentation, natively handling high-bitrate 4K/8K content with minimal CPU load.
- **Three Aspect Ratio Fill Modes**
  - **Contain**: Preserves the native aspect ratio with black letterboxing.
  - **Fill**: Stretches the image to fill the entire window.
  - **Cover**: Crops margins proportionally to eliminate black bars.

---

## ✨ Adaptive Local Detail Enhancement

![Video Enhancement Filters](/assets/images/docs/dlss5.png)

- **Adaptive Enhancement**
  Real-time 1× local detail and contrast booster that refines edges and clarifies dark scenes while preserving smooth color gradients.
- **Research Enhancement**
  Offers experimental neural upscaling filter extensions for ultra-demanding video sources.

---

## 🌸 Anime4K Super-Resolution

![Anime4K Upscaling](/assets/images/docs/anime4K.png)

- **Anime 2× Upscaling**
  Built-in shaders optimized specifically for 2D animation (`Anime4K CNN x2 S` & `Anime4K DTD x2`).
- **Edge Reconstruction & Anti-Aliasing**
  Rebuilds crisp outlines and removes compression artifacts, delivering pristine visuals on 2K/4K high-resolution displays.
""")

    write_doc(d, "subtitles.md", """---
title: "Subtitles & Appearance"
description: "Embedded & external subtitles, dual subtitle side-by-side display, and styling."
order: 1
group: "Subtitles & AI Lab"
---

# 💬 Subtitles & Appearance

Kyna Player features a powerful subtitle rendering engine with dual subtitle support and fine-grained style customization.

---

## 📑 Loading & Selecting Subtitles

![Subtitle Menu & Dual Subtitles](/assets/images/docs/subtitle-menu.png)

- **Control Bar & Context Menu**
  Click the subtitle icon or right-click to quickly select primary and secondary subtitle tracks.
- **Drag & Drop External Files**
  Drag `.srt`, `.ass`, `.ssa`, or `.vtt` files directly into the window to load instantly.
- **Auto-Association**
  Subtitles in the same folder sharing the video filename (e.g., `movie.en.srt`) are loaded automatically.

---

## 👥 Dual Subtitles System

The ideal companion for language learning and bilingual comparison:
- **Primary Subtitle**: Typically set to translated text with a larger font size.
- **Secondary Subtitle**: Typically set to original language dialogue.
- **Independent Size Control**: Adjust font sizes individually for primary (13~48px) and secondary (13~40px) subtitles.

---

## 🎨 Styling & Online Search

- **Custom Styles**
  Customize font family, font scale, bold outlines, and translucent shadow boxes.
- **Online Subtitle Extensions**
  Built-in subtitle plugin engine enables accurate hash-based matching and one-click downloading.
""")

    write_doc(d, "ai-lab.md", """---
title: "AI Speech-to-Text & Translation"
description: "Local offline Whisper voice recognition, LLM contextual subtitle translation workflow."
order: 2
group: "Subtitles & AI Lab"
---

# 🤖 AI Speech-to-Text & Translation

Never worry about untranslated raw videos again! Kyna Player offers a complete automated AI subtitle workflow from speech extraction to bilingual subtitles.

---

## ⚡ Core Pipeline

```
[ Extract Audio ] ──> [ Local Whisper Offline ASR ] ──> [ LLM Context Translation ] ──> [ Real-Time Dual Subtitle Mount ]
```

![Whisper Lab Workflow](/assets/images/docs/whisper-lab-workflow.png)

- **100% Offline Privacy Protection**
  Whisper speech recognition runs entirely on your local GPU or CPU without uploading any audio.
- **Context-Aware LLM Translation**
  Integrates with DeepSeek, ChatGPT, Claude, or local Ollama to produce natural translations based on cinematic context.

![Whisper Lab Translation](/assets/images/docs/whisper-lab-translate.png)

---

## 🧠 Whisper Model Specifications

| Model Size | VRAM Usage | Speed (RTX 4060) | Accuracy | Recommended Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Base** | ~1.0 GB | ~20x Ultra Fast | Good | Short clips, clear English/Chinese speech |
| **Small** | ~1.8 GB | ~12x Fast | Excellent *(Recommended)* | TV dramas, anime series daily use |
| **Medium** | ~3.5 GB | ~6x Steady | Very High | Academic lectures, multi-language speech |
| **Large-v3** | ~6.0 GB | ~3x Steady | Top-tier Peak | Complex background music, high-precision needs |
""")

    write_doc(d, "audio-and-tools.md", """---
title: "Audio & Sound Enhancement"
description: "Multi-track switching, Night Mode (DRC), Voice Enhance, and A/V sync adjustment."
order: 1
group: "Tools & Settings"
---

# 🔊 Audio & Sound Enhancement

Beyond exceptional video rendering, Kyna Player packs a suite of practical audio DSP tools.

---

## 🎧 Audio Enhancement & Sync

- **Fast Audio Track Switching**
  Switch audio tracks instantly from the control bar with native support for multi-channel lossless audio.

![Audio Track Switching](/assets/images/docs/audio-tracks.png)

- **🌙 Night Mode (Dynamic Range Compression)**
  Suppresses sudden loud explosions while lifting quiet whispers, complete with **Live Waveform Comparison**.

![Night Mode & Live Waveform](/assets/images/docs/audio-night-mode.png)

- **🗣️ Voice Enhance**
  Intelligently boosts centered dialogue in stereo mixes, accompanied by **40Hz~16kHz Live Band Energy Spectrum**.

![Voice Enhance & Spectrum](/assets/images/docs/audio-void-enhance.png)

- **⏱️ Audio/Video Sync Adjustment**
  Provides `-100ms` / `Reset` / `+100ms` delay controls to easily rectify audio desynchronization.
""")

    write_doc(d, "dlna.md", """---
title: "DLNA Wireless Casting"
description: "Big-screen TV casting (DMC) and local media receiver (DMR) dual functionality guide."
order: 2
group: "Tools & Settings"
---

# 📺 DLNA Wireless Casting

Kyna Player provides full DLNA / UPnP screencasting support, featuring both **Big-Screen TV Casting (DMC)** and **Local Media Receiver (DMR)** modes.

---

## 📡 1. Big-Screen TV Casting (DMC)

Stream local high-definition videos wirelessly to your living room Smart TV, projector, or TV box.

![DLNA Cast to TV](/assets/images/docs/dlna-cast-to-tv.png)

### Steps
1. **Open Cast Workbench**
   While playing media, click the `📺 Cast` icon on the control bar to expand the cast workbench.
2. **Select Target Device**
   The workbench automatically scans your local network. Click your smart TV from the list.
3. **Stream Instantly**
   Click **Connect / Cast** to start playback on your TV immediately.

### Synchronized PC Remote Control
- **Playback & Seeking**: Pause, resume, or scrub the timeline on your PC with real-time TV synchronization.
- **Volume**: Adjust or mute big-screen volume directly from your computer.
- **Disconnect**: Click "Disconnect" at any time to resume playing locally.

---

## 📥 2. Local Media Receiver (DMR)

Kyna Player can also function as a DLNA renderer to receive media casts from smartphones or tablets.

![DLNA Receive Cast](/assets/images/docs/dlna-recv-cast.png)

- **Enable Receiver**
  Click the **Receive Casts** button on the control bar.
- **Cast from Mobile**
  In mobile video apps (YouTube, Bilibili, etc.), tap the "TV Cast" icon and select **Kyna Player** to stream to your PC screen.

---

## 🛠️ Network & Firewall Configuration

- **Same Local Network**
  Ensure PC and TV connect to the same router (5GHz Wi-Fi or Gigabit Ethernet recommended).
- **Windows Firewall**
  Allow Kyna Player through Windows Firewall when prompted for both private and public networks.
- **AP Isolation**
  If devices cannot be discovered, verify that "AP Isolation" or "Guest Network" is disabled on your router.
""")

    write_doc(d, "playlist.md", """---
title: "Playlist & File Management"
description: "Playlist management, M3U8 export, folder batch scanning, and playback history."
order: 3
group: "Tools & Settings"
---

# 📑 Playlist & File Management

Effortlessly manage large collections of TV dramas, anime series, and music tracks.

---

## ➕ Playlist Operations & Export

![Playlist Sidebar](/assets/images/docs/player-playlist.png)

- **Open Playlist**
  Click the `📑 Playlist` button on the control bar to open the sidebar.
- **Drag to Reorder**
  Drag items up and down in the list to reorder playback immediately.
- **Save & Export**
  Export playlists as universal UTF-8 `.m3u8` files with relative paths that stay valid when moved.

---

## 📁 Smart Batch Folder Scanning

![Folder Batch Scanning](/assets/images/docs/drag-files-and-folder.png)

Dragging a TV series folder into the player brings up the import dialog:
- **Recursive Scan**: Traverses all subdirectories to collect audio and video files.
- **Smart Filtering**: Automatically filters out poster images, `.nfo` metadata, and cache files.
- **Natural Number Sorting**: Orders episodes cleanly from `Ep 1` → `Ep 2` → `Ep 10`.

---

## 🕒 Recent History & Resume

- **Playback Resume**: Records exact exit timestamps for instant, seamless resuming.
- **File Management**: Locate files in File Explorer or remove entries right from the list.
""")

    write_doc(d, "settings.md", """---
title: "Preferences & Troubleshooting"
description: "Preferences center, Windows file associations, troubleshooting, and feedback."
order: 4
group: "Tools & Settings"
---

# ⚙️ Preferences & Troubleshooting

Customize your player according to your hardware environment and resolve common playback issues.

---

## 🎛️ Settings Navigation

![Settings Navigation](/assets/images/docs/player-settings.png)

- **General**: Multi-language switching (Simplified Chinese, English, Japanese, Korean), instance limits, and AppData directory shortcut.
- **Playback**: Default open behavior (Replace / Append), auto-play next item, and history memory.
- **Hotkeys**: View and customize keyboard shortcut bindings.
- **File Associations**: Register system-level default video extensions with the `Play with Kyna Player` context menu.

![Playlist Settings](/assets/images/docs/openfile-playlist-settings.png)

---

## 🛠️ Common Troubleshooting

### 1. 4K/8K Playback Stuttering or Frame Drops
- **GPU Scheduling**: On laptops with dual GPUs, assign Kyna Player to "High Performance Dedicated GPU" in Windows Settings.
- **Hardware Acceleration**: Verify that Direct3D 11 acceleration is enabled.
- **Filter Load**: If Anime4K is active, reduce the scaling preset based on GPU capacity.

### 2. Subtitle Character Encoding Errors
- Ensure subtitle files are saved in `UTF-8` format. Re-save files as UTF-8 in a text editor if needed.

---

## 💬 Feedback & Logs

- **Retrieve Logs**: Click "Open AppData Directory" in Settings and look into the `logs/` folder for `kyna_player.log`.
- **Submit Issue**: Visit [GitHub Issues](https://github.com/fynx-dev/kyna-release/issues) to submit your bug report.
""")
    print("[en] Generated all 10 English docs.")

# ==============================================================================
# JAPANESE (ja)
# ==============================================================================
def gen_ja():
    d = clean_and_prepare('ja')

    write_doc(d, "getting-started.md", """---
title: "クイックスタート"
description: "Kyna Player の主要機能、インターフェース構成、メディアの開き方を紹介。"
order: 1
group: "入門ガイド"
---

# 🚀 クイックスタート

**Kyna Player** は、Windows 向けに設計されたモダンで軽量な動画プレーヤーです。GPU ハードウェアアクセラレーション、ローカル完全オフライン Whisper AI 字幕、Anime4K 超解像技術を融合し、純粋で没入感のある視聴体験をお届けします。

---

## ✨ コア機能

- **GPU ハードウェアアクセラレーション**
  Direct3D 11 ハードウェアデコードと VRAM ゼロコピー直接描画により、CPU 負荷を極限まで抑えて 4K/8K 動画を滑らかに再生。
- **HDR トーンマッピング**
  通常の SDR モニター上でも Dolby Vision および HDR10 の豊かな色彩を自然に再現。
- **オフライン AI 字幕**
  内蔵の Whisper 音声認識と LLM 翻訳により、完全ローカルで動作しプライバシーを 100% 保護。
- **Anime4K アニメ超解像**
  鮮明な輪郭線とクリアな色面をリアルタイムに再構築。アニメ鑑賞に最適な機能です。
- **没入型ミニマルデザイン**
  余計な装飾を排したデザインで、コントロールバーは自動的にフェードアウト。多彩なショートカット操作に対応。

---

## 🖥️ インターフェース構成

![インターフェース概要](/assets/images/docs/main-ui.png)

- **上部タイトルバー**
  マウスを画面上部に移動すると表示。ピン留め 📌、最小化、全画面、閉じる操作に対応。
- **動画メインビュー**
  シングルクリックで再生/一時停止、ダブルクリックで全画面切り替え、ホイールで音量調整。
- **フローティングコントロールバー**
  シークバー、サムネイルプレビュー、再生速度、ループモード、各ツールへのアクセスを集約。
- **右側サイドバー**
  プレイリスト、字幕トラック、音声強化、画質フィルターをすばやく展開。

---

## 📂 メディアの開き方

![ファイルを開くメニュー](/assets/images/docs/openfile-menu.png)

- **ドラッグ＆ドロップ**
  動画、音楽ファイル、またはフォルダーを直接プレーヤーウィンドウにドラッグ。
- **ショートカットキー**
  <kbd>O</kbd> キーを押してファイル選択ダイアログを表示。
- **ネットワークストリーム再生**
  メニューから「URL を開く」を選択し、HTTP/HTTPS、HLS (`.m3u8`)、RTMP などの配信 URL を入力。
""")

    write_doc(d, "installation.md", """---
title: "インストールとシステム要件"
description: "動作環境、インストール手順、アップデート、アプリデータディレクトリの管理。"
order: 2
group: "入門ガイド"
---

# 📦 インストールとシステム要件

## 💻 動作環境

| 項目 | 最低環境 | 推奨環境 |
| :--- | :--- | :--- |
| **OS** | Windows 10 (64-bit) 1909+ | Windows 11 (22H2+) |
| **CPU** | Intel Core i3 / AMD Ryzen 3 | Intel Core i5 / AMD Ryzen 5 以上 |
| **GPU** | Direct3D 11 ハードウェアデコード対応 | DX12 / HEVC / AV1 / VP9 加速対応 |
| **メモリ (RAM)** | 4 GB | 8 GB 以上 |

---

## 🚀 インストールとアップデート

1. **インストーラーのダウンロード**
   [GitHub Releases](https://github.com/fynx-dev/kyna-release/releases/latest) から `Kyna-Setup.exe` をダウンロード。
2. **セットアップウィザード**
   インストーラーを起動し、画面の指示に従って完了させます。
3. **アップデート**
   プレーヤーを終了し、最新のインストーラーを実行して上書きインストールします。設定やダウンロード済みの AI モデルはそのまま保持されます。

---

## 🗄️ アプリデータとキャッシュディレクトリ

ユーザーデータは標準の AppData フォルダに保存されます：
- **ディレクトリパス**: `%APPDATA%\\KynaPlayer\\`（**設定 → 一般** からワンクリックで開けます）。
- **構造**:
  - `config.json`: 設定とキーバインド。
  - `history.json`: 再生履歴とレジューム情報。
  - `thumbnails\\`: タイムラインサムネイルのキャッシュ。
  - `models\\`: ローカルの Whisper AI 音声認識モデル。
""")

    write_doc(d, "playback.md", """---
title: "再生制御とショートカット"
description: "基本再生操作、高精度シーク、速度・ループモード、主要ショートカットキー一覧。"
order: 1
group: "再生と画質"
---

# ⏯️ 再生制御とショートカット

Kyna Player はミリ秒精度のシークとキーボード操作に対応した高速再生エンジンを搭載しています。

---

## 🎮 主要ショートカットキー一覧

| 操作 | デフォルトキー | マウス操作 | 説明 |
| :--- | :--- | :--- | :--- |
| **再生 / 一時停止** | <kbd>Space</kbd> | 画面中央をクリック | 再生と一時停止を切り替え |
| **停止** | <kbd>S</kbd> | コントロールバーの停止ボタン | 再生を停止し先頭にリセット |
| **全画面切り替え** | <kbd>F</kbd> | 画面をダブルクリック | 全画面表示の切り替え |
| **全画面/レイヤー解除** | <kbd>Escape</kbd> | - | 全画面を終了または開いているポップアップを閉じる |
| **コマ送り** | <kbd>.</kbd> | - | 一時停止中に 1 フレーム進める |
| **音量調整** | <kbd>↑</kbd> / <kbd>↓</kbd> | マウスホイール上下 | 音量を増減 |
| **ミュート切り替え** | <kbd>M</kbd> | 音量アイコンをクリック | 消音 / 消音解除 |
| **ファイルを開く** | <kbd>O</kbd> | 開くボタンをクリック | ファイル選択ダイアログを表示 |
| **性能統計 OSD** | <kbd>Tab</kbd> | - | FPS、ドロップフレーム、ビットレート、描画時間を表示 |

---

## ⏳ シークバーとサムネイルプレビュー

![タイムラインサムネイル](/assets/images/features/thumbnails.webp)

- **サムネイルプレビュー**
  シークバー上にマウスを置くと、該当シーンの映像とタイムスタンプをリアルタイム表示。
- **ステップ移動**
  方向キー <kbd>→</kbd> / <kbd>←</kbd> で前後にミリ秒単位ですばやくシーク。

---

## 🔁 ループと再生モード

コントロールバー右側のループアイコンをクリックして切り替え：
- 🔁 **全曲ループ**: リスト末尾まで再生後、最初から繰り返します。
- 🔂 **1曲ループ**: 現在の動画を繰り返し再生。
- 🔀 **シャッフル**: リスト内の項目をランダムに再生。
- ➡️ **順次再生**: 末尾まで再生すると自動停止します。
""")

    write_doc(d, "video-enhance.md", """---
title: "画質強化と映像設定"
description: "Direct3D 11 ハードウェアアクセラレーション、適応型ディテール補正、Anime4K アニメ超解像。"
order: 2
group: "再生と画質"
---

# 🎨 画質強化と映像設定

Direct3D パイプラインを基盤とし、多彩な画面調整と AI 超解像アルゴリズムを提供します。

---

## 🚀 映像描画とハードウェアアクセラレーション

- **Direct3D 11 高速描画パイプライン**
  GPU ハードウェアデコードとゼロコピー描画により、高ビットレートな 4K/8K 映像も低負荷で再生。
- **3 種類のアスペクト比フィットモード**
  - **Contain (アスペクト比維持)**: 歪みなく黒帯を入れて原画比率で表示。
  - **Fill (引き伸ばし)**: 画面全体に引き伸ばして表示。
  - **Cover (トリミング)**: 黒帯なしで等比率拡大し余白を切り抜きます。

---

## ✨ 適応型ローカルディテール補正

![画質フィルターとディテール補正](/assets/images/docs/dlss5.png)

- **適応型補正 (Adaptive enhancement)**
  輪郭と明暗差をスマートに強調し、自然な階調を保ちながらディテールをくっきりと表現。
- **研究向け補正 (Research Enhancement)**
  高精度が求められる映像向けに、高度な超解像フィルター拡張を提供。

---

## 🌸 Anime4K アニメ超解像

![Anime4K アニメ超解像](/assets/images/docs/anime4K.png)

- **アニメ 2 倍超解像**
  2D アニメに特化した超解像シェーダー（`Anime4K CNN x2 S` / `Anime4K DTD x2`）を内蔵。
- **輪郭再構築とアンチエイリアス**
  圧縮ノイズを除去し輪郭線を鮮明に再構築。大画面 2K/4K ディスプレイでも美しいアニメ鑑賞が楽しめます。
""")

    write_doc(d, "subtitles.md", """---
title: "字幕管理とスタイル外観"
description: "内蔵/外部字幕の読み込み、メイン・サブのデュアル字幕表示、スタイル外観設定。"
order: 1
group: "字幕と AI ラボ"
---

# 💬 字幕管理とスタイル外観

強力な字幕レンダリングエンジンを搭載し、2 言語のデュアル字幕同時表示や外観カスタマイズに対応しています。

---

## 📑 字幕の読み込みと切り替え

![字幕メニューとデュアル字幕設定](/assets/images/docs/subtitle-menu.png)

- **コントロールバーとコンテキストメニュー**
  字幕アイコンまたは右クリックメニューから、主字幕と副字幕のトラックを即座に指定。
- **外部字幕のドラッグ＆ドロップ**
  `.srt`, `.ass`, `.ssa`, `.vtt` ファイルを直接ウィンドウにドラッグするだけで即座に反映。
- **同名ファイル自動関連付け**
  動画と同じフォルダにある同名字幕（例: `movie.ja.srt`）を自動的に読み込みます。

---

## 👥 デュアル字幕システム (Dual Subtitles)

語学学習や対訳表示に最適：
- **主字幕 (Primary Subtitle)**: 通常は日本語訳などの母国語（大きめのフォント）。
- **副字幕 (Secondary Subtitle)**: 原語のセリフ（小さめのフォント）。
- **独立フォントサイズ調整**: 主字幕 (13~48px) と副字幕 (13~40px) の文字サイズを個別に調整可能。

---

## 🎨 スタイル設定とオンライン検索

- **フォントと外観の微調整**
  フォントファミリー、文字サイズ、アウトラインの太さ、半透明シャドウボックスを自由に設定。
- **オンライン字幕検索拡張**
  プラグインエンジンにより、動画ハッシュから一致する字幕を検索してワンクリックで適用できます。
""")

    write_doc(d, "ai-lab.md", """---
title: "AI 音声認識と翻訳"
description: "完全ローカル Whisper 音声認識、大規模言語モデル (LLM) 文脈字幕翻訳。"
order: 2
group: "字幕と AI ラボ"
---

# 🤖 AI 音声認識と翻訳

字幕のない動画も安心！Kyna Player は音声認識から高品質な対訳字幕の生成まで、完全自動化された AI 字幕ワークフローを備えています。

---

## ⚡ コアパイプライン

```
[ 音声抽出 ] ──> [ ローカル Whisper オフライン認識 ] ──> [ LLM 文脈翻訳 ] ──> [ デュアル字幕リアルタイム適用 ]
```

![Whisper ラボ ワークフロー](/assets/images/docs/whisper-lab-workflow.png)

- **100% オフラインのプライバシー保護**
  Whisper 音声認識はローカルの GPU または CPU 上で完全に動作し、音声データを外部に送信しません。
- **文脈を考慮した LLM 翻訳**
  DeepSeek、ChatGPT、Claude、またはローカル Ollama と連携し、ストーリーの流れに合った自然な翻訳を出力。

![Whisper ラボ 翻訳](/assets/images/docs/whisper-lab-translate.png)

---

## 🧠 Whisper モデル仕様

| モデルサイズ | VRAM 目安 | 認識速度 (RTX 4060) | 精度 | 推奨用途 |
| :--- | :--- | :--- | :--- | :--- |
| **Base** | ~1.0 GB | ~20x 超高速 | 良好 | ショート動画、明瞭な英語/日本語会話 |
| **Small** | ~1.8 GB | ~12x 高速 | 優秀 *(おすすめ)* | ドラマ、アニメ日常鑑賞 |
| **Medium** | ~3.5 GB | ~6x 安定 | 非常に高い | 講義、複数言語が混在する音声 |
| **Large-v3** | ~6.0 GB | ~3x 安定 | 最高峰の精度 | BGM が多い動画、高精度重視 |
""")

    write_doc(d, "audio-and-tools.md", """---
title: "音声とオーディオ強化"
description: "音声トラック切り替え、夜間モード (DRC)、声の強調、音ズレ補正。"
order: 1
group: "ツールとシステム設定"
---

# 🔊 音声とオーディオ強化

優れた映像再生に加え、実用的なオーディオ DSP ツールキットを搭載しています。

---

## 🎧 音声強化と同期調整

- **音声トラックの素早い切り替え**
  コントロールバーから即座に音声を切り替え可能。マルチチャンネルロスレス音声もネイティブサポート。

![音声トラック切り替え](/assets/images/docs/audio-tracks.png)

- **🌙 夜間モード (ダイナミックレンジ圧縮 / DRC)**
  突然の爆発音を抑え、小さなささやき声を明瞭化。**リアルタイム波形比較 (Live waveform)** を備えています。

![夜間モードとリアルタイム波形](/assets/images/docs/audio-night-mode.png)

- **🗣️ 声の強調 (Voice enhance)**
  ステレオ中央のセリフ成分を自然にブースト。**40Hz〜16kHz リアルタイム帯域スペクトラム** で効果を確認可能。

![声の強調とスペクトラム](/assets/images/docs/audio-void-enhance.png)

- **⏱️ 音画同期の微調整**
  `-100ms` / `リセット` / `+100ms` の遅延調整で、映像と音声のズレを簡単に解消。
""")

    write_doc(d, "dlna.md", """---
title: "DLNA ワイヤレス投影"
description: "大画面テレビへのワイヤレス投影 (DMC) とローカル受信 (DMR) の双方向ガイド。"
order: 2
group: "ツールとシステム設定"
---

# 📺 DLNA ワイヤレス投影

Kyna Player は DLNA / UPnP 投影をサポートし、**大画面テレビへの投影 (DMC)** と **ローカル投影受信 (DMR)** の両方に対応しています。

---

## 📡 1. 大画面テレビへの投影 (DMC)

パソコン内の高画質動画を、リビングのスマートテレビやプロジェクターへワイヤレス配信して大画面再生。

![DLNA テレビ投影ワークベンチ](/assets/images/docs/dlna-cast-to-tv.png)

### 手順
1. **投影ワークベンチを開く**
   動画再生中にコントロールバー右側の `📺 投影` アイコンをクリック。
2. **機器を選択**
   同一ネットワーク内の DLNA 機器を自動スキャンします。リストからお使いのテレビを選択。
3. **大画面再生スタート**
   **接続 / 投影** をクリックすると、テレビ側で即座に再生が始まります。

### PC からの同期リモコン操作
- **再生とシーク**: PC 側で一時停止やシークバーを操作すると、テレビ側もリアルタイムに追従します。
- **音量調整**: 大画面の音量やミュートを PC から直接コントロール。
- **切断**: いつでも「切断」をクリックしてローカル再生に戻せます。

---

## 📥 2. ローカル投影受信 (DMR)

Kyna Player を DLNA レシーバーとして動作させ、スマートフォンやタブレットから動画を受信できます。

![DLNA 受信通知](/assets/images/docs/dlna-recv-cast.png)

- **受信を有効化**
  コントロールバーの **投影を受信** ボタンをクリック。
- **スマホからキャスト**
  スマートフォンの動画アプリで「TVキャスト」をタップし、**Kyna Player** を選択するとパソコン画面で再生されます。

---

## 🛠️ ネットワークとファイアウォール設定

- **同一ローカルネットワーク**
  PC とテレビが同じルーターに接続されていることを確認してください（5GHz Wi-Fi または有線 LAN を推奨）。
- **Windows ファイアウォールの許可**
  初回利用時にファイアウォールの確認が出た場合は、プライベートおよびパブリック両方のアクセスを許可してください。
- **AP 分離機能の確認**
  機器が検出されない場合は、ルーターの「プライバシーセパレーター (AP 分離)」が無効になっているかご確認ください。
""")

    write_doc(d, "playlist.md", """---
title: "プレイリストとファイル管理"
description: "プレイリスト管理、M3U8 エクスポート、フォルダー一括スキャン、再生履歴。"
order: 3
group: "ツールとシステム設定"
---

# 📑 プレイリストとファイル管理

膨大なアニメシリーズや映画、音楽コレクションを快適に整理・再生できます。

---

## ➕ プレイリスト操作と書き出し

![プレイリストサイドバー](/assets/images/docs/player-playlist.png)

- **リストパネルを開く**
  コントロールバー右下の `📑 リスト` ボタンをクリックしてサイドバーを展開。
- **ドラッグで並び替え**
  リスト内で項目を上下にドラッグするだけで再生順を瞬時に変更。
- **M3U8 書き出し**
  UTF-8 形式の `.m3u8` プレイリストとして保存可能（相対パス保存のため別環境へ移動しても利用可能）。

---

## 📁 フォルダー一括スキャン

![フォルダー一括スキャン](/assets/images/docs/drag-files-and-folder.png)

シリーズ物のフォルダーをドラッグ＆ドロップすると、インポートダイアログが起動します：
- **再帰的ディープスキャン**: サブフォルダー内のメディアファイルを網羅的に抽出。
- **不要ファイルの除外**: ポスター画像や `.nfo` などの非メディアファイルを自動除外。
- **自然順ソート**: `第1話` → `第2話` → `第10話` の順にきれいに自動整列。

---

## 🕒 再生履歴とレジューム

- **正確なレジューム再生**: 前回の終了位置を正確に記録し、ダブルクリックですぐに続きから再生。
- **ファイル管理**: リストから直接エクスプローラーで表示したり、項目を整理できます。
""")

    write_doc(d, "settings.md", """---
title: "設定とトラブルシューティング"
description: "設定センターナビゲーション、ファイル関連付け、問題解決とフィードバック。"
order: 4
group: "ツールとシステム設定"
---

# ⚙️ 設定とトラブルシューティング

使用環境に合わせてプレーヤーをカスタマイズし、一般的な問題を解決します。

---

## 🎛️ 設定センターナビゲーション

![設定センター](/assets/images/docs/player-settings.png)

- **一般 (General)**: 言語切り替え（簡体字中国語、英語、日本語、韓国語）、多重起動制限、AppData ディレクトリへのショートカット。
- **再生 (Playback)**: ファイルを開いた時の挙動（置換 / 追加）、自動再生、レジューム記憶。
- **ショートカット (Hotkeys)**: キーボード操作の確認とカスタマイズ。
- **ファイル関連付け (Files)**: 動画ファイルの既定プレーヤー登録、右クリックメニューに `Play with Kyna Player` を追加。

![プレイリスト設定](/assets/images/docs/openfile-playlist-settings.png)

---

## 🛠️ トラブルシューティング

### 1. 4K/8K 動画の再生でコマ落ちやカクつきが発生する
- **GPU スケジューリング**: ノート PC 等のデュアル GPU 環境では、Windows 設定で Kyna Player を「高パフォーマンス (専用 GPU)」に指定してください。
- **ハードウェアアクセラレーション**: Direct3D 11 加速が有効になっているかご確認ください。
- **フィルター負荷**: Anime4K をお使いの場合は、GPU 性能に合わせて設定を調整してください。

### 2. 字幕の文字化け
- 字幕ファイルが `UTF-8` 形式で保存されているかご確認ください。

---

## 💬 フィードバックとログ

- **ログの取得**: 設定内の「AppData ディレクトリを開く」をクリックし、`logs/` フォルダ内の `kyna_player.log` を取得。
- **問題報告**: [GitHub Issues](https://github.com/fynx-dev/kyna-release/issues) から問題の内容とログを添えて送信してください。
""")
    print("[ja] Generated all 10 Japanese docs.")

# ==============================================================================
# KOREAN (ko)
# ==============================================================================
def gen_ko():
    d = clean_and_prepare('ko')

    write_doc(d, "getting-started.md", """---
title: "빠른 시작"
description: "Kyna Player의 핵심 기능, 인터페이스 레이아웃 및 미디어 재생 방법 안내."
order: 1
group: "시작 가이드"
---

# 🚀 빠른 시작

**Kyna Player**는 Windows 전용으로 제작된 현대적인 경량 비디오 플레이어입니다. GPU 하드웨어 가속 렌더링, 완전 오프라인 Whisper AI 자막, Anime4K 업스케일링 기술이 결합되어 가장 순수하고 몰입감 넘치는 감상 환경을 제공합니다.

---

## ✨ 핵심 기능

- **GPU 하드웨어 가속**
  Direct3D 11 하드웨어 디코딩과 VRAM 제로카피 직접 렌더링으로 CPU 점유율을 최소화하며 4K/8K 영상을 부드럽게 재생합니다.
- **HDR 톤 매핑**
  일반 SDR 모니터에서도 Dolby Vision 및 HDR10의 풍부한 색감을 자연스럽게 재현합니다.
- **오프라인 AI 자막**
  내장된 Whisper 음성 전사와 LLM 번역으로 100% 로컬에서 동작하여 개인정보를 완벽하게 보호합니다.
- **Anime4K 애니메이션 초해상화**
  선명한 윤곽선과 생생한 색상을 실시간으로 재구성하여 애니메이션 감상에 최적화되어 있습니다.
- **몰입형 미니멀 인터페이스**
  불필요한 요소를 최소화하여 컨트롤 바가 자동으로 사라지며, 풍부한 단축키와 마우스 조작을 지원합니다.

---

## 🖥️ 인터페이스 레이아웃 개요

![인터페이스 개요](/assets/images/docs/main-ui.png)

- **상단 타이틀 바**
  마우스를 상단으로 이동하면 나타나며 윈도우 고정 📌, 최소화, 전체화면, 닫기를 지원합니다.
- **비디오 뷰포트**
  클릭하여 재생/일시정지, 더블클릭으로 전체화면 전환, 마우스 휠로 볼륨을 조절합니다.
- **플로팅 컨트롤 바**
  재생 바, 호버 썸네일 미리보기, 재생 속도, 반복 모드 및 도구 바로가기를 제공합니다.
- **우측 사이드바**
  재생목록, 자막 트랙, 오디오 향상 및 비디오 필터를 빠르게 전환할 수 있습니다.

---

## 📂 미디어 열기 방법

![파일 열기 메뉴](/assets/images/docs/openfile-menu.png)

- **드래그 앤 드롭**
  동영상, 오디오 파일 또는 전체 시즌 폴더를 플레이어 창에 바로 끌어다 놓습니다.
- **단축키 열기**
  단축키 <kbd>O</kbd>를 눌러 Windows 파일 선택 창을 엽니다.
- **네트워크 스트리밍 URL**
  메뉴에서 "URL 열기"를 선택하고 HTTP/HTTPS, HLS (`.m3u8`) 또는 RTMP 라이브 스트림 주소를 입력합니다.
""")

    write_doc(d, "installation.md", """---
title: "설치 및 시스템 요구사항"
description: "시스템 요구 사양, 설치 및 업데이트, 앱 데이터 디렉터리 관리."
order: 2
group: "시작 가이드"
---

# 📦 설치 및 시스템 요구사항

## 💻 시스템 요구 사양

| 항목 | 최소 사양 | 권장 사양 |
| :--- | :--- | :--- |
| **운영체제 (OS)** | Windows 10 (64-bit) 1909+ | Windows 11 (22H2+) |
| **프로세서 (CPU)** | Intel Core i3 / AMD Ryzen 3 | Intel Core i5 / AMD Ryzen 5 이상 |
| **그래픽 (GPU)** | Direct3D 11 하드웨어 디코딩 지원 | DX12 / HEVC / AV1 / VP9 가속 지원 |
| **메모리 (RAM)** | 4 GB | 8 GB 이상 |

---

## 🚀 설치 및 업데이트

1. **설치 프로그램 다운로드**
   [GitHub Releases](https://github.com/fynx-dev/kyna-release/releases/latest)에서 `Kyna-Setup.exe`를 다운로드합니다.
2. **설치 마법사 실행**
   설치 프로그램을 실행하고 화면의 안내에 따라 설치를 완료합니다.
3. **업데이트**
   플레이어를 종료한 후 최신 설치 프로그램을 실행하여 덮어쓰기 설치합니다. 기존 설정과 다운로드한 AI 모델은 그대로 유지됩니다.

---

## 🗄️ 앱 데이터 및 캐시 디렉터리

사용자 데이터는 표준 AppData 폴더에 저장됩니다:
- **디렉터리 경로**: `%APPDATA%\\KynaPlayer\\` (**설정 → 일반**에서 한 번의 클릭으로 열 수 있습니다).
- **구조**:
  - `config.json`: 환경설정 및 단축키 바인딩.
  - `history.json`: 재생 기록 및 이어보기 위치.
  - `thumbnails\\`: 타임라인 썸네일 캐시.
  - `models\\`: 로컬 오프라인 Whisper AI 음성 모델.
""")

    write_doc(d, "playback.md", """---
title: "재생 제어 및 단축키 탐색"
description: "핵심 재생 제어, 정밀 탐색, 속도 및 반복 모드, 주요 단축키 안내."
order: 1
group: "재생 및 화질"
---

# ⏯️ 재생 제어 및 단축키 탐색

Kyna Player는 밀리초 단위의 정밀한 탐색과 전면 키보드 제어를 지원하는 고성능 재생 엔진을 갖추고 있습니다.

---

## 🎮 주요 단축키 안내

| 동작 | 기본 단축키 | 마우스 동작 | 설명 |
| :--- | :--- | :--- | :--- |
| **재생 / 일시정지** | <kbd>Space</kbd> | 화면 중앙 클릭 | 재생 및 일시정지 상태 전환 |
| **재생 정지** | <kbd>S</kbd> | 컨트롤 바 정지 버튼 | 디코딩을 중지하고 처음 위치로 리셋 |
| **전체화면 전환** | <kbd>F</kbd> | 화면 더블클릭 | 전체화면 모드 전환 |
| **전체화면/레이어 닫기** | <kbd>Escape</kbd> | - | 전체화면 종료 또는 열린 팝업 창 닫기 |
| **프레임 단위 전진** | <kbd>.</kbd> | - | 일시정지 상태에서 정확히 1프레임 앞으로 이동 |
| **볼륨 조절** | <kbd>↑</kbd> / <kbd>↓</kbd> | 마우스 휠 스크롤 | 볼륨 조절 |
| **음소거 전환** | <kbd>M</kbd> | 볼륨 아이콘 클릭 | 음소거 / 음소거 해제 |
| **파일 열기** | <kbd>O</kbd> | 열기 버튼 클릭 | 파일 선택 대화상자 표시 |
| **성능 통계 OSD** | <kbd>Tab</kbd> | - | 실시간 FPS, 드롭 프레임, 비트레이트, 렌더링 지연시간 표시 |

---

## ⏳ 타임라인 및 호버 썸네일

![타임라인 썸네일 미리보기](/assets/images/features/thumbnails.webp)

- **호버 썸네일**
  재생 바 위로 마우스를 올리면 해당 장면의 영상과 타임스탬프를 실시간으로 미리 볼 수 있습니다.
- **단계별 탐색**
  방향키 <kbd>→</kbd> / <kbd>←</kbd>를 눌러 앞뒤로 신속하게 이동합니다.

---

## 🔁 반복 및 재생 정책

컨트롤 바 우측의 반복 아이콘을 클릭하여 모드를 전환합니다:
- 🔁 **전체 반복**: 목록 끝까지 재생 후 처음부터 다시 재생합니다.
- 🔂 **한 곡 반복**: 현재 영상을 무한 반복합니다.
- 🔀 **셔플 재생**: 목록의 항목을 무작위 순서로 재생합니다.
- ➡️ **순차 재생**: 목록 끝에 도달하면 자동으로 정지합니다.
""")

    write_doc(d, "video-enhance.md", """---
title: "화질 향상 및 비디오 설정"
description: "Direct3D 11 하드웨어 가속, 적응형 로컬 디테일 향상, Anime4K 애니메이션 초해상화."
order: 2
group: "재생 및 화질"
---

# 🎨 화질 향상 및 비디오 설정

Direct3D 하드웨어 렌더링 파이프라인을 기반으로 다채로운 화면 조정과 AI 초해상화 기능을 제공합니다.

---

## 🚀 비디오 렌더링 및 하드웨어 가속

- **Direct3D 11 가속 렌더링**
  GPU 하드웨어 디코딩과 VRAM 제로카피 직접 표시로 고비트레이트 4K/8K 영상도 극히 낮은 CPU 점유율로 처리합니다.
- **3가지 화면 채우기 모드**
  - **Contain (비율 유지)**: 원본 비율을 유지하며 레터박스를 표시합니다.
  - **Fill (늘려 채우기)**: 화면 전체에 맞게 늘려 채웁니다.
  - **Cover (잘라 채우기)**: 레터박스 없이 비율에 맞춰 확대하고 여백을 잘라냅니다.

---

## ✨ 적응형 로컬 디테일 향상

![화질 필터 및 디테일 향상](/assets/images/docs/dlss5.png)

- **적응형 향상 (Adaptive enhancement)**
  실시간 1× 로컬 디테일 및 대비를 강화하여 부드러운 색감을 보존하면서 윤곽선과 암부 디테일을 또렷하게 개선합니다.
- **연구용 향상 (Research Enhancement)**
  초정밀 영상 소스를 위한 고급 신경망 업스케일링 필터 확장을 제공합니다.

---

## 🌸 Anime4K 애니메이션 초해상화

![Anime4K 애니메이션 초해상화](/assets/images/docs/anime4K.png)

- **애니메이션 2배 초해상화**
  2D 애니메이션에 특화된 초해상화 셰이더(`Anime4K CNN x2 S` 및 `Anime4K DTD x2`)가 내장되어 있습니다.
- **윤곽선 재구성 및 안티에일리어싱**
  압축 노이즈를 제거하고 또렷한 선을 재구성하여 2K/4K 대형 모니터에서도 선명한 애니메이션을 감상할 수 있습니다.
""")

    write_doc(d, "subtitles.md", """---
title: "자막 관리 및 스타일 외관"
description: "내장/외부 자막 로드, 메인·서브 듀얼 자막 동시 표시, 스타일 외관 설정."
order: 1
group: "자막 및 AI 랩"
---

# 💬 자막 관리 및 스타일 외관

Kyna Player는 강력한 자막 렌더링 엔진을 탑재하여 듀얼 자막 동시 표시와 세밀한 스타일 설정을 지원합니다.

---

## 📑 자막 로드 및 전환

![자막 메뉴 및 듀얼 자막 설정](/assets/images/docs/subtitle-menu.png)

- **컨트롤 바 및 메뉴**
  자막 아이콘을 클릭하거나 우클릭 메뉴를 통해 주 자막과 보조 자막 트랙을 즉시 지정할 수 있습니다.
- **외부 자막 드래그 앤 드롭**
  `.srt`, `.ass`, `.ssa`, `.vtt` 파일을 창 안으로 끌어다 놓기만 하면 즉시 로드됩니다.
- **동명 파일 자동 연결**
  동영상과 같은 폴더에 위치한 동일한 이름의 자막(예: `movie.ko.srt`)은 자동으로 연결됩니다.

---

## 👥 듀얼 자막 시스템 (Dual Subtitles)

외국어 학습 및 다국어 대조 감상에 최적화:
- **주 자막 (Primary Subtitle)**: 일반적으로 모국어 번역(큰 글꼴).
- **보조 자막 (Secondary Subtitle)**: 원어 대사(작은 글꼴).
- **독립 글꼴 크기 조절**: 주 자막(13~48px)과 보조 자막(13~40px)의 크기를 각각 개별 조절할 수 있습니다.

---

## 🎨 스타일 설정 및 온라인 검색

- **글꼴 및 외관 커스텀**
  글꼴 패밀리, 크기, 굵은 테두리 및 반투명 배경 상자를 자유롭게 지정할 수 있습니다.
- **온라인 자막 확장 검색**
  플러그인 엔진을 통해 동영상 해시값으로 일치하는 자막을 검색하여 원클릭으로 다운로드 및 적용합니다.
""")

    write_doc(d, "ai-lab.md", """---
title: "AI 음성 전사 및 번역"
description: "로컬 오프라인 Whisper 음성 인식, 대형 언어 모델 (LLM) 문맥 자막 번역."
order: 2
group: "자막 및 AI 랩"
---

# 🤖 AI 음성 전사 및 번역

자막이 없는 영상도 걱정 없습니다! Kyna Player는 음성 인식부터 고품질 이중언어 자막 생성까지 전 과정을 자동화한 AI 자막 워크플로우를 제공합니다.

---

## ⚡ 핵심 파이프라인

```
[ 오디오 추출 ] ──> [ 로컬 Whisper 오프라인 인식 ] ──> [ LLM 문맥 번역 ] ──> [ 듀얼 자막 실시간 적용 ]
```

![Whisper 랩 워크플로우](/assets/images/docs/whisper-lab-workflow.png)

- **100% 오프라인 개인정보 보호**
  Whisper 음성 인식은 로컬 GPU 또는 CPU에서 완전히 실행되며 오디오를 외부로 업로드하지 않습니다.
- **문맥 인식 LLM 번역**
  DeepSeek, ChatGPT, Claude 또는 로컬 Ollama와 연동하여 영상의 흐름에 맞는 자연스러운 번역을 생성합니다.

![Whisper 랩 번역](/assets/images/docs/whisper-lab-translate.png)

---

## 🧠 Whisper 모델 사양

| 모델 크기 | VRAM 사용량 | 전사 속도 (RTX 4060) | 정확도 | 추천 용도 |
| :--- | :--- | :--- | :--- | :--- |
| **Base** | ~1.0 GB | ~20x 초고속 | 양호 | 숏폼 영상, 또렷한 영어/한국어 대화 |
| **Small** | ~1.8 GB | ~12x 고속 | 우수 *(권장)* | 드라마, 애니메이션 일상 감상 |
| **Medium** | ~3.5 GB | ~6x 안정 | 매우 높음 | 학술 강의, 다국어 혼합 음성 |
| **Large-v3** | ~6.0 GB | ~3x 안정 | 최고 수준 정확도 | 배경음악이 복잡한 영상, 고정밀 작업 |
""")

    write_doc(d, "audio-and-tools.md", """---
title: "오디오 및 사운드 향상"
description: "다중 오디오 트랙 전환, 야간 모드 (DRC), 음성 향상, 싱크 미세조절."
order: 1
group: "도구 및 시스템 설정"
---

# 🔊 오디오 및 사운드 향상

탁월한 비디오 재생 외에도 실용적인 오디오 DSP 툴킷을 탑재하고 있습니다.

---

## 🎧 오디오 향상 및 싱크 조절

- **빠른 오디오 트랙 전환**
  컨트롤 바에서 오디오 트랙을 즉시 전환할 수 있으며, 다채널 무손실 오디오를 기본 지원합니다.

![오디오 트랙 전환](/assets/images/docs/audio-tracks.png)

- **🌙 야간 모드 (동적 범위 압축 / DRC)**
  갑작스러운 폭발음을 억제하고 작은 대사를 또렷하게 만들어주며, **실시간 파형 비교 (Live waveform)**를 제공합니다.

![야간 모드 및 실시간 파형](/assets/images/docs/audio-night-mode.png)

- **🗣️ 음성 향상 (Voice enhance)**
  스테레오 중앙 대사를 자연스럽게 증폭하며, **40Hz~16kHz 실시간 대역별 에너지 스펙트럼**으로 확인 가능합니다.

![음성 향상 및 스펙트럼](/assets/images/docs/audio-void-enhance.png)

- **⏱️ 싱크 미세조절**
  `-100ms` / `리셋` / `+100ms` 딜레이 조절로 영상과 음성의 불일치를 손쉽게 해결합니다.
""")

    write_doc(d, "dlna.md", """---
title: "DLNA 무선 전송"
description: "스마트 TV 대화면 무선 전송 (DMC) 및 로컬 수신 (DMR) 양방향 기능 안내."
order: 2
group: "도구 및 시스템 설정"
---

# 📺 DLNA 무선 전송

Kyna Player는 완전한 DLNA / UPnP 미디어 전송을 지원하며, **대화면 TV 무선 전송 (DMC)** 및 **로컬 수신 (DMR)** 양방향 기능을 제공합니다.

---

## 📡 1. 대화면 TV 무선 전송 (DMC)

PC에 저장된 고화질 영상을 거실의 스마트 TV나 빔프로젝터로 무선 전송하여 대화면으로 감상합니다.

![DLNA TV 전송 워크벤치](/assets/images/docs/dlna-cast-to-tv.png)

### 단계별 안내
1. **전송 워크벤치 열기**
   영상 재생 중 컨트롤 바 우측의 `📺 전송` 아이콘을 클릭합니다.
2. **대상 기기 선택**
   로컬 네트워크의 DLNA 기기를 자동 검색합니다. 목록에서 스마트 TV를 클릭합니다.
3. **대화면 즉시 재생**
   **연결 / 전송**을 클릭하면 TV에서 즉시 재생이 시작됩니다.

### PC 동기화 리모컨 제어
- **재생 및 탐색**: PC에서 일시정지하거나 재생 바를 이동하면 TV 화면이 실시간으로 동기화됩니다.
- **볼륨 조절**: PC에서 대화면 볼륨 및 음소거를 직접 제어합니다.
- **연결 해제**: 언제든 "연결 해제"를 클릭하여 로컬 재생으로 복귀할 수 있습니다.

---

## 📥 2. 로컬 미디어 수신 (DMR)

Kyna Player를 DLNA 수신기로 동작시켜 스마트폰이나 태블릿의 미디어를 PC 화면으로 수신합니다.

![DLNA 수신 알림](/assets/images/docs/dlna-recv-cast.png)

- **수신 활성화**
  컨트롤 바에서 **전송 수신** 버튼을 클릭합니다.
- **모바일에서 캐스트**
  스마트폰 영상 앱에서 "TV 화면 전송"을 누르고 **Kyna Player**를 선택하면 PC 화면으로 바로 스트리밍됩니다.

---

## 🛠️ 네트워크 및 방화벽 설정

- **동일한 로컬 네트워크**
  PC와 TV가 동일한 공유기에 연결되어 있는지 확인하세요 (5GHz Wi-Fi 또는 유선 LAN 권장).
- **Windows 방화벽 허용**
  처음 사용 시 방화벽 알림이 뜨면 개인 및 공용 네트워크 액세스를 모두 허용해야 합니다.
- **AP 격리 확인**
  기기가 검색되지 않을 경우 공유기 설정에서 "AP 격리 (AP Isolation)"가 비활성화되어 있는지 확인하세요.
""")

    write_doc(d, "playlist.md", """---
title: "재생목록 및 파일 관리"
description: "재생목록 관리, M3U8 내보내기, 폴더 일괄 스마트 스캔, 최근 재생 기록."
order: 3
group: "도구 및 시스템 설정"
---

# 📑 재생목록 및 파일 관리

방대한 분량의 시리즈 드라마, 애니메이션 및 음악 컬렉션을 효율적으로 관리할 수 있습니다.

---

## ➕ 재생목록 조작 및 내보내기

![재생목록 사이드바](/assets/images/docs/player-playlist.png)

- **목록 패널 열기**
  컨트롤 바 우측 하단의 `📑 목록` 버튼을 클릭하여 사이드바를 펼칩니다.
- **드래그하여 순서 변경**
  목록 내에서 항목을 위아래로 끌어다 놓기만 하면 즉시 재생 순서가 변경됩니다.
- **M3U8 내보내기**
  상대 경로로 저장되는 표준 UTF-8 `.m3u8` 파일로 내보낼 수 있어 다른 기기로 이동해도 그대로 유지됩니다.

---

## 📁 폴더 일괄 스마트 스캔

![폴더 일괄 스캔](/assets/images/docs/drag-files-and-folder.png)

시리즈 폴더를 창으로 끌어다 놓으면 가져오기 창이 열립니다:
- **재귀적 하위 스캔**: 하위 폴더의 모든 미디어 파일을 빠짐없이 검색합니다.
- **불필요한 파일 제외**: 포스터 이미지, `.nfo` 등의 비미디어 파일을 자동 제외합니다.
- **자연수 정렬**: `1화` → `2화` → `10화` 순서로 깔끔하게 자동 정렬됩니다.

---

## 🕒 최근 재생 기록 및 이어보기

- **정확한 이어보기**: 이전 종료 시점을 기록하여 더블클릭으로 바로 이어볼 수 있습니다.
- **파일 관리**: 목록에서 바로 파일 위치를 열거나 항목을 정리할 수 있습니다.
""")

    write_doc(d, "settings.md", """---
title: "환경설정 및 문제 해결"
description: "설정 센터 안내, Windows 파일 연결, 문제 해결 및 피드백."
order: 4
group: "도구 및 시스템 설정"
---

# ⚙️ 환경설정 및 문제 해결

하드웨어 환경에 맞춰 플레이어를 최적화하고 재생 문제를 빠르게 해결할 수 있습니다.

---

## 🎛️ 설정 센터 안내

![설정 센터](/assets/images/docs/player-settings.png)

- **일반 (General)**: 다국어 전환(간체 중국어, 영어, 일본어, 한국어), 다중 실행 제한, AppData 폴더 바로가기.
- **재생 (Playback)**: 파일 열기 동작(교체 / 추가), 자동 재생 정책 및 재생 기록 기억.
- **단축키 (Hotkeys)**: 키보드 단축키 바인딩 확인 및 커스텀.
- **파일 연결 (Files)**: 비디오 확장자 기본 연결 등록 및 우클릭 메뉴에 `Play with Kyna Player` 추가.

![재생목록 설정](/assets/images/docs/openfile-playlist-settings.png)

---

## 🛠️ 자주 묻는 문제 해결

### 1. 4K/8K 영상 재생 시 끊김 또는 프레임 드롭 발생
- **GPU 설정**: 노트북 듀얼 그래픽 환경인 경우 Windows 설정에서 Kyna Player를 "고성능 외장 GPU"로 지정하세요.
- **하드웨어 가속**: Direct3D 11 하드웨어 가속이 켜져 있는지 확인하세요.
- **필터 부하**: Anime4K를 사용하는 경우 GPU 사양에 맞게 단계를 조절하세요.

### 2. 자막 글자 깨짐 현상
- 자막 파일이 `UTF-8` 인코딩으로 저장되어 있는지 확인하세요.

---

## 💬 문제 피드백 및 로그

- **로그 확인**: 설정에서 "AppData 디렉터리 열기"를 클릭하고 `logs/` 폴더에서 `kyna_player.log` 파일을 확인하세요.
- **이슈 제출**: [GitHub Issues](https://github.com/fynx-dev/kyna-release/issues)에서 문제 내용과 로그를 제출해주세요.
""")
    print("[ko] Generated all 10 Korean docs.")

if __name__ == '__main__':
    gen_en()
    gen_ja()
    gen_ko()
    print("All 3 languages (en, ja, ko) generated successfully!")
