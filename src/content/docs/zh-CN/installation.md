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
   前往 [GitHub Releases](https://github.com/fynx-dev/kyna-release/releases/latest) 下载 `Kyna-Setup.exe`。
2. **运行安装向导**
   双击安装程序并按照提示完成安装，从开始菜单启动。
3. **版本更新**
   退出播放器后直接运行新版本安装包覆盖安装，个性化配置与 AI 模型将完整保留。

---

## 🗄️ 应用数据与缓存目录

Kyna Player 的用户数据集中保存在标准用户目录中：
- **目录路径**：`%APPDATA%\KynaPlayer\`（在 **设置 → 通用** 中可一键打开）。
- **文件结构**：
  - `config.json`：软件偏好设置与快捷键绑定。
  - `history.json`：历史播放进度与断点记忆。
  - `thumbnails\`：时间轴悬停预览缩略图缓存。
  - `models\`：本地离线 Whisper 语音模型。
