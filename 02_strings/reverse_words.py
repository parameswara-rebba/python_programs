"""Reverse a string, and reverse the order of words in a sentence."""


def reverse_string(text: str) -> str:
    return text[::-1]


def reverse_words(sentence: str) -> str:
    return " ".join(reversed(sentence.split()))


if __name__ == "__main__":
    print(reverse_string("python"))
    print(reverse_words("learning python is fun"))
