import os
import re

sidebar_file = r'd:\Side\kyna\kyna-release\src\config\docs-sidebar.ts'
docs_root = r'd:\Side\kyna\kyna-release\src\content\docs\zh-CN'

actual_slugs = set()
for root, _, files in os.walk(docs_root):
    for f in files:
        if f.endswith('.md'):
            rel = os.path.relpath(os.path.join(root, f), docs_root)
            slug = rel.replace('\\', '/')[:-3]
            actual_slugs.add(slug)

print(f"Total actual doc files: {len(actual_slugs)}")

with open(sidebar_file, 'r', encoding='utf-8') as fp:
    content = fp.read()

for lang in ['zh-CN', 'en', 'ja', 'ko']:
    pattern = rf"'{lang}':\s*\[(.*?)\]\s*,\s*(?:'[a-zA-Z-]+'|\}};\n|$)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        block = match.group(1)
        sidebar_links = re.findall(r"link:\s*['\"]([^'\"]+)['\"]", block)
        sidebar_set = set(sidebar_links)
        missing = actual_slugs - sidebar_set
        extra = sidebar_set - actual_slugs
        print(f"[{lang}] Sidebar links count: {len(sidebar_links)}")
        if missing:
            print(f"  Missing: {missing}")
        if extra:
            print(f"  Extra: {extra}")
        if not missing and not extra:
            print(f"  [OK] All {len(actual_slugs)} pages are present in the sidebar!")
