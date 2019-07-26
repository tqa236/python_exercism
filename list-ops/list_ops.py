from typing import Any, Callable, List, Union
def append(list1: List[int], list2: List[int]) -> None:
    pass


def concat(lists: Union[List[Union[List[List[int]], List[List[Any]]]], List[List[int]]]) -> None:
    pass


def filter(function: Callable, list: List[int]) -> None:
    pass


def length(list: List[int]) -> None:
    pass


def map(function: Callable, list: List[int]) -> None:
    pass


def foldl(function: Callable, list: List[int], initial: int) -> None:
    pass


def foldr(function: Callable, list: Union[List[int], List[str]], initial: Union[int, str]) -> None:
    pass


def reverse(list: Union[List[List[int]], List[Union[str, float, int]], List[int]]) -> None:
    pass
