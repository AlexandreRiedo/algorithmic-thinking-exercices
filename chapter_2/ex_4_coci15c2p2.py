num_ingredients, num_restrictions = map(int, input().split())
ingredients = list(range(num_ingredients))
restrictions = [[-1 for _ in range(num_ingredients)] for _ in range(num_ingredients)]
for _ in range(num_restrictions):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    restrictions[a][b] = b
    restrictions[b][a] = a


def is_valid_new_pizza(pizza: list[int], new_ingredient: int):
    for ingredient in pizza:
        if restrictions[new_ingredient][ingredient] == ingredient:
            return False
    return True


def solve(pizza: list[int], ingredient: int) -> int:
    if ingredient >= num_ingredients:
        return 0

    total = 0
    if is_valid_new_pizza(pizza, ingredient):
        new_pizza = pizza.copy()
        new_pizza.append(ingredient)
        total += 1
        total += solve(new_pizza, ingredient + 1)

    total += solve(pizza, ingredient + 1)

    return total


print(solve([], 0) + 1)
