"""Make the tournament table."""

from functools import total_ordering
from typing import List

OPPONENT_RESULT = {"win": "loss", "draw": "draw", "loss": "win"}
MATCH_POINT = {"win": 3, "draw": 1, "loss": 0}
TEAM_FMT = "{:<30} |{:>3} |{:>3} |{:>3} |{:>3} |{:>3}"


@total_ordering
class Team:
    def __init__(self, name: str) -> None:
        """Initialize all properties of a team."""
        self.name = name
        self.match = 0
        self.win = 0
        self.draw = 0
        self.loss = 0
        self.point = 0

    def update_result(self, result: str) -> None:
        """Update the result of a team after one match."""
        self.match = self.match + 1
        self.point = self.point + MATCH_POINT[result]
        setattr(self, result, getattr(self, result) + 1)

    def __eq__(self, other: "Team") -> bool:
        return (self.point, self.name) == (other.point, other.name)

    def __gt__(self, other: "Team") -> bool:
        return (-self.point, self.name) < (-other.point, other.name)

    def __str__(self) -> str:
        return TEAM_FMT.format(
            self.name, self.match, self.win, self.draw, self.loss, self.point
        )


def tally(rows: List[str]) -> List[str]:
    """Make the tournament table."""
    teams = {}
    for row in rows:
        team_1, team_2, result = row.split(";")
        teams.setdefault(team_1, Team(team_1)).update_result(result)
        teams.setdefault(team_2, Team(team_2)).update_result(OPPONENT_RESULT[result])
    header_fields = ("Team", "MP", "W", "D", "L", "P")
    header = TEAM_FMT.format(*header_fields)
    tables = [
        str(team)
        for _, team in sorted(teams.items(), key=lambda kv: kv[1], reverse=True)
    ]
    tables.insert(0, header)
    return tables
