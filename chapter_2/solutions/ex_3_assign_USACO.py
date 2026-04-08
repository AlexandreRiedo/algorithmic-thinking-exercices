with open("assign.in", "r") as file:
    n, k = map(int, file.readline().split())
    # NB: make it size n+1 (n = 5 will have values 0-1-2-3-4-5) and just ignore the 0th row/column
    mat = [["" for _ in range(n + 1)] for _ in range(n + 1)]
    breed = [0 for _ in range(n + 1)]

    for _ in range(k):
        parts = file.readline().split()
        c = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        mat[x][y] = c
        mat[y][x] = c


def rec(x: int) -> int:
    count = 0
    if x > n:
        return 1

    for i in range(1, 4):
        conflict = 0
        for j in range(1, x):
            # fmt: off
            if (mat[x][j] == "S" and breed[j] != i) or (mat[x][j] == "D" and breed[j] == i):
                conflict = 1
                break
            # fmt: on
        if not conflict:
            breed[x] = i
            count += rec(x + 1)
            breed[x] = 0

    return count


with open("assign.out", "w") as file:
    file.write(str(rec(1)) + "\n")
