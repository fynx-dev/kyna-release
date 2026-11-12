---
title: "安装与系统要求"
description: "系统配置要求、安装升级、数据目录与缓存管理说明。"
order: 2
group: "入门指南"
---

# 📦 安装与系统要求

## 💻 系统要求

| 项目 | 最低要求 | 推荐配置 |
| :--- | :--- | :--- |
| **操作系统** | Windows 10 (64-bit) 1909+ | Windows 11 (22H2+) |
| **处理器 (CPU)** | Intel Core i3 / AMD Ryzen 3 | Intel Core i5 / AMD Ryzen 5 或更高 |
| **显卡 (GPU)** | 支持 Direct3D 11 硬件解码 | 支持 DX12 / HEVC / AV1 / VP9 硬件加速 |
| **内存 (RAM)** | 4 GB | 8 GB 或更高 |

---

## 🚀 安装与升级

1. **下载安装包**
   前往 [GitHub Releases](https://github.com/fynx-dev/kyna-release/releases/latest) 下载 `Kyna-Player-vX.Y.Z-windows-x64.exe`。
2. **运行安装向导**
   双击安装程序并按照提示完成安装，从开始菜单启动。
3. **版本更新**
   退出播放器后直接运行新版本安装包覆盖安装，个性化配置与 AI 模型将完整保留。

---

## 🗄️ 应用数据与日志

安装版的用户数据位于 `%LOCALAPPDATA%\Kyna\`。若程序旁有 `data` 目录，便携版会使用该目录。日志保存在其中的 `logs\`；仅在用户选择保存时，崩溃 dump 才会写入 `dumps\`。

---

## 🛠️ 启动崩溃或闪退时怎么办？

1. **记下错误提示。** 记录发生时间和错误码。若提示缺少必需组件，请使用[官方安装包](https://github.com/fynx-dev/kyna-release/releases/latest)重新安装。安装包已包含所需 MSVC 运行库，不要从第三方网站下载单独的 DLL。
2. **查看日志。** 在文件资源管理器中打开 `%LOCALAPPDATA%\Kyna\logs`，查看 `kyna-launcher.log` 和崩溃时间附近最新的 `kyna-player-*.log`。便携版还需检查程序旁的 `data\logs`。
3. **按需保存 dump。** 如果崩溃窗口提供保存选项，选择后文件会留在本机，并在文件资源管理器中定位。dump 可能包含私人内存数据，不会自动上传；有些早期故障无法生成 dump。请勿将 dump 发布在公开 Issue 中。
4. **查找系统事件。** 按 **Win+R** 输入 `eventvwr.msc`，打开 **Windows 日志 → 应用程序**，找到崩溃时刻的错误，记录“**故障模块名称**”与“**异常代码**”。

[反馈问题](https://github.com/fynx-dev/kyna-release/issues/new?template=bug.yml)时，请附上播放器和 Windows 版本、复现步骤、崩溃时间、错误码及相关日志。分享前请检查日志：普通日志即使经过尽力脱敏，仍可能包含私人路径或网址。dump 请在了解隐私风险后通过私密渠道提供。
