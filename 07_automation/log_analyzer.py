"""Summarise a log file: count lines per level and list the error messages.

Usage: python log_analyzer.py [path/to/file.log]
Without a path it analyses a built-in sample.
"""

import re
import sys
from collections import Counter
from pathlib import Path

LINE = re.compile(r"^(?P<time>\S+ \S+) (?P<level>[A-Z]+) (?P<message>.*)$")

SAMPLE = """\
2025-01-10 09:00:01 INFO Service started
2025-01-10 09:00:05 WARNING Disk usage at 81%
2025-01-10 09:01:12 ERROR Connection to database timed out
2025-01-10 09:01:15 INFO Retrying connection
2025-01-10 09:01:20 ERROR Connection to database timed out
2025-01-10 09:02:00 INFO Connection restored
"""


def analyze(text: str) -> tuple[Counter, Counter]:
    """Return (lines per level, occurrences of each error message)."""
    levels: Counter = Counter()
    errors: Counter = Counter()
    for line in text.splitlines():
        match = LINE.match(line)
        if not match:
            continue
        levels[match["level"]] += 1
        if match["level"] == "ERROR":
            errors[match["message"]] += 1
    return levels, errors


if __name__ == "__main__":
    text = Path(sys.argv[1]).read_text(encoding="utf-8") if len(sys.argv) > 1 else SAMPLE
    levels, errors = analyze(text)
    print("Lines per level:")
    for level, count in levels.most_common():
        print(f"  {level:<8} {count}")
    print("Errors:")
    for message, count in errors.most_common():
        print(f"  {count}x {message}")
