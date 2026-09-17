---
title: "インストール"
description: "Windows 環境における Kyna Player のシステム推奨スペック、SHA-256 ハッシュ検証、インストール、アップデートおよびアンインストール手順。"
order: 2
group: "ビギナーズガイド"
---

## システム要件

快適な 4K / HDR 映像再生および AI 字幕生成を行うため、以下のシステムスペックを推奨します：

| 項目 | 最小要件 | 推奨スペック |
| :--- | :--- | :--- |
| **OS** | Windows 10 (64-bit) 1909 以降 | Windows 11 (22H2 以降) |
| **CPU** | Intel Core i3 / AMD Ryzen 3 | Intel Core i5 / AMD Ryzen 5 以上 |
| **GPU** | DX11 ハードウェアデコード対応 | DX12 / HEVC / AV1 / VP9 ハードウェアアクセラレーション対応 |
| **RAM** | 4 GB | 8 GB 以上 |

## インストール手順

1. 公式 [GitHub Releases](https://github.com/fynx-dev/kyna-release/releases/latest) から最新のインストーラー `Kyna-Setup.exe` と `SHA256SUMS` 検証ファイルをダウンロードします。
2. （任意）PowerShell でハッシュ値を検証します：
   ```powershell
   Get-FileHash .\Kyna-Setup.exe -Algorithm SHA256
   ```
   出力されたハッシュ値が公式公開値と一致することを確認します。
3. `Kyna-Setup.exe` を実行し、画面の指示に従ってインストールを完了します。
4. スタートメニューまたはデスクトップのショートカットから Kyna Player を起動します。

## 初回起動時のヒント

- **ハードウェアデコード & トーンマッピング**
  初回起動時に GPU 性能を自動検出し、Direct3D 11 ハードウェアアクセラレーションと HDR-SDR トーンマッピングが有効化されます。
- **Whisper AI モデル**
  インストーラー本体に巨大なモデルファイルは含まれていません。「字幕 → ローカル AI」パネルからワンクリックでダウンロードまたは手動配置できます。

## 更新とアンインストール

- **アップデート**
  実行中の Kyna Player を終了し、新しい `Kyna-Setup.exe` を実行して上書きインストールしてください。設定やダウンロード済み AI モデルはそのまま保持されます。
- **アンインストール**
  Windows の「設定 → インストールされているアプリ」から安全にアンインストールできます。
