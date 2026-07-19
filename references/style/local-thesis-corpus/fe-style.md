# Local Thesis Finite-Element Style

Use this file for finite-element modelling, validation, and parameter analysis sections in civil-engineering theses.

## Section Order

1. Modelling objective and model role in the thesis.
2. Geometry, element types, material constitutive models, and interaction definitions.
3. Boundary conditions, loading, mesh strategy, and convergence or sensitivity notes.
4. Validation against experiment, analytical result, or trusted benchmark.
5. Parameter analysis.
6. Mechanism explanation and modelling boundary.

## Modelling Assumptions

- State assumptions as modelling boundaries, not hidden simplifications.
- Explain why the selected constitutive model, contact definition, or connector representation is suitable for the response being studied.
- If a parameter is calibrated, specify the evidence used for calibration.
- If a parameter is assumed, mark it as an assumption and avoid overclaiming validation.

## Validation Writing

Validation should compare at least one of the following:

- load-displacement or moment-curvature curve;
- peak load or stiffness;
- damage/failure mode;
- strain or slip response;
- crack or crushing region;
- trend under comparable parameter change.

Write the comparison by indicator. Do not say only `吻合较好`.

## Parameter Analysis Writing

Use the chain:

```text
parameter -> condition range -> response indicator -> trend -> mechanism -> boundary
```

For each parameter group:

- define the baseline model;
- vary one primary parameter when possible;
- compare normalized or absolute indicators consistently;
- state whether the trend affects stiffness, capacity, ductility, damage, slip, or composite action;
- avoid turning FE results into design provisions without additional validation.

## Boundary And Reliability

Always state relevant boundaries:

- material constitutive assumptions;
- connector stiffness/capacity representation;
- interface/contact settings;
- mesh and element limitations;
- loading and boundary condition limitations;
- validation specimen or data range.

## Common Risks

- Treating an FE model as fully verified after only peak-load comparison.
- Reporting many cloud plots without linking them to indicators.
- Mixing calibration results and prediction results.
- Using FE parameter analysis as a substitute for experiment or code verification.
