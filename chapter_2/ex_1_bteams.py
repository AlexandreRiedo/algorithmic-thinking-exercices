import itertools
from math import inf

with open("bteams.in", "r") as file:
    skills = [int(digit.strip()) for digit in file.readlines()]

result = inf
for team1 in itertools.combinations(skills, 3):
    skills_no1 = skills.copy()
    for skill in team1:
        skills_no1.remove(skill)
    for team2 in itertools.combinations(skills_no1, 3):
        skills_no2 = skills_no1.copy()
        for skill in team2:
            skills_no2.remove(skill)
        for team3 in itertools.combinations(skills_no2, 3):
            team4 = skills_no2.copy()
            for skill in team3:
                team4.remove(skill)

            better_min = max(sum(team) for team in (team1, team2, team3, team4)) - min(
                (sum(team) for team in (team1, team2, team3, team4))
            )
            if (better_min) < result:
                result = better_min

with open("bteams.out", "w") as file:
    file.write(str(result))
