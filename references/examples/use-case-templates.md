# Use-Case Templates for Civil Thesis and Paper Writing

Use this file when the user asks how to use `civil-thesis-body-writing`, requests prompt templates, or wants a formal manuscript-level use of the skill. Treat these as starting templates, not fixed output forms.

## 1. 大论文二/三级节正文写作

User prompt template:

```md
使用 civil-thesis-body-writing，帮我写/改写【章节编号+标题】。

研究对象：
方法：
变量/工况：
已有证据：图X、表X、公式X、数据范围...
想证明的结论：
边界/限制：
引用要求：是否需要本地优先检索文献。
输出要求：正文稿 + 写作依据 + 需补充或确认。
```

Expected output:

- `正文稿`：按“对象-方法-参数-指标-结果-机理-边界”展开。
- `引用候选清单`：仅在背景、方法依据、参数依据或对比讨论需要文献时输出。
- `写作依据`：列明图表、公式、数据和参考文献如何支撑正文。
- `需补充或确认`：缺少数值、图表编号、参数范围或支撑文献时列出。

## 2. 小论文/SCI 摘要重写

User prompt template:

```md
使用 civil-thesis-body-writing，按 SCI 工程期刊风格重写摘要。

题目：
研究对象：
研究问题/空白：
方法：
数据/样本量：
输入变量：
输出指标：
关键结果：
应用边界：
目标期刊：
```

Expected output:

- `论点地图`：中心问题、主张、证据、变量、边界、审稿风险。
- `正文稿`：按“problem -> method -> object/data -> variables -> results -> boundary”组织。
- `证据与图表对应`：每个结果句对应指标、图表或数据。
- `SCI写作QC`：指出过强贡献、缺少边界或缺少量化结果的位置。

## 3. 引言与研究现状写作

User prompt template:

```md
使用 civil-thesis-body-writing 写【研究背景/国内外研究现状】。

主题：
希望分成的研究脉络：
已有参考文献或 Zotero/本地文库位置：
必须覆盖的概念：
不希望展开的内容：
输出引用方式：临时编号 [R1] 或沿用原编号。
```

Expected output:

- 先扫描哪些句子需要文献支撑。
- 本地文献/Zotero/已有参考文献优先，不足时再网络补充。
- 每篇候选文献标注引用功能：`background`、`gap`、`method`、`comparison` 或 `boundary`。
- 避免按论文逐篇罗列，按技术问题综合。

## 4. Results and Discussion 段落写作

User prompt template:

```md
使用 civil-thesis-body-writing 写 Results and Discussion。

图/表：
响应指标：
主要趋势：
可用数值：
对比基准：
力学解释：
需要对比的已有研究/规范：
适用范围：
```

Expected output:

- 每段先落到图表或指标，再解释趋势和机理。
- 有数据时写数值和对比基准；无数据时降级为趋势描述。
- 讨论必须包含机制、比较、边界，避免重复结果。
- 外部文献只用于机制或对比，不替代本文结果。

## 5. 模型应用/GUI 辅助设计段落

User prompt template:

```md
使用 civil-thesis-body-writing 改写模型应用章节。

工具/GUI功能：
输入参数：
模型输出：
后处理公式或工程响应：
SHAP/可解释性用途：
验证方式：
不能过度表述的点：
```

Expected output:

- 先写工具如何使用，再写预测结果如何转化为工程指标。
- 对 PCSP 任务，明确 `DCA_s` 可用于等效刚度、服役阶段挠度等后处理，`DCA_c` 可用于极限承载力或弯矩承载力估算。
- SHAP 只解释模型预测行为和参数调整方向，不写成独立因果证明。
- GUI 定位为初步方案筛选、快速评估和参数优化辅助，不替代规范验算、试验或有限元复核。

## 6. 中译英逻辑校核与英文投稿稿

User prompt template:

```md
使用 civil-thesis-body-writing 做中译英逻辑校核，再给英文稿。

中文原文：
术语表：
目标期刊：
需要保留的变量/公式/图表编号：
需要降级的中文表述：
输出：逻辑校准 + 英文稿 + 作者需确认。
```

Expected output:

