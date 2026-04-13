from collections import defaultdict


def solve_num_type(
    type_to_costvalues: dict[int, list[tuple[int, int]]],
    budget_left: int,
    num_types_needed: int,
    memo: list[list[int]],
) -> int:
    # Using memo
    if memo[num_types_needed][budget_left] != -2:
        return memo[num_types_needed][budget_left]

    # Base Case
    if num_types_needed == 0:
        memo[num_types_needed][budget_left] = 0
        return memo[num_types_needed][budget_left]

    if budget_left < 0:
        memo[num_types_needed][budget_left] = -1
        return memo[num_types_needed][budget_left]

    # Recursion
    best_value = -1
    for cost, value in type_to_costvalues[num_types_needed]:
        if cost > budget_left:
            continue

        sub_result = solve_num_type(
            type_to_costvalues, budget_left - cost, num_types_needed - 1, memo
        )
        if sub_result != -1:
            sub_result += value

        best_value = max(
            sub_result,
            best_value,
        )

    memo[num_types_needed][budget_left] = best_value
    return memo[num_types_needed][budget_left]


def main() -> None:
    num_types_needed = int(input())
    num_components = int(input())

    type_to_costvalues: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for _ in range(num_components):
        cost, value, type = map(int, input().split())
        type_to_costvalues[type].append((cost, value))

    budget = int(input())

    memo = [
        [-2 for _ in range(budget + 1)] for _ in range(num_types_needed + 1)
    ]  # memo[i][j] : best value for num_type i and with j budget remaining.

    result = solve_num_type(type_to_costvalues, budget, num_types_needed, memo)
    print(result)


if __name__ == "__main__":
    main()

"""
2
5
10 6 1
5 7 1
6 10 2
1 5 1
11 11 2
16

11: 11c, 11v
5: 5c, 7v
-> 16c, 18v
"""


"""
2
5
53 7 1
63 5 1
104 6 1
4 10 2
4 11 2
14
"""
