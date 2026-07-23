# DOCX and OOXML Editing Safety Strategy

Use this reference when the task requires modifying an existing `.docx` thesis, paper, bilingual manuscript, or Word revision file. The goal is to preserve Word compatibility while making targeted academic text edits.

For the author-confirmed HFUT thesis Word project, load [hfut-thesis-word-objects.md](../style/hfut-thesis-word-objects.md) before changing figures, tables, bilingual captions, or numbered equations. Its verified container structure overrides the generic fallback layouts in this guide.

## Default Policy

- Always create a new revision file. Do not overwrite the original `.docx`.
- Prefer low-risk OOXML text-node edits for academic prose revision.
- Do not rebuild the whole document unless the user explicitly asks for a clean regenerated manuscript.
- Preserve images, tables, styles, numbering, references, comments, headers, footers, and relationship files unless the task specifically requires changing them.
- After editing, validate by extracting `word/document.xml`, parsing XML, and sampling key paragraphs/tables. When compatibility matters, open and save the file once through Microsoft Word.
- For formal manuscript-level revision, create or summarize a traceable logic path before editing: original logic map, evidence bank, writing rationale matrix, rewrite matrix, and logic-transfer audit. For a small targeted paragraph replacement, a concise summary in the final response is enough.

## Targeted Revision Loop

Use a targeted loop before touching OOXML:

1. Locate the exact section, paragraph, caption, table cell, or term set that must change.
2. Classify the change as `local wording`, `logic rewrite`, `term unification`, `citation/evidence fix`, `formula/symbol fix`, or `structure move`.
3. For `local wording` and `term unification`, edit only the affected text nodes and preserve paragraph/table structure.
4. For `logic rewrite`, create a short rewrite matrix before replacement so the original evidence is not lost.
5. For `structure move`, captions, fields, equations, references, or numbered objects, inspect OOXML first and prefer a preview or Word-assisted edit.
6. After editing, sample the old and new text, run terminology counts when relevant, and verify that the targeted change did not spill into unrelated sections.

Do not turn a local supervisor comment into a full-manuscript rewrite unless the user explicitly asks for that scope. If a local fix reveals a manuscript-level problem, report it as a follow-up risk.

## Single-Section Visual Review Scope

Apply this scope when exactly one section or subsection is edited, even in a long formal thesis. Define the section from its heading to the next heading at the same or higher level. Render the revised DOCX as required by the available tool, then visually inspect every page intersecting the changed section pages and no unrelated pages. Do not create or inspect full-document contact sheets for this case.

Validate unaffected content structurally through DOCX package/XML parsing, targeted text extraction, terminology or object counts, source-file hashes, and preservation checks. Do not extend visual inspection from the first changed page to the document end solely because line wrapping or pagination may shift.

Use full-document visual review only when the edit spans multiple sections, changes global styles/page geometry/headers/footers/numbering or other document-wide fields, or the user explicitly requests a final-submission audit. Report the actual scoped page range; never describe a single-section check as a full-document visual audit.

## Formal Revision Traceability

Use this workflow when revising an existing Word thesis, bilingual manuscript, paper draft, or supervisor-marked document beyond a short local edit.

### 1. Original Logic Map

Map the existing manuscript units before rewriting:

| Original Unit | Current Text Role | Evidence Used | Motivation Link | Problem | Keep / Move / Rewrite / Delete |
|---|---|---|---|---|---|

This prevents the revision from becoming surface-level polishing or losing the author's original evidence.

### 2. Rewrite Matrix

Record how original units become revised units:

| Original Unit | Revised Unit | Change Type | Evidence/Citation Anchor | Reason for Change | Risk |
|---|---|---|---|---|---|

Change types include `keep`, `move`, `merge`, `split`, `rewrite`, `delete`, `add evidence`, `narrow claim`, and `add boundary`.

### 3. Logic Transfer Audit

After editing, check:

