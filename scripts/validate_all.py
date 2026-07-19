#!/usr/bin/env python3
"""Run all available civil-thesis-body-writing skill validators."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run(label: str, command: list[str]) -> int:
    print(f"\n== {label} ==")
    completed = subprocess.run(command)
    return completed.returncode


def main() -> int:
    root = (Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]).resolve()
    python = sys.executable

    validators: list[tuple[str, list[str]]] = [
        ("manifest", [python, "-X", "utf8", str(root / "scripts/validate_manifest.py"), str(root)]),
        ("contracts", [python, "-X", "utf8", str(root / "scripts/validate_skill_contracts.py"), str(root)]),
        ("pressure-tests", [python, "-X", "utf8", str(root / "scripts/validate_pressure_tests.py"), str(root)]),
        ("forward-tests", [python, "-X", "utf8", str(root / "scripts/validate_forward_tests.py"), str(root)]),
        ("router-entry", [python, "-X", "utf8", str(root / "scripts/validate_router_entry.py"), str(root)]),
        ("local-thesis-corpus", [python, "-X", "utf8", str(root / "scripts/validate_local_thesis_corpus.py"), str(root)]),
        ("local-paper-style", [python, "-X", "utf8", str(root / "scripts/validate_local_paper_style.py"), str(root)]),
        ("style-qc", [python, "-X", "utf8", str(root / "scripts/validate_style_qc.py"), str(root)]),
        ("citation-workflow", [python, "-X", "utf8", str(root / "scripts/validate_citation_workflow.py"), str(root)]),
        ("distribution", [python, "-X", "utf8", str(root / "scripts/validate_distribution.py"), str(root)]),
        ("distribution-mutations", [python, "-X", "utf8", str(root / "scripts/test_validate_distribution.py")]),
    ]

    quick_validate = root.parent / ".system" / "skill-creator" / "scripts" / "quick_validate.py"
    if quick_validate.exists():
        validators.append(("quick-validate", [python, "-X", "utf8", str(quick_validate), str(root)]))
    else:
        print(f"WARNING: quick_validate.py not found at {quick_validate}; skipping official skill validation.")

    failures = 0
    for label, command in validators:
        failures += 1 if run(label, command) else 0

    if failures:
        print(f"\nValidation failed: {failures} validator(s) failed.")
        return 1

    print("\nAll validations passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
