"""Reimplementation of various list operations."""

from typing import Any, Callable, List, Union


def append(list1: List[int], list2: List[int]) -> None:
    return list1 + list2


def concat(
    lists: Union[List[Union[List[List[int]], List[List[Any]]]], List[List[int]]]
) -> None:
    return sum(lists, [])


def filter(function: Callable, list: List[int]) -> None:
    return [element for element in list if function(element)]


def length(list: List[int]) -> None:
    return len(list)


def map(function: Callable, list: List[int]) -> None:
    return [function(element) for element in list]


def foldl(function: Callable, list: List[int], initial: int) -> None:
    if not list:
        return initial
    return foldl(function, list[1:], function(initial, list[0]))


def foldr(
    function: Callable, list: Union[List[int], List[str]], initial: Union[int, str]
) -> None:
    if not list:
        return initial
    return foldr(function, list[:-1], function(list[-1], initial))


def reverse(
    list: Union[List[List[int]], List[Union[str, float, int]], List[int]]
) -> None:
    return list[::-1]
