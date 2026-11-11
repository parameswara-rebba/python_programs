"""Find files with identical contents under a folder, by SHA-256 hash.

Usage: python find_duplicate_files.py [folder]
It only reports duplicates; it never deletes anything.
"""

import hashlib
import sys
from collections import defaultdict
from pathlib import Path


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def find_duplicates(folder: Path) -> list[list[Path]]:
    by_hash: dict[str, list[Path]] = defaultdict(list)
    for path in sorted(folder.rglob("*")):
        if path.is_file() and not path.is_symlink():
            by_hash[file_hash(path)].append(path)
    return [paths for paths in by_hash.values() if len(paths) > 1]


if __name__ == "__main__":
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    groups = find_duplicates(folder)
    if not groups:
        print("No duplicate files found.")
    for group in groups:
        print("Identical files:")
        for path in group:
            print(f"  {path}")
