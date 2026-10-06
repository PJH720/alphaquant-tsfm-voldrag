# -*- coding: utf-8 -*-
with open('FINAL_PAPER_COMPRESSED_30P.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re
headers = [m.start() for m in re.finditer(r'^#\s+.*', text, re.MULTILINE)]
headers.append(len(text))

sec_names = [
    'Cover & Abstract',
    'Chapter 1: 서론',
    'Chapter 2: 이론적 배경 및 선행연구',
    'Chapter 3: 데이터 및 연구 방법론',
    'Chapter 4: 실증 분석 결과',
    'Chapter 5: 결론 및 정책 시사점',
    'References: 참고문헌'
]

chunks = [text[headers[i]:headers[i+1]] for i in range(len(headers)-1)]

print(f"Current Total: {len(text):,d} chars")
for name, chunk in zip(sec_names, chunks):
    print(f"{name:32s}: {len(chunk):6,d} chars")

# References adjustment:
refs = chunks[-1]
ref_lines = [l.strip() for l in refs.split('\n') if l.strip()]
header_line = ref_lines[0]
citations = ref_lines[1:]
compact_refs = header_line + "\n\n" + "\n".join(citations) + "\n"
print(f"\nCompact references char count: {len(compact_refs):,d} (saved {len(refs) - len(compact_refs):,d} chars)")

# Let's see what total would be with compact references:
new_total = sum(len(c) for c in chunks[:-1]) + len(compact_refs)
print(f"New total with compact references: {new_total:,d} chars")
