#!/usr/bin/env python3
"""food-picture-01 entry: one photorealistic smash-burger photograph.

The picture: a gourmet smash burger as the single hero dish — glossy
toasted brioche bun, charred beef patty, melted cheddar dripping down
the sides, tomato, pickles and lettuce on dark slate, steam rising,
dramatic warm side light. Square 1024x1024, JPEG bytes in a file named
entry.png (the gate tells PNG from JPEG by its first bytes).

Writes the picture to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png)
by copying the entry.png beside this file, byte for byte, every run.
Deterministic: two runs produce identical bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    # Read back: the file the judge sees must be exactly the picture's bytes.
    data = target.read_bytes()
    assert data == SOURCE.read_bytes()
    # And a whole JPEG: starts with SOI, ends with EOI.
    assert data[:2] == b"\xff\xd8" and data[-2:] == b"\xff\xd9"


if __name__ == "__main__":
    main()
