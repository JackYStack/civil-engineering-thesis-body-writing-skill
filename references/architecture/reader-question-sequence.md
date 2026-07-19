# Reader Question Sequence

Use this guide for full sections, full manuscripts, thesis-to-paper conversion, SCI drafts, formal `.docx` revisions, and any section that feels flat even when the facts are correct.

The goal is to make the manuscript answer the reader's questions in the order they naturally arise. This is adapted from nature-style article architecture, but calibrated for civil-engineering thesis and paper writing.

## Core Sequence

| Reader Question | Manuscript Job | Typical Section |
|---|---|---|
| Why should I care about this object or problem? | Establish engineering relevance and the exact design/research pain point. | Introduction, chapter opening, abstract opening |
| What is not yet resolved? | Convert broad background into a focused contradiction, limitation, or missing design capability. | Literature review, final introduction paragraph |
| What will this study do about it? | State the method route, object, variables, and evidence plan. | Methods opening, research contents, abstract method sentence |
| Why is this route credible? | Show data source, experiment/FE/ML design, validation, metrics, and reproducibility boundary. | Methods, validation, model training |
| What was found? | Translate figures, tables, equations, and metrics into a bounded claim. | Results and Discussion |
| What does the finding mean mechanically or methodologically? | Explain mechanism, comparison, sensitivity, limitation, or design implication. | Discussion, model application |
| Where can this be used, and where not? | State application scope, parameter range, safety/design boundary, and future work. | Conclusion, model application, limitations |

## Section Handoff Checks

For a substantial writing task, write one short note before drafting:

1. `Question raised`: what the current section makes the reader want to know.
2. `Answer provided`: the claim, method, or result this section gives.
3. `Evidence used`: figure, table, formula, dataset, metric, citation, standard, or code artifact.
4. `Next question`: what the next section must answer.

If two adjacent sections answer the same question, merge, shorten, or change one section's job. If a section introduces a new question that the paper never answers, narrow or delete that claim.

## Civil-Engineering Calibration

- For thesis chapters, allow slower setup, but every subsection still needs a reader question.
- For SCI or journal paper drafts, compress background and move faster toward the unresolved problem and evidence route.
- For model application or GUI sections, the reader question is usually not "is the model accurate?" but "how does the prediction become a usable design indicator?"
- For PCSP/DCA topics, distinguish the question "what is the DCA?" from "how does DCA affect deflection, capacity, connector demand, or design screening?"

## Output Add-On

When this guide is used, include a compact `reader-question calibration` block for formal work:

| Unit | Reader Question | Answer/Evidence | Next Handoff | Risk |
|---|---|---|---|---|

Do not include the block for a one-paragraph polish unless the user asks for a visible audit.
