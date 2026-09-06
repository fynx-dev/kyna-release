# 发布流程

Kyna 的构建环境保持私有。本仓库只接收已经在私有环境验证完成的 draft release。

## 本地维护者流程

1. 在私有源码工作区运行 `scripts/package-release.ps1`，传入符合 `vX.Y.Z` 的版本和独立工作目录。
2. 脚本下载并校验锁定的依赖、构建 Release、通过 CMake install/CPack 创建 ZIP、解压校验布局，并执行 `kyna_subtitle.exe --version`。
3. 准备 release notes 后，用仅有本仓库 Contents: Read/Write 权限的细粒度 `GH_TOKEN` 运行 `scripts/upload-release-draft.ps1`。该脚本只创建或更新 draft，不会发布它。
4. 在 Actions 页面手动运行 `Publish verified draft`，输入相同 `vX.Y.Z` tag。

## 发布工作流

`publish-draft.yml` 仅使用本仓库的 `GITHUB_TOKEN`。它必须找到同 tag draft 中唯一的 Windows x64 ZIP 与 `SHA256SUMS`，重新计算 checksum，解压检查运行时布局，并执行 `kyna_subtitle.exe --version`。所有检查通过后才发布 draft；任何失败都会保留 draft。

## 权限与保密

- 本仓库不得保存 Kyna 源码、`vendor/`、构建输出、模型、媒体、下载缓存或本地绝对路径。
- 本仓库的 Actions 不得 checkout 私有源码或接收私有构建 token。
- 本地上传 token 只授予 `kyna-release` 的 Contents: Read/Write 权限。
- 已发布 tag 不得被本地上传脚本覆盖。
