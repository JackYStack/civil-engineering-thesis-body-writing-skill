# Router Compression Map

This file records how the former long `SKILL.md` body was mapped into the router-compatible architecture. It is a maintenance aid for auditing the compressed root `SKILL.md`.

## Compression Goal

Convert `SKILL.md` from a large all-in-one instruction file into a concise router:

- keep trigger metadata and essential guardrails in `SKILL.md`;
- move reusable operating rules into `static/core/`;
- move mode, section, source, and operation details into `static/fragments/`;
- keep heavy workflows and examples in `references/`;
- enforce coverage through scripts rather than by repeating text.

## Section Mapping

| Current long-entry section | Destination after compression | Notes |
|---|---|---|
| Core Stance | `static/core/stance.md`; router `Core Rules` | Keep only non-negotiable rules in router. |
| When to Ask Before Writing | router `Ask Before Acting`; `static/core/workflow.md` | Router keeps the blocking-question test. |
| Collaboration and Chunking Strategy | `static/core/workflow.md`; `references/examples/use-case-templates.md` | Detailed examples stay outside the entry file. |
| Intake Checklist | `static/core/workflow.md`; mode/section fragments | Router only asks agents to detect axes. |
| Writing Workflow | `static/core/workflow.md`; `manifest.yaml`; architecture/workflow references | Long numbered procedure is replaced by manifest routing. |
| Chapter-Type Defaults | `references/index.md`; `static/fragments/section/` | Section-specific routing belongs in fragments. |
| Common Chapter Logic | `references/sections/chapter-templates.md`; section fragments | Keep chapter templates outside router. |
| Citation Trigger Rules | `references/workflows/citation-workflow.md`; router source rules | Router keeps local-first and metadata/full-text boundary. |
| Paragraph Patterns | `references/style/local-thesis-style.md`; `references/style/local-paper-style.md` | Router should not carry reusable sentence templates. |
| Output Format | `static/core/output-format.md`; `references/meta/output-contracts.md` | Router points to mode-specific contracts. |
| Local Evidence Used to Shape This Skill | `references/meta/update-log.md`; style files | Keep provenance summarized, no concrete paper references. |

## Coverage Requirements

The compressed root `SKILL.md` must mention:

- `manifest.yaml`;
- all `always_load` core files;
- task mode selection and output contracts;
- local-first citation support;
- no invention of data, references, or conclusions;
- user's own results before external literature;
- Zotero, InstSci, PDF/OCR, and external-search boundaries;
- `.docx` and OOXML safety;
- anti-vague language QC;
- validation through `scripts/validate_all.py`.

## Replacement Plan

1. Maintain root `SKILL.md` as a concise router.
2. Keep detailed rules in `static/core`, `static/fragments`, and `references`.
3. Run `scripts/validate_router_entry.py` and `scripts/validate_all.py` after router edits.
4. Keep rollback available through git.
