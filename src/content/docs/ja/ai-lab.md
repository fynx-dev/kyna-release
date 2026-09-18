---
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
