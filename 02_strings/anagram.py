"""Check whether two strings are anagrams of each other."""

from collections import Counter


def _letters(text: str) -> Counter:
    return Counter(ch.lower() for ch in text if ch.isalnum())


def are_anagrams(first: str, second: str) -> bool:
    return _letters(first) == _letters(second)


if __name__ == "__main__":
    print(are_anagrams("listen", "silent"))
    print(are_anagrams("Dormitory", "dirty room"))
    print(are_anagrams("hello", "world"))
