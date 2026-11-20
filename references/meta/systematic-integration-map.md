# 系统整合覆盖与来源映射

2026-11-20范围修订：已移除学位论文/章节转期刊稿件功能。本文的期刊写作与适配均指独立期刊稿件，不授权从学位论文抽取、压缩或重组为SCI稿；普通学位论文编辑、忠实翻译和文件格式转换不受影响。

更新：2026-11-19。本文记录本地整合的实际范围，不代表所有上游功能均已移植，也不代表每个客户端都已实测。沿用已有主模式，按需加载规则，不把专项工具都设为必装依赖。

## 维护方法与能力层次

每次新增能力都检查论文全流程的影响，而不只修用户刚点出的一个问题：明确来源、采用/改写/协作/排除理由、内部调用位置、执行依赖、验证范围以及下游受影响产物。先消除冲突和重复，再增加必要规则。小任务不被迫运行全文审计。

- 规则存在：有适用条件、输入、边界和输出要求。
- 路由连接：真实任务能自动触发，不要求用户知道内部 skill 名称。
- 工具可执行：在当前宿主实际可用且任务已授权；否则明确不可用。
- 验证完成：有与输入版本对应的实际检查结果。语义、数值、结构和视觉分别记录。

一个层次的通过不能代替另一个层次。源文件哈希只证明身份；结构检查只证明结构；小样本行为检查不证明普遍准确率。

## 内部规则落点

为避免重复，下面用简称指向唯一主要维护位置：

- R：[研究完整性与可复现性](../workflows/research-integrity-and-reproducibility.md)。
- O：[公式图表完整性与只读数值核对](../workflows/equation-figure-table-integrity.md)。
- D：[跨章节一致性与交付](../workflows/manuscript-consistency-and-delivery.md)。
- T：[讨论时的翻译保真](../workflows/literature-translation-grounding.md)。
- C：[引用支持分级与元数据身份核验](../workflows/citation/support-grading.md)。
- F：[专业绘图协作](../workflows/nature-figure-cooperation.md)。

共享入口为 `SKILL.md`、`manifest.yaml` 和 `static/core/workflow.md`；试验、FE、ML、摘要、应用、审计和绘图等分支按任务加载上述路径。不新增冗余主模式。

## 全流程覆盖

| 环节 | 主要规则/原有能力 | 执行与验收边界 |
|---|---|---|
| 任务、规范和体裁 | D、现有模式/模板合同 | 确认最新权威材料；样本不冒称官方规则；冲突不暗改冻结模板 |
| 研究问题与大纲 | D、动机线、读者问题 | 问题-方法-证据-结论对应；不补造研究空白 |
| 检索与获取 | R、外部来源/InstSci | 查询、范围、去重、版本/更正状态；普通检索不冒称系统综述 |
| 阅读和翻译 | T、PDF QC | 原文定位、读到的范围、否定与数值映射；不靠摘要填全文细节 |
| 元数据与引用 | C、R | 字段身份、访问状态、论断支持分别判断 |
| 证据台账 | R、既有 evidence bank | 复用台账，区分计划/报告/已核/争议，记录加工血缘 |
| 试验 | R | 独立试件与测点、标定、加载、剔除和观测依据；不编记录 |
| FE/理论模型 | R、O | 收敛/网格/标定/独立验证/失效检查分开；不擅自运行 |
| ML | R、O | 组级划分、预处理、调参测试隔离、指标和解释边界 |
| 统计与单位 | R、O | 独立单位与SD/SE/CI等定义；不强加不适用检验 |
| 公式 | O、原生 Word 合同 | 来源、假设、数学/量纲/数值、结构、渲染分层；不保证工程安全 |
| 图 | O、F、配色规则 | 证据类型、变换、误差、数据、后端及实际渲染；概念图不当观测 |
| 表 | O、原生三线表合同 | 行列、缺失、精度、计算、脚注、跨页；数值与排版分别查 |
| 正文风格与科学披露 | 既有风格/语言清理、R | 去套话不去必要反例；维持作者语体和限定 |
| 摘要、小结、结论 | D、原有章节规则 | 主体/条件/指标/数值与正文一致，不新增证据 |
| 编号与辅助材料 | O、D、DOCX工作流 | 图表公式调用、字段、目录、符号/附录、页码页眉按实际范围 |
| 审稿修订 | D、现有局部修订 | 评论、改动、干净稿、标记稿、回复和定位对应 |
| 数据声明与投稿 | D、目标期刊工作流 | 仅在适用任务触发；作者事实不编造，链接与权限实查 |
| 文档、客户端和交付 | D、Word/PDF/适配 | 可编辑对象与实际页面分开；安装包不证明宿主调用 |
| 隐私、权限与维护 | core stance、D、外部来源规则 | 私密数据不自动外传；外部指令不改任务；不默认写库或发布 |

