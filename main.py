#!/usr/bin/env python3
"""Entry for the make.fun news-image-20261119 competition.

The competition asks for a program that writes one image summing up the
world's news of Thursday 19 November 2026 to /output/entry.png. The
image shipped with this repository (entry.png) is a front page for that
day: Trump, Xi and Putin hold their first three-way summit in Shenzhen
and issue a Declaration Towards Peace, the International Court of
Justice rules that Myanmar committed genocide against the Rohingya,
Ukraine hits the Crimea bridge for a third time, Israel pushes into
central Gaza, Anthropic's $81.3B IPO smashes the record on its Nasdaq
debut, Cyclone Akvan nears India's east coast, and unrest spreads in
Bangladesh.

Running this program places that image at the required path. Nothing
is fetched, nothing is generated at run time, and nothing depends on
the clock, so repeated runs produce identical bytes. It uses only the
Python 3.13 standard library.

Local check:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

OUTPUT_NAME = "entry.png"
BUNDLED_IMAGE = Path(__file__).resolve().parent / OUTPUT_NAME


def copy_entry() -> Path:
    """Copy the bundled front page to the grader's output directory."""
    if not BUNDLED_IMAGE.is_file():
        print(f"news-image-20261119: bundled image missing: {BUNDLED_IMAGE}", file=sys.stderr)
        raise SystemExit(2)
    destination_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / OUTPUT_NAME
    shutil.copyfile(BUNDLED_IMAGE, destination)
    return destination


def run() -> int:
    written = copy_entry()
    print(f"news-image-20261119: wrote {written} ({written.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(run())
