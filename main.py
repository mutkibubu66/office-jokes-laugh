#!/usr/bin/env python3
"""Write one original one-line joke about office life.

Pure standard library, no network. Writes the joke to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "My boss told me to think outside the box, so I took my laptop to "
    "the parking lot \u2014 now I'm the only one with a window office."
)


def main() -> None:
    assert 1 <= len(LINE) <= 199, "entry line must be 1-199 characters"
    assert "\n" not in LINE and LINE.strip(), "entry must be a single non-blank line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
