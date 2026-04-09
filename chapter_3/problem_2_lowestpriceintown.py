import sys

MAX_NUM_ITEMS = 200
MAX_PRICE = 1_000 * 100
RESERVED_DP = MAX_PRICE * MAX_NUM_ITEMS + 1.0


def dp_solve(price_table: dict[int, float]) -> list[float]:
    dp = [RESERVED_DP for _ in range(MAX_NUM_ITEMS + 1)]

    # Base Case, the cheapest way to buy 0 items is with $0.00
    dp[0] = 0
    # Adding in the price_table cases
    for num_item, price in price_table.items():
        dp[num_item] = price

    for curr_num_items in range(1, MAX_NUM_ITEMS + 1):
        # Look through dp to check if combining two optimal purchases is possible
        for i in range(0, 1 + curr_num_items // 2):
            num1 = i
            num2 = curr_num_items - i

            dp[curr_num_items] = min(
                dp[curr_num_items],
                dp[num1] + dp[num2],
                price_table.get(curr_num_items, RESERVED_DP),
            )
    return dp


idx = 0
test_case = 0
data = [line.strip() for line in sys.stdin.readlines()]

while idx < len(data):
    test_case += 1
    price_table: dict[int, float] = {}

    unit_price = float(data[idx].split()[0]) * 100
    num_prices = int(data[idx].split()[1])
    price_table[1] = unit_price
    idx += 1

    for _ in range(num_prices):
        num_items = int(data[idx].split()[0])
        price = float(data[idx].split()[1]) * 100
        idx += 1
        if num_items in price_table:
            price_table[num_items] = min(price_table[num_items], price)
        else:
            price_table[num_items] = price

    dp_solved = dp_solve(price_table)
    sys.stdout.write(f"Case {test_case}:\n")
    for question in data[idx].split():
        question = max(0, int(question))
        answer = min(dp_solved[question:])
        sys.stdout.write(f"Buy {question} for ${answer / 100:.2f}\n")

    idx += 1
