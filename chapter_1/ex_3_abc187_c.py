from collections import defaultdict


def solve():
    num_strings = int(input())
    strings: set[str] = set()
    string_counts: dict[str, int] = defaultdict(int)

    for _ in range(num_strings):
        current_string = input()
        strings.add(current_string.lstrip("!"))
        string_counts[current_string] += 1

    for string in strings:
        if string_counts[string] >= 1:
            if string_counts.get("!" + string, 0) >= 1:
                return string
    return "satisfiable"


if __name__ == "__main__":
    print(solve())
