# UVa 10391 - Compound Words
"""
TO RUN:
Get-Content .\chapter_1\problem_2.txt | python .\chapter_1\problem_2_10391.py
"""

import sys
from collections import defaultdict

data = sys.stdin.readlines()
words = set(word.strip() for word in data)
len_to_prefix = defaultdict(set)
compound_count = defaultdict(int)
result = []

for word in words:
    len_to_prefix[len(word)].add(word)

for word in words:
    for prefix_index in range(len(word)):
        if (
            word[0:prefix_index] in len_to_prefix[prefix_index]
            and word[prefix_index:] in len_to_prefix[len(word) - prefix_index]
        ):
            compound_count[word] += 1

result = sorted([word for word in compound_count.keys()])
for answer in result:
    sys.stdout.write(answer + "\n")
