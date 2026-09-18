---
title: "设置偏好与故障排查"
description: "偏好设置中心导航、Windows 文件关联、常见播放故障排查与问题反馈。"
order: 4
group: "工具与系统设置"
---

# ⚙️ 设置偏好与故障排查

根据硬件环境与使用偏好个性化定制播放器，并快速解决常见播放异常。

---

## 🎛️ 设置中心导航

![设置中心导航](/assets/images/docs/player-settings.png)

- **通用 (General)**：多语言切换（简体中文/英文/日文/韩文）、多开实例控制、AppData 数据目录一键打开。
- **播放 (Playback)**：默认打开媒体行为（替换/追加）、自动播放策略与断点记忆。
- **快捷键 (Hotkeys)**：查看与自定义键盘按键绑定。
- **文件关联 (Files)**：一键注册系统级视频默认关联，右键菜单显示 `Play with Kyna Player`。

![播放列表设置](/assets/images/docs/openfile-playlist-settings.png)

---

## 🛠️ 常见故障排查指南

### 1. 播放 4K/8K 视频出现卡顿丢帧
- **检查 GPU 调度**：笔记本双显卡用户，请在 Windows 设置中将 Kyna Player 指定为“高性能独立显卡”。
- **确认硬件加速**：确保已启用 Direct3D 11 硬件加速。
- **降低滤镜负荷**：若开启了 Anime4K 增强，可根据显卡性能适当降低档位。

### 2. 字幕出现乱码
- 检查字幕文件是否为 `UTF-8` 编码，建议将文本另存为 UTF-8 编码保存。

---

## 💬 问题反馈与日志导出

- **获取日志**：在设置中点击“打开 AppData 目录”，进入 `logs/` 文件夹即可获取 `kyna_player.log`。
- **提交 Issue**：前往 [GitHub Issues](https://github.com/fynx-dev/kyna-release/issues) 提交问题描述与日志。
