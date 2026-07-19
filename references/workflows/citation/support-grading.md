# Support Grading

Use this guide to decide whether a candidate source can support a sentence. Support grade and access status are separate.

## Sentence-Level Test

Before inserting a citation, answer:

- Which exact sentence or focused claim does the source support?
- Does the source match the research object, method, variable, output indicator, condition, and conclusion?
- Is the source being used for background, gap, method, formula, comparison, standard, or boundary?
- Is the evidence full-text checked, abstract-only, metadata-only, snippet-only, or official-document based?
- Does the claim instead need the user's own figure, table, formula, dataset, or section evidence?

If these questions cannot be answered, do not cite the source in the draft.

## Support Grades

| Grade | Meaning | Use |
|---|---|---|
| `强支撑` | Directly studies the same object, method, mechanism, variable, or output and supports the sentence. | Safe for focused technical claims. |
| `部分支撑` | Supports part of the sentence, but not all objects, variables, methods, or conclusions. | Use with narrowed wording or another source. |
| `背景支撑` | Supports broad field context, definitions, application background, or general demand. | Use in background, not for mechanism/result comparison. |
| `不建议引用` | Related by title, keyword, or field, but does not support the sentence. | Do not insert; optionally mention as excluded. |

For full-text workflows, add evidence-status labels:

| Evidence Status | Meaning |
|---|---|
| `全文强支撑` | Inspected full text directly supports the exact sentence. |
| `全文部分支撑` | Inspected full text supports only part of the claim or boundary. |
| `摘要支撑` | Abstract supports broad background only; avoid mechanism, result-comparison, or design claims. |
| `元数据仅发现` | Title/metadata found the source; not enough for citation insertion. |
| `全文片段抽样` | Only snippets or partial extracted text were reviewed; use for screening unless the exact claim appears in the inspected part. |
| `待核对全文` | Candidate may be useful, but full text or relevant content has not been checked. |

## Access Status Is Not Support

When InstSci, publisher pages, Zotero, or local files are used, record access separately:

| Access Status | Meaning |
|---|---|
| `open access retrieved` | A permitted/open full text was retrieved and can be inspected. |
| `browser verified` | Visible browser verified access or access failure. |
| `HTTP preflight` | HTTP/metadata route was checked but no final browser verdict was made. |
| `auth_required` | Institution login, SSO, CAPTCHA, or user action is required. |
| `blocked` | Access failed or is not permitted through the available route. |
| `unverified PDF` | A file exists but source/authenticity/access route has not been verified. |

Only access status plus actual content inspection can justify `全文强支撑` or `全文部分支撑`.

## Citation Function Tags

Assign one primary function to each inserted marker:

| Function | Use |
|---|---|
| `背景引用` | Research object, engineering demand, application context, classification, or definition. |
| `空白引用` | Existing studies do not cover a parameter range, connector type, loading condition, output, or design workflow. |
| `方法引用` | Model, formula, algorithm, evaluation metric, test method, or standard basis. |
| `比较引用` | Compare the user's results with published experimental, FE, analytical, or ML findings. |
| `边界引用` | Applicability limits, uncertainty, assumptions, parameter range, or future verification needs. |

One source can serve different functions in different places, but one inserted marker should support one focused sentence or claim.

## Common Failure Modes

Flag the candidate if:

- the title sounds related but the specimen type, connector type, loading state, parameter range, or method differs materially;
- the source supports a general field statement but is used for a mechanism or design conclusion;
- the source only appears in metadata but is treated as full-text evidence;
- one citation marker is asked to support background, method, and result claims at once;
- a network-only result is inserted without `待核对全文`;
- the paragraph cites external literature for the user's own original result.

When in doubt, downgrade the claim or move the source to the candidate table rather than inserting it in the text.
