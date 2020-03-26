from typing import List


def slices(series: str, length: int) -> List[str]:
    if len(series) < length or length <= 0:
        raise ValueError("length is not suitable")
    return [series[i : i + length] for i in range(len(series) - length + 1)]
