# QC Index

This directory contains focused quality-control rules for civil-engineering thesis and SCI manuscript writing. Use it after the router has selected the task mode, section type, evidence source, and operation.

## Files

| File | Primary Job |
|---|---|
| [failure-mode-diagnosis.md](failure-mode-diagnosis.md) | Decide what kind of problem the text has before rewriting it. |
| [claim-evidence-boundary.md](claim-evidence-boundary.md) | Check whether each technical judgement has a concrete object, metric, evidence, mechanism, and boundary. |
| [final-polish-checklist.md](final-polish-checklist.md) | Run the final pass before returning revised text, audit findings, or file-edit summaries. |

## Minimal QC Path

For small paragraph polishing:

1. Identify the section job.
2. Check whether key claims have evidence and boundary.
3. Remove or downgrade vague judgement words.
4. Return revised text plus only unresolved material risks.

For formal thesis or paper review:

1. Diagnose failure mode with [failure-mode-diagnosis.md](failure-mode-diagnosis.md).
2. Repair claim support with [claim-evidence-boundary.md](claim-evidence-boundary.md).
3. Use [final-polish-checklist.md](final-polish-checklist.md) before delivery.

## Shared Rules

- Do not invent missing data, standards, formula sources, experimental results, FE results, machine-learning metrics, or literature conclusions.
- Prefer user evidence first: figures, tables, equations, datasets, scripts, model outputs, Word comments, existing references, and Zotero full text.
- Treat external retrieval status as access evidence, not claim support. A downloaded or found paper still needs sentence-level relevance checking.
- Technical prose can be smooth only after it is specific. If a sentence cannot answer "相对谁、哪个指标、什么证据、何种机理、适用到哪里", revise it or flag it.
- Keep thesis writing complete and traceable; keep SCI writing compressed and contribution-centered. Do not mix the two styles without an explicit thesis-to-paper task.

## When Not To Load All QC Files

Do not open every file in this directory for a tiny wording change, a simple translation of a sentence, or a direct factual answer. Use the smallest relevant guide:

- vague sentence only: [../anti-vague-language.md](../anti-vague-language.md);
- unsupported technical claim: [claim-evidence-boundary.md](claim-evidence-boundary.md);
- user says the revision direction is wrong: [failure-mode-diagnosis.md](failure-mode-diagnosis.md);
- final manuscript/Word/file-producing work: [final-polish-checklist.md](final-polish-checklist.md).
