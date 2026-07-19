# Thesis-Skills Deterministic Audit Workflow

Use this workflow when `civil-thesis-body-writing` needs to learn from or invoke `quzhiii/thesis-skills` for deterministic thesis/project checks, LaTeX readiness gates, safe fixers, final-audit reports, reference ledgers, claim-citation reports, or submission/defense handoff.

For a format-focused audit matrix that also covers DOCX and PDF adaptation, load [thesis-format-audit.md](thesis-format-audit.md).

`thesis-skills` is not an AI writing assistant and does not generate thesis prose. Treat it as a deterministic audit and delivery layer for LaTeX-oriented thesis projects.

## Installed Commands

On this machine, the stable wrappers are:

```powershell
thesis-check --help
thesis-fix --help
```

They should call a local ASCII-path copy, for example:

```text
<user-home>\.local\share\thesis-skills
```

If a workspace source copy is used, keep it under the current project workspace, for example:

```text
<workspace>\tools\thesis-skills
```

Check `--help` and the installed version before relying on module names or report fields. The upstream repository evolves independently of this workflow.

## When to Use

Use this workflow when the user asks for:

- LaTeX thesis/project checks;
- reference, citation, language, format, content, or compile checks;
- readiness gate before submission, defense, supervisor handoff, or final PDF;
- safe fixer preview/dry-run;
- final-audit report, reference audit ledger, claim-citation triage, or HTML report generation;
- learning deterministic quality gates from thesis-skills and migrating them into writing rules.

Do not use this workflow for:

- ordinary Chinese paragraph drafting;
- Word-only manuscripts unless they have been converted into a supported project structure;
- replacing academic judgment, supervisor decisions, or school rules;
- applying fixes without preview and user confirmation.

## Check Workflow

Start with a smoke test that does not require LaTeX:

```powershell
thesis-check --project-root path\to\thesis --ruleset university-generic --skip-compile
```

If the project has a working LaTeX toolchain and final PDF is required, rerun without `--skip-compile`.

Important reports:

| Report | Use |
|---|---|
| `reports/run-summary.json` | step-by-step checker status |
| `reports/readiness-report.json` | aggregate PASS/WARN/BLOCK gate |
| `reports/check_references-report.json` | reference and citation compatibility |
| `reports/citation-integrity-report.json/.md` | citation risk summary |
| `reports/check_language-report.json` | deterministic language issues |
| `reports/check_language_deep-report.json` | manual-first deeper language screening |
| `reports/check_format-report.json` | labels, references, figures, tables, structure |
| `reports/check_content-report.json` | abstract/content metadata checks |
| `reports/final-cleanup-report.json` | final-process residue and temporary markers |
| `reports/statistical-consistency-report.json` | mixed statistical notation families |
| `reports/manual-anchor-report.json` | manual TOC/LOF/LOT hyperlink-anchor risks |
| `reports/final-audit-report.json` | aggregation of existing final-audit evidence |
| `reports/reference-audit-ledger.csv` | auditable reference evidence ledger |

JSON/CSV artifacts are authoritative. HTML report pages are navigation and reading surfaces, not replacement evidence.

## Format Audit Route

1. Identify the artifact source of truth: LaTeX, DOCX, PDF, or mixed handoff.
2. Select and calibrate a school/journal ruleset against the current specification.
3. Use [thesis-format-audit.md](thesis-format-audit.md) to define dimensions, severities, manual checks, and required evidence.
4. Run deterministic checks without source mutation.
5. Preview only allowlisted fixes; preserve captions, labels, numbering, figures, tables, equations, and references unless separately reviewed.
6. Rerun checks and produce the final delivery bundle.

## Safe Fixer Workflow

Preview before applying:

```powershell
thesis-fix --project-root path\to\thesis --ruleset university-generic --apply false
```

Only apply after the user accepts the planned changes:

```powershell
thesis-fix --project-root path\to\thesis --ruleset university-generic --apply true
```

Rules:

- Prefer `--apply false` for first pass.
- Treat `WARN` as review-needed, not automatic failure.
- Treat `BLOCK` as a gate that must be resolved or explicitly waived by the user.
- Do not run broad apply modes on a user manuscript without a new output copy, backup, or explicit approval.

## Final-Audit Concepts to Migrate into Writing

Borrow these ideas for `civil-thesis-body-writing` audits:

| thesis-skills concept | Writing-skill adaptation |
|---|---|
| readiness gate | classify manuscript status as `PASS / WARN / BLOCK` rather than vague "basically OK" |
| run summary | list which checks were performed and which were not |
| citation integrity | every citation marker must support a concrete claim |
| reference audit ledger | maintain a table of source, claim, support status, and action |
| language deep check | flag manual-review language risks instead of silently rewriting uncertain claims |
| format/content checks | separate formatting issues from content/evidence issues |
| rule pack as policy | keep school/journal requirements and severity outside checker mechanics |
| structured reports as contracts | use machine-readable artifacts as evidence and HTML only as a reading layer |
| final-audit extensions | add cleanup residue, statistical notation, manual anchors, reference scope, and delivery evidence |
| safe fixer | preview changes before applying, especially for Word/LaTeX/OOXML documents |
| final delivery | create a handoff bundle: revised file, reports, unresolved risks, and next actions |

## Output for Civil Thesis Work

When thesis-skills is used or emulated, include:

1. `确定性检查范围`: artifact source of truth, commands/reports used, skipped checks, ruleset/version, project root.
2. `Readiness gate`: PASS/WARN/BLOCK and reasons.
3. `问题分层`: blockers, warnings, informational items.
4. `引用/证据台账`: claim, citation/source, status, required action.
5. `修复建议`: safe automatic fixes, manual fixes, author decisions.
6. `交付清单`: revised files, generated reports, unresolved risks.

## Boundary

- `thesis-skills` is strongest for LaTeX projects and deterministic reports.
- For Word/docx editing, keep using [docx-ooxml-editing.md](docx-ooxml-editing.md).
- For Word/docx format review, adapt [thesis-format-audit.md](thesis-format-audit.md) through OOXML/style/render checks rather than claiming direct LaTeX checker coverage.
- For prose generation, keep using motivation-thread, evidence-bank, anti-vague-language, and citation workflows.
- If a command fails because the project is not LaTeX-like, report the mismatch and fall back to `civil-thesis-body-writing` manual audit tables.
