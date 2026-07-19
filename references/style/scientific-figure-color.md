# Scientific Figure Color Guide

Use this guide when selecting, revising, or auditing colours for thesis and journal figures. It converts visual examples into task-specific rules; it is not a licence to copy a palette without checking data semantics, accessibility, and the target journal.

When the user requests an actual rendered figure rather than a colour plan/audit, first build the manuscript-facing brief with [nature-figure-cooperation.md](../workflows/nature-figure-cooperation.md), then hand plotting, export, and visual QA to `nature-figure`.

## Source status

- Primary visual source reviewed: [论文配色：跟着顶刊学配色（Nature篇）](https://zhuanlan.zhihu.com/p/704390338), published on 2024-06-20. A user-supplied 23-page PDF archive was rendered and visually checked on 2026-07-17.
- The article samples colour groups from selected 2024 *Nature* figures and reports Hex, RGB, HSB, CMYK, and LAB values. Pages 2-18 are image-heavy palette examples; pages 19-20 explain the five colour models.
- Source boundary: these are author-curated examples extracted from published figures. They are **not** an official Nature house palette, endorsement, or universal accessibility guarantee.
- Hex values below were transcribed from the visible palette cards. Use Hex/RGB as the working master; do not recompute or claim the article's CMYK/LAB values unless the original card is checked.
- Additional accessibility and export rules in this guide are based on the current [Nature research figure guide](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/) and general non-colour redundancy principles. They are independent safeguards, not claims made by the Zhihu article.

## What the source contributes

The useful pattern is not a single default palette. The examples repeatedly show five design strategies:

1. Use a neutral control plus one or two saturated accents for comparisons.
2. Keep related curves within a coherent cool, warm, or muted family.
3. Use lightness progression for ordered quantities and distinct hues for nominal categories.
4. Reserve the strongest colour for the main comparison, intervention, or extreme state.
5. Use pastel high-cardinality palettes mainly for maps, stacked compositions, taxonomies, or schematic groups, not for dense overlapping curves.

## Palette register

These representative groups are sufficient for ordinary civil-engineering figures. Keep the listed order only when it matches the role mapping; otherwise assign colours by semantics and record the assignment.

| ID | Hex colours | Source anchor | Recommended use | Main caution |
|---|---|---|---|---|
| `N3-control` | `#BF1D2D`, `#262626`, `#293890` | PDF p.2 | Three-group control/intervention comparison; black as reference | Red-black discrimination can weaken under colour-vision deficiency; add markers or line styles |
| `N3-ordered` | `#F1B656`, `#397FC7`, `#040676` | PDF p.2 | Low/medium/high or measured/predicted/reference series | Orange-blue is categorical unless the blue pair alone carries order |
| `N4-categorical` | `#DE582B`, `#1868B2`, `#018A67`, `#F3A332` | PDF p.4 | Four nominal groups, component diagrams, grouped bars | Red/green pair is not safe by colour alone |
| `N4-cool` | `#909090`, `#0095FF`, `#019092`, `#6FDCB5` | PDF p.6 | Control plus three related methods or material states | Light green needs dark outlines on white backgrounds |
| `N4-muted` | `#2F2D54`, `#9193B4`, `#BD9AAD`, `#E8D2B3` | PDF p.6 | Model comparison, uncertainty summaries, secondary panels | Pale beige is weak for thin lines and small markers |
| `N5-balanced` | `#808080`, `#F94141`, `#F3B169`, `#589FF3`, `#37AB78` | PDF p.8 | Five groups with a neutral baseline | Red/green requires marker, label, or pattern redundancy |
| `N5-topic` | `#60966D`, `#5B3660`, `#FFC839`, `#E90F44`, `#63ADEE` | PDF p.8 | Five distinct mechanisms, damage modes, or parameter families | Yellow needs an outline and should not carry small text |
| `N3-warm-cool` | `#C72228`, `#F98F34`, `#0C4E9B` | PDF p.9 | Three clearly separated states or temperatures | Do not imply a continuous scale unless values are ordered and lightness is controlled |
| `N6-sequential-blue` | `#91CDC8`, `#6FB9D0`, `#5499BD`, `#3981AF`, `#386195`, `#324C63` | PDF p.12 | Ordered parameter bins, increasing damage/age/load level | Verify monotonic lightness after export and in grayscale |
| `N6-pastel` | `#FB8463`, `#80B1D3`, `#F47F72`, `#BDBADB`, `#FBFBB4`, `#8DD1C6` | PDF p.12 | Stacked composition or six labelled categories | Several colours converge in grayscale; direct labels are preferable |
| `N15-soft` | `#C0E2FD`, `#FEC0C1`, `#CDC6FF`, `#FDC0F7`, `#F3D8F1`, `#D6EBBF`, `#E1CAF7`, `#BFDCE2`, `#F8F0BE`, `#BEEFBF`, `#FEC9C8`, `#C0E2D2`, `#E9BFC0`, `#E3E3E3`, `#BFBFBF` | PDF p.16 | High-cardinality taxonomy, circular tree, or labelled schematic | Not suitable for unlabelled line charts; many pairs have low contrast |

Do not treat this register as exhaustive. It is a compact, verified subset selected for reusable figure tasks rather than a transcription of every source card.

## Color-role mapping

Choose the palette only after defining the variable type and visual hierarchy.

| Figure task | Role assignment |
|---|---|
| Experiment versus FE/analytical prediction | Experimental data: black or dark neutral; principal model: one saturated blue; additional models: ordered shades or distinct line styles; uncertainty: lighter fill of the same hue |
| Load-displacement or moment-curvature curves | Use one hue per specimen family, then markers/dashes for connector spacing, reinforcement ratio, or model type; never assign random colours to an ordered parameter |
| Parameter study | Sequential palette for monotonic parameter levels; diverging palette only when a meaningful reference or zero exists |
| ML model comparison | Baseline in grey, selected/best model in one accent, remaining models in restrained categorical colours; colour must not encode ranking if the ranking changes across metrics |
| SHAP or signed effect | Use a tested diverging map centred at zero; do not substitute a nominal article palette merely because it looks balanced |
| Damage/strain/temperature field | Use a perceptually ordered continuous map with a labelled colour bar; avoid rainbow maps and arbitrary category palettes |
| Component or mechanism schematic | Stable categorical colours may identify concrete wythes, insulation, connectors, reinforcement, loads, and failure modes; keep the same object-colour mapping across all figures |
| Multi-panel manuscript | Maintain a manuscript-level colour ledger: the same specimen, parameter, material, and method retain the same colour in every panel and caption |

When there are more than six categories, first reduce, group, facet, or directly label them. Use `N15-soft` only when spatial separation and labels already carry most of the identification load.

## Selection workflow

1. State the figure's one-sentence conclusion and identify the visual priority.
2. Classify each encoded variable as nominal, ordinal, continuous, or diverging about a reference.
3. Count simultaneously visible series and identify the control/reference series.
4. Select the smallest palette that can express the semantics.
5. Create a colour ledger with `object/series -> Hex -> marker/line style -> panel scope`.
6. Preview at final print size, under colour-vision simulation, and in grayscale.
7. Export a vector master for charts where possible and inspect the journal-ready output, not only the plotting window.

## Color accessibility

- Do not rely on colour alone. Pair hues with markers, line styles, direct labels, keylines, or panel separation.
- Avoid red/green pairs and rainbow scales unless the information remains recoverable without hue discrimination.
- Treat source palettes containing red/green or red/black as candidates requiring testing, not as automatically accessible because they appeared in *Nature*.
- Use black or white text with sufficient contrast; avoid coloured legend text. Prefer colour swatches plus black labels.
- Thin pale lines, semi-transparent points, and overlapping confidence bands need stronger luminance or outlines than large filled bars.
- Check protanopic and deuteranopic simulations. If two scientific states merge, change the mapping rather than merely increasing saturation.

## Grayscale and print

- Desaturate the final figure. The control, main method, and critical state must remain distinguishable by value, marker, or line pattern.
- Print or render at the final column width. A palette that works on a monitor can fail after downscaling.
- Use RGB for the editable digital master unless the target journal explicitly requires otherwise. Preview conversion to CMYK when print reproduction matters.
- Recheck pale yellows, light greens, and pastel pinks after conversion; add dark outlines or use them only as fills.
- Preserve vector text and strokes in PDF/SVG/EPS where accepted. For raster images, follow the target journal's resolution and colour-space requirements.

## Journal precedence

Apply rules in this order:

1. Controlling university or target-journal template and current author instructions.
2. Official figure/accessibility and file-format guidance for the target venue.
3. Data semantics, scientific hierarchy, colour accessibility, and grayscale legibility.
4. The representative palettes in this guide.
5. Personal aesthetic preference.

If the target journal specifies a house palette, RGB/CMYK mode, colour-charge policy, or figure dimensions, that instruction overrides this guide. Never describe these extracted examples as "Nature official colours".

## Output contract

For a figure-colour task, return or record:

1. `Figure purpose`: conclusion, variable types, and series count.
2. `Palette`: selected Hex values and why the family fits the semantics.
3. `Mapping ledger`: each object/series and its colour plus non-colour cue.
4. `QA`: colour-vision, grayscale, final-size, contrast, and export checks.
5. `Boundary`: target-journal rules not yet checked or visual distinctions still at risk.
