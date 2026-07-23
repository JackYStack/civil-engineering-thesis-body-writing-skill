#!/usr/bin/env python3
"""Validate manifest.yaml and static router files for civil-thesis-body-writing."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_ALWAYS_LOAD = [
    "static/core/stance.md",
    "static/core/workflow.md",
    "static/core/output-format.md",
    "static/core/reader-question-sequence.md",
    "static/core/terminology-ledger.md",
]

REQUIRED_AXES = {
    "mode": [
        "thesis-body",
        "paper-sci",
        "target-journal-polish",
        "citation-support",
        "docx-revision",
        "translation-logic",
        "instsci-zotero",
        "thesis-audit",
        "figure-support",
    ],
    "section": [
        "abstract",
        "introduction",
        "literature-review",
        "method",
        "experiment",
        "finite-element",
        "machine-learning",
        "model-application",
        "results-discussion",
        "chapter-summary",
        "conclusion",
    ],
    "source": [
        "user-materials",
        "local-style-corpus",
        "zotero-fulltext",
        "pdf-ocr",
        "instsci",
        "external-search",
    ],
    "operation": [
        "draft",
        "revise",
        "audit",
        "translate-precheck",
        "docx-edit",
        "cite",
        "import-library",
    ],
}

REQUIRED_REFERENCES = [
    "references/index.md",
    "references/meta/task-mode-manifest.md",
    "references/meta/output-contracts.md",
    "references/meta/pressure-test-scenarios.md",
    "references/meta/forward-test-scenarios.md",
    "references/meta/regression-test-checklist.md",
    "references/examples/public-usage-recipes.md",
    "references/meta/external-skill-sources.md",
    "references/workflows/docx-creation-and-formatting.md",
    "references/workflows/docx-ooxml-editing.md",
    "references/workflows/thesis-format-audit.md",
    "references/style/scientific-figure-color.md",
    "references/style/hfut-thesis-word-objects.md",
    "references/workflows/nature-figure-cooperation.md",
]

REQUIRED_VALIDATORS = [
    "scripts/validate_manifest.py",
    "scripts/validate_skill_contracts.py",
    "scripts/validate_pressure_tests.py",
    "scripts/validate_forward_tests.py",
    "scripts/validate_router_entry.py",
    "scripts/validate_local_thesis_corpus.py",
    "scripts/validate_local_paper_style.py",
    "scripts/validate_style_qc.py",
    "scripts/validate_citation_workflow.py",
    "scripts/validate_distribution.py",
    "scripts/test_validate_distribution.py",
    "scripts/validate_all.py",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def value_path(manifest: str, axis: str, value: str) -> str | None:
    pattern = rf"^\s{{4}}{re.escape(value)}:\s+(\S+)\s*$"
    in_axis = False
    for line in manifest.splitlines():
        if re.match(rf"^\s{{2}}{re.escape(axis)}:\s*$", line):
            in_axis = True
            continue
        if in_axis and re.match(r"^\s{2}[a-zA-Z0-9_-]+:\s*$", line):
            return None
        if in_axis:
            match = re.match(pattern, line)
            if match:
                return match.group(1)
    return None


def listed_paths(manifest: str) -> set[str]:
    paths = set(re.findall(r"(?:static|references|scripts)/[A-Za-z0-9_./-]+\.(?:md|py)", manifest))
    return paths


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    manifest_path = root / "manifest.yaml"
    errors: list[str] = []

    if not manifest_path.exists():
        print("missing manifest.yaml")
        return 1

    manifest = read_text(manifest_path)
    paths = listed_paths(manifest)

    for rel in REQUIRED_ALWAYS_LOAD:
        if rel not in paths:
            errors.append(f"always_load missing {rel}")

    for axis, values in REQUIRED_AXES.items():
        if f"  {axis}:" not in manifest:
            errors.append(f"axis missing: {axis}")
            continue
        for value in values:
            rel = value_path(manifest, axis, value)
            if not rel:
                errors.append(f"axis `{axis}` missing value `{value}`")
            elif not (root / rel).exists():
                errors.append(f"axis `{axis}` value `{value}` points to missing file: {rel}")

    for rel in REQUIRED_REFERENCES:
        if rel not in paths:
            errors.append(f"manifest references missing {rel}")

    for rel in REQUIRED_VALIDATORS:
        if rel not in paths:
            errors.append(f"manifest validation list missing {rel}")

    for rel in paths:
        if not (root / rel).exists():
            errors.append(f"manifest path does not exist: {rel}")

    if errors:
        print("Manifest validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    axis_count = sum(len(values) for values in REQUIRED_AXES.values())
    print(f"Manifest validation passed ({axis_count} axis values, {len(paths)} linked files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
