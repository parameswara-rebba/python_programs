"""Count how often each word appears in a piece of text."""

import re
from collections import Counter


def word_frequency(text: str) -> Counter:
    return Counter(re.findall(r"[a-z0-9']+", text.lower()))


if __name__ == "__main__":
    sample = "the quick brown fox jumps over the lazy dog. The dog sleeps."
    for word, count in word_frequency(sample).most_common(3):
        print(f"{word}: {count}")
