"""Common list tasks: de-duplicate, flatten, chunk, second largest."""


def remove_duplicates(items: list) -> list:
    """Remove duplicates while keeping the original order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def flatten(nested: list) -> list:
    """Flatten a list nested to any depth."""
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat


def chunk(items: list, size: int) -> list[list]:
    """Split a list into pieces of at most `size` items."""
    if size < 1:
        raise ValueError("size must be at least 1")
    return [items[i:i + size] for i in range(0, len(items), size)]


def second_largest(numbers: list[int]) -> int:
    unique = sorted(set(numbers))
    if len(unique) < 2:
        raise ValueError("need at least two distinct values")
    return unique[-2]


if __name__ == "__main__":
    print(remove_duplicates([3, 1, 3, 2, 1]))
    print(flatten([1, [2, [3, 4]], 5]))
    print(chunk([1, 2, 3, 4, 5], 2))
    print(second_largest([10, 20, 20, 5]))
