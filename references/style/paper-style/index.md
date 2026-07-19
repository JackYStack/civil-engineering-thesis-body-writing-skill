# Local Paper Style Index

Use this index for small-paper, SCI, target-journal, or thesis-to-paper work. The rules are distilled from local civil-engineering paper writing patterns and SCI writing materials, but they intentionally keep only generalized writing logic. Do not copy sample-paper facts, paper titles, author names, DOI strings, local paths, or specific conclusions into output.

## File Map

| File | Primary Use | Main Risk Controlled |
|---|---|---|
| [abstract-intro.md](abstract-intro.md) | Abstract, introduction, contribution framing, and gap compression. | Turning the paper into a broad field review. |
| [results-discussion.md](results-discussion.md) | Methods rationale, result paragraphs, discussion, and figure/table interpretation. | Reporting tables without explaining the engineering meaning. |
| [conclusion-title.md](conclusion-title.md) | Conclusion, title, highlights, and thesis-to-paper adaptation. | Repeating the abstract or overstating design applicability. |
| [sci-phrase-guardrails.md](sci-phrase-guardrails.md) | Reviewer-facing language, overclaim checks, phrase discipline, and final QC. | Fluent but vague or unsupported journal prose. |

## Mode Routing

- `paper-sci`: load the file for the section being drafted plus `sci-phrase-guardrails.md` before final output.
- `target-journal-polish`: load the target-journal workflow first, then use these guides to rewrite the manuscript against the exemplar/style findings.
- `translation-logic`: use these guides before English translation so that the Chinese claim chain is already paper-ready.
- `docx-revision`: let the DOCX workflow control file safety, then use the relevant paper-style guide only for replacement text.

## Paper-Style Baseline

Local paper style differs from thesis style in density and scope:

- one paper normally carries one dominant question, not an entire chapter system;
- background is limited to what creates the technical problem;
- methods are justified by why they can answer that problem;
- result paragraphs start from the key observation, then use figures, tables, metrics, and mechanisms to support it;
- conclusions state usable findings and boundaries rather than repeating every result.

When evidence is incomplete, do not mask it with polished wording. Mark the missing data, figure, formula, citation, or boundary in `需补充或确认`.

## Minimum Deliverable

For paper-style rewriting, output should normally include:

1. `修改稿` or `英文稿`;
2. `修改依据`, explaining which evidence or manuscript logic each change follows;
3. `需补充或确认`, listing missing data, uncertain formulas, unsupported claims, or target-journal constraints.

For short paragraph polishing, the second and third parts may be compressed into one short note.
