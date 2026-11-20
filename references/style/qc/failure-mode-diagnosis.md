# Failure-Mode Diagnosis

Use this guide before editing a weak paragraph, thesis section, SCI manuscript section, Word revision, or advisor-feedback response. The goal is to identify the real failure before changing wording.

## Priority Order

Diagnose in this order. Stop at the earliest active failure, repair it, then move downward.

1. `Task-mode failure`: the text is being handled as the wrong genre, such as thesis body, SCI article, target-journal polish, translation logic, citation support, or Word/docx revision.
2. `Section-job failure`: the paragraph does not perform its required job, such as background narrowing, literature synthesis, method rationale, validation, result translation, mechanism explanation, model application, or boundary statement.
3. `Reader-question failure`: the section does not answer the question raised by the previous unit or does not prepare the next unit.
4. `Evidence failure`: the claim has no figure, table, formula, metric, dataset, citation, standard, code output, or source anchor.
5. `Terminology failure`: terms, symbols, abbreviations, captions, variable names, or GUI/code labels drift across the text.
6. `Boundary failure`: the claim is stronger than the specimen type, model assumptions, dataset coverage, parameter range, validation evidence, or design-code basis allows.
7. `Language failure`: after the above are repaired, the wording remains vague, repetitive, too translated, or stylistically weak.

## First Fix By Failure Type

| Failure Mode | First Fix |
|---|---|
| Task-mode failure | Re-select mode and output contract before rewriting. |
| Section-job failure | Rewrite the paragraph function, not only the sentences. |
| Reader-question failure | Rebuild the handoff: what the reader now knows, what question remains, and why the next step is necessary. |
| Evidence failure | Build or request an evidence bank before strengthening the claim. |
| Terminology failure | Refresh the terminology ledger and apply canonical terms consistently. |
| Boundary failure | Narrow the claim to the tested/modelled/data-supported range. |
| Language failure | Apply anti-vague and local style polishing rules. |

## Section-Specific Signals

### Introduction

Failure signals:

- starts with a broad field slogan but never states the exact engineering contradiction;
- says "existing studies ignored..." without explaining why the omission blocks design, modelling, or evaluation;
- introduces too many disconnected gaps.

First fix:

- state the phenomenon or design contradiction;
- explain the mechanism or missing link;
- define the condition or boundary that makes the problem hard;
- end with the paper/thesis route.

### Literature Review

Failure signals:

- each sentence is one paper, one method, one result;
- citation clusters are grouped by author order rather than technical issue;
- the final gap does not follow from the reviewed methods.

First fix:

- reorganize as a conversation: mainstream explanation, neglected aspect, complementary or conflicting view, and resulting model/gap.

### Method

Failure signals:

- describes software, specimen, model, or algorithm steps but not why they answer the research question;
- lacks assumptions, boundary conditions, parameter choices, or evaluation metrics;
- uses a method name as proof of validity.

First fix:

- add method rationale: object, variable, condition, evidence route, and validation target.

### Results And Discussion

Failure signals:

- reports table values without translating them into trends, mechanism, threshold, or design implication;
- repeats every figure visually but does not identify the core finding;
- mixes result observation, mechanism, and new literature review without clear roles.

First fix:

- begin each result paragraph with object, condition, indicator, and observed trend;
- add quantitative comparison when available;
- explain mechanism and boundary after the observation is clear.

### Model Application

Failure signals:

- overstates a GUI, prediction model, SHAP explanation, or parameter screening workflow as a code-level design replacement;
- does not explain how predicted indicators become engineering outputs;
- calls an adjustment workflow "inverse design" or "optimization" without a real optimization algorithm.

First fix:

- define the tool as preliminary design, rapid evaluation, parameter screening, assisted decision, or verification support;
- state the calculation chain and finite-element/code/manual verification boundary.

## Targeted Revision Loop

When the user says the revision is not what they want, do not rewrite the whole section immediately. Instead:

1. Identify whether the mismatch is task mode, section job, evidence emphasis, tone, length, terminology, or claim strength.
2. Preserve parts that already satisfy the chosen mode.
3. Rewrite only the affected claim, paragraph, or section handoff.
4. Report the changed rationale in one or two sentences.

This loop is especially important for Word/docx editing and advisor-feedback rounds, where unrelated rewrites can damage already-approved text.
