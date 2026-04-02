num_lines, num_people = map(int, input().split())
lines = [int(line) for line in input().split()]

output = []
for people in range(num_people):
    shortest_idx = lines.index(min(lines))
    output.append(lines[shortest_idx])
    lines[shortest_idx] += 1

for answer in output:
    print(answer)