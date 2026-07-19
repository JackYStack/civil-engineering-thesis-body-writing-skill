#!/usr/bin/env python3
"""Validate pressure-test scenario structure for civil-thesis-body-writing."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_FIELDS = [
    "Mode:",
    "Trigger:",
    "Pressure:",
    "Expected response:",
    "Must do:",
    "Must not:",
    "Validation prompt:",
]

MIN_SCENARIOS = 5


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_modes(manifest_text: str) -> set[str]:
    return set(re.findall(r"\| `([^`]+)` \|", manifest_text))


def split_scenarios(text: str) -> list[tuple[str, str]]:
    pattern = re.compile(r"^## Scenario: (.+)$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    scenarios: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        scenarios.append((match.group(1).strip(), text[start:end].strip()))
    return scenarios


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    scenario_path = root / "references/meta/pressure-test-scenarios.md"
    manifest_path = root / "references/meta/task-mode-manifest.md"
    index_path = root / "references/index.md"

    errors: list[str] = []
    for path in [scenario_path, manifest_path, index_path]:
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(root)}")
    if errors:
        print("\n".join(errors))
        return 1

    text = read_text(scenario_path)
    modes = extract_modes(read_text(manifest_path))
    scenarios = split_scenarios(text)

    if len(scenarios) < MIN_SCENARIOS:
        errors.append(f"expected at least {MIN_SCENARIOS} scenarios, found {len(scenarios)}")

    seen_titles: set[str] = set()
    seen_modes: set[str] = set()

    for title, body in scenarios:
        if title in seen_titles:
            errors.append(f"duplicate scenario title: {title}")
        seen_titles.add(title)

        for field in REQUIRED_FIELDS:
            if field not in body:
                errors.append(f"{title}: missing field `{field}`")

        mode_match = re.search(r"Mode:\s*`([^`]+)`", body)
        if not mode_match:
            errors.append(f"{title}: missing backticked mode")
            continue

        mode = mode_match.group(1)
        seen_modes.add(mode)
        if mode not in modes:
            errors.append(f"{title}: unknown mode `{mode}`")

        must_not = body.split("Must not:", 1)[1].split("Validation prompt:", 1)[0] if "Must not:" in body and "Validation prompt:" in body else ""
        if not re.search(r"^- ", must_not, re.MULTILINE):
            errors.append(f"{title}: `Must not` needs bullet items")

    required_mode_coverage = {"thesis-body", "paper-sci", "target-journal-polish", "citation-support", "docx-revision", "translation-logic", "instsci-zotero", "figure-support"}
    missing_coverage = sorted(required_mode_coverage - seen_modes)
    if missing_coverage:
        errors.append(f"missing scenario coverage for modes: {', '.join(missing_coverage)}")

    index_text = read_text(index_path)
    if "meta/pressure-test-scenarios.md" not in index_text:
        errors.append("references/index.md does not reference meta/pressure-test-scenarios.md")

    if errors:
        print("Pressure-test validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Pressure-test validation passed ({len(scenarios)} scenarios).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
