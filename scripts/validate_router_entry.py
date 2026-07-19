#!/usr/bin/env python3
"""Validate the root router-compressed SKILL.md entry."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_SNIPPETS = [
    "manifest.yaml",
    "static/core/stance.md",
    "static/core/workflow.md",
    "static/core/output-format.md",
    "static/core/reader-question-sequence.md",
    "static/core/terminology-ledger.md",
    "references/index.md",
    "references/meta/task-mode-manifest.md",
    "references/meta/output-contracts.md",
    "references/workflows/docx-ooxml-editing.md",
    "references/workflows/pdf-extraction-and-fulltext-qc.md",
    "references/workflows/nature-figure-cooperation.md",
    "references/meta/pressure-test-scenarios.md",
    "scripts/validate_all.py",
]

REQUIRED_CONCEPTS = [
    "Do not invent",
    "local-first citation support",
    "user's own results",
    "Metadata discovery is not full-text support",
    "Zotero",
    "InstSci",
    "PDF/OCR",
    ".docx",
    "OOXML",
    "anti-vague language QC",
    "nature-figure",
]

FORBIDDEN_VERBOSE_SECTIONS = [
    "## Chapter-Type Defaults",
    "### Common Chapter Logic",
    "## Citation Trigger Rules",
    "## Paragraph Patterns",
    "## Local Evidence Used to Shape This Skill",
]

MAX_BODY_CHARS = 12000
MAX_DESCRIPTION_CHARS = 900


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def body_without_frontmatter(text: str) -> str:
    return re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    skill_path = root / "SKILL.md"
    map_path = root / "references/meta/router-compression-map.md"
    errors: list[str] = []

    if not skill_path.exists():
        errors.append("missing root SKILL.md")
    if not map_path.exists():
        errors.append("missing references/meta/router-compression-map.md")

    if errors:
        print("Router entry validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    skill = read(skill_path)
    body = body_without_frontmatter(skill)
    meta = frontmatter(skill)

    if meta.get("name") != "civil-thesis-body-writing":
        errors.append("frontmatter name must be civil-thesis-body-writing")

    description = meta.get("description", "")
    if not description.startswith("Use when"):
        errors.append("description must start with 'Use when'")
    if len(description) > MAX_DESCRIPTION_CHARS:
        errors.append(f"description too long: {len(description)} characters")

    if len(body) > MAX_BODY_CHARS:
        errors.append(f"router body too long: {len(body)} characters")

    if "\ufffd" in skill:
        errors.append("root SKILL.md contains Unicode replacement characters")

    for snippet in REQUIRED_SNIPPETS:
        if snippet not in skill:
            errors.append(f"root router missing required route snippet: {snippet}")

    for concept in REQUIRED_CONCEPTS:
        if concept not in skill:
            errors.append(f"root router missing required concept: {concept}")

    for heading in FORBIDDEN_VERBOSE_SECTIONS:
        if heading in skill:
            errors.append(f"root router still contains verbose legacy section: {heading}")

    if "Router Compression Map" not in read(map_path):
        errors.append("router-compression-map.md missing expected title")

    if errors:
        print("Router entry validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Router entry validation passed "
        f"(body={len(body)} chars, description={len(description)} chars)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
