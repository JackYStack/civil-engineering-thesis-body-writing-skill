# External Skill Sources and Migration Ledger

This ledger records public repositories consulted while developing `civil-thesis-body-writing`. It exists for provenance, maintenance, and scope control. The skill retains generalized workflows and constraints, not third-party manuscript facts, example data, credentials, binaries, or copied implementations.

## How to read this ledger

- `Migrated`: a generalized rule is materially present in this skill.
- `Integrated`: this skill defines how to cooperate with the external tool/skill, without absorbing its implementation.
- `Consulted only`: the source was installed or reviewed, but no clearly attributable core rule is claimed.
- Unless a row gives another review date, its revision was checked on `2026-07-17`. Later entries record their own review date. A provenance recheck is not necessarily the historical commit first migrated.
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
| [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) | Migrated | `102c8b21acf5eda3a0aef3d9779a65db646c8980` (main, reviewed 2026-09-20) | MIT | Strongest-supported-contribution narrative, explicit advantage, experiment roles, removal of irrelevant rhetorical self-defense, and rebuilding weak storylines while retaining material adverse evidence | Blanket exclusion of negative findings or necessary conditions; upstream slogans, data alteration, invented superiority, or silent baseline changes |
| [matsuikentaro1/humanizer_academic](https://github.com/matsuikentaro1/humanizer_academic) | Migrated (generalized principles) | `f68b0b070d705fb7250b87c95b38c450678b2386` (main, reviewed 2026-11-18) | MIT (repository LICENSE) | Reader clarity before compression; explicit actors/comparators/conditions; substantive short claims and legitimate transitions; methods-results correspondence | Medical facts/examples, author's personal rhythm/connective profile, compulsory burstiness, upstream scripts and detector claims |
| [AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) | Migrated (generalized principles) | `94b88b23703bed7df507acae7d6d5876209a0cdf` (main, reviewed 2026-11-18) | MIT (repository LICENSE) | Claim-evidence strength calibration, supplied author-style matching, academic rather than casual voice, audit-revise-check sequence | NSF/NIH-specific proposal expansion, absolute punctuation bans, example data, code or empirical success claims |
| [junbolian/Academic-Humanizer](https://github.com/junbolian/Academic-Humanizer) | Migrated (generalized principles) | `62b0a02627e063015466c70f0a4dd4929a9f7f5b` (main, reviewed 2026-11-18) | MIT (repository LICENSE) | Cleanup/polish/draft intensity within existing operations; located edit reasons; invented contrasts/undefined labels; invariant and qualifier comparison | Upstream checker implementation, deletion of thesis chapter summaries, automatic removal of engineering details, mandatory manuscript placeholders or added theorems |
| [taehyeonglim/academic-humanizer](https://github.com/taehyeonglim/academic-humanizer) | Migrated (generalized principles) | `801c2bd5ecb3b70f5404a154d71b2c92201da29e` (main, reviewed 2026-11-18) | MIT (repository LICENSE) | Register protection; preservation of genuine epistemic hedges, method passive, technical vocabulary, statistics/citations and range punctuation | Vendoring/setup, upstream code, fixed 25%/50% change-rate gates, zero-dash requirement and self-grades |

## Internal destinations

### Systematic source re-review — 2026-11-19

The earlier rows retain their historical revisions. A new pinned review uses Nature Skills `14ca69710cae192325395a380e9cdd4ae5d9d0c8` and PaperSpine `5c332ba8eaac811aa37d439c068993f67bf372a6`; see [systematic-integration-map.md](systematic-integration-map.md) for exact review depth, file/blob locators, adopted constraints, rejected assumptions and optional dependencies. The review covers all 24 Nature entrypoints for routing scope and selected relevant deep references, not all upstream implementations. It adds self-contained research, equation/display and cross-file delivery rules; no upstream implementation is vendored. Local specialty snapshots are fingerprinted separately and are not mislabeled as freshly reviewed upstream revisions.

| Source | Main internal destinations |
|---|---|
| `docx-skill-4-cn-paper` | [docx-creation-and-formatting.md](../workflows/docx-creation-and-formatting.md), [docx-ooxml-editing.md](../workflows/docx-ooxml-editing.md), `static/fragments/mode/docx-revision.md` |
| `nature-skills` | [task-mode-manifest.md](task-mode-manifest.md), [output-contracts.md](output-contracts.md), [reader-question-sequence.md](../architecture/reader-question-sequence.md), [terminology-ledger.md](../architecture/terminology-ledger.md), [nature-figure-cooperation.md](../workflows/nature-figure-cooperation.md) |
| `PaperSpine` | [motivation-thread-writing.md](../architecture/motivation-thread-writing.md), [evidence-bank-and-claim-register.md](../architecture/evidence-bank-and-claim-register.md), [writing-rationale-matrix.md](../architecture/writing-rationale-matrix.md) |
| `science-skills` | [external-source-and-tool-use.md](../workflows/external-source-and-tool-use.md), [citation-workflow.md](../workflows/citation-workflow.md) |
| `InstSci` | [instsci-paper-retrieval-workflow.md](../workflows/instsci-paper-retrieval-workflow.md), [instsci-to-zotero-import-workflow.md](../workflows/instsci-to-zotero-import-workflow.md) |
| `thesis-skills` | [thesis-skills-audit-workflow.md](../workflows/thesis-skills-audit-workflow.md), [thesis-format-audit.md](../workflows/thesis-format-audit.md) |
| `anti-defensive-writing-Skill` | [evidence-led-narrative-and-defensive-writing.md](../architecture/evidence-led-narrative-and-defensive-writing.md), `static/core/workflow.md`, `static/fragments/mode/paper-sci.md`, `SKILL.md` |
| Four academic humanizer repositories above | [academic-prose-cleanup.md](../style/academic-prose-cleanup.md), `SKILL.md`, `static/core/stance.md`, `static/core/workflow.md`, `static/fragments/operation/revise.md`, and cleanup/disclosure pressure scenarios |

### Academic prose integration scope — 2026-11-18

Reviewed each repository's `SKILL.md`; additionally reviewed Matsui's `references/reader-clarity.md` and Lim's `rules/academic-overrides.md`. Main-branch revisions were resolved with `git ls-remote`; licenses were read from repository `LICENSE` files. This migration is an original synthesis of editorial principles, not redistribution of upstream prose, examples or scripts. No four standalone skills were installed, no upstream setup script ran, and no upstream checker result is claimed. Clarified the existing anti-defensive route to preserve material contrary evidence and scientifically necessary conditions, while retaining the author's preference against generic self-critical paragraphs. Historical update entries describe their original behavior, not the current precedence rule.

## Local source migrations

### Nature-reader local rule migration — 2026-11-19

Reviewed local `nature-reader` manifest 2.0.0 and its `static/core/principles.md`, `static/core/workflow.md`, `references/grounding-rules.md`, and `references/output-spec.md`. This records a local installed snapshot, not a new upstream commit review. Upstream project: [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills), whose previously reviewed license is recorded above.

Retained in [literature-translation-grounding.md](../workflows/literature-translation-grounding.md): traceable source locations and coverage, faithful translation separate from explanation, figure/table context, genuine uncertainty, and missing/unclear content labels. Adapted the scope for discussion-time excerpts, not only file-producing tasks. No upstream code, manuscript material, full-reader default, forced cropping, or shared-package dependency was copied. Full-paper reader cooperation remains optional and capability-gated.

Local file SHA256 fingerprints:

- `static/core/principles.md`: `0275152b564c7241c4b1180a48390ca4efdf21a5e2e42ff52e8c7e10a99350b4`
- `static/core/workflow.md`: `6ee5b665a7cb96e1c9a4987607389d25a9aa712417d598550dbccf8de554ccfd`
- `references/grounding-rules.md`: `9042ef5c948767bb74a8eb148c472ea31d37953e216c60d5ee572344950b5a9b`

The earlier generic mention of a nature-reader-style reading route was not equivalent to this explicit translation-grounding migration.

## Maintenance procedure

When another external skill materially changes this skill:

1. record repository owner/name, direct URL, reviewed branch/commit, review date, and detected license;
2. state the exact generalized ideas retained;
3. state code, defaults, examples, data, or claims deliberately not retained;
4. link the internal destination files;
5. update [update-log.md](update-log.md) and run the full validation suite.

If a source is merely installed, mentioned, or experimentally tested, label it `Consulted only` instead of implying migration.

## Local reviewer-response integration — 2026-10-16

Consulted the locally maintained `nature-response` 1.1.0 (`SKILL.md`, `references/revision-evidence.md`, and `references/model-assumptions.md`), updated through the author's revision workflow. This is a local integration record, not a claim about a newly reviewed upstream commit. Retained: minimal changed excerpts, current-file authority, accurate locations, and the distinction between sampling constraints, model assumptions, and physical checks. Destination: `references/workflows/reviewer-driven-revision.md`. Reply-package assembly remains with `nature-response` when available; no scripts, manuscript facts, citation numbers, private paths, or journal-specific template requirements were copied.
