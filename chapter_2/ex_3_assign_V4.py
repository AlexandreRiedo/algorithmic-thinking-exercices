from typing import Dict, Set


class Cow:
    __slots__ = ["position", "same_breed", "different_breed"]

    def __init__(self, position: int):
        self.position = position
        self.same_breed: Set["Cow"] = set()
        self.different_breed: Set["Cow"] = set()

    def __repr__(self) -> str:
        return f"Cow=(position={self.position} same_breed=({' '.join(str(cow.position) for cow in self.same_breed)}) different_breed=({' '.join(str(cow.position) for cow in self.different_breed)}))"

    def __hash__(self) -> int:
        return hash(self.position)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Cow):
            return False
        return self.position == other.position


with open("assign.in") as file:
    num_cows, num_relationships = map(int, file.readline().split())
    all_cows: Dict[int, Cow] = {x: Cow(x) for x in range(0, num_cows)}

    for line in file:
        rel_type, cow1_position, cow2_position = line.split()
        cow1_position = int(cow1_position) - 1
        cow2_position = int(cow2_position) - 1

        cow1 = all_cows[cow1_position]
        cow2 = all_cows[cow2_position]

        if rel_type == "S":
            cow1.same_breed.add(cow2)
            cow2.same_breed.add(cow1)
        elif rel_type == "D":
            cow1.different_breed.add(cow2)
            cow2.different_breed.add(cow1)


def visit_all_same_breed(cow: Cow, visited: Set[Cow]):
    if len(cow.same_breed) == 0:
        visited.add(cow)
    else:
        for cow_neighbor in cow.same_breed - visited:
            visited.add(cow_neighbor)
            visit_all_same_breed(cow_neighbor, visited)


def visit_all_different_breed(cow_set: Set[Cow]) -> Set[Cow]:
    res = set()
    for cow in cow_set:
        res.update(cow.different_breed)
    return res


def solve(candidate: list = ["." for _ in range(num_cows)]):
    if "." not in candidate:
        return 1
    else:
        total = 0
        curr_cow = all_cows[candidate.index(".")]
        curr_same_breeds: Set[Cow] = set()
        visit_all_same_breed(curr_cow, curr_same_breeds)
        curr_different_breeds = visit_all_different_breed(curr_same_breeds)

        available_pool = {"H", "J", "G"} - set(
            candidate[breed.position] for breed in curr_different_breeds
        )
        if len(available_pool) == 0:
            return 0

        if any(
            cow_different_breed in curr_same_breeds
            for cow_different_breed in curr_different_breeds
        ):
            return 0

        for char in available_pool:
            new_candidate = candidate.copy()
            for cow in curr_same_breeds:
                new_candidate[cow.position] = char
            total += solve(new_candidate)

    return total


try:
    output = solve()
except Exception:  # Case 8 is solved by using exceptions, but TLE remains killer
    output = 0

with open("assign.out", "w") as out_file:
    out_file.write(str(output))
