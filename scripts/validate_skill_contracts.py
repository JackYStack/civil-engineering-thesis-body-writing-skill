#!/usr/bin/env python3
"""Validate civil-thesis-body-writing mode and contract wiring."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "references/index.md",
    "references/meta/task-mode-manifest.md",
    "references/meta/output-contracts.md",
    "references/meta/external-skill-sources.md",
    "references/workflows/docx-creation-and-formatting.md",
    "references/workflows/docx-ooxml-editing.md",
    "references/workflows/thesis-format-audit.md",
    "references/style/local-thesis-style.md",
    "references/style/scientific-figure-color.md",
    "references/workflows/nature-figure-cooperation.md",
]

REQUIRED_MODES = [
    "thesis-body",
    "paper-sci",
    "target-journal-polish",
    "citation-support",
    "docx-revision",
    "translation-logic",
    "instsci-zotero",
    "thesis-audit",
    "figure-support",
]

SKILL_REQUIRED_LINKS = [
    "references/meta/task-mode-manifest.md",
    "references/meta/output-contracts.md",
    "references/workflows/docx-creation-and-formatting.md",
    "references/workflows/thesis-format-audit.md",
    "references/style/scientific-figure-color.md",
    "references/workflows/nature-figure-cooperation.md",
]

INDEX_REQUIRED_LINKS = [
    "meta/task-mode-manifest.md",
    "meta/output-contracts.md",
    "meta/external-skill-sources.md",
    "workflows/docx-creation-and-formatting.md",
    "workflows/thesis-format-audit.md",
    "style/scientific-figure-color.md",
    "workflows/nature-figure-cooperation.md",
]

EXTERNAL_SKILL_SOURCES = [
    "https://github.com/Gostyan/docx-skill-4-cn-paper",
    "https://github.com/Yuan1z0825/nature-skills",
    "https://github.com/WUBING2023/PaperSpine",
    "https://github.com/google-deepmind/science-skills",
    "https://github.com/Rimagination/instsci",
    "https://github.com/quzhiii/thesis-skills",
    "https://github.com/zsyggg/paper-craft-skills",
]

DOCX_WORKFLOW_REQUIRED_TERMS = [
    "create / convert / revise",
    "Template precedence",
    "Three-line tables",
    "OMML",
    "Validation ladder",
]

THESIS_FORMAT_AUDIT_REQUIRED_TERMS = [
    "Rule-pack calibration",
    "Format audit matrix",
    "Machine-readable reports are authoritative",
    "Bounded fixes",
    "Final-audit extensions",
]

SCIENTIFIC_FIGURE_COLOR_REQUIRED_TERMS = [
    "Source status",
    "Palette register",
    "Color-role mapping",
    "Color accessibility",
    "Grayscale and print",
    "Journal precedence",
]

NATURE_FIGURE_COOPERATION_REQUIRED_TERMS = [
    "Figure brief",
    "Handoff gate",
    "Backend ownership",
    "Artifact return",
    "Manuscript reintegration",
    "Failure boundaries",
]

THESIS_BODY_GUARDRAIL_REQUIRED_TERMS = [
    "Body-Prose Meta-Discourse Gate",
    "direct technical statement",
    "writing rationale",
]

DOCX_OOXML_REQUIRED_TERMS = [
    "Single-Section Visual Review Scope",
    "changed section pages",
    "full-document visual review",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_markdown_links(root: Path, rel_file: str) -> list[str]:
    path = root / rel_file
    text = read_text(path)
    missing: list[str] = []
    for match in re.finditer(r"\]\(([^)#]+)\)", text):
        raw = match.group(1)
        if raw.startswith(("http://", "https://", "mailto:")):
            continue
        base = path.parent
        target = (base / raw).resolve()
        if not target.exists():
            missing.append(f"{rel_file} -> {raw}")
    return missing


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            errors.append(f"missing required file: {rel}")

    if errors:
        print("\n".join(errors))
        return 1

    skill = read_text(root / "SKILL.md")
    index = read_text(root / "references/index.md")
    manifest = read_text(root / "references/meta/task-mode-manifest.md")
    contracts = read_text(root / "references/meta/output-contracts.md")
    external_sources = read_text(root / "references/meta/external-skill-sources.md")
    docx_workflow = read_text(root / "references/workflows/docx-creation-and-formatting.md")
    docx_ooxml = read_text(root / "references/workflows/docx-ooxml-editing.md")
    thesis_format_audit = read_text(root / "references/workflows/thesis-format-audit.md")
    local_thesis_style = read_text(root / "references/style/local-thesis-style.md")
    scientific_figure_color = read_text(root / "references/style/scientific-figure-color.md")
    nature_figure_cooperation = read_text(root / "references/workflows/nature-figure-cooperation.md")

    for link in SKILL_REQUIRED_LINKS:
        if link not in skill:
            errors.append(f"SKILL.md does not reference {link}")

    for link in INDEX_REQUIRED_LINKS:
        if link not in index:
            errors.append(f"references/index.md does not reference {link}")

    for mode in REQUIRED_MODES:
        if f"`{mode}`" not in manifest:
            errors.append(f"task-mode-manifest missing mode `{mode}`")
        if f"### `{mode}`" not in contracts:
            errors.append(f"output-contracts missing contract `{mode}`")

    for source_url in EXTERNAL_SKILL_SOURCES:
        if source_url not in external_sources:
            errors.append(f"external-skill-sources missing source URL: {source_url}")

    for term in DOCX_WORKFLOW_REQUIRED_TERMS:
        if term not in docx_workflow:
            errors.append(f"docx creation workflow missing required term: {term}")

    for term in THESIS_FORMAT_AUDIT_REQUIRED_TERMS:
        if term not in thesis_format_audit:
            errors.append(f"thesis format audit workflow missing required term: {term}")

    for term in SCIENTIFIC_FIGURE_COLOR_REQUIRED_TERMS:
        if term not in scientific_figure_color:
            errors.append(f"scientific figure color guide missing required term: {term}")

    for term in NATURE_FIGURE_COOPERATION_REQUIRED_TERMS:
        if term not in nature_figure_cooperation:
            errors.append(f"nature-figure cooperation workflow missing required term: {term}")

    for term in THESIS_BODY_GUARDRAIL_REQUIRED_TERMS:
        if term not in local_thesis_style:
            errors.append(f"local thesis style missing body-prose guardrail: {term}")

    for term in DOCX_OOXML_REQUIRED_TERMS:
        if term not in docx_ooxml:
            errors.append(f"docx OOXML workflow missing local visual-review rule: {term}")

    for rel in [
        "SKILL.md",
        "references/index.md",
        "references/meta/task-mode-manifest.md",
        "references/meta/output-contracts.md",
        "references/meta/external-skill-sources.md",
        "references/workflows/docx-creation-and-formatting.md",
        "references/workflows/docx-ooxml-editing.md",
        "references/workflows/thesis-format-audit.md",
        "references/style/local-thesis-style.md",
        "references/style/scientific-figure-color.md",
        "references/workflows/nature-figure-cooperation.md",
    ]:
        errors.extend(check_markdown_links(root, rel))

    if errors:
        print("Contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Contract validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
