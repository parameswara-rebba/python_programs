"""Report disk usage for a path and warn above a threshold.

Usage: python disk_usage.py [path] [threshold-percent]
"""

import shutil
import sys


def usage_percent(path: str = "/") -> float:
    usage = shutil.disk_usage(path)
    return usage.used / usage.total * 100


def human_readable(size: float) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "/"
    threshold = float(sys.argv[2]) if len(sys.argv) > 2 else 80
    usage = shutil.disk_usage(path)
    percent = usage_percent(path)
    print(f"{path}: {human_readable(usage.used)} of {human_readable(usage.total)} used ({percent:.1f}%)")
    if percent >= threshold:
        print(f"WARNING: usage is above {threshold:.0f}%")
        sys.exit(1)
