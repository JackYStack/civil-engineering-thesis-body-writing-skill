# Phenomenon-Mechanism-Condition Writing Framework

Use this guide when drafting or revising introductions, literature reviews, methods, results, discussions, conclusions, thesis-to-paper manuscripts, SCI papers, or any section that feels like a flat "gap list" or data report.

The goal is to convert thesis/paper prose from:

`background -> prior studies -> this paper does something`

into a stronger causal argument:

`phenomenon -> mechanism -> condition -> testable question -> evidence -> bounded implication`.

## 0. Conflict-Driven Academic Storyline

Use storytelling logic as an internal planning tool, not as dramatic language in the manuscript. The goal is to keep the reader's technical curiosity active while preserving civil-engineering precision.

Core storyline:

`core contradiction -> why existing explanations/methods are insufficient -> proposed route -> decisive evidence -> mechanism clarified -> limitation and next refinement`.

Rules:

1. **One paper, one core problem.** Do not let the manuscript become a list of independent contributions. Secondary methods, parameters, and figures should all serve the same contradiction or research question.
2. **Introduction raises the question.** Show why the problem is not optional by exposing a design trade-off, modelling contradiction, prediction failure, or unexplained response.
3. **Methods provide the route map.** After the question is raised, methods should tell the reader how the study will break the problem into testable steps. If the paper combines A and B, explain what A cannot solve, what B cannot solve, and why A+B is necessary.
4. **Results answer in stages.** Do not list every table in order. Lead each major result subsection with the central finding, then use figures, tables, and metrics to prove it. If a finding reverses an expectation, shows a threshold, or changes the controlling mechanism, state that before detailing secondary numbers.
5. **Discussion closes and reopens carefully.** Acknowledge limitations as technical boundaries and future refinements, not as decorative "cliffhangers". State what remains unresolved because of data range, specimen type, model assumptions, or validation scope.
6. **Transitions should carry curiosity.** Section endings should make the next section necessary: after the introduction, the reader should ask "how will this be solved?"; after methods, "what did the route reveal?"; after results, "why does this happen and where does it hold?"; after discussion, "what needs refinement next?"

Do not overuse dramatic connectors. Words such as "however", "in contrast", "unexpectedly", "nevertheless", and "this indicates" are useful only when supported by evidence. In Chinese thesis prose, prefer measured transitions such as "然而", "需要指出的是", "与上述趋势不同", "进一步分析可知", and "这说明".

## 1. Three-Layer Logic

Every important argument should be checked against three layers.

| Layer | Question | Civil-engineering form |
|---|---|---|
| Phenomenon | What observable fact, contradiction, trend, failure mode, or modelling problem starts the section? | A measured response, design contradiction, prediction error, failure pattern, parameter trend, or engineering practice problem. |
| Mechanism | What process explains why the phenomenon occurs? | Load transfer, stiffness degradation, interface slip, cracking, confinement, bond deterioration, corrosion damage, data feature interaction, model bias, or uncertainty propagation. |
| Condition | Under what parameter, boundary, material, loading, dataset, or design condition does the mechanism change? | Connector stiffness/capacity, spacing, wythe thickness, reinforcement ratio, concrete strength, corrosion rate, axial compression ratio, shear span ratio, sample range, model assumption, or load level. |

Do not write a mechanism without a phenomenon. Do not write a broad conclusion without its conditions.

## 2. Introduction: Start From a Puzzle, Not Only a Gap

Weak introduction logic:

`Existing studies investigated X, but few studies considered Y. Therefore, this paper studies Y.`

Stronger introduction logic:

`A technically plausible expectation or engineering assumption conflicts with observed behaviour. This contradiction creates a question. Existing work explains part of the question, but leaves a mechanism or condition unresolved. This study addresses that unresolved part through a defined method and evidence route.`

Use this structure:

1. **Expected relation**: what engineers or prior theory would expect.
2. **Observed puzzle**: what trend, failure mode, prediction problem, or design trade-off complicates that expectation.
3. **Competing explanations**: what existing studies or methods can and cannot explain.
4. **Research question**: what mechanism or condition this paper will clarify.
5. **Study response**: test, FE model, analytical model, ML model, SHAP interpretation, GUI workflow, design equation, or validation route.

The opening should create a technical need, not entertainment suspense. Replace "this is mysterious" with "the existing explanation cannot simultaneously account for...".

Civil-engineering examples:

- Expected: denser or stiffer connectors should improve composite action.
- Puzzle: excessive connector stiffness may introduce thermal bridges or local stress concentration, so structural improvement and thermal performance are not automatically aligned.
- Question: under which connector stiffness/capacity/spacing range does the benefit to DCA dominate the penalty or diminishing return?

Avoid making the gap the first source of interest. The gap should appear after the puzzle is clear.

## 3. Literature Review: Build a Dialogue, Not a Display Case

Do not organize literature as a row of unrelated exhibits:

`Author A did... Author B did... Author C did...`

Organize it as a dialogue among explanations:

1. **Mainstream explanation**: what the dominant method or view says.
2. **Ignored dimension**: what it does not capture, such as nonlinear slip, material degradation, coupled loading, parameter interaction, uncertainty, or design usability.
3. **Alternative view**: another modelling, experimental, analytical, or data-driven perspective.
4. **Conflict or complementarity**: where the two views disagree or complement each other.
5. **Model integration**: under which conditions each mechanism is more likely to dominate.

