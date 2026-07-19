# Target-Journal Polish and Full-Manuscript Revision Workflow

Use this reference when the user asks for target-journal polishing, SCI submission polishing, journal-specific rewriting, whole-manuscript English revision, or matching a manuscript to a named journal such as `Engineering Structures`, `Structures`, `Journal of Building Engineering`, `Construction and Building Materials`, etc.

This is a branch workflow. Do not run it for ordinary thesis-section writing or short paragraph polishing.

## Trigger Phrases

Activate this workflow when the user asks for:

- `目标期刊润色`, `按目标期刊修改`, `期刊适配`, `投稿前修改`;
- `整篇SCI润色`, `英文投稿稿整篇修改`, `SCI投稿稿重写`;
- `对标Engineering Structures/Structures/JOBE/...`;
- `下载/学习几篇同方向范文`;
- `比较我的论文和目标期刊论文的风格、字数、深度`;
- `判断亮点是否符合期刊偏好`.

## Required Inputs

Before full execution, identify:

| Field | Required? | Notes |
|---|---|---|
| Target journal | Yes | If absent, ask for it or offer 2-3 suitable candidates only when the user asks for journal selection. |
| Manuscript path/text | Yes | Word/docx, Markdown, LaTeX, or pasted text. |
| Research object and contribution | Yes | Needed for finding comparable papers and checking journal fit. |
| User evidence | Yes | Figures, tables, formulas, data, metrics, or results. |
| Reference access | Optional | Local library/Zotero/PDF folder preferred; web fallback only when needed. |
| Output form | Optional | analysis report, revised sections, revised docx, English draft, cover-letter points, etc. |

## Stage 1 — Target Journal Research

Search or inspect current target-journal information when the task depends on it. Prefer official and primary sources:

1. journal aims and scope;
2. guide for authors or submission instructions;
3. article type, word/page limits, abstract/keyword limits, graphical abstract or highlights requirements;
4. reference style and figure/table conventions;
5. recent accepted papers in the same field.

Record findings as:

| Item | Journal Requirement or Pattern | Source | Impact on This Manuscript |
|---|---|---|---|

Do not rely on memory for current author guidelines, APC policy, article type rules, or formatting requirements. These can change.

When journal requirements are gathered through web pages, publisher pages, literature-search skills, or API/database outputs, follow [external-source-and-tool-use.md](external-source-and-tool-use.md): record source URL/DOI, query or selection rule, access status, and reviewed-result boundary.

## Stage 2 — Exemplar Paper Collection

Collect 3-6 comparable target-journal papers.

Selection priority:

1. same journal + same component/material/problem;
2. same journal + adjacent method or object;
3. same publisher/journal family + same object;
4. high-quality SOTA papers only when the target journal lacks close examples.

Download/access policy:

- Use local PDFs, Zotero attachments, user-provided files, publisher open-access PDFs, author-accepted manuscripts, arXiv/preprints, or official pages.
- Use [instsci-paper-retrieval-workflow.md](instsci-paper-retrieval-workflow.md) when DOI batch retrieval, publisher PDF access evidence, closed-access verification, or authorized target-journal exemplar acquisition is needed.
- Do not bypass paywalls, institutional access restrictions, DRM, or private databases.
- Do not record a final publisher PDF verdict from HTTP/curl/metadata alone. Treat those routes as `HTTP preflight`; final access/no-access claims require visible-browser evidence.
- If only metadata/abstract is available, mark `metadata only` and do not claim full-text style analysis.
- Save or report a source index when files are downloaded or collected.
- Keep exemplar use separate from citation use: a paper can calibrate style/structure without becoming a manuscript citation.
- For downloaded or collected exemplars, record query terms, filters, DOI/URL/path, access status, and whether full text or metadata only was reviewed.

Recommended source index:

| Exemplar ID | Title | Journal | Year | Why Comparable | Access Status | Path/DOI/URL | Use |
|---|---|---:|---:|---|---|---|---|

Use labels such as `local full text`, `Zotero full text`, `open access retrieved`, `browser verified`, `HTTP preflight`, `metadata only`, `auth_required`, or `blocked`. Only full text can support section-depth style metrics such as paragraph length, figure placement, discussion moves, and conclusion style.

## Stage 3 — Whole-Manuscript Structure and Style Metrics

