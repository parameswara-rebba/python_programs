"""Count vowels and consonants in a string."""

VOWELS = set("aeiou")


def count_vowels_and_consonants(text: str) -> tuple[int, int]:
    vowels = consonants = 0
    for ch in text.lower():
        if ch in VOWELS:
            vowels += 1
        elif ch.isalpha():
            consonants += 1
    return vowels, consonants


if __name__ == "__main__":
    v, c = count_vowels_and_consonants("Hello, World!")
    print(f"vowels={v} consonants={c}")
