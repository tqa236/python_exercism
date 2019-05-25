
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def check_sublist(sublist, lst):
    """Check if a list is an ordered sublist of another list."""
    if not isinstance(sublist, list):
        raise ValueError("sublist must be a list")
    if not isinstance(lst, list):
        raise ValueError("lst must be a list")

    sublist_len = len(sublist)
    index = 0

    if sublist_len > len(lst):
        return False
    if sublist_len == 0:
        return True
    for element in lst:
        if element == sublist[index]:
            index = index + 1
            if index == sublist_len:
                return True
        elif index > 0 and sublist[index - 1] != element:
            index = 0
    return False


def check_lists(first_list, second_list):
    """Check the relation of 2 lists."""
    if first_list == second_list:
        return EQUAL

    sublist = check_sublist(first_list, second_list)
    superlist = check_sublist(second_list, first_list)

    if sublist:
        return SUBLIST
    if superlist:
        return SUPERLIST
    return UNEQUAL