Compare the user's manuscript with exemplars at the level of structure, not only language.

Metrics to extract when full text is available:

- section order and heading names;
- abstract length and rhetorical moves;
- introduction paragraph count and literature-review density;
- methods length and reproducibility depth;
- results/discussion balance;
- number and placement of figures/tables;
- conclusion count and claim style;
- citation density and citation functions;
- average paragraph length;
- use of quantified results in abstract, results, discussion, and conclusion;
- boundary/limitation placement.

Use this table:

| Dimension | Target Journal / Exemplar Pattern | Current Manuscript | Gap | Action |
|---|---|---|---|---|

Do not force the user's paper to imitate one exemplar. Identify repeated patterns across several comparable papers.

## Stage 4 — Contribution-to-Journal Fit Check

Check whether the manuscript's亮点 fit the target journal's apparent preferences.

Use this matrix:

| Manuscript Claim/Highlight | Evidence Anchor | Journal Preference or Exemplar Pattern | Fit | Needed Adjustment |
|---|---|---|---|---|

Fit labels:

- `strong`: journal scope and exemplars commonly accept this type of contribution, and the user's evidence supports it.
- `moderate`: contribution fits scope but needs clearer evidence, comparison, or boundary.
- `weak`: contribution is too narrow, too local, too under-validated, or not aligned with journal emphasis.
- `risky`: overclaims beyond evidence or likely reviewer objection.

Typical civil-engineering journal preferences to check:

- validated model rather than unvalidated calculation;
- quantified comparison rather than qualitative claim;
- mechanism explanation rather than pure prediction;
- reproducible method details;
- parameter range and applicability boundary;
- discussion of limitations, uncertainty, or engineering use;
- contribution stated as a concrete output: design equation, validated FE model, ML prediction workflow, experimental dataset, connector behavior mechanism, DCA evaluation method, or assisted design tool.

## Stage 5 — Revision Blueprint

Before rewriting the whole manuscript, create a target-journal writing rationale matrix.

| Unit | Current Problem | Target-Journal Pattern | Evidence Anchor | Planned Change | Risk |
|---|---|---|---|---|---|

Required decisions:

- title: expose object and contribution;
- abstract: include problem, method/data, variables, quantified results, and boundary;
- introduction: narrow to the exact gap and reduce unrelated literature;
- methods: ensure reproducibility without thesis-style over-detail;
- results: organize by indicator and evidence;
- discussion: add mechanism, comparison, uncertainty, and boundary;
- conclusion: keep only proven claims, preferably 3-5 concise items;
- figures/tables: keep only those that support the manuscript's central claim;
- references: remove weak decorative citations and add claim-level support where needed.

## Stage 6 — Full-Manuscript Rewrite

Rewrite according to the blueprint, not by applying surface polish paragraph by paragraph.

Rules:

- Preserve all validated user data, figure/table numbering, formulas, and terms unless the user asks to restructure them.
- Do not invent new experiments, metrics, comparisons, p-values, or references.
- Use target-journal exemplars to calibrate depth and structure, not to copy phrasing.
- If the manuscript is a Word/docx file, follow [docx-ooxml-editing.md](docx-ooxml-editing.md) and create a new revision file.
- If the user asks for English, first fix logic and claim strength, then polish language.

## Stage 7 — Final Submission-Oriented Audit

Before returning the final manuscript or revised sections, check:

- target journal scope and article type fit;
- abstract length, keywords, highlights, graphical abstract or declaration requirements if applicable;
- claim-evidence-boundary consistency;
- figure/table order and captions;
- citation function and reference freshness;
- terminology and symbol consistency;
- conclusion does not introduce new results;
- remaining gaps that require author decision.

## Output Format

For target-journal polish/revision:

1. `目标期刊调研：` aims/scope, author-guide constraints, exemplar selection logic.
2. `范文索引：` 3-6 comparable papers with path/DOI/URL and access status.
3. `全文风格量化对比：` structure, section length, paragraph length, figures/tables, citation density, result/discussion depth.
4. `亮点-期刊匹配矩阵：` contribution fit, evidence, risks, and adjustment.
5. `重写蓝图：` unit-by-unit planned changes.
6. `修改稿/修改文件：` revised text or new docx path.
7. `投稿前风险：` unresolved data, missing references, journal requirement gaps, or author decisions.
