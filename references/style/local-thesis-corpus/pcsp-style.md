# Local Thesis PCSP Style

Use this file for precast concrete sandwich panels (PCSPs), connector behavior, composite action, DCA, FE/ML-assisted PCSP design, and GUI-assisted preliminary design sections.

## Core Object Chain

PCSP writing should keep the following object chain stable:

```text
inner/outer concrete wythes -> insulation layer -> connector shear transfer -> interface slip -> composite action/DCA -> stiffness/capacity/deflection -> design or verification boundary
```

Do not discuss connector arrangement, thermal insulation, or machine learning as isolated topics. Link them to composite action or structural response.

## Composite Action And DCA

- Define DCA before using it as a design indicator.
- Distinguish stiffness DCA and capacity DCA if both are used.
- State whether DCA is measured, FE-derived, formula-derived, or ML-predicted.
- Explain how DCA affects flexural stiffness, midspan deflection, bearing capacity, or moment capacity.
- Avoid treating DCA as a constant independent of connector stiffness, connector capacity, spacing, material nonlinearity, and load level.

## Connector Variables

When writing about connectors, tie each parameter to a mechanism:

- connector spacing -> shear transfer density and interface slip;
- initial connector stiffness -> service-stage composite deformation;
- connector capacity -> ultimate-stage shear transfer and capacity DCA;
- connector material/type -> stiffness, capacity, durability, and thermal bridge boundary;
- connector layout -> load path and local stress concentration.

## PCSP FE Writing

- State how wythes, insulation, connectors, and interfaces are represented.
- Validate both global response and composite action-related response where possible.
- Use FE parameter analysis to explain mechanisms before using it to generate ML samples.
- Mark connector constitutive assumptions and interface simplifications.

## PCSP ML Writing

- Inputs should correspond to geometry, material, reinforcement, insulation, connector spacing, connector stiffness, and connector capacity.
- Outputs should be clearly named, such as stiffness DCA, capacity DCA, midspan deflection, ultimate capacity, or design response.
- Use SHAP to explain which design variables control each output.
- For assisted design, present the process as rapid evaluation, scheme screening, or parameter adjustment support unless a true optimization algorithm is implemented.

## GUI-Assisted Design

A PCSP GUI/application section should follow:

1. Input design parameters.
2. Predict DCA or response indicators.
3. Convert DCA to engineering response through stiffness/capacity calculation.
4. Compare with demand or service/ultimate criteria.
5. Use SHAP or sensitivity results to adjust connector and geometry parameters.
6. Verify selected schemes by FE, experiment, or code-based checks.

## Boundary Statements

Use explicit boundaries:

- `该流程适用于本文样本和参数范围内的初步方案筛选。`
- `机器学习预测结果不能替代最终结构设计校核。`
- `对于超出连接件刚度、承载力或墙板几何范围的方案，需重新验证模型适用性。`
