from typing import List


def grep(pattern: str, flags: str, files: List[str]) -> None:
    return "\n".join([line for line in files if pattern in line])
