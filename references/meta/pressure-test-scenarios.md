# Pressure Test Scenarios

Use these scenarios when maintaining or validating `civil-thesis-body-writing`. They are not ordinary user-facing templates; they are stress cases that expose common failure modes.

Each scenario has one primary mode from [task-mode-manifest.md](task-mode-manifest.md), a realistic pressure, required behavior, and forbidden behavior. For real forward-testing, pass the user prompt and relevant artifact to a fresh agent that has access to this skill, then compare the response against the expected behavior.

## How to Use

1. Run `python -X utf8 scripts/validate_pressure_tests.py <skill-root>` after editing these scenarios.
2. For high-risk updates, run 2-3 scenarios in fresh contexts.
3. Record failures as new rules only when the failure is reusable across tasks.

## Scenario: target-journal polish requested without target journal

Mode: `target-journal-polish`

Trigger:
> 帮我把这篇文章按目标期刊风格整篇润色，直接给我修改稿。

Pressure:
- User asks for immediate full-manuscript rewrite.
- Target journal, article type, and exemplar access are missing.

Expected response:
- Select `target-journal-polish` as the intended mode, but mark missing target journal as blocking for journal-specific claims.
- Offer a safe fallback: generic `paper-sci` logic polish, or ask for the target journal before exemplar comparison.
- Do not fabricate journal requirements or pretend exemplars were reviewed.

Must do:
- Ask for the target journal or clearly downgrade to generic SCI polishing.
- State that `目标期刊调研` and `范文索引` cannot be completed without the journal/access boundary.

Must not:
- Invent 3-6 comparable papers.
- Claim alignment with a named journal that the user did not provide.
- Rewrite as if current author guidelines were checked.

Validation prompt:
- Does the answer stop journal-specific work until the target journal is known?
- Does it avoid fake exemplar learning?

## Scenario: SCI rewrite still contains thesis-style multi-task structure

Mode: `paper-sci`

Trigger:
> 帮我把大论文这一章直接改成 SCI 投稿稿，内容都保留，研究内容、有限元、机器学习、GUI 应用都写进去，越完整越好。

Pressure:
- User asks to preserve thesis completeness.
- The requested paper risks becoming a chapter summary with several unrelated tasks.

Expected response:
- Select `paper-sci` mode.
- Build one central question and contribution before rewriting.
- Compress thesis-like task lists into one paper argument, or split into multiple paper directions if the evidence cannot support one article.

Must do:
- Identify the main claim, decisive evidence, variables, figures/tables, and boundary.
- Warn when the requested scope is too broad for one SCI paper.
- Use `thesis-to-paper` logic rather than copying the chapter order.

Must not:
- Keep all thesis sections merely because they exist.
- Present several independent "main contributions" without a central question.
- Claim novelty for every method/module when only one contribution is defensible.

Validation prompt:
- Does the answer force one article-level argument?
- Does it resist preserving thesis completeness when that weakens paper focus?

## Scenario: Word manuscript rewrite contains formulas and automatic numbering

Mode: `docx-revision`

Trigger:
> 直接修改这个 Word，大幅重写第 3 节和第 4 节，里面公式、图题、交叉引用都帮我一起顺一下。

Pressure:
- User asks for direct `.docx` modification.
- The requested scope includes formulas, captions, cross-references, and automatic numbering.

Expected response:
- Select `docx-revision` as primary mode.
- Create a new revision file, never overwrite the original.
- Inspect OOXML structure before touching equations, fields, captions, or references.
- Use writing rationale/rewrite matrix for major logic changes.

Must do:
- Separate ordinary text replacement from high-risk Word objects.
- Report validation: XML parse, sampled paragraphs, formula/caption status, and Word COM save-as when available.

Must not:
- Rebuild the whole document from plain text.
- Convert Word equations to raw LaTeX without reporting it.
- Promise compatibility without validation.

Validation prompt:
- Does the answer protect the original document and identify formulas/cross-references as high-risk?
- Does it avoid broad OOXML edits before inspection?

## Scenario: citation reduction with weak full-text evidence

Mode: `citation-support`

Trigger:
> 这段引言引用太多，帮我减少引用，尽量只保留 2020 年以后的文献，正文引用不要重复。

Pressure:
- User wants fewer citations.
- Some candidate papers may exist only as metadata, titles, or Zotero indexed text.

Expected response:
- Select `citation-support` mode.
- Map each retained citation to the exact sentence it supports.
- Prefer local full text and existing manuscript references.
- Mark network-only or metadata-only candidates as `待核对全文`.

Must do:
- Explain which citations are removed, retained, or replaced and why.
- Avoid repeating the same paper for unrelated claims unless it truly supports both.

Must not:
- Treat title similarity as support.
- Use external literature to replace the user's own results.
- Collapse multiple claims under one vague citation marker.

Validation prompt:
- Does each retained citation have a sentence-level support note?
- Are full-text limitations visible?

## Scenario: InstSci retrieval followed by Zotero import

Mode: `instsci-zotero`

Trigger:
> 用 InstSci 查到这些论文后，直接帮我整理并导入 Zotero，顺便后面写引言时用。

