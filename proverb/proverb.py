def proverb(*items, qualifier):
    if not items:
        return []

    lines = []
    for i in range(len(items) - 1):
        lines.append(f"For want of a {items[i]} the {items[i + 1]} was lost.")

    qualifier_prefix = f"{qualifier} " if qualifier else ""
    lines.append(f"And all for the want of a {qualifier_prefix}{items[0]}.")

    return lines
