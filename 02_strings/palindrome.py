"""Palindrome check that ignores case, spaces and punctuation."""


def is_palindrome(text: str) -> bool:
    cleaned = [ch.lower() for ch in text if ch.isalnum()]
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    for text in ("madam", "A man, a plan, a canal: Panama", "python"):
        print(f"{text!r}: {is_palindrome(text)}")
