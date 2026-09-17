#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kyna Player Documentation List Item Formatter
Reformats long inline list items with titles (e.g. "- **Title**: Description...")
into clean two-line structured items:
- **Title**
  Description...
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_ROOT = os.path.join(BASE_DIR, 'src', 'content', 'docs')

# Matches list items like:
# - **Title**: Description
# - 🔄 **Title** (Extra): Description
# * **Title**：Description
PATTERN = re.compile(
    r'^(\s*[-*]\s+(?:[^\s*`]+?\s+)?\*\*[^*]+?\*\*(?:\s*[(（][^)\n]+[)）])?)\s*[:：]\s*(.+)$',
    re.MULTILINE
)

def reformat_content(text):
    def repl(m):
        header = m.group(1).rstrip()
        desc = m.group(2).strip()
        # Calculate indentation: 2 spaces for standard bullet, or bullet indent + 2
        indent = "  "
        if header.startswith("    ") or header.startswith("\t"):
            indent = "    "
        return f"{header}\n{indent}{desc}"

    return PATTERN.sub(repl, text)

total_files_changed = 0
for root, _, files in os.walk(DOCS_ROOT):
    for f in files:
        if f.endswith('.md') or f.endswith('.mdx'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                original = fp.read()
            
            reformatted = reformat_content(original)
            if reformatted != original:
                with open(p, 'w', encoding='utf-8') as fp:
                    fp.write(reformatted)
                total_files_changed += 1

print(f"[SUCCESS] Formatted list items in {total_files_changed} documentation files.")
