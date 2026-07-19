# Local Thesis Corpus Index

This directory contains the split local big-thesis body style corpus. It distills the former merged Word/PDF corpus into focused style guides so agents can load only the relevant rules.

## Routing

| Task | File |
|---|---|
| Chapter sequence, chapter logic, section transitions, chapter summaries | [chapter-flow.md](chapter-flow.md) |
| Paragraph skeletons, common local thesis phrases, anti-vague replacements | [paragraph-phrases.md](paragraph-phrases.md) |
| Experiments, specimen design, loading, failure process, performance indices | [experiment-style.md](experiment-style.md) |
| Finite-element modelling, validation, parameter analysis, numerical result paragraphs | [fe-style.md](fe-style.md) |
| Machine learning, data-driven models, feature/output design, metrics, SHAP | [ml-style.md](ml-style.md) |
| PCSP, connectors, composite action, DCA, assisted design GUI | [pcsp-style.md](pcsp-style.md) |

## Shared Principles

- Keep the local master's thesis style: complete process, explicit object, clear parameter or condition, figure/table evidence, mechanism explanation, and bounded conclusion.
- Write one paragraph for one analytical job. Avoid mixing design background, method detail, result trend, and limitation in the same paragraph unless the section is intentionally summarizing.
- Use measured judgement verbs: `表明`, `说明`, `可以看出`, `在本文参数范围内`. Do not write broad claims such as `具有重要意义` without a concrete design object, indicator, and boundary.
- Prioritize the user's own figures, tables, equations, data, and model outputs. External literature supports background, mechanisms, or comparison, not the user's results.
- Use the focused file closest to the task. Loading the whole corpus defeats the split.

## Do Not Include

- Concrete paper titles, author names, Zotero keys, local source paths, sample data, or thesis-specific conclusions.
- Unsupported superlatives, policy-like claims, or design recommendations beyond the data/code boundary.
- Sentence templates that hide missing evidence.
