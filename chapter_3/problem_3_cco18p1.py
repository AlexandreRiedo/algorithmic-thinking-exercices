from functools import lru_cache


def calc_score(index_geese, index_hawks) -> int:
    if geese_outcomes[index_geese] == "W" and hawks_outcomes[index_hawks] == "L":
        if geese_scores[index_geese] > hawks_scores[index_hawks]:
            return geese_scores[index_geese] + hawks_scores[index_hawks]
        else:
            return 0
    elif hawks_outcomes[index_hawks] == "W" and geese_outcomes[index_geese] == "L":
        if hawks_scores[index_hawks] > geese_scores[index_geese]:
            return hawks_scores[index_hawks] + geese_scores[index_geese]
        else:
            return 0
    else:
        return 0


def find_best_hawk(fixed_cursor, moving_cursor) -> int:
    best = 0
    for i in range(moving_cursor, num_games):
        best = max(best, calc_score(fixed_cursor, i))
    return best


def find_best_geese(fixed_cursor, moving_cursor) -> int:
    best = 0
    for i in range(moving_cursor, num_games):
        best = max(best, calc_score(i, fixed_cursor))
    return best


@lru_cache(maxsize=None)
def solve(cursor_geese, cursor_hawks) -> int:
    if cursor_geese == num_games - 1:
        print("GEESE HERE")
        return find_best_hawk(cursor_geese, cursor_hawks)
    elif cursor_hawks == num_games - 1:
        print("HAWK HERE")
        return find_best_geese(cursor_hawks, cursor_geese)

    best = 0
    for explore_geese in range(cursor_geese, num_games):
        print(f"IN explore_geese, {explore_geese=} {cursor_geese=} {cursor_hawks=}")
        if calc_score(explore_geese, cursor_hawks + 1) == 0:
            continue
        if explore_geese <= cursor_hawks + 1:
            continue

        prev_best = best
        best = max(
            best,
            solve(explore_geese, cursor_hawks + 1)
            + calc_score(explore_geese, cursor_hawks + 1),
        )
        if best != prev_best:
            print(f"{best=} {prev_best=}")
            print(f"{cursor_geese=} {cursor_hawks=} {explore_geese=}")

    for explore_hawks in range(cursor_hawks, num_games):
        print(f"IN explore_geese, {explore_hawks=} {cursor_geese=} {cursor_hawks=}")
        if calc_score(cursor_geese + 1, explore_hawks) == 0:
            continue
        if explore_hawks <= cursor_geese + 1:
            continue

        prev_best = best
        best = max(
            best,
            solve(cursor_geese + 1, explore_hawks)
            + calc_score(cursor_geese + 1, explore_hawks),
        )
        if best != prev_best:
            print(f"{best=} {prev_best=}")
            print(f"{cursor_geese=} {cursor_hawks=} {explore_hawks=}")

    return best


num_games = int(input())
geese_outcomes = list(input())
geese_scores = list(map(int, input().split()))
hawks_outcomes = list(input())
hawks_scores = list(map(int, input().split()))


# TESTING
# for cursor_geese in range(num_games):
#     rprint("")
#     for cursor_hawks in range(num_games):
#         rprint(
#             f"{cursor_geese=} {cursor_hawks=} {calc_score(cursor_geese, cursor_hawks)=}"
#         )

# test_cursor_hawks = random.randint(0, num_games - 1)
# rprint(f"{test_cursor_hawks=}")
# rprint(f"{solve(num_games - 1, test_cursor_hawks)=}")

# rprint("\n\n\n")
print(solve(0, 0))

"""
4
WLLW
1 2 3 4
LWWL
6 5 3 2
-> 14

6
LWWLLW
4 5 9 3 2 6
WLLWLW
7 2 6 1 8 9
-> 47

8
LWWLWLWL
7 6 9 5 8 4 3 2
LWLWWWLL
4 5 2 8 1 3 6 7
-> 49
"""

"""
IDEA:
Explore all possibilities by using first the geese, than the hawks.
Go left to right.

Advance from left to right. When picking a pair, 
the pick on the other side can't be to the left of the furthest picked.
"""

"""
IDEA:
Recursion base case is when cursor_geese == 0 or cursor_hawks == 0.
If so, return geese_scores[cursor_geese] + cursor_hawks[cursor_hawks] 
OR 0 if no W/L combo.
"""
