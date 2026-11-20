# SCI Writing Principles for Civil-Engineering Papers

Use this reference for independent journal/SCI manuscripts, English abstracts, introductions, Results and Discussion, conclusions, or bilingual logic checks. It does not support converting a thesis/chapter into a journal article.

Do not use this file as a general phrasebank. Its purpose is to make the manuscript argument clear before wording is polished.

If the user asks for target-journal polishing, named-journal matching, downloading/learning exemplars, full-manuscript journal adaptation, or whole-paper comparison against accepted papers, use [target-journal-polish-workflow.md](../workflows/target-journal-polish-workflow.md) first. This file then supports the section-level SCI logic and language checks.

If the user asks for SCI投稿稿 to refer to `nature-writing`, or the task involves full English manuscript argument rebuilding, use [nature-writing-adapted-sci-workflow.md](../architecture/nature-writing-adapted-sci-workflow.md) first. It adapts `nature-writing` article architecture to civil-engineering evidence and boundary requirements.

## Argument Map First

Before drafting a paper-style or SCI-style section, identify:

- `central question`: the specific engineering or scientific problem;
- `main claim`: the claim, hypothesis, model capability, or design conclusion the section must support;
- `evidence`: figures, tables, equations, datasets, validation metrics, tests, FE results, or literature;
- `variables`: design parameters, material properties, model inputs, or output indicators;
- `boundary`: specimen type, connector type, loading condition, parameter range, model assumption, or dataset coverage;
- `reader risk`: what a reviewer may question first, such as novelty, reproducibility, extrapolation, weak comparison, or unsupported design implication.

For introductions, literature reviews, methods, and Results and Discussion, also apply the phenomenon-mechanism-condition check in [phenomenon-mechanism-condition-framework.md](../architecture/phenomenon-mechanism-condition-framework.md). A strong SCI argument should not only say "few studies considered X"; it should show what observed puzzle exists, what mechanism may explain it, and under what condition the mechanism changes.

For full paper drafting, keep a restrained storyline contract: the introduction raises one core contradiction, methods provide the route map, results answer the contradiction with evidence, and discussion states what remains bounded or unresolved. This should guide structure, not produce dramatic or promotional wording.

If the user only gives a topic without data, figures, model metrics, or intended conclusions, first output `待补证据清单` instead of drafting fluent but unsupported SCI prose.

## Section Functions

### Title

The title should identify the object and the main method or problem. Avoid broad titles that hide the contribution.

Good title slots:

`object + key method/indicator + application/problem`

### Abstract

Treat the abstract as a compressed mini-paper:

`problem -> method -> object/data -> variables -> key quantified results -> contribution/boundary`

Must include:

- research object;
- method or workflow;
- data source or sample scale when relevant;
- main inputs/variables and output indicators;
- key quantitative or directional findings;
- bounded use, such as preliminary design, parameter screening, model validation, or assisted evaluation.

Avoid:

- long background;
- vague value claims such as `important`, `effective`, or `promising` without metrics;
- introducing a design replacement if the work only supports preliminary evaluation.

### Introduction

The introduction should introduce this manuscript, not the whole discipline.

Prefer starting from a puzzle or technical contradiction before naming the gap. Use five moves:

1. engineering demand or field context;
2. technical contradiction, counter-intuitive trend, or unsolved design problem;
3. grouped prior work as a dialogue among explanations, with references serving specific claims;
4. unresolved mechanism or condition;
5. precise gap and present study.

Keep background only if it helps the reader understand the manuscript's problem. Do not write a chronological literature list.

### Methods

Report enough detail for interpretation and reproducibility.

- Experimental paper: `specimen design -> materials -> test setup -> instrumentation -> loading protocol`.
- FE paper: `model assumptions -> constitutive laws -> elements/mesh -> contact/interface -> boundary/loading -> validation`.
- ML/data-driven paper: `dataset -> input/output variables -> preprocessing -> model candidates -> metrics -> validation/tuning -> interpretation/application`.

Avoid routine equipment description unless it changes the interpretation of results.

