---
title: "データ・キャッシュ・ログ"
description: "設定ファイル、サムネイルキャッシュ、AI モデル保存先、診断ログの場所。"
order: 3
group: "設定・システム統合・トラブルシューティング"
---

# データ・キャッシュ・ログ

Kyna Player はすべての設定、キャッシュ、ログを Windows の標準ユーザーデータ領域に整然と保存します。

---

## 📂 AppData フォルダの場所

```plaintext
%APPDATA%\KynaPlayer\
(絶対パス: C:\Users\<ユーザー名>\AppData\Roaming\KynaPlayer\)
```

> [!TIP]
> **設定 → 一般** の **「📂 AppData フォルダを開く」** ボタンをクリックすると直接開けます。

---

## 🌲 フォルダ構成

```plaintext
AppData\Roaming\KynaPlayer\
├── 📄 config.json           # プレイヤーの設定とショートカット割り当て
├── 📄 history.json          # 再生履歴とレジュームタイムスタンプ
├── 📁 thumbnails\           # タイムラインサムネイルキャッシュ
├── 📁 subtitles\            # ダウンロードしたオンライン字幕
├── 📁 models\               # ローカル Whisper 音声認識モデル
└── 📁 logs\                 # 診断ログ (kyna_player.log)
```

---

## 🧹 キャッシュの削除と初期化

- **キャッシュ削除**
  設定の「一時キャッシュを削除」をクリックするとディスク容量を安全に解放できます。
- **初期化**
  プレイヤーを終了した状態で `config.json` を削除すると、出荷時デフォルト設定にリセットされます。
