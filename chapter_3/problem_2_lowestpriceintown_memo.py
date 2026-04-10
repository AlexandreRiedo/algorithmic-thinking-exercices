import sys

MAX_NUM_ITEMS = 200
MAX_PRICE = 1_000 * 100
MAX_RESERVED = MAX_PRICE * MAX_NUM_ITEMS + 1.0


def solve(num_items: int, price_table: dict[int, float], memo: list[float]) -> float:
    def solve_item(num_items: int, price_table: dict[int, float]) -> float:
        if num_items == 1:
            return price_table[num_items]
        if memo[num_items] != -1.0:
            return memo[num_items]

        min_price = MAX_RESERVED
        for i in range(1, 1 + num_items // 2):
            a = i
            b = num_items - i

            if memo[a] != -1.0:
                a_solution = memo[a]
            else:
                a_solution = solve_item(a, price_table)
                memo[a] = a_solution

            if memo[b] != -1.0:
                b_solution = memo[b]
            else:
                b_solution = solve_item(b, price_table)
                memo[b] = b_solution

            min_price = min(
                a_solution + b_solution,
                price_table.get(num_items, MAX_RESERVED),
                min_price,
            )

        if memo[num_items] == -1.0:
            memo[num_items] = min_price
        else:
            memo[num_items] = min(min_price, memo[num_items])
        return memo[num_items]

    min_price_extended = MAX_RESERVED
    for num_items_extended in range(num_items, 200):
        min_price_extended = min(
            min_price_extended, solve_item(num_items_extended, price_table)
        )

    return min_price_extended


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

    memo = [-1.0 for _ in range(MAX_NUM_ITEMS + 1)]
    memo[0] = 0.0
    sys.stdout.write(f"Case {test_case}:\n")
    for question in data[idx].split():
        question = max(0, int(question))
        answer = solve(question, price_table, memo)
        sys.stdout.write(f"Buy {question} for ${answer / 100:.2f}\n")

    idx += 1
