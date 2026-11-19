# civil-thesis-body-writing 更新日志汇总

## 2026-11-19: Claude Code 与 WorkBuddy 部署适配

新增共享的 `scripts/install_agent.py`：Claude Code 个人/项目安装，WorkBuddy 本地代码项目 `.codebuddy/skills/` 安装，以及两平台ZIP导出。WorkBuddy导出副本补充开放平台展示字段，不改核心源文件；不推测其用户级目录、不发布到市场、不迁移凭据或修改客户端权限。既有目录默认拒绝覆盖，显式更新先留备份；隔离检查覆盖备份恢复、路径重叠与包完整性。

新增按需加载的 `references/workflows/agent-compatibility.md`，将工具、MCP、渲染、其他skill和宿主专属接口的能力缺失与跳过规则接入入口、manifest及索引。中英文首页补充安装与边界，不添加对照实验介绍。新检查接入全套验证；安装/导出检查不代表已在实际Claude Code/WorkBuddy客户端完成技能发现、调用或全部文件工作流验证。

本次本地核对包括17项隔离安装/打包检查、既有42项分发变异检查及全套验证。Claude Code仅确认本机命令版本可读，未启动模型会话；WorkBuddy未进行实际客户端导入。未安装到现有个人技能库，未迁移外部服务配置或凭据，未发布到技能市场。
## 2026-11-18: 对照结果归档与发布整理

在 `references/meta/real-task-regression-results.md` 补充公开安全的对照摘要：8个真实节选与4个构造样本，两条件各重复2次，48份修订组成24对隐藏标签比较，全部判平，未检出明确质量增益或退化。明确旧组为写作规则重建、评分天花板、每对单评审及小样本限制，不将满分或平局宣传为显著提升或等效性证明。完整语料、源路径、论文数据和原始实验材料保留在作者本地，不进入skill仓库。

本次发布整理同时纳入入口已经引用的审稿局部修订工作流及其合同、技术披露保护和压力场景；不遗漏该未提交依赖，不发布缓存或私有论文文件。此前“未提交或推送”的描述是当时执行阶段的历史记录。

## 2026-11-18: 四源学术表达清理与反防御性边界校准

审阅 `matsuikentaro1/humanizer_academic`、`AIScientists-Dev/academic-humanizer`、`junbolian/Academic-Humanizer`、`taehyeonglim/academic-humanizer` 的核心规则及相关语域/可读性指南，版本和许可证见来源台账。新增 `references/style/academic-prose-cleanup.md`，将最小清理、常规润色和新稿写作作为既有操作内的编辑强度接入 router、manifest、index、core 和 revise 路由，不新增主模式或安装四个独立 skill。

保留证据强度校准、作者风格、清楚优先于压缩、术语/数据/引用及对应关系保护；不迁移医学事实、个人句长与标点偏好、固定改写率、强制节奏变化、上游代码或检测率承诺。澄清反防御性写作针对冗余自辩，不得隐瞒重要负面发现、必要假设、真实不确定性或适用条件。保留“不默认添加泛化局限性段落”的原有偏好。更新既有对比压力场景并新增四个清理场景；结构校验不等于行为验证，运行结果以本次交付记录为准。

本次验证：`scripts/validate_all.py` 全部通过，包括 router/manifest/contract、20 个压力场景结构检查、9 个前向场景结构检查、42 项分发变异测试及官方 quick_validate；`git diff --check` 无空白错误。另由独立上下文只读执行三项短文本行为抽查：定稿最小清理、保留真实不确定性及必要工况/不利结果、识别模型与数值映射互换，三项均符合要求。该抽查不代表全文、Word 版式、原始数据核验或检测器性能验证。本轮未提交或推送，保留原有未提交改动。

## 2026-09-20: 反防御性写作规则整合

安装并审阅 `Adkid-Zephyr/anti-defensive-writing-Skill` 中文版（main: `102c8b21acf5eda3a0aef3d9779a65db646c8980`，MIT）。新增 `references/architecture/evidence-led-narrative-and-defensive-writing.md`，将最强证据驱动的中心主张、贡献直陈、实验论证职责和摘要至结论的结构检查接入 router、manifest、core workflow 与 paper/SCI 模式。按用户反馈，以该上游 Skill 的理念为主：负面结果和局限性不进入普通正文，留在证据库或写作记录中用于检查主张；正文只陈述有证据支持、限定了对象与指标的贡献，不虚构全面领先或更改原始数据。同步更新来源台账与中英文致谢。

更新时间：2026-07-19

## 2026-07-19: Public repository readiness

This update prepares the repository for public visibility without changing skill behavior:

- changed README and Issue Form notices from private-repository wording to explicit public-issue visibility warnings;
- added deterministic rejection of stale private-repository guidance;
- retained the requirement to remove manuscript text, local paths, credentials, Zotero storage keys, and unpublished data from public issues;
- required current-tree validation and Git-history privacy review before the visibility change.

Design boundary: public visibility does not grant a licence beyond the repository's stated terms and does not make user manuscripts or local research data suitable for issue submission.

## 2026-07-18: thesis body meta-discourse and scoped single-section visual QA

This update adds two reusable guardrails based on a real thesis-revision regression:

