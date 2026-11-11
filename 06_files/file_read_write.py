"""Write, append to and read a text file, and count its lines and words."""

import tempfile
from pathlib import Path


def write_lines(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_line(path: Path, line: str) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def file_stats(path: Path) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "notes.txt"
        write_lines(path, ["first line", "second line"])
        append_line(path, "third line")
        print(path.read_text(encoding="utf-8"), end="")
        print(file_stats(path))
