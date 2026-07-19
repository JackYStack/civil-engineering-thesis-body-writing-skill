# Local Thesis Machine Learning Style

Use this file for data-driven, machine-learning, surrogate-model, SHAP, and engineering application sections in civil-engineering theses.

## Section Order

1. Data source and sample composition.
2. Input features, output indicators, and engineering meaning.
3. Data preprocessing, train/test split, and scaling or encoding.
4. Candidate models and hyperparameter strategy.
5. Evaluation metrics and model comparison.
6. Explainability analysis.
7. Engineering application workflow and boundary.

## Data And Feature Writing

- Define each input variable by engineering meaning, unit, and range when available.
- Distinguish specimen/test/FE/analytical/generated samples.
- State whether outputs are directly measured, simulated, calculated, or post-processed.
- Avoid writing `the model learns the law` unless the data coverage and validation support that claim.

## Model Comparison

Use model comparison to answer which model is suitable for which output, not to praise every algorithm.

Report:

- dataset size and split;
- metrics such as R2, MAE, RMSE, MAPE, MBE, or task-specific accuracy;
- training/test distinction;
- whether cross-validation or hyperparameter optimization was used;
- whether different outputs have different prediction difficulty.

## SHAP Or Explainability

Explainability should support engineering interpretation:

- identify dominant variables for each output;
- state direction or threshold only when the SHAP result supports it;
- compare SHAP ranking with known mechanics;
- avoid replacing mechanism verification with feature importance alone.

## Engineering Application

When writing GUI or assisted design:

1. Put the tool/workflow first.
2. Define inputs.
3. Define predicted outputs.
4. Explain post-processing from predicted indicators to engineering response.
5. Explain parameter adjustment or scheme screening.
6. State that finite-element, experiment, or code verification is still required for final design.

## Common Risks

- Treating small-sample model accuracy as general design validity.
- Mixing data-driven prediction with physical causation.
- Reporting metrics without specifying data split and output indicator.
- Calling assisted screening `inverse design` when no true inverse optimization is implemented.
- Writing GUI as a code product rather than an engineering decision workflow.
