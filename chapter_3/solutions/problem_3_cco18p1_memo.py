import sys

SIZE = 1000
sys.setrecursionlimit(
    3000
)  # Otherwise it causes a Recursion Depth Error. Still TLEs though.


def solve(
    outcome1: str,
    outcome2: str,
    goals1: list[int],
    goals2: list[int],
    i: int,
    j: int,
    memo: list[list[int]],
) -> int:
    # If the subproblem was already calculated in memo, use it.
    if memo[i][j] != -1:
        return memo[i][j]

    # Base Case
    # NB: Values begin from index 1 onwards, if it's 0, that means we've reached out of games.
    if i == 0 or j == 0:
        memo[i][j] = 0
        return memo[i][j]

    # Option 1: Consider the ith Geese and jth Hawks games as rivalry ones. Add the score to the subproblem solution for i-1 and j-1.
    if (outcome1[i] == "W" and outcome2[j] == "L" and goals1[i] > goals2[j]) or (
        outcome1[i] == "L" and outcome2[j] == "W" and goals1[i] < goals2[j]
    ):
        first = (
            solve(outcome1, outcome2, goals1, goals2, i - 1, j - 1, memo)
            + goals1[i]
            + goals2[j]
        )
    else:
        first = 0

    # Option 2: Solving the subproblem for the first i-1 Geese games and j-1 Hawks games (skipping both Geese and Hawks game).
    second = solve(outcome1, outcome2, goals1, goals2, i - 1, j - 1, memo)

    # Option 3: Solving for the first i-1 Geese games and j Hawks game (skipping a Geese game).
    third = solve(outcome1, outcome2, goals1, goals2, i - 1, j, memo)

    # Option 4: Solving for the first i Geese games and j-1 Hawks game (skipping a Hawks game).
    fourth = solve(outcome1, outcome2, goals1, goals2, i, j - 1, memo)

    memo[i][j] = max(first, second, third, fourth)
    return memo[i][j]


def main() -> None:

    n = int(sys.stdin.readline().strip())
    outcome1 = "_" + sys.stdin.readline().strip()
    goals1 = [0] + [int(item) for item in sys.stdin.readline().strip().split()]
    outcome2 = "_" + sys.stdin.readline().strip()
    goals2 = [0] + [int(item) for item in sys.stdin.readline().strip().split()]
    memo = [
        [-1 for _ in range(SIZE + 1)] for _ in range(SIZE + 1)
    ]  # memo[i][j] is the solution for the first i Geese and first j Hawks games.

    result = solve(outcome1, outcome2, goals1, goals2, n, n, memo)
    sys.stdout.write(f"{result}\n")


if __name__ == "__main__":
    main()
