SIZE = 1000


def solve(
    outcome1: str, outcome2: str, goals1: list[int], goals2: list[int], n: int
) -> int:
    dp = [[0 for _ in range(SIZE + 1)] for _ in range(SIZE + 1)]

    # dp[i][j] can be solved if the following are also solved:
    # dp[i-1][j-1] (Option 1-2), dp[i-1][j] (Option 3), dp[i][j-1] (Option 4)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Option 1: Consider the ith Geese and jth Hawks games as rivalry ones. Add the score to the subproblem solution for i-1 and j-1.
            if (
                outcome1[i] == "W" and outcome2[j] == "L" and goals1[i] > goals2[j]
            ) or (outcome1[i] == "L" and outcome2[j] == "W" and goals1[i] < goals2[j]):
                first = dp[i - 1][j - 1] + goals1[i] + goals2[j]
            else:
                first = 0

            # Option 2: Solving the subproblem for the first i-1 Geese games and j-1 Hawks games (skipping both Geese and Hawks game)
            second = dp[i - 1][j - 1]

            # Option 3: Solving for the first i-1 Geese games and j Hawks game (skipping a Geese game)
            third = dp[i - 1][j]

            # Option 4: Solving for the first i Geese games and j-1 Hawks game (skipping a Hawks game)
            fourth = dp[i][j - 1]

            dp[i][j] = max(first, second, third, fourth)

    return dp[n][n]


def main() -> None:
    n = int(input())
    outcome1 = "_" + input()
    goals1 = [0] + [int(item) for item in input().split()]
    outcome2 = "_" + input()
    goals2 = [0] + [int(item) for item in input().split()]

    result = solve(outcome1, outcome2, goals1, goals2, n)
    print(result)


if __name__ == "__main__":
    main()
