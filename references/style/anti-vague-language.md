# Anti-Vague Language Rules

Use this file when drafting, revising, polishing, or auditing Chinese civil-engineering thesis or paper text. The goal is to prevent fluent but empty prose. Prefer a rough sentence with traceable evidence over a smooth sentence with no object, indicator, data, mechanism, or boundary.

## Core Rule

Every key judgement sentence should answer at least four of these six slots:

`研究对象 + 条件/参数 + 指标 + 证据 + 机理 + 边界`

Use all six slots when writing results, conclusions, model validation, design recommendations, or engineering implications.

If a sentence cannot answer the required slots, either:

- rewrite it with the available evidence;
- downgrade the claim strength;
- or move the missing item to `需补充或确认`.

Do not invent values, figures, equations, standards, or references to make a sentence look specific.

## Vague Word Watchlist

These words are allowed only when supported by indicators, evidence, and boundaries:

- degree words: `显著`, `明显`, `较大`, `较高`, `较好`, `良好`, `有效`, `重要`, `复杂`;
- value words: `具有重要意义`, `具有较高价值`, `工程应用价值`, `推广价值`, `参考价值`;
- effect words: `优化效果明显`, `预测效果较好`, `吻合较好`, `验证了可靠性`, `提高了精度`, `改善了性能`;
- method words: `可行可靠`, `准确预测`, `快速设计`, `智能优化`, `有效指导`, `合理反映`;
- broad nouns: `性能`, `规律`, `机制`, `影响`, `作用`, `水平`, `能力`, `效果`.

When these words appear, ask:

- 相对谁？
- 体现在哪个指标？
- 由哪张图、哪张表、哪个公式、哪个误差或哪篇文献支持？
- 在什么参数范围、模型假定或工程条件下成立？

If the sentence cannot answer these questions, revise it.

## Claim Strength Ladder

Choose claim strength from the available evidence.

- Strong evidence with data: use `提高/降低...%`, `误差为...`, `由...变化至...`, `在...范围内`.
- Medium evidence without exact data: use `呈增大趋势`, `变化幅度有限`, `整体上高于/低于`, `基本一致`.
- Weak evidence or missing value: use `可能与...有关`, `可作为初步判断`, `仍需结合...复核`.
- No evidence: do not make the claim; write `缺少...数据，暂不能判断...`.

## Sentence Slot Templates

### Result Sentence

Weak:

`拉结件间距对墙板性能影响较大。`

Better with data:

`在其他参数保持不变时，拉结件间距由...增至...后，墙板...指标由...变为...，变化幅度为...，说明拉结件间距主要通过改变两叶板间剪力传递能力影响整体受力性能。`

Better without data:

`从图X可看出，拉结件间距增大后，墙板...指标整体呈下降趋势，但具体变化幅度仍需结合表X中的承载力和挠度数据进一步量化。`

### Validation Sentence

Weak:

`有限元结果与试验结果吻合较好。`

Better:

`有限元模型得到的荷载-位移曲线在弹性阶段与试验曲线基本一致，峰值承载力误差为...，破坏位置均集中于...，说明该模型能够在本文试件参数范围内反映构件的主要受力响应。`

Without data:

`有限元结果与试验结果在破坏模式和曲线趋势上具有一致性，但由于尚未给出峰值承载力误差和刚度误差，暂不宜表述为“吻合较好”。`

### Engineering Value Sentence

Weak:

`该方法具有重要工程意义。`

Better:

`该方法可在初步设计阶段快速估计...，减少逐一建立有限元模型的工作量；但其适用性仍限定于本文数据集覆盖的...参数范围。`

### Model Performance Sentence

Weak:

`该模型具有较高预测精度和应用价值。`

Better:

`该模型在测试集上的R2、RMSE和MAE分别为...、...和...，误差水平低于...模型，说明其对...与...之间的非线性映射具有较好的拟合能力，可用于本文参数范围内的...初步预测。`

Without data:

`由于尚未给出R2、RMSE、MAE或交叉验证结果，暂不能判断该模型预测精度是否优于对比模型。`

### Design Recommendation Sentence

Weak:

`GUI可为工程设计提供有效参考。`

Better:

`GUI将...输入参数转换为...预测结果，并进一步计算...等设计指标，可用于方案比选和参数敏感性分析；正式工程设计仍需结合规范验算和有限元复核。`

## PCSP-Specific Rewrite Rules

### DCA and Composite Action

Do not write only:

`组合度反映墙板协同工作水平。`

Write:

`组合度用于表征内、外叶板在弯曲或受压过程中共同工作的程度，其变化会影响截面刚度、跨中挠度和极限承载力。本文中应明确采用刚度组合度、承载力组合度，或二者分别讨论。`

### Connector Spacing

Do not write only:

`拉结件间距越大，墙板性能越差。`

Write:

