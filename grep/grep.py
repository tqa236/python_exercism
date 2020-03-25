import string
from typing import List

ILIADFILENAME = "iliad.txt"
ILIADCONTENTS = """Achilles sing, O Goddess! Peleus' son;
His wrath pernicious, who ten thousand woes
Caused to Achaia's host, sent many a soul
Illustrious into Ades premature,
And Heroes gave (so stood the will of Jove)
To dogs and to all ravening fowls a prey,
When fierce dispute had separated once
The noble Chief Achilles from the son
Of Atreus, Agamemnon, King of men."""

MIDSUMMERNIGHTFILENAME = "midsummer-night.txt"
MIDSUMMERNIGHTCONTENTS = """I do entreat your grace to pardon me.
I know not by what power I am made bold,
Nor how it may concern my modesty,
In such a presence here to plead my thoughts;
But I beseech your grace that I may know
The worst that may befall me in this case,
If I refuse to wed Demetrius."""

PARADISELOSTFILENAME = "paradise-lost.txt"
PARADISELOSTCONTENTS = """Of Mans First Disobedience, and the Fruit
Of that Forbidden Tree, whose mortal tast
Brought Death into the World, and all our woe,
With loss of Eden, till one greater Man
Restore us, and regain the blissful Seat,
Sing Heav'nly Muse, that on the secret top
Of Oreb, or of Sinai, didst inspire
That Shepherd, who first taught the chosen Seed"""
FILENAMES = [ILIADFILENAME, MIDSUMMERNIGHTFILENAME, PARADISELOSTFILENAME]
FILES = {
    ILIADFILENAME: ILIADCONTENTS,
    MIDSUMMERNIGHTFILENAME: MIDSUMMERNIGHTCONTENTS,
    PARADISELOSTFILENAME: PARADISELOSTCONTENTS,
}


def grep(pattern: str, flags: str, files: List[str]) -> None:
    content = [line for file in files for line in FILES[file].split("\n")]
    flags = [flag for flag in flags if flag in string.ascii_lowercase]
    if "i" in flags:
        pattern = pattern.lower()
        content = [line.lower() for line in content]
    return "\n".join([line for line in content if pattern in line]) + "\n"