Good literature-review paragraph shape:

`Research stream A explains phenomenon P through mechanism M1, and is suitable for condition C1. However, when condition C2 appears, M1 is insufficient because... Research stream B introduces mechanism M2, which improves... but still lacks... Therefore, this study integrates/compares/extends... to clarify...`

For civil-engineering thesis writing, the "dialogue" can be between:

- experiment vs finite element modelling;
- simplified analytical formula vs refined numerical simulation;
- mechanics-based model vs machine learning surrogate;
- serviceability stiffness vs ultimate capacity;
- structural performance vs thermal/constructability constraints;
- local damage mechanism vs global component response.

## 4. Methods: Explain Why the Design Is Necessary

Methods should not only report what was done. They should explain why each design choice is needed for the research question.

For each major method choice, identify:

- **Purpose**: which phenomenon/mechanism/condition it tests.
- **Reason for design**: why this specimen group, parameter range, model, metric, or evaluator is used.
- **Bias controlled**: what error, uncertainty, or alternative explanation the design reduces.
- **Output link**: which figure, table, formula, or metric will later support the claim.

Method paragraph shape:

`To distinguish mechanism M1 from M2 under condition C, this study selected/constructed/measured... This design is necessary because... The corresponding output indicator is..., which is later used to evaluate...`

Civil-engineering examples:

- If both stiffness DCA and capacity DCA are predicted, explain that serviceability and ultimate limit states are governed by different connector properties.
- If both ML prediction and SHAP interpretation are used, explain that prediction accuracy alone cannot identify which design parameter controls the response.
- If FE validation follows ML screening, explain that fast prediction is used for preliminary screening, whereas FE remains the higher-fidelity check for selected schemes.
- If the method combines two routes, such as mechanics-based modelling and data-driven prediction, state which limitation each route addresses and why the combined route is more suitable for the core question.

## 5. Results: Translate Data, Do Not Only Report Statistics

Weak result sentence:

`H1 is supported (B = 0.25, p < 0.05).`

Civil-engineering equivalent:

`The model has good accuracy, and the parameter has a significant effect.`

Stronger result logic:

`The data show which response changed, by how much, relative to what baseline, and why this supports or modifies the proposed mechanism. If the trend is nonlinear, staged, threshold-like, or boundary-dependent, state that explicitly.`

For major result subsections, lead with the answer before the evidence details:

`The key finding is not that parameter X changes the response, but that the controlling mechanism shifts from M1 to M2 when condition C is reached. Fig. X and Table Y support this shift by...`

Result paragraph shape:

1. **Evidence**: point to figure, table, metric, or curve.
2. **Trend**: describe the dominant direction or stage.
3. **Magnitude or comparison**: provide difference, error, ranking, threshold, or interval when available.
4. **Mechanism translation**: explain what the trend means mechanically or computationally.
5. **Condition/boundary**: state when the trend holds or changes.

Nonlinear and conditional results deserve explicit wording:

- "The effect is not monotonic..."
- "The marginal increase decreases after..."
- "The controlling factor changes from... to... when..."
- "This relationship holds within the tested range, but extrapolation beyond... requires verification."

## 6. Section-Specific Checklist

### Introduction

- What is the puzzle or contradiction?
- Why is the puzzle practically or theoretically important?
- Which mechanism or condition remains unclear?
- What exact method will this study use to answer it?
- Does the final paragraph make the reader expect the method route rather than only accept a gap statement?

### Literature Review

- What is the mainstream explanation?
- Which perspective is missing?
- Are studies grouped by problem/mechanism rather than chronology?
- Does the final paragraph integrate the dialogue into this study's model?

### Methods

- Why is each specimen/model/feature/metric needed?
- Which bias or alternative explanation is controlled?
- Are method choices tied to later evidence?
- Are assumptions and parameter ranges stated?
- Does the method section act as a route map for solving the core contradiction?

### Results and Discussion

- Is each data result translated into a mechanical/model meaning?
- Is any nonlinear, threshold, stage, or interaction effect described?
- Does the paragraph explain mechanism rather than only repeat the figure?
- Is the boundary of the conclusion clear?
- Does each major result answer a question raised earlier instead of merely reporting another table?
- Are limitations framed as evidence boundaries and future refinements rather than unsupported weakness or overpromised future work?

## 7. Fast Diagnostic Questions

Before finalizing a section, ask:

1. If all citations were removed, would the reader still know what puzzle the study answers?
2. If all data tables were hidden, would the reader still know what mechanism the data support?
3. If a parameter changes, have we stated whether the mechanism strengthens, weakens, reverses, saturates, or becomes invalid?
4. Does the method description explain why this design is necessary, or only describe what was done?
5. Does the result paragraph translate the data into engineering meaning?
6. Does each section leave a legitimate technical question that the next section answers?

If the answer is no, revise the section before polishing language.

## 8. Output Add-On

When this framework is used for a substantial rewrite, include a compact block if helpful:

```md
现象-机制-条件校准：
- 现象/困惑：
- 主导机制：
- 条件变量：
- 需要验证的关系：
- 对应证据：
- 适用边界：
- 读者期待链：引言提出什么问题；方法如何承接；结果回答什么；讨论留下什么边界
```

For short paragraph polishing, silently apply the framework and only report unrepaired missing items under `需补充或确认`.
