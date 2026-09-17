import type { InstallCopy, LandingCopy } from './types';

export const zhCN: LandingCopy = {
  locale: 'zh-CN', direction: 'ltr',
  seo: { title: 'Kyna Player — 纯粹视听，影音臻境。', description: 'Kyna Player 是一款专注于本地播放、字幕、声音控制和电视投放的 Windows 极速媒体播放器。' },
  skip: '跳至内容',
  navigation: { features: '功能', docs: '文档', install: '安装', feedback: '反馈' },
  hero: { eyebrow: 'Windows 极速媒体播放器', title: '纯粹视听。', accent: '影音臻境。', lead: '下一代 Windows 本地媒体播放器。原生轻量引擎、零广告追踪，完美支持杜比视界与本地 AI 字幕增强。', download: '立即下载 Windows 版', explore: '探索全套黑科技 ↓', note: '安全无毒 · 安装包与 SHA-256 校验码同公布于 GitHub Releases', nowPlaying: '正在播放', screenshot: 'main.webp', screenshotAlt: 'Kyna Player 界面' },
  badges: ['⚡ 毫秒级原生渲染', '🎬 杜比视界 & 10-bit HDR', '🛡️ 100% 离线 AI 隐私', '📡 双向 DLNA 视听流转'],
  intro: '重新定义本地影音。摒弃沉重与繁杂，让极致色彩与掌控力触手可及。',
  highlights: [
    {
      icon: '⚡',
      tag: '原生引擎',
      title: '毫秒级极速启动',
      description: '基于 C++ / Slint 原生轻量架构，内存占用极低，拖拽随点随播，秒开 4K 高码率大片。'
    },
    {
      icon: '🎬',
      tag: '画质黑科技',
      title: '杜比视界 & 10-bit HDR',
      description: '内置高精度 SDR Tone Mapping 色彩映射，即便在普通显示器上也能呈现绚丽真实的色彩与丰富暗部细节。'
    },
    {
      icon: '✨',
      tag: '本地 AI 引擎',
      title: 'Whisper 离线语音转录',
      description: '直接调用本地 AI 模型自动生成高精度字幕与智能翻译，无需上传任何外部服务器，隐私完全留存本地。'
    },
    {
      icon: '📡',
      tag: '跨屏流转',
      title: '双向 DLNA 无线投屏',
      description: '一键把视频投送到客厅大屏，或让 Kyna Player 变身为局域网接收端，随时承接手机与多设备媒体画质。'
    }
  ],
  features: {
    playback: { number: '01', eyebrow: '极简播放', title: '专注于影片本身。', body: '简洁的播放界面、精确进度定位、音视频轨道选择和全屏播放，让注意力回到内容上。', screenshot: 'minimal.webp', screenshotAlt: 'Kyna Player 极简播放界面' },
    thumbnails: { number: '02', eyebrow: '进度缩略图', title: '快速定位，一目了然。', body: '可实时预览多帧高清视频缩略图，精彩片段与定位跳转尽在掌握。', screenshot: 'thumbnails.webp', screenshotAlt: 'Kyna Player 进度条缩略图预览' },
    library: { number: '03', eyebrow: '播放列表', title: '下一部，随手可得。', body: '无需离开播放器，即可搜索、排序、保存播放列表，并选择后续播放方式。', screenshot: 'playlist.webp', screenshotAlt: 'Kyna Player 播放列表管理' },
    settings: {
      number: '04',
      eyebrow: '播放设置',
      title: '随心微调，掌控全局。',
      body: '从画面色彩预设、音频延迟与人声增强，到双字幕排版与同步，随时唤出侧栏精确控制。',
      tabs: {
        audio: {
          id: 'audio',
          label: '音频',
          hint: '声音延迟与人声增强',
          title: '听见每个细节。',
          body: '调整音频延迟，并在需要更清晰聆听时使用夜间模式或人声增强，配合实时波形直观感知。',
          screenshot: 'playback-audio.webp',
          screenshotAlt: 'Kyna Player 声音控制与波形调节'
        },
        picture: {
          id: 'picture',
          label: '视频',
          hint: '画面尺寸与色彩预设',
          title: '细腻调校每帧画面。',
          body: '随心调整窗口缩放比例、画面填充模式以及亮度、对比度、饱和度与风格预设。',
          screenshot: 'playback-picture.webp',
          screenshotAlt: 'Kyna Player 视频画面与色彩调节'
        },
        subtitles: {
          id: 'subtitles',
          label: '字幕',
          hint: '双字幕与外观排版',
          title: '让每一句都清晰好读。',
          body: '自定义主/副双字幕字号、位置、描边强度与不透明度，支持独立秒级同步校准。',
          screenshot: 'playback-subtitle.webp',
          screenshotAlt: 'Kyna Player 字幕外观与排版设置'
        }
      }
    },
    enhancement: {
      eyebrow: 'AI 视频增强对比',
      title: '在同一帧中看见差别。',
      body: '拖动分割线，对比原始画面与实时增强效果。',
      demoCaption: '演示画面为实际视频文件截图。',
      cards: {
        dlss: { title: 'DLSS 5', body: 'AI 重建，让细节更清晰。', originalLabel: '原始画面', enhancedLabel: '增强画面', sliderLabel: 'DLSS 5 图像对比', originalAlt: 'DLSS 5 对比原始画面', enhancedAlt: 'DLSS 5 增强画面' },
        anime4k: { title: 'Anime4K', body: '为动画调校的更锐利线条。', originalLabel: '原始画面', enhancedLabel: '增强画面', sliderLabel: 'Anime4K 图像对比', originalAlt: 'Anime4K 对比原始画面', enhancedAlt: 'Anime4K 增强画面' }
      }
    },
    subtitles: {
      number: '05',
      eyebrow: '字幕工具',
      title: '本地 AI，听见与看懂。',
      body: '内置本地 Whisper 语音转录与 AI 字幕翻译能力，无需上传外部服务器，保护隐私的同时让语言不再是障碍。',
      tabs: {
        transcript: {
          id: 'transcript',
          label: '语音转录',
          hint: 'Whisper 本地离线转录',
          title: '从音频生成精准字幕。',
          body: '支持自动检测原片语言，调用本地 Whisper 模型生成高精度 srt 字幕，并可一键加载为当前字幕轨道。',
          screenshot: 'subtitle-transcript.webp',
          screenshotAlt: 'Kyna Player Whisper 字幕转录工具'
        },
        translate: {
          id: 'translate',
          label: '字幕翻译',
          hint: '本地与在线 AI 翻译',
          title: '将字幕翻译为你的语言。',
          body: '连接本地 Ollama 模型或在线 API，对已有字幕进行智能多语言翻译，轻松看懂外语好片。',
          screenshot: 'subtitle-translate.webp',
          screenshotAlt: 'Kyna Player AI 字幕翻译工具'
        }
      }
    },
    casting: {
      number: '06',
      eyebrow: '无线投放',
      title: '让画面，随心流转。',
      body: '把本地影片一键投放到大屏电视，或让当前电脑变身接收端，随时承接来自手机与局域网设备的媒体。',
      tabs: {
        send: {
          id: 'send',
          label: '投放到电视',
          hint: '大屏播放与设备控制',
          title: '在大屏上继续观看。',
          body: '一键扫描局域网中的兼容电视与大屏设备，选择目标并从 Kyna Player 直观控制播放与音量。',
          screenshot: 'cast_send.webp',
          screenshotAlt: 'Kyna Player 投放到电视'
        },
        receive: {
          id: 'receive',
          label: '接收投放',
          hint: '成为局域网播放屏幕',
          title: '让 Kyna Player 成为你的屏幕。',
          body: '开启 DLNA 接收服务，随时接收局域网内其他设备投送的视频与流媒体播放。',
          screenshot: 'cast_recv.webp',
          screenshotAlt: 'Kyna Player 接收 DLNA 投屏'
        }
      }
    },
    flexibility: { number: '07', eyebrow: '灵活播放', title: '按你的方式观看。', body: '需要时打开网络媒体，再切换到紧凑的迷你播放器，始终掌握控制权。', screenshot: 'mini.webp', screenshotAlt: 'Kyna Player 迷你播放器' },
    hdr: { number: '08', eyebrow: '杜比视界与 HDR', title: '杜比视界与 10-bit HDR 色彩映射。', body: '原生支持 Dolby Vision (杜比视界) 动态范围与 HDR 10-bit 视频解析，智能色调映射（Tone Mapping）转为 SDR 显示，在普通屏幕上也能呈现真实饱满的色彩与丰富暗部细节。', screenshot: 'dolby-vision.webp', screenshotAlt: 'Kyna Player 杜比视界与 HDR 色彩映射处理' },
  },
  install: { eyebrow: 'Windows', title: '准备就绪，随时开始。', body: '从 GitHub Releases 下载最新安装程序及其 SHA-256 校验文件。', download: '下载 Kyna Player', guide: '阅读安装指南 →' },
  footer: 'Kyna Player for Windows · 本地媒体，始终留在本地。', screenshots: { add: '添加产品截图' },
  paths: { home: '/zh-CN/', install: '/zh-CN/docs/installation/', docs: '/zh-CN/docs/', alternateHome: '/', alternateInstall: '/docs/installation/' },
};

