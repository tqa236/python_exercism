"""Transform legacy to new data format."""


from typing import Dict, List
def transform(legacy_data: Dict[int, List[str]]) -> Dict[str, int]:
    """Transform legacy to new data format."""
    return {
        letter.lower(): score
        for score, letters in legacy_data.items()
        for letter in letters
    }
