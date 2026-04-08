import itertools

with open("scode.in", "r") as file:
    final_encrypted = file.readline().strip()


def op_1(s: str) -> str:
    return s[1:] + s


def op_2(s: str) -> str:
    return s[:-1] + s


def op_3(s: str) -> str:
    return s + s[:-1]


def op_4(s: str) -> str:
    return s + s[1:]


def solve(s: str, count) -> None:
    if len(s) <= 2:
        return
    else:
        to_explore = set()
        for i in range(2, len(s)):
            prefix = s[:i]
            to_explore.add(prefix)
        for j in range(1, len(s) - 1):
            suffix = s[j:]
            to_explore.add(suffix)
        for substring in to_explore:
            if op_1(substring) == s:
                next(count)
                solve(substring, count)
            if op_2(substring) == s:
                next(count)
                solve(substring, count)
            if op_3(substring) == s:
                next(count)
                solve(substring, count)
            if op_4(substring) == s:
                next(count)
                solve(substring, count)
        return


count = itertools.count()
with open("scode.out", "w") as file:
    solve(final_encrypted, count)
    file.write(str(next(count)))
