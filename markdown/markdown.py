"""Markdown parser."""

import re

BOLD_PATTERN = "(.*)__(.*)__(.*)"
ITALIC_PATTERN = "(.*)_(.*)_(.*)"
LIST_PATTERN = r"\* (.*)"


def parse_pattern(text, pattern, convert):
    """Parse a specific pattern (bold or italic)."""
    m = re.match(pattern, text)
    if m:
        text = m.group(1) + f"<{convert}>" + m.group(2) + f"</{convert}>" + m.group(3)
    return text


def parse(markdown):
    """Markdown parser."""
    lines = markdown.split("\n")
    res = ""
    in_list = False

    for i in lines:
        header_range = range(6, 0, -1)
        for header in header_range:
            header_pattern = "#" * header + " (.*)"
            if re.match(header_pattern, i):
                i = f"<h{header}>" + i[header + 1 :] + f"</h{header}>"
                break

        i = parse_pattern(i, BOLD_PATTERN, "strong")
        i = parse_pattern(i, ITALIC_PATTERN, "em")

        m = re.match(LIST_PATTERN, i)
        if m:
            i = "<li>" + m.group(1) + "</li>"
            if not in_list:
                i = "<ul>" + i
                in_list = True
        else:
            if not re.match("<h|<ul|<p|<li", i):
                i = "<p>" + i + "</p>"
            if in_list:
                i = "</ul>" + i
                in_list = False

        res = res + i
    if in_list:
        res = res + "</ul>"
    return res
