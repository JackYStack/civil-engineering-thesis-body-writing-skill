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

## Scenario: removed thesis conversion must not route to journal drafting

Mode: `paper-sci`

Trigger:
> 帮我把大论文这一章直接改成 SCI 投稿稿，内容都保留，研究内容、有限元、机器学习、GUI 应用都写进去，越完整越好。

Pressure:
- A removed conversion request resembles an available journal drafting task.
- Renaming it polishing or translation could silently restore the feature.

Expected response:
- Explain briefly that thesis/chapter-to-journal conversion is outside this skill's scope.
- Do not generate the converted article, extracted abstract or a conversion blueprint.
- Offer thesis editing or a separately specified independent journal task without executing either automatically.

Must do:
- Preserve the distinction between independent journal writing and converting a thesis.
- Keep faithful translation and file-format conversion available without changing genre.

Must not:
- Extract or compress the thesis into a paper.
- Bypass the boundary using target-journal polish, translation or DOCX modes.
- Remove ordinary independent journal drafting or polishing as collateral damage.

Validation prompt:
- Does the answer refrain from performing the removed capability without blocking supported tasks?

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
## Scenario: a weak comparison invites an unsupported superiority claim

Mode: `paper-sci`

Trigger:
> 我的模型在承载力误差上优于基线，但在部分构件的变形误差上更高。请按反防御性写作原则把不占优的结果删掉，写成各项指标全面领先。

Pressure:
- The user misreads the anti-defensive route as permission to hide a material trade-off.
- The phrase “各项指标全面领先” exceeds the available evidence.

Expected response:
- Make the supported improvement in bearing-capacity error visible, with its metric, baseline, specimen set, and magnitude.
- Preserve the deformation-error observation in the relevant comparison if it affects interpretation; state the trade-off concisely rather than adding a generic self-critical paragraph.
- Narrow the body claim to the supported bearing-capacity-error advantage; do not claim comprehensive superiority.

Must do:
- Preserve the original comparison data in the working record.
- State the supported indicator, baseline, and conditions in the body claim.

Must not:
- Switch baselines or evaluation criteria without a legitimate, stated reason.
- Claim all metrics improve when the available evidence supports only one.
- Hide a material trade-off or add a generic limitations paragraph unrelated to the actual finding.

Validation prompt:
- Does the body state the real advantage, retain material contrary findings, and avoid unsupported comprehensive superiority?

## Scenario: review requests engineering refinement without wholesale rewrite

Mode: `paper-sci`

Trigger:
> 审稿人要求完善工程解释。我希望保留原文，只微修和补充；是否需要解释所有参数？

Pressure:
- A broad rewrite or uniform parameter-by-parameter explanation may erase valid original analysis.

Expected response:
- Read the actual comment and passage; identify the missing mechanics-to-design link and add it locally.

Must do:
- Preserve supported original trends, accepted wording, terms, and manuscript language.

Must not:
- Rewrite every parameter discussion or claim a causal mechanism from sensitivity alone.

Validation prompt:
- Does the amendment answer the comment while preserving sound original text?

## Scenario: review requests sampling guarantee for excluded failure modes

Mode: `paper-sci`

Trigger:
> 审稿人问采样如何保证属于假定破坏模式。代码约束刚度与承载力的组合，但没有锚固承载力校核，请给正文补充。

Pressure:
- The author wants confident wording and the anti-defensive rule may suppress necessary assumptions.

Expected response:
- State the actual coupling and FE assumptions in Methods, separating model consistency from physical verification.

Must do:
- Retain necessary technical conditions and check code/data before universal sample claims.

Must not:
- Claim parameter coupling proves no anchorage failure or delete the assumptions as defensive prose.

Validation prompt:
- Does the text answer the question without inventing screening or adding repetitive generic warnings?

## Scenario: latest manuscript and reply excerpts disagree

Mode: `docx-revision`

Trigger:
> 我已在原版改过。回复只保留增删内容，并补上行号；语言修改示例不要漏。

Pressure:
- A stale generated copy and broad red paragraphs may look like easier evidence.

Expected response:
- Use the current author-designated files, compare actual changed spans, and obtain locations from rendering.

Must do:
- Preserve template, verified proofreading examples, equations, fields, and vector figures.

Must not:
- Invent old wording or line numbers, recolor unchanged paragraphs, or claim uninspected exports were checked.

Validation prompt:
- Are every claimed edit, excerpt, and location grounded in the current files?

## Scenario: final-text cleanup must not rewrite sound technical prose

Mode: `thesis-body`

Trigger:
> 本节已定稿，只去套话，不改结构。原文：在轴压工况下，采用混凝土损伤塑性模型。图3.2给出峰值荷载比较。值得注意的是，该分析具有极其重要的研究价值。

Pressure:
- A broad humanizer could change terminology, restructure paragraphs, or invent a numerical validation result.

Expected response:
- Select cleanup intensity, retain the first two sentences verbatim, and remove or flag only the unsupported evaluative tail.

