# Equation, figure and table integrity

Load automatically when drafting, explaining, generating or auditing formulas, quantitative displays, captions, or claims derived from them. The user need not name a specialist skill. Apply only relevant checks: preserving an unchanged equation during language editing does not require a new derivation or experiment.

Scientific validity, numeric agreement, editable-object structure and visual appearance are separate checks. No one layer certifies the others. Reuse evidence/terminology records and the controlling template, not a parallel ledger.

## Shared object contract

For formal object work identify:

| Field | Minimum meaning |
|---|---|
| Identity | Stable object/claim ID, current figure/table/equation number, manuscript version |
| Source | Actual file/version and page, sheet/range, row/column, run or source-code locator |
| Semantics | Object/condition, variable definitions, units, aggregation and uncertainty where relevant |
| Transformation | Formula, conversion, filtering, normalization, interpolation, rounding or image processing actually used |
| Output | Requested format, target specification, generated file/object or planning-only status |
| Verification | What was checked, how, evidence/result and unresolved questions |

Create the smallest useful record. A shared-source revision should update dependent objects and prose, not just the visible caption. Disputed source values remain disputed until resolved.

## Equations: source, meaning and validity

1. Classify the expression as source transcription, standard provision, author derivation, empirical fit or illustration. Record actual provenance. An unexplained coefficient is not an established code factor.
2. Preserve source symbols, operators, signs, subscripts, superscripts and conditions. Define variables and units; distinguish definition, approximation, inequality, regression and equilibrium/compatibility equations. Do not silently repair a cited equation.
3. For a new/changed/calculated formula, check as applicable: dimensional consistency, algebra under stated assumptions, domain/denominator, limiting cases, numerical substitution, sign and order of magnitude. Use available symbolic/unit tools rather than unverified hand algebra for fragile transformations; record assumptions and actual execution.
4. For engineering interpretation also check loading convention, unit system, geometry/support assumptions, elastic/ultimate regime, reference state, parameter applicability and standard edition. Same dimensions do not mean the same quantity: stiffness K versus EI, strength versus stress, total versus per-point load, and stiffness/capacity DCA need distinct definitions.
5. Symbolic equivalence or correct dimensions do not prove a mechanical model, empirical transferability or structural safety. An empirical coefficient's validity comes from its source/calibration and tested domain, not a successful substitution.
6. Low-confidence PDF/OCR symbols require the original region. Keep the source crop/locator and uncertainty in reading notes; do not guess from expected mechanics. A verified source image can be a reading fallback, but does not satisfy a final DOCX requirement for editable native math.

For Markdown use supported math delimiters, not plain code as rendered equations. Preserve the printed source number as a locator; generated manuscript numbering is a separate namespace. Do not translate variable names inside a formula.

For DOCX follow [docx-creation-and-formatting.md](docx-creation-and-formatting.md) and, only for the confirmed project, [hfut-thesis-word-objects.md](../style/hfut-thesis-word-objects.md). Use native OMML when required, check the actual mathematical payload and number/callout mapping, and inspect rendered affected pages. Raw LaTeX in ordinary text and a raster equation are not native editable equations. No universal equation wrapper overrides the controlling template.

## Figures: distinguish evidence types

| Figure type | Required distinction |
|---|---|
| Quantitative plot | Traceable actual data, definitions, transformations and reproducible plotting path |
| Test photo / FE contour | Actual specimen/run, view/stage, scale/legend and source/processing provenance |
| Structure / apparatus / method schematic | Verified geometry/components/sequence or explicit conceptual simplification |
| Generated conceptual illustration | Label as illustration; not a real specimen, test photo, FE solution or quantitative result |

Never use generated images to fabricate curves, cracks, stress clouds, specimens, measured geometry or statistical evidence. Demonstration data require explicit authorization and conspicuous labeling; they cannot enter manuscript results as observations.

For quantitative work check:

- correct x/y columns, groups, curve identities, ordering, paired comparisons and axis units;
- missing/censored values, exclusions, filters, sampling, smoothing, fitting, interpolation and normalization; document any processing that can change apparent trends;
- axis bounds/scales, broken/log axes, aspect ratio, dual axes and legends do not manufacture a relationship; log axes cannot silently drop nonpositive observations;
- center, uncertainty definition, sample/run/fold count and aggregation; comparable panels either use consistent uncertainty or explain a real difference;
- captions and body statements agree with actual values, rank/direction, conditions and visible evidence; do not claim exact values from an unreadable image.

For image/contour work preserve raw files and record crop, contrast, scale calibration, colormap/range, stitching, reuse and data linkage as relevant. Do not selectively hide contrary damage or compare separately auto-scaled clouds as if their colors had a common scale.

