---
title: "LLM Subtitle Translation"
description: "Translate subtitles with natural nuance using DeepSeek, OpenAI, Claude, or local Ollama models."
order: 3
group: "Subtitle AI & Translation"
---

# LLM Subtitle Translation

Unlike traditional word-by-word machine translation, Kyna Player uses **sliding context windows** to provide LLMs with preceding and subsequent dialogue lines for natural, idiom-aware translations.

---

## 🔌 Supported Translation Engines

| Engine | Models | Features |
| :--- | :--- | :--- |
| **DeepSeek** *(Recommended)* | `deepseek-chat`, `deepseek-reasoner` | Exceptional value, localized phrasing |
| **OpenAI** | `gpt-4o`, `gpt-4o-mini` | Strong multi-language reasoning |
| **Anthropic Claude** | `claude-3-5-sonnet` | Natural literary flair & dialogue flow |
| **Ollama (Local)** | `qwen2.5`, `llama3.1`, `gemma2` | 100% offline, free, private |
| **Custom Endpoint** | Any OpenAI-compatible API | Reverse proxies and enterprise gateways |

---

## 💬 Bilingual Layout Options

- **Bilingual Top/Bottom**
  Target translation on top, original speech on bottom.
- **Target Translation Only**
  Clean single-language experience.
- **Export Standards**
  Export directly as `.srt` or `.ass` subtitle files.
