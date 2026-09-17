import type { InstallCopy, LandingCopy } from './types';

export const ko: LandingCopy = {
  locale: 'ko', direction: 'ltr',
  seo: { title: 'Kyna Player — 당신의 영화, 당신의 공간.', description: 'Kyna Player는 로컬 재생, 자막, 오디오 제어 및 TV 캐스팅에 최적화된 초고속 Windows 미디어 플레이어입니다.' },
  skip: '본문으로 스킵',
  navigation: { features: '기능', docs: '문서', install: '설치', feedback: '피드백' },
  hero: { eyebrow: 'Windows 초고속 미디어 플레이어', title: '순수한 몰입.', accent: '시네마틱 미디어 경험.', lead: '차세대 Windows 로컬 미디어 플레이어. 가벼운 네이티브 엔진, 광고/추적 제로. Dolby Vision 및 로컬 AI 자막 완벽 지원.', download: 'Windows용 다운로드', explore: '주요 기능 탐색 ↓', note: '보안 및 검증 완료 · 설치 파일과 SHA-256 체크섬은 GitHub Releases에 공개되어 있습니다', nowPlaying: '재생 중', screenshot: 'main.webp', screenshotAlt: 'Kyna Player 인터페이스' },
  badges: ['⚡ 초고속 네이티브 렌더링', '🎬 Dolby Vision & 10-bit HDR', '🛡️ 100% 오프라인 AI 개인정보 보호', '📡 양방향 DLNA 스트리밍'],
  intro: '로컬 미디어를 재정의하다. 불필요한 무게를 줄이고 압도적인 색감과 제어력을 경험하세요.',
  highlights: [
    {
      icon: '⚡',
      tag: '네이티브 엔진',
      title: '밀리초 단위 초고속 실행',
      description: 'C++ / Slint 네이티브 아키텍처. 가벼운 메모리로 4K 고화질 영상도 즉시 재생.'
    },
    {
      icon: '🎬',
      tag: '화질 톤 매핑',
      title: 'Dolby Vision & 10-bit HDR',
      description: '고정밀 SDR Tone Mapping으로 일반 모니터에서도 풍부한 색감과 암부 표현.'
    },
    {
      icon: '✨',
      tag: '로컬 AI',
      title: 'Whisper 오프라인 음성 자막 생성',
      description: '로컬 AI 모델로 자막 생성 및 번역. 외부 서버 전송 없이 완벽한 보안 유지.'
    },
    {
      icon: '📡',
      tag: '무선 캐스팅',
      title: '양방향 DLNA 스트리밍',
      description: '원클릭으로 거실 TV에 전송하거나 PC를 수신기 화면으로 활용.'
    }
  ],
  features: {
    playback: { number: '01', eyebrow: '미니멀 재생', title: '영상 자체에 집중.', body: '깔끔한 플레이어 화면, 정밀한 탐색, 트랙 선택 및 전체 화면 재생으로 콘텐츠 본연에 몰입하세요.', screenshot: 'minimal.webp', screenshotAlt: 'Kyna Player 미니멀 재생 화면' },
    thumbnails: { number: '02', eyebrow: '타임라인 썸네일', title: '한눈에 빠른 탐색.', body: '타임라인 위에 마우스를 올려 고화질 비디오 프레임을 실시간 미리보고 원하는 장면을 즉시 찾으세요.', screenshot: 'thumbnails.webp', screenshotAlt: 'Kyna Player 타임라인 썸네일' },
    library: { number: '03', eyebrow: '재생 목록', title: '다음 영상도 손쉽게.', body: '플레이어를 벗어나지 않고도 재생 목록을 검색, 정렬, 저장하고 연속 재생 모드를 선택하세요.', screenshot: 'playlist.webp', screenshotAlt: 'Kyna Player 재생 목록 관리' },
    settings: {
      number: '04',
      eyebrow: '재생 설정',
      title: '디테일한 디스플레이 제어.',
      body: '컬러 프리셋, 오디오 딜레이, 음성 강조부터 이중 자막 배치 및 동기화까지 사이드 패널에서 직관적으로 제어.',
      tabs: {
        audio: {
          id: 'audio',
          label: '오디오',
          hint: '음성 동기화 & 음성 강조',
          title: '모든 소리를 선명하게.',
          body: '오디오 딜레이를 조절하고 야간 모드 및 음성 강조를 토글. 실시간 파형 피드백 제공.',
          screenshot: 'playback-audio.webp',
          screenshotAlt: 'Kyna Player 오디오 설정'
        },
        picture: {
          id: 'picture',
          label: '비디오',
          hint: '화각 & 컬러 튜닝',
          title: '이상적인 화질 구현.',
          body: '창 크기, 화면 비율, 밝기, 대비, 채도 및 색상 프리셋을 자유롭게 맞춤 설정.',
          screenshot: 'playback-picture.webp',
          screenshotAlt: 'Kyna Player 비디오 설정'
        },
        subtitles: {
          id: 'subtitles',
          label: '자막',
          hint: '이중 자막 & 스타일',
          title: '선명하고 가독성 높은 자막.',
          body: '주/보조 자막 크기, 위치, 외곽선, 투명도 및 초 단위 오프셋 동기화 조정.',
          screenshot: 'playback-subtitle.webp',
          screenshotAlt: 'Kyna Player 자막 설정'
        }
      }
    },
    enhancement: {
      eyebrow: 'AI 영상 향상 비교',
      title: '같은 프레임에서 차이를 확인하세요.',
      body: '분할선을 드래그하여 원본과 실시간 향상 결과를 비교하세요.',
      demoCaption: '데모 화면은 실제 동영상 파일의 스크린샷입니다.',
      cards: {
        dlss: { title: 'DLSS 5', body: 'AI 재구성으로 섬세한 디테일까지 선명하게.', originalLabel: '원본', enhancedLabel: '향상됨', sliderLabel: 'DLSS 5 이미지 비교', originalAlt: 'DLSS 5 비교용 원본 이미지', enhancedAlt: 'DLSS 5 향상 이미지' },
        anime4k: { title: 'Anime4K', body: '애니메이션에 맞춘 더욱 선명한 라인.', originalLabel: '원본', enhancedLabel: '향상됨', sliderLabel: 'Anime4K 이미지 비교', originalAlt: 'Anime4K 비교용 원본 이미지', enhancedAlt: 'Anime4K 향상 이미지' }
      }
    },
    subtitles: {
      number: '05',
      eyebrow: '자막 도구',
      title: '로컬 AI 자막 지원.',
      body: 'Whisper 음성 자막 생성 및 AI 자막 번역 기능 내장. 외부 서버 전송 없이 개인정보를 보호하며 언어의 장벽을 해소.',
      tabs: {
        transcript: {
          id: 'transcript',
          label: '음성 자막 생성',
          hint: 'Whisper 오프라인 자막 생성',
          title: '음성에서 정밀 자막 추출.',
          body: '원본 언어를 자동 감지하고 로컬 Whisper 모델을 실행하여 정밀 srt 자막 생성 및 적용.',
          screenshot: 'subtitle-transcript.webp',
          screenshotAlt: 'Kyna Player Whisper 자막 도구'
        },
        translate: {
          id: 'translate',
          label: '자막 번역',
          hint: '로컬 & AI 번역',
          title: '자막을 원하는 언어로 번역.',
          body: '로컬 Ollama 모델 또는 API에 연결하여 기존 자막을 다국어로 스마트하게 번역.',
          screenshot: 'subtitle-translate.webp',
          screenshotAlt: 'Kyna Player AI 자막 번역 도구'
        }
      }
    },
    casting: {
      number: '06',
      eyebrow: '무선 캐스팅',
      title: '대형 화면으로 감상.',
      body: '로컬 영상을 TV로 원클릭 전송하거나, PC를 DLNA 수신기로 만들어 모바일 기기 영상을 스트리밍 감상.',
      tabs: {
        send: {
          id: 'send',
          label: 'TV로 전송',
          hint: '대형 화면 재생 제어',
          title: '거실 TV에서 이어서 감상.',
          body: '네트워크 내 호환 TV를 검색하고 Kyna Player에서 직접 재생 및 볼륨을 리모컨처럼 제어.',
          screenshot: 'cast_send.webp',
          screenshotAlt: 'Kyna Player TV 캐스팅'
        },
        receive: {
          id: 'receive',
          label: '캐스팅 수신',
          hint: 'PC를 화면으로 전환',
          title: 'Kyna Player를 수신 디스플레이로.',
          body: 'DLNA 수신 서비스를 활성화하여 모바일 또는 타 기기에서 전송된 비디오 스트리밍 감상.',
          screenshot: 'cast_recv.webp',
          screenshotAlt: 'Kyna Player DLNA 수신 화면'
        }
      }
    },
    flexibility: { number: '07', eyebrow: '유연한 재생', title: '원하는 방식으로 감상.', body: '네트워크 미디어를 열고 미니 플레이어로 전환하여 작업 중에도 자유롭게 시청.', screenshot: 'mini.webp', screenshotAlt: 'Kyna Player 미니 플레이어' },
    hdr: { number: '08', eyebrow: 'Dolby Vision & HDR', title: 'Dolby Vision & 10-bit HDR 톤 매핑.', body: 'Dolby Vision 및 HDR 10-bit 비디오 디코딩 지원. 고정밀 SDR Tone Mapping으로 일반 모니터에서도 풍부한 색감 표현.', screenshot: 'dolby-vision.webp', screenshotAlt: 'Kyna Player Dolby Vision & HDR' },
  },
  install: { eyebrow: 'Windows', title: '시작할 준비가 되었습니다.', body: 'GitHub Releases에서 최신 설치 파일과 SHA-256 체크섬을 다운로드하세요.', download: 'Kyna Player 다운로드', guide: '설치 가이드 보기 →' },
  footer: 'Kyna Player for Windows · 로컬 미디어는 언제나 로컬에.', screenshots: { add: '제품 스크린샷 추가' },
  paths: { home: '/ko/', install: '/ko/docs/installation/', docs: '/ko/docs/', alternateHome: '/', alternateInstall: '/docs/installation/' },
};

