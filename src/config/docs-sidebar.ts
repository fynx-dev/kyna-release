export interface SidebarItem {
  title: string;
  link: string;
}

export interface SidebarGroup {
  text: string;
  items: SidebarItem[];
}

export const docsSidebar: Record<string, SidebarGroup[]> = {
  'zh-CN': [
    {
      text: '入门指南',
      items: [
        { title: '快速上手', link: 'getting-started' },
        { title: '安装与系统要求', link: 'installation' },
        { title: '界面导览', link: 'getting-started/interface-overview' },
        { title: '打开媒体', link: 'getting-started/opening-media' },
        { title: '基础播放与快捷键', link: 'getting-started/basic-playback' },
      ],
    },
    {
      text: '播放控制与定位',
      items: [
        { title: '播控与单帧步进', link: 'playback/controls' },
        { title: '进度条与精确定位', link: 'playback/seeking' },
        { title: '全屏与状态统计', link: 'playback/fullscreen-mini-stats' },
        { title: '循环与播放模式', link: 'playback/modes' },
        { title: '缩略图预览', link: 'playback/timeline-thumbnails' },
      ],
    },
    {
      text: '画面与画质增强',
      items: [
        { title: '视频输出与画质', link: 'video/output-and-picture' },
        { title: 'Anime4K 动画超分', link: 'video/anime4k' },
        { title: '增强对比与性能', link: 'video/comparison-performance' },
        { title: '高级滤镜与增强', link: 'video/research-filters' },
      ],
    },
    {
      text: '字幕功能',
      items: [
        { title: '内嵌与双字幕', link: 'subtitles/embedded-tracks' },
        { title: '外挂字幕加载', link: 'subtitles/external-files' },
        { title: '字幕样式与同步', link: 'subtitles/appearance' },
        { title: '在线字幕搜索', link: 'subtitles/online-search' },
        { title: '字幕常见问题', link: 'subtitles/troubleshooting' },
      ],
    },
    {
      text: 'AI 字幕实验室',
      items: [
        { title: 'AI 转录与翻译概览', link: 'subtitle-ai/overview' },
        { title: '本地语音转录', link: 'subtitle-ai/transcription' },
        { title: '大模型字幕翻译', link: 'subtitle-ai/translation' },
        { title: '模型与硬件加速', link: 'subtitle-ai/models' },
        { title: '字幕编辑与导出', link: 'subtitle-ai/results' },
      ],
    },
    {
      text: '音频、截图与投屏',
      items: [
        { title: '音轨与音画同步', link: 'audio-and-tools/audio' },
        { title: '音频增强与夜间模式', link: 'audio-and-tools/audio-enhancement' },
        { title: '截图与保存管理', link: 'audio-and-tools/screenshots' },
        { title: '媒体属性与诊断', link: 'audio-and-tools/media-information' },
        { title: 'DLNA 电视投屏', link: 'audio-and-tools/dlna' },
      ],
    },
    {
      text: '播放列表管理',
      items: [
        { title: '播放列表概览', link: 'playlist/overview' },
        { title: '播放列表管理', link: 'playlist/create-save-load' },
        { title: '文件夹批量导入', link: 'playlist/import-folder' },
        { title: '搜索、排序与净化', link: 'playlist/search-sort' },
        { title: '播放历史与文件', link: 'playlist/recent-and-files' },
      ],
    },
    {
      text: '设置与系统排错',
      items: [
        { title: '设置中心', link: 'settings/overview' },
        { title: '文件关联与系统集成', link: 'settings/file-associations' },
        { title: '数据、缓存与日志', link: 'settings/app-data-and-logs' },
        { title: '性能调优与排错', link: 'settings/performance-troubleshooting' },
        { title: '问题反馈与诊断', link: 'settings/feedback' },
      ],
    },
  ],
  'en': [
    {
      text: 'Getting Started',
      items: [
        { title: 'Getting Started', link: 'getting-started' },
        { title: 'Installation', link: 'installation' },
        { title: 'Interface Overview', link: 'getting-started/interface-overview' },
        { title: 'Opening Media', link: 'getting-started/opening-media' },
        { title: 'Basic Playback', link: 'getting-started/basic-playback' },
      ],
    },
    {
      text: 'Playback & Seeking',
      items: [
        { title: 'Playback & Stepping', link: 'playback/controls' },
        { title: 'Seeking & Precision', link: 'playback/seeking' },
        { title: 'Fullscreen & Stats', link: 'playback/fullscreen-mini-stats' },
        { title: 'Repeat & Modes', link: 'playback/modes' },
        { title: 'Thumbnail Previews', link: 'playback/timeline-thumbnails' },
      ],
    },
    {
      text: 'Video & Enhancement',
      items: [
        { title: 'Video Output & Color', link: 'video/output-and-picture' },
        { title: 'Anime4K Upscaling', link: 'video/anime4k' },
        { title: 'Comparison & Budget', link: 'video/comparison-performance' },
        { title: 'Advanced Filters', link: 'video/research-filters' },
      ],
    },
    {
      text: 'Subtitles',
      items: [
        { title: 'Tracks & Dual Subs', link: 'subtitles/embedded-tracks' },
        { title: 'External Subtitles', link: 'subtitles/external-files' },
        { title: 'Subtitle Styling & Sync', link: 'subtitles/appearance' },
        { title: 'Online Subtitle Search', link: 'subtitles/online-search' },
        { title: 'Subtitle Troubleshooting', link: 'subtitles/troubleshooting' },
      ],
    },
    {
      text: 'AI Subtitles Lab',
      items: [
        { title: 'AI Subtitles Overview', link: 'subtitle-ai/overview' },
        { title: 'Whisper Transcription', link: 'subtitle-ai/transcription' },
        { title: 'LLM Subtitle Translation', link: 'subtitle-ai/translation' },
        { title: 'AI Models & Acceleration', link: 'subtitle-ai/models' },
        { title: 'Subtitle Editing & Export', link: 'subtitle-ai/results' },
      ],
    },
    {
      text: 'Audio, Stills & Cast',
      items: [
        { title: 'Audio Tracks & Sync', link: 'audio-and-tools/audio' },
        { title: 'Audio Enhancement', link: 'audio-and-tools/audio-enhancement' },
        { title: 'Screenshots & Stills', link: 'audio-and-tools/screenshots' },
        { title: 'Media Info & Diagnostics', link: 'audio-and-tools/media-information' },
        { title: 'DLNA Wireless Casting', link: 'audio-and-tools/dlna' },
      ],
    },
    {
      text: 'Playlist Management',
      items: [
        { title: 'Playlist Overview', link: 'playlist/overview' },
        { title: 'Playlist Management', link: 'playlist/create-save-load' },
        { title: 'Batch Folder Import', link: 'playlist/import-folder' },
        { title: 'Search, Sort & Clean', link: 'playlist/search-sort' },
        { title: 'Recent History & Files', link: 'playlist/recent-and-files' },
      ],
    },
    {
      text: 'Settings & Troubleshooting',
      items: [
        { title: 'Settings Center', link: 'settings/overview' },
        { title: 'File Associations', link: 'settings/file-associations' },
        { title: 'App Data & Logs', link: 'settings/app-data-and-logs' },
        { title: 'Performance Tuning', link: 'settings/performance-troubleshooting' },
        { title: 'Feedback & Diagnostics', link: 'settings/feedback' },
      ],
    },
  ],
  'ja': [
    {
      text: 'スタートガイド',
      items: [
        { title: 'クイックスタート', link: 'getting-started' },
        { title: 'インストール', link: 'installation' },
        { title: 'インターフェース', link: 'getting-started/interface-overview' },
        { title: 'メディアを開く', link: 'getting-started/opening-media' },
        { title: '基本操作とキー', link: 'getting-started/basic-playback' },
      ],
    },
    {
      text: '再生とシーク',
      items: [
        { title: '再生とコマ送り', link: 'playback/controls' },
        { title: 'シークと位置決め', link: 'playback/seeking' },
        { title: '全画面と統計情報', link: 'playback/fullscreen-mini-stats' },
        { title: 'リピートと再生モード', link: 'playback/modes' },
        { title: 'サムネイルプレビュー', link: 'playback/timeline-thumbnails' },
      ],
    },
    {
      text: '映像と画質向上',
      items: [
        { title: '映像出力と画質設定', link: 'video/output-and-picture' },
        { title: 'Anime4K アニメ超解像', link: 'video/anime4k' },
        { title: '画質比較と性能管理', link: 'video/comparison-performance' },
        { title: '高度な映像フィルター', link: 'video/research-filters' },
      ],
    },
    {
      text: '字幕機能',
      items: [
        { title: '内蔵字幕とデュアル字幕', link: 'subtitles/embedded-tracks' },
        { title: '外部字幕の読み込み', link: 'subtitles/external-files' },
        { title: '字幕スタイルと同期', link: 'subtitles/appearance' },
        { title: 'オンライン字幕検索', link: 'subtitles/online-search' },
        { title: '字幕トラブル対処', link: 'subtitles/troubleshooting' },
      ],
    },
    {
      text: 'AI 字幕ラボ',
      items: [
        { title: 'AI 字幕機能の概要', link: 'subtitle-ai/overview' },
        { title: '音声文字起こし', link: 'subtitle-ai/transcription' },
        { title: 'LLM 字幕翻訳', link: 'subtitle-ai/translation' },
        { title: 'AI モデルと加速設定', link: 'subtitle-ai/models' },
        { title: '字幕の編集と出力', link: 'subtitle-ai/results' },
      ],
    },
    {
      text: '音声・画像・キャスト',
      items: [
        { title: '音声トラックと同期', link: 'audio-and-tools/audio' },
        { title: '音声強化と夜間モード', link: 'audio-and-tools/audio-enhancement' },
        { title: 'スクリーンショット', link: 'audio-and-tools/screenshots' },
        { title: 'メディア情報と診断', link: 'audio-and-tools/media-information' },
        { title: 'DLNA ワイヤレス投影', link: 'audio-and-tools/dlna' },
      ],
    },
    {
      text: 'プレイリスト管理',
      items: [
        { title: 'プレイリスト概要', link: 'playlist/overview' },
        { title: 'プレイリスト管理', link: 'playlist/create-save-load' },
        { title: 'フォルダ一括追加', link: 'playlist/import-folder' },
        { title: '検索・ソート・整形', link: 'playlist/search-sort' },
        { title: '再生履歴とファイル', link: 'playlist/recent-and-files' },
      ],
    },
    {
      text: '設定とトラブル対処',
      items: [
        { title: '設定センター', link: 'settings/overview' },
        { title: 'ファイル関連付け', link: 'settings/file-associations' },
        { title: 'データ・キャッシュ・ログ', link: 'settings/app-data-and-logs' },
        { title: '性能調整とトラブル', link: 'settings/performance-troubleshooting' },
        { title: 'フィードバックと診断', link: 'settings/feedback' },
      ],
    },
  ],
  'ko': [
    {
      text: '시작 가이드',
      items: [
        { title: '빠른 시작', link: 'getting-started' },
        { title: '설치 안내', link: 'installation' },
        { title: '인터페이스', link: 'getting-started/interface-overview' },
        { title: '미디어 열기', link: 'getting-started/opening-media' },
        { title: '기본 조작 및 키', link: 'getting-started/basic-playback' },
      ],
    },
    {
      text: '재생 및 탐색',
      items: [
        { title: '재생 및 프레임 이동', link: 'playback/controls' },
        { title: '탐색 및 위치 지정', link: 'playback/seeking' },
        { title: '전체화면 및 성능 통계', link: 'playback/fullscreen-mini-stats' },
        { title: '반복 및 재생 모드', link: 'playback/modes' },
        { title: '썸네일 미리보기', link: 'playback/timeline-thumbnails' },
      ],
    },
    {
      text: '화면 및 화질 향상',
      items: [
        { title: '비디오 출력 및 화면', link: 'video/output-and-picture' },
        { title: 'Anime4K 초해상도', link: 'video/anime4k' },
        { title: '화질 비교 및 성능', link: 'video/comparison-performance' },
        { title: '고급 필터 및 셰이더', link: 'video/research-filters' },
      ],
    },
    {
      text: '자막 기능',
      items: [
        { title: '내장 자막 및 듀얼 자막', link: 'subtitles/embedded-tracks' },
        { title: '외부 자막 로드', link: 'subtitles/external-files' },
        { title: '자막 스타일 및 싱크', link: 'subtitles/appearance' },
        { title: '온라인 자막 검색', link: 'subtitles/online-search' },
        { title: '자막 문제 해결', link: 'subtitles/troubleshooting' },
      ],
    },
    {
      text: 'AI 자막 연구실',
      items: [
        { title: 'AI 자막 기능 개요', link: 'subtitle-ai/overview' },
        { title: '로컬 음성 전사', link: 'subtitle-ai/transcription' },
        { title: 'LLM 자막 번역', link: 'subtitle-ai/translation' },
        { title: 'AI 모델 및 가속 설정', link: 'subtitle-ai/models' },
        { title: '자막 편집 및 내보내기', link: 'subtitle-ai/results' },
      ],
    },
    {
      text: '오디오, 캡처 및 전송',
      items: [
        { title: '오디오 트랙 및 싱크', link: 'audio-and-tools/audio' },
        { title: '오디오 향상 및 야간 모드', link: 'audio-and-tools/audio-enhancement' },
        { title: '스크린샷 및 캡처', link: 'audio-and-tools/screenshots' },
        { title: '미디어 속성 및 진단', link: 'audio-and-tools/media-information' },
        { title: 'DLNA 무선 전송', link: 'audio-and-tools/dlna' },
      ],
    },
    {
      text: '재생목록 관리',
      items: [
        { title: '재생목록 개요', link: 'playlist/overview' },
        { title: '재생목록 관리', link: 'playlist/create-save-load' },
        { title: '폴더 일괄 가져오기', link: 'playlist/import-folder' },
        { title: '검색, 정렬 및 정리', link: 'playlist/search-sort' },
        { title: '최근 기록 및 파일', link: 'playlist/recent-and-files' },
      ],
    },
    {
      text: '설정 및 문제 해결',
      items: [
        { title: '설정 센터', link: 'settings/overview' },
        { title: '파일 연결 설정', link: 'settings/file-associations' },
        { title: '데이터, 캐시 및 로그', link: 'settings/app-data-and-logs' },
        { title: '성능 최적화 및 해결', link: 'settings/performance-troubleshooting' },
        { title: '문제 신고 및 피드백', link: 'settings/feedback' },
      ],
    },
  ],
};
