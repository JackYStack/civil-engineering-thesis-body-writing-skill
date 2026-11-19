# Regression Test Checklist

Use this checklist before publishing repository changes, after router/reference restructuring, or after adding workflow scripts.

## Required Commands

Run from the skill root:

```bash
python -X utf8 scripts/validate_all.py .
git status --short --branch
```

## Phase 8D Regression Cases

At minimum, review the following ordinary workflows after major changes:

1. Thesis sentence anti-vague revision.
2. PCSP model-application paragraph revision.
3. Citation reduction with local/Zotero-first support.
4. DOCX abstract or conclusion safe revision.
5. InstSci-to-Zotero import preview.
6. SCI abstract or introduction rewrite.
7. Target-journal full-manuscript polishing blueprint.
8. Thesis subsection revision that removes chapter-role meta-discourse from the body.
9. Single-section DOCX revision with visual QA limited to the changed section pages.
10. Author-confirmed HFUT figure/table/equation objects preserve the calibrated OOXML container structure and bilingual labels.
11. Scientific reporting distinguishes independent specimens/measurements, FE calibration/validation and ML grouping/preprocessing leakage.
12. Formula transcription, mathematics/units, mechanical assumptions, native-object structure and rendering are checked separately.
13. Quantitative tables/plots reconcile with mapped source data, including missingness, signed bias, percentages, uncertainty and transforms.
14. Changed results propagate to affected abstract/conclusion/captions/reply quotations without claiming unseen files were checked.
15. Metadata lookup failures and overlapping error bars do not become unsupported scientific verdicts.

Use [forward-test-scenarios.md](forward-test-scenarios.md) for reusable fresh-context prompts. Use [public-usage-recipes.md](../examples/public-usage-recipes.md) for human-facing prompt templates. Record public-safe outcomes in [real-task-regression-results.md](real-task-regression-results.md).

## Repository Distribution Gate

Do not push or merge repository changes unless:

- all validators pass;
- README installation and usage instructions are current;
- examples are generic and do not contain private paths, real Zotero keys, specific unpublished paper titles, or hidden data;
- `references/index.md` links all public-facing examples and maintenance guides;
- `manifest.yaml` links all validators required by `validate_all.py`;
- the intended diff excludes temporary files, generated analysis reports, local Word/PDF drafts, and user data;
- the working tree is clean after the changes are committed.

## Privacy And Distribution Gate

Before publishing repository changes, scan for:

- private Windows paths such as `C:\Users\<用户名>\...` or project-specific drive locations;
- Zotero storage paths or item keys tied to a personal library;
- actual DOI strings copied from sample papers;
- API keys, cookies, access tokens, or browser profile paths;
- concrete sample-paper titles, author names, unpublished results, or raw data.

Generic placeholders such as `[docx 路径]`, `[DOI/title list]`, `YOUR_ELSEVIER_KEY`, and `C:\Users\<用户名>\.codex\skills\` are allowed.

## Maintenance Notes

- Add new validators to `manifest.yaml`, `scripts/validate_manifest.py`, and `scripts/validate_all.py` together.
- Add new public references to `references/index.md`.
- Record architecture or distribution changes in `references/meta/update-log.md`.
- Prefer focused reference files over growing the root `SKILL.md`.
- Use [systematic-integration-map.md](systematic-integration-map.md) for lifecycle/source coverage. Record structural, numeric, behavioral, rendered and native-client checks separately, including unperformed ones; a scenario definition is not a passed behavioral test.
