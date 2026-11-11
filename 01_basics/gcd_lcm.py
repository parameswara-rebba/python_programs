"""Greatest common divisor (Euclid's algorithm) and least common multiple."""


def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    print("gcd(48, 18) =", gcd(48, 18))
    print("lcm(4, 6)   =", lcm(4, 6))
