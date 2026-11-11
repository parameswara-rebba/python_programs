"""Factorial, computed iteratively and recursively."""


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    return 1 if n <= 1 else n * factorial_recursive(n - 1)


if __name__ == "__main__":
    for n in (0, 1, 5, 10):
        print(f"{n}! = {factorial(n)}")
