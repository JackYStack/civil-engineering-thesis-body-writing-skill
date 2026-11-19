# Output Contracts

Use this file with [task-mode-manifest.md](task-mode-manifest.md). A contract defines what the response must contain for each task mode.

Prefer the smallest contract that completes the task. Do not paste every possible section into every response.

## Global Contract Rules

- Lead with the deliverable, not a long explanation.
- Keep citations, evidence, and uncertainty visible when they affect the prose.
- Put unresolved evidence, weak citations, missing standards, Word risks, or author decisions under a clearly labelled risk/confirmation section.
- Do not mix final reference numbering with temporary markers unless the user provides an existing numbering system.
- For file-producing work, report output path and validation performed.

## Reviewer-driven local revision

For a single review comment or local amendment, use this smaller contract instead of a full paper-rebuilding package: give the insertion/replacement location with a searchable original-text anchor, the ready-to-paste passage in the manuscript language, and a brief explanation of the actual change. Include unresolved evidence only when material. Provide old/new snippets when requested or useful for proofreading. Distinguish proposed text, author-reported completion, and edits verified in the current file. Add the reply text only when requested; use `nature-response` if available for a full response package. Do not invent line numbers before rendering the current manuscript.

## Contracts by Mode

### `thesis-body`

Required:

1. `正文稿`
2. `写作依据`
3. `需补充或确认`

Add when needed:

- `引用候选清单` if external support is inserted.
- `下一步建议` if the thesis will continue section by section.

### `paper-sci`

Required:

1. `论证架构`
2. `正文稿`
3. `证据与图表对应`
4. `SCI写作QC`
5. `需补充或确认`

Use `Nature-writing式论证架构` only when the user asks for high-level SCI, English manuscript rebuilding, or nature-writing adaptation.

### `target-journal-polish`

Required:

1. `目标期刊调研`
2. `范文索引`
3. `全文风格量化对比`
4. `亮点-期刊匹配矩阵`
5. `重写蓝图`
6. `修改稿/修改文件`
7. `投稿前风险`

If exemplar full text is unavailable, keep `范文索引` but mark access status and downgrade the comparison.

### `citation-support`

Required:

1. `需引用论点`
2. `引用候选清单`
3. `支撑等级`
4. `正文插入建议`
5. `待核对项`

Every candidate must state what sentence it supports.

### `docx-revision`

Required:

1. `修改文件`
2. `任务分支与格式依据`
3. `修改/生成范围`
4. `主要修改`
5. `验证结果`
6. `剩余风险`

Add `写作理由矩阵` or a saved matrix path for formal manuscript-level edits.
For `create` or `convert`, state the formatting authority and unresolved specification fields. For `revise`, state that the original was preserved and whether tracked changes, fields, comments, and equations were left intact.

### `translation-logic`

Required:

1. `术语校准`
2. `逻辑校准`
3. `译文/修订译文`
4. `需作者确认`

For paragraph-by-paragraph work, keep the source paragraph and translation aligned.

### `instsci-zotero`

Required:

1. `导入预览`
2. `需确认操作`
3. `导入结果`
4. `访问与引用边界`
5. `后续动作`

Never hide Zotero write operations.

### `thesis-audit`

Required:

1. `审查依据与范围`
2. `Readiness Gate`
3. `格式问题台账`
4. `关键报告与证据状态`
5. `修复预览`
6. `终稿交付清单`
7. `需作者/导师确认`

Use `PASS`, `WARN`, `BLOCK`, `UNAVAILABLE`, and `NOT_APPLICABLE` consistently. State the artifact source of truth, controlling specification/ruleset, skipped checks, and whether machine-readable evidence was generated.

### `figure-support`

Required:

1. `Figure brief`
2. `Handoff status`
3. `Figure artifacts`
4. `Figure QA`
5. `Manuscript reintegration`
6. `Unresolved evidence or blockers`

For planning-only tasks, mark artifact fields `not generated`. For execution tasks, state whether `nature-figure` was loaded, which backend it selected, which files were generated, and which final-size/export checks actually ran.

## Contract Failure Modes

Flag the output before final response if:

- the selected mode is unclear;
- the answer uses a contract from another mode;
- a file path is promised but no file is created;
- citation candidates appear without sentence-level support notes;
- a `.docx` deliverable lacks its `create/convert/revise` branch, formatting authority, or validation details;
- a thesis conclusion contains a new unsupported result;
- a journal-polish answer lacks target-journal evidence.
- a thesis audit treats a generic ruleset, skipped check, or HTML reading surface as authoritative compliance evidence.
- a figure-support answer bypasses `nature-figure` for actual plotting, invents data, omits the backend status, or claims artifacts/QA that were not generated and inspected.
