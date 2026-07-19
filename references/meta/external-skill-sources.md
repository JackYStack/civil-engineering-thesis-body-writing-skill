# External Skill Sources and Migration Ledger

This ledger records public repositories consulted while developing `civil-thesis-body-writing`. It exists for provenance, maintenance, and scope control. The skill retains generalized workflows and constraints, not third-party manuscript facts, example data, credentials, binaries, or copied implementations.

## How to read this ledger

- `Migrated`: a generalized rule is materially present in this skill.
- `Integrated`: this skill defines how to cooperate with the external tool/skill, without absorbing its implementation.
- `Consulted only`: the source was installed or reviewed, but no clearly attributable core rule is claimed.
- The revision below is the repository snapshot checked on `2026-07-17`. For migrations completed earlier, it is a current provenance check, not necessarily the exact historical commit originally reviewed.
- Repository licenses govern upstream content. This project records concepts in original wording and does not redistribute upstream scripts unless separately documented.

## Source register

| Source | Status in this skill | Reviewed revision | License reported by GitHub | What was retained | What was not retained |
|---|---|---|---|---|---|
| [Gostyan/docx-skill-4-cn-paper](https://github.com/Gostyan/docx-skill-4-cn-paper) | Migrated | `e3b2f7edd2aa7c6d96c16e594035ebc906c2faf4` | MIT | DOCX `create / convert / revise` branching; formatting-contract discipline; headings, lists, three-line tables, captions, native equations, fields, tracked changes, and layered validation | Node/Python scripts, dependencies, examples, binaries, fixed font/margin defaults, and any claim of universal university compliance |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | Migrated and integrated | `9965debf24986c2c1cc422a6f4472a571e778bff` | Apache-2.0 | Router/reference architecture, task modes and output contracts, reader-question sequencing, terminology control, evidence-aware writing, on-demand loading, and a bounded `nature-figure` handoff for publication-figure execution | Nature branding, domain-specific claims, sample wording, copied plotting APIs/scripts/palettes, and any requirement to imitate Nature style for Chinese theses |
| [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) | Migrated | `d4529208cda72aa075767611b0265b95b709b550` | MIT | Motivation thread, evidence bank, claim register, writing-rationale matrix, rewrite matrix, and logic-transfer audit | Upstream orchestration/code, manuscript-specific examples, LaTeX project internals, and claims about bypassing AI detection |
| [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills) | Migrated | `0b42509800f49e6eb7809505d96e20a890ef99bd` | Apache-2.0 | Bounded tool output, source/query/access records, metadata-versus-full-text boundaries, credential protection, and failure-aware external-source use | Biomedical/database-specific skills, API clients, and domain conclusions unrelated to civil engineering writing |
| [Rimagination/instsci](https://github.com/Rimagination/instsci) | Integrated | `836cd6b65ad74136b7a1ff17672816a3b8b789aa` | MIT | Retrieval/access workflow, DOI batch handling, publisher access verification, target-journal exemplar acquisition, and InstSci-to-Zotero handoff boundaries | InstSci implementation, credentials/session data, and the false inference that retrieval success proves sentence-level citation support |
| [quzhiii/thesis-skills](https://github.com/quzhiii/thesis-skills) | Migrated and integrated | `bc625156ac5e4d3edd03136cf3862c9b76e164c6` | MIT | Deterministic readiness gates; rule-pack policy; format/content/language/compile dimensions; final cleanup, statistical consistency, manual-anchor and reference-scope audits; machine-readable report contracts; preview-first bounded fixes | Upstream scripts, institution rule packs, hard-coded school requirements, automatic risky fixes, HTML treated as source evidence, and LaTeX checks used as a prose-writing substitute |
| [zsyggg/paper-craft-skills](https://github.com/zsyggg/paper-craft-skills) | Consulted only | `3be47a2a53cc35a411c587bca5231a08de57287a` | No SPDX license reported | General awareness of paper-reading and presentation workflows | No clearly attributable core writing rule or upstream implementation is currently claimed in this skill |

## Internal destinations

| Source | Main internal destinations |
|---|---|
| `docx-skill-4-cn-paper` | [docx-creation-and-formatting.md](../workflows/docx-creation-and-formatting.md), [docx-ooxml-editing.md](../workflows/docx-ooxml-editing.md), `static/fragments/mode/docx-revision.md` |
| `nature-skills` | [task-mode-manifest.md](task-mode-manifest.md), [output-contracts.md](output-contracts.md), [reader-question-sequence.md](../architecture/reader-question-sequence.md), [terminology-ledger.md](../architecture/terminology-ledger.md), [nature-figure-cooperation.md](../workflows/nature-figure-cooperation.md) |
| `PaperSpine` | [motivation-thread-writing.md](../architecture/motivation-thread-writing.md), [evidence-bank-and-claim-register.md](../architecture/evidence-bank-and-claim-register.md), [writing-rationale-matrix.md](../architecture/writing-rationale-matrix.md) |
| `science-skills` | [external-source-and-tool-use.md](../workflows/external-source-and-tool-use.md), [citation-workflow.md](../workflows/citation-workflow.md) |
| `InstSci` | [instsci-paper-retrieval-workflow.md](../workflows/instsci-paper-retrieval-workflow.md), [instsci-to-zotero-import-workflow.md](../workflows/instsci-to-zotero-import-workflow.md) |
| `thesis-skills` | [thesis-skills-audit-workflow.md](../workflows/thesis-skills-audit-workflow.md), [thesis-format-audit.md](../workflows/thesis-format-audit.md) |

## Maintenance rule

When another external skill materially changes this skill:

1. record repository owner/name, direct URL, reviewed branch/commit, review date, and detected license;
2. state the exact generalized ideas retained;
3. state code, defaults, examples, data, or claims deliberately not retained;
4. link the internal destination files;
5. update [update-log.md](update-log.md) and run the full validation suite.

If a source is merely installed, mentioned, or experimentally tested, label it `Consulted only` instead of implying migration.
