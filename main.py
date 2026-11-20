#!/usr/bin/env python3
"""Entry point for the 'THE WORLD - 19 November 2026' news-image entry.

The artwork lives in the repository root as entry.png (1024x1024).
This script stages that single image into /output so the harness can
collect it, and then proves the staged copy is byte-identical to the
original by comparing SHA-256 digests of both files.

Standard library only; no third-party dependencies.
"""

import hashlib
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_DIR = Path("/output")


def sha256_of(path: Path) -> str:
    """Return the hex SHA-256 digest of the file at *path*."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    source = Path(__file__).resolve().parent / SOURCE_NAME

    if not source.is_file():
        print(f"error: {SOURCE_NAME} not found next to main.py", file=sys.stderr)
        return 1

    if OUTPUT_DIR.exists() and not OUTPUT_DIR.is_dir():
        print(f"error: {OUTPUT_DIR} exists but is not a directory", file=sys.stderr)
        return 1

    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"error: could not create {OUTPUT_DIR}: {exc}", file=sys.stderr)
        return 1

    destination = OUTPUT_DIR / SOURCE_NAME
    shutil.copyfile(source, destination)

    source_hash = sha256_of(source)
    destination_hash = sha256_of(destination)
    if source_hash != destination_hash:
        print(
            f"error: {destination} differs from {source} "
            f"(source {source_hash}, copy {destination_hash})",
            file=sys.stderr,
        )
        return 1

    print(f"ok: {SOURCE_NAME} copied to {destination} (sha256 {destination_hash})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
