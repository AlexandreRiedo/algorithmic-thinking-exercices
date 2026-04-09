import itertools
import sys


def solve_t(m: int, n: int, t: int, memo: list) -> int:
    next(calls_to_solve_t)

    if memo[t] != -2:
        return memo[t]

    if t == 0:
        memo[t] = 0
        return memo[t]

    if t >= m:
        first = solve_t(m, n, t - m, memo)
    else:
        first = -1

    if t >= n:
        second = solve_t(m, n, t - n, memo)
    else:
        second = -1

    if first == -1 and second == -1:
        memo[t] = -1
        return memo[t]
    else:
        memo[t] = max(first, second) + 1
        return memo[t]


def solve(m: int, n: int, t: int) -> None:
    memo = [-2 for _ in range(t + 1)]

    result = solve_t(m, n, t, memo)

    if result >= 0:
        sys.stdout.write(f"{result}\n")
    else:
        i = t - 1
        result = solve_t(m, n, i, memo)
        while result == -1:
            i -= 1
            result = solve_t(m, n, i, memo)
        sys.stdout.write(f"{result} {t - i}\n")

    # sys.stdout.write(f"Total calls to solve_t: {next(calls_to_solve_t)}\n")


def main():
    for line in sys.stdin.readlines():
        global calls_to_solve_t
        calls_to_solve_t = itertools.count()
        m, n, t = map(int, line.strip().split())
        solve(m, n, t)


if __name__ == "__main__":
    main()
