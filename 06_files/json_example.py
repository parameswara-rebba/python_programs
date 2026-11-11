"""Save a Python object as JSON, load it back and update it."""

import json
import tempfile
from pathlib import Path


def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    config = {"app": "demo", "replicas": 2, "ports": [80, 443], "debug": False}
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "config.json"
        save_json(path, config)
        loaded = load_json(path)
        loaded["replicas"] += 1
        save_json(path, loaded)
        print(path.read_text(encoding="utf-8"))
