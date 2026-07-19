# Abstract And Introduction Style

Use this guide for abstracts, introductions, contribution framing, research gaps, and the opening logic of small papers or SCI manuscripts.

## Abstract As A Mini-Paper

A paper abstract should not be a compressed thesis chapter. It should let a reviewer reconstruct the whole study in one pass:

`engineering problem -> method -> object/data -> variables/indicators -> key quantitative result -> contribution -> boundary`

For civil-engineering manuscripts, keep the object and response indicator close together. For example, do not write only "a prediction model was established"; state what structural object is predicted, which response is predicted, and which input conditions define the prediction space. If numerical metrics are available, include the most representative metric and the comparison baseline. If they are not available, use cautious wording and flag the missing metric.

## Abstract Compression Rules

- Use one opening sentence for the engineering problem, not a full background paragraph.
- State the method as a response to the problem, not as a list of tools.
- Include the data basis, model basis, specimen basis, FE basis, or parameter-analysis basis when it controls reliability.
- Report the key result through indicators such as error, stiffness, bearing capacity, deflection, ductility, DCA, or sensitivity ranking.
- End with the use boundary: preliminary design, rapid evaluation, parameter screening, mechanism interpretation, or verification support.

Avoid inflated endings such as "provides an important reference for engineering practice" unless the sentence names the specific design link and applicable range.

## Introduction From Puzzle To Question

The introduction should open from a technical tension or design puzzle, not only from a generic gap. A useful pattern is:

`application demand -> observed difficulty or contradiction -> limits of existing approaches -> unresolved question -> proposed route -> contribution`

In PCSP or structural ML writing, the puzzle might be that high-fidelity simulation is accurate but slow, simplified formulas are efficient but narrow, or machine-learning prediction is fast but needs evidence-bounded interpretability. The introduction should convert that tension into a question the paper can actually answer.

## Literature Review As Dialogue

Do not arrange prior studies as an exhibition of names. Organize them as a short dialogue:

- mainstream explanation or method;
- what it explains well;
- what it leaves unresolved for the current object, parameter range, or design use;
- how the present method complements or narrows that unresolved part.

Use citations to support claims, not to decorate sentences. If a cited paper only supports background, do not use it as proof of a method, mechanism, or design conclusion.

## Contribution Framing

A contribution sentence should contain object, method, evidence, and boundary. Prefer:

`This study develops/validates/compares... for [object] under [condition], using [evidence], to estimate/explain [indicator], within [boundary].`

Avoid "innovation lies in using machine learning" unless the novelty is tied to a structural-engineering problem, a missing response indicator, a new evidence chain, a transferable workflow, or a validated design calculation path.

## Introduction QC

Before finalizing the introduction, check:

- Can the reader name the central question after the first two paragraphs?
- Does each cited cluster support a different function: background, limitation, method basis, comparison, or boundary?
- Does the last paragraph preview the method and contribution without promising more than the data can prove?
- Are broad phrases such as "widely used", "great significance", and "urgent need" tied to object, indicator, or design consequence?
