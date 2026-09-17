---
title: "데이터, 캐시 및 로그"
description: "설정 파일, 썸네일 캐시, AI 모델 저장 위치 및 진단 로그 관리."
order: 3
group: "설정, 시스템 연동 및 문제 해결"
---

# 데이터, 캐시 및 로그

Kyna Player는 모든 사용자 설정, 캐시, 로그를 Windows 표준 사용자 데이터 디렉터리에 체계적으로 저장합니다.

---

## 📂 AppData 폴더 위치

```plaintext
%APPDATA%\KynaPlayer\
(절대 경로: C:\Users\<사용자명>\AppData\Roaming\KynaPlayer\)
```

> [!TIP]
> **설정 → 일반**의 **"📂 AppData 폴더 열기"** 버튼을 클릭하면 즉시 열립니다.

---

## 🌲 폴더 구조

```plaintext
AppData\Roaming\KynaPlayer\
├── 📄 config.json           # 사용자 설정 및 단축키 바인딩
├── 📄 history.json          # 재생 기록 및 이어보기 타임스탬프
├── 📁 thumbnails\           # 타임라인 썸네일 캐시
├── 📁 subtitles\            # 다운로드된 온라인 자막
├── 📁 models\               # 로컬 Whisper 음성 모델 파일
└── 📁 logs\                 # 진단 로그 (kyna_player.log)
```

---

## 🧹 캐시 정리 및 초기화

- **캐시 정리**
  설정에서 "임시 캐시 정리"를 클릭하여 디스크 공간을 안전하게 확보.
- **초기화**
  플레이어를 종료한 상태에서 `config.json`을 삭제하면 공장 초기화 설정으로 복원됩니다.