export const installKo: InstallCopy = {
  locale: 'ko', seo: { title: 'Windows에 Kyna Player 설치', description: 'Windows용 Kyna Player 다운로드, 검증, 설치, 업데이트 및 삭제 방법.' },
  heading: 'Windows에 Kyna Player 설치', lead: 'GitHub Releases에서 최신 Windows 설치 파일을 받으시고 설치 전 해시를 검증하세요.', download: 'GitHub Releases 열기', back: '← Kyna Player로 돌아가기', skip: '본문으로 스킵', paths: ko.paths,
  sections: [
    { title: '설치', steps: ['GitHub Releases에서 최신 Kyna Player Windows 설치 파일과 SHA256SUMS 파일을 다운로드합니다.', 'PowerShell에서 Get-FileHash 명령을 실행하여 SHA-256 결과를 SHA256SUMS와 비교 검증합니다.', '설치 프로그램을 실행합니다. 설치 마법사에서 디렉토리를 선택할 수 있습니다.', '시작 메뉴 또는 설치 디렉토리에서 Kyna Player를 실행합니다.'] },
    { title: '첫 사용', steps: ['설치 파일에는 Whisper 모델이나 샘플 미디어가 포함되어 있지 않습니다.', '자막을 생성하기 전에 앱 내에서 호환 모델을 가져오거나 모델 다운로드 기능을 이용하세요.'] },
    { title: '업데이트 및 삭제', steps: ['업데이트 전 Kyna Player를 종료하세요.', '동일한 설치 디렉토리에서 새 설치 프로그램을 실행하면 업데이트됩니다.', '가져온 모델과 앱 설정은 사용자 데이터 디렉토리에 유지됩니다.', '삭제는 Windows 설치된 앱 또는 시작 메뉴에서 진행할 수 있습니다.'] },
  ],
};
