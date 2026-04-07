from dataclasses import dataclass, field


@dataclass
class Node:
    value: str
    children: "list[Node]" = field(default_factory=list)


def nth_children(node: Node, n: int):
    result: list[Node] = []

    def get_nth_children(node: Node, n: int):
        if n == 0:
            result.append(node)
        else:
            for child_node in node.children:
                get_nth_children(child_node, n - 1)

    get_nth_children(node, n)

    return result


num_test_cases = int(input())
output = []

for test_case in range(num_test_cases):
    num_lines, question = map(
        int, input().split()
    )  # 1=most children, 2=most grandchildren, etc.
    nodes: dict[str, Node] = {}

    for _ in range(num_lines):
        parent_name, _, *children_names = input().split()
        parent_node = nodes.setdefault(parent_name, Node(parent_name))
        for child_name in children_names:
            child_node = nodes.setdefault(child_name, Node(child_name))
            parent_node.children.append(child_node)

    nodes_with_nth_children: list[tuple[str, int]] = []
    for node in nodes.values():
        if valid_nth_children := nth_children(node, question):
            nodes_with_nth_children.append((node.value, len(valid_nth_children)))
    nodes_with_nth_children.sort(key=lambda x: (-x[1], x[0]))

    output.append(f"Tree {test_case + 1}:")
    left_to_print = 3
    for index, (name, num_nth_children) in enumerate(nodes_with_nth_children):
        left_to_print -= 1

        if left_to_print == 0:
            index_tie = index
            while (
                index_tie < len(nodes_with_nth_children)
                and nodes_with_nth_children[index_tie][1] == num_nth_children
            ):
                output.append(
                    f"{nodes_with_nth_children[index_tie][0]} {nodes_with_nth_children[index_tie][1]}"
                )
                index_tie += 1
            break
        else:
            output.append(f"{name} {num_nth_children}")
    output.append("")

output.pop()
for answer in output:
    print(answer)
