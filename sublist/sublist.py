from typing import List, Union

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def check_sublist(
    sublist_: Union[List[str], List[int]], lst: Union[List[str], List[int]]
) -> bool:
    """Check if a list is an ordered sublist of another list."""
    if not isinstance(sublist_, list):
        raise ValueError("sublist must be a list")
    if not isinstance(lst, list):
        raise ValueError("lst must be a list")

    sublist_len = len(sublist_)
    index = 0

    if sublist_len > len(lst):
        return False
    if sublist_len == 0:
        return True
    for element in lst:
        if element == sublist_[index]:
            index = index + 1
            if index == sublist_len:
                return True
        elif index > 0 and sublist_[index - 1] != element:
            index = 0
    return False


def sublist(
    first_list: Union[List[str], List[int]], second_list: Union[List[str], List[int]]
) -> int:
    """Check the relation of 2 lists."""
    if first_list == second_list:
        return EQUAL

    is_sublist = check_sublist(first_list, second_list)
    is_superlist = check_sublist(second_list, first_list)

    if is_sublist:
        return SUBLIST
    if is_superlist:
        return SUPERLIST
    return UNEQUAL