For each major design choice, explain why it is needed. Link specimens, variables, model inputs, metrics, evaluators, or validation routes to the mechanism or condition being tested. If the method controls bias or avoids an alternative explanation, say so briefly.

At the section level, methods should function as a route map: the reader should understand which step validates the platform, which step isolates the parameter/mechanism, and which step supports application or boundary assessment.

### Results

Results paragraphs should be organized by response indicator:

`figure/table evidence -> trend -> quantified comparison -> mechanism -> implication`

Prefer indicators such as failure mode, load-deflection response, slip, strain, stiffness, DCA, capacity, prediction error, or sensitivity ranking.

Do not only report statistics or model metrics. Translate the data into the claim it supports: which indicator changed, relative to what baseline, what mechanism this implies, and whether the relation is linear, nonlinear, threshold-like, staged, or condition-dependent.

For major findings, state the central answer before giving secondary numbers. Use figures and tables to substantiate the answer, not as the paragraph's only organizing logic.

### Discussion

Discussion is not repeated results and not a literature review. It should explain:

- why the result occurs;
- how it compares with representative studies, formulas, standards, or mechanisms;
- where the supported result applies.

Do not write only `the results are consistent with previous studies`. State which studies, which result, which indicator, and whether differences exist.

Keep unrelated self-critique and generic warnings in working notes. Retain adverse findings, assumptions and scope conditions that materially affect the claim in the relevant Discussion/Methods passage. State the object, conditions and metric directly; narrow unsupported claims rather than hiding contrary evidence. A separate limitations section is not required.

### Conclusion

Use concise numbered conclusions. Each item should be:

`one claim + evidence basis + boundary/implication`

Do not add new results, new references, or unverified design recommendations in conclusions.

## Citation Functions

For SCI-style text, each citation should have a visible job:

- `background`: supports engineering demand, object definition, or application context;
- `gap`: supports the claim that existing studies lack a method, parameter range, loading condition, or design workflow;
- `method`: supports models, formulas, algorithms, standards, or evaluation metrics;
- `comparison`: compares the user's result with published experimental, FE, analytical, or ML findings;
- `boundary`: supports applicability limits, parameter ranges, uncertainty, or assumptions.

Do not cite a source simply because the title is related. A citation must support the exact sentence or claim.

## English Draft Guardrails

For Chinese-to-English or English manuscript tasks:

- first lock terms, variables, indicators, and claim boundaries;
- use clear subject-verb structure and short sentences;
- move from known information to new information;
- prefer engineering-journal clarity over decorative phrasing;
- do not translate Chinese vague praise into stronger English claims;
- reserve `significant`, `effective`, `robust`, `promising`, `superior`, and `valuable` for claims with metrics, baselines, or boundaries.

For Nature-leaning or high-impact English polishing, use this file to fix the technical logic first, then use `nature-polishing` for final language style when requested.

## Submission-Oriented QC

Before returning an SCI-style draft, check:

- Does the title expose the object and core method/problem?
- Does the abstract contain problem, method, object/data, variables, key results, and boundary?
- Does the introduction narrow from field context to the manuscript's exact gap?
- Are methods reproducible at the level needed for peer review?
- Does every results paragraph point to a figure, table, metric, or dataset?
- Does the discussion explain the supported mechanism, comparison, and conditions without defensive limitations prose?
- Does the paper keep one core contradiction from introduction through discussion, rather than switching to unrelated claims?
- Are conclusions supported by earlier results?
- Are figure/table titles, variable names, units, and references consistent?
- Are all citations assigned a function rather than used as decoration?
- Are cover letter, author declarations, conflicts of interest, and target-journal formatting outside the body draft unless the user explicitly asks for submission materials?

## Output Behavior

For SCI-style or paper-style drafting, add this block before the draft when useful:

```md
论点地图：
- 中心问题：
- 本文主张：
- 证据来源：
- 关键变量：
- 主要图表/公式：
- 适用边界：
- 审稿风险：
```

For Chinese-to-English checking, use:

```md
逻辑校准：
- 术语：
- 主语与研究对象：
- 指标与数据：
- 需要降级的表述：
- 边界：
```

If evidence is missing, list the missing item under `需补充或确认` instead of inventing details.

