from typing import List


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    lower_word = word.lower()
    sorted_word = sorted(lower_word)
    return [
        candidate
        for candidate in candidates
        if sorted(candidate.lower()) == sorted_word and candidate.lower() != lower_word
    ]
