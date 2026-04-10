import sys

SIZE = 200
MAX_SCHEMES = 20


def solve_k(
    num: list[int],
    price: list[float],
    num_schemes: int,
    unit_price: float,
    num_apples: int,
    memo: list[float],
) -> float:
    if memo[num_apples] != -1.0:
        return memo[num_apples]

    if num_apples == 0:
        memo[num_apples] = 0
        return memo[num_apples]
    else:
        result = solve_k(num, price, num_schemes, unit_price, num_apples - 1, memo)
        best = result + unit_price

        for i in range(0, num_schemes):
            if num_apples - num[i] >= 0:
                result = solve_k(
                    num, price, num_schemes, unit_price, num_apples - num[i], memo
                )
                best = min(best, result + price[i])
        memo[num_apples] = best
        return memo[num_apples]


def solve(
    num: list[int],
    price: list[float],
    num_schemes: int,
    unit_price: float,
    num_apples: int,
    memo: list[float],
) -> float:
    best = solve_k(num, price, num_schemes, unit_price, num_apples, memo)
    for i in range(num_apples + 1, SIZE):
        best = min(best, solve_k(num, price, num_schemes, unit_price, i, memo))

    return best


def main():
    input_data = [line.strip() for line in sys.stdin.readlines()]

    num = [-1 for _ in range(MAX_SCHEMES)]
    price = [-1.0 for _ in range(MAX_SCHEMES)]
    memo = [-1.0 for _ in range(SIZE)]
    test_case = 0

    idx = 0
    while idx < len(input_data):
        test_case += 1

        unit_price, num_schemes = input_data[idx].split()
        idx += 1
        unit_price = float(unit_price)
        num_schemes = int(num_schemes)

        for i in range(0, num_schemes):
            num_scheme, price_scheme = input_data[idx].split()
            idx += 1
            num[i] = int(num_scheme)
            price[i] = float(price_scheme)

        sys.stdout.write(f"Case {test_case}:\n")
        for i in range(0, SIZE):
            memo[i] = -1.0

        for num_apples in map(int, input_data[idx].split()):
            result = solve(num, price, num_schemes, unit_price, num_apples, memo)
            sys.stdout.write(f"Buy {num_apples} for ${result:.2f}\n")
        idx += 1


if __name__ == "__main__":
    main()
