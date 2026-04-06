NUM_TEST = 2


class Tree:
    def __init__(self, left, right) -> None:
        self.left: int | Tree = left
        self.right: int | Tree = right

for _ in range(NUM_TEST):
    str_input = input()
    sum_candy = sum(
        int(digit)
        for digit in str_input.replace("(", "").replace(")", "").replace(" ", "")
    )

    

"""
((1 (2 3)) (10 12))
(2 ((4 6) (7 8)))
"""
