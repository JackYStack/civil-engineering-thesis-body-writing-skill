# Chapter Templates for Civil Engineering Master's Thesis Body Text

Use this reference when drafting full sections or chapters. Adapt the templates to the user's actual outline and evidence.

## 1. 绪论

### 1.1 研究背景与意义

Paragraph jobs:

1. Engineering background and application scale.
2. Existing structural/material problem.
3. Why the problem matters for safety, serviceability, durability, carbon reduction, construction efficiency, or design.
4. Introduce the specific research object.
5. State why the thesis studies this object.

Recommended flow:

`工程应用需求 -> 现有构件/材料不足 -> 目标对象的潜在优势 -> 尚待解决的关键问题 -> 本文研究必要性`

Avoid:

- broad policy slogans without connection to the research object;
- saying "具有重要意义" without specifying the mechanical/design issue.

### 1.2 国内外研究现状

Group literature by technical topic, not by year:

- component mechanical performance;
- connector/shear transfer mechanism;
- material properties;
- FE or analytical modelling;
- data-driven prediction or design method.

Each literature paragraph should use:

`topic sentence -> representative studies -> shared conclusion -> remaining gap tied to this thesis`

Useful endings:

- `然而，现有研究多集中于...，针对...条件下...的研究仍相对不足。`
- `上述研究为...提供了基础，但在...方面仍缺乏可直接用于...的分析方法。`

### 1.3 本文主要研究内容

Use numbered items. Each item should include object, method, parameter, output, and purpose.

Pattern:

`（1）...研究：设计/建立/采集...，以...为主要参数，分析...，为后续...提供依据。`

Do not overstate results here. Keep it as task preview.

## 2. 材料与试验章节

Default section order:

1. 引言
2. 材料性能
3. 试件设计与制作
4. 试验装置与测点布置
5. 加载制度
6. 试验现象与破坏模式
7. 结果分析
8. 本章小结

### 试件设计

Must include:

- specimen naming rule;
- controlled variables;
- fixed parameters;
- dimensions, reinforcement, connector layout, material strength;
- why the parameter values are chosen.

Pattern:

`本章共设计...个试件，以...为主要变化参数，其余参数保持一致。试件编号中...表示...。参数取值主要依据...，同时考虑...。`

### 试验结果分析

Use one indicator per paragraph:

- failure process;
- load-displacement curve;
- strain distribution;
- stiffness degradation;
- ductility;
- energy dissipation;
- bearing capacity.

Pattern:

`图X给出了...曲线。可以看出，...阶段曲线呈现...特征；当荷载达到...时，...；随后...。与试件A相比，试件B的...提高/降低...，说明...。`

Mechanism sentence:

`其主要原因在于...，使得...，进而影响...。`

## 3. 有限元/数值模拟章节

Default section order:

1. 引言
2. 建模平台与基本假定
3. 材料本构模型
4. 单元类型与网格划分
5. 接触、约束与边界条件
6. 加载方式与求解设置
7. 模型验证
8. 参数分析
9. 设计公式/工程建议 if applicable
10. 本章小结

### Model Description

Write reproducibly:

`本节采用...软件建立...模型。混凝土/钢筋/连接件分别采用...单元模拟；...之间采用...相互作用；边界条件与试验保持一致。`

Do not write only "建立有限元模型". Name the material laws, element types, contact assumptions, mesh, and loading.

### Model Validation

Validation must compare at least one of:

- load-displacement curves;
- peak capacity;
- initial stiffness;
- failure mode;
- strain response;
- crack/damage pattern.

Pattern:

`图X和表X分别给出了...对比。整体来看，模拟曲线与试验曲线在...阶段吻合较好；峰值承载力误差为...。破坏模式方面，模拟得到的...与试验观察到的...基本一致，说明模型能够较好反映...。`

### Parameter Analysis

Use control-variable logic:

`在验证模型可靠性的基础上，选取...作为变化参数，其余参数保持不变，分析...对...的影响。`

Each parameter subsection:

`parameter definition -> trend -> quantitative comparison -> mechanism -> design implication/boundary`

## 4. 机器学习/数据驱动章节

Default section order:

1. 数据来源与样本构建
2. 输入特征与输出指标
3. 数据预处理
4. 模型选择与训练
5. 评价指标
6. 模型性能对比
7. 可解释性分析
8. 工程应用

### Dataset

Must state:

- source: experiment, FE simulation, literature, hybrid;
- sample number;
- variables and ranges;
- output labels;
- train/test split or cross-validation;
- normalization or feature selection.

Pattern:

`为建立...预测模型，本文构建了包含...个样本的数据集。输入特征包括...，输出指标为...。各参数取值范围见表X。`

### Model Comparison

Avoid praising one model without evidence.

Pattern:

`由表X可知，...模型在...指标上表现最优，其R²为...，RMSE为...。与...相比，...误差降低...，说明该模型对...非线性映射关系具有较好的拟合能力。`

### SHAP/Interpretability

Separate result from mechanism:

`SHAP结果表明...是影响...的主要特征。结合结构受力机制可知，...会增强/削弱...，从而导致...。`

Do not claim causality beyond the model and mechanics.

## 5. 模型应用/设计方法章节

For GUI or assisted design tools, write tool use before optimization:

1. What tool/workflow is provided.
2. What inputs are required.
3. What the model outputs.
4. How outputs are converted into engineering responses.
5. How SHAP guides parameter adjustment.
6. How selected schemes are verified.

Preferred wording:

`辅助设计`, `快速评估`, `初步设计`, `参数优化支持`, `有限元复核`

Avoid unsupported wording:

`替代规范设计`, `自动完成设计`, `反向设计` unless a true inverse optimization algorithm is implemented.

## 6. 本章小结

Start with a one-sentence chapter task:

`本章围绕...开展了...研究，主要得到以下结论：`

Each numbered item should be claim + evidence + boundary:

`（1）...结果表明，...。在...条件下，...，说明...。`

Avoid:

- repeating the entire method in detail;
- introducing new literature or new data;
- making claims not shown in the chapter.

## 7. 结论与展望

Opening paragraph:

`本文以...为研究对象，围绕...问题，采用...方法开展研究。主要研究工作包括...。`

Numbered conclusions should follow thesis chapters, not random result order.

Research outlook should be honest and bounded:

- limitations from parameter range;
- limitations from specimen number;
- limitations from FE assumptions;
- need for long-term performance, fire, durability, thermal effects, axial load, two-way bending, engineering validation, etc.
