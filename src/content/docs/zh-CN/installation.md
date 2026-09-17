---
title: "安装与系统要求"
description: "详细说明 Kyna Player 在 Windows 平台上的系统推荐配置、校验哈希、安装、更新及卸载步骤。"
order: 2
group: "新手指南"
---

## 系统要求

为了获得最佳的 4K / HDR 视频解码与 AI 字幕生成体验，建议你的 Windows 系统满足以下配置要求：

| 配置项 | 最低要求 | 推荐配置 |
| :--- | :--- | :--- |
| **操作系统** | Windows 10 (64-bit) 1909+ | Windows 11 (22H2+) |
| **处理器 (CPU)** | Intel Core i3 / AMD Ryzen 3 | Intel Core i5 / AMD Ryzen 5 或更高 |
| **显卡 (GPU)** | 支持 DX11 硬件解码 | 支持 DX12 / HEVC / AV1 / VP9 硬件解码 |
| **内存 (RAM)** | 4 GB | 8 GB 或更高 |

## 安装步骤

1. 前往官方 [GitHub Releases](https://github.com/fynx-dev/kyna-release/releases/latest) 下载最新的 Kyna Player 安装包 `Kyna-Setup.exe` 以及同版本的 `SHA256SUMS` 校验文件。
2. （可选）在终端中运行 PowerShell 命令对文件哈希进行安全校验：
   ```powershell
   Get-FileHash .\Kyna-Setup.exe -Algorithm SHA256
   ```
   比对生成的 SHA-256 字符串与官方公布的 `SHA256SUMS` 是否完全吻合。
3. 双击运行 `Kyna-Setup.exe` 启动安装向导，选择安装路径并完成安装。
4. 从开始菜单或桌面快捷方式启动 Kyna Player。

## 首次使用指引

- **硬件解码与色调映射**：软件首次启动会自动检测你的显卡与 GPU 能力，默认开启杜比视界 (Dolby Vision) / HDR 10-bit 到 SDR 的硬件 Tone Mapping。
- **Whisper AI 模型导入**：安装包本身不内置体积巨大的 AI 语言模型。如需使用语音转字幕功能，请在播放器“字幕 -> 本地 AI”面板中一键下载或手动导入兼容模型（存储于用户 Data 目录）。

## 更新与卸载

- **应用更新**：更新前请先退出正在运行的 Kyna Player，直接运行新版本的 `Kyna-Setup.exe` 覆盖安装即可。已导入的 AI 模型与用户偏好设置将完整保留。
- **软件卸载**：可以通过 Windows“设置 -> 已安装的应用”或开始菜单中的卸载入口干净卸载。
