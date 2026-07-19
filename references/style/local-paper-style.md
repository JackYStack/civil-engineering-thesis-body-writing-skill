# Local Civil-Engineering Paper Style

This is a compatibility entry for the split local paper/SCI style guides. Use it when an old prompt or reference points to `local-paper-style.md`; for new tasks, route to the focused files below.

## When To Use

Use this branch when the user asks for:

- small-paper or SCI manuscript drafting, compression, or polishing;
- thesis-to-paper adaptation;
- abstract, introduction, Results and Discussion, conclusion, title, highlights, or contribution rewriting;
- target-journal style alignment when the target is an engineering journal family;
- Chinese technical-paper style checks before English translation or journal polishing.

Do not use this branch as the default for Chinese master's thesis body writing. For thesis chapters, start from [local-thesis-style.md](local-thesis-style.md) and use this branch only when the user explicitly wants paper-style compression.

## Split Guides

| File | Use When |
|---|---|
| [paper-style/index.md](paper-style/index.md) | Choosing which local paper/SCI style guide to load. |
| [paper-style/abstract-intro.md](paper-style/abstract-intro.md) | Writing or auditing abstracts, introductions, contribution framing, and research-gap compression. |
| [paper-style/results-discussion.md](paper-style/results-discussion.md) | Writing methods rationale, results, discussion, figure/table interpretation, and evidence chains. |
| [paper-style/conclusion-title.md](paper-style/conclusion-title.md) | Writing conclusions, titles, highlights, contribution statements, and thesis-to-paper adaptation notes. |
| [paper-style/sci-phrase-guardrails.md](paper-style/sci-phrase-guardrails.md) | Checking reviewer-facing boundaries, forbidden overclaims, and local paper style quality. |

## Core Rule

Paper style is not "short thesis style." It is argument-compressed writing. Each section should answer one reader question with a narrow evidence chain:

`problem -> method -> object/data -> indicator -> key result -> mechanism/explanation -> boundary`

Use this rule to remove broad background, repeated method explanation, unsupported praise, and conclusions that go beyond the data.

## Minimal Load Path

- Abstract or introduction task: load `paper-style/abstract-intro.md`.
- Results, methods, or discussion task: load `paper-style/results-discussion.md`.
- Conclusion, title, highlights, or contribution task: load `paper-style/conclusion-title.md`.
- Reviewer-risk, overclaim, or final language check: load `paper-style/sci-phrase-guardrails.md`.

If the task involves a named journal, also load the target-journal workflow. If it involves citation replacement or reduction, run the citation workflow before rewriting.
