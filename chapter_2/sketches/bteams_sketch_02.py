import itertools
from math import inf

from rich import print as rprint

result = inf
test1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
test5 = {
    241539,
    129390,
    154938,
    565474,
    425945,
    196903,
    630612,
    963680,
    113284,
    605279,
    21744,
    666493,
}
skills = test5
for team1 in itertools.combinations(skills, 3):
    skills_no1 = skills - set(team1)
    for team2 in itertools.combinations(skills_no1, 3):
        skills_no2 = skills_no1 - set(team2)
        for team3 in itertools.combinations(skills_no2, 3):
            team4 = tuple(skills_no2 - set(team3))

            if (
                better_min := max(sum(team) for team in (team1, team2, team3, team4))
                - min((sum(team) for team in (team1, team2, team3, team4)))
            ) < result:
                result = better_min
                rprint(
                    f"New better_min of {better_min} with Team 1: {team1}, Team 2: {team2}, Team 3: {team3}, Team 4: {team4}"
                )
