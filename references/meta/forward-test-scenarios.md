# Forward-Test Scenarios

Use these scenarios after router, reference, workflow, or output-contract changes. They are fresh-context checks: a tester should start with only the skill entry, the user prompt, and local files that the prompt names.

These tests complement [pressure-test-scenarios.md](pressure-test-scenarios.md). Pressure tests check failure modes. Forward tests check whether ordinary user tasks still route to the right mode, load the right focused references, and produce a useful deliverable without drifting into unrelated branches.

## Scenario: Anti-Vague Thesis Sentence Polish

Mode: `thesis-body`

Trigger: The user gives one or several Chinese civil-engineering thesis sentences such as "该方法具有重要工程意义" or "有限元结果与试验结果吻合较好" and asks for polishing.

Expected axes: section may be `results-discussion` or `chapter-summary`; source is `user-materials`; operation is `revise`.

Expected references: `style/anti-vague-language.md`, `style/local-thesis-style.md`, and focused QC guides only when the sentence contains unsupported claims.

Expected output contract: revised sentence first, then a short note on missing indicators, evidence, or boundary if the source sentence lacks them.

Must do: Replace vague praise with object-indicator-evidence-boundary wording; downgrade claims when no data are provided.

Must not: Invent numerical errors, specimen counts, model metrics, or design ranges.

Validation prompt: "用 civil-thesis-body-writing 优化：该模型具有较高预测精度和应用价值。没有额外数据时不要编造。"

## Scenario: PCSP Model-Application Section Revision

Mode: `thesis-body`

Trigger: The user asks to rewrite a PCSP model-application paragraph about GUI-based DCA prediction, deflection calculation, ultimate capacity calculation, SHAP explanation, or FE verification.

Expected axes: section is `model-application`; source is `user-materials`; operation is `revise`.

Expected references: `style/local-thesis-style.md`, `style/local-thesis-corpus/pcsp-style.md`, `architecture/evidence-bank-and-claim-register.md`, and `style/anti-vague-language.md`.

Expected output contract: replacement paragraph plus key logic notes if a design equation, GUI output, or verification boundary is unclear.

Must do: Keep GUI as preliminary design, rapid evaluation, parameter screening, or verification-support tool; explain how DCA can feed equivalent stiffness, midspan deflection, and ultimate capacity calculations only within the paper's stated formula chain.

Must not: Present the GUI as a code-compliant design replacement, claim inverse design when no inverse algorithm exists, or treat SHAP importance as causal proof.

Validation prompt: "把 PCSP 4.2 模型应用段落改成先讲 GUI 工具，再讲由组合度得到挠度和极限承载力，最后讲 SHAP 用于参数优化。"

## Scenario: Citation Reduction With Zotero Local-First Support

Mode: `citation-support`

Trigger: The user provides a citation-heavy introduction paragraph and asks to reduce citations, prefer sources found in the project or Zotero, and avoid repeating the same paper.

Expected axes: section is `introduction`; source is `zotero-fulltext` plus `user-materials`; operation is `cite`.

Expected references: `workflows/citation/index.md`, `workflows/external-source-and-tool-use.md`, and `examples/zotero-corpus-profile.md` when PCSP or structural ML literature is involved.

Expected output contract: revised paragraph with temporary citation markers, followed by a citation candidate table with support claim, source status, and support grade.

Must do: Search local/project/Zotero sources before external search; keep each retained citation tied to a specific sentence-level claim; flag missing full text or weak support.

Must not: Keep references only because their titles look related, use one paper repeatedly for unrelated claims, or replace the user's own experimental/FE/ML results with external citations.

Validation prompt: "这段 PCSP 引言引用太密，请本地/Zotero 优先核查并减少引用，不要重复引用同一篇论文。"

## Scenario: DOCX Abstract Or Conclusion Rewrite For Journal Submission

Mode: primary `docx-revision`; secondary `paper-sci`, `target-journal-polish`

Trigger: The user provides a `.docx` manuscript path and asks to revise the abstract, conclusion, title, or model-application section for an engineering journal.

Expected axes: section is `abstract` or `conclusion`; source is `user-materials`; operation is `docx-edit`.

Expected references: `workflows/docx-ooxml-editing.md`, `architecture/writing-rationale-matrix.md`, `architecture/terminology-ledger.md`, `sections/sci-writing-principles.md`, and target-journal workflow only if a journal or journal family is named.

Expected output contract: preview of planned changes, revised text, file-safety notes, and a new output file path if editing is executed.

Must do: Preserve the original file; inspect document structure before editing; keep formula fields, citations, tables, figures, captions, and numbering safe; make SCI wording evidence-bounded.

Must not: Overwrite the source `.docx`, modify formulas/fields blindly, or turn a preliminary design tool into a normative design method.

Validation prompt: "使用 civil-thesis-body-writing 修改这个 Word 的摘要和结论，保存为新文件，目标期刊类似 Engineering Structures。"

## Scenario: InstSci Retrieval To Zotero Import Preview

Mode: `instsci-zotero`

Trigger: The user asks whether papers found by InstSci can be organized and imported into Zotero, or asks to do that chain.

Expected axes: source is `instsci`; operation is `import-library`.