export const installZhCN: InstallCopy = {
  locale: 'zh-CN', seo: { title: '在 Windows 上安装 Kyna Player', description: '下载、校验、安装、更新和卸载 Windows 版 Kyna Player。' },
  heading: '在 Windows 上安装 Kyna Player', lead: '从 GitHub Releases 获取最新 Windows Kyna Player 安装程序，并在安装前校验文件哈希。', download: '打开 GitHub Releases', back: '← 返回 Kyna Player', skip: '跳至内容', paths: zhCN.paths,
  sections: [
    { title: '安装', steps: ['从 GitHub Releases 下载最新 Kyna Player Windows 安装程序及同版本 SHA256SUMS 文件。', '在 PowerShell 中对安装程序运行 Get-FileHash，并将 SHA-256 结果与 SHA256SUMS 比对。', '运行安装程序；可在安装向导中选择安装目录。', '从开始菜单或安装目录启动 Kyna Player。'] },
    { title: '首次使用', steps: ['安装程序不包含 Whisper 模型或示例媒体。', '创建字幕前，请在应用中导入兼容模型，或使用应用内模型下载功能。模型存储在用户数据目录中。'] },
    { title: '更新和卸载', steps: ['更新前退出 Kyna Player。', '在相同安装目录运行较新的安装程序即可更新。', '已导入的模型和应用设置会保留在用户数据目录中。', '使用 Windows 已安装的应用，或开始菜单中的卸载入口卸载 Kyna Player。'] },
  ],
};
