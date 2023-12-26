"""Reimplementation of various list operations."""

from collections.abc import Callable
from typing import Any, Union


def append(list1: list[int], list2: list[int]) -> None:
    return list1 + list2


def concat(
    lists: Union[list[Union[list[list[int]], list[list[Any]]]], list[list[int]]],
) -> None:
    return sum(lists, [])


def filter(function: Callable, list: list[int]) -> None:
    return [element for element in list if function(element)]


def length(list: list[int]) -> None:
    return len(list)


def map(function: Callable, list: list[int]) -> None:
    return [function(element) for element in list]


def foldl(function: Callable, list: list[int], initial: int) -> None:
    if not list:
        return initial
    return foldl(function, list[1:], function(initial, list[0]))


def foldr(
    function: Callable,
    list: Union[list[int], list[str]],
    initial: Union[int, str],
) -> None:
    if not list:
        return initial
    return foldr(function, list[:-1], function(initial, list[-1]))


def reverse(
    list: Union[list[list[int]], list[Union[str, float, int]], list[int]],
) -> None:
    return list[::-1]