- key figures, tables, formulas, variables, metrics, and citations were not lost;
- no new conclusion was added without evidence;
- original claims were either preserved, narrowed, or explicitly removed for a reason;
- section openings and conclusions still serve the same motivation thread;
- Chinese-English bilingual or translated drafts preserve technical meaning, not only sentence order.

For large edits, save these as Markdown artifacts near the revised `.docx`, such as `original_logic_map.md`, `rewrite_matrix.md`, and `logic_transfer_audit.md`.

## Low-Risk OOXML Edits

These are appropriate for direct OOXML modification:

- replacing ordinary paragraph text in `w:t` text nodes;
- replacing table-cell text when the table structure is unchanged;
- unifying terminology and symbols, such as `DCAs -> DCA_s` or `fc -> f_c`;
- replacing title, abstract, keywords, section text, model-application paragraphs, conclusions, and captions;
- removing stray text fragments introduced by previous edits;
- correcting plain text in figure/table captions.

Preferred approach:

1. Unzip/read `.docx` as a ZIP archive.
2. Modify only `word/document.xml` unless another part is explicitly required.
3. Keep existing paragraph/table elements and replace text nodes inside them.
4. Repackage the document with all original ZIP entries preserved.
5. Re-open the output file for XML parsing and text extraction checks.

## Medium- and High-Risk OOXML Edits

Treat these as higher risk:

- changing Word equations represented as OMML (`m:oMath`, `m:oMathPara`);
- changing field codes, cross-references, captions with automatic numbering, or bibliography fields;
- changing tracked changes, comments, footnotes, endnotes, headers, or footers;
- changing multi-level heading numbering or style definitions;
- inserting or deleting rows/columns in complex tables;
- replacing paragraphs that contain drawings, equations, references, bookmarks, hyperlinks, or field codes.

For these tasks, inspect the OOXML structure first and use the least disruptive edit. If the object is complex, prefer Word COM automation or manual user review after generating a candidate revision.

## Formula Policy

Do not treat LaTeX strings and Word equations as the same thing.

- If the goal is readable formula text only, a plain text formula such as `DCA_s=(K_T-K_NC)/(K_FC-K_NC)` is acceptable but should be flagged as linearized.
- If the goal is a real Word equation, write or preserve OMML rather than inserting raw LaTeX into `w:t`.
- If replacing an existing equation, first determine whether the original is OMML, a field, an embedded object, or split plain text.
- If an equation is temporarily linearized during a broad revision, report it in the final response and recommend restoring it as Word equation formatting before submission.

## Compatibility Validation

Minimum validation after OOXML edits:

- confirm the new `.docx` exists and the original remains unchanged;
- parse `word/document.xml` successfully;
- extract key paragraphs/tables and verify intended replacements;
- count old/new terminology where symbol consistency matters;
- check that no obvious stray text remains in edited paragraphs.

Recommended Word-level validation on Windows:

```python
import win32com.client as win32

word = win32.gencache.EnsureDispatch("Word.Application")
word.Visible = False
doc = word.Documents.Open(r"<workspace>\revision.docx")
doc.SaveAs2(r"<workspace>\revision_word_resaved.docx", FileFormat=16)
doc.Close()
word.Quit()
```

If Word opens and saves without repair prompts or exceptions, compatibility risk is much lower. If the environment cannot observe prompts, still report that Word-level validation may need manual confirmation.

## Reporting Requirements

When returning a modified `.docx`, report:

- output path;
- whether the original file was preserved;
- which sections were replaced;
- whether a motivation thread, evidence bank, writing rationale matrix, rewrite matrix, or logic-transfer audit was created or summarized;
- whether formulas were kept as Word equations, converted to plain text, or left unchanged;
- validation performed, including XML parse, terminology counts, or Word COM save-as check;
- remaining risks requiring user review.

## Practical Rule

Use OOXML directly for normal text and table text. Use OMML or Word itself for equations and other rich Word objects. If in doubt, preserve the object and modify the surrounding prose.
