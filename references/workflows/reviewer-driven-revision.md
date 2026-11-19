# Reviewer-driven manuscript revision

Use for revising thesis/paper body text in response to a specific reviewer or supervisor comment. Keep the existing primary mode; this is a focused revision workflow, not a requirement to rebuild every section or generate a reply letter.

## Establish the request and current text

- Identify each question in the comment: rationale, method detail, engineering interpretation, evidence, scope, language, or presentation. Distinguish requests to explain existing work from requests for new analyses.
- Use the author-designated latest manuscript, reply, and template. Manually updated source files supersede stale generated copies. Read the target passage and adjacent context before offering replacement text. Do not silently edit files during a wording discussion or read-only audit.
- In a step-by-step discussion, handle the active comment, carry forward accepted decisions, and retain deferred items. Do not reopen accepted wording without a concrete new contradiction or evidence gap.
- Map each subquestion to existing evidence, a required local change, or a reply-only explanation. If the manuscript already states the point adequately, cite that passage rather than manufacturing another revision.

## Choose the smallest complete amendment

Preserve the original voice, paragraph order, valid results, terms, and citation numbering when the user requests refinement. Prefer a sentence insertion or local replacement; replace a whole paragraph only when its reasoning cannot be repaired locally. Give a searchable insertion anchor and specify whether text is added or replaced. Check the transition into and out of the amendment.

For introduction endings, connect the research need to a gap already established earlier. If that need is absent, repair the preceding gap statement locally or adjust the closing claim. Put the author-confirmed main contribution first and explain how prediction targets, analyses, or tools support it; do not turn every component into a separate novelty claim.

For engineering interpretation, add the missing link between the observed trend, a supported mechanical explanation, and its design implication. Prioritize the variables and contrasts that answer the reviewer; equal-length explanations of every input are not automatically necessary. Preserve sound analyses the author has retained. Distinguish normalized indices from absolute stiffness/capacity, sensitivity from causation, and a plausible explanation from a directly verified mechanism.

## Assumptions and sampling are technical content

Do not let anti-defensive writing erase necessary scientific conditions. State model assumptions, excluded mechanisms, actual bounds, coupling rules, and screening criteria where readers need them to understand the method. Keep generic apologies and unrelated future-work warnings out of the passage.

Distinguish three kinds of evidence:

| Evidence | What it establishes |
|---|---|
| Input bounds, discrete levels, allowed parameter pairs | The sampled domain and compatibility with a chosen constitutive relation |
| Interface/anchorage laws and excluded mechanisms in the FE model | The assumptions under which numerical responses were generated |
| Mechanism-specific capacity checks, simulations, or relevant tests | Whether physical configurations satisfy the assumed regime |

Coupled stiffness/capacity parameters do not by themselves verify anchorage or interface failure exclusion. Omitting bond transfer is different from assuming a bonded interface remains intact. Statistical outlier filters are not physical failure-mode screens unless their criterion tests that mechanism. Inspect code and actual retained data before saying all samples meet a numerical constraint.

If a bound or candidate set was selected by the author with reference to experimental data, describe it as such; do not upgrade it into a code limit or a literature-established universal threshold. Provide reproducible bounds and selection/coupling rules. List exact candidate pairs, or supply a table/supplement, when the discrete set is needed to reproduce sampling and is not recoverable from those rules; do not require a long list for every method clarification.

Once model consistency and physical verification are clearly distinguished, assess completeness against the reviewer's actual question. Do not repeatedly append equivalent disclaimers; do not conceal a material unverified condition merely to sound confident. Existing validation steps in an application flowchart may support that workflow, but do not retrospectively validate every training sample's physical failure mode.

## Literature support for new sentences

Check the actual publication/version and exact passage, not only an attachment title, abstract, or earlier chat summary. Preserve material type, surface treatment, loading, time, and anchorage conditions. A simulation precedent supports using an idealization under its conditions, not a universal statement that the excluded mechanism cannot occur. Preserve qualifiers such as “may”; possible degradation is not inevitable failure. Do not reuse a nearby citation number for a newly added claim until its support has been verified.

## Body-to-reply handoff

Keep proposed wording, implemented manuscript edits, and reply-only explanation distinct. For a local request, return the insertion anchor and ready-to-paste text, followed by a brief account of what changed. A user-reported edit can guide the discussion; file-level consistency is verified only after inspecting the current file.

When the user requests a reply/package and `nature-response` is available, load its current instructions for letter structure and revision evidence. Pass the comment ID, exact changed passage, source/version, evidence, and verified location. Do not depend on that skill for ordinary body editing; the rules here remain usable on their own.

Quote only the actual changed spans plus necessary context. Preserve the user's template and technical formatting; red color alone is neither sufficient nor necessary evidence of a change. Keep representative verified old/new language examples when a general proofreading comment is answered. Obtain page/line numbers from the current rendered manuscript; use page and figure/table identifiers where lines are not numbered. Recheck locations after edits that affect pagination.

For Word edits, use the existing DOCX workflow, preserve the latest author edits, and inspect affected rendered pages. Preserve vectors, equations, fields, and caption numbering. On a final package check, reconcile every reviewer ID, text excerpt, change marking, and location so shortening one response does not remove another comment's evidence.

Use [manuscript-consistency-and-delivery.md](manuscript-consistency-and-delivery.md) for clean/marked/reply coupling, baseline-based marking, changed-result propagation and target-specific declarations. A companion's LaTeX checker does not verify a DOCX package; report the formats and checks actually supported.
