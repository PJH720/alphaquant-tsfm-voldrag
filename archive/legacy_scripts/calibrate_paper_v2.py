# -*- coding: utf-8 -*-
"""
Fine-tuning character count to precisely 31,000 - 31,500 characters.
"""
import re

with open('FINAL_PAPER_COMPRESSED_30P.md', 'r', encoding='utf-8') as f:
    text = f.read()

print("Original length:", len(text))
