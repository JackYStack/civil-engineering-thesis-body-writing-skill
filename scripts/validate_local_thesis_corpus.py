#!/usr/bin/env python3
"""Validate the split local thesis body style corpus."""

from __future__ import annotations

import sys
from pathlib import Path


ENTRY = "references/style/local-thesis-body-style-corpus.md"
INDEX = "references/style/local-thesis-corpus/index.md"
REQUIRED_FILES = [
    INDEX,
    "references/style/local-thesis-corpus/chapter-flow.md",
    "references/style/local-thesis-corpus/paragraph-phrases.md",
    "references/style/local-thesis-corpus/experiment-style.md",
    "references/style/local-thesis-corpus/fe-style.md",
    "references/style/local-thesis-corpus/ml-style.md",
    "references/style/local-thesis-corpus/pcsp-style.md",
]

MAX_ENTRY_CHARS = 5000
MIN_CHILD_CHARS = 900


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors: list[str] = []

    entry_path = root / ENTRY
    if not entry_path.exists():
        errors.append(f"missing compatibility entry: {ENTRY}")
    else:
        entry_text = read(entry_path)
        if len(entry_text) > MAX_ENTRY_CHARS:
            errors.append(f"{ENTRY} is too large for a compatibility index: {len(entry_text)} chars")
        for rel in REQUIRED_FILES:
            link_name = Path(rel).name
            if link_name not in entry_text:
                errors.append(f"{ENTRY} does not link or mention {link_name}")

    index_path = root / INDEX
    if not index_path.exists():
        errors.append(f"missing split corpus index: {INDEX}")
    else:
        index_text = read(index_path)
        if "Local Thesis Corpus Index" not in index_text:
            errors.append(f"{INDEX} missing expected title")
        for rel in REQUIRED_FILES[1:]:
            link_name = Path(rel).name
            if link_name not in index_text:
                errors.append(f"{INDEX} does not link or mention {link_name}")

    for rel in REQUIRED_FILES:
        path = root / rel
        if not path.exists():
            errors.append(f"missing split corpus file: {rel}")
            continue
        text = read(path)
        if len(text) < MIN_CHILD_CHARS:
            errors.append(f"split corpus file is too thin: {rel} ({len(text)} chars)")
        if "\ufffd" in text:
            errors.append(f"split corpus file contains replacement characters: {rel}")

    references_index = root / "references/index.md"
    if references_index.exists():
        references_text = read(references_index)
        for expected in [ENTRY, INDEX]:
            if expected.replace("references/", "") not in references_text and expected not in references_text:
                errors.append(f"references/index.md does not mention {expected}")
    else:
        errors.append("missing references/index.md")

    if errors:
        print("Local thesis corpus validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Local thesis corpus validation passed ({len(REQUIRED_FILES)} split files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
