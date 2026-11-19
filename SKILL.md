---
name: civil-thesis-body-writing
description: Use when drafting, revising in response to peer review, citing, translating, auditing, target-journal polishing, coordinating publication figures, or safely editing Chinese civil-engineering master's thesis body text, local paper/SCI manuscripts, Word/docx drafts, Zotero/InstSci-supported literature evidence, or thesis-to-paper materials, especially for 大论文, 小论文, SCI投稿稿, 章节正文, 试验研究, 有限元分析, 机器学习模型, 模型应用, 科研图表, and OOXML-safe revision.
---

# Civil Thesis Body Writing

Shared writing rules for Codex, Claude Code, and WorkBuddy. Load only needed routes. On non-Codex hosts, read `references/workflows/agent-compatibility.md`; skip unavailable tool operations rather than simulate them.

## Mandatory Router

1. Read `manifest.yaml` for every formal, multi-axis, manuscript-level, file-producing, citation-heavy, or maintenance task.
2. Load all `always_load` files from the manifest:
   - `static/core/stance.md`
   - `static/core/workflow.md`
   - `static/core/output-format.md`
   - `static/core/reader-question-sequence.md`
   - `static/core/terminology-ledger.md`
3. Detect the applicable axes:
   - `mode`: thesis body, paper/SCI, target-journal polish, citation support, docx revision, translation logic, InstSci-Zotero, thesis audit, or figure support.
   - `section`: abstract, introduction, literature review, method, experiment, finite element, machine learning, model application, results/discussion, chapter summary, or conclusion.
   - `source`: user materials, local style corpus, Zotero full text, PDF/OCR, InstSci, or external search.
   - `operation`: draft, revise, audit, translate-precheck, docx-edit, cite, or import-library.
4. Open only the matching static fragments under `static/fragments/`.
5. Use `references/index.md` to choose any deeper on-demand guide.
6. For formal output, select one primary mode from `references/meta/task-mode-manifest.md` and follow `references/meta/output-contracts.md`.

For a short paragraph polish or one-sentence rewrite, the lightweight path is allowed: identify the claim, preserve terms/data/citations, remove vague wording, and return the revised text plus material risks.

## Core Rules

- Write in Chinese unless the user asks for English or translation.
- Do not invent experiments, data, parameters, formulas, figures, tables, standards, references, Zotero records, InstSci access results, or conclusions.
- Preserve symbols, units, figure/table numbers, formulas, citation markers, GUI/code labels, and Word/docx structure.
- Thesis writing is evidence-first: each key claim needs object, condition, indicator, evidence, mechanism, and boundary.
- Prefer local thesis style for 大论文正文 and local paper/SCI style for 小论文 or SCI稿件. Do not copy sample wording or paper-specific facts.
- Use conflict/puzzle/story logic only as hidden planning. Formal prose should remain measured and civil-engineering oriented.
- Keep chapter-role comparison and reviewer-facing structural explanation out of thesis body prose. State the engineering object, reused model/formula, method, process, evidence, and boundary directly; keep “Section X solves...Section Y solves...” reasoning in the writing rationale, outline, or response notes.
- Keep gratuitous self-critique and generic disclaimers in working notes, not ordinary body prose. Retain material contrary findings, necessary assumptions, and conditions affecting interpretation in the relevant passage; anti-defensive writing must not suppress scientific disclosure. Bound claims by tested objects, conditions, metrics, and evidence.
- Do not use external literature to replace the user's own results. For the user's test, FE, ML, GUI, formula, or chapter-result claims, cite the user's figures, tables, formulas, data, and section evidence first.
- Use local-first citation support: user-provided references, current draft citations, Zotero/library full text, local notes, and project files before web or publisher search.
- Metadata discovery is not full-text support. For translated literature discussion, read `references/workflows/literature-translation-grounding.md`; keep source, faithful translation, and interpretation distinct.
- When using external tools or databases, record source, query, access status, and support boundary. Protect credentials and access tokens.
- For `.docx` work, first classify the branch as `create`, `convert`, or `revise`. Use `references/workflows/docx-creation-and-formatting.md` for new/Markdown-derived documents and formatting contracts; use `references/workflows/docx-ooxml-editing.md` for targeted edits to existing files. Preserve the original by default.
- For the author-confirmed HFUT thesis Word project, load `references/style/hfut-thesis-word-objects.md` before creating or auditing bilingual figure captions, bilingual table captions, three-line tables, or numbered equations; do not substitute generic Word layouts for the calibrated object structure.
- For a local edit confined to one thesis section, visually inspect only the rendered pages occupied by that section. Do not inspect full-document contact sheets or every page unless the change spans sections, affects global layout/fields/styles, or the user requests a final-submission audit.
- For PDF-derived text, OCR, Zotero indexed full text, or publisher PDFs, use `references/workflows/pdf-extraction-and-fulltext-qc.md` before treating extracted text as evidence.
- For thesis format/readiness audits, use `references/workflows/thesis-format-audit.md`; calibrate rules against the controlling template, keep structured reports authoritative, and treat skipped checks as unavailable rather than passed.
- For thesis or journal figure colour selection/audits, use `references/style/scientific-figure-color.md`; map colour to variable semantics, preserve a manuscript-level colour ledger, and verify colour-vision, grayscale, final-size, and target-journal constraints.
- For publication-figure planning or execution, use `references/workflows/nature-figure-cooperation.md`: this skill owns the manuscript-facing figure brief and reintegration, while `nature-figure` owns backend selection, plotting, rendering, export, and visual QA.
- For methods/results or scientific audits, load `references/workflows/research-integrity-and-reproducibility.md`; for equations or quantitative displays/derived claims, load `references/workflows/equation-figure-table-integrity.md`. Apply without waiting for the user to name the risk. For changed shared results, cross-section checks or final packages, use `references/workflows/manuscript-consistency-and-delivery.md`. A formatting pass is not scientific validation.

