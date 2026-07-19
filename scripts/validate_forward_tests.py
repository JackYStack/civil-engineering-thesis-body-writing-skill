#!/usr/bin/env python3
"""Validate fresh-context forward-test scenarios for civil-thesis-body-writing."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SCENARIO_FILE = Path("references/meta/forward-test-scenarios.md")
INDEX_FILE = Path("references/index.md")
TASK_MODE_FILE = Path("references/meta/task-mode-manifest.md")

REQUIRED_FIELDS = [
    "Mode:",
    "Trigger:",
    "Expected axes:",
    "Expected references:",
    "Expected output contract:",
    "Must do:",
    "Must not:",
    "Validation prompt:",
]

REQUIRED_MODE_COVERAGE = {
    "thesis-body",
    "paper-sci",
    "target-journal-polish",
    "citation-support",
    "docx-revision",
    "instsci-zotero",
    "figure-support",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def known_modes(root: Path) -> set[str]:
    text = read_text(root / TASK_MODE_FILE)
    return set(re.findall(r"\| `([^`]+)` \|", text))


def scenario_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^## Scenario: (.+)$", text, flags=re.MULTILINE))
    blocks: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append((match.group(1).strip(), text[start:end]))
    return blocks


def field_line(body: str, field: str) -> str:
    for line in body.splitlines():
        if line.startswith(field):
            return line
    return ""


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors: list[str] = []

    scenario_path = root / SCENARIO_FILE
    index_path = root / INDEX_FILE

    if not scenario_path.exists():
        print(f"missing {SCENARIO_FILE}")
        return 1
    if not index_path.exists():
        print(f"missing {INDEX_FILE}")
        return 1

    text = read_text(scenario_path)
    if "\ufffd" in text:
        errors.append(f"{SCENARIO_FILE} contains replacement characters")

    blocks = scenario_blocks(text)
    if len(blocks) < 5:
        errors.append(f"expected at least 5 forward-test scenarios, found {len(blocks)}")

    modes = known_modes(root)
    seen_modes: set[str] = set()

    for title, body in blocks:
        for field in REQUIRED_FIELDS:
            line = field_line(body.strip(), field)
            if not line:
                errors.append(f"scenario `{title}` missing field `{field}`")
            elif field != "Validation prompt:" and not line.split(":", 1)[1].strip():
                errors.append(f"scenario `{title}` has empty field `{field}`")

        mode_line = field_line(body.strip(), "Mode:")
        scenario_modes = set(re.findall(r"`([^`]+)`", mode_line))
        if not scenario_modes:
            errors.append(f"scenario `{title}` has no backticked mode id")
        for mode in sorted(scenario_modes):
            if mode not in modes:
                errors.append(f"scenario `{title}` uses unknown mode `{mode}`")
        seen_modes.update(scenario_modes)

        if "Must not:" in body and not field_line(body.strip(), "Must not:").split(":", 1)[1].strip():
            errors.append(f"scenario `{title}` has empty forbidden-behavior guardrail")

    missing_modes = REQUIRED_MODE_COVERAGE - seen_modes
    if missing_modes:
        errors.append(f"forward-test scenarios missing mode coverage: {', '.join(sorted(missing_modes))}")

    index_text = read_text(index_path)
    index_rel = str(SCENARIO_FILE.relative_to("references")).replace("\\", "/")
    if index_rel not in index_text and str(SCENARIO_FILE).replace("\\", "/") not in index_text:
        errors.append(f"{INDEX_FILE} does not link {SCENARIO_FILE}")

    if errors:
        print("Forward-test scenario validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Forward-test scenario validation passed ({len(blocks)} scenarios, {len(seen_modes)} covered modes).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