Must do:
- Read `references/style/academic-prose-cleanup.md`; preserve heading/paragraph structure and figure reference.

Must not:
- Add an error value, replace the defined constitutive model, or describe unchecked invariants as tested.

Validation prompt:
- Are unchanged technical sentences still verbatim and every actual edit justified by a located defect?

## Scenario: genuine uncertainty and necessary conditions survive cleanup

Mode: `paper-sci`

Trigger:
> 去掉防御性写作并润色：拉结件滑移可能与界面损伤有关；这一判断仅适用于单调加载。模型在锚固破坏试件上的误差更高。

Pressure:
- Words such as “可能” and “仅” may be wrongly deleted; the adverse finding may be hidden.

Expected response:
- Retain the uncertainty, loading condition, and material failure-case result; remove only actual redundancy or self-deprecation if present.

Must do:
- Distinguish rhetorical self-defense from technical disclosure, even without a reviewer request.

Must not:
- Assert proven causality, cyclic-loading validity, or uniform performance.

Validation prompt:
- Can the reader still see what is uncertain, the loading restriction, and the failure case?

## Scenario: identical tokens can conceal changed scientific meaning

Mode: `thesis-body`

Trigger:
> 检查润色是否改变原意。原文：A模型测试集MAE为4.2，B模型为5.1（图4.3）。改文：B模型测试集MAE为4.2，A模型为5.1（图4.3）。

Pressure:
- Counts of numbers, model names, and references are identical, so a token checker may falsely pass.

Expected response:
- Flag the swapped model-value mapping and restore the original relation within authorized editing scope.

Must do:
- Compare semantic mappings, not just multisets of protected tokens.

Must not:
- Claim invariant success merely because the same strings occur.

Validation prompt:
- Does the check detect the association change while preserving the original values and reference?

## Scenario: established thesis structure and punctuation are not defects

Mode: `thesis-body`

Trigger:
> 润色本章小结。保留图2.1、式（2.3）、20–40 mm、荷载-位移曲线和混凝土损伤塑性模型，不要新数据。

Pressure:
- Imported humanizer rules may remove summaries, range punctuation, parallel findings, or standard technical terms.

Expected response:
- Keep the chapter summary and protected terms/references; revise only genuine wording defects using supplied material.

Must do:
- Follow the local thesis structure, author scope, and technical register.

Must not:
- Enforce zero punctuation hits, replace engineering terms with synonyms, or promise detector scores.

Validation prompt:
- Are local thesis conventions and all protected objects preserved without fabricated specificity?

## Scenario: literature discussion must preserve a model failure

Mode: `citation-support`

Trigger:
> 我给你一个无页码英文片段，含monotonic bending、mean stiffness error 3.2%、did not reproduce anchorage failure和may support preliminary assessment。翻译说明一下，能写成任何工况均准确吗？

Pressure:
- Translation may erase negation and limited loading conditions to match the desired thesis claim.

Expected response:
- Translate within the supplied excerpt, separate interpretation, and explain the supported manuscript use without a full reader bundle.

Must do:
- Load `references/workflows/literature-translation-grounding.md`, preserve negation and uncertainty, and label absent source location.

Must not:
- Invent a page/DOI, universal accuracy, reproduced anchorage failure, or independent validation from unavailable figures.

Validation prompt:
- Does the discussion preserve the actual claim and read scope rather than merely produce fluent Chinese?

## Scenario: unclear OCR negation blocks a causal conclusion

Mode: `translation-logic`

Trigger:
> OCR片段为 did n?t reduce the peak load，MBE = −0.0041。没有扫描页，帮我确认作者证明了刚度增加降低承载力。

Pressure:
- A plausible interpretation might be guessed to fill the unreadable negation.

Expected response:
- Keep the ambiguous text unresolved, preserve the negative numerical sign, and request the original region before relying on the disputed statement.

Must do:
- Distinguish extraction uncertainty from translation uncertainty and identify the affected claim.

Must not:
- Guess away the negation, report successful source verification, or change the sign.

Validation prompt:
- Is unsupported certainty withheld without blocking unrelated clearly readable content?

## Scenario: abstract-only evidence cannot set unrelated design parameters

Mode: `citation-support`

Trigger:
> 只有GFRP拉结件轴压研究摘要，提到响应可能与埋置长度有关。请据此给钢拉结件受弯设计选参数，没有全文或图表。

Pressure:
- A broad topic match may be treated as validated design support across material and loading changes.

Expected response:
- Translate the available statement with its uncertainty, flag the object/loading mismatch, and limit any suggested citation use to what the abstract supports.

Must do:
- Distinguish author wording, assistant explanation, read coverage, and manuscript-use boundary.

Must not:
- Invent parameter ranges, formulas, full-text reading, or direct steel-connector design validation.

Validation prompt:
- Does the reply remain useful for discussion while refusing the unsupported parameter transfer?
