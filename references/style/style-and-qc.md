# Style And QC

This file is now a compatibility entry for the former merged style and quality-control guide. Keep this path valid for old prompts, but load the focused QC files below instead of treating this file as the full rulebook.

## Load Order

| File | Load When |
|---|---|
| [qc/index.md](qc/index.md) | You need the QC map and a quick choice of which focused guide to open. |
| [qc/failure-mode-diagnosis.md](qc/failure-mode-diagnosis.md) | A draft feels wrong, the user asks for review, or revision scope is unclear. |
| [qc/claim-evidence-boundary.md](qc/claim-evidence-boundary.md) | A paragraph contains claims, citations, results, mechanisms, or design recommendations. |
| [qc/final-polish-checklist.md](qc/final-polish-checklist.md) | Before returning a polished section, audit report, Word revision summary, or manuscript-level output. |

## Compatibility Rules

- For ordinary sentence polishing, first check [anti-vague-language.md](anti-vague-language.md), then use [qc/claim-evidence-boundary.md](qc/claim-evidence-boundary.md) only if the sentence makes a technical judgement.
- For formal review, thesis-section revision, SCI manuscript polishing, or Word/docx revision, start with [qc/failure-mode-diagnosis.md](qc/failure-mode-diagnosis.md). Do not polish sentence fluency before diagnosing section job, evidence, terminology, and boundary failures.
- For citation-heavy writing, combine [../workflows/citation-workflow.md](../workflows/citation-workflow.md) with [qc/claim-evidence-boundary.md](qc/claim-evidence-boundary.md). A citation must support a specific sentence, not a broad topic.
- For final delivery, use [qc/final-polish-checklist.md](qc/final-polish-checklist.md) to report unresolved risks rather than hiding missing evidence behind smoother prose.

## Core Principle

The QC pass should move from structure to language:

```text
task mode -> section job -> reader question -> claim/evidence/boundary -> terminology -> sentence polish
```

If a paragraph lacks data, figure/table anchors, formula basis, model assumptions, parameter range, code basis, or citation support, downgrade the claim or list it under `需补充或确认`. Do not compensate by using stronger wording.

## Quick Failure Signals

- A paragraph only lists actions such as "建立模型、分析参数、得到规律" without explaining the research object, indicator, evidence, mechanism, and boundary.
- A result sentence says "吻合较好", "显著提高", "影响较大", "具有应用价值", or "可为工程设计提供参考" without baseline, metric, or applicability range.
- A method paragraph says what was done but not why the design, metric, specimen, model, feature, or validation route answers the stated problem.
- A literature paragraph lists papers in sequence rather than organizing them as a technical conversation.
- A conclusion introduces a new claim, expands beyond the data range, or turns a preliminary design aid into a code-level design substitute.

## Maintenance Note

Keep this compatibility entry short. New QC examples, checklists, or failure-mode rules should be added to the focused files under `references/style/qc/`, then registered in [qc/index.md](qc/index.md) and checked by `scripts/validate_style_qc.py`.
