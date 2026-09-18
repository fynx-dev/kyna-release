---
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
