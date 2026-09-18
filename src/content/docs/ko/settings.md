---
title: "환경설정 및 문제 해결"
description: "설정 센터 안내, Windows 파일 연결, 문제 해결 및 피드백."
order: 4
group: "도구 및 시스템 설정"
---

# ⚙️ 환경설정 및 문제 해결

하드웨어 환경에 맞춰 플레이어를 최적화하고 재생 문제를 빠르게 해결할 수 있습니다.

---

## 🎛️ 설정 센터 안내

![설정 센터](/assets/images/docs/player-settings.png)

- **일반 (General)**: 다국어 전환(간체 중국어, 영어, 일본어, 한국어), 다중 실행 제한, AppData 폴더 바로가기.
- **재생 (Playback)**: 파일 열기 동작(교체 / 추가), 자동 재생 정책 및 재생 기록 기억.
- **단축키 (Hotkeys)**: 키보드 단축키 바인딩 확인 및 커스텀.
- **파일 연결 (Files)**: 비디오 확장자 기본 연결 등록 및 우클릭 메뉴에 `Play with Kyna Player` 추가.

![재생목록 설정](/assets/images/docs/openfile-playlist-settings.png)

---

## 🛠️ 자주 묻는 문제 해결

### 1. 4K/8K 영상 재생 시 끊김 또는 프레임 드롭 발생
- **GPU 설정**: 노트북 듀얼 그래픽 환경인 경우 Windows 설정에서 Kyna Player를 "고성능 외장 GPU"로 지정하세요.
- **하드웨어 가속**: Direct3D 11 하드웨어 가속이 켜져 있는지 확인하세요.
- **필터 부하**: Anime4K를 사용하는 경우 GPU 사양에 맞게 단계를 조절하세요.

### 2. 자막 글자 깨짐 현상
- 자막 파일이 `UTF-8` 인코딩으로 저장되어 있는지 확인하세요.

---

## 💬 문제 피드백 및 로그

- **로그 확인**: 설정에서 "AppData 디렉터리 열기"를 클릭하고 `logs/` 폴더에서 `kyna_player.log` 파일을 확인하세요.
- **이슈 제출**: [GitHub Issues](https://github.com/fynx-dev/kyna-release/issues)에서 문제 내용과 로그를 제출해주세요.
