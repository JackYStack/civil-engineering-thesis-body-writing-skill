# PCSP Citation Directions

Use this guide for precast concrete sandwich panels, insulated concrete sandwich panels, partially composite sandwich panels, connectors, degree of composite action, flexural behaviour, analytical/FE modelling, and PCSP data-driven prediction.

## Keyword Set

Search both English and Chinese terms:

- `precast concrete sandwich panel`, `insulated concrete sandwich panel`, `sandwich wall panel`, `composite sandwich panel`;
- `partially composite`, `degree of composite action`, `DCA`, `composite action`;
- `connector`, `shear connector`, `wythe tie`, `FRP connector`, `GFRP`, `BFRP`;
- `load-deflection`, `flexural performance`, `serviceability`, `ultimate capacity`;
- `beam-spring model`, `analytical model`, `finite element`, `nonlinear finite element`;
- `machine learning`, `surrogate model`, `SHAP`, `assisted design`, `data-driven prediction`;
- `夹心保温墙板`, `预制混凝土夹心墙板`, `组合度`, `拉结件`, `连接件`, `部分组合`.

## Priority By Claim Type

| Claim Type | Prefer These Sources |
|---|---|
| Structure/classification/background | PCSP/ICSP state-of-the-art, connector studies, composite-action reviews or representative studies. |
| Partial composite design difficulty | Analytical beam-spring models, load-deflection models, DCA calculation/comparison papers. |
| Connector influence | Direct shear tests, connector spacing/material/inclination studies, connector damage evolution studies. |
| FE modelling basis | Nonlinear FE studies validated against PCSP tests, connector slip/contact/material nonlinearity papers. |
| DCA definition/calculation | Papers that explicitly define the same DCA type or calculation route used in the manuscript. |
| ML prediction/assisted design | Structural ML prediction papers for method support plus PCSP-specific data-driven studies for object support. |

## DCA Citation Guardrail

Do not cite any DCA paper generically. First identify the DCA meaning:

- stiffness or displacement DCA;
- strain DCA;
- load or capacity DCA;
- neutral-axis DCA;
- design DCA;
- model-predicted DCA;
- service-stage versus ultimate-stage DCA.

Then check whether the cited paper uses the same stage, indicator, formula, or interpretation. If not, grade it as `部分支撑` or `不建议引用`.

## ML Citation Guardrail

For PCSP machine-learning manuscripts, separate two citation needs:

- object-specific support: PCSP/ICSP, connectors, DCA, flexural behaviour;
- method-specific support: ensemble learning, neural networks, SHAP, surrogate modelling, small-sample structural prediction.

Generic AI/ML papers should not be used to support PCSP mechanical claims. PCSP-specific papers should not be used to support an ML algorithm unless they actually use or validate that method.

## Suggested Citation Functions

Use citation functions deliberately:

- background: PCSP application, composition, connector role, classification;
- gap: lack of fast, practical DCA prediction under multi-parameter coupling;
- method: analytical DCA formula, FE modelling basis, ML/SHAP method basis;
- comparison: published test/FE/analytical/ML findings relevant to flexural response or DCA;
- boundary: parameter range, connector type, data coverage, service/ultimate state, extrapolation risk.

## Common Weak Matches

Be cautious when a paper:

- studies generic sandwich composites rather than concrete sandwich panels;
- studies axial or in-plane shear behaviour while the claim concerns flexural DCA;
- studies a different connector material or layout but is used for a universal connector conclusion;
- reports fully composite or non-composite behaviour while the claim concerns partial composite action;
- uses thermal bowing or energy performance while the claim concerns structural capacity;
- provides ML method examples in unrelated structural components but is cited as PCSP evidence.

These sources may still be useful, but their support grade should reflect the mismatch.