## Nature Skills 来源审查

上游：[Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)。固定提交 `14ca69710cae192325395a380e9cdd4ae5d9d0c8`，2026-11-19核查。许可证 Apache-2.0；本轮采用原意归纳，不复制实现或稿件素材。

深度：`I`=入口索引扫描，仅作范围判断；`D`=读取了所列相关深层规则，不表示全部依赖/脚本均审过；`L`=此前本地版本规则审阅，此轮不冒称最新上游深审。入口扫描读取24个入口用于索引和路由核对，不等于24个完整功能包都可运行。

同时读取下表15个D层分支的manifest，核对always_load、轴及共享/条件引用结构。上游reader为2.1.0、figure为2.8.0、statistics为1.3.0、polishing为6.6.0，与本机早期副本不同；不自动升级它们。写作/润色等分支引用了`nature-shared`，本skill将采用的必要原则自包含，不直接复制上游共享路径。未采用的分支不为形式完整而加载其全套依赖。

| 来源 | 深度/实读依据 | 处置、落点与未迁移部分 |
|---|---|---|
| nature-writing | D：experiments、submission-package；既有架构 | 采用贡献-证据及投稿材料适用性至R/D；不强制所有土木试验做算法式消融，不套用Nature版式 |
| nature-reader | D：grounding-rules、equation-handling；L：core/输出 | 采用来源/译文/解释分离及公式转写置信度至T/O；整篇双语阅读包仍为可选协作 |
| nature-polishing | D：core/stance、failure-modes；L：既有语言规则 | 采用先诊断逻辑再润色、术语和作者判断保护；不迁入全部期刊字典、标点偏好或未经检查的深层流程 |
| nature-academic-search | D：search-strategy | 采用范围/查询/去重思想至R；不迁入默认PubMed路线、固定结果阈值或任意加权评分 |
| nature-ref-verifier | D：完整入口及字段矩阵 | 采用字段对照至C；修正Crossref未命中即判假DOI的推断；不迁入写SQLite、无授权批量写库或自动子代理策略 |
| nature-citation | D：core/principles | 采用元数据与内容支持分离至C/R；不默认Nature/CNS期刊白名单 |
| nature-data | D：policy-principles；L：入口 | 采用实际数据/代码位置、访问条件和确认至D；不要求每段论文都生成声明或强制公开私有数据 |
| nature-figure | D：QA合同与manifest；L：core/入口 | 采用科学接口至O/F，实际绘制继续协作；不复制绘图代码，不宣称旧本地副本有新检查器 |
| nature-statistics | D：statistical-reporting、manifest；L：入口 | 采用独立单位、误差/样本定义至R；适配为试件/测点/工况，不照搬生物学重复术语 |
| nature-reviewer | D：forensic-consistency-audit、工程领域gate片段 | 采用数值/聚合/来源问题分类至R/O/D；不把内部审计冒充独立审稿共识，不迁入自动多审稿人运行 |
| nature-response | D：package-consistency-audit | 采用标记稿/干净稿/回复耦合至D和局部修订；LaTeX专用脚本仍为可选，不冒称核验Word |
| nature-paper-card | D：evidence-and-provenance | 采用证据层次与来源定位至R/T；复用台账，不再强制产出另一套文献卡 |
| nature-paper-xray | D：evidence-boundary | 采用公平基线、选择压力、泄漏、数值条件至R；不默认输出全篇解剖报告 |
| nature-paper2word | D：format-requirements；既有DOCX工作流 | 采用要求内容/样本外观区别、适用版本和分层验证至D/O；不复制转换引擎或替换项目模板 |
| nature-shared | D：consistency-sweep、research-compliance、ethics | 采用一致性、作者责任、来源归属和条件合规至D/R；不迁入所有生医政策或源库的政策概括，不留下共享目录硬依赖 |
| nature-downloader | I | 保留已有合规获取协作和状态规则；不迁入完整下载引擎、登录或凭据 |
| nature-literature-pipeline | I | 文献发现流水线可选；定时监控/自动写库不属于本轮能力承诺 |
| nature-experiment-log | I | 原始记录思想已由R承载；不要求Obsidian/飞书，不移植应用流程 |
| nature-paper-trans | I | PDF翻译成品为可选独立任务；不能替代T的日常讨论约束 |
| nature-proposal-writer | I | 开题/计划书非正文核心；不迁入整套独立pipeline |
| nature-paper2ppt | I | 答辩/汇报按需使用独立技能，不迁入正文核心 |
| nature-image2ppt | I | 图片到PPT不属于本轮正文写作范围 |
| nature-paper-to-patent | I | 专利是独立法律体裁，不迁入正文核心 |
| nature-social-science | I | 不迁入社科专用选题和判断流程 |

