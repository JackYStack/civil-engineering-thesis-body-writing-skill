# Nature-Figure Cooperation Workflow

Use this workflow when a civil-engineering thesis or paper needs a figure plan, a revision of an existing figure, or an actual publication figure. The two skills cooperate through a bounded handoff: `civil-thesis-body-writing` defines what the figure must prove; `nature-figure` decides how to plot, render, export, and visually validate it.

## Responsibility boundary

| Responsibility | Owner |
|---|---|
| Manuscript claim, section role, evidence hierarchy, terminology, variable meaning, units, panel questions, caption context, target-journal boundary | `civil-thesis-body-writing` |
| Python/R backend gate, plotting code, layout, rendering, export, visual/statistical QA, backend-specific blockers | `nature-figure` |
| Colour-role proposal | Civil skill may propose it; `nature-figure` must validate it in the final rendering |
| Results paragraph, figure callout, caption reintegration, claim-strength audit | `civil-thesis-body-writing` after artifacts return |

Do not copy `nature-figure` plotting APIs or backend rules into this skill. Load and follow that skill at execution time so its current contract remains authoritative.

## Figure brief

Before invoking a plotting backend, create the following manuscript-facing brief:

```text
Core conclusion:
Manuscript section and figure role:
Target journal/output:
Available data and source files:
Evidence hierarchy:
  hero evidence:
  validation evidence:
  controls/robustness:
Variable ledger:
  variable -> meaning -> unit -> type -> order/reference:
Provisional panel map:
  a:
  b:
  c:
Colour/marker ledger:
Statistics and uncertainty needed:
Caption facts and terminology:
Reviewer risk:
Missing evidence or author decisions:
```

The brief must not invent a panel, trend, statistic, specimen, or model result. If the user provides a topic but no data, produce a provisional plan and a missing-data list instead of mock scientific results.

## Handoff gate

Hand off to `nature-figure` only after the following are known or explicitly marked unresolved:

1. The one-sentence conclusion and manuscript role.
2. The data/source files or the exact reason they are unavailable.
3. Variable semantics, units, category order, control/reference, and uncertainty definition.
4. The minimum panel set and evidence priority.
5. Target output: planning only, code, preview, vector master, raster export, or complete bundle.
6. Target journal/template when journal-specific dimensions or formats are claimed.

For actual plotting, load `nature-figure`. Its backend gate is blocking: use an explicit user choice, a clearly language-specific workflow, or its saved Python/R preference. If it has no saved preference, let `nature-figure` ask its required one-line backend question. Do not answer that question on the user's behalf merely because one language is installed.

## Backend ownership

- All plotting, previews, exports, and visual QA belong to the single backend selected by `nature-figure`.
- The civil-writing route may inspect data or prepare a non-visual mapping table, but it must not render a substitute figure with another backend.
- If the selected runtime or plotting package is unavailable, return the exact blocker. A selected-backend script or installation command may be supplied, but a cross-backend fallback is not permitted.
- AI-generated schematics or graphical abstracts must follow the explicit AI-schematic route in `nature-figure`; quantitative panels must remain data-driven.
- Do not create mock data unless the user explicitly requests a labelled demonstration unrelated to manuscript evidence.

## Colour coordination

Use [scientific-figure-color.md](../style/scientific-figure-color.md) to propose semantic mappings for specimens, materials, methods, parameter levels, and signed effects. Treat that proposal as input to the figure contract, not as final visual approval.

Priority order:

1. Target-journal or institution requirements.
2. Scientific semantics, integrity, statistics, and accessibility.
3. The active `nature-figure` figure/QA contract.
4. The civil skill's representative palette register.
5. Aesthetic preference.

## Artifact return

When execution completes, expect only the artifacts actually requested and generated. Record their paths or status:

```text
Figure source/code:
Source-data mapping:
Editable vector output:
Raster/preview output:
Final dimensions:
Backend used:
Statistics/legend notes:
QA report:
Known blockers:
```

Do not report SVG/PDF/TIFF/PNG outputs, editable text, final dimensions, or QA as complete unless the files were generated and inspected. Planning-only tasks should explicitly say `not generated` for artifact fields.

## Manuscript reintegration

After the figure artifacts return to the civil-writing route:

1. Verify that panel labels, variables, symbols, units, specimen names, model names, and colours match the terminology ledger and manuscript.
2. Draft or revise the caption using only visible panels and confirmed statistical details.
3. Update the in-text figure callout and results paragraph in the order `claim -> figure evidence -> quantified comparison -> mechanism/boundary`.
4. Keep observation in Results and interpretation in Discussion when the manuscript separates them.
5. Check that the figure does not visually imply a stronger conclusion than the text or data support.
6. For DOCX/LaTeX insertion, preserve caption numbering, cross-references, resolution, aspect ratio, and the original manuscript file.

## Failure boundaries

- `nature-figure` missing: complete the figure brief, state the missing dependency, and stop before claiming execution.
- Data missing or ambiguous: provide a panel/data requirement table; do not fabricate values.
- Backend preference unresolved: allow the `nature-figure` backend gate to ask once and wait.
- Runtime/package missing: report the exact selected-backend blocker; do not switch languages.
- Target-journal requirements unavailable: use a generic publication contract but label dimensions/formats as provisional.
- Existing figure has only a raster image and no data/code: visual audit and redesign advice are possible; numerical reconstruction is not assumed.
- Caption statistics or sample size unavailable: retain placeholders or flag them; do not infer them from appearance.

## Delivery sequence

1. `Figure brief`
2. `Handoff status`
3. `Figure artifacts`
4. `Figure QA`
5. `Manuscript reintegration`
6. `Unresolved evidence or blockers`
