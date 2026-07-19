# Claim Evidence Boundary

Use this guide whenever a sentence makes a technical judgement, explains a mechanism, cites literature, interprets a result, proposes a design use, or summarizes a conclusion.

## Key Sentence Slots

For each important judgement sentence, try to fill these slots:

```text
research object -> condition/parameter -> indicator -> evidence -> mechanism -> boundary
```

Not every sentence needs all six slots, but a paragraph-level claim should be traceable to them. If four or more slots are missing, the sentence is probably vague.

## Own Evidence First

Claims about this study should first point to user-owned evidence:

- experiments: specimen ID, loading condition, observed failure mode, curve stage, crack/slip/strain feature, peak load, stiffness, ductility, or displacement;
- finite element analysis: validation case, mesh/model assumption, constitutive model, boundary condition, peak error, curve agreement, damage pattern, stress/strain/slip distribution;
- machine learning: dataset size, input variables, output indicators, train/test split, model family, metrics such as R2, MAE, RMSE, MAPE, SHAP ranking, applicability range;
- design/application: formula chain, DCA value, stiffness/capacity conversion, deflection or ultimate capacity calculation, GUI output, verification route.

External literature should not replace these sources for original results. Use literature for background, method origin, comparison, standards, or boundary discussion.

## Citation Support Test

Each citation marker must answer:

- Which exact sentence does this source support?
- Does the source support the claim, not only the topic or keyword?
- Is the source local full text, local record, official page, DOI metadata, abstract-only, or network-only?
- Is the citation being used for background, method, formula, comparison, standard, or boundary?
- Is a temporary marker such as `[R1]` matched to a candidate list entry?

Flag a citation if:

- one marker covers several unrelated claims;
- the source title sounds relevant but specimen type, method, parameter range, or conclusion does not match;
- network-only metadata is presented as verified full-text evidence;
- the paragraph cites external literature for a result that should cite this study's figure, table, formula, or dataset.

## Vague Judgement Repair

The following words are allowed only when they are supported by indicators, baselines, and boundaries:

- `显著`, `明显`, `较好`, `较高`, `有效`, `重要`, `价值`, `影响较大`, `吻合较好`, `提供参考`;
- English equivalents such as `significant`, `effective`, `robust`, `valuable`, `promising`, and `good agreement`.

Repair patterns:

| Weak Claim | Repair Direction |
|---|---|
| `该方法具有重要工程意义。` | Name the design step, performance indicator, parameter range, and limitation. |
| `有限元结果与试验结果吻合较好。` | State curve stage, peak-load error, failure mode, strain/slip comparison, and mismatch if present. |
| `拉结件间距影响较大。` | State the affected indicator, baseline spacing, direction, magnitude if available, and mechanism. |
| `模型具有较高预测精度。` | State test-set metrics, comparison model, target variable, and data range. |
| `GUI 可为工程设计提供参考。` | State it supports preliminary design, rapid screening, parameter adjustment, or verification preparation, not code-level replacement. |

## Mechanism Check

A mechanism sentence should explain a path, not only restate the trend.

Weak:

```text
随着拉结件间距增大，墙板性能降低。
```

Better direction:

```text
随着拉结件间距增大，单位长度内可传递的界面剪力降低，内外叶板协同变形能力减弱，因此截面整体抗弯刚度或承载力随之降低。
```

When no mechanism is proven, downgrade:

```text
该趋势可能与...有关，仍需结合更多试件或参数分析验证。
```

## Boundary Check

State boundaries when claims concern:

- specimen type, connector type, material grade, reinforcement ratio, geometry, or loading mode;
- FE constitutive model, contact setting, mesh sensitivity, boundary condition, or validation range;
- ML dataset coverage, extrapolation, feature space, model uncertainty, or target distribution;
- GUI/design workflow, code verification, safety factor, serviceability state, or ultimate limit state.

Boundary language:

- `在本文参数范围内`;
- `对于采用...连接件的 PCSP`;
- `在所建立有限元模型假定下`;
- `基于当前数据集覆盖范围`;
- `可用于初步筛选，工程应用仍需结合规范、试验或有限元复核`.

## Output For Formal Audits

When reporting claim problems, use traceable wording:

| 编号 | 问题类型 | 原句/位置 | 缺失槽位 | 建议处理 |
|---|---|---|---|---|
| C1 | evidence | ... | evidence, baseline | Add figure/table/metric or downgrade claim. |
| C2 | boundary | ... | boundary | Limit to parameter range and validation condition. |
| C3 | citation | ... | sentence-level support | Replace citation or mark as background-only. |
