# Nature-Writing Adapted SCI Workflow for Civil Engineering Manuscripts

Use this reference when the user asks for `SCI投稿稿`, `英文投稿稿`, `SCI小论文`, `整篇SCI润色`, `thesis-to-paper`, or high-level English manuscript rebuilding, especially when they explicitly ask to refer to `nature-writing`.

This file adapts the structure of `nature-writing` to civil-engineering papers. It does not turn the manuscript into Nature-style hype. The default target remains engineering-journal clarity, bounded claims, and evidence-first argument.

## Core Adaptation

Borrow from `nature-writing`:

- write the argument before the sentences;
- reduce the paper to one controlling argument;
- assign one job to each paragraph;
- keep claims close to evidence;
- calibrate verbs and claim strength;
- return a claim-evidence map.
- when using Zotero full text, learn article spines, paragraph jobs, evidence ladders, and boundary placement from comparable papers before polishing language.

Keep from `civil-thesis-body-writing`:

- no invented data, mechanisms, references, figures, standards, or conclusions;
- local-first literature support;
-土木工程 result logic: test/FE/ML/design evidence before application claim;
- bounded engineering implications;
- Word/OOXML safety when editing `.docx`.

## One-Sentence Argument

Before drafting an SCI manuscript or major section, write:

```text
In [civil-engineering object/problem], this study addresses [unresolved bottleneck] by [method/workflow], supported by [key evidence], and is applicable within [boundary].
```

For PCSP-style work:

```text
In partially composite precast concrete sandwich panels, this study addresses the rapid evaluation of composite action by developing a data-driven DCA prediction and assisted-design workflow, supported by FE/sample validation, model metrics and SHAP analysis, within the parameter range covered by the dataset.
```

When comparable Zotero full-text papers are available, first write the same one-sentence argument for 3-6 exemplar papers. Use the repeated spine pattern to calibrate the target manuscript's argument. Do not copy exemplar phrasing.

## Full-Paper Argument Architecture

Use the adapted chain:

`engineering demand -> unresolved technical bottleneck -> proposed method/workflow -> decisive evidence -> design or modelling implication -> applicability boundary`

When the manuscript needs a stronger introduction, literature review, methods rationale, or Results and Discussion, expand the chain with [phenomenon-mechanism-condition-framework.md](phenomenon-mechanism-condition-framework.md):

`engineering demand -> observed puzzle/phenomenon -> governing mechanism -> changing condition -> proposed method/workflow -> decisive evidence -> bounded implication`

For whole-manuscript rewriting, keep a restrained reader-curiosity chain:

`Introduction: why must this contradiction be resolved? -> Methods: what route map resolves it? -> Results: what central finding changes or confirms the expectation? -> Discussion: why does it happen, where does it hold, and what remains for future refinement?`

Use this as architecture only. Do not introduce sensational phrasing, overstate novelty, or imply that limitations are advantages.

Civil-engineering examples:

- `engineering demand`: prefabricated structures, structural safety, durability, serviceability, thermal-structural trade-off.
- `technical bottleneck`: connector slip, partial composite action, nonlinear FE cost, lack of design equation, small-sample prediction, coupled damage mechanism.
- `method/workflow`: experiment, FE model, analytical equation, ML surrogate, SHAP-assisted design, GUI, hybrid data-physics method.
- `decisive evidence`: load-deflection response, failure mode, validation error, DCA metrics, R2/RMSE/MAE/MAPE, parameter sensitivity, code/formula comparison.
- `implication`: preliminary design, parameter screening, model validation, design-equation correction, uncertainty-aware assessment.
- `boundary`: specimen type, connector type, data coverage, parameter range, loading condition, model assumptions.

## Section Architecture

### Title

Prefer:

`object + method/output + engineering purpose`

Avoid broad prestige words such as `novel`, `advanced`, `efficient`, or `robust` unless the title makes the claim concrete.

### Abstract

Use one of three patterns.

Pattern A: `problem -> method -> object/data -> variables -> key results -> bounded implication`

Pattern B: `challenge -> insight -> workflow -> validation -> application boundary`