- 先锁定术语、研究对象、指标、数据和边界。
- 先改逻辑强度，再翻译句子。
- 不把中文的“有效、显著、具有价值”翻译成更强英文。
- 英文采用工程期刊清晰风格，优先主谓明确和变量一致。

## 7. 结论防空泛改写

User prompt template:

```md
使用 civil-thesis-body-writing 检查并改写结论。

原结论：
对应证据：图/表/公式/指标/章节
可保留的数值：
适用边界：
```

Expected output:

- 每条结论只保留一个主张。
- 每条结论必须对应至少一个证据来源。
- `吻合较好`、`精度较高`、`有效` 等词必须配指标、基准或边界。
- 缺少数据时用占位提示，而不是编造数值。

## 8. 文稿级正式审查与使用

User prompt template:

```md
使用 civil-thesis-body-writing 正式审查这篇论文/章节。

文件路径：
目标：投稿稿/硕士论文/中英对照稿/导师修改稿
重点检查：
1. 论点链条
2. 术语和符号一致性
3. 图表与正文对应
4. 引用功能
5. 防空泛表达
6. 可直接替换文本
输出为 md 文件。
```

Expected output:

- `文稿级论点地图`：中心问题、主张、证据、变量、边界、审稿风险。
- `问题清单`：按严重程度排序，先列会影响投稿或答辩说服力的问题。
- `章节审查`：题名、摘要、引言、方法、结果、讨论/应用、结论分别评价。
- `可直接替换文本`：优先给题名、摘要、关键应用段和结论。
- `后续修改路线`：按“先术语/符号 -> 再摘要结论 -> 再正文证据 -> 最后语言润色”推进。

## 9. 正式章节/论文重构：主线-证据-矩阵流程

User prompt template:

```md
使用 civil-thesis-body-writing，按正式流程重构【章节/论文/Word文件】。

文件或原文：
目标类型：硕士论文正文/小论文/SCI投稿稿/中英对照稿/导师修改稿
核心研究对象：
希望突出的主线：
已有证据：图、表、公式、数据、试验现象、FE验证、ML指标、SHAP结果、GUI功能等
必须保留的内容：
需要删减或降级的表述：
引用要求：本地文库/Zotero优先，必要时网络补充
输出要求：主线校准 + 证据库摘要 + 写作理由矩阵 + 修改稿 + 风险与需确认
```

Expected output:

- `主线校准`：明确本节/本文要证明的问题、技术路径、证据路线、边界和禁止过度表述。
- `证据库摘要`：列出可用于正文的图表、公式、数据、文献和风险。
- `写作理由矩阵`：说明每个写作单元为什么保留、移动、合并、重写、删除或补证据。
- `正文稿/修改稿`：按矩阵执行，不做简单句子拼接。
- `证据与引用对应`：每个关键结论能追溯到用户证据或 claim 级引用。
- `风险与需确认`：缺数据、缺全文、Word对象风险、公式/图表编号风险等。

## 10. 目标期刊润色修改：调研-范文-量化对比-整篇重写

User prompt template:

```md
使用 civil-thesis-body-writing，按目标期刊润色修改整篇论文。

目标期刊：
文章类型：Research article / Review / Short communication / 其他
稿件文件路径：
研究对象：
核心贡献/亮点：
已有证据：图、表、公式、数据、试验、FE、ML指标、SHAP、GUI等
本地参考文献或Zotero/论文库路径：
范文要求：自动检索/只用本地/我指定范文
输出要求：
1. 目标期刊调研
2. 3-6篇同方向范文索引
3. 全文风格量化对比
4. 亮点-期刊匹配矩阵
5. 重写蓝图
6. 修改稿或新docx
7. 投稿前风险
```

Expected output:

- `目标期刊调研`：核查当前 aims and scope、author guide、文章类型、摘要/关键词/图表/声明等要求。
- `范文索引`：优先本地/Zotero，必要时网络补充；只使用开放获取、官方页面、用户提供或有权限访问的全文；无法获取全文时标注 `metadata only`。
- `全文风格量化对比`：比较章节结构、摘要长度与 rhetorical moves、引言段落和引用密度、方法深度、结果/讨论比例、图表数量、结论条数和边界表述。
- `亮点-期刊匹配矩阵`：判断本文贡献与目标期刊偏好的匹配程度，并指出需要补证据、降级或强化的位置。
- `重写蓝图`：先定结构和每个单元的修改动作，再写正文。
- `修改稿/修改文件`：按目标期刊风格重写整篇或关键部分；若改 Word，遵守 OOXML 安全策略并新建文件。
- `投稿前风险`：列出缺少全文、期刊要求未满足、证据不足、引用薄弱、图表/格式风险等。

