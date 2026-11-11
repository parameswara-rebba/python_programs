"""Write and read a CSV file, then summarise a numeric column."""

import csv
import tempfile
from pathlib import Path

ROWS = [
    {"name": "web-01", "region": "eastus", "cpu": 42},
    {"name": "web-02", "region": "eastus", "cpu": 77},
    {"name": "db-01", "region": "westus", "cpu": 58},
]


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def average(rows: list[dict], column: str) -> float:
    return sum(float(row[column]) for row in rows) / len(rows)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "servers.csv"
        write_csv(path, ROWS)
        rows = read_csv(path)
        for row in rows:
            print(row)
        print(f"average cpu: {average(rows, 'cpu'):.1f}")
