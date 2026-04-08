from dataclasses import dataclass, field

from rich import print as rprint


@dataclass(slots=True)
class Cow:
    position: int
    same_breed: "set[Cow]" = field(default_factory=set, compare=False)
    different_breed: "set[Cow]" = field(default_factory=set, compare=False)

    def __repr__(self) -> str:
        return f"Cow=({self.position=} same_breed=({' '.join(str(cow.position) for cow in self.same_breed)}) different_breed=({' '.join(str(cow.position) for cow in self.different_breed)}))"

    def __hash__(self) -> int:
        return hash(self.position)


with open("assign.in") as file:
    num_cows, num_relationships = map(int, file.readline().split())
    all_cows: dict[int, Cow] = {x: Cow(x, set(), set()) for x in range(1, num_cows + 1)}

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
            # cow2.different_breed.add(cow1) # SUPER HACKEY WTF!!!


def visit_all_same_breed(cow: Cow, visited: set[Cow]):
    if len(cow.same_breed) == 0:
        visited.add(cow)
    else:
        for cow_neighbor in cow.same_breed - visited:
            visited.add(cow_neighbor)
            visit_all_same_breed(cow_neighbor, visited)


def visit_all_different_breed(cow_set: set[Cow]):
    res = set()
    for cow in cow_set:
        res.update(cow.different_breed)
    return res


# for cow in all_cows.values():
#     rprint(cow)
# print("\n\n")

# same_breeds_test: set[Cow] = set()
# visit_all_same_breed(all_cows[48], same_breeds_test)
# rprint("SAME BREEDS")
# rprint(same_breeds_test)
# print("\n\n")

# different_breeds_test = visit_all_different_breed(same_breeds_test)
# rprint("DIFFERENT BREEDS FROM THE SAMEBREEDS ABOVE")
# rprint(different_breeds_test)
# print("\n\n")


def solve(num_cows, all_cows: dict[int, Cow]) -> int:
    assignments = 1
    visited_cows: set[Cow] = set()
    for index in range(1, num_cows + 1):
        curr_cow = all_cows[index]
        curr_same_breeds: set[Cow] = set()
        visit_all_same_breed(curr_cow, curr_same_breeds)
        curr_different_breeds = visit_all_different_breed(curr_same_breeds)

        rprint(f"{assignments=}")
        rprint(f"{curr_cow=} {curr_same_breeds=} {curr_different_breeds=}")
        if len(curr_different_breeds) >= 3:
            return 0

        if curr_cow in visited_cows:
            continue
        else:
            visited_cows.update(curr_same_breeds)
            rprint(f"{assignments * (3 - len(curr_different_breeds))=}")
            rprint(f"{len(curr_different_breeds)=}")
            assignments = assignments * (3 - len(curr_different_breeds))
        rprint("")
    return assignments

rprint(all_cows)

print(solve(num_cows, all_cows))

"""
3 * (3 - 1) * 3 
"""

"""
S 1 2
D 1 3
D 1 4

HHGJ
HHJG
GGJH
GGHJ
JJGH
JJHG

HHGG
HHJJ
GGJJ
GGHH
JJGG
JJHH
= 3 * 2 * 2

IDEA: if len(different_breed) >= 3 for any cow, then return 0!

for each same_breed_set/letter : 3 *
if the letter has 1,2,3 different_breed: 2, 1, 0 (impossible)
"""
