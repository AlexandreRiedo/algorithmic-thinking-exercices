SIZE = 1000


def solve(
    outcome1: str, outcome2: str, goals1: list[int], goals2: list[int], n: int
) -> int:
    previous = [0 for _ in range(SIZE + 1)]
    current = [0 for _ in range(SIZE + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Option 1: Consider the ith Geese and jth Hawks games as rivalry ones. Add the score to the subproblem solution for i-1 and j-1.
            if (
                outcome1[i] == "W" and outcome2[j] == "L" and goals1[i] > goals2[j]
            ) or (outcome1[i] == "L" and outcome2[j] == "W" and goals1[i] < goals2[j]):
                first = previous[j - 1] + goals1[i] + goals2[j]
            else:
                first = 0

            # Option 2: Solving the subproblem for the first i-1 Geese games and j-1 Hawks games (skipping both Geese and Hawks game)
            second = previous[j - 1]

            # Option 3: Solving for the first i-1 Geese games and j Hawks game (skipping a Geese game)
            third = previous[j]

            # Option 4: Solving for the first i Geese games and j-1 Hawks game (skipping a Hawks game)
            fourth = current[j - 1]

            current[j] = max(first, second, third, fourth)

        # Once the row is fully solved, copy it into the previous row list to be used for the next row.
        for k in range(SIZE + 1):
            previous[k] = current[k]

    return current[n]


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
