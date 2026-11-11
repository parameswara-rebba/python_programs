"""Generate random passwords with the cryptographically secure `secrets` module.

Usage: python password_generator.py [length]
"""

import secrets
import string
import sys

SYMBOLS = "!@#$%^&*-_=+"


def generate_password(length: int = 16) -> str:
    """Return a password with at least one lower, upper, digit and symbol."""
    if length < 4:
        raise ValueError("length must be at least 4")
    groups = [string.ascii_lowercase, string.ascii_uppercase, string.digits, SYMBOLS]
    chars = [secrets.choice(group) for group in groups]
    everything = "".join(groups)
    chars += [secrets.choice(everything) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


if __name__ == "__main__":
    length = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    print(generate_password(length))
