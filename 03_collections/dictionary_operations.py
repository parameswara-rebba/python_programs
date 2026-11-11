"""Common dictionary tasks: merge, invert, group, sort by value."""

from collections import defaultdict


def merge(first: dict, second: dict) -> dict:
    """Merge two dictionaries; values from `second` win on duplicate keys."""
    return {**first, **second}


def invert(mapping: dict) -> dict:
    """Swap keys and values."""
    return {value: key for key, value in mapping.items()}


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)


def sort_by_value(mapping: dict, reverse: bool = False) -> dict:
    return dict(sorted(mapping.items(), key=lambda item: item[1], reverse=reverse))


if __name__ == "__main__":
    print(merge({"a": 1, "b": 2}, {"b": 3, "c": 4}))
    print(invert({"a": 1, "b": 2}))
    print(group_by_length(["hi", "to", "cat", "dog", "bird"]))
    print(sort_by_value({"x": 3, "y": 1, "z": 2}, reverse=True))
