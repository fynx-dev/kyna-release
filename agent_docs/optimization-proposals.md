# Kyna Landing 优化建议与推进路线图

本文档总结了 `kyna-landing` 项目在视觉与交互重构后的进一步优化空间，涵盖 **分析统计**、**文档系统**、**多语言 (i18n)**、**SEO & 性能** 以及 **UI/UX 细节** 五大维度。

---

## 1. 流量与数据统计 (Analytics / PV-UV)

- [ ] **集成 Cloudflare Web Analytics**
  - **背景**：已在 [`docs/analytics-pv-uv-options.md`](file:///d:/Side/kyna/kyna-landing/docs/analytics-pv-uv-options.md) 中确定选用 Cloudflare 免费且无 Cookie 的 Web Analytics。
  - **建议优化**：
    - 在 `BaseLayout.astro` 中增加可选环境变量或配置项注入 Cloudflare JS Beacon。
    - 在 GitHub Actions 部署流程或环境变量中传入 Token，实现零运维且隐私友好的 PV / UV 监控。

---

## 2. 文档系统 (Docs System)

- [ ] **多语言文档补齐 (en / ja / ko)**
  - **现状**：目前 `src/content/docs/` 下仅 `zh-CN` 拥有完整的 4 篇 Markdown 导览与功能说明，英文 (`en`)、日文 (`ja`)、韩文 (`ko`) 的文档尚未完全对齐。
  - **建议优化**：将 `installation.md`、`dolby-vision.md`、`shortcuts.md` 翻译并同步到 `en`、`ja`、`ko` 目录，确保多语言用户点进 Docs 不会遭遇 404 或内容缺省。
- [ ] **文档移动端侧边栏抽屉 (Mobile Sidebar Drawer)**
  - **现状**：在移动端/窄屏环境下，`DocSidebar` 会被隐藏或置底，查阅多篇文档不够便捷。
  - **建议优化**：为 `DocLayout` 顶部 Navbar 添加移动端侧边栏切换按钮 (Hamburger Menu / Drawer Panel)，方便手机端随时快速切换章节。
- [ ] **文档内标题 anchor 锚点平滑滚动与复制**
  - **建议优化**：给 Markdown `h2`/`h3` 标题生成自动 Hover 显示的 `#` 锚点链接，方便直接复制分享特定段落链接。

---

## 3. SEO 与 结构化数据 (SEO & Structured Data)

- [ ] **动态与精确的 `hreflang` 映射**
  - **现状**：`BaseLayout.astro` 中对 `hreflang` 仅处理了 `/` 与 `/install/` 的路径关联。
  - **建议优化**：扩展 `langPaths` 函数，使其能根据当前页面的多语言路径（包括 `/docs/...` 和后续新增页面）自动拼接精确的互链 `hreflang`。
- [ ] **文档页 Schema.org 结构化数据补强**
  - **建议优化**：在 `DocLayout.astro` 中除了 `SoftwareApplication` 之外，为文档页面注入 `TechArticle` / `BreadcrumbList` 的 JSON-LD 结构化数据，提升搜索引擎收录展现形态。

---

## 4. 性能与 Web Vitals 优化 (Performance & Web Vitals)

- [ ] **Hero 核心资源预加载 (Preload / High Priority)**
  - **建议优化**：给 Hero 区域主图 `main.webp` 添加 `fetchpriority="high"` 和 `loading="eager"` 标记，最大程度缩短 LCP (Largest Contentful Paint) 时间。
- [ ] **次要图片延迟加载与解码优化**
  - **建议优化**：为 Features / Deck / Tab 区域的所有次要图片统一配置 `loading="lazy"` 和 `decoding="async"`。

---

## 5. UI / UX 细节与可访问性 (Accessibility / A11y)

- [ ] **Lightbox 全屏原图预览键盘与手势增强**
  - **建议优化**：
    - **键盘导航**：按 `←` / `→` 键时自动在当前 Feature 组的相邻 Tab 或多图之间切换。
    - **触屏手势**：支持左右滑动 (Swipe Left/Right) 切换图片。
- [ ] **Deck 扑克牌组件在移动端的高度与触摸体验微调**
  - **建议优化**：进一步测试极窄屏幕（如 iPhone SE 375px）下 3 图叠层的高宽比展现，防止极窄屏下卡片发生意外挤压。

---

## 推荐的下一步优先事项 (Priority Ranking)

1. **高优先级 (High Priority)**：
   - [ ] 接入 Cloudflare Analytics 脚本（实现基础 PV/UV 监控）
   - [ ] 补充 `en` 英文文档（保障海外用户核心阅读体验）
   - [ ] 优化 Hero 图片 LCP 预加载 (`fetchpriority="high"`)

2. **中优先级 (Medium Priority)**：
   - [ ] 文档移动端侧边栏 Drawer 抽屉菜单
   - [ ] 补齐 `ja` 与 `ko` 语言文档
   - [ ] 精细化 `hreflang` 自动化生成

3. **低优先级 / 体验加分 (Low Priority / Polish)**：
   - [ ] Lightbox 键盘左右键与手势翻页
   - [ ] 文档标题锚点 Hover 复制
