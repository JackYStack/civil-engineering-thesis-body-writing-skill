# Terminology Ledger

Use this guide before drafting, translating, polishing, or editing a `.docx` when terminology can drift across sections, languages, formulas, figures, tables, or captions.

The ledger prevents the manuscript from using several names for one concept, or one name for several concepts.

## When to Build One

Build or refresh a terminology ledger when:

- the task covers more than one subsection;
- the manuscript is bilingual or being translated;
- symbols such as `DCA_s`, `DCA_c`, `R2`, `RMSE`, `MAE`, or formula variables appear;
- the text mixes thesis language, journal language, GUI labels, code variable names, and figure/table captions;
- the user asks for formal Word/docx revision, target-journal polish, or thesis-to-paper conversion.

For a short local polish, silently preserve existing terms unless a term is clearly wrong.

## Required Ledger

| Concept | Canonical Term | Allowed Variants | Forbidden Variants | First-Use Definition | Scope/Note |
|---|---|---|---|---|---|

Column rules:

- `Concept`: the underlying idea, not only the word.
- `Canonical Term`: the term to use in final prose.
- `Allowed Variants`: abbreviations, plural forms, or figure/table labels that are acceptable.
- `Forbidden Variants`: terms that would blur meaning or imply a stronger claim.
- `First-Use Definition`: how the term should be introduced.
- `Scope/Note`: formula symbol, unit, parameter range, or language-specific boundary.

## Civil-Engineering Examples

| Concept | Canonical Term | Allowed Variants | Forbidden Variants | First-Use Definition | Scope/Note |
|---|---|---|---|---|---|
| Precast concrete sandwich panel | precast concrete sandwich panel (PCSP) | PCSPs after first use | sandwich wall without context | Use full term at first mention, then PCSPs. | Keep singular/plural consistent. |
| Inner/outer wythe | inner concrete wythe / outer concrete wythe | inner wythe, outer wythe after first use | inner slab, outer slab if the manuscript uses wythe | Define as the two concrete layers separated by insulation. | Keep `wythe` in English paper drafts. |
| Degree of composite action | degree of composite action (DCA) | DCA after first use | composite rate, cooperation degree | Define as the index describing interaction between wythes. | Do not let DCA replace direct strength/serviceability checks. |
| Stiffness DCA | stiffness degree of composite action (`DCA_s`) | `DCA_s` | stiffness composite degree, DCAs | Define with the corresponding stiffness formula or indicator. | Distinguish from capacity DCA. |
| Capacity DCA | capacity degree of composite action (`DCA_c`) | `DCA_c` | strength DCA unless defined | Define with ultimate capacity or moment basis. | Distinguish from `DCA_s`. |
| Connector property | initial connector stiffness | connector initial stiffness | connector rigidity when stiffness is meant | Define unit and test/source if available. | Usually affects service stiffness/DCA_s. |
| Connector strength | connector capacity | ultimate connector capacity | connector stiffness | Define unit and failure basis if available. | Usually affects ultimate response/DCA_c. |

## Ledger-Based Revision Rules

- Use canonical terms in prose, captions, tables, and output reports.
- Preserve the user's formula symbols unless they are inconsistent; then flag the change.
- If two terms may both be valid, do not silently choose one for formal work. Record the decision in the ledger and list it under `needs confirmation` if evidence is missing.
- In Word/OOXML edits, count old and new terminology in sampled text after replacement.
- For English manuscripts, avoid upgrading a cautious Chinese term into a stronger English term. For example, translate `辅助设计` as `assisted design` or `preliminary design support`, not `code-compliant design`.

## Output Add-On

For formal tasks, include a compact `terminology ledger` or save it as a Markdown artifact before large `.docx` edits. For short tasks, mention only terminology changes that materially affect meaning.
