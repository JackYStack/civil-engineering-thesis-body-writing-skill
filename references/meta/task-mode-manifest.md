# Task Mode Manifest

Use this manifest before formal, multi-branch, or manuscript-level tasks. Choose one primary mode, then add secondary modes only when they are necessary.

The purpose is to prevent the skill from mixing thesis prose, SCI rewriting, citation search, Word editing, and library import in one undifferentiated workflow.

## Mode Selection Rule

1. Identify the user's requested deliverable.
2. Select one `primary mode`.
3. Load only the references required by that mode, plus any explicitly requested secondary workflow.
4. Follow the matching output contract in [output-contracts.md](output-contracts.md).
5. If the request spans several modes, finish the blocking upstream mode first. For example, do citation support before rewriting a citation-heavy introduction, and do evidence-bank extraction before editing a `.docx`.

## Modes

| Mode ID | Use When | Required Inputs | Required Guides | Blocking Checks |
|---|---|---|---|---|
| `thesis-body` | Writing or revising Chinese master's thesis body sections. | section type, research object, method, variables, evidence, boundary | `chapter-templates`, `local-thesis-style`, `style-and-qc`, `anti-vague-language` | missing figure/table/data anchors; unsupported design conclusion |
| `paper-sci` | Drafting or revising independent journal/SCI manuscripts, not converting a thesis. | author-defined journal question, claim, evidence, variables, target language, boundary | `sci-writing-principles`, `nature-writing-adapted-sci-workflow`, `reader-question-sequence`, `terminology-ledger` | thesis conversion request; unbounded novelty claim |
| `target-journal-polish` | Matching a manuscript to a named journal or journal family. | target journal, article type, manuscript, exemplar access | `target-journal-polish-workflow`, `external-source-and-tool-use`, `output-contracts` | no target journal; no permission/access path for exemplars |
| `citation-support` | Adding, reducing, verifying, or replacing citations. | claim list or draft paragraph, local references, Zotero/library status | `citation-workflow`, `external-source-and-tool-use`, `pdf-extraction-and-fulltext-qc` | citation supports only title similarity; full text not checked for claim-level support |
| `docx-revision` | Creating, converting, formatting, or revising a Word `.docx` manuscript. | selected `create/convert/revise` branch, input/source path, formatting authority, scope, rich-object requirements | `docx-creation-and-formatting`, `docx-ooxml-editing`, `writing-rationale-matrix`, `terminology-ledger` | generic defaults presented as institutional compliance; original overwritten; formulas/fields/tables changed without object-level inspection |
| `translation-logic` | Chinese-English thesis/paper translation or bilingual logic checking. | source text, target style, terminology, figures/tables/formulas, boundary | `terminology-ledger`, `sci-writing-principles`, `reader-question-sequence` | term drift; English wording strengthens the Chinese claim |
| `instsci-zotero` | Retrieving papers through InstSci and importing/organizing them in Zotero. | DOI/title list, retrieval output, Zotero write intent | `instsci-paper-retrieval-workflow`, `instsci-to-zotero-import-workflow`, `external-source-and-tool-use` | Zotero write without preview/confirmation; retrieval status treated as citation evidence |
| `thesis-audit` | Running format, final-audit, or deterministic thesis readiness checks for LaTeX/DOCX/PDF artifacts. | artifact source of truth, template/specification, calibrated ruleset, check mode, required evidence, fix policy | `thesis-format-audit`, `thesis-skills-audit-workflow`, `docx-ooxml-editing`, `style-and-qc` | generic rules presented as school compliance; skipped checks reported as PASS; risky fix applied without preview or confirmation |
| `figure-support` | Planning, revising, auditing, or generating a thesis/journal figure tied to manuscript claims. | core conclusion, section role, data/source files, variables/units, panel needs, target output, journal/template | `nature-figure-cooperation`, `scientific-figure-color`, then `nature-figure` for execution | plotting starts before the evidence brief; mock data substitutes manuscript evidence; backend gate is bypassed; artifacts or QA are claimed without files |

## Mode Mixing Rules

- Thesis-to-journal conversion is outside scope. Do not route it through `paper-sci`, target-journal polishing, translation or DOCX operations. Explain the boundary without generating an extraction plan or converted abstract; a supported independent task must be separately specified.

- `docx-revision` may call `thesis-body`, `paper-sci`, or `translation-logic` for manuscript text, but it controls the `create/convert/revise` branch, formatting contract, file safety, and Word-object validation.
- `citation-support` may precede any writing mode, but it should not replace the user's own result evidence.
- `target-journal-polish` may call `paper-sci`, but journal requirements and exemplars control the rewrite blueprint.
- `instsci-zotero` ends at library organization; it does not prove citation support until `citation-support` checks full text.
- `thesis-audit` reports rule-calibrated readiness and final-audit evidence; it does not rewrite prose or rich document objects unless the user separately confirms that scope.
- `figure-support` may call `thesis-body`, `paper-sci`, `target-journal-polish`, or `docx-revision` for manuscript reintegration. Actual plotting, rendering, export, and visual QA remain owned by `nature-figure`.

## Minimal Visible Output

For formal tasks, state the selected mode in one short line:

`任务模式：paper-sci；辅助模式：citation-support；原因：...`

Do not show this line for tiny local edits unless it clarifies the boundary.
