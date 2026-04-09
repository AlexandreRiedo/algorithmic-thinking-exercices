import pprint
import sys


def solve(m: int, n: int, t: int) -> None:
    ### DP
    dp = [-2 for _ in range(t + 1)]

    # Base case
    dp[0] = 0

    # Populating the DP
    for i in range(1, t + 1):
        # Number of m-duration burgers that can fit perfectly in the time i
        if i >= m:
            first = dp[i - m]
        else:
            first = -1

        # Number of n-duration burgers that can fit perfectly in the time i
        if i >= n:
            second = dp[i - n]
        else:
            second = -1

        # Assigning the answer to the most number of burgers that can fit in the time i
        if first == -1 and second == -1:
            dp[i] = -1
        else:
            dp[i] = max(first, second) + 1

    ### Solving the main problem
    result = dp[t]
    if result >= 0:
        sys.stdout.write(f"{result}\n")
    else:
        i = t - 1
        result = dp[i]
        while result == -1:
            i -= 1
            result = dp[i]
        sys.stdout.write(f"{result} {t - i}\n")

    pprint.pprint(dp)


def main():
    for line in sys.stdin.readlines():
        m, n, t = map(int, line.strip().split())
        solve(m, n, t)


if __name__ == "__main__":
    main()
