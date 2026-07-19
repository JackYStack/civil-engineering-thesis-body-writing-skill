# Figure Support Mode

Use this mode when the requested deliverable is a publication figure plan, figure revision brief, figure-colour audit, or an actual thesis/journal figure tied to manuscript claims.

- Load `references/workflows/nature-figure-cooperation.md` and, when colour is material, `references/style/scientific-figure-color.md`.
- `civil-thesis-body-writing` owns the manuscript-facing figure brief: claim, evidence, variable semantics, panel logic, terminology, caption context, and target-journal boundary.
- `nature-figure` owns actual plotting, Python/R backend selection, rendering, export, and visual QA. Do not imitate or bypass that backend gate inside this skill.
- If `nature-figure` is unavailable, complete the figure brief and report the missing execution dependency; do not claim that a figure was generated.
- After artifacts return, reconnect them to the manuscript through captions, figure callouts, results/discussion wording, units, terminology, and evidence boundaries.
