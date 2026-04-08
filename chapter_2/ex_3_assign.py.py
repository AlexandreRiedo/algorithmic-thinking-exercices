with open("assign.in") as file:
    num_cows, num_relationships = file.readline().split()
    same_breed_sets: list[set[int]] = []
    different_breed_sets: list[set[int]] = []
    for line in file:
        rel_type, cow1, cow2 = line.split()
        cow1 = int(cow1)
        cow2 = int(cow2)

        if rel_type == "S":
            for same_breed_set in same_breed_sets:
                if cow1 in same_breed_set or cow2 in same_breed_set:
                    same_breed_set.add(cow1)
                    same_breed_set.add(cow2)

                    
            else:
                same_breed_sets.append({cow1, cow2})

print(f"{same_breed_sets=}")