"""Linear search and binary search."""


def linear_search(items: list, target) -> int:
    """Return the index of target, or -1. Works on any list. O(n)."""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def binary_search(sorted_items: list, target) -> int:
    """Return the index of target, or -1. The list must be sorted. O(log n)."""
    low, high = 0, len(sorted_items) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_items[mid] == target:
            return mid
        if sorted_items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    data = [2, 5, 8, 12, 16, 23, 38, 56]
    print(linear_search(data, 23))
    print(binary_search(data, 23))
    print(binary_search(data, 7))
