def egg_count(display_value):
    count = 0
    while display_value:
        count += display_value & 1
        display_value >>= 1
    return count
