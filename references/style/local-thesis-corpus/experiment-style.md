# Local Thesis Experiment Style

Use this file for civil-engineering experimental chapters, including specimen design, material properties, loading protocol, observed damage, and structural performance analysis.

## Section Order

1. Test objective and investigated variables.
2. Specimen design and parameter table.
3. Material properties and measurement methods.
4. Test setup, boundary conditions, loading protocol, and measurement points.
5. Failure process and damage observations.
6. Load-displacement, strain, stiffness, ductility, bearing capacity, or energy indicators.
7. Mechanism explanation and chapter summary.

## Specimen And Material Writing

- State why each variable is selected before listing dimensions or reinforcement details.
- Describe specimen groups by comparison role, not only by specimen number.
- For material properties, specify batch, test method, measured indicator, and whether the value is used in later FE or analytical modelling.
- If connector type, spacing, angle, or quantity is varied, connect the variation to the expected shear transfer, interface slip, or composite action mechanism.

## Loading And Measurement Writing

- Explain loading mode, boundary condition, support constraint, and measurement layout as parts of the reliability chain.
- State which response each sensor or measurement point supports.
- Avoid equipment description that is not used later in result interpretation.

## Failure Process Writing

Use a staged structure:

1. Initial elastic stage.
2. Crack initiation or interface slip.
3. Crack development, connector deformation, reinforcement yielding, or concrete crushing.
4. Peak load and post-peak response.
5. Final failure mode.

Each stage should connect visible phenomena with a mechanical explanation.

## Result Paragraphs

- Lead with the indicator: bearing capacity, stiffness, displacement, strain, ductility, damage, crack width, or slip.
- Compare specimens that isolate one variable.
- Use `相较于...` only when the baseline is explicit.
- Use quantitative values where available; otherwise state the direction and mark missing data.
- End with mechanism or boundary, not a broad design conclusion.

## Common Risks

- Specimen description becomes a construction list without research purpose.
- Failure process only describes cracks but does not explain load transfer or damage evolution.
- Curves are repeated one by one instead of compared by variable.
- Experimental findings are generalized beyond specimen size, boundary condition, or material grade.
