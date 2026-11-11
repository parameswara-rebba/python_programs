"""Classic sorting algorithms. Each returns a new sorted list."""


def bubble_sort(items: list) -> list:
    """Repeatedly swap adjacent items that are out of order. O(n^2)."""
    result = list(items)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break
    return result


def selection_sort(items: list) -> list:
    """Repeatedly move the smallest remaining item to the front. O(n^2)."""
    result = list(items)
    for i in range(len(result)):
        smallest = min(range(i, len(result)), key=result.__getitem__)
        result[i], result[smallest] = result[smallest], result[i]
    return result


def insertion_sort(items: list) -> list:
    """Insert each item into its place in the sorted part. O(n^2)."""
    result = list(items)
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result


def merge_sort(items: list) -> list:
    """Split in half, sort each half, merge. O(n log n)."""
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left, right = merge_sort(items[:mid]), merge_sort(items[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]


def quick_sort(items: list) -> list:
    """Partition around a pivot, sort each side. O(n log n) on average."""
    if len(items) <= 1:
        return list(items)
    pivot = items[len(items) // 2]
    smaller = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    larger = [x for x in items if x > pivot]
    return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    for sort in (bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort):
        print(f"{sort.__name__:<15} {sort(data)}")
