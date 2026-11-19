# Core Workflow

1. Select one primary task mode from `manifest.yaml` and `references/meta/task-mode-manifest.md`.
2. Load only the fragments matching the task axes: mode, section, source, and operation.
3. Use `references/index.md` to open deeper guides only when the task requires them.
   - Methods/results, statistical claims or evidence audits: `references/workflows/research-integrity-and-reproducibility.md`.
   - Equations, quantitative plots/tables, captions or derived claims: `references/workflows/equation-figure-table-integrity.md`.
   - Shared results changing, cross-section work, final delivery or reviewer packages: `references/workflows/manuscript-consistency-and-delivery.md`.
4. Build evidence, terminology, and reader-question checks before major drafting or Word edits.
5. For major argument or section revisions, load `references/architecture/evidence-led-narrative-and-defensive-writing.md`; state the strongest supported contribution and each experiment's role, without suppressing evidence or conditions material to interpretation.
6. Draft, revise, audit, or edit according to the selected output contract.
7. Before returning thesis body prose, remove meta-discourse that explains what adjacent chapters “solve,” why their tasks differ, or why content is not repeated; preserve only direct technical cross-references.
8. Remove generic applicability warnings and gratuitous self-defense, not necessary technical disclosure. For language cleanup, use `references/style/academic-prose-cleanup.md`, choose edit intensity, and compare protected values, terms, citations, and their semantic mappings before delivery.
9. For a DOCX edit confined to one section, visually inspect only the pages occupied by that section and validate unaffected content structurally.
10. Validate generated artifacts with the applicable scientific/numeric, object and render checks, reporting each layer separately. The scripts in `manifest.yaml` primarily validate this skill's packaging/contracts, not a manuscript's truth or layout. Run them for skill maintenance; use the bounded numeric helper only for its declared CSV checks.

For reviewer-driven work, apply `references/workflows/reviewer-driven-revision.md` before the body-prose filtering steps. Those steps do not remove technically necessary assumptions or qualifications. Work on the active comment, retain deferred items, and distinguish proposed wording from edits actually made.
