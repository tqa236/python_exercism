def format_real_value(value):
    str_value = f"{value:.2f}"
    while str_value.endswith("0") and "." in str_value:
        str_value = str_value.rstrip("0").rstrip(".")

    return str_value


def determine_unit(value):
    if value >= 1_000_000:
        return "megaohms"
    elif value >= 1_000:
        return "kiloohms"
    return "ohms"


def resistor_label(colors):
    color_to_value = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    tolerance_map = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10,
    }

    if len(colors) == 1:
        return "0 ohms" if colors[0] == "black" else None
    if len(colors) == 4:
        value = color_to_value[colors[0]] * 10 + color_to_value[colors[1]]
        multiplier = 10 ** color_to_value[colors[2]]
        tolerance = tolerance_map.get(colors[3], 0)
        total_value = value * multiplier

    elif len(colors) == 5:
        value = (
            color_to_value[colors[0]] * 100
            + color_to_value[colors[1]] * 10
            + color_to_value[colors[2]]
        )
        multiplier = 10 ** color_to_value[colors[3]]
        tolerance = tolerance_map.get(colors[4], 0)
        total_value = value * multiplier

    else:
        return None

    if total_value >= 1_000_000:
        display_value = total_value / 1_000_000
    elif total_value >= 1_000:
        display_value = total_value / 1_000
    else:
        display_value = total_value

    formatted_value = format_real_value(display_value)
    unit = determine_unit(total_value)
    label = f"{formatted_value} {unit}"
    if tolerance > 0:
        formatted_tolerance = format_real_value(tolerance)
        label += f" ±{formatted_tolerance}%"

    return label
