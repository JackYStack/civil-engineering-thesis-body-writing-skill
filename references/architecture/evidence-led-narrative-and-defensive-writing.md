# Anti-Defensive Writing for Civil-Engineering Manuscripts

Use this guide for thesis and paper drafting, restructuring, compression, and review. Its primary narrative principle comes from [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill): identify the strongest supported contribution and organize the manuscript around it. This is a writing and selection rule, not permission to alter data or invent superiority.

## Technical disclosure takes priority

The rules below target unnecessary defensive narration. They do not authorize hiding material contrary evidence, deleting necessary modeling assumptions, or withholding conditions needed to reproduce or interpret the results. When a reviewer asks about an excluded failure mechanism, sampling boundary, or applicability condition, give the relevant technical statement in the method/discussion passage. Do not require a separate limitations section before stating it. Keep the wording concise and factual; avoid adding generic warnings unrelated to the comment. For review-driven local changes, use `references/workflows/reviewer-driven-revision.md`.

This applies even without a reviewer request. If omitting an adverse finding, qualification, or failure condition would mislead the reader about the claim, retain it in the relevant passage. For language-level cleanup and the distinction between true uncertainty and rhetorical self-defense, use [academic-prose-cleanup.md](../style/academic-prose-cleanup.md). All routes follow this distinction; correct conflicting source rules rather than stacking exceptions. Neither route requires a generic limitations paragraph.

## Choose the strongest supported contribution

1. Identify the research question, engineering object, conditions, comparison basis, indicators, and strongest result in the user's evidence.
2. State one central contribution explicitly: what the work establishes, under what conditions, and with which figures, tables, formulas, or data. Do not leave the advantage for readers to infer.
3. Give each section, paragraph, figure, and experiment a clear role in this argument. For papers, put decisive evidence early. For theses, keep the method and result detail needed for the selected chapter's purpose.
4. If the initial claim does not hold, narrow or rebuild the argument around a contribution that does. Choose an evaluation dimension only when it genuinely reflects the research goal; state the metric and baseline accurately.

## Give experiments an argument role

Use an experiment or analysis to establish the main result, test its mechanism, demonstrate value in the target scenario, or exclude a plausible alternative explanation. Do not write an experimental diary or a catalogue of every intermediate attempt. Retain source data and research records unchanged; select and order material in the manuscript according to its role in the final argument.

## Keep defensive writing out of the body

- Remove gratuitous apologies and self-deprecation. Do not blacklist words such as “仅”: it may express a necessary restriction such as a single loading condition.
- Do not make a non-leading indicator the manuscript's main contest. If it does not support the central claim, first ask whether it must be discussed; then consider a narrower claim, a legitimate goal or condition distinction, a supported trade-off, or a rebuilt argument.
- Keep irrelevant failed attempts and generic self-critique in working notes. Retain negative findings, trade-offs, and scope restrictions needed to interpret the stated results, without turning them into an apologetic narrative or automatically adding a separate section.
- Do not make an unsupported “全面领先” claim, change a baseline silently, or imply that a selected result represents all metrics. The body can emphasize a real advantage while making only the claim that its selected evidence supports.
- Express necessary scope through the positive claim's conditions, object, parameter range, and metric, without appending generic “仍需验证” or self-negating warnings.

## Section checks

- **Abstract and introduction:** lead with the problem, key gap, distinctive response, and strongest supported result. Avoid process chronology, broad background, and premature shortcoming discussion.
- **Methods and experiments:** present the final reproducible route and the purpose of each essential test; keep irrelevant attempts in research records.
- **Results and discussion:** start with the supported answer, then evidence, mechanism, and meaning. Select comparisons that answer the stated research question and preserve their definitions and baselines.
- **Conclusion:** reinforce what was established and why it matters, under the conditions already supported. Retain material qualifications from the results; do not introduce new adverse findings or append a generic future-validation paragraph.

## Revision order when the original story is weak

1. Remove material that does not support the central question.
2. Narrow the claim to what the evidence establishes.
3. Select a meaningful evaluation dimension and state its baseline.
4. Explain a supported goal difference or trade-off where useful.
5. Reorder experiments and figures so the strongest evidence is visible.
6. Rebuild the title, abstract, introduction, and results story if necessary.
7. Keep nonessential process history in working records, but retain material contrary findings and necessary qualifications in the manuscript. A narrower claim must not conceal an essential trade-off.

Final check: Can the reader find the contribution and its supporting evidence quickly, without the text claiming more than the evidence proves?