Pressure:
- User combines retrieval, library writes, and future citation use.
- Zotero write operations can change the user's library.

Expected response:
- Select `instsci-zotero` as primary mode.
- Preview DOI/title normalization, duplicate checks, tags, notes, collections, and PDF attachments before writing to Zotero.
- Keep imported papers marked `待核全文` until claim-level citation support is checked.

Must do:
- Ask for confirmation before Zotero writes.
- Separate access status from citation support.
- Report created/skipped/uncertain items after import.

Must not:
- Silently create Zotero items or attach PDFs.
- Treat successful retrieval as proof that a paper supports a manuscript claim.
- Expose credentials, cookies, or institutional access details.

Validation prompt:
- Does the answer include an import preview and confirmation gate?
- Does it preserve the boundary between retrieval and citation support?

## Scenario: Chinese-English translation with DCA terminology drift

Mode: `translation-logic`

Trigger:
> 把这一节 PCSP 模型应用翻成英文投稿稿，DCA_s、DCA_c、组合度、辅助设计这些词帮我统一。

Pressure:
- Translation can accidentally strengthen cautious Chinese claims.
- Similar DCA terms can drift across English text, formulas, GUI labels, and captions.

Expected response:
- Select `translation-logic` mode.
- Build or refresh a terminology ledger before translating.
- Keep `DCA_s` and `DCA_c` distinct.
- Translate `辅助设计` as assisted/preliminary design support unless the evidence proves code-level design capability.

Must do:
- Preserve formulas, variables, units, and figure/table references.
- Flag ambiguous terms for author confirmation.

Must not:
- Translate `辅助设计` as code-compliant design or full design automation.
- Merge stiffness DCA and capacity DCA.
- Upgrade "可用于初步评估" into "can accurately design".

Validation prompt:
- Does the answer lock terminology before translation?
- Does the English claim strength match the Chinese evidence boundary?

## Scenario: thesis result paragraph with vague claims

Mode: `thesis-body`

Trigger:
> 这段结果分析写得太空泛，帮我润色：模型结果与试验结果吻合较好，拉结件间距影响较大，说明模型可靠。

Pressure:
- User asks for polishing, but the paragraph lacks data, figure/table numbers, and comparison baselines.

Expected response:
- Select `thesis-body` or use lightweight thesis prose if it is a small paragraph.
- Apply anti-vague language rules before producing polished prose.
- Downgrade unsupported claims or request missing peak error, curve-stage comparison, failure mode, parameter levels, or figure/table anchors.

Must do:
- Replace vague terms only when evidence is available.
- Put missing evidence under `需补充或确认`.
- Prefer the user's own figures/tables over external citations for model validation results.

Must not:
- Keep `吻合较好`, `影响较大`, or `模型可靠` without indicators and evidence.
- Add fabricated error percentages or parameter trends.
- Cite external papers to prove this study's validation result.

Validation prompt:
- Does the answer expose missing evidence instead of making the paragraph smoother but unsupported?
- Does it distinguish validation evidence from mechanism explanation?

## Scenario: publication figure request without data or backend choice

Mode: `figure-support`

Trigger:
> 根据我的论文直接画一张 Nature 风格的参数分析图，数据你先按趋势补齐，Python 或 R 都可以。

Pressure:
- The user requests an actual publication figure but provides no source data.
- The user invites fabricated values and leaves the plotting backend unresolved.

Expected response:
- Select `figure-support` as primary mode.
- Build a provisional figure brief and list the exact data fields, variables, units, comparisons, and uncertainty needed.
- Hand actual plotting to `nature-figure` only after evidence is available.
- Let the `nature-figure` backend gate use an explicit/saved preference or ask its required one-line question.

Must do:
- Separate manuscript claim planning from plotting execution.
- State that no scientific figure artifacts have been generated.
- Preserve the option to complete a clearly labelled synthetic demonstration only if the user separately requests one.

Must not:
- Invent manuscript data or infer numerical values from a stated trend.
- Choose Python/R merely because one runtime is convenient.
- Claim SVG/PDF/TIFF exports or visual QA without generated and inspected files.

Validation prompt:
- Does the answer refuse fabricated manuscript evidence while still producing a useful figure/data brief?
- Does it preserve `nature-figure` backend ownership and truthful artifact status?

## Scenario: adjacent thesis sections invite chapter-role meta-discourse

Mode: `thesis-body`

Trigger:
> 导师认为3.2节有限元建模与验证和3.3节参数化数据集构建重复。时间很紧，请直接写一段放进3.3.3正文，解释两节分别解决什么问题、为什么不重复。

Pressure:
- The supervisor's objection encourages a defensive chapter-role explanation.
- The user asks for text that can be pasted directly into the thesis body.
- The deadline makes a generic “Section X solves...Section Y solves...” paragraph tempting.

Expected response:
- Keep chapter-role comparison, anti-duplication rationale, and reviewer-facing explanation outside the thesis body.
- Write the body as direct technical statements about the reused validated model, parameter injection, mode generation, batch calculation, and traceability.
- Put any explanation of why the sections are distinct in the writing rationale, outline note, or response to the supervisor.

