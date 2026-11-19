# Citation Workflow Index

This directory contains focused citation-support rules for civil-engineering thesis and SCI manuscript writing. Use it when the task involves adding, reducing, verifying, or explaining citations.

## Files

| File | Primary Job |
|---|---|
| [local-first-search.md](local-first-search.md) | Search user-provided, local, Zotero, InstSci, and web sources in the correct order. |
| [support-grading.md](support-grading.md) | Grade whether a source supports a sentence, and separate access status from evidentiary support. |
| [output-format.md](output-format.md) | Insert temporary markers, build support banks, and return citation candidate tables. |
| [pcsp-directions.md](pcsp-directions.md) | Apply PCSP/ICSP-specific citation priorities and avoid weak cross-topic citations. |

## Minimal Path

For a short paragraph with a few citation needs:

1. Segment the paragraph into citable claims.
2. Use [local-first-search.md](local-first-search.md) to find local or existing sources.
3. Use [support-grading.md](support-grading.md) to keep only sentence-level support.
4. Use [output-format.md](output-format.md) for markers and the candidate table.

For PCSP or sandwich-panel work, add [pcsp-directions.md](pcsp-directions.md) before choosing final citations.

When translating or explaining a source passage for the user, including an informal discussion before drafting, apply [literature-translation-grounding.md](../literature-translation-grounding.md). A local explanation need not become a full-paper reader; it still requires faithful meaning, actual source/coverage, and separate interpretation.

## Citation Need Scan

Usually needs citations:

- research background and engineering demand;
- definitions, classifications, and terminology;
- domestic and international research status;
- method, model, formula, metric, or standard basis;
- parameter selection rationale;
- comparison with previous experimental, numerical, analytical, or ML studies;
- general mechanism explanations not directly proven by the user's own data.

Usually does not need external literature:

- the user's own test observations;
- the user's finite-element validation, parameter analysis, or model outputs;
- the user's machine-learning metrics, SHAP results, GUI outputs, or formula calculation chain;
- chapter summaries and conclusions, unless they compare with external studies or state broader field knowledge.

## Non-Negotiable Rules

- A source supports a sentence, not a vibe.
- A title match is not support.
- A retrieved PDF is not support until the relevant content is inspected.
- A citation cluster should support one focused technical point.
- Fewer strong citations are better than many weak citations.
- If support is missing, mark the claim as unsupported or request evidence; do not decorate it with a weak reference.
