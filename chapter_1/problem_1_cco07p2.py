# CCO '07 P2 - Snowflakes
import itertools
from collections import defaultdict


def all_indices(l: tuple[int], value: int) -> list[int]:  # noqa: E741
    indices = []
    left_index = 0

    while value in l[left_index:]:
        value_index = l.index(value, left_index)
        indices.append(value_index)
        left_index = value_index + 1

    return indices


def check_order(a: tuple[int], b: tuple[int]) -> bool:
    test_value = a[0]
    b_test_indices = all_indices(b, test_value)

    for b_test_index in b_test_indices:
        if tuple(b[i % 6] for i in range(b_test_index, b_test_index + 6)) == a:
            return True
        if tuple(b[i % 6] for i in range(b_test_index, b_test_index - 6, -1)) == a:
            return True

    return False


def solve(arm_pools: dict[str, list]) -> str:
    for _, snowflakes in sorted(arm_pools.items(), key=lambda x: -len(x[1])):
        if len(snowflakes) <= 1:
            continue

        for a, b in itertools.combinations(snowflakes, 2):
            if check_order(a, b):
                return "Twin snowflakes found."

    return "No two snowflakes are alike."


num_snowflakes = int(input())
arm_pool_to_snowflakes: dict[str, list[tuple]] = defaultdict(list)
for _ in range(num_snowflakes):
    input_str = input()
    arm_pool = "".join(sorted(input_str.split()))
    snowflake = tuple(map(int, input_str.split()))
    arm_pool_to_snowflakes[arm_pool].append(snowflake)

# NB: This is hack to bypass MLE
arm_pool_to_snowflakes = {k: v for k, v in arm_pool_to_snowflakes.items() if len(v) > 1}

print(solve(arm_pool_to_snowflakes))
