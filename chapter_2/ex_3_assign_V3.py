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
    all_cows: Dict[int, Cow] = {x: Cow(x) for x in range(1, num_cows + 1)}

    for line in file:
        rel_type, cow1_position, cow2_position = line.split()
        cow1_position = int(cow1_position)
        cow2_position = int(cow2_position)

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


def solve(num_cows, all_cows: Dict[int, Cow]) -> int:
    assignments = 1
    visited_cows: Set[Cow] = set()
    visited_differents: Set[Cow] = set()
    for index in range(1, num_cows + 1):
        curr_cow = all_cows[index]
        curr_same_breeds: Set[Cow] = set()
        visit_all_same_breed(curr_cow, curr_same_breeds)
        curr_different_breeds = visit_all_different_breed(curr_same_breeds)

        if any(
            cow_different_breed in curr_same_breeds
            for cow_different_breed in curr_different_breeds
        ):
            return 0

        # Bug Is Definitely Here!
        if len(curr_different_breeds) >= 2:
            return 0

        if curr_cow in visited_cows:
            continue
        else:
            if any(
                cow_same_breed in visited_differents
                for cow_same_breed in curr_same_breeds
            ):
                assignments = assignments * 2
            else:
                assignments = assignments * 3

            visited_differents.update(curr_different_breeds)
            visited_cows.update(curr_same_breeds)
    return assignments


with open("assign.out", "w") as out_file:
    out_file.write(str(solve(num_cows, all_cows)))
# print(solve(num_cows, all_cows))

"""
5 3
S 1 2
D 1 2
D 1 3
D 1 4

HH (GJ) (GJ) (GJ) (HGJ) = 3 * 2 * 2 * 2 * 3
JJ
GG

"""

"""
INCOHERENCE on cow 4

D 2 1
D 3 1
D 3 2
D 4 1
D 4 2
D 4 3

H J G x

"""

"""
HINT: Maybe a brute-force/recursive approach is better? 
Doing the combinatories seems to lead to nowhere.
"""