## 11. Zotero 文库辅助写作/更新 Skill

User prompt template:

```md
使用 civil-thesis-body-writing，调用 Zotero 文库辅助写作/更新规则。

主题：
写作任务：绪论/研究现状/SCI引言/Discussion/目标期刊润色/更新skill
检索关键词：
优先方向：PCSP/连接件/DCA/有限元/解析模型/机器学习/SHAP/其他
是否需要全文核查：是/否
输出要求：
1. Zotero检索概况
2. 文献谱系图
3. 可迁移写作结构
4. claim级引用候选
5. 正文稿或skill更新建议
```

Expected output:

- `Zotero检索概况`：列出查询词、命中数量、代表性条目、附件/全文状态。
- `文献谱系图`：按综述、连接件试验、墙板试验、FE/解析模型、ML预测等聚类。
- `可迁移写作结构`：学习文章架构、段落功能、证据链、讨论方式，不复制句子。
- `claim级引用候选`：每条候选绑定一个可支撑的句子或论点。
- `限制`：标注 metadata-only、未核全文、需OCR、需用户确认的文献。

If the task is to update the skill, expected changed files may include:

- `workflows/citation-workflow.md`
- `workflows/zotero-library-learning.md`
- `examples/zotero-corpus-profile.md`
- `style/local-paper-style.md`
- `sections/sci-writing-principles.md`

## 12. Science-skills / 外部数据库辅助检索与写作

User prompt template:

```md
使用 civil-thesis-body-writing，并按 science-skills 式来源纪律进行外部检索辅助写作。

写作任务：绪论/研究现状/方法依据/目标期刊润色/Discussion/其他
优先本地来源：Zotero/本地PDF/已有参考文献/analysis文件
外部来源：OpenAlex/CrossRef/Semantic Scholar/出版商页面/期刊官网/标准官网/其他
检索主题：
必须支撑的论点：
是否允许网络补充：
输出要求：
1. 外部来源记录
2. claim级引用候选
3. 正文稿
4. 引用边界和需确认
```

Expected output:

- `外部来源记录`：列出工具/来源、查询词或筛选规则、审阅数量、选用 DOI/URL/path、全文/摘要/元数据状态。
- `claim级引用候选`：每条候选绑定一个具体句子，不用题名相关性代替支撑关系。
- `正文稿`：仅把已核查或边界清楚的来源写入正文，网络补充文献标注 `待核对全文`。
- `引用边界和需确认`：说明哪些只是 metadata-only、哪些缺全文、哪些需要标准原文或作者确认。
- 不要求把外部检索结果全部写进正文；检索结果应先服务于论点筛选和证据校核。

## 13. Zotero-xpropel `[zotero_fulltext]` 全文语料学习

User prompt template:

```md
使用 civil-thesis-body-writing，并调用 Zotero-xpropel [zotero_fulltext] 读取论文库，进行全文语料学习。

主题：
优先方向：PCSP/DCA/连接件/有限元/解析模型/机器学习/目标期刊范文/其他
检索关键词：
读取规模：先抽样 5-20 篇 / 指定文献 / 全库分批
重点抽取：
1. 论文主线
2. 参数变量
3. 响应指标
4. 图表/公式证据锚点
5. 可迁移写作结构
6. claim级引用候选
输出要求：保存调查报告 + 更新 skill 规则/只给建议
```

Expected output:

- `Zotero全文检索概况`：查询词、命中数量、抽样规则、全文来源状态。
- `全文样本文献索引`：Zotero key、题名、年份、来源状态、读取边界、迁移价值。
- `参数变量谱系`：按几何、材料、连接件、边界条件、响应指标、ML变量分类。
- `可迁移写作规则`：说明哪些规则进入章节模板、引用流程、SCI结构、语料画像或防空泛规则。
- `已更新/建议更新文件`：列出实际修改的 reference 文件。
- `边界与需确认`：标注全文片段抽样、metadata-only、缺OCR、未核全文等限制。

