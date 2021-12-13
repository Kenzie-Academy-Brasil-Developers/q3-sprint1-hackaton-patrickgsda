# Seu código aqui
hackathon_1 = ["Team Kenzie", "Team Ateliware", "Team VHSYS", "Team Mirum"]
hackathon_2 = ["Team Ateliware", "Team Kenzie", "Team VHSYS", "Team Mirum"]
hackathon_3 = ["Team Mirum", "Team Ateliware","Team VHSYS", "Team Kenzie"]

def get_score(team_name, teams):
    index_team = teams.index(team_name) + 1
    return ("A " f"{team_name}" " ficou classificada em " f"{index_team}")


get_score_1 = get_score("Team Ateliware", hackathon_1)
print(get_score_1)

get_score_2 = get_score("Team Kenzie", hackathon_1)
print(get_score_2)

get_score_3 = get_score("Team Mirum", hackathon_3)
print(get_score_3)
