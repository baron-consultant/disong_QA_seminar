from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'reference/source'
items = json.loads((ROOT / 'reference/inventory.json').read_text(encoding='utf-8'))
packets = []
catalog = ['# 원본 문서 전체 검토 목록', '', 'ZIP의 모든 Markdown을 UTF-8로 읽어 제목·절·체크리스트를 추출한 탐색용 목록입니다. 체크 수는 구현률이 아닙니다.', '']
for i, item in enumerate(items, 1):
    body = (source / item['path']).read_text(encoding='utf-8-sig')
    headings = re.findall(r'^#{1,6} .+', body, re.M)
    done = len(re.findall(r'^\s*[-\d.)]+\s+\[[xX]\]', body, re.M))
    pending = len(re.findall(r'^\s*[-\d.)]+\s+\[ \]', body, re.M))
    item.update(number=i, headings=headings, checked=done, unchecked=pending)
    catalog += [f"## {i:03d}. {item['path']}", '', f"분류: {item['group']} / {item['lines']}행 / 완료 표시 {done} / 미완료 표시 {pending}", '', *headings, '']
    # Omit executable examples and repetitive diagram/SQL blocks from the prose review.
    prose = re.sub(r'```[^\n]*\n.*?```', '[코드·도식 블록: 원본 보존]', body, flags=re.S)
    prose = re.sub(r'\n{3,}', '\n\n', prose)
    packets.append(f"\n===== {i:03d} {item['path']} [{item['group']}] =====\n{prose}")
(ROOT / 'reference/catalog.md').write_text('\n'.join(catalog), encoding='utf-8')
(ROOT / 'reference/inventory.json').write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding='utf-8')
review = ROOT / 'reference/review-packets'
review.mkdir(exist_ok=True)
buf = ''
idx = 1
for text in packets:
    if len(buf) + len(text) > 16000:
        (review / f'{idx:02d}.txt').write_text(buf, encoding='utf-8')
        idx += 1
        buf = ''
    buf += text
if buf:
    (review / f'{idx:02d}.txt').write_text(buf, encoding='utf-8')
print(f'{len(items)} documents; {idx} review packets')
