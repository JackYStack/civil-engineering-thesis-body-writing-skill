# SCI Phrase Guardrails

Use this guide as the final paper-style language and reviewer-risk pass. It is especially useful for SCI manuscripts, target-journal polishing, and Chinese-to-English translation prechecks.

## Reviewer View

A reviewer usually asks five questions:

1. What exact engineering problem is being solved?
2. What evidence proves the method or finding?
3. What is new relative to existing methods or design routes?
4. What are the limits of the dataset, experiment, FE model, formula, or tool?
5. Can another researcher reproduce the main logic?

Polished sentences that cannot answer these questions should be rewritten or moved to `需补充或确认`.

## Forbidden Overclaims

Avoid or downgrade these phrases unless the sentence includes comparison baseline, metric, evidence, and boundary:

- "significantly improves";
- "high accuracy";
- "excellent agreement";
- "robust and reliable";
- "universal method";
- "optimal design";
- "important engineering value";
- "can guide engineering practice";
- "fills the gap";
- "fully explains the mechanism".

Safer replacements include:

- "reduced the prediction error relative to...";
- "captured the initial stiffness and peak-load stages";
- "ranked the tested parameter schemes";
- "supported preliminary screening within...";
- "provided a rapid estimate before detailed FE verification";
- "identified the dominant feature under the trained model".

## Evidence-Linked Sentence Test

Before final output, each key sentence should answer at least four of the following:

- object: which member, material, connector, model, dataset, or loading condition?
- condition: under which parameter range, model assumption, or load state?
- indicator: which response or metric?
- evidence: which test, FE result, figure, table, equation, dataset, or citation?
- comparison: relative to which baseline?
- mechanism: why does the trend occur?
- boundary: where does the conclusion stop?

If a sentence answers fewer than four and makes a strong judgment, it is probably too vague for paper style.

## Local Paper Style Quality Check

Check the manuscript at three levels:

- Section level: each section answers a different reader question and does not repeat the same background or method justification.
- Paragraph level: each paragraph has one claim, one evidence anchor, and one engineering interpretation.
- Sentence level: terms, symbols, units, and indicators are stable; no vague praise substitutes for data.

For bilingual or translated manuscripts, check that English wording does not strengthen the original Chinese claim. "Potentially useful for preliminary design" should not become "provides a reliable design method" unless the paper validates that stronger claim.

## Learning From Samples Without Copying

When using local papers, target-journal exemplars, or Zotero full text:

- learn paragraph function, evidence order, section length, and phrase restraint;
- do not copy topic-specific conclusions, author claims, specimen parameters, or paper-specific language;
- record only generalized style rules in the skill;
- keep citation support separate from style learning.

This distinction matters: a sample paper may be a style exemplar without being a valid technical citation for the current claim.

## Final Output Discipline

For SCI polishing, final output should make the revision traceable:

- show the revised paragraph or section;
- mention the main logic adjustment, not every small word change;
- list missing data, formula checks, or citation checks that affect claim strength;
- avoid creating fake certainty for convenience.

If the user asks for direct replacement text only, keep the notes short but still flag any claim that cannot be supported.
