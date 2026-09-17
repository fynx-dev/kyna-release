export interface SidebarItem {
  title: string;
  link: string; // relative slug without lang prefix, e.g. "getting-started" or "features/dolby-vision"
}

export interface SidebarGroup {
  text: string;
  items: SidebarItem[];
}

export const docsSidebar: Record<string, SidebarGroup[]> = {
  'zh-CN': [
    {
      text: '新手指南',
      items: [
        { title: '快速入门', link: 'getting-started' },
        { title: '安装与系统要求', link: 'installation' },
      ],
    },
    {
      text: '核心功能说明',
      items: [
        { title: 'Dolby Vision 与 HDR 10bit 转 SDR', link: 'features/dolby-vision' },
        { title: '快捷键与全键盘操作', link: 'features/shortcuts' },
      ],
    },
  ],
  'en': [
    {
      text: 'Getting Started',
      items: [
        { title: 'Quick Start', link: 'getting-started' },
        { title: 'Installation & System Requirements', link: 'installation' },
      ],
    },
    {
      text: 'Core Features',
      items: [
        { title: 'Dolby Vision & HDR 10-bit to SDR', link: 'features/dolby-vision' },
        { title: 'Shortcuts & Keyboard Controls', link: 'features/shortcuts' },
      ],
    },
  ],
  'ja': [
    {
      text: 'スタートガイド',
      items: [
        { title: 'クイックスタート', link: 'getting-started' },
        { title: 'インストールと動作环境', link: 'installation' },
      ],
    },
    {
      text: '主要功能说明',
      items: [
        { title: 'Dolby Vision および HDR 10-bit 转换', link: 'features/dolby-vision' },
        { title: 'ショートカット一覧', link: 'features/shortcuts' },
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
      text: '주요 기능',
      items: [
        { title: 'Dolby Vision 및 HDR 10bit SDR 변환', link: 'features/dolby-vision' },
        { title: '단축키 가이드', link: 'features/shortcuts' },
      ],
    },
  ],
};
