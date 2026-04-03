# UVa 10391 - Compound Words
"""
TO RUN:
Get-Content .\chapter_1\problem_2.txt | python .\chapter_1\problem_2_10391.py
"""

import sys
from collections import defaultdict

data = sys.stdin.readlines()
words = set(word.strip() for word in data)
compound_count = defaultdict(int)

for word_as_prefix in words:
    for word in words:
        if word.startswith(word_as_prefix):
            if word[len(word_as_prefix) :] in words:
                compound_count[word] += 1

result = sorted([word for word, count in compound_count.items() if count == 1])
for answer in result:
    sys.stdout.write(answer + "\n")

"""
a
al
alien
lien
ien

alienista
ista
"""
