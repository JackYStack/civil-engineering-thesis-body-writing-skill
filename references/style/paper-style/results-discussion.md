# Methods, Results, And Discussion Style

Use this guide when writing methods rationale, result paragraphs, discussion sections, figure/table interpretation, or engineering meaning for paper-style manuscripts.

## Method Rationale

Paper methods should explain why the selected method can answer the stated question. The reader needs enough detail to judge validity, not a thesis-length tutorial.

Use the pattern:

`question -> method role -> input/source -> output/indicator -> validation/comparison -> limitation`

For FE or ML manuscripts, separate three layers:

- evidence generation: experiment, simulation, literature dataset, parametric model, or hybrid source;
- model construction: constitutive model, FE mesh/contact/boundary setting, ML algorithm, feature set, train-test split, or tuning method;
- reliability check: comparison with tests, error metrics, sensitivity analysis, SHAP, external validation, or applicability range.

Do not describe software buttons or generic algorithm principles unless they affect reproducibility or interpretation.

## Common Paper Evidence Chain

A paper result paragraph should normally follow:

`finding -> figure/table/metric -> trend or comparison -> mechanism -> design implication -> boundary`

The first sentence should translate the result, not merely point to a figure. "Figure 6 shows..." is acceptable only when followed immediately by what the figure proves. Stronger paragraphs begin with the observation: "Increasing connector stiffness mainly improves the stiffness-related DCA, whereas the capacity-related DCA is more sensitive to connector strength."

## Data Translation Rules

Do not write results as a statistical log. Convert numbers into engineering meaning:

- Instead of only reporting an error metric, state whether the model is adequate for ranking, preliminary sizing, or final verification.
- Instead of only reporting a parameter ranking, state whether the parameter affects stiffness, capacity, ductility, deflection, slip, or failure mode.
- Instead of only reporting a curve trend, identify the stage, threshold, plateau, or nonlinear change.
- Instead of only reporting agreement, state which aspects agree: peak value, initial stiffness, curve shape, cracking load, ultimate load, displacement, strain distribution, failure mode, or crack pattern.

If the manuscript lacks a numerical basis for "significant" or "good agreement", replace those words with measured indicators or downgrade the claim.

## Results And Discussion Integration

For engineering papers, Results and Discussion may be combined when the mechanism explanation is inseparable from the result. Keep the discussion anchored to evidence:

1. name the observed phenomenon;
2. point to the figure, table, metric, or model output;
3. explain the structural mechanism;
4. compare only with studies or methods that are genuinely comparable;
5. state the design or modeling consequence;
6. close with a boundary or uncertainty when needed.

Avoid drifting into a second literature review. Prior work belongs in discussion only when it explains, contrasts, or bounds the current result.

## Figure And Table Interpretation

Each figure or table should have one main job. Before writing, ask:

- What claim does this figure/table support?
- Which variable or indicator is the reader meant to compare?
- What is the baseline?
- Does the trend change by load level, failure stage, geometry, material, or connector property?
- Does the caption and text use the same symbols and names?

If a figure contains multiple messages, split the paragraph by claim rather than describing the subfigures mechanically.

## Boundary Language

Results should not be generalized beyond the evidence source. Use boundary phrases such as:

- "within the investigated parameter range";
- "for preliminary design and parameter screening";
- "before detailed FE verification";
- "for the selected connector type and loading condition";
- "under the dataset and feature definition used in this study".

These phrases are not hedging for weakness. They help reviewers see that the paper knows exactly what it has and has not proven.
