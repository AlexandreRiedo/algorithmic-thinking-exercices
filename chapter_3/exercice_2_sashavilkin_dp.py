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
current = [-inf for _ in range(num_meals + 1)]
previous = [-inf for _ in range(num_meals + 1)]


def solve(
    start_index: int,
    end_index: int,
    nutritions: list[int],
    current: list[float],
    previous: list[float],
) -> float:
    for i in range(end_index, start_index - 1, -1):
        for j in range(i, end_index + 1):
            if i == j:
                current[j] = nutritions[i]
            else:
                first = previous[j]
                second = current[j - 1]
                third = calc_fullness(i, j, nutritions)
                current[j] = max(first, second, third)
        for k, value in enumerate(current):
            previous[k] = value

    return current[end_index]


print(max(solve(1, num_meals, nutritions, current, previous), 0))

"""
NB DP array:
5
1 -2 3 -4 5
15
[
    [0, 0, 0, 0, 0, 0],
    [0, 1, 3, 6, 10, 15],
    [0, 0, -2, 3, 7, 12],
    [0, 0, 0, 3, 7, 12],
    [0, 0, 0, 0, -4, 5],
    [0, 0, 0, 0, 0, 5]
]
"""