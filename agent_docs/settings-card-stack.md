# AI 研发记录：播放设置扑克牌叠层动效设计

## 需求概述
将落地页原先单独的“声音”板块升级为“播放设置 (Playback Settings)”，并将 3 张侧边栏截图（音频 `playback-audio.png`、视频/画面 `playback-picture.png`、字幕 `playback-subtitle.png`）设计为扑克牌（Card Deck Stack）叠层切牌交互形式。

## 关键实现
1. **数据与类型扩展**
   - 增加 `SettingTabCopy` 与 `SettingsCopy` 类型。
   - `zh-CN.ts` 与 `en.ts` 支持 3 个 Tab（音频、视频、字幕）的标题、副标题、文案及截图路径映射。
2. **交互式扑克牌组件**
   - 包含 3 张定位卡片（`.deck-card`）及对应的 `.settings-nav` Tab 切换按钮。
   - 调整为平直平整叠放布局（无倾斜角度 `rotate(0deg)`），卡片尺寸放大 150% 至 `375px × 680px`（接近原生 1:1 分辨率展示）。
   - 增加了 CSS `mask-image: linear-gradient(...)` 底部渐隐消失效果，使卡片底部自然融入背景。
   - 支持双向交互：点击左侧 Tab 或点击右侧叠层中的任何一张卡片，均可平滑将目标卡片置顶并高亮发光。
   - 次层卡片支持 Hover 挑起反馈。
3. **响应式与无障碍**
   - 支持键盘方向键/Tab 导航。
   - 移动端自适应缩放卡片尺寸与偏移量，杜绝横向滚动溢出。
