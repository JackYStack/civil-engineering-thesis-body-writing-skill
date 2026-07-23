# Thesis Format and Final-Audit Workflow

Use this workflow for deterministic or evidence-based review of thesis formatting, structure, cross-references, final-cleanup residue, statistical notation, and submission readiness. It adapts reusable concepts from [quzhiii/thesis-skills](https://github.com/quzhiii/thesis-skills) while keeping prose writing, institutional policy, and file-format editing under `civil-thesis-body-writing` controls.

For command-level integration with an installed thesis-skills checkout, also load [thesis-skills-audit-workflow.md](thesis-skills-audit-workflow.md). For Word generation or editing, use [docx-creation-and-formatting.md](docx-creation-and-formatting.md) and [docx-ooxml-editing.md](docx-ooxml-editing.md).

When auditing the author-confirmed HFUT thesis Word project, load [hfut-thesis-word-objects.md](../style/hfut-thesis-word-objects.md) as the calibrated object-level ruleset for figures, tables, bilingual captions, and numbered OMML equations.

## Select the artifact path

| Source artifact | Primary audit path | What can be asserted | Main limitation |
|---|---|---|---|
| LaTeX project | deterministic checker plus selected rule pack, compile evidence, and rendered PDF | source-level structure, labels, references, configured rules, compile diagnostics | generic rules do not prove school compliance |
| Existing DOCX | styles/OOXML inventory, field and relationship checks, rendered-page inspection | Word object structure, style use, numbering/field status, visual compliance | thesis-skills LaTeX checks do not run directly on DOCX |
| PDF only | page inventory and visual/manual format audit | visible pagination, layout, captions, object placement, obvious inconsistencies | cannot reliably infer source styles, fields, labels, or hidden revision state |
| Mixed LaTeX/DOCX/PDF | select one source of truth, then compare exports | handoff and export consistency | conflicting sources must not be silently merged |

Do not convert a Word thesis to LaTeX merely to claim deterministic audit coverage. Use the native artifact path unless the user already maintains a controlled conversion workflow.

## Formatting authority

Resolve authority in this order:

1. current university, faculty, degree, journal, or competition specification;
2. official template/class/reference document supplied for the submission;
3. author-confirmed project ruleset calibrated against that specification;
4. stable styles and conventions already present in the manuscript;
5. generic starter rules, explicitly labelled as provisional.

An automated checker validates only encoded rules. It does not prove compliance with requirements that were never encoded or inspected.

## Rule-pack calibration

Keep policy separate from checking mechanics. A ruleset should record at least:

| Dimension | Policy to define |
|---|---|
| `project` | main source candidates, chapter paths, bibliography paths, report directory |
| `reference` | missing keys, duplicate/conflicting entries, unused entries, metadata quality and severity |
| `language` | punctuation, brackets, CJK/Latin/number/unit spacing, full-width/half-width usage |
| `language_deep` | overclaim signals, formulaic transitions, collocation risks, boundary statements, acronym first use |
| `consistency` | canonical terminology, symbols, abbreviations, statistical notation, allowed variants |
| `format` | required front matter, figure/table lists, captions, labels, centering, numbering and cross-reference policy |
| `content` | required sections, abstract/keyword constraints, submission-specific components |
| `compile` | engine expectations, blocking errors, warnings, unresolved citations/references, overflow diagnostics |

Calibration procedure:

1. cite the controlling specification and its date/version;
2. map each auditable requirement to a rule ID, expected value, severity, and detection method;
3. mark non-automatable requirements as manual checks rather than omitting them;
4. run against representative clean and intentionally broken samples;
5. downgrade noisy rules, disable inapplicable rules, and add missed mandatory requirements;
6. version the calibrated ruleset and retain the mapping from specification clause to rule.

Generic university or journal packs are starting points. Do not rename a generic pack after a school and treat it as calibrated.

## Format audit matrix

Use the matrix to define audit scope before running checks. `Deterministic` means a stable source-level test is possible; `Rendered/manual` means visual or human confirmation remains necessary.

| Dimension | Checks | Evidence | Typical handling |
|---|---|---|---|
| Project discovery | main source, chapter set, bibliography, figures, report directory | discovered-file inventory and ruleset mapping | `BLOCK` if the intended source cannot be identified |
| Required components | title/front matter, abstracts, keywords, TOC, figure/table lists, references, appendices | source commands/styles plus rendered pages | severity follows the controlling specification |
| Heading structure | hierarchy, numbering, skipped levels, TOC inclusion, page-break behavior | style/command inventory and TOC comparison | deterministic structure plus rendered/manual confirmation |
| Figures and tables | object exists, caption exists, label exists, caption order, numbering, centering/alignment, list entry, in-text callout | source block/object inventory and rendered pages | missing mandatory caption/label may block; visual placement normally warns |
| Equations | native equation object, numbering, punctuation, symbol definition, in-text callout | OMML/LaTeX inventory, terminology ledger, rendered equations | never rewrite formulas during format-only repair |
| Labels and cross-references | broken target, duplicate label, unused/orphan label, unresolved field, stale number | source labels/refs, Word fields, compile log | broken required references block; orphan labels usually warn |
| Citations and references | unresolved citation, bibliography inclusion scope, style consistency, DOI/URL advisory status | source keys, bibliography, compile evidence, citation reports | keep local integrity separate from external metadata and claim support |
| Typography and page layout | page size, margins, fonts, spacing, indentation, headers/footers, page-number sections | template/specification, styles/OOXML, rendered-page samples | Word/PDF needs visual sampling; no generic default is authoritative |
| Language and terminology | punctuation, brackets, unit spacing, term/symbol variants, acronym first use | deterministic lint plus terminology ledger | auto-fix only allowlisted mechanical cases |
| Compile/export/review evidence | compile errors, unresolved references, overflow, Word/PDF export, review-loop closure | logs, output artifacts, handoff records | missing required evidence is `WARN` or `BLOCK`, never silent `PASS` |

The upstream deterministic format baseline specifically supports configured figure/table-list requirements, missing figure/table captions and labels, configured figure centering, broken cross-references, and orphan labels. Broader layout or institutional checks require calibrated rules and/or rendered inspection.

## Finding and gate model

Each finding should include:

| Field | Meaning |
|---|---|
| `dimension` | project, format, content, language, consistency, references, compile, export, or final audit |
| `rule_id` | stable rule/check identifier |
| `severity` | `BLOCK`, `WARN`, or `INFO` according to the calibrated policy |
| `location` | file/page/section/paragraph/object and line where available |
| `observed` | concrete detected state |
| `expected` | requirement and its authority |
| `evidence` | source fragment, object property, report field, log, or rendered-page observation |
| `action` | bounded fix or manual decision required |
| `fix_class` | `safe-preview`, `manual`, `author-decision`, or `not-applicable` |

Gate meanings:

- `PASS`: all configured mandatory checks ran and no blocker remains.
- `WARN`: review is required, optional evidence is absent, or a non-blocking inconsistency remains.
- `BLOCK`: a mandatory requirement, source integrity condition, or required delivery artifact is unresolved.
- `UNAVAILABLE`: a check could not run because the artifact, dependency, or access path was unavailable.
- `NOT_APPLICABLE`: the check is outside the selected artifact path or submission rules.

Never convert `UNAVAILABLE` or a skipped compile/render step into `PASS`. The overall verdict should be the strictest material dimension after documented waivers.

## Machine-readable reports are authoritative

- Treat JSON/CSV or equivalent structured reports as the source of truth for checker results and issue identity.
- Treat Markdown/HTML dashboards as reading and navigation layers only.
- A final-audit aggregator should summarize existing evidence; it should not rerun hidden checks or change source files.
- Preserve links from summary findings to the originating report, rule ID, and source location.
- Record missing, unreadable, stale, or version-mismatched reports explicitly.

For manual DOCX/PDF audits, create an equivalent structured Markdown/CSV ledger rather than reporting only a narrative impression.

## Bounded fixes

Use `report -> preview -> diff -> confirmation -> apply to copy/branch -> rerun`.

Potential low-risk candidates, only when the applicable rule is explicit:

- exact final-process markers such as unresolved TODO/FIXME/draft/debug annotations;
- mechanical spacing or punctuation cases with unambiguous spans;
- statistical-notation variants when one dominant project style is clear and the change does not alter values;
- a missing manual hyperlink anchor at an explicitly detected manual contents entry;
- a bibliography entry proven unused by both source citation and final-reference evidence.

Do not auto-fix:

- captions, labels, numbering, figures, tables, equations, or cross-reference targets;
- statistical values, effect estimates, uncertainty intervals, units, or result interpretation;
- prose claims, evidence strength, citation placement, or author conclusions;
- page layout, styles, or institution-specific settings without a confirmed template;
- tracked changes, comments, fields, bookmarks, or bibliography-manager links through broad text replacement.

An allowlisted fixer is still preview-first. Apply only to a new file, branch, or backed-up project and report every changed location.

## Final-audit extensions

Add these checks after the normal format/content/reference pass:

1. `final cleanup`: unresolved process markers, temporary color markup, placeholders, debug/draft residue;
2. `statistical consistency`: mixed notation families and deviations from the manuscript's confirmed dominant style;
3. `manual anchors`: manual TOC/figure-list/table-list entries with hyperlink-target risk;
4. `reference scope`: distinguish final compiled references, source-cited entries, and all bibliography entries;
5. `citation evidence`: keep local integrity, external metadata advisory checks, hallucination-risk signals, and claim-support review as separate layers;
6. `delivery evidence`: compile, rendered PDF, Word review export when required, review-loop closure, and unresolved waiver list.

Final cleanup is not permission to delete uncertain content. Statistical consistency is not a statistical-validity audit. External metadata failure is not proof that a reference is false.

## Delivery bundle

Return or save:

1. `审查依据`: artifact source of truth, template/specification, ruleset/version, tool/version, skipped checks;
2. `Readiness Gate`: overall and per-dimension `PASS/WARN/BLOCK/UNAVAILABLE/NOT_APPLICABLE`;
3. `格式问题台账`: stable finding rows ordered by severity;
4. `修复预览`: exact proposed changes, excluded changes, and confirmation requirement;
5. `验证结果`: rerun, compile, XML/package, export, and rendered-page checks actually completed;
6. `终稿交付清单`: revised artifact, structured reports, reading dashboards, waivers, and next actions.

Do not report a manuscript as submission-ready solely because a checker exits successfully. Submission readiness requires the controlling rules, expected evidence, and manual visual checks appropriate to the artifact.
