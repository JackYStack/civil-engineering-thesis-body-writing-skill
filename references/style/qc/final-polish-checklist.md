# Final Polish Checklist

Use this guide before returning revised text, a formal audit, a Word/docx modification report, a citation-support package, or a manuscript-level polishing result.

## Universal Final Pass

Check the output in this order:

1. The selected task mode is still correct.
2. The output follows the required contract for that mode.
3. Technical terms, symbols, abbreviations, figure/table captions, and GUI/code labels are consistent.
4. Key claims have evidence, mechanism, and boundary.
5. Vague judgement words have been replaced, quantified, or downgraded.
6. Missing evidence is reported under `需补充或确认`, not hidden.
7. The final answer does not overstate preliminary design, auxiliary tools, prediction models, or parameter screening as normative design.

## Thesis Body Checklist

- Body paragraphs state engineering content directly; chapter-role comparison, anti-duplication defense, and reviewer-facing structural explanation remain outside the body.
- Each section has a clear task: background, method, validation, result, mechanism, application, or summary.
- Each result paragraph identifies object, condition, indicator, trend, evidence, and boundary where available.
- Chapter summaries only summarize what the chapter proved; they do not introduce new data or unsupported future claims.
- The tone remains objective and thesis-appropriate, with enough explanation for advisor review.
- Local style is used as a structure guide, not as copied sample wording or copied conclusions.

## SCI Or Paper Checklist

- The manuscript has one central problem or contribution rather than several thesis-like tasks.
- Title and abstract name the object, method, key output, and boundary.
- Introduction narrows from engineering demand to a specific unresolved problem.
- Results and Discussion translate data into mechanism and boundary; they do not only report tables.
- Conclusions are short, evidenced, and restricted to proved claims.
- Target-journal polishing does not begin until journal, article type, and exemplar evidence are clear.

## Citation Checklist

- Every inserted marker has a matching citation candidate entry.
- Every candidate includes title, year, source, DOI/path/access status when available, and sentence-level support.
- Local/Zotero/full-text evidence is prioritized before web-only supplementation.
- Network-supplemented sources are marked as not fully verified unless full text has been checked.
- Standards/codes or original method papers support normative formulas, limits, or design procedures when available.
- Existing manuscript reference numbers are reused before adding temporary `[R1]` markers.

## Word/OOXML Checklist

Before editing:

- create a new output file rather than overwriting the source;
- identify whether the change is text-only, paragraph-level, figure/table caption, formula-adjacent, style, or structural;
- avoid touching equations, references, field codes, embedded objects, and numbering unless explicitly required.

After editing:

- confirm the output path;
- report preserved original path;
- report edited scope;
- validate that the `.docx` package opens structurally, or state if validation could not be run;
- list any formula, citation, numbering, or compatibility risk.
- for a local single-section edit, visually inspect only the pages occupied by that section and report that page range; do not claim a full-document visual audit.

## Formal Audit Table

For formal reviews, use a traceable table rather than generic comments:

| 问题编号 | 严重程度 | 发现内容 | 根因 | 修改动作 | 不修改的影响 | 可直接替换文本 |
|---|---|---|---|---|---|---|

Severity levels:

- `高`: affects thesis/paper logic, unsupported conclusion, wrong data/term, citation cannot support the claim, or Word/OOXML risk may damage the file.
- `中`: weak paragraph function, missing boundary, vague mechanism, poor figure/table linkage, incomplete citation support.
- `低`: wording, flow, repeated phrase, minor style inconsistency.

Each finding should say exactly what is wrong, why it happened, what action fixes it, and what risk remains.

## Return-Time Risk Notes

Report unresolved issues when present:

- missing figure/table number;
- missing variable definition;
- missing parameter range;
- missing comparison baseline;
- claim stronger than evidence;
- method not reproducible;
- design recommendation lacks code or safety boundary;
- conclusion introduces new result;
- external background, method, standard, or comparison claim lacks citation support;
- citation marker has no candidate-list entry or no sentence-level support note;
- key judgement sentence remains vague after revision.

Do not end with a vague "建议进一步完善" unless the missing evidence, affected unit, and next action are named.
