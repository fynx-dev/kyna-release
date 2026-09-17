---
title: "Dolby Vision 与 HDR 10bit 转 SDR"
description: "介绍 Kyna Player 强大的色调映射与 Dolby Vision 解码转换能力。"
order: 3
group: "核心功能说明"
---

## 技术背景

HDR (High Dynamic Range) 和 Dolby Vision (杜比视界) 视频拥有极宽的动态范围和极其丰富的色彩信息（10-bit/12-bit 深色彩）。

但是，如果在普通的 SDR (Standard Dynamic Range) 8-bit 显示器上直接播放，往往会出现**画面发灰、色彩失真、对比度严重不足**的问题。

## 硬件加速色调映射 (Tone Mapping)

Kyna Player 内置先进的 GPU 硬件加速算法，能够在播放过程中对 Dolby Vision 和 HDR 动态元数据进行实时分析与 Tone Mapping 转换：

![Dolby Vision 演示图片](./dolby-demo.webp)

### 核心亮点

1. **精准色彩还原**：防止色彩过饱和或发灰，保持人像与对比度的自然平衡。
2. **零卡顿零延迟**：纯 GPU 硬件管线渲染，即使在 4K 60fps 杜比视界影片下也能保持低帧率开销。
3. **广泛格式兼容**：支持 Profile 5, Profile 8.1 等多种 Dolby Vision 格式。
