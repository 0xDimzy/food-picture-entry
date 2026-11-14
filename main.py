"""Photorealistic smash burger photograph for the food-picture-01 bounty.

The bundled image is a square 1024x1024 JPEG of a gourmet smash burger
served on dark slate. This script performs no image processing at all: it
copies the bundled file byte-for-byte into the output directory the
make.fun harness provides, so every run yields identical bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # Read the copy back and check it is the same whole JPEG we shipped.
    copied = target.read_bytes()
    original = SOURCE.read_bytes()
    assert copied == original, "copied file differs from bundled entry.png"
    assert copied[:2] == b"\xff\xd8", "missing JPEG SOI marker"
    assert copied[-2:] == b"\xff\xd9", "missing JPEG EOI marker"


if __name__ == "__main__":
    main()
