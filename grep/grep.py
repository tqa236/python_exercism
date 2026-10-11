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


def grep(pattern: str, flags: str, files: List[str]) -> str:
    flag_set = set(flags.split()) if flags else set()
    ignore_case = "-i" in flag_set
    whole_line = "-x" in flag_set
    invert = "-v" in flag_set
    line_numbers = "-n" in flag_set
    file_names_only = "-l" in flag_set

    pattern_text = pattern.lower() if ignore_case else pattern
    results = []

    for filename in files:
        with open(filename, encoding="utf-8") as handle:
            lines = handle.read().splitlines()

        matches = []
        for number, line in enumerate(lines, start=1):
            text = line.lower() if ignore_case else line
            line_pattern = pattern_text
            if whole_line:
                matched = text == line_pattern
            else:
                matched = line_pattern in text
            if invert:
                matched = not matched

            if matched:
                if file_names_only:
                    matches.append(filename)
                    break
                rendered = line
                if line_numbers and len(files) > 1:
                    rendered = f"{filename}:{number}:{line}"
                elif line_numbers:
                    rendered = f"{number}:{line}"
                elif len(files) > 1:
                    rendered = f"{filename}:{line}"
                else:
                    rendered = line
                matches.append(rendered)

        if file_names_only and matches:
            results.extend(matches)
        elif not file_names_only:
            results.extend(matches)

    if not results:
        return ""
    return "\n".join(results) + "\n"
