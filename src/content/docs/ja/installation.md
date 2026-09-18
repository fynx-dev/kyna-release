---
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
- **ディレクトリパス**: `%APPDATA%\KynaPlayer\`（**設定 → 一般** からワンクリックで開けます）。
- **構造**:
  - `config.json`: 設定とキーバインド。
  - `history.json`: 再生履歴とレジューム情報。
  - `thumbnails\`: タイムラインサムネイルのキャッシュ。
  - `models\`: ローカルの Whisper AI 音声認識モデル。
