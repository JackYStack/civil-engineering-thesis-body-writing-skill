# Zotero Library Learning Workflow

Use this workflow when the user asks to read the Zotero library, learn from the local paper collection, build a literature-backed writing style, or update this skill using Zotero papers.

The goal is not to dump references into the manuscript. The goal is to convert the user's own Zotero library into reusable writing knowledge:

`library search -> corpus map -> article-structure patterns -> evidence-chain patterns -> claim-level citation directions -> skill update`.

## Default Policy

- Read only unless the user explicitly asks to write notes back to Zotero.
- Prefer Zotero metadata, attachments, notes, tags, and local full text before web search.
- Treat Zotero search results as a source index, not as verified full-text evidence.
- When Zotero is combined with web search, literature-search skills, publisher pages, DOI lookups, or downloaded PDFs, follow [external-source-and-tool-use.md](external-source-and-tool-use.md) to record source/tool, query terms, access status, and reviewed-result boundaries.
- When full text is unavailable through MCP, move to local PDF/TXT extraction, OCR, or nature-reader-style reading before making fine-grained claims.
- When Zotero-xpropel `[zotero_fulltext]` is available or the user asks for full-text corpus learning, follow [zotero-fulltext-corpus-workflow.md](zotero-fulltext-corpus-workflow.md) to extract paper spines, variables, response indicators, evidence anchors, and boundaries.
- Do not cite a Zotero item only because it appears in search results. It must support a sentence-level claim.

## Search Strategy

Start with topic clusters instead of one broad query.

For PCSP / sandwich panel work:

- `precast concrete sandwich panel`
- `insulated concrete sandwich panel`
- `degree of composite action`
- `partial composite action`
- `FRP connector`, `GFRP connector`, `shear connector`
- `flexural performance`, `load-deflection`, `analytical model`
- `finite element`, `parametric study`
- `data-driven`, `machine learning`, `SHAP`, `prediction`

For RC / CFST / structural ML work:

- `machine learning structural engineering concrete prediction`
- `bearing capacity prediction`
- `load-deflection prediction`
- `SHAP structural engineering`
- `finite element reinforced concrete`
- `RC beam column shear flexural damage`

## Corpus Map

Create a corpus map before updating writing rules:

| Cluster | Source Category | Typical Evidence | Writing Use |
|---|---|---|---|
| Review/background | review papers, state-of-the-art papers | classification, field gap, research trend | introduction, research status |
| Connector tests | shear/pull-out/direct shear papers | connector stiffness/capacity, failure mode, spacing/material effect | mechanism, parameter rationale |
| Panel tests | flexural/axial/eccentric panel papers | load-deflection, DCA, failure mode, bearing capacity | results comparison, design implication |
| FE/analytical models | nonlinear FE, beam-spring, load-deflection model | assumptions, validation, parametric variables | methods, model validation, discussion |
| ML/data-driven papers | prediction, SHAP, surrogate models | features, metrics, model comparison, interpretability | ML methods, application, limitations |

## Article-Structure Learning

Learn structure from the papers in the same way nature-skills learn article architecture:

1. Identify the paper's one-sentence argument:
   `object -> bottleneck -> method -> evidence -> implication -> boundary`.
2. Map section jobs:
   `abstract`, `introduction`, `methods`, `results`, `discussion`, `conclusion`.
3. Extract result paragraph moves:
   `figure/table -> indicator -> trend -> quantified comparison -> mechanism -> boundary`.
4. Extract citation function:
   background, gap, method, comparison, boundary.
5. Transfer only the writing move, not the paper's wording, data, or conclusion.

## Skill Update Rules

When Zotero reading is used to update this skill, update the appropriate file:

| Finding Type | Update File |
|---|---|
| article structure or full-paper argument pattern | `architecture/nature-writing-adapted-sci-workflow.md` or `style/local-paper-style.md` |
| thesis chapter pattern | `sections/chapter-templates.md` or `style/local-thesis-style.md` |
| claim-level citation direction | `workflows/citation-workflow.md` |
| full-text corpus extraction rule | `workflows/zotero-fulltext-corpus-workflow.md` |
| target-journal exemplar pattern | `workflows/target-journal-polish-workflow.md` |
| vague language or review risk | `style/anti-vague-language.md` or `style/style-and-qc.md` |
| reusable prompts | `examples/use-case-templates.md` |
| library profile or learned corpus map | `examples/zotero-corpus-profile.md` |

## Output Format

For a Zotero-learning run, output or save:

1. `Zotero检索概况`: queries, result counts, major clusters, attachment/full-text status.
2. `文献谱系图`: topic clusters and representative items.
3. `写作结构模式`: article or chapter moves learned from the corpus.
4. `引用功能建议`: which papers support background, gap, method, comparison, or boundary claims.
5. `外部来源记录`: only when Zotero is supplemented by external tools, list source/tool, query/filter, reviewed count, selected DOI/URL/path, and access status.
6. `skill更新建议/已更新文件`: exact reference files changed.
7. `限制`: metadata-only items, missing full text, OCR needs, or unverified support.