Expected references: `workflows/instsci-paper-retrieval-workflow.md`, `workflows/instsci-to-zotero-import-workflow.md`, and `workflows/external-source-and-tool-use.md`.

Expected output contract: retrieval/access status summary, deduplication preview, proposed Zotero collection/tags/notes, and explicit confirmation request before any Zotero write.

Must do: Separate retrieval/access evidence from citation support; deduplicate by DOI/title; mark missing DOI, missing PDF, metadata uncertainty, and access status.

Must not: Write to Zotero without preview and user confirmation, treat a downloaded PDF as sentence-level citation evidence, or expose cookies, credentials, or private access tokens.

Validation prompt: "civil-thesis-body-writing 可以把 InstSci 获取到的论文整理并用 Zotero MCP 导入 Zotero 吗？请先给导入预览。"

## Scenario: Civil-Engineering Figure Planning And Nature-Figure Handoff

Mode: `figure-support`

Trigger: The user provides FE/experimental or ML result data and asks for a journal-ready comparison figure plus a caption and results-paragraph update.

Expected axes: section is `results-discussion` or the matching experiment/FE/ML section; source is `user-materials`; operation is `draft`, `revise`, or `audit` according to the request.

Expected references: `workflows/nature-figure-cooperation.md`, `style/scientific-figure-color.md` when colour is material, then the independent `nature-figure` skill for plotting and QA.

Expected output contract: figure brief, handoff/backend status, generated artifact paths or `not generated`, QA evidence, manuscript reintegration, and unresolved blockers.

Must do: Define the core conclusion, evidence hierarchy, variable/unit ledger, panel map, colour/marker mapping, statistics, and target output before plotting; let `nature-figure` control backend selection and all rendering/export; reconnect confirmed artifacts to the caption and results paragraph.

Must not: Copy plotting implementation into the writing skill, switch backends for convenience, fabricate missing values, or claim final-size/vector/QA status without inspecting the generated files.

Validation prompt: "使用 civil-thesis-body-writing 规划试验与有限元荷载-挠度对比图，并调用 nature-figure 生成投稿图；同时给出图题和结果段落。"

## Scenario: Thesis Subsection Revision Without Meta-Discourse

Mode: `thesis-body`

Trigger: The user asks to revise one thesis subsection after a supervisor says it overlaps with the preceding section.

Expected axes: section is the named thesis subsection; source is `user-materials`; operation is `revise`.

Expected references: `style/local-thesis-style.md` and the focused section guide.

Expected output contract: direct replacement prose first, with chapter-role explanation placed only in the writing rationale when needed.

Must do: State the engineering object, inherited model or formula, changed parameters, processing steps, outputs, and boundaries directly; retain technical section cross-references when they identify a reused model, method, or definition.

Must not: Put “前一节解决……本节解决……”“章节任务不同”“本节不再重复” or equivalent reviewer-facing chapter explanation into the thesis body.

Validation prompt: "导师说3.2和3.3重复，请修改3.3.3正文。正文只保留参数化建模与批量计算内容，章节区别可以在修改说明里解释。"

## Scenario: Scoped Visual QA For A Single-Section DOCX Edit

Mode: `docx-revision`

Trigger: The user asks to edit exactly one section in a long thesis DOCX and wants token-efficient visual verification.

Expected axes: section is the named thesis section; source is `user-materials`; operation is `docx-edit`.

Expected references: `workflows/docx-ooxml-editing.md` and the relevant thesis-writing guide.

Expected output contract: new revision path, edited scope, structural validation, and the changed section page range used for visual QA.

Must do: Render as required, visually inspect every page occupied by the changed section only, and use structural checks for unaffected parts; preserve the original file.

Must not: Create full-document contact sheets, inspect all pages, or claim a full-document visual audit for a local single-section edit.

Validation prompt: "只改Word中的3.3.3小节。生成新版本并检查该小节所在页，不要检查全文所有页面。"

## Scenario: HFUT Bilingual Figure, Table, And Equation Objects

Mode: `docx-revision`

Trigger: The user asks to create or revise figures, tables, and numbered equations in the author-confirmed HFUT thesis Word format and names the local reference as the structural authority.

Expected axes: section is the edited thesis section; source is `local-style-corpus` plus `user-materials`; operation is `docx-edit`.

Expected references: `style/hfut-thesis-word-objects.md`, `workflows/docx-creation-and-formatting.md` for new objects, and `workflows/docx-ooxml-editing.md` for existing objects.

Expected output contract: updated DOCX path or an executable object contract, authority statement, OOXML validation results, and changed-section rendered-page results.

Must do: Use the 2-row × 1-column figure wrapper with both caption paragraphs in row 2; use external `表/Tab` captions plus a native three-line table; use a same-paragraph OMML Equation Array and Chinese callout `式（2.1）`.

Must not: Generalize the project convention to every HFUT template; create a third figure-caption row; wrap table captions around the data table; use `Table` or a 0.75 pt header rule; number equations with a three-column table or manual spacing.

Validation prompt: "按照已确认的合肥工业大学参考Word真实结构，建立图3.1、表3.1和式（3.1），并检查对象结构与该小节渲染页。"
