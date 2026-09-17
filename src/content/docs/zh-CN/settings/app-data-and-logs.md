---
title: "数据、缓存与日志"
description: "定位 Kyna Player 的配置文件、缩略图缓存、AI 模型存储目录与诊断日志。"
order: 3
group: "设置、系统集成与排错"
---

# 数据、缓存与日志

为了实现绿色、规范的系统集成，Kyna Player 将所有用户配置、缓存数据与诊断日志集中存放在标准的 Windows 用户数据目录中。

---

## 📂 应用数据根目录 (AppData Location)

在 Windows 系统中，Kyna Player 的数据目录位于：

```plaintext
%APPDATA%\KynaPlayer\
(实际绝对路径: C:\Users\<你的用户名>\AppData\Roaming\KynaPlayer\)
```

> [!TIP]
> 打开 **设置 → 通用 (General)**，直接点击 **“📂 打开 AppData 目录”** 按钮即可一键在资源管理器中打开该路径。

---

## 🌲 目录结构与各文件说明

```plaintext
AppData\Roaming\KynaPlayer\
├── 📄 config.json           # 播放器的全部偏好设置与个性化配置
├── 📄 history.json          # 播放历史记录与断点续播时间戳
├── 📁 thumbnails\           # 时间轴悬停预览缩略图的高速磁盘缓存
├── 📁 subtitles\            # 在线搜索下载的字幕暂存库
├── 📁 models\               # 本地离线 Whisper 语音模型权重文件
└── 📁 logs\                 # 运行与崩溃诊断日志
    └── 📄 kyna_player.log   # 包含解码器、渲染器与 AI 推理的关键运行日志
```

---

## 🧹 磁盘缓存清理策略

随着播放视频数量的增加，缩略图和临时字幕可能会占用一定存储空间：

- **自动老化淘汰 (LRU Cache)**
  缩略图缓存默认限制最大容量（如 500MB），超出时会自动淘汰最久未访问的媒体缓存。
- **手动一键清空缓存**
  - 在 **设置 → 通用** 中点击 **“清空临时缓存”** 按钮，即可瞬间安全释放所有临时缩略图与在线字幕缓存。

---

## 🔄 备份与重置出厂设置

- **迁移与备份**
  若要更换新电脑，只需复制 `config.json` 文件到新电脑的对应目录，即可 100% 还原所有偏好设置与快捷键绑定。
- **彻底重置出厂**
  关闭播放器，直接删除 `%APPDATA%\KynaPlayer\config.json`，再次启动播放器时将自动生成初始默认配置。
