---
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
- **디렉터리 경로**: `%APPDATA%\KynaPlayer\` (**설정 → 일반**에서 한 번의 클릭으로 열 수 있습니다).
- **구조**:
  - `config.json`: 환경설정 및 단축키 바인딩.
  - `history.json`: 재생 기록 및 이어보기 위치.
  - `thumbnails\`: 타임라인 썸네일 캐시.
  - `models\`: 로컬 오프라인 Whisper AI 음성 모델.
