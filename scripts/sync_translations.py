#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kyna Player Documentation Multi-language Sync Generator
Translates and synchronizes all 39 zh-CN docs into en, ja, and ko.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_ROOT = os.path.join(BASE_DIR, 'src', 'content', 'docs')

def write_doc(lang, rel_path, content):
    full_path = os.path.join(DOCS_ROOT, lang, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"[{lang}] Generated {rel_path}")

print("Starting multi-language docs generation...")
