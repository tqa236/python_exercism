"""Make the tournament table."""


def update_result(team, result):
    """Update the result for one team after one match."""
    team["MP"] = team["MP"] + 1
    if result == "win":
        team["W"] = team["W"] + 1
        team["P"] = team["P"] + 3
    if result == "loss":
        team["L"] = team["L"] + 1
    if result == "draw":
        team["D"] = team["D"] + 1
        team["P"] = team["P"] + 1
    return team


def tally(rows):
    """Make the tournament table."""
    teams = {}
    for row in rows:
        team_1, team_2, result = row.split(";")
        if team_1 not in teams:
            teams[team_1] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        if team_2 not in teams:
            teams[team_2] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        if result == "win":
            teams[team_1] = update_result(teams[team_1], "win")
            teams[team_2] = update_result(teams[team_2], "loss")
        if result == "loss":
            teams[team_1] = update_result(teams[team_1], "loss")
            teams[team_2] = update_result(teams[team_2], "win")
        if result == "draw":
            for team in [team_1, team_2]:
                teams[team] = update_result(teams[team], "draw")
    tables = ["Team                           | MP |  W |  D |  L |  P"]
    for team, value in sorted(teams.items(), key=lambda kv: (-1 * kv[1]["P"], kv[0])):
        row = (
            team.ljust(31)
            + f"|  {value['MP']} |  {value['W']} |  {value['D']} |  {value['L']} |  {value['P']}"
        )
        tables.append(row)
    return tables
