# External Source and Tool Use Discipline

Use this guide when civil-thesis-body-writing relies on external search tools, APIs, database skills, Zotero connectors, literature-search skills, publisher pages, or downloaded exemplar papers. The purpose is to keep writing evidence traceable, rate-limit safe, and free from fabricated support.

This guide is adapted from the operational discipline used in science-skills: use existing wrappers, protect credentials, keep outputs bounded, record sources, and never turn metadata into unsupported manuscript claims.

## When to Apply

Apply this guide when any of the following are used:

- Zotero MCP/API, local RDF exports, or local full-text library search;
- OpenAlex, CrossRef, Semantic Scholar, PubMed, arXiv, Europe PMC, Google Scholar discovery, publisher pages, journal author guides, or official standard pages;
- InstSci paper retrieval, publisher PDF checks, DOI batch download, closed-access verification, or target-journal exemplar acquisition;
- downloaded target-journal exemplar papers;
- command-line wrappers or scripts that call external APIs;
- any source that may have access limits, rate limits, license limits, or metadata-only results.

Do not apply it to pure editing of user-provided text when no new source is queried.

## Source-Use Contract

Before using external material in writing, record:

| Field | Required Content |
|---|---|
| Source/tool | Zotero, local PDF, InstSci, OpenAlex, publisher page, journal guide, standard page, etc. |
| Query or selection rule | Search terms, filters, DOI/title lookup, target journal, date range, or local folder path. |
| Result boundary | Number of results reviewed, fields inspected, whether full text was available. |
| Evidence status | `已有全文`, `InstSci open access retrieved`, `InstSci browser verified`, `HTTP preflight`, `auth_required`, `blocked`, `摘要/元数据`, `官方页面`, `待核对全文`, or `不建议引用`. |
| Use in manuscript | Background, gap, method basis, comparison, boundary, style exemplar, or not used. |

Metadata can support discovery and bibliographic verification. It should not support a technical mechanism, result comparison, or design recommendation unless the relevant abstract/full text/official documentation was actually inspected.

## Credential and Access Safety

- Never ask the user to paste API keys, tokens, cookies, or private database credentials into chat.
- Never read, print, summarize, or expose `.env`, config files, browser cookies, or tokens.
- If a key is needed, provide a local command the user can run or ask them to configure it outside the conversation.
- Do not bypass paywalls, institutional restrictions, DRM, CAPTCHA, or private library access controls.
- If only metadata is available, mark the source as `metadata only` or `待核对全文` and do not overstate support.
- For InstSci/CloakBrowser workflows, the user must complete SSO, 2FA, CAPTCHA, or institutional login in the visible browser. Do not request, read, paste, or summarize passwords, OTP codes, cookies, API keys, or browser secrets.
- For Zotero MCP/API write workflows, preview the planned library changes and ask for user confirmation before creating items, importing attachments, writing tags/notes, adding collections, or updating metadata.

## Tool and API Discipline

- Prefer established skills, wrappers, or official APIs over improvised scraping.
- Respect rate limits and retry behavior. If a tool reports throttling, empty results, or API errors, report that boundary instead of fabricating results.
- Use narrow queries first; vary 3-5 high-quality queries for broad literature scans unless the user asks for exhaustive retrieval.
- For large JSON/CSV/API outputs, write results to a local file and inspect only bounded fields needed for the task, such as title, year, DOI, abstract, source, and URL.
- Keep source records small in the response; save long inventories to `analysis/` when they are needed for traceability.

## Output Control

When external tools produce more than a screen of results:

1. save raw or semi-raw output to an `analysis/` file when allowed;
2. create a slim reviewed table with only the rows and fields used for writing;
3. state how many records were searched, screened, and selected;
4. do not paste long API payloads into the final answer.

Recommended slim table:

| ID | Source/tool | Query/filter | Title/source | Year | DOI/URL/path | Access status | Use decision |
|---|---|---|---|---:|---|---|---|
| S1 | OpenAlex | PCSP + DCA | ... | 2024 | ... | metadata/abstract | candidate citation |

## Citation and Writing Rules

- Convert source findings into claim-level evidence using [citation-workflow.md](citation-workflow.md).
- A citation candidate must answer: "Which exact sentence does this support?"
- Do not insert a source because it is a target-journal exemplar unless it also supports a technical claim.
- Do not use generic AI/ML papers to support PCSP mechanics, connector behavior, or DCA calculation unless the claim is about the method itself.
- For target-journal style learning, separate `style exemplar` from `technical citation`.
- For InstSci results, separate `access evidence` from `claim support`. A retrieved or browser-verified paper still needs content inspection before it can support a manuscript sentence.
- For standards or codes, prefer official pages or provided standard documents; do not cite secondary summaries as if they were the standard.

## Failure Handling

If search or API access fails:

- report the tool/source, query, and error class briefly;
- fall back to local Zotero/PDF/library evidence when available;
- mark unsupported claims under `需补充或确认`;
- avoid silently replacing a missing high-relevance source with a weak adjacent paper.

## Final Reporting

When external tools materially influenced the draft, include a compact note:

- `外部来源记录：` source/tool, query/filter, reviewed count, selected sources, access status.
- `引用边界：` which sources are full-text checked and which are metadata-only.
- `未完成核查：` missing full text, paywalled sources, unverified DOI, missing standard, or weak support.
