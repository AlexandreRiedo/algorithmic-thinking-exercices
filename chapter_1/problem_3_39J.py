import sys
from itertools import zip_longest

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

num_deletable_symbols = 0
position_deletable_symbols = []

for index, (char1, char2) in enumerate(zip_longest(str1, str2)):
    if char1 != char2:
        if index < len(str1) - 1 and str1[index + 1:] != str2[index:]:
            break

        same_char_start_index = index
        while same_char_start_index >= 0 and str1[same_char_start_index] == char1:
            same_char_start_index -= 1
        same_char_start_index += 1

        for index in range(same_char_start_index, index + 1):
            num_deletable_symbols += 1
            position_deletable_symbols.append(str(index + 1))
        break

sys.stdout.write(f"{num_deletable_symbols}\n")
sys.stdout.write(" ".join(position_deletable_symbols))
