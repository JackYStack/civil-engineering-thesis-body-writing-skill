# Local Thesis Body Style Corpus

This is now a compatibility entry for the former merged Word/PDF thesis-body style corpus. It stays at the old path so existing references do not break, but the heavy content has been split into focused files under `local-thesis-corpus/`.

Use this file only to choose the right focused guide. Do not load every subfile unless the task truly needs a full chapter-level style calibration.

## Split Corpus Index

| File | Load When |
|---|---|
| [local-thesis-corpus/index.md](local-thesis-corpus/index.md) | You need the map of the split local thesis corpus. |
| [local-thesis-corpus/chapter-flow.md](local-thesis-corpus/chapter-flow.md) | You are planning or revising chapter/section order, chapter transitions, or chapter summaries. |
| [local-thesis-corpus/paragraph-phrases.md](local-thesis-corpus/paragraph-phrases.md) | You need local thesis paragraph structures, transition phrases, result phrasing, or anti-vague sentence patterns. |
| [local-thesis-corpus/experiment-style.md](local-thesis-corpus/experiment-style.md) | You are writing specimen design, material properties, loading protocol, damage process, structural performance, or experimental result analysis. |
| [local-thesis-corpus/fe-style.md](local-thesis-corpus/fe-style.md) | You are writing finite-element assumptions, model construction, validation, parameter analysis, or FE result interpretation. |
| [local-thesis-corpus/ml-style.md](local-thesis-corpus/ml-style.md) | You are writing data preprocessing, feature/output definitions, model comparison, prediction metrics, SHAP/explainability, or ML limitations. |
| [local-thesis-corpus/pcsp-style.md](local-thesis-corpus/pcsp-style.md) | You are writing PCSP, connector, composite action, DCA, GUI-assisted design, or PCSP-specific FE/ML content. |

## Compatibility Rules

- For normal thesis body drafting, first use [local-thesis-style.md](local-thesis-style.md). Load this corpus only when the user asks for close local thesis style calibration or when chapter-level PCSP/FE/ML writing needs more detail.
- For mixed PCSP + FE + ML sections, load `pcsp-style.md` first, then add `fe-style.md` or `ml-style.md` only if the paragraph actually uses those methods.
- For result paragraphs, prefer `paragraph-phrases.md` plus the method-specific file.
- For chapter structure, prefer `chapter-flow.md`; do not load method-specific files just to write transitions.
- The split files retain reusable style rules only. They intentionally exclude concrete thesis titles, author names, file paths, sample IDs, and paper-specific conclusions.
