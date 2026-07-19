# Zotero Fulltext Corpus Workflow

Use this workflow when the user explicitly asks to use Zotero-xpropel `[zotero_fulltext]`, read Zotero full text, learn from the paper library at the full-text level, or migrate full-text corpus findings into `civil-thesis-body-writing`.

This workflow adapts nature-skills-style paper reading to civil-engineering thesis and paper writing. The goal is not to summarize every paper. The goal is to convert local full text into reusable writing knowledge:

`fulltext search -> paper structure extraction -> variable/indicator extraction -> claim-evidence-boundary map -> citation candidates -> skill update`.

Before using Zotero indexed text, OCR output, or PDF-derived text as evidence, run [pdf-extraction-and-fulltext-qc.md](pdf-extraction-and-fulltext-qc.md). Mark Zotero index, OCR, equations, tables, and figure-derived evidence with confidence levels before treating them as citation support.

## Default Policy

- Prefer Zotero full text and local TXT/MD/PDF-derived text over metadata-only records.
- Use `zotero_search` to find candidates, then `zotero_fulltext` to inspect selected items.
- Start with a focused corpus of 5-20 highly relevant papers unless the user asks for full-library mapping.
- Treat partial fulltext snippets as sampling evidence. Mark them as `全文片段抽样` if the entire paper was not reviewed.
- Do not copy sentences, tables, captions, or conclusions from source papers into the user's manuscript.
- Do not cite a paper only because its title or abstract is relevant. Citation support must be claim-level.
- Follow [external-source-and-tool-use.md](external-source-and-tool-use.md) for source/tool records, access boundaries, and output control.

## When to Use `zotero_fulltext`

Use fulltext reading for:

- building a local literature corpus profile;
- extracting thesis/paper writing style from local examples;
- checking whether a source supports a specific sentence;
- identifying variables, parameters, specimen designs, model inputs, response indicators, and applicability boundaries;
- comparing how similar papers organize introduction, methods, results, discussion, and conclusion;
- updating this skill from actual local papers rather than general memory.

Do not use fulltext reading when:

- the user only asks for quick metadata;
- the paragraph can be revised using user-provided evidence without external support;
- the paper is unrelated to the requested research object or writing task.

## Search and Sampling Strategy

Use topic-cluster queries instead of one broad query.

For PCSP / sandwich wall panels:

- `precast concrete sandwich panel degree composite action connector`
- `insulated concrete sandwich panel load deflection analytical model partially composite`
- `BFRP 连接件 混凝土 夹心墙板`
- `GFRP connector sandwich panel flexural performance`
- `machine learning sandwich panel DCA prediction`

For structural ML / RC / CFST:

- `machine learning reinforced concrete shear strength SHAP`
- `CFST load strain prediction ensemble learning`
- `RC column damage prediction graph neural network`
- `remaining capacity corrosion concrete machine learning`

Sampling priority:

1. local full text available as MD/TXT;
2. full text available through Zotero index;
3. local PDF requiring OCR only if the paper is essential;
4. metadata-only records for discovery only.

## Paper Structure Extraction

For each selected fulltext item, extract only the fields needed for writing:

| Field | What to Extract |
|---|---|
| Source ID | Zotero key, title, year, source status |
| Research object | Component, material, connector, model, dataset |
| Bottleneck | What engineering or modelling problem the paper addresses |
| Method route | Experiment, FE, analytical model, ML, design formula, SHAP/GEP, etc. |
| Variables | Geometry, material, connector, loading, model input variables |
| Response indicators | Load-deflection, cracking load, ultimate load, stiffness, DCA, slip, strain, ductility, error metrics |
| Evidence anchors | Figures, tables, equations, specimens, validation cases, parameter study |
| Key bounded claims | Claims that can be supported by the inspected full text |
| Boundary | Parameter range, test setup, model assumptions, data source, loading condition |
| Writing use | Background, gap, method, comparison, result-discussion pattern, or style learning |

## Nature-Skills-Style Article Spine

For each paper, identify the one-sentence argument:

```text
In [object/problem], the paper addresses [bottleneck] by [method], supported by [evidence], and limited to [boundary].
```

Then map paragraph/section jobs:

- `Introduction`: field demand -> object-specific contradiction -> prior work clusters -> remaining gap -> study response.
- `Methods`: design need -> specimen/model/data -> variables -> procedure -> evaluation indicators.
- `Results`: figure/table -> indicator -> trend -> quantified comparison -> mechanism -> boundary.
- `Discussion`: central finding -> relation to prior work/design practice -> uncertainty -> engineering use.
- `Conclusion`: one claim per item, each tied to evidence and boundary.

Transfer the move, not the wording.

## PCSP Variable Extraction Rules

When reading PCSP papers, extract variables in these groups:

| Group | Examples | Writing Function |
|---|---|---|
| Geometry | span, panel length/width/thickness, inner/outer wythe thickness, insulation thickness | model input, applicability boundary |
| Materials | concrete strength, elastic modulus, reinforcement grade, FRP/GFRP/BFRP properties, XPS/EPS properties | method reproducibility, FE/analytical model |
| Connectors | material, type, shape, diameter, spacing, number, inclination, embedment, rib width, layout zone | DCA, shear transfer, thermal bridge discussion |
| Loading/boundary | four-point bending, six-point bending, simple support, pure bending region, loading rate | result comparability and limitation |
| Response | cracking load, peak/ultimate load, initial stiffness, midspan deflection, slip, strain, failure mode, DCA, ductility | results and conclusions |
| Data-driven fields | sample count, feature list, model candidates, metrics, SHAP/GEP, train/test split | ML section and application boundary |

## DCA-Specific Extraction Rules

When a paper discusses degree of composite action, record:

- DCA type: stiffness, displacement, strain, load/capacity, neutral-axis, design DCA, or model-predicted DCA;
- calculation basis: stiffness, deflection, strain, moment, ultimate load, connector layout, or ML prediction;
- loading stage: elastic, cracking, service, yielding, ultimate;
- intended use: deflection/serviceability, capacity/strength, method comparison, design parameter screening, or model output;
- limitations: required measurements, assumptions, connector type, loading condition, and whether DCA is calculated after testing or predicted during design.

Never write DCA as a single context-free constant when the source distinguishes stiffness-stage and capacity-stage behavior.

## Support Grades for Fulltext Corpus

Use these grades before inserting citations:

| Grade | Meaning |
|---|---|
| `全文强支撑` | Inspected full text directly supports the exact claim. |
| `全文部分支撑` | Full text supports part of the claim but not all variables, methods, or boundaries. |
| `摘要支撑` | Abstract supports broad background only; do not use for detailed mechanism or comparison. |
| `元数据仅发现` | Title/metadata found the paper; not enough for citation support. |
| `不建议引用` | Related topic but does not support the claim. |

## Corpus Report Output

Save a report under `analysis/` for substantial runs:

```text
Zotero全文语料学习调查报告_YYYY-MM-DD.md
```

Minimum report sections:

1. `检索与读取范围`: queries, result counts, sampling rule.
2. `全文样本文献索引`: Zotero key, title, year, source status, characters/read boundary, writing value.
3. `结构化规律`: article spine, section moves, evidence chain.
4. `参数变量谱系`: variables and indicators found.
5. `可迁移规则`: exact skill files that should be updated.
6. `边界说明`: fulltext snippets vs complete review, metadata-only limits, missing OCR/full text.

## Skill Update Targets

After fulltext learning, update only the relevant files:

| Finding | Update File |
|---|---|
| fulltext corpus workflow or Zotero reading procedure | `workflows/zotero-fulltext-corpus-workflow.md` |
| source/citation support grades | `workflows/citation-workflow.md` |
| local corpus profile and paper clusters | `examples/zotero-corpus-profile.md` |
| prompt templates | `examples/use-case-templates.md` |
| article spine / nature-writing transfer | `architecture/nature-writing-adapted-sci-workflow.md` |
| thesis chapter chain | `sections/chapter-templates.md` or `style/local-thesis-style.md` |
| anti-vague rules learned from weak claims | `style/anti-vague-language.md` |

## Output for User

When this workflow is used, return:

1. `Zotero全文检索概况`
2. `全文样本文献索引`
3. `参数变量谱系`
4. `可迁移写作规则`
5. `已更新/建议更新文件`
6. `边界与需确认`
