---
title: "AI 语音转录与翻译"
description: "本地离线 Whisper 语音识别、大模型上下文字幕翻译与结果导出全流程。"
order: 2
group: "字幕与 AI 实验室"
---

# 🤖 AI 语音转录与翻译

告别无字幕“生肉”困扰！Kyna Player 支持完整的 AI 字幕工作流，实现从音频识别到高质量双语字幕的全流程自动化。

---

## ⚡ 核心流水线

```
[ 提取视频音频 ] ──> [ 本地 Whisper 离线识别 ] ──> [ 大模型上下文翻译 ] ──> [ 实时双语字幕挂载 ]
```

![whisper_lab_workflow](/assets/images/docs/whisper-lab-workflow.png)

- **100% 本地离线隐私保护**
  Whisper 语音识别完全在本地 GPU 或 CPU 上运行，音频零上传。
- **大模型语境感知翻译**
  支持接入 DeepSeek、ChatGPT、Claude 或本地 Ollama，结合影视前后文输出地道译文。

![whisper_lab_translate](/assets/images/docs/whisper-lab-translate.png)

---

## 🧠 Whisper 模型规格推荐

| 模型尺寸 | 显存占用 | 识别速度 (RTX 4060) | 准确度 | 推荐场景 |
| :--- | :--- | :--- | :--- | :--- |
| **Base** | ~1.0 GB | ~20x 极速 | 优良 | 日常短视频、清晰英语/中文对白 |
| **Small** | ~1.8 GB | ~12x 高速 | 优秀 *(综合推荐)* | 影视剧集、动漫番剧日常使用 |
| **Medium** | ~3.5 GB | ~6x 稳定 | 极高 | 学术讲座、多语种混合与方言 |
| **Large-v3** | ~6.0 GB | ~3x 稳定 | 最高顶尖水准 | 背景音乐复杂、高精度需求片源 |

