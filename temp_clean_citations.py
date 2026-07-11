from pathlib import Path
import re

root = Path(r'd:\smart-image-platform-report\content\1-Worklog')
updated = []
for path in root.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    new_text = re.sub(r'\[cite_start\]', '', text)
    new_text = re.sub(r'\[cite:\s*[0-9,\s]+\]', '', new_text)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        updated.append(str(path))

print(f'Updated {len(updated)} files')
for path in updated:
    print(path)