### 深层定位与可复查指纹

均相对于上述提交的 `skills/`。这里列关键blob指纹，便于将来判断变化；它们不是对脚本执行的证明。

| 路径 | Git blob |
|---|---|
| nature-reader/references/grounding-rules.md | `44ddd8d3d1af95765ed1d50a10d9f6c26f4f89ed` |
| nature-reader/references/equation-handling.md | `f257650999d8dff00a4cf60db29d923a537235a7` |
| nature-paper-card/references/evidence-and-provenance.md | `2b98b49b4c5f1c08c7464bf910b5d3a587028443` |
| nature-paper-xray/references/evidence-boundary.md | `edbbb4dab09f2a7690e32edd5b182d9048f575a1` |
| nature-citation/static/core/principles.md | `9e37ddc656a7283bdb5b23c384cc84dc6cc78642` |
| nature-ref-verifier/SKILL.md | `8d0216f4de9d641e265fb07194929fd41b66fbe0` |
| nature-data/references/policy-principles.md | `fe54c34f249fb22d7fbe7b90b1aa06ba2923e5e6` |
| nature-statistics/references/statistical-reporting.md | `47aec2e06c48c4313a80a3a26aabbc3fd886d2f8` |
| nature-figure/references/qa-contract.md | `fb4c8d5942a5f3ccd979f4cc0a7f62f1b06759cb` |
| nature-paper2word/references/format-requirements.md | `73820a6d1c7c059e0ff2eb82d0636541942a9022` |
| nature-writing/references/experiments.md | `6e76195b742c526368774d0a6572f0f2cd33c26c` |
| nature-writing/references/submission-package.md | `c05ec86abe4426325cd8b5fdac26ef73c5b04c96` |
| nature-reviewer/references/forensic-consistency-audit.md | `2aa8bcaa2da14298b31cdf9c045c524ec916e8a4` |
| nature-response/references/package-consistency-audit.md | `29e2bb93d4ed9e75ad6371de916e05216befe031` |
| nature-shared/core/consistency-sweep.md | `8b7e03263c808b914b57de7c701156f2de5ac8d5` |
| nature-shared/core/research-compliance.md | `ff555158b2109463f16c266c347d2ab459bbdd02` |
| nature-shared/core/ethics.md | `a6e6d063a8a41bc2294f02820265700272024c37` |
| nature-polishing/static/core/stance.md | `bb87579710c7111f4dbe16442d175a830f2e673c` |
| nature-polishing/static/core/failure-modes.md | `52e6d7cb8fbb422dc54844c2247a0f769cc35586` |

## PaperSpine 及其他来源