- thesis body paragraphs now state engineering objects, reused models/formulas, methods, processes, evidence, and boundaries directly; chapter-role comparison and reviewer-facing anti-duplication explanations move to writing rationale or revision notes;
- local DOCX edits confined to one section now visually inspect only the pages occupied by that section, while unaffected content uses structural regression checks;
- full-document visual review remains reserved for multi-section or document-wide layout/field/style changes and explicit final-submission audits;
- pressure tests, forward tests, the final polish checklist, and deterministic contract validation now enforce both rules.

Design boundary: necessary technical cross-references to a model, formula, definition, dataset, or method in another section remain valid thesis prose.

## 2026-07-17: Repository-only distribution

This update removes the former GitHub version-publication route and keeps repository distribution as the single installation source:

- deleted the existing GitHub publication entry and both version labels;
- removed the version badge, publication-page links, archive instructions, and tagging guidance from public and maintenance documentation;
- changed installation guidance to `git clone` or GitHub `Code -> Download ZIP` followed by the existing platform installer;
- changed the maintenance gate from packaging checks to validation, privacy review, and intentional-diff checks before push or merge;
- added deterministic rejection of removed publication links and instructions.

Design boundary: this change does not alter skill routing, writing behavior, installers, output contracts, or repository history.

## 2026-07-17: thesis-skills v3.5 format-audit migration

