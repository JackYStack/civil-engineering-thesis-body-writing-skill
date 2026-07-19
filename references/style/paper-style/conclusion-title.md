# Conclusion, Title, And Contribution Style

Use this guide for paper conclusions, titles, highlights, contribution statements, and thesis-to-paper adaptation.

## Conclusion Pattern

Conclusions should answer the paper's central question through a small number of evidence-backed findings. A useful structure is:

`method validity -> main response findings -> mechanism/parameter insight -> design/application boundary`

Each conclusion item should contain:

- the object or condition;
- the indicator or response;
- the evidence anchor, such as test, FE, dataset, model metric, figure, or formula;
- the engineering meaning;
- the boundary if the statement could otherwise be overgeneralized.

Do not use the conclusion to introduce new mechanisms, new citations, or new design claims that were not established in the results.

## Avoid Abstract Repetition

The abstract previews the study. The conclusion extracts what has been learned. To avoid repetition:

- Abstract: why the study was done, how it was done, and what headline result was obtained.
- Conclusion: what the evidence proves, how the key parameters behave, and where the method can be used.

If the conclusion reads like a reordered abstract, rewrite each item around one result indicator.

## Title And Highlight Rules

A title should contain the object and the method or central response, not a slogan. Good technical titles normally include:

`object + method/design route + response indicator`

Keep the title narrow enough that the paper can defend it. Avoid titles that imply universal design, full automation, complete optimization, or code-level applicability unless the study truly provides that evidence.

Highlights should be even more specific:

- one highlight for the method or workflow;
- one for the strongest quantitative or comparative result;
- one for the mechanism or design implication;
- one for the boundary or application path when needed.

Do not repeat the same claim with different wording across all highlights.

## Thesis-To-Paper Adaptation

When compressing a thesis chapter into a paper:

1. Select one central question.
2. Keep only the experiments, simulations, formulas, or ML results that answer that question.
3. Move general theory, lengthy software operations, and broad background out of the main paper unless they are necessary for reproducibility.
4. Convert chapter summaries into result-driven conclusions.
5. Replace thesis-style "research contents" with paper-style "contribution and evidence".

The paper should not try to preserve every thesis subsection. It should preserve the strongest argument chain.

## Chinese Technical-Paper Style

For Chinese technical papers, maintain a formal and restrained style:

- prefer "结果表明" only when followed by the specific indicator and trend;
- prefer "可用于初步判断/参数筛选/设计复核前评估" over "可指导工程应用";
- prefer "在所研究参数范围内" when the dataset or model is limited;
- avoid stacking "具有重要意义、较高价值、显著优势" without evidence;
- keep symbols, abbreviations, figure numbers, and terminology consistent before English translation.

## Contribution Boundary

Contribution claims should be calibrated:

- If the paper proposes a calculation workflow, state which outputs it calculates and what verification supports it.
- If the paper proposes a prediction model, state the feature space, response indicators, performance metrics, and validation boundary.
- If the paper proposes an optimization route, distinguish parameter screening from true inverse design or automated optimization.
- If the paper proposes a design tool, state whether it is for preliminary design, comparison, or code-level design.

This boundary discipline is often the difference between a strong paper and a reviewer comment saying the claim is overstated.
