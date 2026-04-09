from itertools import product


def main():
    with open("assign.in") as f:
        n, k = map(int, f.readline().split())
        constraints = []
        for _ in range(k):
            rel, x, y = f.readline().split()
            constraints.append((rel, int(x) - 1, int(y) - 1))

    count = sum(
        1
        for assignment in product("HJG", repeat=n)
        if all(
            (assignment[x] == assignment[y])
            if rel == "S"
            else (assignment[x] != assignment[y])
            for rel, x, y in constraints
        )
    )

    with open("assign.out", "w") as f:
        f.write(f"{count}\n")


if __name__ == "__main__":
    main()
