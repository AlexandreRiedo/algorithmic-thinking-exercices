import sys
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


num_meals = int(sys.stdin.readline().strip())
nutritions = [0] + [int(item) for item in sys.stdin.readline().strip().split()]
current = [(-inf, -inf) for _ in range(num_meals + 1)]
previous = [(-inf, -inf) for _ in range(num_meals + 1)]


def solve(
    start_index: int,
    end_index: int,
    nutritions: list[int],
    current: list[tuple[float, float]],
    previous: list[tuple[float, float]],
) -> float:
    for i in range(end_index, start_index - 1, -1):
        # Filling in the "current" row
        for j in range(i, end_index + 1):
            # rprint(f"{current=}")
            # rprint(f"{previous=}")
            # rprint(f"{pre_previous=}")
            # rprint("")
            if i == j:
                current[j] = (nutritions[i], nutritions[i])
            else:
                first = previous[j][0]
                second = current[j - 1][0]
                if (j - i) % 2 == 0:
                    third = current[j - 1][1] + nutritions[j]
                else:
                    third = current[j - 1][1] - nutritions[j]
                # third = calc_fullness(i, j, nutritions)
                current[j] = (max(first, second, third), third)

        # Updating the previous rows to reuse in the calculations for the next row
        previous[:] = current

    return current[end_index][0]


sys.stdout.write(f"{max(solve(1, num_meals, nutritions, current, previous), 0)}\n")

"""
3 2 10 5 8 1 6 4 9 7
"""

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

BAD IDEA! The dp array ain't the array of calc_fullness values, don't do this!
TIP:
To calculate dp[1][5],
it's smart to reuse the value of dp[3][5]
and just calc_fullness(1,3,nutritions) + dp[3][5]

BETTER:
dp[1][5] = dp[1+2][5] + dp[1][num_meals-(1+2) = 2]
dp[i][j] = dp[i+2][j] + dp[i][num_meals - (i+2)] #FORMULA

dp[1][3] = dp[3][3] + dp[1][2]
dp[2][4] = dp[4][4] + dp[2][1] # NOPE! Manual calculation needed if any values are missing?
dp[2][5] = dp[4][5] + dp[2][3]
"""
