import sys


def solve_t(m: int, n: int, t: int) -> int:
    if t == 0:
        return 0

    if t >= m:
        first = solve_t(m, n, t - m)
    else:
        first = -1

    if t >= n:
        second = solve_t(m, n, t - n)
    else:
        second = -1

    if first == -1 and second == -1:
        return -1
    else:
        return max(first, second) + 1


def solve(m: int, n: int, t: int) -> None:
    result = solve_t(m, n, t)
    if result >= 0:
        sys.stdout.write(f"{result}\n")
    else:
        i = t - 1
        result = solve_t(m, n, i)
        while result == -1:
            i -= 1
            result = solve_t(m, n, i)
        sys.stdout.write(f"{result} {t - i}\n")


def main():
    for line in sys.stdin.readlines():
        m, n, t = map(int, line.strip().split())
        solve(m, n, t)


if __name__ == "__main__":
    main()
