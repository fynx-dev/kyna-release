#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verification Script for All Multi-Language Docs"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_ROOT = os.path.join(BASE_DIR, 'src', 'content', 'docs')
LANGS = ['zh-CN', 'en', 'ja', 'ko']

def get_markdown_files(lang):
    lang_dir = os.path.join(DOCS_ROOT, lang)
    md_files = set()
    for root, _, files in os.walk(lang_dir):
        for f in files:
            if f.endswith('.md') or f.endswith('.mdx'):
                rel = os.path.relpath(os.path.join(root, f), lang_dir)
                md_files.add(rel.replace('\\', '/'))
    return md_files

print("=== Checking Doc Symmetry Across Languages ===")
files_by_lang = {lang: get_markdown_files(lang) for lang in LANGS}
base_files = files_by_lang['zh-CN']
print(f"Base (zh-CN) Markdown files count: {len(base_files)}")

all_matched = True
for lang in LANGS:
    count = len(files_by_lang[lang])
    diff_missing = base_files - files_by_lang[lang]
    diff_extra = files_by_lang[lang] - base_files
    print(f"[{lang}] Count: {count}")
    if diff_missing:
        print(f"  ❌ Missing in {lang}: {diff_missing}")
        all_matched = False
    if diff_extra:
        print(f"  ❌ Extra in {lang}: {diff_extra}")
        all_matched = False

if all_matched:
    print("[SUCCESS] All 4 languages have 100% symmetric documentation files!")
else:
    print("[ERROR] Documentation files mismatch!")
    sys.exit(1)
