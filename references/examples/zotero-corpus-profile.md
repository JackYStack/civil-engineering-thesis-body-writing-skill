# Zotero Corpus Profile for Civil Thesis Body Writing

This file records summarized writing patterns learned from the local Zotero corpus. It is not a bibliography, paper index, or citation list. Concrete paper titles, authors, Zotero item keys, DOI strings, file names, and local paths are intentionally excluded.

Use this profile only to guide topic clustering, claim functions, variable extraction, and paragraph organization. Before inserting any citation into a manuscript, use the claim-level citation workflow and verify the exact sentence against the relevant source.

## Corpus Coverage

The Zotero corpus provides strong coverage for precast concrete sandwich panels (PCSPs), insulated sandwich wall panels, connector behavior, partial composite action, finite-element modelling, analytical models, and structural machine-learning prediction.

Common source categories include:

- review and state-of-the-art papers for background, classification, and research trends;
- connector direct-shear, pull-out, and shear-performance studies for connector stiffness, capacity, failure mode, and spacing/material effects;
- panel flexural-performance and DCA studies for load-deflection response, stiffness, capacity, slip, and degree of composite action;
- partial-composite analytical models for DCA-to-deflection/capacity logic and simplified design calculation;
- nonlinear finite-element studies for model assumptions, validation sequences, and parametric boundaries;
- data-driven prediction studies for feature-output definition, model comparison, interpretability, and assisted-design boundary;
- adjacent structural ML papers for response-curve prediction, strength prediction, damage-state prediction, and metric reporting.

## Writing Use by Cluster

| Cluster | Writing Use |
|---|---|
| PCSP review/background | Establish engineering demand, component classification, connector role, thermal-structural contradiction, and development trend. |
| Connector shear behavior | Support paragraphs on connector stiffness, capacity, failure mode, spacing effect, material effect, interface slip, and shear transfer mechanism. |
| Panel flexural behavior and DCA | Support DCA definition, stiffness/capacity distinction, load-deflection interpretation, neutral-axis or strain-based reasoning, and design implications. |
| Partial-composite analytical models | Support simplified calculation logic, service-stage deflection estimation, capacity-stage reasoning, and limitations of full-composite assumptions. |
| FE and numerical modelling | Support model assumption statements, validation-before-expansion sequence, material/interface modelling, boundary conditions, and parameter ranges. |
| Data-driven prediction | Support dataset construction, feature-output mapping, model comparison, SHAP/sensitivity interpretation, uncertainty or applicability statements, and GUI-assisted design framing. |
| Structural ML adjacent fields | Support general ML method selection, metric definitions, small-sample caution, response-curve prediction, and model generalization discussion. |

## Full-Text Sampling Patterns

Full-text sampling was used to learn transferable writing structures rather than to store paper references. The recurring structures are:

- Chinese thesis chain: material tests -> connector tests -> panel tests -> DCA estimation -> connector layout or safety evaluation;
- analytical model chain: partial-composite difficulty -> connector contribution -> simplified response model -> validation against prior tests -> parameter analysis -> design boundary;
- DCA method chain: DCA calculation basis -> method comparison -> applicability boundary -> design or interpretation use;
- design-DCA chain: design parameters -> calculated/predicted DCA -> structural response estimation -> engineering-use boundary;
- data-driven chain: tests or FE data -> feature/output definition -> model comparison -> interpretability -> assisted-design workflow.

## Writing Patterns Learned

### Introduction

Use a topic-clustered narrowing chain:

`PCSP engineering role -> connector/composite-action contradiction -> existing tests/FE/analytical models/ML work -> remaining gap -> this study's response`.

Avoid chronological listing. Each citation cluster should support one focused function: background, gap, method, comparison, or boundary.

### Methods

Use method-specific reproducibility chains:

- connector/panel tests: `specimen design -> material properties -> connector/panel geometry -> setup -> instrumentation -> loading protocol -> response indicators`;
- FE/analytical: `model assumption -> constitutive law/interface -> boundary/loading -> validation -> parameter range`;
- ML/data-driven: `data source -> input variables -> outputs -> preprocessing -> models -> metrics -> interpretability -> application`.

### Results and Discussion

Prefer indicator-based paragraphs:

`figure/table evidence -> response indicator -> trend -> numerical comparison -> mechanism -> implication/boundary`.

For PCSPs, common indicators are DCA, stiffness, ultimate capacity, load-deflection response, connector slip/shear, failure mode, and service-load deflection.

### Model Application

Frame application conservatively:

`input design parameters -> predicted DCA_s / DCA_c -> post-processing response such as stiffness, deflection or capacity -> SHAP-guided parameter adjustment -> FE/test/code verification boundary`.

Do not present GUI or ML models as replacements for design codes unless code-level validation is available.

### DCA Paragraphs

State the DCA type and stage before discussing the result:

`DCA type -> calculation basis -> loading stage -> design/use implication -> limitation`.

Common DCA functions:

- stiffness/displacement DCA for service-stage stiffness and deflection;
- load/capacity DCA for ultimate strength or moment capacity;
- neutral-axis/strain DCA for experimentally observed composite action;
- design DCA for parameter-based preliminary design;
- model-predicted DCA for rapid screening within the training/validation range.

Avoid writing DCA as a single fixed constant when the evidence separates stiffness-stage and capacity-stage behavior.

## Parameter Extraction for PCSP Full Text

When using Zotero full text, extract:

- specimen geometry: length/span, width, total thickness, inner/outer wythe thickness, insulation thickness;
- connector properties: type, material, diameter/shape, spacing, number, inclination, embedment, rib width/layout;
- materials: concrete strength/modulus, reinforcement grade, FRP/GFRP/BFRP properties, insulation type/properties;
- loading and boundary: four-point/six-point bending, simple support, loading rate, pure bending region;
- response indicators: cracking/peak/ultimate load, initial stiffness, midspan deflection, slip, strain, DCA, ductility, failure mode;
- ML fields when present: data source, feature list, outputs, model candidates, validation metrics, interpretability method, explicit equations.

## Citation Directions

Use Zotero items by function, not by title resemblance:

- `background`: review and state-of-the-art sources;
- `gap`: partial-composite analytical/model papers and DCA comparison studies;
- `method`: FE, analytical, ML prediction, SHAP, or evaluation-metric sources;
- `comparison`: sources with the same response indicator, connector type, loading condition, or modelling assumption;
- `boundary`: sources showing limited parameter range, connector-specific behavior, dataset scope, or model assumptions.

## Limitations

- This profile is a summarized corpus map, not a final bibliography.
- It should not be cited directly.
- If Zotero returns metadata only, inspect the local PDF/TXT/HTML or use a reader/OCR workflow before relying on details.
- A candidate source must be tied to a sentence-level claim before it enters the manuscript.
