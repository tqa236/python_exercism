from typing import List, Tuple


def can_chain(dominoes: List[Tuple[int, int]]) -> None:
    if not dominoes:
        return []
    chain = [dominoes[0]]
    for i in range(1, len(dominoes)):
        pass
    if chain[0][0] != chain[-1][1]:
        return None
    return chain