Actual figure execution follows [nature-figure-cooperation.md](nature-figure-cooperation.md), including its backend gate and dependency boundary. Hand over source/semantics/transforms/uncertainty, then inspect returned files rather than claiming a brief is a generated figure. On newer companion versions check source-preflight, alignment, rendered collisions and transform/uncertainty consistency when available; use the companion's actual current interface, not invented commands.

Inspect final inserted/printed size: readable labels and math, no clipping/collision, coherent panels, color-vision and grayscale distinctions, expected physical size, actual export format and embedded fonts/raster resolution as relevant. A source-code lint cannot replace rendered review, and a visually attractive figure cannot validate its data.

## Tables: numeric and semantic checks

- Define response, units, grouping, row IDs, metric direction, statistic and precision. Keep zero, missing, not applicable and below-detection states distinct. Do not substitute zeros or impute values without a supplied/authorized method.
- Reconcile row/column identity after sorting, translating, merging or transposing; especially verify multi-level headers and model/specimen aliases.
- Recompute appropriate totals, counts, weighted/unweighted means, signed/absolute errors, change rates and ranks from identified data. State denominator, weighting and rounding. A rounded column may not sum exactly; distinguish expected rounding from a real discrepancy.
- Keep percent change, percentage-point difference and dimensionless ratios distinct. Verify comparison direction and reference baseline. A lower metric is not universally better.
- Explain abbreviations, uncertainty, exclusions, markers and source in caption/notes. Best/second-best emphasis must match the supplied values and metric direction; respect the controlling template, including black-only text where required.
- Use native editable tables for final Word data, correct bilingual captions/numbering when required, legible widths, meaningful repeated headers and continuation handling. Check merged cells, split rows and page boundaries in rendered pages. A screenshot is not a native table.

## Bounded numeric helper

`scripts/audit_numeric_consistency.py` is a read-only standard-library helper for declared CSV aggregations, relative changes, regression error metrics and disjoint split/group IDs. It does not parse a manuscript, infer scientific definitions, validate arbitrary formulas, prove leakage freedom or check plotting/rendering.

The agent builds the JSON spec from actual source mappings, not guessed rows. Resolve ambiguous definitions first. Run:

```shell
python -X utf8 scripts/audit_numeric_consistency.py /path/to/checks.json
```

The schema is `schema_version: 1`, with `datasets` mapping IDs to relative CSV paths and optional SHA-256, and `checks` entries with unique `id` and `kind`. Paths must stay under the spec directory. CSV headers and row identities must be unambiguous. No expressions/code are evaluated and no files are modified.

```json
{
  "schema_version": 1,
  "datasets": {"loads": {"path": "loads.csv"}},
  "checks": [
    {"id": "mean-load", "kind": "aggregate", "dataset": "loads",
     "column": "peak_kN", "operation": "mean", "reported": 120,
     "abs_tol": 0.05, "rel_tol": 0},
    {"id": "group-split", "kind": "split_disjoint", "dataset": "loads",
     "split_column": "split", "group_column": "base_geometry"}
  ]
}
```

Supported checks and required fields:

- `aggregate`: `dataset`, `column`, `operation` (`sum`, `mean`, `min`, `max`), `reported`; missing data fail unless explicitly `missing: "exclude"`, which reports excluded counts. Units must already match and be documented outside the helper.
- `relative_change`: `baseline`, `current`, `reported`; each input is a cell locator `{dataset, row_key, row_id, column}`. Computes `(current-baseline)/baseline` as a ratio, or percent only if `scale: "percent"`. A zero baseline is undefined. Percentage-point differences are not this operation.
- `regression_metrics`: `dataset`, `actual`, `predicted`, `reported` mapping selected `mae`, `rmse`, `mbe`, `r2`, `mape` to values. MBE means prediction minus observation; MAPE is a ratio. Missing data, undefined requested metrics and nonfinite values fail. Macro/group-weighted variants require another explicitly justified calculation, not relabeling this pooled result.
- `split_disjoint`: `dataset`, `split_column`, `group_column`; reports any group in multiple partitions and sample/partition counts. Groups are user-defined strings; absence of overlap does not detect near-duplicates, wrong grouping or preprocessing leakage.

For numeric comparisons supply justified nonnegative `abs_tol`/`rel_tol` (defaults `1e-9`/`0`). Tolerances are a reporting choice, not uncertainty estimates. The report includes actual CSV hashes. Overall `PASS` covers declared checks only; failed checks or empty/unusable specs cannot pass. A failed check is a finding, not permission to rewrite the author's data.

## Delivery status

Report only performed layers: scientific/source review, numeric checks, native-object checks, and visual checks. Link actual artifacts or say not generated/not checked/unavailable. Follow [manuscript-consistency-and-delivery.md](manuscript-consistency-and-delivery.md) for downstream updates. Never substitute a structural validator's pass for source verification or science correctness.
