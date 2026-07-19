# Local Thesis Paragraph And Phrase Patterns

Use this file for paragraph-level writing, result phrasing, transitions, and anti-vague replacements in local civil-engineering master's thesis style.

## Paragraph Skeletons

### Parameter Analysis Paragraph

```text
为明确 [参数] 对 [研究对象/响应指标] 的影响，本文以 [模型/试件/数据集] 为对象，设置 [参数范围/工况]，对 [指标] 的变化规律进行分析。由图/表 [编号] 可知，随着 [参数] 的增大/减小，[指标] 呈现 [趋势]。其原因在于 [机制解释]。需要指出的是，上述规律是在 [边界条件] 下得到的。
```

### Validation Paragraph

```text
为验证 [模型/方法] 的可靠性，将 [计算结果/预测结果] 与 [试验结果/有限元结果/已有公式] 进行对比。由图/表 [编号] 可见，[峰值/刚度/破坏模式/曲线阶段] 整体一致，[误差或差异] 主要出现在 [阶段/指标]。这说明该方法能够在 [适用范围] 内反映 [关键行为]，但对 [薄弱环节] 仍需进一步校核。
```

### Result-Mechanism Paragraph

```text
由图 [编号] 可以看出，在 [工况] 下，[指标] 随 [变量] 的变化表现为 [趋势]。该现象表明 [直接结论]。从受力机制上看，[机制] 改变了 [传力路径/变形协调/损伤发展/界面滑移]，从而导致 [结果]。
```

### Boundary Paragraph

```text
需要说明的是，上述结论基于 [材料参数/几何尺寸/边界条件/数据范围/模型假定] 得到。对于 [超出范围的情况]，仍需结合 [试验/有限元/规范/工程复核] 进一步验证。
```

## Preferred Expressions

- `为明确...的影响`
- `以...为研究对象`
- `设置...作为主要参数`
- `由图/表...可以看出`
- `整体呈现...趋势`
- `其原因在于...`
- `这说明...`
- `在本文参数范围内`
- `需要指出的是...`
- `仍需结合...进一步验证`

## Vague Expression Downgrades

| Vague wording | Replace with |
|---|---|
| `具有重要工程意义` | `可用于 [具体设计/校核/筛选环节] 中 [具体指标] 的初步判断` |
| `吻合较好` | `[峰值/刚度/曲线阶段/破坏模式] 与 [对比对象] 基本一致，误差为 [数值/范围]` |
| `影响较大` | `[参数] 改变后，[指标] 从 [A] 变化至 [B]，变化幅度为 [数值/比例]` |
| `预测精度较高` | `在 [测试集/验证集] 上，[R2/MAE/RMSE/MAPE] 为 [数值]` |
| `可为工程设计提供参考` | `在 [参数范围] 内，可用于 [初步设计/方案筛选/有限元复核前判断]` |

If data are unavailable, downgrade the sentence and list the missing indicator under `需补充或确认`.

## Avoid

- Do not use multiple judgement adjectives without evidence.
- Do not repeat figure content line by line.
- Do not combine result trend, mechanism, and design recommendation unless each is supported.
- Do not replace a missing value with `显著`, `明显`, or `较好`.
- Do not introduce a new technical term only for stylistic variety.
