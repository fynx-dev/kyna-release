# AI 研发记录：落地页 Section 扩展与通用 Deck 卡片组件重构

## 1. 任务背景与需求
- Hero 主图切换为 `main.png`（4K HDR 高画质主播放器视图）。
- 新增独立的 02 Section「进度缩略图」(`thumbnails.png`)，文案重点突出“进度缩略图，快速定位视频内容”。
- 将字幕 Section 重构为双图 Tab 切换叠层（`subtitle-transcript.png` 与 `subtitle-translate.png`）。
- 将投放 Section 重构为双图 Tab 切换叠层（`cast_send.png` 与 `cast_recv.png`）。
- 保持播放设置 Section 3 图扑克牌叠层（放大 150%、底部渐隐、左上角徽标、平直无倾斜）。

## 2. 核心架构调整
1. **多语言与配置数据层 (`src/i18n/`)**：
   - 定义通用 `DeckSectionCopy` 与 `TabDeckItemCopy` 接口，解耦不同板块的卡片数据。
   - 包含 7 个标准 Feature 板块：`playback`, `thumbnails`, `library`, `settings`, `subtitles`, `casting`, `flexibility`。
2. **UI 组件与交互逻辑 (`src/components/LandingPage.astro`)**：
   - 使用统一属性 `data-deck-section` 与 `data-deck-tab` 驱动所有可切换 Deck 板块。
   - 动态计算 rank 序列（`is-top`, `is-middle`, `is-bottom`），支持任意 2~N 张图片的平滑堆叠与层级切换。
3. **样式系统 (`src/styles/global.css`)**：
   - 统一 `.deck-container` / `.deck-card` 结构。
   - 针对不同长宽比类型针对性定制容器与阴影：
     - `settings`：竖向抽屉（~0.42）+ 底部渐隐遮罩 + 放大 150%；
     - `subtitles`：对话框（718×678，1.059:1）；
     - `casting`：`cast_send.png`（1046×801，1.306:1）与 `cast_recv.png`（1126×627，1.796:1）独立设置 `aspect-ratio`，采用 `top: 50%` 垂直居中叠放，图片 `object-fit: contain` 100% 完整显示不被裁切。
4. **全站图片 Lightbox 原图预览系统**：
   - 包含磨砂玻璃遮罩（`backdrop-filter: blur(18px)`）、关闭按钮、图片标题说明、ESC 键及遮罩点击关闭。
   - **交互分流逻辑**：
     - 单图（Hero、01、02、03、07）：点击直接打开 Lightbox 预览原图，光标显示 `zoom-in`；
     - 扑克牌叠层（04 设置、05 字幕、06 投放）：
       - **当前处于顶层的卡片**（`.is-top`）：点击触发 Lightbox 预览原图，光标显示 `zoom-in`；
       - **非当前卡片**（`.is-middle` / `.is-bottom`）：点击执行扑克牌切牌，切换至前台，光标显示 `pointer`。

## 3. 验证结果
- `npm run build` 成功通过，所有静态路由打包编译无异常。
