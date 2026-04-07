"""
1 2 3 4 5 6 | 7 8 9 10 11 12
-> 12 1 7 = 20

2 3 4 5 |6| 8 9 10 11
- Pick 11
- Walk down from the highest according to the lowest value till the sum matches the most (10, 9, 8, 6)
-> 11 2 6 = 20

3 4 5 | 8 9 10
-> 10 5 4 = 19

3 8 9
-> 9 8 3 = 19
"""

"""
1 

2

3

4

"""


"""
2 sized team case
1 2 3 4 5 6 7 8
-> 8 1 = 9

2 3 4 5 6 7
-> 7 2 = 9

3 4 5 6
-> 3 6 = 9

4 5
-> 3 5 = 9
"""


"""
1 sized team case
[1, 4, 7, 14, 21, 32, 50, 66]
[1,2,3,4,5,6,7,8,9,10,11,12]
"""
import itertools
from collections import defaultdict

from rich import print as rprint

test1 = [1, 4, 7, 14, 21, 32, 50, 66]
test2 = [1, 4, 7, 14, 21, 32, 50, 66]
test3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
test4 = [
    337911,
    513734,
    671681,
    940478,
    885835,
    836936,
    855940,
    265186,
    558314,
    749716,
    482129,
    962473,
]
test5 = [
    241539,
    129390,
    154938,
    565474,
    425945,
    196903,
    630612,
    963680,
    113284,
    605279,
    21744,
    666493,
]
test6 = [0, 1, 2, 3, 4, 4, 6, 6, 8, 8, 18, 19]
test7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 25]
result = defaultdict(list)
for cows in itertools.combinations(test7, 4):
    result[max(cows) - min(cows)].append(cows)
rprint(result)
rprint("\n\n")
for key in sorted(result.keys(), key=lambda x: (len(result[x]), x)):
    rprint(f"{key}: {len(result[key])}")
rprint("\n\n")
rprint(
    f"minimum S-s {min(result.keys())} has possibilities {result[min(result.keys())]}"
)
rprint("\n\n")

COMMON_KEYS = [8, 7, 9, 6]
for key in COMMON_KEYS:
    rprint(f"{result[key]=}")
