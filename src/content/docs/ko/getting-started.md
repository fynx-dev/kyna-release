---
title: "빠른 시작"
description: "Kyna Player의 주요 특징, 하드웨어 가속 비디오 렌더링, Anime4K 초해상도 및 로컬 Whisper AI 자막 기능 소개."
order: 1
group: "초보자 가이드"
---

# 빠른 시작

**Kyna Player**에 오신 것을 환영합니다! Windows 10 및 11 환경에 완벽하게 최적화된 초경량 고성능 미디어 플레이어로, Direct3D 11 하드웨어 가속 렌더링, 100% 오프라인 로컬 Whisper AI 음성 자막 전사, Anime4K 초해상도 화질 향상 및 DLSS 5 지원을 통해 최고의 시청각 경험을 선사합니다.

---

## ✨ 핵심 기능 및 하이라이트

### 🎬 차세대 Direct3D 11 GPU 렌더링 파이프라인
- **하드웨어 가속 (D3D11VA)**
  디코딩 연산을 GPU에 완전히 위임하여, 4K 및 8K 초고화질 HEVC, AV1, VP9 영상을 CPU 점유율 5% 미만으로 부드럽게 재생합니다.
- **HDR 톤 매핑**
  정교한 Reinhard 및 Mobius 알고리즘을 내장하여, 일반 SDR 디스플레이에서도 Dolby Vision 및 HDR10의 풍부한 명암과 색감을 왜곡 없이 자연스럽게 재현합니다.
- **실시간 성능 진단 OSD (F12)**
  프레임 렌더링 시간(ms), 프레임 드롭 수, VRAM 사용량을 화면에 오버레이로 즉시 확인 가능합니다.

### 🤖 100% 로컬 오프라인 Whisper AI 자막 랩
- **완전한 오프라인 음성 인식**
  로컬 Whisper 모델(`tiny`, `base`, `small`, `medium`, `large-v3`)을 내장하여 외부 서버 전송 없이 안전하게 고정밀 타임스탬프 자막을 생성합니다.
- **LLM 문맥 인식 자막 번역**
  DeepSeek, OpenAI GPT-4o, Claude, 로컬 Ollama 모델과 연동하여 대화 문맥을 고려한 자연스러운 이중 언어 자막을 제공합니다.
- **Silero VAD 무음 필터링**
  배경음악과 효과음을 자동 분리하여 무음 구간에서의 AI 환각(Hallucination) 텍스트 생성을 차단합니다.

### 🎨 Anime4K 및 신경망 초해상도 (DLSS 5)
- **실시간 애니메이션 화질 향상**
  2D 애니메이션의 윤곽선을 또렷하게 복원하고 풍부한 색감을 4K 해상도로 실시간 업스케일링합니다.
- **Compute Shader 범용 호환**
  NVIDIA RTX, AMD Radeon, Intel Arc 등 다양한 GPU에서 안정적으로 구동됩니다.
- **동적 프레임 예산 관리**
  GPU 부하가 급증할 경우 자동으로 셰이더 부하를 조절하여 60 FPS의 매끄러운 재생을 보장합니다.

### 🎛️ 모던한 보더리스 UI 및 직관적인 단축키
- **프레임리스 몰입형 디자인**
  자동 숨김 제어바, 타임라인 썸네일 미리보기, 우측 슬라이드 드로어 패널 지원.
- **듀얼 자막 시스템**
  기본 자막과 보조 자막을 화면에 동시에 표시하며, 폰트 및 스타일을 독립적으로 설정 가능.
- **DLNA / UPnP 무선 전송**
  로컬 미디어를 스마트 TV, 프로젝터, Apple TV로 무선 스트리밍 지원.

---

## 🧭 문서 가이드

- 📦 [설치 및 시스템 요구사항](/docs/ko/installation/): 권장 사양, SHA-256 무결성 검증 및 설치 가이드.
- 🖥️ [인터페이스 둘러보기](/docs/ko/getting-started/interface-overview/): 뷰포트, 타이틀바, 제어바 및 사이드 드로어 안내.
- 📂 [미디어 열기](/docs/ko/getting-started/opening-media/): 폴더 일괄 스캔, M3U 재생목록, 네트워크 스트림 재생.
- ⏯️ [기본 재생 제어](/docs/ko/getting-started/basic-playback/): 재생/일시정지, 타임라인 탐색, 볼륨 증폭.
- 💬 [자막 및 듀얼 자막](/docs/ko/subtitles/embedded-tracks/): 내장 트랙 선택, 온라인 자막 검색, 스타일 설정.
- 🤖 [AI 자막 연구실](/docs/ko/subtitle-ai/overview/): Whisper 전사 및 LLM 번역 파이프라인.
