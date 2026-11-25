#!/usr/bin/env python3
"""Worst Superpower — make.fun entry (u-suroto-worst-superpower-461dcdbe).

Writes one useless-superpower one-liner to <OUTPUT_DIR>/entry.txt
(default /output). Deterministic: the same line every run, no
network, no secrets, no input read from anywhere.

The line is a 2-beat one-liner with the reveal in the last clause:
lasers from the eyes, usable only at 3 a.m. against the hero's own
ceiling — 214 tiny holes so far, and one very patient landlord.
"""

import os
import sys

MAX_CHARS = 140  # bounty limit for the one-liner


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-140 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(f"ERROR: entry is {len(line)} chars, over the "
              f"{MAX_CHARS}-char limit", file=sys.stderr)
        sys.exit(1)


def verify_written(path: str, line: str) -> None:
    """Round-trip check: the file on disk must be byte-for-byte the line.

    Fails loudly (non-zero exit) so a truncated or altered write never
    ships silently.
    """
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != line:
            print(f"ERROR: {path} does not match the entry line",
                  file=sys.stderr)
            sys.exit(1)


LINE = (
    "I can shoot lasers from my eyes, but only at 3 a.m. and only at "
    "my own ceiling: 214 tiny holes so far, and one very patient landlord."
)


def entry_path() -> str:
    """Resolve <OUTPUT_DIR>/entry.txt, creating the directory if needed."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    validate_line(LINE)
    path = entry_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    verify_written(path, LINE)
    print(LINE)


if __name__ == "__main__":
    main()