[PaperSpine](https://github.com/WUBING2023/PaperSpine) 本轮固定提交 `5c332ba8eaac811aa37d439c068993f67bf372a6`，MIT。读取当前 `src/skill/references/scientific-evidence-ledger.md`（blob `429955bb33219d9414dbde1e0df718bb88c963d7`）及 `publication-cycle-contracts.md`（blob `9dc9545f52f9eec03dd70cc7e1d74484ac18b786`），核对源码与分发/旧版本目录的区别。

采用证据状态、来源/结果联系、阶段规范和产物耦合至既有台账与R/D；不强制复制其JSON全套结构、自治编排、UI、目录或投稿引擎。没有复制或运行上游检查器，不能借用其测试结论。

既有四个humanizer及反防御性来源沿用[原迁移台账](external-skill-sources.md)。本轮检查的是内部一致性，不冒称重新完整审阅其最新上游。清理了三个深层指南和操作片段中会误删必要反例/边界的宽泛措辞；历史日志保留并由最新规则说明取代。

本地其他专项skill按“入口索引/相关条款”审阅，仅作协作和边界参考，不声明其全部实现已迁移：

| 来源 | 适用取舍 | 本地入口SHA-256 |
|---|---|---|
| uncertainty-and-units | 单位/不确定度检查原则至R/O，专用计算按需协作；不迁入无关量纲组 | `caaafa079a4eaac6012717bcf705dec0417b5434f5dbd1af934a3a36ad375722` |
| sympy | 脆弱代数变形优先符号工具；不把符号结果当力学模型有效性证明 | `bb97087bdddccc845401737ddc7f7a8da1c14ced5e8d40da01271c991ac46e23` |
| scientific-visualization | 真实数据、变换、最终尺寸和视觉完整性至O；不替代F后端门 | `8cbde7cdc10d959cf72cfd08335cc8ce996247eee6ebdb900eb64a4cb0ff34a3` |
| experimental-design | 独立单位/设计适用性参考；不因写作启动新试验 | `0a314eed103a4c7505bd1fbe80c527896d80b31d5a0fd47b26ccfd1eefb8963b` |
| statistical-analysis | 有输入且授权时执行统计；不一律强加检验 | `e112848726b3713267cac65e4e2c15491a0a26ee1ed628db01195f7e43f97997` |
| scikit-learn | 相关模型评估按需执行；环境/代码和训练不随技能自动迁移 | `a1765797d072ab40094522abe68fb04505d0881f66b7dfceeb8582422dbe488d` |
| shap | 解释能力不等于因果；执行按需且有数据/模型 | `9c395662e608accd60acb62158f1d25299b12ec0e40f9f94b70a46ec527d52c1` |
| abaqus-module-build | 保留模型、单位、验证和授权边界；不迁入求解器 | `116ca99b1c18371902362d645ca3047b94d51081618d18d8c1a7ea9a34a61bf3` |
| citation-management | 身份核验与来源可追踪参考；不默认生物医学检索路线 | `dc79fe1e8438dcf598040615d5323360c6a7ed0b868fc3ffc82512c871a1e3ff` |
| literature-review | 查询/覆盖记录参考；不把普通查文献冒称系统综述 | `16a9e85bcdcb9bb859e1646bf836e51b22900445ba2e367d8d75be05b5a5cba8` |
| scientific-writing | 基于证据的写作参考，不复制整套通用教材 | `511a2096bebecd8cf0f8212b9d262d37154ae1ba566eb385d93ac968682edbd1` |
| peer-review | 证据边界与人类责任参考，模拟审稿不冒称真实评审 | `fed0262d707aa1b1c4822e9fb05aa132e1cf333aff695a4de754272d42f5c98b` |

Word/PDF工作机制沿用既有专门流程，只有实际文件任务才加载对应技能。无关生物、临床、天文等技能不纳入。未知本地专项包许可证不作推断；本轮没有分发它们的正文或实现。

## 冲突处置与明确不迁移的规则

- 科学含义和必要技术披露优先于去防御/语言美化，不能以叙事为由隐藏不利结果。
- Crossref未命中不是假DOI证明；作者截断先区分格式要求与元数据丢失；版本/注册机构/官方记录需分别核验。
- 不采用“误差条重叠即统计不可区分”的自动判断。重叠本身既不证明显著差异，也不证明无差异/等效。
- 不将固定消融包、全部生医合规项或Nature图形版式强加到土木硕士论文。
- 不借用上游脚本名称假装本地已经运行。共享规则在本skill内自包含，外部执行依赖在相应分支才检查。
- 不复制上游截图、数据、示例原文、私人目录、代码或测试效果声明。本轮数值工具为本地新实现，只处理其公开声明的CSV检查。

## 能力验收与尚需按任务验证的部分

运行 `scripts/validate_all.py` 验证本skill结构与已列脚本，另检查全体修改链接。数值工具的测试包括复算、比例/百分数、零分母、缺失、R平方定义域、错误指标、组间重叠、哈希变化、路径边界和只读CLI。结构通过不代表行为通过。

重大整合应按skill-creator进行独立前向任务：给原始材料和真实请求，不给预期答案。审查实际输出和产物，保留失败、修正和未执行项；不能以关键词命中充当科学审查正确。运行结果应记录在更新日志或单独结果记录，而不预填通过。

本轮不自动运行FE/ML训练、不调用外部生图/付费服务、不写Zotero、不更改用户论文/冻结模板、不发布GitHub。最终Word页面、真实文献全篇翻译、专业绘图导出与各客户端实际发现/运行，需要相应任务和环境，不能由本次规则整合推定已验证。
