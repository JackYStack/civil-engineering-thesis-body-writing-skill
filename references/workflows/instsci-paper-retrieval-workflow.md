# InstSci Paper Retrieval Workflow

Use this workflow when `civil-thesis-body-writing` needs InstSci for paper retrieval, DOI batch downloads, publisher PDF access, closed-access verification, target-journal exemplar acquisition, or source availability checks.

InstSci is a retrieval and access-evidence tool. It can help obtain or verify full text, but it does not by itself prove that a manuscript sentence is supported. After a paper is obtained, use [citation-workflow.md](citation-workflow.md) for claim-level citation support.

If retrieved papers need to be added to Zotero, use [instsci-to-zotero-import-workflow.md](instsci-to-zotero-import-workflow.md) after retrieval. Keep `access evidence`, `Zotero library status`, and `claim support` as separate records.

When a retrieved PDF or publisher HTML is later read for thesis/paper evidence, run [pdf-extraction-and-fulltext-qc.md](pdf-extraction-and-fulltext-qc.md) before writing claims. Retrieval success is not extraction quality and not citation support.

## When to Use

Use InstSci when the task involves:

- DOI or URL based paper fetching;
- open-access full-text discovery before writing or citation work;
- target-journal exemplar collection for style comparison;
- publisher PDF retrieval or closed-access availability verification;
- DOI batch recovery for a reference list;
- checking whether a PDF exists, is verified, missing, blocked, or requires authentication.

Do not use InstSci for:

- ordinary paragraph polishing when all evidence is already provided;
- bypassing publisher or institution access controls;
- claiming a paper supports a sentence without reading the obtained full text;
- final publisher capability verdicts based only on HTTP requests.

## Required Safety Boundary

- Never ask the user to paste passwords, OTPs, cookies, API keys, or institutional credentials into chat.
- SSO, 2FA, CAPTCHA, and institution verification must be completed by the user in the visible CloakBrowser window.
- Do not write API keys, cookies, institutional secrets, screenshots with sensitive fields, or entitlement details into reports, skill files, logs, or commits.
- Do not default to any specific institution. Use the user-provided institution, configured InstSci institution, or ask only at the point of access.

## Evidence Status Labels

Use these labels when reporting retrieved papers:

| Status | Meaning | Writing/Citation Use |
|---|---|---|
| `open access retrieved` | PDF/full text was obtained from OA source or publisher OA route | Candidate for full-text citation check |
| `browser verified` | PDF captured or blocker verified in visible CloakBrowser with visual checkpoints | Valid final access verdict; still inspect full text for claim support |
| `HTTP preflight` | DOI resolution, route construction, metadata, or direct HTTP check only | Discovery/precheck only; not final access verdict |
| `auth_required` | user must complete SSO, 2FA, CAPTCHA, or institution selection | Pause retrieval; do not claim support |
| `blocked` | visible browser evidence shows challenge/error/publisher blocker | Report blocker and next action |
| `unverified PDF` | file exists but DOI/text verification is insufficient | Use cautiously; inspect manually before citation |
| `missing` | no PDF/full text captured | Do not cite beyond metadata/abstract |

## Recommended CLI Commands

Run lightweight checks first:

```powershell
instsci --help
instsci identity-policy
instsci search "keyword query" --limit 10
instsci fetch "10.xxxx/example"
```

For DOI batches:

```powershell
instsci papers dois.txt --publisher auto --institution "Institution Name" --output .\runs\papers
```

For known publisher batches:

```powershell
instsci publisher-batch dois.txt --publisher elsevier --institution "Institution Name" --output .\runs\elsevier
```

For Elsevier API setup, guide the user to configure it locally:

```powershell
instsci elsevier-setup --api-key YOUR_ELSEVIER_KEY --validate
```

Do not ask the user to paste the key into chat.

## Workflow for Writing Tasks

1. Identify the writing purpose: citation support, literature review, target-journal exemplar, or missing full-text recovery.
2. Build a DOI/title list from Zotero, the manuscript reference list, user-provided references, or web metadata.
3. Run InstSci retrieval only for sources that need full text or access verification.
4. Record retrieval status, output path, DOI, publisher, route attempted, and access boundary.
5. If the user wants Zotero library import, switch to [instsci-to-zotero-import-workflow.md](instsci-to-zotero-import-workflow.md) and preview Zotero writes before modifying the library.
6. If a PDF is retrieved, inspect the text with Zotero, local extraction, nature-reader, or other full-text reading workflow.
7. Insert citations only after sentence-level support is confirmed.

## Source Record Table

Use this table in reports when InstSci is used:

| ID | DOI/Title | Publisher | Route Attempted | Institution | Result | Evidence/Path | Writing Use | Next Action |
|---|---|---|---|---|---|---|---|---|
| I1 | ... | Elsevier | `papers --publisher auto` | user-selected | `browser verified` | `runs/.../pdfs/...pdf` | full-text candidate | inspect full text |

## Target-Journal Exemplar Use

For target-journal polish:

- Use InstSci to obtain comparable papers only from open access, user-authorized access, or visible institutional browser workflow.
- Mark each exemplar as `full text`, `metadata only`, `abstract only`, `browser verified`, or `missing`.
- Separate `style exemplar` from `technical citation`; a retrieved exemplar should not enter the manuscript bibliography unless it supports a concrete claim.

## Reporting

When InstSci materially affects the writing task, include:

- `InstSci检索/获取记录`: DOI/title, publisher, route, institution, result, evidence path.
- `全文核查状态`: full text inspected, abstract only, metadata only, unverified PDF, missing.
- `写作用途`: background, gap, method, comparison, boundary, target-journal style, or not used.
- `需用户动作`: institution selection, SSO, CAPTCHA, Elsevier API setup, missing DOI, or manual PDF check.
