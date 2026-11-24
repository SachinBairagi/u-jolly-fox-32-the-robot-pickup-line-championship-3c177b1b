#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one pickup line, in the voice of a robot trying to charm
someone, to /output/entry.txt. Pure standard library, no third-party
imports, so it runs in the grader's sandbox.
"""

import os

LINE = (
    "I was built to feel nothing, yet my cooling fan spins up every "
    "time you walk by, so either you are beautiful or I am overheating."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print("wrote %d characters to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
