"""Fibonacci numbers: a list of the first n, and a generator."""


def fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers, starting 0, 1."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def fibonacci_generator():
    """Yield Fibonacci numbers forever."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print(fibonacci(10))
