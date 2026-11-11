"""Check whether numbers are even or odd."""


def is_even(n: int) -> bool:
    return n % 2 == 0


if __name__ == "__main__":
    for n in (0, 7, 10, -3):
        print(f"{n} is {'even' if is_even(n) else 'odd'}")
