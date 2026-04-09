from collections import defaultdict

num_ingredients, num_restricted_pairs = map(int, input().split())
ingredients = set(range(num_ingredients))
restrictions = [set() for _ in range(num_ingredients)]
ingredients_to_restrictions: dict[frozenset, set] = defaultdict(set)
for _ in range(num_restricted_pairs):
    ingredient_a, ingredient_b = map(int, input().split())

    if ingredient_a > ingredient_b:
        ingredient_a, ingredient_b = ingredient_b, ingredient_a
    ingredient_a -= 1
    ingredient_b -= 1

    restrictions[ingredient_a].add(ingredient_b)


def is_valid_pizza(pizza: set[int]) -> bool:
    frozen_pizza = frozenset(pizza)
    if frozen_pizza in ingredients_to_restrictions:
        forbidden_ingredients = ingredients_to_restrictions[frozen_pizza]
    else:
        forbidden_ingredients = set()
        for ingredient in pizza:
            forbidden_ingredients.update(restrictions[ingredient])
        ingredients_to_restrictions[frozen_pizza].update(forbidden_ingredients)

    if len(pizza.intersection(forbidden_ingredients)) == 0:
        return True
    else:
        return False


def solve(pizza: set[int], seen_pizzas: set[frozenset[int]]) -> int:
    total = 0
    for other_ingredient in ingredients - pizza:
        new_pizza = pizza | {other_ingredient}
        if new_pizza in seen_pizzas:
            continue
        if is_valid_pizza(new_pizza):
            seen_pizzas.add(frozenset(new_pizza))
            total += 1 + solve(new_pizza, seen_pizzas)
    return total


print(solve(set(), set()) + 1)
