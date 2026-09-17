#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shorten Titles across all documentation languages to prevent visual overflow."""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_ROOT = os.path.join(BASE_DIR, 'src', 'content', 'docs')

TITLE_MAP = {
    "getting-started.md": {
        "zh-CN": "快速上手",
        "en": "Getting Started",
        "ja": "クイックスタート",
        "ko": "빠른 시작",
    },
    "installation.md": {
        "zh-CN": "安装与系统要求",
        "en": "Installation",
        "ja": "インストール",
        "ko": "설치 안내",
    },
    "getting-started/interface-overview.md": {
        "zh-CN": "界面导览",
        "en": "Interface Overview",
        "ja": "インターフェース",
        "ko": "인터페이스",
    },
    "getting-started/opening-media.md": {
        "zh-CN": "打开媒体",
        "en": "Opening Media",
        "ja": "メディアを開く",
        "ko": "미디어 열기",
    },
    "getting-started/basic-playback.md": {
        "zh-CN": "基础播放与快捷键",
        "en": "Basic Playback",
        "ja": "基本操作とキー",
        "ko": "기본 조작 및 키",
    },
    "playback/controls.md": {
        "zh-CN": "播控与单帧步进",
        "en": "Playback & Stepping",
        "ja": "再生とコマ送り",
        "ko": "재생 및 프레임 이동",
    },
    "playback/seeking.md": {
        "zh-CN": "进度条与精确定位",
        "en": "Seeking & Precision",
        "ja": "シークと位置決め",
        "ko": "탐색 및 위치 지정",
    },
    "playback/fullscreen-mini-stats.md": {
        "zh-CN": "全屏与状态统计",
        "en": "Fullscreen & Stats",
        "ja": "全画面と統計情報",
        "ko": "전체화면 및 성능 통계",
    },
    "playback/modes.md": {
        "zh-CN": "循环与播放模式",
        "en": "Repeat & Modes",
        "ja": "リピートと再生モード",
        "ko": "반복 및 재생 모드",
    },
    "playback/timeline-thumbnails.md": {
        "zh-CN": "缩略图预览",
        "en": "Thumbnail Previews",
        "ja": "サムネイルプレビュー",
        "ko": "썸네일 미리보기",
    },
    "video/output-and-picture.md": {
        "zh-CN": "视频输出与画质",
        "en": "Video Output & Color",
        "ja": "映像出力と画質設定",
        "ko": "비디오 출력 및 화면",
    },
    "video/anime4k.md": {
        "zh-CN": "Anime4K 动画超分",
        "en": "Anime4K Upscaling",
        "ja": "Anime4K アニメ超解像",
        "ko": "Anime4K 초해상도",
    },
    "video/comparison-performance.md": {
        "zh-CN": "增强对比与性能",
        "en": "Comparison & Budget",
        "ja": "画質比較と性能管理",
        "ko": "화질 비교 및 성능",
    },
    "video/research-filters.md": {
        "zh-CN": "高级滤镜与增强",
        "en": "Advanced Filters",
        "ja": "高度な映像フィルター",
        "ko": "고급 필터 및 셰이더",
    },
    "subtitles/embedded-tracks.md": {
        "zh-CN": "内嵌与双字幕",
        "en": "Tracks & Dual Subs",
        "ja": "内蔵字幕とデュアル字幕",
        "ko": "내장 자막 및 듀얼 자막",
    },
    "subtitles/external-files.md": {
        "zh-CN": "外挂字幕加载",
        "en": "External Subtitles",
        "ja": "外部字幕の読み込み",
        "ko": "외부 자막 로드",
    },
    "subtitles/appearance.md": {
        "zh-CN": "字幕样式与同步",
        "en": "Subtitle Styling & Sync",
        "ja": "字幕スタイルと同期",
        "ko": "자막 스타일 및 싱크",
    },
    "subtitles/online-search.md": {
        "zh-CN": "在线字幕搜索",
        "en": "Online Subtitle Search",
        "ja": "オンライン字幕検索",
        "ko": "온라인 자막 검색",
    },
    "subtitles/troubleshooting.md": {
        "zh-CN": "字幕常见问题",
        "en": "Subtitle Troubleshooting",
        "ja": "字幕トラブル対処",
        "ko": "자막 문제 해결",
    },
    "subtitle-ai/overview.md": {
        "zh-CN": "AI 转录与翻译概览",
        "en": "AI Subtitles Overview",
        "ja": "AI 字幕機能の概要",
        "ko": "AI 자막 기능 개요",
    },
    "subtitle-ai/transcription.md": {
        "zh-CN": "本地语音转录",
        "en": "Whisper Transcription",
        "ja": "音声文字起こし",
        "ko": "로컬 음성 전사",
    },
    "subtitle-ai/translation.md": {
        "zh-CN": "大模型字幕翻译",
        "en": "LLM Subtitle Translation",
        "ja": "LLM 字幕翻訳",
        "ko": "LLM 자막 번역",
    },
    "subtitle-ai/models.md": {
        "zh-CN": "模型与硬件加速",
        "en": "AI Models & Acceleration",
        "ja": "AI モデルと加速設定",
        "ko": "AI 모델 및 가속 설정",
    },
    "subtitle-ai/results.md": {
        "zh-CN": "字幕编辑与导出",
        "en": "Subtitle Editing & Export",
        "ja": "字幕の編集と出力",
        "ko": "자막 편집 및 내보내기",
    },
    "audio-and-tools/audio.md": {
        "zh-CN": "音轨与音画同步",
        "en": "Audio Tracks & Sync",
        "ja": "音声トラックと同期",
        "ko": "오디오 트랙 및 싱크",
    },
    "audio-and-tools/audio-enhancement.md": {
        "zh-CN": "音频增强与夜间模式",
        "en": "Audio Enhancement",
        "ja": "音声強化と夜間モード",
        "ko": "오디오 향상 및 야간 모드",
    },
    "audio-and-tools/screenshots.md": {
        "zh-CN": "截图与保存管理",
        "en": "Screenshots & Stills",
        "ja": "スクリーンショット",
        "ko": "스크린샷 및 캡처",
    },
    "audio-and-tools/media-information.md": {
        "zh-CN": "媒体属性与诊断",
        "en": "Media Info & Diagnostics",
        "ja": "メディア情報と診断",
        "ko": "미디어 속성 및 진단",
    },
    "audio-and-tools/dlna.md": {
        "zh-CN": "DLNA 电视投屏",
        "en": "DLNA Wireless Casting",
        "ja": "DLNA ワイヤレス投影",
        "ko": "DLNA 무선 전송",
    },
    "playlist/overview.md": {
        "zh-CN": "播放列表概览",
        "en": "Playlist Overview",
        "ja": "プレイリスト概要",
        "ko": "재생목록 개요",
    },
    "playlist/create-save-load.md": {
        "zh-CN": "播放列表管理",
        "en": "Playlist Management",
        "ja": "プレイリスト管理",
        "ko": "재생목록 관리",
    },
    "playlist/import-folder.md": {
        "zh-CN": "文件夹批量导入",
        "en": "Batch Folder Import",
        "ja": "フォルダ一括追加",
        "ko": "폴더 일괄 가져오기",
    },
    "playlist/search-sort.md": {
        "zh-CN": "搜索、排序与净化",
        "en": "Search, Sort & Clean",
        "ja": "検索・ソート・整形",
        "ko": "검색, 정렬 및 정리",
    },
    "playlist/recent-and-files.md": {
        "zh-CN": "播放历史与文件",
        "en": "Recent History & Files",
        "ja": "再生履歴とファイル",
        "ko": "최근 기록 및 파일",
    },
    "settings/overview.md": {
        "zh-CN": "设置中心",
        "en": "Settings Center",
        "ja": "設定センター",
        "ko": "설정 센터",
    },
    "settings/file-associations.md": {
        "zh-CN": "文件关联与系统集成",
        "en": "File Associations",
        "ja": "ファイル関連付け",
        "ko": "파일 연결 설정",
    },
    "settings/app-data-and-logs.md": {
        "zh-CN": "数据、缓存与日志",
        "en": "App Data & Logs",
        "ja": "データ・キャッシュ・ログ",
        "ko": "데이터, 캐시 및 로그",
    },
    "settings/performance-troubleshooting.md": {
        "zh-CN": "性能调优与排错",
        "en": "Performance Tuning",
        "ja": "性能調整とトラブル",
        "ko": "성능 최적화 및 해결",
    },
    "settings/feedback.md": {
        "zh-CN": "问题反馈与诊断",
        "en": "Feedback & Diagnostics",
        "ja": "フィードバックと診断",
        "ko": "문제 신고 및 피드백",
    },
}

for rel_path, titles in TITLE_MAP.items():
    for lang in ['zh-CN', 'en', 'ja', 'ko']:
        file_path = os.path.join(DOCS_ROOT, lang, rel_path.replace('/', os.sep))
        if not os.path.exists(file_path):
            continue
        with open(file_path, 'r', encoding='utf-8') as fp:
            content = fp.read()
        
        new_title = titles[lang]
        
        # Replace title: "..." in frontmatter
        content = re.sub(
            r'^title:\s*["\'].+?["\']',
            f'title: "{new_title}"',
            content,
            flags=re.MULTILINE
        )
        # Also replace first `# ...` heading
        content = re.sub(
            r'^#\s+(?:[^\n\w]*\s*)?.+$',
            f'# {new_title}',
            content,
            count=1,
            flags=re.MULTILINE
        )
        
        with open(file_path, 'w', encoding='utf-8') as fp:
            fp.write(content)

print("[SUCCESS] All document titles have been streamlined and updated.")
