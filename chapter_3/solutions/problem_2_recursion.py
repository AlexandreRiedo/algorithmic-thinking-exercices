import sys

SIZE = 200
MAX_SCHEMES = 20


def solve_k(
    num: list[int],
    price: list[float],
    num_schemes: int,
    unit_price: float,
    num_apples: int,
) -> float:
    if num_apples == 0:
        return 0
    else:
        result = solve_k(num, price, num_schemes, unit_price, num_apples - 1)
        best = result + unit_price

        for i in range(0, num_schemes):
            if num_apples - num[i] >= 0:
                result = solve_k(
                    num, price, num_schemes, unit_price, num_apples - num[i]
                )
                best = min(best, result + price[i])
        return best


def solve(
    num: list[int],
    price: list[float],
    num_schemes: int,
    unit_price: float,
    num_apples: int,
) -> float:
    best = solve_k(num, price, num_schemes, unit_price, num_apples)
    for i in range(num_apples + 1, SIZE):
        best = min(best, solve_k(num, price, num_schemes, unit_price, i))

    return best

# TODO: Convert C code to Python
def main():
    input_data = sys.stdin.read().split()

    num = [-1 for _ in range(MAX_SCHEMES)]
    price = [-1.0 for _ in range(MAX_SCHEMES)]
    test_case = 0


if __name__ == "__main__":
    main()
