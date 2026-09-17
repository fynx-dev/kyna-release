# Kyna Landing Page 截图集成规范

本文档记录 Kyna 落地页各功能板块与截图素材的对应关系与配置规范。

## 截图资源清单

所有截图资源位于 `public/assets/images/features/`：

| 板块 / 功能 | 截图文件名 | 分辨率 | 比例 | 交互/展示形式 | 说明 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Hero 首屏** | `main.png` | 976×556 | 16:9 | 大图视差光晕 | 4K HDR 纯净高清播放主视觉 |
| **01 极简播放 (Playback)** | `minimal.png` | 976×556 | 16:9 | 单图卡片 | 纯粹沉浸的极简播放控制与无边框界面 |
| **02 进度缩略图 (Thumbnails)** | `thumbnails.png` | 1504×846 | 16:9 | 单图卡片 | 进度条悬浮多帧缩略图，快速定位精彩瞬间 |
| **03 播放列表 (Library)** | `playlist.png` | 1422×832 | ~16:9 | 单图卡片 | 抽屉式播放列表与选集管理 |
| **04 播放设置 (Settings)** | `playback-audio.png`<br>`playback-picture.png`<br>`playback-subtitle.png` | 378×898 | 竖向抽屉 | 3 图扑克牌叠层 + Tab 切换 | 放大 150%、平直叠放无倾斜、底部渐隐遮罩、左上角徽标 |
| **05 AI 字幕工作流 (Subtitles)** | `subtitle-transcript.png`<br>`subtitle-translate.png` | 718×678 | 对话框 | 2 图扑克牌叠层 + Tab 切换 | 本地 Whisper 离线语音转录与 AI 多语种翻译 |
| **06 无线投放 (Casting)** | `cast_send.png`<br>`cast_recv.png` | 1046×801 / 1126×627 | 宽屏 | 2 图扑克牌叠层 + Tab 切换 | 一键发现投屏至大屏 TV，以及本机作为接收端就绪 |
| **07 灵活小窗 (Flexibility)** | `mini.png` | 1239×989 | 1.25:1 (5:4) | 单图卡片 | 紧凑型画中画/迷你悬浮播放器，按原图宽高比完整显示 |
