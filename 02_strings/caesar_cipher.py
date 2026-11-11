"""Caesar cipher: shift each letter by a fixed number of positions."""


def encrypt(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)


if __name__ == "__main__":
    secret = encrypt("Hello, World!", 3)
    print(secret)
    print(decrypt(secret, 3))
