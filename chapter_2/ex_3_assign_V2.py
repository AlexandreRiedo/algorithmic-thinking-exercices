from dataclasses import dataclass

from rich import print as rprint


@dataclass(slots=True)
class Cow:
    position: int
    same_breed: "set[Cow]"
    different_breed: "set[Cow]"

    def __repr__(self) -> str:
        return f"Cow=({self.position=} same_breed=({' '.join(str(cow.position) for cow in self.same_breed)}) different_breed=({' '.join(str(cow.position) for cow in self.different_breed)}))"

    def __hash__(self) -> int:
        return hash(self.position)


with open("assign.in") as file:
    num_cows, num_relationships = map(int, file.readline().split())
    cows_seen: dict[int, Cow] = {}

    for line in file:
        rel_type, cow1, cow2 = line.split()
        cow1 = int(cow1)
        cow2 = int(cow2)

        if cow1 in cows_seen:
            cow1 = cows_seen[cow1]
        else:
            cow1 = Cow(cow1, set(), set())
            cows_seen[cow1.position] = cow1

        if cow2 in cows_seen:
            cow2 = cows_seen[cow2]
        else:
            cow2 = Cow(cow2, set(), set())
            cows_seen[cow2.position] = cow2

        if rel_type == "S":
            cow1.same_breed.add(cow2)
            cow2.same_breed.add(cow1)
        elif rel_type == "D":
            cow1.different_breed.add(cow2)
            cow2.different_breed.add(cow1)


def visit_all_same_breed(cow: Cow, visited: set[Cow]):
    if len(cow.same_breed) == 0:
        visited.add(cow)
    else:
        for cow_neighbor in cow.same_breed - visited:
            visited.add(cow_neighbor)
            visit_all_same_breed(cow_neighbor, visited)


def visit_all_different_breed(cow: Cow, visited: set[Cow]):
    if len(cow.different_breed) == 0:
        visited.add(cow)
    else:
        for cow_neighbor in cow.different_breed - visited:
            visited.add(cow_neighbor)
            visit_all_different_breed(cow_neighbor, visited)


for cow in cows_seen.values():
    rprint(cow)
print("\n\n")

same_breeds_test: set[Cow] = set()
visit_all_same_breed(cows_seen[3], same_breeds_test)
rprint(same_breeds_test)
print("\n\n")

different_breeds_test: set[Cow] = set()
visit_all_different_breed(cows_seen[3], different_breeds_test)
rprint(different_breeds_test)
print("\n\n")


def solve(num_cows) -> int:
    assignments = 0
    for index in range(1, num_cows+1):
        # curr_cow = cows_seen[]
        pass
    return assignments

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

