# Kyna Release

公开的 Kyna Windows 发布、安装文档与反馈仓库。Kyna 源码、构建依赖和本地构建配置不存放于此。

## 下载

从 [Releases](../../releases) 下载最新的 `Kyna-vX.Y.Z-windows-x64.zip` 与同版本的 `SHA256SUMS`。安装、校验和升级步骤见 [Windows 安装说明](docs/windows-install.md)。

## 反馈

- 程序问题：[提交 bug](../../issues/new?template=bug.yml)
- 功能建议：[提交建议](../../issues/new?template=feature.yml)
- 文档问题：[提交文档反馈](../../issues/new?template=docs.yml)

请不要在公开 issue 中提交日志中的访问 token、API key、个人媒体路径或安全漏洞。安全问题请通过 GitHub 的私密安全报告功能提交。

## 发布边界

维护者在私有本地环境构建、验证并上传 draft release。本仓库的发布工作流仅复核 draft 资产后发布；它不检出、不读取或不构建 Kyna 源码。详见 [发布流程](docs/release-process.md)。
