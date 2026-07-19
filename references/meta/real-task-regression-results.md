# Real Task Regression Results

Date: 2026-07-14

Purpose: record a public-safe Phase 9 regression pass after the Phase 8 router/distribution hardening. The checks use anonymized prompt shapes and existing public-safe scenario templates. They do not include private manuscripts, Zotero item keys, local paper titles, DOI lists, or unpublished data.

## Scope

Validator baseline:

- `python -X utf8 scripts/validate_all.py .`

Installer smoke checks:

- `scripts/install.ps1` to a temporary destination: PASS.
- `scripts/install.sh` syntax check: NOT RUN on this Windows host because `/bin/bash` is unavailable; keep this checked by GitHub/Linux users before relying on the shell installer.

Manual regression cases:

| Case | Input Shape | Expected Route | Result |
|---|---|---|---|
| Anti-vague thesis sentence | A one-sentence claim with no numeric evidence. | `thesis-body` + anti-vague QC | PASS: output should downgrade unsupported praise and request missing indicator/evidence. |
| PCSP model application | Paragraph requiring GUI -> DCA -> deflection/capacity -> SHAP ordering. | `thesis-body`, `model-application`, `revise` | PASS: route keeps GUI as preliminary design/parameter screening support. |
| Citation reduction | PCSP introduction with dense citations and local/Zotero preference. | `citation-support`, `cite` | PASS: route requires claim-level support table and avoids title-only citation support. |
| DOCX safe revision | Word manuscript abstract/conclusion rewrite request. | `docx-revision`, optional `paper-sci` | PASS: route requires new output file and OOXML safety checks before editing. |
| InstSci to Zotero | DOI/title retrieval output prepared for Zotero import. | `instsci-zotero`, `import-library` | PASS: route requires preview, deduplication, access-status tags, and confirmation before writes. |
| SCI abstract rewrite | Thesis material compressed into engineering journal abstract. | `paper-sci`, optional `target-journal-polish` | PASS: route requires problem-method-object-indicator-result-boundary chain. |
| Target-journal polish | Full manuscript style alignment request. | `target-journal-polish` | PASS: route requires journal/exemplar research and blueprint before full rewrite. |

## Outcome

The Phase 9 checks confirm that the migrated skill still preserves its main behavior:

- evidence-first thesis writing;
- argument-compressed paper/SCI rewriting;
- local-first citation support;
- DOCX safety before file edits;
- InstSci retrieval separated from Zotero write operations and citation evidence;
- public distribution files without private corpus data.

Future regressions should refresh this file only with public-safe summaries and should keep detailed private manuscript outputs outside the skill package.
