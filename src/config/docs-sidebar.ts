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
      ],
    },
    {
      text: '播放与画质',
      items: [
        { title: '播控与快捷导航', link: 'playback' },
        { title: '画质增强与视频设置', link: 'video-enhance' },
      ],
    },
    {
      text: '字幕与 AI 实验室',
      items: [
        { title: '字幕管理与样式外观', link: 'subtitles' },
        { title: 'AI 语音转录与翻译', link: 'ai-lab' },
      ],
    },
    {
      text: '工具与系统设置',
      items: [
        { title: '音频与声音增强', link: 'audio-and-tools' },
        { title: 'DLNA 无线投屏', link: 'dlna' },
        { title: '播放列表与文件管理', link: 'playlist' },
        { title: '设置偏好与故障排查', link: 'settings' },
      ],
    },
  ],
  'en': [
    {
      text: 'Getting Started',
      items: [
        { title: 'Quick Start', link: 'getting-started' },
        { title: 'Installation & Requirements', link: 'installation' },
      ],
    },
    {
      text: 'Playback & Video',
      items: [
        { title: 'Playback & Navigation', link: 'playback' },
        { title: 'Video Enhancement & Settings', link: 'video-enhance' },
      ],
    },
    {
      text: 'Subtitles & AI Lab',
      items: [
        { title: 'Subtitles & Appearance', link: 'subtitles' },
        { title: 'AI Transcription & Translation', link: 'ai-lab' },
      ],
    },
    {
      text: 'Tools & Settings',
      items: [
        { title: 'Audio & Sound Enhancement', link: 'audio-and-tools' },
        { title: 'DLNA Wireless Casting', link: 'dlna' },
        { title: 'Playlist & File Management', link: 'playlist' },
        { title: 'Preferences & Troubleshooting', link: 'settings' },
      ],
    },
  ],
  'ja': [
    {
      text: '入門ガイド',
      items: [
        { title: 'クイックスタート', link: 'getting-started' },
        { title: 'インストールとシステム要件', link: 'installation' },
      ],
    },
    {
      text: '再生と画質',
      items: [
        { title: '再生制御とショートカット', link: 'playback' },
        { title: '画質強化と映像設定', link: 'video-enhance' },
      ],
    },
    {
      text: '字幕と AI ラボ',
      items: [
        { title: '字幕管理とスタイル外観', link: 'subtitles' },
        { title: 'AI 音声認識と翻訳', link: 'ai-lab' },
      ],
    },
    {
      text: 'ツールとシステム設定',
      items: [
        { title: '音声とオーディオ強化', link: 'audio-and-tools' },
        { title: 'DLNA ワイヤレス投影', link: 'dlna' },
        { title: 'プレイリストとファイル管理', link: 'playlist' },
        { title: '設定とトラブルシューティング', link: 'settings' },
      ],
    },
  ],
  'ko': [
    {
      text: '시작 가이드',
      items: [
        { title: '빠른 시작', link: 'getting-started' },
        { title: '설치 및 시스템 요구사항', link: 'installation' },
      ],
    },
    {
      text: '재생 및 화질',
      items: [
        { title: '재생 제어 및 단축키 탐색', link: 'playback' },
        { title: '화질 향상 및 비디오 설정', link: 'video-enhance' },
      ],
    },
    {
      text: '자막 및 AI 랩',
      items: [
        { title: '자막 관리 및 스타일 외관', link: 'subtitles' },
        { title: 'AI 음성 전사 및 번역', link: 'ai-lab' },
      ],
    },
    {
      text: '도구 및 시스템 설정',
      items: [
        { title: '오디오 및 사운드 향상', link: 'audio-and-tools' },
        { title: 'DLNA 무선 전송', link: 'dlna' },
        { title: '재생목록 및 파일 관리', link: 'playlist' },
        { title: '환경설정 및 문제 해결', link: 'settings' },
      ],
    },
  ],
};
