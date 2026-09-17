---
title: "설치 안내"
description: "Windows 환경에서의 Kyna Player 권장 시스템 사양, SHA-256 해시 검증, 설치, 업데이트 및 삭제 가이드."
order: 2
group: "초보자 가이드"
---

## 시스템 요구사항

안정적인 4K / HDR 영상 디코딩 및 AI 자막 생성을 위해 다음 시스템 사양을 권장합니다:

| 구성 요소 | 최소 사양 | 권장 사양 |
| :--- | :--- | :--- |
| **운영체제** | Windows 10 (64-bit) 1909 이상 | Windows 11 (22H2 이상) |
| **프로세서 (CPU)** | Intel Core i3 / AMD Ryzen 3 | Intel Core i5 / AMD Ryzen 5 이상 |
| **그래픽카드 (GPU)** | DX11 하드웨어 디코딩 지원 | DX12 / HEVC / AV1 / VP9 하드웨어 가속 지원 |
| **메모리 (RAM)** | 4 GB | 8 GB 이상 |

## 설치 단계

1. 공식 [GitHub Releases](https://github.com/fynx-dev/kyna-release/releases/latest) 페이지에서 최신 `Kyna-Setup.exe` 설치 파일 및 `SHA256SUMS` 체크섬 파일을 다운로드합니다.
2. (선택 사항) PowerShell 터미널에서 해시 무결성을 검증합니다:
   ```powershell
   Get-FileHash .\Kyna-Setup.exe -Algorithm SHA256
   ```
   계산된 SHA-256 값이 공식 체크섬과 일치하는지 확인합니다.
3. `Kyna-Setup.exe`를 실행하고 설치 마법사의 안내에 따라 설치를 완료합니다.
4. 시작 메뉴 또는 바탕화면 바로가기에서 Kyna Player를 실행합니다.

## 최초 실행 안내

- **하드웨어 가속 및 톤 매핑**
  최초 실행 시 시스템 GPU 성능을 자동 감지하여 Direct3D 11 하드웨어 가속 및 HDR-to-SDR 톤 매핑이 기본 활성화됩니다.
- **Whisper AI 모델 다운로드**
  설치 프로그램 용량 최적화를 위해 대용량 모델 파일은 기본 번들되지 않습니다. "자막 → 로컬 AI" 패널에서 원클릭으로 다운로드하여 사용할 수 있습니다.

## 업데이트 및 제거

- **업데이트**
  실행 중인 Kyna Player를 종료한 후 최신 `Kyna-Setup.exe`를 덮어쓰기 설치합니다. 기존 사용자 설정과 AI 모델은 안전하게 유지됩니다.
- **제거**
  Windows "설정 → 설치된 앱"에서 깔끔하게 제거할 수 있습니다.
