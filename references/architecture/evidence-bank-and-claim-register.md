# Evidence Bank and Claim Register

Use this reference when drafting or revising from mixed materials: Word/docx files, figures, tables, Excel data, experiment records, FE outputs, ML metrics, GUI code, formulas, or reference notes.

The goal is to keep the manuscript evidence-led and prevent invented data, unsupported claims, or accidental loss of original results during revision.

For substantial scientific reporting, use [research-integrity-and-reproducibility.md](../workflows/research-integrity-and-reproducibility.md). Extend this same ledger with source version/locator, planned/reported/checked/disputed status, processing lineage and verification receipt as needed; do not create a competing ledger. Hashes identify artifacts, not scientific validity. Use the object-integrity guide for calculations/displays and the consistency/delivery guide for changed-result propagation.

## Source Inventory

Before major writing or formal Word revision, list the available materials:

| Source ID | File/Source | Type | What It Contains | Read Status | Used For |
|---|---|---|---|---|---|

Typical types:

- `draft_docx`: original Word manuscript;
- `figure`: image, plot, schematic, screenshot;
- `table_data`: Excel/CSV/table extracted from Word;
- `experiment`: specimen plan, loading protocol, observation record;
- `FE`: finite element model, validation, parameter analysis;
- `ML`: dataset, feature list, metrics, SHAP output, GUI code;
- `reference`: paper, standard, bibliography, Zotero/RDF entry;
- `formula`: analytical equation or design calculation.

## Evidence Bank

Extract only evidence that can support manuscript claims:

| Evidence ID | Evidence Type | Location | Indicator/Variable | Key Value or Trend | Supports Which Claim | Boundary/Risk |
|---|---|---|---|---|---|---|

Recommended evidence categories for civil-engineering writing:

- Test evidence: specimen ID, failure mode, crack pattern, load-displacement curve, peak load, stiffness, ductility, slip, strain.
- FE evidence: modelling assumption, constitutive model, element/contact setting, mesh, validation error, failure mode, parameter range.
- ML evidence: sample count, input features, output variables, data split, R2, MAE, RMSE, MAPE, SHAP ranking, applicability range.
- Design-method evidence: equation, variable definition, code/standard source, calculation example, safety or serviceability boundary.
- Literature evidence: claim-supported sentence, DOI/path, support grade, verification status.

## Claim Register

Convert evidence into writable claims before drafting:

| Claim ID | Draft Claim | Evidence Anchor | Citation Need | Claim Strength | Boundary | Risk/Action |
|---|---|---|---|---|---|---|

Claim strength levels:

- `direct result`: supported directly by the user's figure/table/data.
- `interpretation`: supported by result plus mechanism explanation.
- `comparison`: supported by result plus baseline, standard, or literature.
- `application`: supported by calculation workflow and boundary.
- `hypothesis/needs confirmation`: not ready for final manuscript wording.

## Rules

- Do not write a result sentence unless it has an evidence anchor.
- Do not use external literature to replace missing user results.
- If a claim has evidence but lacks parameter range, add the boundary before returning the text.
- If the evidence is a figure without numerical extraction, write a trend sentence and mark missing values under `需补充或确认`.
- If the evidence comes from GUI or code, distinguish implemented function from validated engineering conclusion.
- If a claim is only an intended contribution, label it as a planned objective rather than a proven conclusion.

## Minimal Workflow

For short section writing, the evidence bank can be internal and summarized under `写作依据`.

For formal manuscript work, produce or update these artifacts:

- `source_inventory.md`
- `evidence_bank.md`
- `claim_register.md`
- `writing_rationale_matrix.md`
- `rewrite_matrix.md` when revising an existing draft
- `logic_transfer_audit.md` when preserving original logic matters

