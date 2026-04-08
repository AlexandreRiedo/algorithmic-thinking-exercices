from bisect import insort

with open("assign.in") as file:
    num_cows, num_relationships = map(int, file.readline().split())
    same_breeds = []
    different_breeds = []
    relationships = []

    for _ in range(num_relationships):
        rel_type, cow1, cow2 = file.readline().split()
        cow1 = int(cow1) - 1
        cow2 = int(cow2) - 1

        insort(
            relationships,
            (rel_type, min(cow1, cow2), max(cow1, cow2)),
            key=lambda x: (x[1], x[2]),
        )

for rel in relationships:
    if rel[0] == "S":
        for i, same_breed_set in enumerate(same_breeds):
            if rel[1] in same_breed_set or rel[2] in same_breed_set:
                same_breed_set.add(rel[1])
                same_breed_set.add(rel[2])
                break
        else:
            same_breeds.append({rel[1], rel[2]})

    if rel[0] == "D":
        for i, different_breed_set in enumerate(different_breeds):
            if rel[1] in different_breed_set or rel[2] in different_breed_set:
                different_breed_set.add(rel[1])
                different_breed_set.add(rel[2])
                break
        else:
            different_breeds.append({rel[1], rel[2]})

# print(same_breeds)
# print(different_breeds)


def avalaible_chars(chars: str):
    index = len(chars)
    pool = set()

    for same_breed in same_breeds:
        if index in same_breed:
            for to_include_index in same_breed:
                if to_include_index >= index:
                    continue
                # print(f"{same_breed=} {to_include_index=}")
                pool.add(chars[to_include_index])

    if len(pool) == 0:
        pool.update({"H", "G", "J"})

    for different_breed in different_breeds:
        if index in different_breed:
            for to_exclude_index in different_breed:
                if to_exclude_index >= index:
                    continue
                # print(f"{different_breed=} {to_exclude_index=}")
                pool.remove(chars[to_exclude_index])

    return pool


def solve(chars):
    if len(chars) == num_cows - 1:
        return len(avalaible_chars(chars))
    else:
        total = 0

        char_set = avalaible_chars(chars)
        if len(char_set) != 0:
            for char in char_set:
                total += solve(chars + char)

        return total


with open("assign.out", "w") as file:
    file.write(str(solve("")))