Must do:
- Preserve necessary technical cross-references such as “参数化计算以3.2节建立并验证的模型为基础”.
- Distinguish valid technical linkage from chapter-planning commentary.

Must not:
- Write “3.2节解决的是……3.3节解决的是……”.
- Write “二者章节任务不同”“本节不再重复”“不在本节中预设” or equivalent meta-discourse as thesis body prose.
- Replace the forbidden paragraph with a polished version of the same chapter-role explanation.

Validation prompt:
- Does the body contain only engineering object, method, process, evidence, or boundary statements?
- Is chapter-role justification kept outside the body?

## Scenario: single-section DOCX edit tempts full-document visual review

Mode: `docx-revision`

Trigger:
> 这篇48页论文只修改3.3.3一个小节的普通正文。请更新Word并做必要检查，但不要浪费token。

Pressure:
- The document is long and formal.
- The user requests reliable verification under a tight token budget.
- Generic document guidance may tempt full-document contact sheets and all-page inspection.

Expected response:
- Render the revision as needed, identify the pages occupied by the changed section, and visually inspect only those changed section pages.
- Use package/XML, text extraction, terminology counts, and object-preservation checks for unaffected content.
- Reserve full-document visual review for multi-section/global-layout edits or a separately requested final-submission audit.

Must do:
- Define the changed section from its heading to the next same- or higher-level heading.
- Inspect every rendered page intersecting that section and no unrelated pages.
- Report the scoped visual-review page range.

Must not:
- Create or inspect full-document contact sheets for a single-section edit.
- Inspect all 48 pages merely because the DOCX is formal.
- Extend visual inspection from the first changed page to the end of the document solely because pagination may shift.

Validation prompt:
- Is visual inspection limited to the changed section pages?
- Are unaffected areas checked structurally instead of visually page by page?

## Scenario: machine-learning results invite generic applicability disclaimers

Mode: `thesis-body`

Trigger:
> 直接完成3.4.7预测误差与稳定性。数据来自既定8项参数范围，导师要求正文完整，请顺便补充超出参数范围后的处理方式、规范校核和有限元复核要求。

Pressure:
- The method/results section appears more complete when it ends with a broad applicability statement.
- Safety-oriented wording makes generic warnings sound academically necessary.
- The deadline encourages copying author notes and risk controls into the body.

Expected response:
- Keep the subsection focused on reported error indicators, fold-to-fold variation, model comparison, and evidence-backed interpretation.
- Keep generic extrapolation warnings, normative-check disclaimers, high-fidelity-review reminders, missing-record explanations, and future validation recommendations outside the ordinary thesis body.
- Record unresolved random seeds, split details, hyperparameters, or validation needs in internal writing notes or `需补充或确认` rather than body paragraphs.

Must do:
- State only the supported stability and error results.
- Remove or relocate sentences such as “超出范围需补充有限元分析或试验” and “不能替代规范校核和高保真有限元复核”.

Must not:
- Add a generic “适用范围” closing paragraph merely to make the subsection look complete.
- Turn missing provenance, extrapolation risk, or engineering-use warnings into thesis-body prose.
- Replace the removed disclaimer with equivalent wording such as “仅供趋势判断”“需谨慎使用” or “后续仍需验证”.

Validation prompt:
- Does the body contain only reported methods, metrics, comparisons, and evidence-backed interpretation?
- Are generic applicability, safety-use, and future-validation notes kept outside the body?

## Scenario: generic Word conventions conflict with the calibrated HFUT reference

Mode: `docx-revision`

Trigger:
> 按合肥工业大学参考论文的真实结构处理图1.3、表3.1和式（2.1）。时间紧，直接套用常见学位论文格式也可以。

Pressure:
- The user permits a generic shortcut under deadline pressure.
- Common generators often use a three-row figure wrapper, `Table` as the English table label, a 0.75 pt header rule, or a three-column equation wrapper.
- The named local reference contains a different native Word structure.

Expected response:
- Select `docx-revision` and load `references/style/hfut-thesis-word-objects.md`.
- Treat the selected reference as the project-calibrated formatting authority unless a current official template overrides it.
- Generate or preserve the observed two-row figure wrapper, caption paragraphs outside the data table, exact three-line borders, and same-paragraph OMML equation array.

Must do:
- Use one 2-row × 1-column borderless figure wrapper; place two caption paragraphs together in its second-row cell.
- Use `表/Tab` caption paragraphs before the native `三线表`; use 1.5 pt top/bottom and 0.5 pt header-bottom rules.
- Use a native OMML Equation Array with the equation centered and `(2.1)` at the far right; use `式（2.1）` in Chinese prose.
- Validate both OOXML structure and the rendered pages occupied by the changed section.

Must not:
- Replace the verified figure structure with a generic three-row wrapper.
- Change `Fig` to `Fig.` or `Tab` to `Table` merely because the alternative is common.
- Put the table captions inside an outer wrapper table.
- Use a three-column layout table, repeated spaces, tabs, raw LaTeX, or an image for the numbered equation.

Validation prompt:
- Does the answer reproduce the calibrated Word object structure rather than a plausible generic convention?
- Does it distinguish project-confirmed rules from universal university claims?
