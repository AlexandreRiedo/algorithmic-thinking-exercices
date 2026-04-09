import sys
from collections import defaultdict

idx = 0
test_case = 0
data = [line.strip() for line in sys.stdin.readlines()]

while idx < len(data):
    test_case += 1
    price_table: dict[int, set[float]] = defaultdict(set)

    unit_price = float(data[idx].split()[0])
    num_prices = int(data[idx].split()[1])
    price_table[1].add(unit_price)
    idx += 1

    for _ in range(num_prices):
        num_items = int(data[idx].split()[0])
        price = float(data[idx].split()[1])
        idx += 1
        price_table[num_items].add(price)

    sys.stdout.write(f"Case {test_case}:\n")
    for question in data[idx].split():
        answer = 22.345  # TODO!
        sys.stdout.write(f"Buy {question} for ${answer:.2f}\n")
    idx += 1
