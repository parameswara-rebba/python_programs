"""Recursion examples: Tower of Hanoi, permutations, power, digit sum."""


def hanoi(disks: int, source: str = "A", spare: str = "B", target: str = "C") -> list[tuple[str, str]]:
    """Return the moves that solve the Tower of Hanoi."""
    if disks == 0:
        return []
    return (
        hanoi(disks - 1, source, target, spare)
        + [(source, target)]
        + hanoi(disks - 1, spare, source, target)
    )


def permutations(text: str) -> list[str]:
    if len(text) <= 1:
        return [text]
    result = []
    for i, ch in enumerate(text):
        for rest in permutations(text[:i] + text[i + 1:]):
            result.append(ch + rest)
    return result


def power(base: float, exponent: int) -> float:
    """Fast exponentiation by squaring, for a non-negative exponent."""
    if exponent < 0:
        raise ValueError("exponent must be non-negative")
    if exponent == 0:
        return 1
    half = power(base, exponent // 2)
    return half * half * (base if exponent % 2 else 1)


def digit_sum(n: int) -> int:
    n = abs(n)
    return n if n < 10 else n % 10 + digit_sum(n // 10)


if __name__ == "__main__":
    moves = hanoi(3)
    print(f"Hanoi with 3 disks takes {len(moves)} moves: {moves}")
    print(permutations("abc"))
    print(power(2, 10))
    print(digit_sum(12345))
