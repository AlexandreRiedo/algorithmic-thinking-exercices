with open("scode.in", "r") as file:
    final_encrypted = file.readline().strip()


def solve(s: str) -> int:
    if len(s) == 2:
        return 1
    else:
        sum = 0
        for n in range(1, len(s)):
            if s[:n] == s[n:][-n:]:
                sum += solve(s[n:])
            if s[:n] == s[n:][:n]:
                sum += solve(s[n:])
            if s[-n:] == s[:-n][-n:]:
                sum += solve(s[:-n])
            if s[:n] == s[n:][:n]:
                sum += solve(s[n:])
        return sum


with open("scode.out", "w") as file:
    file.write(str(solve(final_encrypted)))

"""
ABCD

BCD + ABCD(og)
ABC + ABCD(og)
ABCD(og) + BCD
ABCD(og) + ABC


OP1
BCDABCD -> ABCD
Inverse
    take first n chars away and check if the last n are the same
    BCD + ABCD

OP2
ABCABCD -> ABCD
idea:
    take first n chars away and check if the first n chars are the same

OP3
ABCDBCD -> ABCD
idea:
    take last n chars away, check if last n chars are the same

OP4
ABCDABC -> ABCD
idea:
    take first n char way, check if first n chars are the same
"""


"""
1. AB+ABA
OP3 with n=2 -> ABA

2. ABA+BA
OP4 with n=2 -> ABA

3. AB+ABA
OP3 with n=2 -> AB+A
OP2 with n=2 -> AB
"""