## 14. InstSci 论文获取与目标期刊范文采集

User prompt template:

```md
使用 civil-thesis-body-writing，并调用 InstSci 辅助获取论文全文/目标期刊范文。

任务类型：引用全文核查 / 目标期刊范文采集 / DOI批量下载 / 出版社PDF访问验证
目标期刊或主题：
DOI/题名列表：
本地优先路径或Zotero库：
允许的访问方式：本地全文 / 开放获取 / 出版社页面 / 机构浏览器验证
输出要求：
1. 检索与访问记录
2. 文献/范文索引
3. 访问状态与证据边界
4. 可用于写作或引用的候选
5. 未完成核查
```

Expected output:

- `检索与访问记录`：列出 DOI、题名、来源、路径、InstSci route、访问状态和是否检查全文。
- `访问状态`：使用 `open access retrieved`、`browser verified`、`HTTP preflight`、`auth_required`、`blocked`、`unverified PDF` 等标签。
- `引用候选`：只有检查过相关全文/摘要/官方页面的来源才能进入 claim 级引用候选。
- `范文用途`：目标期刊范文可用于结构和风格学习，但不自动成为正文引用。
- `安全边界`：不要求用户粘贴密码、验证码、cookie 或 API key；SSO/2FA/CAPTCHA 由用户在可见浏览器中完成。

## 15. thesis-skills 确定性审查与 Readiness Gate

User prompt template:

```md
使用 civil-thesis-body-writing，并调用 quzhiii/thesis-skills 对论文项目做确定性审查。

项目路径：
稿件类型：LaTeX项目 / Word转LaTeX草稿 / 参考文献审查 / 投稿前检查 / 答辩前检查
规则集：university-generic / 自定义规则
是否编译：是/否
是否只预览修复：是，先不应用
重点检查：
1. 引用-参考文献一致性
2. 格式与模板风险
3. 语言空泛或AI痕迹
4. 章节完整性
5. 最终提交阻断项
```

Expected output:

- `Readiness Gate`：给出 `PASS`、`WARN` 或 `BLOCK`，并说明触发原因。
- `关键报告`：概括 run summary、citation/reference issues、format/language/content risks。
- `可执行修复`：默认只做 `thesis-fix --apply false` 预览；实际应用前需用户确认。
- `正文写作联动`：把确定性检查发现的空泛、缺引用、缺图表对应、章节缺口，转化为可改写的正文任务。
- `边界`：thesis-skills 更适合 LaTeX/项目级审查；Word/docx 修改仍遵守 OOXML 安全策略。

## 16. InstSci 获取论文整理并通过 Zotero MCP 导入 Zotero

User prompt template:

```md
使用 civil-thesis-body-writing，把 InstSci 获取到的论文整理并通过 Zotero MCP 导入 Zotero。

InstSci 输出目录：
manifest 路径：
PDF 文件夹：
目标 Zotero collection：
导入模式：只预览 / 创建缺失条目 / 只挂PDF / 完整导入
导入规则：
1. DOI 查重
2. 缺 DOI 的列为待确认
3. 导入 PDF 附件
4. 写入 InstSci 访问状态标签
5. 为每篇文献创建获取记录子笔记
6. 导入前先给我确认清单
```

Expected output:

- `导入预览`：读取 InstSci manifest/PDF，按 DOI 和题名查重，列出每篇文献的拟操作。
- `需确认操作`：明确哪些 Zotero 写入会发生，包括新建条目、导入附件、加标签、建子笔记或加入 collection。
- `Zotero写入结果`：用户确认后再执行，报告 item key、附件状态、标签、子笔记和失败项。
- `访问状态标签`：保留 `open access retrieved`、`browser verified`、`HTTP preflight`、`auth_required`、`blocked`、`unverified PDF`、`待核全文` 等状态。
- `引用边界`：导入 Zotero 不等于可引用；后续仍需全文读取和 claim 级支撑判断。
