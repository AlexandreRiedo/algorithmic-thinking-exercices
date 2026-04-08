def solve():
    with open("assign.in") as f:
        lines = f.read().split()

    if not lines:
        return

    num_cows = int(lines[0])
    num_relationships = int(lines[1])

    # Adjacency lists to store backward-looking rules
    same_breed = [[] for _ in range(num_cows)]
    diff_breed = [[] for _ in range(num_cows)]

    idx = 2
    for _ in range(num_relationships):
        rel_type = lines[idx]
        # Convert to 0-indexed
        u = int(lines[idx + 1]) - 1
        v = int(lines[idx + 2]) - 1
        idx += 3

        # Ensure 'u' is the smaller index, 'v' is the larger.
        # This guarantees we only check previously assigned cows.
        if u > v:
            u, v = v, u

        if rel_type == "S":
            same_breed[v].append(u)
        else:
            diff_breed[v].append(u)

    # Array to track assignments. -1 means unassigned.
    assign = [-1] * num_cows

    def is_valid(current_cow, breed):
        """Checks if assigning 'breed' violates any rules with already assigned cows."""
        # Check 'Same' constraints
        for prev_cow in same_breed[current_cow]:
            if assign[prev_cow] != breed:
                return False

        # Check 'Different' constraints
        for prev_cow in diff_breed[current_cow]:
            if assign[prev_cow] == breed:
                return False

        return True

    def dfs(current_cow):
        """Recursively explores valid breed assignments."""
        # Base Case: All cows are assigned successfully
        if current_cow == num_cows:
            return 1

        total_ways = 0

        # Try all 3 breeds (0: Holstein, 1: Jersey, 2: Guernsey)
        for breed in (0, 1, 2):
            if is_valid(current_cow, breed):
                assign[current_cow] = breed
                total_ways += dfs(current_cow + 1)

        return total_ways

    ans = dfs(0)

    with open("assign.out", "w") as out_file:
        out_file.write(str(ans) + "\n")


if __name__ == "__main__":
    solve()