`拉结件间距增大会降低单位长度内的剪力传递能力，使内、外叶板间相对滑移增大，从而降低组合度；该趋势应结合承载力、刚度、挠度或DCA指标进行量化。`

### Connector Stiffness and Capacity

Separate stiffness and capacity:

- `初始刚度` mainly supports service-stage stiffness, slip control, and stiffness DCA.
- `极限承载力` mainly supports ultimate shear transfer, interface failure delay, and capacity DCA.

Do not merge them into a vague `拉结件性能较好`.

### FE Validation

A credible validation sentence should mention at least two:

- load-deflection curve agreement;
- peak load error;
- initial stiffness difference;
- failure mode or damage location;
- strain/slip response;
- applicability range.

### ML Prediction

A credible ML sentence should mention at least two:

- dataset size and source;
- input and output variables;
- train/test or cross-validation setting;
- metrics such as `R2`, `MAE`, `RMSE`, `MAPE`;
- comparison baseline;
- parameter range or extrapolation warning.

### SHAP Interpretation

Do not write:

`SHAP结果有效指导参数优化。`

Write:

`SHAP结果用于识别模型预测中贡献较大的输入参数，并结合结构受力机理判断参数调整方向；该分析解释的是模型在当前数据范围内的预测行为，不等同于独立的因果试验结论。`

### GUI and Assisted Design

Do not write:

`GUI实现了智能设计。`

Write:

`GUI集成参数输入、DCA预测和工程响应后处理，可用于初步方案筛选；筛选结果仍需通过有限元分析、试验结果或规范公式进行复核。`

## SCI Phrase Template Guardrails

SCI phrase templates are allowed only after the technical claim is clear. Do not let English fluency hide missing evidence.

### English Judgement Words

Words such as `significant`, `effective`, `robust`, `promising`, `valuable`, `superior`, `accurate`, `efficient`, and `reliable` must be tied to at least one of the following:

- a metric, such as `R2`, `MAE`, `RMSE`, `MAPE`, peak-load error, stiffness error, or capacity ratio;
- a comparison baseline, such as another model, code formula, specimen group, parameter level, or published result;
- a specific response indicator, such as DCA, deflection, capacity, stiffness, slip, strain, ductility, or failure mode;
- an applicability boundary, such as dataset range, connector type, loading condition, or preliminary design stage.

If none is available, downgrade the claim or move the missing item to `需补充或确认`.

### Template Sentence Failure Modes

Revise these patterns:

- `This method is effective.` -> state which indicator improves or which workflow step it supports.
- `The model shows high accuracy.` -> report metrics and the comparison model or validation setting.
- `The results agree with previous studies.` -> identify the study group, response indicator, and agreement or difference.
- `The GUI is useful for design.` -> state whether it supports preliminary screening, parameter sensitivity analysis, or assisted evaluation, and note required FE/code verification.
- `The proposed approach has broad application prospects.` -> replace with the design stage and parameter range actually covered.

### Figure and Table Sentence Guardrails

Do not use generic figure phrases without a result:

Weak:

`Figure X presents the results of the analysis.`

Better:

`Figure X shows that ... changes from ... to ... as ... increases, indicating that ... within the investigated parameter range.`

If values are unavailable:

`Figure X shows a monotonic increasing/decreasing trend in ..., but the magnitude should be reported before claiming a significant effect.`

### Discussion Sentence Guardrails

Discussion templates must include comparison and boundary.

Weak:

`This finding is consistent with previous studies.`

Better:

`This trend is consistent with connector-based PCSP studies in which increasing shear-transfer capacity reduced wythe slip; however, the present conclusion is limited to the connector type and spacing range considered in this dataset.`

Do not write a causal claim from SHAP alone. SHAP explains model behavior within the dataset; mechanical causality must be supported by structural reasoning, tests, FE results, or literature.

## Section-Specific Checks

### Background and Significance

Avoid policy slogans. Every `意义` sentence should identify:

- the engineering pain point;
- the research object;
- the performance or design issue affected;
- why the current method is insufficient.

### Literature Review

Avoid `研究较多` and `研究不足` without topic boundaries. State:

- which object has been studied;
- which method was used;
- what conclusion is established;
- which parameter, loading condition, connector type, or design method remains insufficient.

### Result Analysis

Do not write a result paragraph without figure/table/equation/data support. If no value is available, explicitly refer to curve trend, failure process, or visual comparison.

### Chapter Summary and Conclusion

Each numbered item should be:

`one claim + one evidence basis + one boundary/implication`

Do not introduce new data, new literature, or unverified engineering recommendations in summaries.

## Output Behavior

When using this skill:

- silently replace vague wording when the missing details are available in the user's material;
- downgrade the claim when only partial evidence is available;
- list the missing evidence under `需补充或确认` when the claim cannot be made defensibly;
- do not add a separate warning for every minor word if the final prose has already been corrected.
