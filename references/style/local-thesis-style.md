# Local Civil-Engineering Thesis Style

Use this file as the fast execution guide for Chinese civil-engineering master's thesis body writing. It distills the local big-thesis corpus into rules that can be applied during drafting, revising, and auditing.

For close chapter-level calibration, source tracing, or full corpus examples, use [local-thesis-body-style-corpus.md](local-thesis-body-style-corpus.md). That file is the heavy provenance layer; this file is the lightweight writing layer.

## Source Hierarchy

- `local-thesis-style.md`: quick operational rules; load by default for local thesis body writing.
- `local-thesis-body-style-corpus.md`: merged Word/PDF corpus summary; load only when the user asks to closely follow the local corpus, revise a full chapter, or calibrate PCSP/FE/ML thesis prose against local examples.
- `anti-vague-language.md`: load for wording cleanup when claims contain `显著`, `较好`, `有效`, `重要`, `影响较大`, `价值`, or similar judgement words.
- If this file and the corpus differ, prefer this file for ordinary output structure, and use the corpus for examples, wording tendencies, or source-level justification.

## Core Writing Contract

Every substantive paragraph should answer as many of these slots as the evidence allows:

`研究对象 -> 方法/模型 -> 参数/工况 -> 指标 -> 证据 -> 机理 -> 边界/用途`

Minimum acceptable paragraph density:

- method paragraph: object, method, controlled variables, output indices, assumptions;
- result paragraph: figure/table/data anchor, trend, quantified change or qualitative comparison, mechanism, implication;
- literature paragraph: theme, prior consensus, remaining gap, thesis response;
- design paragraph: input, output, calculation/check route, usable scenario, review boundary.

Do not hide missing evidence behind smooth wording. If a number, figure, table, formula, code condition, or citation is needed but absent, downgrade the claim and list it under `需补充或确认`.

## Body-Prose Meta-Discourse Gate

Write every thesis body paragraph as a direct technical statement about the engineering object, reused model or formula, parameter, method, process, response, evidence, mechanism, or boundary. A cross-reference to another section is valid when it identifies the source of a model, definition, formula, dataset, or method.

Keep chapter-role comparison, anti-duplication defense, and reviewer-facing explanation out of the body. Move them to the writing rationale, outline note, revision report, or response to the supervisor. Do not write or polish variants of:

- `3.2节解决的是……本节解决的是……`;
- `二者章节任务不同/前后承接`;
- `本节不再重复/不再次论证`;
- `不在本节中预设`;
- `本节只规定……` when it merely explains chapter scope.

Rewrite as direct content. For example, use `参数化计算以3.2节建立并验证的模型为基础，按连接状态生成三类算例并记录参数、模式与结果文件。` Do not replace forbidden meta-discourse with a more polished chapter-comparison paragraph.

## Default Chapter Recipes

| Section Type | Recommended Logic | Must Include | Avoid |
|---|---|---|---|
| 绪论/研究背景 | 工程需求 -> 研究对象 -> 关键问题 -> 分主题研究现状 -> 不足 -> 本文内容 | topic-based literature synthesis, numbered gaps, thesis response | long author lists without synthesis |
| 试验研究 | 引言 -> 材料 -> 试件 -> 装置/测点 -> 加载 -> 破坏现象 -> 曲线/指标 -> 机理 -> 小结 | specimen IDs, variables, material properties, measured indices | only describing photos or curves |
| 有限元/数值模拟 | 建模目的 -> 本构/单元/相互作用 -> 边界/加载 -> 验证 -> 参数分析 -> 建议/公式 -> 小结 | assumptions, parameters, validation evidence before expansion | parameter analysis before validation |
| 机器学习/数据驱动 | 数据来源 -> 输入/输出 -> 预处理 -> 模型与调参 -> 评价指标 -> 对比 -> 解释 -> 应用边界 | sample size, feature meaning, metrics, train/test logic, SHAP or sensitivity boundary | treating the model as an unexplained black box |
| 模型应用/设计方法 | 工具/流程先行 -> 输入参数 -> 模型输出 -> 工程后处理 -> 参数调整 -> 复核方式 -> 适用范围 | GUI/function inputs, predicted indices, deflection/capacity checks, FE/code review boundary | claiming replacement of design codes |
| 本章小结 | task recap -> 3-5 numbered evidence-based findings | each finding tied to earlier figures/tables/data | new results not discussed in body text |

## Paragraph Patterns

### Literature Review

Use topic synthesis rather than chronological listing.

Pattern:

`已有研究围绕...开展了...，主要形成了...认识；但针对...条件下的...问题，仍存在...不足。因此，本文从...入手，进一步研究...。`

Rules:

- cite literature for background, classifications, prior mechanisms, methods, standards, and comparison baselines;
- do not cite literature to prove the user's own test, FE, or ML results;
- one paragraph should usually support one technical theme.

### Method

Pattern:

`为明确...对...的影响，本节以...为研究对象，设置...为主要参数，采用...方法获取...指标，并结合...分析其变化规律。`

Rules:

- state why the method is suitable for the question;
- name controlled variables and output indices;
- include assumptions or parameter range when the method leads to design or prediction claims.

### Result

Pattern:

`图/表X给出了...。由图/表可知，随着...变化，...呈现...趋势。其中，...由...变化至...，表明...。其原因在于...，从而导致...。`

Rules:

