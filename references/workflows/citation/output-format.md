# Citation Output Format

Use this guide when inserting citation markers, building a support bank, or returning citation candidates to the user.

## Marker Rules

- Use temporary markers `[R1]`, `[R2]`, ... unless the user provides a stable numbered bibliography.
- Reuse existing manuscript reference numbers when the source is clearly matched.
- Keep one marker per focused claim when possible.
- For one sentence supported by multiple sources, group markers: `[R1, R2]` or `[R1-R3]`.
- Do not cite every sentence if a focused paragraph group is supported by the same source cluster.
- If a paragraph mixes user results and literature mechanism, cite only the literature mechanism sentence.
- Do not renumber the final bibliography unless the user explicitly asks for bibliography integration.

## Support Bank Scale

Build a candidate support bank before insertion for substantial introduction, research-status, discussion, or independent journal tasks.

Recommended scale:

- short subsection: 3-8 strong candidates;
- introduction or research-status section: 10-25 candidates;
- SCI Introduction or Discussion: enough candidates to cover background, gap, method, comparison, and boundary claims;
- ordinary thesis paragraph: only the candidates needed for its actual claims.

Do not force a large bank when the section has few external claims.

## Candidate Table

Use this table whenever citations are inserted:

| 临时编号 | 引用功能 | 支撑句/支撑论点 | 文献 | 年份 | 来源/路径/DOI | 验证状态 | 支撑等级 | 备注 |
|---|---|---|---|---:|---|---|---|---|
| [R1] | 背景引用 | ... | Author, Title | 2024 | local path or DOI | 已有全文 | 强支撑 | 支撑第X段第Y句 |

Required fields:

- `临时编号`: marker used in the draft;
- `引用功能`: background, gap, method, comparison, or boundary;
- `支撑句/支撑论点`: a sentence-level claim, not a broad topic;
- `文献`: author/title or enough metadata to identify the source;
- `年份`: publication year when known;
- `来源/路径/DOI`: local path, DOI, publisher URL, Zotero record, or search source;
- `验证状态`: full text, abstract, metadata, snippet, official page, or pending full-text check;
- `支撑等级`: support grade from [support-grading.md](support-grading.md);
- `备注`: where to use it and what limitation remains.

## Draft Output Shape

For citation-support tasks, return:

1. `正文稿`: revised draft with temporary markers or reused manuscript numbers.
2. `引用候选清单`: candidate table with sentence-level support notes.
3. `写作依据`: which claims rely on user data and which rely on literature.
4. `需补充或确认`: missing full text, weak support, standards/code needs, or claims that should be downgraded.

For simple citation reduction, return:

1. `建议保留引用`;
2. `建议删除或合并引用`;
3. `删除原因`;
4. `可能缺口`.

## Claim-To-Citation Workflow

1. Segment the draft into citable claims.
2. Skip claims that are purely the user's own results and should cite figures/tables instead.
3. Search local sources using precise keywords.
4. Select the smallest set of sources that strongly supports the claims.
5. If local support is weak or fewer than two strong sources are found for a major background/research-status paragraph, use web or InstSci fallback.
6. Insert temporary markers into the draft.
7. Output the citation candidate table.
8. Flag unsupported claims or sources needing full-text confirmation.

Before returning, check that every inserted marker has a table row and every table row states which sentence it supports. Remove unused weak candidates from the main draft; keep them only as optional notes if useful.

## Do Not Hide These Problems

Report these explicitly:

- citation marker has no candidate row;
- candidate row lacks DOI/path/source or verification status;
- source is metadata-only but used as full-text evidence;
- source supports topic but not sentence;
- external citation is being used for the user's own result;
- final reference numbering and temporary numbering are mixed without explanation.
