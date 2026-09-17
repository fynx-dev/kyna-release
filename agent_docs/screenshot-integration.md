# AI 研发记录：落地页截图替换与静态优化

## 任务背景
kyna-landing 落地页原先使用占位符，缺少真实产品截图。工作区 `public/assets/images/features` 中提供了 11 张真实运行截图，本次任务完成了截图映射确认、静态 HTML/CSS 优化和 Astro 构建验证。

## 变更明细
1. **类型定义升级 (`src/i18n/types.ts`)**
   - 为 `hero` 增加了 `screenshot` 与 `screenshotAlt` 属性，支持首屏主视觉与 01 播放模块使用独立截图。
   - 为 `casting.send` 与 `casting.receive` 支持可配置的 `screenshot` 属性。
2. **多语言配置更新 (`src/i18n/zh-CN.ts` & `src/i18n/en.ts`)**
   - 映射各模块截图及无障碍 `alt` 描述文本。
3. **组件渲染 (`src/components/LandingPage.astro`)**
   - 服务端直接输出 `<img>` 标签，提升首屏 SEO 及加载稳定性，避免无 JS 时的占位空白。
   - 优化客户端 fallback 脚本。
4. **响应式与展示样式 (`src/styles/global.css`)**
   - 优化 `.screen-frame img` 的展示模式：对于竖向或对话框面板使用 `object-fit: contain` 保证核心控制项完整展示，16:9 播放界面使用 `object-fit: cover`。
