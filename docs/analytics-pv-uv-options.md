# Kyna Landing PV / UV 统计方案（2026-09-08）

## 结论

推荐在 GitHub Pages 托管的静态 Astro 站点使用 **Cloudflare Web Analytics**。它在所有 Cloudflare 套餐可用、明确为免费，且无需将 DNS 或流量代理到 Cloudflare；只需在全站布局中加入其 beacon。它直接提供 page views 和 visitors，适合先解决 PV / UV，不需要自建服务器或数据库。[Cloudflare：概览](https://developers.cloudflare.com/web-analytics/about/) [Cloudflare：非代理站点接入](https://developers.cloudflare.com/web-analytics/get-started/)

若必须让分析数据完全留在自己控制的基础设施，选择 **自托管 Umami**；软件免费，但服务器、PostgreSQL、备份和升级并不免费，也有运维成本。不要把“自托管 Plausible”作为低维护免费方案：官方虽提供免费的 Community Edition，但其部署栈更重，适合已有相应运维能力的团队。[Umami 源码安装要求](https://github.com/umami-software/umami) [Plausible Community Edition](https://github.com/plausible/analytics)

## 各方案对比

| 方案 | 免费可用性 | 静态 Astro / GitHub Pages 接入 | PV / UV 含义 | 隐私与数据去向 | 适用判断 |
| --- | --- | --- | --- | --- | --- |
| **Cloudflare Web Analytics（推荐）** | 免费；官方称所有套餐可用。 | 在公共布局的 `</body>` 前加入控制台生成的 JS beacon；非 Cloudflare 代理站也支持。 | 提供 page views 与 visitors；属于 RUM（真实用户监测）。 | 官方称不收集或使用访客个人数据，也不跨其客户网站追踪个人。非代理站 beacon 数据发送到 `cloudflareinsights.com/cdn-cgi/rum`，即统计请求会发往 Cloudflare。 | 最小接入与零服务端运维，正好满足站点当前目标。 |
| **Umami Cloud** | 可免费注册；官方 Cloud 是按量计费，价格页需以注册时套餐为准，不能将其视为长期不限量免费。 | 将追踪代码放在站点 `<head>`；数据进入 Umami Cloud。 | Views 是访客事件总数；Visitors 是按带轮换 salt 的 session hash 得出的唯一 session 数。 | 项目宣称无 cookie、无监控；Cloud 托管意味着事件数据发送到 Umami 服务。指标文档说明 IP 用于地理位置推导但不存储。 | 需要事件、转化等功能，且可接受托管数据与潜在按量成本。 |
| **Umami 自托管** | 应用为 MIT 开源；软件免费，基础设施费用自行承担。 | 自行部署 Umami + PostgreSQL，然后把追踪 `<script>` 加入 `<head>`，请求发往自有域名/实例。 | 同 Umami Cloud。 | 数据落在自己选定的服务器与数据库；仍应在隐私政策中说明收集的 URL、来源、设备、粗粒度地理等维度。 | 有 Docker / PostgreSQL 运维能力，并且数据驻留优先。 |
| **Plausible Cloud** | 非免费长期方案：官方文档只提供 free trial。 | 在 `<head>` 加站点专属 snippet；数据发送到 Plausible 托管服务。 | PV 为页面加载总次数；UV 不用 cookie 或持久 ID，同日同设备/浏览器按一人计，多日或多设备会分别计数。 | 官方主张无 cookie；托管数据在其服务中。 | 功能成熟但不符合“最好免费”。 |
| **Plausible Community Edition 自托管** | Community Edition 免费；开源仓库采用 AGPL-3.0。服务器与运维自付。 | 自建后接入追踪 snippet。 | 同 Plausible 定义。 | 数据留在自有基础设施，取决于部署位置。 | 仅在能接受较高部署/维护复杂度时考虑。 |
| **Vercel Web Analytics** | Hobby 每月含 50,000 events，免费额度超出后会暂停采集；仅保留 1 个月报表，且 Hobby 不含自定义事件。 | 官方接入流程要求启用 Vercel 项目并部署到 Vercel；Astro 可用 `@vercel/analytics/astro`。当前 GitHub Pages 部署不适合。 | PV 是同一人重复加载也重复计数；UV 为请求生成的、仅当天有效的 hash。 | 不用 cookie，只存匿名数据；统计由 Vercel 提供。 | 只有迁移托管到 Vercel 后才值得选。 |

## 推荐落地：Cloudflare Web Analytics

1. 创建/登录 Cloudflare 账户，在 **Web Analytics → Add a site** 添加生产域名。
2. 复制 Cloudflare 生成的 beacon，放到 Astro 的根布局（所有页面共用）`</body>` 前；不用改 DNS 或把 GitHub Pages 代理到 Cloudflare。
3. 部署后在 Cloudflare 面板核对 PV、Visitors、来源与性能数据；官方说明数据出现可能需要几分钟。
4. 初期不要同时安装多个页面浏览 tracker，以免在排查 PV 时混淆口径。下载按钮等转化指标待产品定义后，再评估 Cloudflare 规则或改用 Umami/Plausible 的事件功能。

## 口径提醒

- **PV（Page Views）**：一次页面加载就是一次计数；同一访客重复载入仍增加 PV。
- **UV（Visitors）不是跨设备、跨长期周期的“真人数”**：无 cookie 的隐私方案会通过按日或按月轮换的哈希估算，因此不同设备或不同日可能被分别计数。比较趋势时，应固定同一产品和同一日期范围，不要与 GA 的用户数直接相加或互换。
- 若页面 URL 带有邮箱、token、订单号等敏感查询参数，应先避免把这些内容放入 URL，再启用任何前端统计。Umami 的官方指标定义明确其会记录 URL 查询参数；其他工具也应按各自的敏感数据过滤能力配置。

## 官方资料

- [Cloudflare Web Analytics：免费、隐私与指标概览](https://developers.cloudflare.com/web-analytics/about/)
- [Cloudflare Web Analytics：非代理站点与 Pages 的接入步骤](https://developers.cloudflare.com/web-analytics/get-started/)
- [Cloudflare Web Analytics：采集与 beacon 数据发送位置](https://developers.cloudflare.com/web-analytics/data-metrics/data-origin-and-collection/)
- [Umami：追踪代码接入](https://docs.umami.is/docs/collect-data)
- [Umami：指标、访客算法和采集字段](https://docs.umami.is/docs/metric-definitions)
- [Umami：开源、自托管安装与 Docker](https://github.com/umami-software/umami)
- [Plausible：PV / UV 的官方定义](https://plausible.io/docs/metrics-definitions)
- [Plausible：追踪 snippet 接入](https://plausible.io/docs/plausible-script)
- [Plausible：自托管 Community Edition](https://github.com/plausible/analytics)
- [Vercel：Web Analytics 的 UV / PV 口径与隐私](https://vercel.com/docs/analytics)
- [Vercel：免费额度与限制](https://vercel.com/docs/analytics/limits-and-pricing)
- [Vercel：Astro 接入与部署流程](https://vercel.com/docs/analytics/quickstart)