- first anchor the claim to a figure, table, formula, metric, or explicit data item;
- quantify when data are available; otherwise use restrained qualitative wording;
- separate observation, mechanism, and implication.

### Mechanism

Pattern:

`参数变化 -> 受力路径/剪力传递/界面滑移/裂缝发展/材料损伤变化 -> 刚度、承载力、延性、变形或组合度指标变化`

Rules:

- do not stop at `这是由于...`; write the intermediate mechanical link;
- connect micro/connector/interface behavior to member-level response;
- keep mechanism strength consistent with available evidence.

### Design Implication

Pattern:

`在...参数范围内，...可用于...的初步评估/参数筛选/复核前判断；工程应用时仍需结合...进行校核。`

Rules:

- use `初步设计`, `快速评估`, `参数化分析`, `辅助决策`, `复核前判断`;
- avoid `直接用于规范设计`, `替代试验`, `替代有限元`, `完全实现反向设计` unless the user gives code-level validation and a real optimization algorithm.

## PCSP / FE / ML Specific Rules

- For PCSPs, distinguish direct structural responses from DCA. Direct responses include initial stiffness, ultimate capacity, service-load deflection, moment, slip, strain, crack development, and failure mode. DCA explains composite action and should not be written as a full replacement for strength or serviceability checks.
- For connector effects, interpret through shear transfer, wythe slip restraint, connector stiffness/capacity, connector distribution density, damage evolution, and thermal-structural trade-off when relevant.
- For insulation thickness, wythe thickness, opening, boundary condition, or span changes, connect geometry to section stiffness, load path, neutral-axis behavior, slip demand, or local stress concentration.
- For FE chapters, always write validation before parameter expansion. Use load-displacement curves, peak-load error, initial stiffness, failure mode, crack/damage pattern, and slip trend as validation anchors.
- For ML chapters, keep model claims tied to dataset boundaries. Report sample size, features, outputs, model families, tuning strategy, train/test split or cross-validation, and metrics such as R2, MAE, RMSE, MAPE, A0.1, or MBE when available.
- For SHAP, write it as explanation and parameter-guidance evidence. It can support why a parameter matters and how to adjust it; it is not by itself proof of causality.
- For GUI or assisted-design workflows, write the route as `输入设计参数 -> 预测DCA或响应指标 -> 工程后处理 -> 参数调整 -> FE/规范复核 -> 输出建议`.

## Reusable Sentence Frames

Use these as adaptable frames, not fixed boilerplate:

- `针对上述问题，本文主要开展以下几个方面的研究。`
- `本章以...为研究对象，围绕...开展试验/模拟/预测分析。`
- `在验证模型可靠性的基础上，进一步开展...参数分析。`
- `由图X可以看出，...随...的增加呈现...变化趋势。`
- `表X列出了...结果，其中...误差为...，说明...。`
- `上述变化主要与...有关，即...改变了...，进而影响...。`
- `需要指出的是，上述结论是在...参数范围和...假定条件下得到的。`
- `工程应用时，该方法可用于...阶段的...判断，后续仍需结合...进行复核。`
- `本章围绕...开展研究，主要得到以下结论：`

## Downgrade or Rewrite These Expressions

Do not leave these expressions unsupported:

| Vague Expression | Rewrite By Naming |
|---|---|
| `具有重要意义` | which design/research step it supports and what problem it reduces |
| `吻合较好` | curve stage, peak error, stiffness trend, failure mode, or crack/damage agreement |
| `显著提高` | compared with what baseline, by how much, in which index |
| `影响较大` | which parameter affects which response and through what mechanism |
| `具有较高预测精度` | R2/MAE/RMSE/MAPE/A0.1/MBE or ranking among models |
| `可为工程应用提供参考` | in what parameter range, for preliminary design, screening, checking, or experiment planning |
| `优化效果明显` | target function, baseline scheme, changed parameter, and improvement indicator |

If the evidence is missing, use restrained wording:

- `在本文数据范围内，模型预测结果表现出较好的稳定性。`
- `该结果表明...可能是影响...的重要因素，仍需结合更多样本或试验进一步验证。`
- `该方法可作为初步筛选工具，不能替代后续有限元分析或规范校核。`

## Quick QC Checklist

Before returning thesis body text, check:

- Does the paragraph name the object, method, parameter, indicator, evidence, mechanism, and boundary where needed?
- Does every result claim point to a figure, table, formula, metric, dataset item, or citation marker?
- Are validation and parameter expansion in the correct order?
- Are DCA, stiffness, capacity, deflection, slip, and failure mode clearly distinguished?
- Are ML/SHAP/GUI claims written as assisted prediction or preliminary design support rather than final code design?
- Are literature citations used for background/method/prior work rather than to replace the user's own evidence?
- Are chapter summaries numbered, evidence-based, and free of new unintroduced results?
- Does the body avoid chapter-role comparison and reviewer-facing explanations while retaining necessary technical cross-references?
- Are vague expressions either quantified, bounded, or moved to `需补充或确认`?

## When to Load the Heavy Corpus

Open [local-thesis-body-style-corpus.md](local-thesis-body-style-corpus.md) only when one of these is true:

- the user asks to merge/use the Word/PDF `正文风格归纳`;
- the task is full-chapter rewriting rather than paragraph-level polishing;
- the user wants close imitation of local big-thesis chapter logic;
- the topic is PCSP, FE, ML, Agent/GUI assisted design, and the draft needs local-corpus calibration;
- you need source-level justification for why a style rule exists.
