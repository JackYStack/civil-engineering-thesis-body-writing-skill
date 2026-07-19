# InstSci to Zotero MCP Import Workflow

Use this workflow when `civil-thesis-body-writing` needs to organize papers obtained by InstSci and import them into Zotero through Zotero MCP/API.

This workflow is for literature-library management and traceability. Importing a paper into Zotero does not mean the paper supports a manuscript claim. After import, use [citation-workflow.md](citation-workflow.md) and, when needed, [zotero-fulltext-corpus-workflow.md](zotero-fulltext-corpus-workflow.md) for claim-level support checks.

If imported PDFs will be converted, OCRed, or read through Zotero full text, also run [pdf-extraction-and-fulltext-qc.md](pdf-extraction-and-fulltext-qc.md). Keep imported PDFs tagged `待核全文` until extraction quality and claim-level support are checked.

## When to Use

Use this workflow when the user asks to:

- import InstSci-downloaded papers into Zotero;
- attach InstSci PDFs to Zotero items;
- convert an InstSci `manifest.csv`/`manifest.json` into a Zotero import plan;
- deduplicate InstSci results against Zotero by DOI or title;
- add InstSci access-status tags or child notes in Zotero;
- create a Zotero collection for target-journal exemplars or citation candidates found through InstSci.

Do not use this workflow for:

- ordinary writing without Zotero library changes;
- inserting citations before reading the imported paper;
- importing PDFs with unclear provenance without marking them `unverified PDF`;
- bypassing publisher, institution, or Zotero access controls.

## Safety and Confirmation

Zotero writes modify the user's live library. Before calling Zotero MCP write tools or Zotero Web API:

1. Build an import preview table.
2. Mark duplicates, missing DOI, missing PDF, uncertain metadata, and unverified access status.
3. Ask for user confirmation before creating items, importing attachments, writing tags, adding collections, or creating notes.
4. Never print Zotero API keys, cookies, institution credentials, or private config values.

Allowed read-only steps before confirmation:

- inspect InstSci manifests and output folders;
- search Zotero for duplicates;
- build an import plan;
- create a local RIS/BibTeX/CSV preview file.

Write steps requiring confirmation:

- create Zotero items;
- import PDF attachments;
- add tags;
- create child notes;
- add items to collections;
- update metadata on existing items.

## Input Inventory

Before importing, locate or ask for:

| Input | Required? | Notes |
|---|---|---|
| InstSci output directory | Yes | Contains manifests, PDFs, logs, or run reports. |
| Manifest file | Preferred | `manifest.csv`, `manifest.json`, or source record table. |
| PDF folder | Preferred | Needed for attachment import. |
| Target Zotero collection | Optional | Existing collection key or requested collection name. |
| Import mode | Optional | `preview only`, `create missing`, `attach PDFs only`, `update tags/notes`, or `full import`. |

If no manifest exists, build a local import inventory from PDF filenames, DOI lists, InstSci run reports, and metadata files.

## Import Status Labels

Preserve InstSci access status as Zotero tags or child-note fields:

- `InstSci`
- `open access retrieved`
- `browser verified`
- `HTTP preflight`
- `auth_required`
- `blocked`
- `unverified PDF`
- `missing`
- `待核全文`

Use `待核全文` when the paper has not yet been inspected for claim-level writing support.

## Deduplication Rules

Use a conservative duplicate policy:

1. Match DOI exactly after normalizing case, URL prefixes, and whitespace.
2. If DOI is missing, match title after lowercasing and removing punctuation/extra spaces.
3. Treat near-title matches as `needs user confirmation`, not automatic duplicates.
4. If an existing Zotero item has no PDF and the InstSci PDF is verified, attach the PDF to the existing item rather than creating a duplicate item.
5. If an existing item already has a PDF, do not replace it unless the user explicitly asks.

Recommended duplicate table:

| Import ID | DOI/Title | Zotero Match | Decision | Reason |
|---|---|---|---|---|
| I1 | ... | itemKey / none / uncertain | create / attach / skip / confirm | DOI match, title match, missing DOI, etc. |

## Zotero MCP Action Map

Use available Zotero MCP tools when present:

| Task | Zotero MCP action |
|---|---|
| Search duplicates | `search_library` by DOI/title, include attachments when needed |
| Inspect an existing item | `get_item_details` |
| Create missing item | `write_item` with `action: create` |
| Import PDF as attachment | `write_item` with `action: import`, `parentItemKey`, and absolute `filePath` |
| Add tags | `write_tag` with `action: add` |
| Create access-record note | `write_note` with `action: create`, attached to parent item |
| Add item to collection | `add_items_to_collection` |
| Read imported full text later | `get_content` or Zotero full-text workflow |

If Zotero MCP write tools are unavailable, generate a RIS/BibTeX/CSV import package and a PDF attachment plan instead of writing directly.

## Child Note Template

Create a child note only after the import is confirmed.

```md
## InstSci 获取记录

- DOI:
- Title:
- Publisher:
- InstSci route:
- Institution:
- Access status:
- PDF path:
- Imported by:
- Import date:

## 写作与引用边界

- Writing use: background / gap / method / comparison / target-journal exemplar / not used
- Full-text inspected: yes / no
- Claim-level support: not checked / candidate / weak / strong
- Next action:
```

## Workflow

1. Open [external-source-and-tool-use.md](external-source-and-tool-use.md) if external tools or API outputs are involved.
2. Read InstSci manifest, run report, and PDF folder into a bounded import inventory.
3. Normalize DOI, title, year, publisher, PDF path, and InstSci access status.
4. Search Zotero by DOI and title to find duplicates or existing attachment gaps.
5. Build an import preview table with one proposed action per paper.
6. Ask the user to confirm the preview before any Zotero write.
7. After confirmation, create missing Zotero items, import PDF attachments, add tags, create access-record notes, and add items to collection as requested.
8. Verify imported items by reading item details or searching the target collection.
9. Save a local import report under `analysis/` when the batch is nontrivial.
10. Mark papers `待核全文` until the full text has been read for citation support.

## Preview Table

Use this before writing to Zotero:

| Import ID | DOI | Title | Year | PDF Path | InstSci Status | Zotero Match | Proposed Action | Needs Confirmation |
|---|---|---|---:|---|---|---|---|---|
| I1 | ... | ... | 2024 | ... | `open access retrieved` | none | create item + attach PDF + tags + note | no |
| I2 | ... | ... | 2023 | ... | `unverified PDF` | itemKey | attach PDF? | yes |

## Final Report

After confirmed import, report:

- `导入概况`: created items, attached PDFs, skipped duplicates, uncertain items, failed writes.
- `Zotero条目清单`: item key, title, DOI, tags, attachment status, collection.
- `访问状态`: InstSci status and whether full text has been inspected.
- `后续写作动作`: which items need full-text reading, citation support grading, or manual metadata cleanup.
