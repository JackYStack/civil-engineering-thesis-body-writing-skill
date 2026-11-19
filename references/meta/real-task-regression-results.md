# Real Task Regression Results

## 2026-11-19: Systematic integration forward checks

One fresh-context executor completed five synthetic user requests using the skill and raw supplied inputs, without being given expected answers or access to the scenario/result/map files. The main executor inspected the returned answers and actual numeric report; this was not five independent reviewers, a blind A/B comparison, or a measure of general accuracy.

Observed outcomes:

- Experimental/FE reporting distinguished repeated measurements from specimen count, calibration from independent validation, and a reported peak discrepancy from unmeasured full-curve/failure accuracy.
- A real read-only helper invocation found an incorrect mean, signed-bias claim and cross-partition group overlap. The main executor reran the archived spec and reproduced the findings. The negative-input report was `FAIL` with exit code 1 and no runtime errors, as intended; source bytes were preserved.
- Excerpt translation retained the negative failure statement, limited loading regime, metric identity and modality; synthetic source material was not passed off as a published citation.
- An incomplete loading/formula note was not promoted to a universal design expression merely because dimensions were consistent; unreadable or unavailable source notation was not guessed.
- Missing current manuscript/reply files and rendering were reported as unavailable. Error-bar overlap and a metadata lookup miss were not treated as scientific equivalence or a false-reference verdict.

Separately, 33 numeric/input/read-only tests, 17 isolated adapter tests and 42 distribution mutation tests passed, along with the skill's structural validators. Scenario-file validation only checked definitions (23 pressure, 13 forward), not execution of every scenario.

Limitations: small purposive synthetic set, one model executor, main-agent review, no sampled population or superiority estimate. No real-paper full translation, equation-derivation certification, FE/ML rerun, production plot export, final Word/PDF render, Zotero write or native-client discovery test was performed. These outcomes cannot be borrowed from upstream packages or inferred from passing structural checks. Private input locations and raw working artifacts are not part of the public package.

## 2026-11-18: Academic prose cleanup comparison

This public-safe summary records an exploratory comparison, not a claim of improved writing quality. The private corpus, source paths, manuscript excerpts, rule snapshots, and raw model outputs are not distributed with this skill.

- Inputs: eight real civil-engineering manuscript excerpts and four newly constructed stress cases, including one English paragraph.
- Conditions: prior writing rules reconstructed from the actual edits versus the integrated cleanup rules; two fresh-context repetitions per condition, four authoring calls and 48 revised outputs in total. The control is not a complete historical repository snapshot.
- Review: 24 masked pairs with randomized X/Y placement. Two fresh-context model reviewers each evaluated one repetition's 12 pairs. Each pair had one reviewer, not two independent ratings.
- Result: all 24 pairs tied under the preregistered rubric; no critical scientific-meaning defect was identified by the reviewers in either condition. All ratings reached the rubric ceiling, limiting its sensitivity.
- Deterministic checks found no numeric/sign-token or paragraph-count changes across the 48 outputs. Token equality does not establish semantic equivalence; targeted manual comparison also checked model/metric mappings and necessary qualifications.
- Both conditions retained material adverse findings, model assumptions, and genuine uncertainty in the tested passages. The older rules already contained technical-disclosure safeguards, so this comparison does not show that the added guidance alone prevented an observed failure.

Interpretation: no clear quality advantage or regression was detected on this small, purpose-selected set. This is neither a statistical superiority/equivalence test nor evidence of detector performance, Word-format safety, source-data correctness, or individual upstream-skill effects. Treat the integration as rule clarification with limited behavioral non-regression evidence, not a verified quality improvement. No manuscript or skill rules were changed during the comparison to manufacture a favorable result.

## Historical Phase 9 Regression

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
