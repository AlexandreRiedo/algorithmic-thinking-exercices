import sys
from functools import lru_cache


def solve(m: int, n: int, t: int) -> None:
    calls = 0

    @lru_cache(maxsize=None)
    def solve_t(t: int) -> int:
        nonlocal calls
        calls += 1

        if t == 0:
            return 0

        first = solve_t(t - m) if t >= m else -1
        second = solve_t(t - n) if t >= n else -1

        if first == -1 and second == -1:
            return -1
        return max(first, second) + 1

    result = solve_t(t)

    if result >= 0:
        sys.stdout.write(f"{result}\n")
    else:
        i = t - 1
        while (result := solve_t(i)) == -1:
            i -= 1
        sys.stdout.write(f"{result} {t - i}\n")

    sys.stdout.write(f"Total calls to solve_t: {calls}\n")


def main():
    for line in sys.stdin:
        m, n, t = map(int, line.split())
        solve(m, n, t)


if __name__ == "__main__":
    main()
