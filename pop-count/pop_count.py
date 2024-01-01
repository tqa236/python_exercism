def egg_count(display_value):
    # Restriction: Do not use bit_count
    return bin(display_value).count("1")
