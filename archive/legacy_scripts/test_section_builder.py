# -*- coding: utf-8 -*-

# Let's inspect the exact lengths of current make_final_submission sections
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

for i in range(len(headers)-1):
    chunk = text[headers[i]:headers[i+1]]
    print(f"{sec_names[i]:35s}: {len(chunk):6,d} chars (with spaces)")

print("-" * 55)
print(f"{'Total':35s}: {len(text):6,d} chars")
