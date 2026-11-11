"""Prime check and the Sieve of Eratosthenes."""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def primes_up_to(limit: int) -> list[int]:
    """Return every prime <= limit using the Sieve of Eratosthenes."""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, limit + 1, i):
                sieve[multiple] = False
    return [n for n, prime in enumerate(sieve) if prime]


if __name__ == "__main__":
    print("97 is prime:", is_prime(97))
    print("Primes up to 50:", primes_up_to(50))
