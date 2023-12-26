import re

BOLD_RE = re.compile(r"__(.*?)__")
ITALICS_RE = re.compile(r"_(.*?)_")
HEADER_RE = re.compile(r"(#+) (.*)")
LIST_RE = re.compile(r"\* (.*)")


def parse(markdown: str) -> str:
    lines = markdown.split("\n")
    result = []
    for line in lines:
        line = BOLD_RE.sub(r"<strong>\1</strong>", line)
        line = ITALICS_RE.sub(r"<em>\1</em>", line)
        is_header = HEADER_RE.match(line)
        is_list = LIST_RE.match(line)
        if is_header and len(is_header.group(1)) <= 6:
            result.append(
                "<h{0}>{1}</h{0}>".format(len(is_header.group(1)), is_header.group(2))
            )
        elif is_list:
            if result and result[-1] == "</ul>":
                result.pop()
            else:
                result.append("<ul>")
            result.extend(["<li>" + is_list.group(1) + "</li>", "</ul>"])
        else:
            result.append("<p>" + line + "</p>")
    return "".join(result)
