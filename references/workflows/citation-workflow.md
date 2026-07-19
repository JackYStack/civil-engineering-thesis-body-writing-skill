# Local-First Citation Workflow

This file is now a compatibility entry for the former merged citation workflow. Keep this path valid for old prompts, but load the focused files below for actual citation work.

## Load Order

| File | Load When |
|---|---|
| [citation/index.md](citation/index.md) | You need the citation workflow map and do not yet know which focused guide to open. |
| [citation/local-first-search.md](citation/local-first-search.md) | You need to find or verify candidate literature from user references, local files, Zotero, InstSci, or web fallback. |
| [citation/support-grading.md](citation/support-grading.md) | You need to decide whether a source strongly supports a sentence, partially supports it, or should not be cited. |
| [citation/output-format.md](citation/output-format.md) | You need to insert temporary markers, build a citation support bank, or return a candidate table. |
| [citation/pcsp-directions.md](citation/pcsp-directions.md) | The topic is PCSP/ICSP, connector behaviour, DCA, partially composite sandwich panels, FE modelling, or PCSP data-driven prediction. |

## Core Policy

- Search local and user-provided evidence first. Use web search only when local evidence is insufficient, stale, or needs metadata verification.
- Treat citation work as claim-level support. Every candidate must state the exact sentence or focused claim it can support.
- Do not use external literature to replace the user's own test, finite-element, machine-learning, GUI, formula, or chapter-result evidence.
- Retrieval/access status is not citation support. A Zotero record, InstSci download result, title match, abstract, or publisher metadata must still be inspected for the specific claim.
- Use temporary markers `[R1]`, `[R2]`, ... unless the user provides a stable numbered bibliography.
- Do not renumber the final bibliography. Output a candidate table for later integration.

## Quick Workflow

1. Segment the draft into citable claims.
2. Skip claims that should be supported by the user's own figures, tables, formulas, datasets, or section evidence.
3. Search user-provided and local sources first.
4. Use web, DOI, publisher, standards, or InstSci fallback only when needed.
5. Grade each candidate with [citation/support-grading.md](citation/support-grading.md).
6. Insert markers and return the table using [citation/output-format.md](citation/output-format.md).
7. Flag unsupported claims, metadata-only candidates, or sources needing full-text confirmation.

## Maintenance Note

Keep this compatibility entry short. New citation rules should be added to the focused files under `references/workflows/citation/`, registered in [citation/index.md](citation/index.md), and checked by `scripts/validate_citation_workflow.py`.
