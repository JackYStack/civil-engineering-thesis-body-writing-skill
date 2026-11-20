# Writing Rationale Matrix for Civil Thesis and Paper Tasks

Use this reference before substantial writing or rewriting. The matrix explains why each writing unit exists before final prose is produced. It is a design tool, not a post-hoc change log.

## When to Use

Use a writing rationale matrix for:

- formal revision of a full `.docx`/Word manuscript;
- abstract, introduction, conclusion, or research-status restructuring;
- independent journal manuscript revision;
- Chinese-to-English submission draft logic rebuilding;
- a section longer than about 800-1000 Chinese characters with multiple claims;
- tasks where the user explicitly says `正式使用 skill`, `整节修改`, `整篇修改`, or `按论文逻辑重构`.

Do not require it for a short paragraph polish, terminology correction, or one-sentence rewrite.

## Confirmation Gate Before Full Drafting

For full sections, full manuscripts, target-journal polishing, or formal `.docx` revision, do not jump directly from "the text is weak" to a rewritten manuscript. First produce a compact confirmation gate unless the user has already provided an explicit plan. This planning step does not authorize converting a thesis into an article.

The gate should contain:

1. `one-sentence argument`: what the section or manuscript must prove;
2. `reader-question sequence`: the main question each major unit answers;
3. `paragraph or unit map`: the planned unit order and function;
4. `terminology ledger`: terms or symbols that must stay fixed;
5. `evidence boundary`: figures, tables, formulas, datasets, citations, standards, or code artifacts that can support claims;
6. `overclaim guard`: claims that must be weakened or avoided.

Proceed directly only when the task is narrow, the replacement target is explicit, or the user asks for an immediate local rewrite. If the gate exposes a material ambiguity, ask only the blocking question and keep the rest of the plan visible.

## Matrix Levels

Choose the lightest level that still controls logic:

- `light`: 3-5 rows for an abstract, short subsection, or application paragraph.
- `standard`: 8-15 rows for one full section or paper-style body segment.
- `full`: 20+ rows for a full manuscript or formal Word revision.

## Required Table

| Unit | Current Function or Problem | Motivation Link | Evidence Anchor | Literature or Exemplar Pattern | Planned Move | Final Check |
|---|---|---|---|---|---|---|

Column requirements:

- `Unit`: title, paragraph, paragraph group, figure/table claim, method step, result claim, conclusion item, or caption.
- `Current Function or Problem`: what this unit currently does, or what it must do if drafting from materials.
- `Motivation Link`: how the unit supports the section/manuscript motivation thread.
- `Evidence Anchor`: figure, table, formula, dataset, metric, experiment, FE result, ML metric, citation marker, or user note.
- `Literature or Exemplar Pattern`: writing pattern learned from local thesis/paper samples or target-journal examples. This is structural learning, not copying wording.
- `Planned Move`: keep, move, merge, split, rewrite, delete, add evidence, narrow claim, add boundary, or convert to transition.
- `Final Check`: how to know the revised text is defensible.

## Whole-Work Row

For full manuscripts or major section rewrites, the first row should justify the whole structure:

- why this section/paper is organized in this order;
- how the order follows the motivation thread;
- which user evidence anchors the main claim;
- which local thesis/paper or target-journal pattern is being transferred;
- what overclaim must be avoided.

## Quality Bar

The matrix fails if most rows only say:

- `润色语言`;
- `提高学术性`;
- `增强逻辑`;
- `补充细节`;
- `使表达更清楚`.

A usable row must name the writing action and the evidence reason. For example:

| Unit | Current Function or Problem | Motivation Link | Evidence Anchor | Literature or Exemplar Pattern | Planned Move | Final Check |
|---|---|---|---|---|---|---|
| 4.2 model application opening | Current paragraph explains SHAP before the user-facing application route, so the design workflow is not visible. | The section should prove that predicted DCA can be converted into preliminary design indicators. | GUI functions, predicted `DCA_s`/`DCA_c`, deflection and capacity post-processing formulas. | Local paper style introduces tool/workflow first, then explains interpretation and optimization. | Move GUI/workflow first; explain DCA-to-response calculation; place SHAP as parameter adjustment support. | Reader can identify input, model output, engineering response, optimization action, and verification boundary. |

## Output Use

When a matrix is used, the response can include:

1. `主线校准`
2. `写作理由矩阵`
3. `正文稿/修改稿`
4. `证据与引用对应`
5. `风险与需确认`

For long documents, save the matrix as a Markdown artifact before editing the Word file so later revisions can be traced.
