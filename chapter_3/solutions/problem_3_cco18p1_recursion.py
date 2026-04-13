SIZE = 1000


def solve(
    outcome1: str, outcome2: str, goals1: list[int], goals2: list[int], i: int, j: int
) -> int:
    # Base Case
    # NB: Values begin from index 1 onwards, if it's 0, that means we've reached out of games.
    if i == 0 or j == 0:
        return 0

    # Option 1: Consider the ith Geese and jth Hawks games as rivalry ones. Add the score to the subproblem solution for i-1 and j-1.
    if (outcome1[i] == "W" and outcome2[j] == "L" and goals1[i] > goals2[j]) or (
        outcome1[i] == "L" and outcome2[j] == "W" and goals1[i] < goals2[j]
    ):
        first = (
            solve(outcome1, outcome2, goals1, goals2, i - 1, j - 1)
            + goals1[i]
            + goals2[j]
        )
    else:
        first = 0

    # Option 2: Solving the subproblem for the first i-1 Geese games and j-1 Hawks games (skipping both Geese and Hawks game)
    second = solve(outcome1, outcome2, goals1, goals2, i - 1, j - 1)

    # Option 3: Solving for the first i-1 Geese games and j Hawks game (skipping a Geese game)
    third = solve(outcome1, outcome2, goals1, goals2, i - 1, j)

    # Option 4: Solving for the first i Geese games and j-1 Hawks game (skipping a Hawks game)
    fourth = solve(outcome1, outcome2, goals1, goals2, i, j - 1)

    return max(first, second, third, fourth)


def main() -> None:
    n = int(input())
    outcome1 = "_" + input()
    goals1 = [0] + [int(item) for item in input().split()]
    outcome2 = "_" + input()
    goals2 = [0] + [int(item) for item in input().split()]

    result = solve(outcome1, outcome2, goals1, goals2, n, n)
    print(result)


if __name__ == "__main__":
    main()