Pattern C: `task -> multiple contributions -> evidence for each contribution -> boundary`

Must include:

- research object;
- unresolved engineering or modelling problem;
- method/workflow;
- data/sample/model basis;
- key variables and outputs;
- quantitative or directional results;
- bounded use.

### Introduction

Use a controlled funnel:

1. field/application demand;
2. object-specific puzzle, counter-intuitive trend, mechanism, or design contradiction;
3. grouped prior work as a dialogue among explanations and their limits;
4. remaining mechanism or condition gap;
5. present study as direct response;
6. contribution list tied to evidence, not slogans.

Do not write a chronological literature list. Do not claim novelty by dismissing prior work.

### Methods

Use:

`design need -> method choice -> implementation -> validation/evaluation`

For each major method choice, state why that choice is needed to distinguish a mechanism, test a condition, control bias, or make the later result interpretable. Do not only list software, specimen dimensions, algorithms, or metrics.

The methods section should let readers predict the logic of the results: validation first, mechanism/parameter isolation second, and application or boundary assessment last when relevant.

Civil-engineering method order:

- Experimental: specimen design -> materials -> test setup -> instrumentation -> loading protocol -> measured indicators.
- FE: assumptions -> constitutive laws -> elements/mesh -> contact/interface -> boundary/loading -> validation.
- ML: dataset -> input/output variables -> preprocessing -> model candidates -> tuning/validation -> metrics -> interpretation/application.
- Design workflow: prediction output -> post-processing formula -> design indicator -> verification route -> applicability range.

### Results

Use an evidence ladder:

1. system/workflow/design-space overview;
2. validation that the experimental, FE, analytical, or ML platform is credible;
3. main result by response indicator;
4. comparison with baseline, code/formula, prior study, or alternative model;
5. mechanism, diagnostic analysis, SHAP interpretation, or parameter sensitivity;
6. application, generalization, or stress-test within boundary.

Translate results rather than only reporting them. After giving a metric, curve trend, ranking, or statistical result, state what it means for the governing mechanism and whether the relation is monotonic, nonlinear, threshold-like, staged, or condition-dependent.

For each major result subsection, lead with the central answer, then use figures, tables, and metrics to substantiate it. Avoid organizing the section as a catalogue of figures.

Subsection opening pattern:

`To evaluate [question/indicator], [test/model/comparison] was conducted using [evidence source].`

### Discussion

Use:

`central finding -> why evidence supports it -> relation to prior work or design practice -> tested conditions -> practical use`

Discussion should not repeat every figure. It should explain the supported mechanism, relevant comparison, and meaning under the tested conditions.

Keep negative-result and limitations commentary in working notes instead of inserting it into ordinary Discussion prose.

### Conclusion

Use:

`contribution -> decisive evidence -> implication -> boundary`

Each numbered conclusion should contain one claim only. Do not add new data or references.

## Paragraph Flow Rule

Each paragraph should have one message:

1. first sentence states the paragraph job;
2. middle sentences provide evidence or reasoning;
3. final sentence states mechanism, implication, transition, or boundary.

If one paragraph contains both literature review and this-study result interpretation, split it.

## Verb Calibration

Use verbs according to evidence strength:

| Verb | Use When |
|---|---|
| `shows/demonstrates` | directly supported by test, FE validation, or model metrics |
| `indicates/suggests` | supported but mechanism or generality remains limited |
| `enables` | the method provides a workflow or capability within stated range |
| `can be used for preliminary...` | design support is bounded and not code replacement |
| `may/could` | implication is plausible but not directly validated |

Avoid `proves`, `guarantees`, `fully solves`, `universally applicable`, and `replaces design codes` unless the evidence is code-level and broad.

## Output Add-On

For SCI稿 using this adapted workflow, include:

```text
Nature-writing式论证架构：
- 一句话主线：
- 文章链条：
- 章节功能：
- 关键证据：
- 不能过度表述：
```

Then continue with the normal `civil-thesis-body-writing` outputs:

- `正文稿/英文稿`;
- `证据与图表对应`;
- `SCI写作QC`;
- `需补充或确认`.