For reviewer-driven work read `references/workflows/reviewer-driven-revision.md`. Use the existing thesis/paper + `revise` route, or `docx-revision` for files. Preserve author voice and necessary disclosure; `nature-response` is optional for reply packages.

## Ask Before Acting

Ask one concise question only when the missing boundary changes the substance or safety of the work:

- the target section, manuscript type, or target journal is unclear;
- the claimed result lacks data, figure/table/formula support, or applicable parameter range;
- the task asks for design or normative conclusions without code/standard/safety boundary;
- Zotero/InstSci import would write to the user's library and no confirmation was given;
- `.docx` edits could affect formulas, tracked changes, comments, or compatibility.
- a formal `.docx` must comply with an institution/journal template, but the controlling template or formatting specification is unavailable.

If the section, evidence, and intended claim are clear, proceed directly.

## Routing Quick Reference

| User request | Primary route |
|---|---|
| Write or expand a thesis subsection | `mode: thesis-body`, matching `section`, `operation: draft` |
| Rewrite thesis content into a paper/SCI section | `mode: paper-sci`, matching `section`, `operation: revise` |
| Polish for a named target journal | `mode: target-journal-polish`, `source: external-search` or `local-style-corpus` |
| Add or reduce citations | `mode: citation-support`, `operation: cite` |
| Revise body text to address a reviewer comment | Existing paper/thesis mode + `revise`; load `references/workflows/reviewer-driven-revision.md` |
| Revise a Word manuscript | `mode: docx-revision`, `operation: docx-edit` |
| Check Chinese-English logic before translation | `mode: translation-logic`, `operation: translate-precheck` |
| Retrieve papers and import to Zotero | `mode: instsci-zotero`, `operation: import-library` |
| Run thesis readiness / deterministic audit | `mode: thesis-audit`, `operation: audit` |
| Plan, revise, or generate a publication figure | `mode: figure-support`, then hand actual plotting/export to `nature-figure` |

## Writing Procedure

1. Reverse-outline the unit and, for substantial work, establish reader questions and a `phenomenon -> mechanism -> condition` argument.
2. Reuse the evidence bank and terminology ledger; link claims to user data, model outputs, objects and actual source passages. Distinguish planned, reported, checked and disputed evidence.
3. Load the relevant integrity guides above; check scientific meaning and numeric/object mappings before prose. Grade citation support for external claims.
4. Draft/revise in the selected civil-engineering style. For major argument use `references/architecture/evidence-led-narrative-and-defensive-writing.md`; retain material contrary evidence and necessary conditions.
5. Run anti-vague language QC, the body-prose meta-discourse gate and disclaimer gate: remove unsupported praise, planning commentary and generic self-defense, not scientific disclosure.
6. Check affected cross-references, abstract/conclusion and delivery artifacts. Report actual validation and material unresolved items separately from ready-to-use prose; do not move necessary technical conditions out of the body.

For language cleanup/polish load `references/style/academic-prose-cleanup.md`. Preserve terms, data/object and citation/claim mappings, author voice, genuine uncertainty and editing scope. Select intensity within existing operations; do not optimize detector scores.

## Source-Specific Rules

- `user-materials`: treat user data, figures, tables, formulas, code, and Word text as primary evidence.
- `local-style-corpus`: use only structural and stylistic patterns, not sample-specific facts.
- `zotero-fulltext`: extract paper spine, variables, indicators, claims, and boundaries before citing.
- `pdf-ocr`: manually check formulas, tables, figure captions, and units before using them.
- `instsci`: use for retrieval/access evidence; do not treat download success as citation support.
- `external-search`: use only when local evidence is weak or current facts are needed; cite official or primary sources when possible.
- `nature-figure`: use only after the figure brief is ready; its Python/R backend gate and execution contract govern all drawing, export, and visual QA.

## Output

Follow the selected mode contract in `references/meta/output-contracts.md`. For small tasks, keep the response compact:

1. `正文稿` or `修改稿`
2. `主要修改`
3. `证据与边界`
4. `需补充或确认`

For file edits, report the new file path, validation run, and unresolved risks. For library import, preview writes first and confirm before changing Zotero.

## Maintenance

- Use `references/meta/pressure-test-scenarios.md` when updating behavior.
- Run `python -X utf8 scripts/validate_all.py <skill-root>` after changes.
- Keep this router concise. Move detailed rules to `static/`, `references/`, or deterministic `scripts/`.
- Record architecture changes in `references/meta/update-log.md`.
- Record materially consulted external skills, source links, reviewed revisions, retained ideas, and migration boundaries in `references/meta/external-skill-sources.md`.
- Use `references/meta/systematic-integration-map.md` to review lifecycle impact, source dependencies, exclusions and observable checks before adding another isolated rule.
