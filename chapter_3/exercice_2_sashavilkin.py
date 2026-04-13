from math import inf


def calc_fullness(start_index: int, end_index: int, nutritions: list[int]) -> int:
    """
    NB: end_index is inclusive!
    """
    res = 0

    for i in range(start_index, end_index + 1):
        if (i - start_index) % 2 == 0:
            res += nutritions[i]
        elif (i - start_index) % 2 == 1:
            res -= nutritions[i]
    return res


num_meals = int(input())
nutritions = [0] + [int(item) for item in input().split()]
memo = [
    [-inf for _ in range(num_meals + 1)] for _ in range(num_meals + 1)
]  # memo[i][j] gives the calculation for start_index=i and end_index=j


def solve(
    start_index: int, end_index: int, nutritions: list[int], memo: list[list[float]]
) -> float:
    # Memo
    if memo[start_index][end_index] != -inf:
        return memo[start_index][end_index]

    # Base Case
    if start_index == end_index:
        return nutritions[start_index]

    # Advance start
    first = solve(start_index + 1, end_index, nutritions, memo)

    # Advance left
    second = solve(start_index, end_index - 1, nutritions, memo)

    # Calculate
    third = calc_fullness(start_index, end_index, nutritions)

    memo[start_index][end_index] = max(first, second, third)
    return memo[start_index][end_index]


print(max(solve(1, num_meals, nutritions, memo), 0))