This update deepens the existing [quzhiii/thesis-skills](https://github.com/quzhiii/thesis-skills) integration after reviewing its Chinese README, active format checker, generic ruleset, architecture guide, and final-audit modules at commit `bc625156ac5e4d3edd03136cf3862c9b76e164c6`:

- added `references/workflows/thesis-format-audit.md` with artifact-specific LaTeX/DOCX/PDF paths, formatting authority, rule-pack calibration, an auditable format matrix, gate semantics, and delivery contracts;
- added final-cleanup, statistical-notation, manual-anchor, reference-scope, compile/export, and review-evidence checks without copying upstream scripts or school rule packs;
- established machine-readable JSON/CSV reports as authoritative evidence and HTML/Markdown dashboards as reading layers only;
- constrained fixes to report-driven, preview-first, allowlisted edits and explicitly excluded captions, labels, numbering, figures, tables, equations, results, and unsupported institutional settings;
- updated the audit mode, output contract, manifest, reference index, public recipe, source ledger, and deterministic validation.

Design boundary: the upstream checker is LaTeX-oriented. DOCX and PDF audits use adapted OOXML/style/rendered evidence and must not be described as direct thesis-skills checker coverage.

## 2026-07-17: DOCX creation workflow and external skill provenance

This update integrates generalized DOCX workflow ideas from [Gostyan/docx-skill-4-cn-paper](https://github.com/Gostyan/docx-skill-4-cn-paper) without copying its implementation:

- added `references/workflows/docx-creation-and-formatting.md` for `create / convert / revise` branching, template precedence, formatting contracts, native Word objects, and layered validation;
- retained `docx-ooxml-editing.md` as the authoritative path for targeted edits to existing Word files;
- updated the DOCX mode fragment, root router, manifest, and reference index so new creation/conversion tasks do not incorrectly enter the existing-file editing path;
- added `references/meta/external-skill-sources.md` as a provenance ledger for this source and previously consulted `nature-skills`, `PaperSpine`, `science-skills`, `InstSci`, `thesis-skills`, and `paper-craft-skills` repositories;
- recorded source links, current reviewed revisions, detected licenses, retained concepts, excluded content, and internal destination files;
- extended deterministic validation so missing DOCX workflow files, route links, or source records fail the contract checks.

Design boundary: institutional or journal templates override generic formatting defaults. No upstream scripts, dependencies, example documents, fixed university settings, or binary assets are redistributed.

## 2026-07-16: Professional GitHub interface pass

Baseline before this phase: `3aab7bd`.

This phase improves first-visit usability without changing skill behavior:

- added bilingual engineering-oriented repository banners;
- restructured both README files around quick start, task prompts, installation, evidence boundaries, and support;
- added structured bug-report and workflow-request issue forms with bilingual privacy warnings and confirmations;
- configured a concise repository description and searchable topics;
- extended distribution validation to parse repository configuration, validate Issue Form option schemas, and scan public files and private-key formats without changing private-repository runtime behavior;
- documented a dedicated `.venv-validation` for local validation dependencies while keeping the skill runtime dependency-free.

Design boundary: this phase does not change the router, writing rules, output contracts, repository visibility, or licensing.

## 2026-07-14: Phase 9 repository usability pass

Baseline before this phase: `b38bf45`.

This phase prepares the skill for easier external use:

- refreshed `agents/openai.yaml` with a clear UI description and concise default prompt;
- added `README.en.md` for English installation and quick-start guidance;
- added `scripts/install.ps1` and `scripts/install.sh` for local installation;
- added `references/meta/real-task-regression-results.md` as a public-safe regression summary;
- extended distribution validation to require installers, bilingual README coverage, UI metadata, and the regression summary;
- prepared repository-based installation guidance and public maintenance checks.

Design boundary: Phase 9 improves repository usability and maintenance traceability. It does not add private manuscript examples, real DOI lists, Zotero item keys, or new domain claims.

## 2026-07-14: Phase 8 distribution hardening

Baseline before this phase: `fefc7c9`.

This phase turns the migrated skill into a more stable public repository:

- added GitHub Actions validation through `.github/workflows/validate.yml`;
- rewrote `README.md` as a clean public installation and usage guide;
- added `references/examples/public-usage-recipes.md` with public-safe prompt templates for thesis, SCI, citation, DOCX, and InstSci-Zotero workflows;
- added `references/meta/regression-test-checklist.md` for distribution gates, regression cases, and privacy checks;
- added `scripts/validate_distribution.py` and wired it into `manifest.yaml`, `validate_manifest.py`, `validate_all.py`, and `references/index.md`.

Design boundary: Phase 8 is packaging and regression hardening. It does not add new thesis-writing claims, sample-paper facts, private corpus data, or Zotero records.

## 2026-07-13: Phase 6D split local paper style

Baseline before this phase: `9dff2db`.

This phase reduces context load for local small-paper and SCI-style writing:

- converted `references/style/local-paper-style.md` into a lightweight compatibility entry;
- added `references/style/paper-style/` with focused guides for abstract/introduction, methods/results/discussion, conclusion/title, and SCI phrase guardrails;
- added `scripts/validate_local_paper_style.py` to keep the compatibility entry small and ensure all split paper-style files remain discoverable;
- wired the validator into `manifest.yaml`, `validate_manifest.py`, `validate_all.py`, and `references/index.md`.

Design boundary: the split paper-style branch supports argument-compressed small-paper and SCI writing. It does not replace the local thesis body-writing guides and does not store concrete sample-paper citations or paper-specific facts.

## 2026-07-13: Phase 7B add forward-test scenarios

Baseline before this phase: `6f78856`.

This phase turns the Phase 7A fresh-context checks into reusable maintenance artifacts:

- added `references/meta/forward-test-scenarios.md` with five ordinary-task forward tests covering anti-vague polishing, PCSP model-application revision, citation reduction, DOCX journal revision, and InstSci-to-Zotero import preview;
- added `scripts/validate_forward_tests.py` to check scenario count, required fields, valid mode IDs, mode coverage, and index wiring;
- wired the validator into `manifest.yaml`, `validate_manifest.py`, `validate_all.py`, and `references/index.md`.

Design boundary: forward tests validate that normal user workflows still route correctly after major changes. They do not replace pressure tests, official skill validation, or real task-specific review.

## 2026-07-12: Phase 6C split citation workflow

Baseline before this phase: `2c08e60`.

This phase reduces context load for citation-heavy writing and citation verification:

- converted `references/workflows/citation-workflow.md` into a lightweight compatibility entry;
- added `references/workflows/citation/` with focused guides for local-first search, support grading, citation output format, and PCSP-specific citation directions;
- added `scripts/validate_citation_workflow.py` to keep the compatibility entry small and ensure all split citation files remain discoverable;
- wired the validator into `manifest.yaml`, `validate_manifest.py`, `validate_all.py`, and `references/index.md`.

Design boundary: old prompts can still open `citation-workflow.md`, but citation-heavy tasks should route to the focused citation files and keep access status separate from sentence-level support.

## 2026-07-12: Phase 6B split style and QC guide

Baseline before this phase: `83df404`.

This phase reduces context load for style polishing and formal quality control:

- converted `references/style/style-and-qc.md` into a lightweight compatibility entry;
- added `references/style/qc/` with focused guides for failure-mode diagnosis, claim-evidence-boundary checking, and final polish;
- added `scripts/validate_style_qc.py` to keep the compatibility entry small and ensure all QC split files remain discoverable;
- wired the validator into `manifest.yaml`, `validate_manifest.py`, `validate_all.py`, and `references/index.md`.

Design boundary: old prompts can still open `style-and-qc.md`, but formal revision tasks should route to the focused QC files instead of loading one merged guide.

## 2026-07-12: Phase 6A split local thesis body style corpus

Baseline before this phase: `24e8f7c`.

This phase reduces context load for local big-thesis style calibration without changing the root router:

- converted `references/style/local-thesis-body-style-corpus.md` from the former merged Word/PDF corpus into a lightweight compatibility entry;
- added `references/style/local-thesis-corpus/` with focused guides for chapter flow, paragraph phrases, experiment style, finite-element style, machine-learning style, and PCSP style;
- added `scripts/validate_local_thesis_corpus.py` to ensure the compatibility entry stays small and all split corpus files remain discoverable;
- wired the new validator into `manifest.yaml`, `validate_manifest.py`, `validate_all.py`, and `references/index.md`.

Design boundary: the old corpus path remains valid. Future tasks can still open `local-thesis-body-style-corpus.md`, but it now routes to focused files rather than loading the full corpus.

## 2026-07-12: Phase 5B root router replacement

Baseline before this phase: `d364d21`.

This phase replaces the root `SKILL.md` with the validated router entry:

- copied the Phase 5A router draft into root `SKILL.md`;
- removed the temporary `static/router/SKILL.router-draft.md` artifact;
- replaced `scripts/validate_router_draft.py` with `scripts/validate_router_entry.py`;
- updated `manifest.yaml`, `validate_manifest.py`, `validate_all.py`, `references/index.md`, and `router-compression-map.md` to validate the root router directly.

Design boundary: detailed writing rules remain in `static/core`, `static/fragments`, and `references`; root `SKILL.md` now serves as the concise router entry.

## 2026-07-12: Phase 5A router compression draft

Baseline before this phase: `db99b59`.

This phase prepares, but does not yet replace, the root `SKILL.md`:

- added `static/router/SKILL.router-draft.md` as a concise router-style replacement candidate;
- added `references/meta/router-compression-map.md` to map long-entry sections to `manifest.yaml`, `static/core`, `static/fragments`, and `references`;
- added `scripts/validate_router_draft.py` to check compression ratio, frontmatter, required guardrails, and route coverage;
- wired the router validator into `manifest.yaml`, `validate_manifest.py`, `validate_all.py`, and `references/index.md`.

Design boundary: formal replacement of root `SKILL.md` is intentionally left to Phase 5B after validation and user confirmation.

## 2026-07-12: Phase 4 compatible manifest/static router layer

Baseline before this phase: `c016d83`.

This phase implements the report's recommended Phase 2 architecture without moving existing `references/`:

- added root `manifest.yaml` with `always_load`, mode/section/source/operation axes, on-demand reference anchors, and validator entries;
- added `static/core/` files for stance, workflow, output format, reader-question sequence, and terminology ledger;
- added `static/fragments/` files for task modes, section types, evidence sources, and operations;
- added `scripts/validate_manifest.py` to check manifest wiring and linked files;
- added `scripts/validate_all.py` to run manifest, contract, pressure-test, and official skill validation from one command;
- updated `SKILL.md` and `references/index.md` to expose the compatible router layer.

Design boundary: this is a compatibility layer. `SKILL.md` is not yet compressed into a pure router, and large reference files are not yet split.

## 2026-07-12: Phase 3 pressure-test scenarios for workflow failure modes

Baseline before this phase: `fe78bd4`.

This phase adds reusable pressure tests for the mode/contract layer:

- added `references/meta/pressure-test-scenarios.md` with stress cases for target-journal polishing without a target journal, thesis-to-SCI over-breadth, Word/OOXML formula risk, citation reduction with weak full-text evidence, InstSci-to-Zotero import, Chinese-English terminology drift, and vague thesis result paragraphs;
- added `scripts/validate_pressure_tests.py` to check scenario count, required fields, valid mode IDs, mode coverage, and index wiring;
- updated `SKILL.md` and `references/index.md` so maintainers can find the pressure-test scenarios.

Design boundary: these scenarios are static pressure tests and prompts for future fresh-context validation. They do not replace real subagent forward-testing when a major behavior change is made.

## 2026-07-12: Phase 2 task modes, output contracts, and static validation

Baseline before this phase: `d5e7e46`.

This phase adds a lightweight nature-skills-style mode/contract layer without changing the core civil-engineering writing rules:

- added `references/meta/task-mode-manifest.md` to force one primary mode before formal or multi-branch tasks;
- added `references/meta/output-contracts.md` to define required output sections for thesis writing, SCI writing, target-journal polishing, citation support, Word revision, translation logic, InstSci-Zotero import, and thesis audit;
- added `scripts/validate_skill_contracts.py` to check that mode and contract files are wired into `SKILL.md` and `references/index.md`;
- updated `SKILL.md` to select task mode and output contract before formal, manuscript-level, citation-heavy, or file-producing work;
- updated `references/index.md` so the new meta guides are discoverable.

Design boundary: the contract layer controls response shape and workflow branching. It does not replace the existing evidence bank, citation workflow, OOXML safety workflow, or anti-vague language pass.

## 2026-07-12: Phase 1 nature-skills logic migration

Baseline saved in git before this migration: `4c74481`.

This phase keeps the existing civil-engineering thesis orientation and adds only lightweight logic controls adapted from nature-skills:

- added `references/architecture/reader-question-sequence.md` for reader-facing section handoffs and question order;
- added `references/architecture/terminology-ledger.md` for canonical terms, symbols, abbreviations, captions, and forbidden variants;
- updated `SKILL.md` so substantial writing/revision tasks trigger reader-question sequencing and terminology ledger checks;
- updated `references/index.md` so the two new architecture guides are discoverable;
- updated `writing-rationale-matrix.md` with a confirmation gate before full drafting or major Word revision;
- updated `docx-ooxml-editing.md` with a targeted revision loop before OOXML edits;
- updated `style-and-qc.md` with failure-mode diagnosis before sentence-level polishing.

Design boundary: this is not a full architecture rewrite. Manifest/static validation layers and richer nature-skills-style automation remain candidates for later phases.

本文件汇总 `civil-thesis-body-writing` skill 的主要更新脉络。已将零散的更新方案、测试记录、迁移记录和上传记录合并为一个总日志；被吸收的零散日志可删除。本文件只记录 skill 演化，不替代具体参考文献、论文审查报告或原始调查资料。

## 1. 总体演化路线

`civil-thesis-body-writing` 已从“土木硕士论文正文写作模板”逐步扩展为一个面向中文大论文、小论文/SCI 投稿稿、目标期刊适配、文献证据核查、Word/OOXML 安全修改和外部工具协同的综合写作 skill。

核心主线包括：

- 从正文生成扩展到 `论点-证据-边界` 控制；
- 从本地写作风格模仿扩展到大论文/小论文/SCI 分支；
- 从人工引用整理扩展到本地优先、网络补充、Zotero/InstSci 辅助的引用候选机制；
- 从普通润色扩展到防空泛语言质检；
- 从段落改写扩展到整篇 Word 文稿的证据迁移和 OOXML 安全修订；
- 从单一写作 skill 扩展到与 PaperSpine、science-skills、InstSci、thesis-skills、Zotero MCP 的分工协同。

## 2. 时间线

### 2026-07-12：加入“现象-机制-条件”论证框架

将“现象 > 机制 > 条件”的三层论文逻辑纳入 skill，用于加强引言、文献综述、方法、结果讨论、thesis-to-paper 和 SCI 投稿稿的深层论证。

新增与更新：

- 新增 `references/architecture/phenomenon-mechanism-condition-framework.md`；
- 在 `SKILL.md` 的核心原则、写作流程和章节触发规则中接入该框架；
- 在 `motivation-thread-writing.md` 中补充“从困惑/矛盾开始，而不是只从缺口开始”的主线校准；
- 在 `sci-writing-principles.md` 中强化引言、方法、结果段的 puzzle、method rationale 和 data translation 规则；
- 在 `nature-writing-adapted-sci-workflow.md` 中把原有工程期刊架构扩展为 `engineering demand -> observed puzzle -> mechanism -> condition -> evidence -> boundary`；
- 在 `style-and-qc.md` 中新增快速质检清单，避免段落只罗列文献、方法或统计结果。

写作效果：

- 引言从“研究缺口”前移到“观察到的困惑/矛盾”；
- 文献综述从“论文展品陈列”改为“主流解释、遗漏视角、互补/冲突、模型整合”的对话；
- 方法部分不仅写“做了什么”，还解释“为什么这样做”；
- 结果部分不仅报告数据，还翻译为机制、阈值、非线性关系和适用边界。

### 2026-07-12：补充“冲突驱动的学术叙事”规则

在“现象-机制-条件”框架基础上，吸收“论文讲好故事”的结构性逻辑，但明确其仅作为幕后规划，不将“悬疑、爽感、彩蛋”等戏剧化表达写入正式论文。

新增规则：

- 一篇文章只死磕一个核心矛盾或核心问题；
- 引言提出技术困惑或设计矛盾，避免只写“已有研究忽略了……”；
- 方法部分承担“路线图”功能，解释为什么用当前方法或 A+B 组合破局；
- 结果部分先给出核心发现，再用图表和指标坐实，而不是按表格顺序平铺；
- 讨论部分把不足写成数据、模型、试件、参数或验证范围的边界，并自然引出未来完善方向；
- 章节之间形成读者期待链：读完引言想知道怎么做，读完方法想知道结果，读完结果想知道机制与边界。

更新位置：

- `SKILL.md`
- `references/architecture/phenomenon-mechanism-condition-framework.md`
- `references/architecture/motivation-thread-writing.md`
- `references/architecture/nature-writing-adapted-sci-workflow.md`
- `references/sections/sci-writing-principles.md`
- `references/style/style-and-qc.md`

### 2026-06-29：刷新 Word/PDF 正文风格归纳语料层

将当前工作区生成的 Word 版与 PDF 版 `civil-thesis-body-writing` 正文风格归纳合并纳入 skill 的重语料层。

处理方式：

- 使用 `references/style/local-thesis-body-style-corpus.md` 作为合并后的完整语料层；
- 保留 Word 语料侧重的段落组织、章节推进、句式模板和 PCSP 写作边界；
- 保留 PDF 语料侧重的合肥工业大学土木/结构工程论文正文风格、试验/有限元/机器学习章节写法和高频工程表达；
- 不把具体本地路径、论文题名、作者名、试件数据或样本文献结论写入 skill 正文；
- `SKILL.md` 已通过 `references/style/local-thesis-body-style-corpus.md` 入口调用该合并语料。

使用边界：

- 普通段落写作仍优先使用 `references/style/local-thesis-style.md`；
- 当用户要求“按本地大论文风格”“使用 Word/PDF 正文风格归纳”“校准 PCSP/有限元/机器学习正文语气”或进行整章改写时，再加载 `local-thesis-body-style-corpus.md`。

### 2026-06-19：SCI 写作规则分支

新增 SCI/小论文写作分支的设计方案，目标是把大论文材料压缩为适合投稿稿的中心论点链条。

主要规则：

- 写 SCI 稿前先建立 `论点地图`，包含中心问题、主张、证据来源、关键变量、图表公式、边界和审稿风险；
- 摘要按 `问题 -> 方法 -> 对象/数据 -> 变量 -> 关键结果 -> 贡献/边界` 组织；
- 引言只服务于本文具体问题，不写成领域百科；
- Results and Discussion 按 `证据 -> 趋势 -> 数量 -> 机理 -> 意义/边界` 展开；
- 英文表达必须服从证据，不把高级句型当作论证替代品；
- 引用按功能区分为背景、空白、方法、比较和边界。

对应实现方向：

- 新增/强化 `sci-writing-principles.md`；
- 更新 `local-paper-style.md`；
- 扩展 `style-and-qc.md`；
- 与 `anti-vague-language.md` 联动，约束“高效、显著、有效、具有价值”等空泛表达。

### 2026-06-19：PCSP 稿件测试

使用 PCSP 中英对照稿对 skill 进行测试，验证 SCI 分支、防空泛语言、引用功能标签和模型应用逻辑是否能正常触发。

测试得到的关键能力：

- 能提取 PCSP 稿件的中心问题、数据来源、输入变量、输出指标和适用边界；
- 能识别 `DCA_s` 与 `DCA_c` 记号混用问题；
- 能区分刚度组合度和承载力组合度的预测难度；
- 能识别“参数优化”“最佳组合度”等可能过强的表述，并建议降级为“参数调整”“方案筛选”或“优化支持”；
- 能把 GUI 应用限定为初步设计、快速评估、参数敏感性分析和有限元/规范复核前的辅助工具；
- 能对已有引用进行功能分类，而不是只保留编号。

### 2026-06-19：PCSP 稿件正式使用

对 PCSP 论文进行正式文稿级使用，不再只是规则触发测试。

主要产出：

- 建立全文级论点地图；
- 抽取公式、样本量、输入变量、输出指标、模型评价指标和 SHAP 解释结果；
- 提出优先问题清单，包括 DCA 记号统一、4.2 节设计指标计算链、摘要/结论强表述降级、有限元验证误差补充等；
- 生成中文题名、英文题名、摘要、英文摘要、4.2 节模型应用和英文 4.2 节的可替换文本；
- 对题名、摘要、引言、方法、模型训练、SHAP 和 GUI 应用进行章节审查。

这次使用确认了：skill 适合按“文稿主线 -> 证据链 -> 段落改写 -> 风险清单”的方式处理整篇小论文/SCI 稿。

### 2026-06-23：吸收 PaperSpine 机制

学习 PaperSpine 后，补充了更强的论文级主线与证据组织机制。

迁移的核心思想：

- 写作前先确认“章节主线”或“全文主线”；
- 对正式文稿级任务使用 `写作理由矩阵`，说明每个段落为什么存在；
- 对 Word、图表、试验结果、有限元结果、机器学习指标等材料建立证据库；
- 用 `claim register` 管理论点、证据和边界；
- 对大段中文转英文、摘要重写、引言删减、结果讨论合并、结论压缩等任务使用逻辑迁移矩阵；
- 用结构化审计输出“发现了什么、根因是什么、怎么修、不修会影响什么”；
- 学习样例的段落功能顺序，而不复制样例措辞、数据和结论。

对应新增/强化：

- `motivation-thread-writing.md`
- `evidence-bank-and-claim-register.md`
- `writing-rationale-matrix.md`
- 文稿级输出格式和风险清单规则。

### 2026-06-24：迁移 science-skills 的外部来源纪律

引入 science-skills 的来源使用纪律，使 Zotero、网络检索、API、出版商页面和目标期刊范文不再只作为“查到即用”的信息源。

新增能力：

- 记录来源/工具、查询词、筛选条件、审阅数量、DOI/URL/path、访问状态和证据边界；
- 区分 metadata-only、abstract、full text、official page 等证据等级；
- 网络检索结果不得直接升级为机理或结果对比依据；
- 目标期刊范文区分 `style exemplar` 与 `technical citation`；
- 大型 API/数据库结果必须裁剪为任务所需字段；
- 缺全文、限速、空结果时降级并标注，不强行写结论。

对应文件：

- `external-source-and-tool-use.md`
- `citation-workflow.md`
- `target-journal-polish-workflow.md`
- `zotero-library-learning.md`
- `use-case-templates.md`
- `README.md`

### 2026-06-26：接入 InstSci 与 thesis-skills

明确 `civil-thesis-body-writing` 与 InstSci、thesis-skills 的分工。

InstSci 定位：

- 作为论文获取与访问证据层；
- 用于 DOI 批量获取、出版社 PDF 访问核查、封闭访问验证和目标期刊范文采集；
- 检索或下载状态不等于引用支撑；
- 机构登录、SSO、2FA、CAPTCHA 等必须由用户在可见浏览器中完成；
- 不读取或粘贴凭据、cookie、API key 等敏感信息。

thesis-skills 定位：

- 作为 LaTeX/项目级确定性审查层；
- 输出 `PASS` / `WARN` / `BLOCK` readiness gate；
- 默认 preview-first，不自动应用风险性修复；
- 不替代正文写作、导师判断或学术审查。

对应新增/强化：

- `instsci-paper-retrieval-workflow.md`
- `thesis-skills-audit-workflow.md`
- `external-source-and-tool-use.md`
- `SKILL.md`
- `README.md`

### 2026-06-26：InstSci 到 Zotero MCP 导入链路

新增 InstSci 获取论文后进入 Zotero 的链路流程。

规则边界：

- Zotero 写入会修改用户文库，必须先输出导入预览并等待确认；
- 导入前按 DOI/题名查重；
- 缺 DOI、缺 PDF、元数据不确定或访问状态未核实时必须标记；
- 导入后写入 tags/notes/collection 需明确操作；
- `open access retrieved`、`browser verified` 等只是访问状态，不等于正文引用支撑；
- 导入 Zotero 后仍需通过全文读取和 `citation-workflow.md` 做 claim 级引用判断。

对应文件：

- `instsci-to-zotero-import-workflow.md`
- `instsci-paper-retrieval-workflow.md`
- `SKILL.md`
- `README.md`

### 2026-06-26：GitHub 上传记录

创建并上传 `civil-thesis-body-writing` 的 GitHub 发布副本。

记录要点：

- 已建立发布副本；
- 远端仓库初始状态为 private；
- 上传时通过基础结构校验和 Markdown 相对链接检查；
- 普通 `git push` 未完全建立 tracking，后续如需公开分发，应确认远端权限、分支和最新本地变更是否同步。

注意：该上传记录反映当时状态。2026-06-27 之后的本地修改不一定已同步到远端。

### 2026-06-26：正文风格归纳合并

将 Word/PDF 风格归纳合并到本地大论文风格参考中。

形成分层：

- `local-thesis-style.md`：默认速查执行版，用于普通段落写作和章节组织；
- `local-thesis-body-style-corpus.md`：完整语料规律版，用于章级改写、PCSP/有限元/机器学习正文风格校准、需要贴近本地大论文语料时调用。

设计原则：

- 不复制样本论文的具体数据、结论和题名；
- 只保留段落组织、语气、证据链、章节顺序和边界表达；
- 普通写作优先读轻量版，避免上下文负担。

### 2026-06-27：本地风格分层优化

进一步明确 `local-thesis-style.md` 与 `local-thesis-body-style-corpus.md` 的关系。

优化后：

- `local-thesis-style.md` 成为“速查执行版”；
- `local-thesis-body-style-corpus.md` 保留为“重型语料/溯源层”；
- 强化 `研究对象 -> 方法/模型 -> 参数/工况 -> 指标 -> 证据 -> 机理 -> 边界/用途` 写作契约；
- 增加 PCSP / FE / ML 专项规则；
- 增加空泛表达降级表；
- 更新 `index.md` 和 `README.md`，避免两个文件职责混淆。

验证：

- `quick_validate.py` 通过；
- Markdown 相对链接检查通过。

### 2026-06-27：去除内置论文引用

按“仅保留总结内容”的原则，清理 skill 中的具体论文引用信息。

已去除：

- 具体论文题名；
- 作者名；
- Zotero item key；
- DOI 字符串；
- 样本文件名；
- 本地论文路径；
- 代表论文清单。

保留：

- 语料类型；
- 写作规律；
- 主题簇；
- 参数、指标和段落组织方式；
- Zotero/InstSci 引用检索工作流字段。

修改位置包括：

- `SKILL.md`
- `references/style/local-thesis-body-style-corpus.md`
- `references/examples/zotero-corpus-profile.md`
- `references/style/local-paper-style.md`
- `references/workflows/zotero-library-learning.md`

验证：

- `quick_validate.py` 通过；
- Markdown 相对链接检查通过；
- 具体论文题名、作者名、样本编号、Zotero key 残留扫描无命中。

## 3. 当前能力模块

### 3.1 中文土木硕士论文正文

- 绪论、研究现状、试验研究、有限元分析、参数分析、机器学习模型、设计方法、本章小结、结论展望；
- 强调对象、方法、参数、指标、证据、机理和边界；
- 支持一节一节少量多次推进。

### 3.2 小论文 / SCI 投稿稿

- 论点地图；
- 摘要/引言/结果讨论/结论的投稿稿结构；
- 目标期刊适配；
- 从大论文压缩为小论文；
- 中译英前逻辑校核。

### 3.3 引用与证据

- 本地文库/Zotero/已有参考文献优先；
- 网络检索补充；
- claim 级引用候选；
- 支撑等级；
- 元数据、摘要、全文、官方页面的证据边界区分。

### 3.4 防空泛语言

- 约束“意义重大、效果较好、显著提高、具有较高价值、影响较大”等表达；
- 强制补充对象、指标、证据、机制和边界；
- 缺证据时降级表达并列入需确认。

### 3.5 Word/OOXML 安全修改

- 修改现有 `.docx` 时默认新建文件；
- 保留原格式和兼容性；
- 对大范围改写先建证据库和逻辑迁移矩阵。

### 3.6 外部工具协同

- Zotero：文库学习、全文抽取、引用候选、导入管理；
- InstSci：论文获取、访问证据、目标期刊范文采集；
- thesis-skills：确定性审查、readiness gate；
- PaperSpine：主线、证据库、写作理由矩阵；
- science-skills：来源纪律、工具记录、访问状态边界。

## 4. 被本日志吸收的零散记录

以下文件的关键信息已并入本总日志，可删除：

- `civil-thesis-body-writing_SCI写作规则更新方案_2026-06-19.md`
- `civil-thesis-body-writing_skill测试_PCSP论文_2026-06-19.md`
- `PCSP论文_civil-thesis-body-writing正式使用结果_2026-06-19.md`
- `PaperSpine补充civil-thesis-body-writing分析_2026-06-23.md`
- `science-skills迁移civil-thesis-body-writing记录_2026-06-24.md`
- `InstSci_ThesisSkills迁移civil-thesis-body-writing_2026-06-26.md`
- `civil-thesis-body-writing_InstSci到Zotero导入链路更新_2026-06-26.md`
- `civil-thesis-body-writing_GitHub上传记录_2026-06-26.md`
- `civil-thesis-body-writing_正文风格归纳合并记录_2026-06-26.md`

以下文件属于资料调查、安装记录或其他研究产物，不作为本次“更新日志合并”的删除对象：

- `SCI写作资料调查报告_2026-06-19.md`
- `SCI写作资料完整文件索引_2026-06-19.md`
- `Zotero全文语料学习调查报告_2026-06-24.md`
- `InstSci安装记录_2026-06-26.md`
- `science-skills安装记录_2026-06-24.md`
- `ThesisSkills安装记录_2026-06-26.md`
- PCSP 文献、图解、综述、证据摘录等专题资料。

## 5. 当前注意事项

- GitHub 上传记录是历史状态，不代表当前本地版本已推送。
- 目前 skill 内已移除具体论文引用，仅保留总结性写作规律。
- Zotero、InstSci 和网络检索仍可在实际写作任务中动态生成引用候选，但不能把检索命中自动当作正文证据。
- 后续如继续修改 skill，建议只新增可复用规则，避免再次把具体论文清单、作者名或本地路径写入 skill。

### 2026-07-17：科研图表配色与可访问性分支

基于用户保存的《论文配色：跟着顶刊学配色（Nature篇）》23 页 PDF 完成逐页渲染核对。新增 `references/style/scientific-figure-color.md`，将可复用内容收敛为：

- 11 组经页面色卡核对的代表性 Hex 色板；
- 名义、顺序、连续和以零为中心变量的颜色角色规则；
- 试验-有限元、参数分析、机器学习、SHAP、场变量和构造示意图的映射建议；
- 色觉模拟、非颜色冗余、灰度打印、终稿尺寸、RGB/CMYK 与导出检查；
- 学校/期刊模板和官方作者指南优先于示例色卡的边界。

来源边界：知乎文章汇总的是已发表图件中的配色示例，不是 Nature 官方标准色板。可访问性与导出约束另外对照 Nature research figure guide，不归因于知乎原文。同步更新 router、manifest、参考索引、公开使用配方、README 和确定性验证器。

### 2026-07-17：与 nature-figure 的图件协作路由

按“正文语义规划与绘图执行分离”的原则，新增 `figure-support` 模式和 `references/workflows/nature-figure-cooperation.md`：

- `civil-thesis-body-writing` 负责核心结论、章节角色、证据层级、变量/单位、面板问题、颜色语义、图题上下文和正文再集成；
- `nature-figure` 负责 Python/R 后端门、绘图代码、渲染、导出和视觉/统计 QA；
- 使用 figure brief 和 artifact return 字段完成显式交接，不复制外部 Skill 的绘图实现；
- `nature-figure` 未安装、数据缺失、后端未确定或运行环境不足时，保留规划产物并如实报告阻塞，不生成替代图或虚构产物；
- 新增前向测试和压力测试，防止补造趋势数据、绕过后端门以及未生成文件却声称完成 QA。

同步更新 router、manifest、模式契约、静态 fragment、配色指南、来源台账、中英文 README、公开使用配方、Codex UI 元数据和验证器。上游来源仍为 [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)，仅集成协作边界，不复制其脚本、API 或内置色板。

### 2026-07-17：GitHub README 尾部致谢与来源索引

在中英文 README 尾部新增致谢区块，直接链接 7 个已记录的公开上游 Skill/工具仓库，并简述各项目对本 Skill 的影响范围。致谢区同时链接 `references/meta/external-skill-sources.md`，由完整台账继续承担审阅版本、许可证、迁移状态、保留/排除内容和内部落点的溯源职责。

分发验证器现强制检查：

- 中英文致谢标题和顶部导航入口存在；
- 完整来源台账链接存在；
- 7 个上游仓库的直接链接同时出现在中英文 README；
- 后续界面重构不能在验证仍通过的情况下静默删除致谢索引。

### 2026-07-18：正文补充说明与适用性免责声明门

根据第3.4节机器学习预测正文反馈，新增普通方法/结果正文的免责声明过滤规则：

- 保留数据、指标、比较和证据支持的结果解释；
- 删除“超出参数范围需补充有限元分析或试验”“不能替代规范校核或高保真有限元复核”等通用适用性、安全使用和复核提醒；
- 将随机种子、分层区间、超参数来源等缺失记录放入内部写作记录或`需补充或确认`，不作为正文解释；
- 仅在用户明确要求独立局限性章节时，才将相应边界组织为正式正文。

同步增加机器学习正文压力测试，防止以“正文完整”或“工程安全”为由重新加入等价免责声明。

### 2026-07-22：合工大论文 Word 图、表、公式真实结构校准

依据用户指定的本地参考 Word/PDF 完成对象级核对，并将可复用结构写入 `references/style/hfut-thesis-word-objects.md`。本次校准只记录结构和样式契约，不保留参考论文题名、作者、路径、数据或结论。

校准结果：

- 图采用 2 行 1 列无可见边框的 Word 表格；首行为图，次行同一单元格内依次放中文、英文两个独立图题段落；
- 表题位于原生三线表之外，英文标签沿用 `Tab`；表格顶底线为 1.5 pt，表头下边线为 0.5 pt，不增加外层包裹表格；
- 公式采用 `公式` 段落中的原生 OMML 公式阵列，公式居中、编号在同一行最右侧，不使用三列表格、空格或制表位模拟；正文引用采用 `式（2.1）`；
- 新增结构验证、压力测试和前向测试，并把该项目规则接入 DOCX 创建、OOXML 修改及格式审查路径；
- 规则被明确限定为用户确认的项目级格式。现行正式模板或明确校方要求始终具有更高优先级。

维护过程遵循内置 `skill-creator` 以及 `superpowers:writing-skills` / `superpowers:test-driven-development` 的 RED-GREEN-REFACTOR 方法。RED 基线暴露出通用经验会误用三行图容器、`Table` 标签、0.75 pt 表头线和三列公式布局；新增确定性契约后再执行同场景回归与完整验证。

### 2026-10-16：审稿驱动的正文局部修订

新增按需加载的 `reviewer-driven-revision` 工作流，沿用现有 paper/thesis/Word 模式，不增加重复模式。重点为保留原文风格、插入位置与上下文衔接、工程解释的局部完善、采样约束与模型假设的证据区分，以及正文改动向回复证据的交接。澄清反防御性规则不删除必要假设、实质性反证或审稿要求的技术条件。补充三个压力场景；场景定义与结构校验不等同于模型行为测试。未将本次论文的参数值、文献编号或本地路径写成通用规则。
