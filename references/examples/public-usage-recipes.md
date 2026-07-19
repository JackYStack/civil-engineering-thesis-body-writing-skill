# Public Usage Recipes

These examples are safe for public distribution. They are prompt templates, not sample-paper content. Replace bracketed fields with the user's real material at runtime.

## Case: Chinese Thesis Section Draft

Use when the user wants to write one thesis subsection in several small passes.

Prompt:

```text
使用 civil-thesis-body-writing，按中文土木硕士论文风格撰写 [章节名]。
研究对象：[构件/材料/结构体系]
本节任务：[试验设计/有限元验证/参数分析/机器学习模型/模型应用]
已有证据：[图表编号、公式、数据、模型指标、试验现象]
边界：[参数范围、荷载条件、材料类型、模型假设]
要求：先给本节主线和段落安排，再写第 1 个段落；不要编造数据。
```

Expected route: `thesis-body`, matching section, `user-materials`, `draft`.

## Case: Anti-Vague Thesis Revision

Use when a paragraph contains vague judgments such as "效果较好", "影响显著", or "具有重要工程意义".

Prompt:

```text
使用 civil-thesis-body-writing 对以下段落做防空泛润色。
原文：[粘贴段落]
已知证据：[误差、曲线阶段、图表编号、对比基准；没有就写“暂无”]
要求：保留原意，补足对象-指标-证据-边界；缺数据时降级表述。
```

Expected route: `thesis-body`, `revise`, anti-vague language pass.

## Case: SCI Abstract Rewrite

Use when the user wants to turn thesis-style Chinese material into a small-paper or SCI abstract.

Prompt:

```text
使用 civil-thesis-body-writing，将以下材料改写为工程期刊 SCI 摘要。
目标期刊/期刊族：[如 Engineering Structures / Structures / Journal of Building Engineering；没有则写“工程结构类期刊”]
中心问题：[一句话]
方法：[试验/有限元/机器学习/解析模型/混合方法]
数据与对象：[样本量、构件类型、输入变量、输出指标]
关键结果：[可公开的指标、误差、排序、对比结论]
应用边界：[初步设计/参数筛选/复核前评估/指定参数范围]
要求：英文工程期刊稳健风；不要把辅助工具写成规范设计替代。
```

Expected route: `paper-sci`, optional `target-journal-polish`, `revise`.

## Case: Citation Reduction And Support Table

Use when a draft paragraph has too many citations or weak citation support.

Prompt:

```text
使用 civil-thesis-body-writing 精简以下引言引用。
正文：[粘贴段落]
已有参考文献/本地文库线索：[参考文献表、Zotero 条目、项目文件路径或“暂无”]
要求：本地/Zotero 优先；每个保留引用必须说明支撑哪句话；不要重复引用同一篇论文承担多个无关论点。
```

Expected route: `citation-support`, local-first search, support grading.

## Case: DOCX Safe Revision

Use when the user asks to revise a Word manuscript without breaking formatting.

Prompt:

```text
使用 civil-thesis-body-writing 安全修改这个 Word 文稿。
文件路径：[docx 路径]
修改范围：[摘要/结论/4.2 模型应用/全文语言润色]
目标风格：[中文硕士论文/工程 SCI/目标期刊]
保留要求：[公式、图表、编号、引用、批注、修订痕迹]
要求：不要覆盖原文件；先说明修改范围和风险，再新建修改版本。
```

Expected route: `docx-revision`, optional writing route for replacement text.

## Case: DOCX Creation Or Markdown Conversion

Use when the user wants a new Word manuscript or a formatted `.docx` generated from Markdown.

Prompt:

```text
使用 civil-thesis-body-writing 创建/转换 Word 论文。
任务分支：[新建 DOCX / Markdown 转 DOCX]
源文件或材料：[路径]
格式依据：[学校/期刊模板路径、书面格式要求；没有则写“待确认”]
对象要求：[标题编号、目录、三线表、图题表题、Word 公式、引用、页眉页脚、页码]
要求：先列格式合同和缺失项；不要把通用格式说成学校官方格式；生成新文件并做渲染抽查。
```

Expected route: `docx-revision`, `create` or `convert` branch, formatting-contract and rendered-output validation.

## Case: InstSci To Zotero Import Preview

Use when the user wants to retrieve papers and organize them in Zotero.

Prompt:

```text
使用 civil-thesis-body-writing 整理 InstSci 获取的论文，并准备通过 Zotero MCP 导入 Zotero。
输入：[DOI/title list 或 InstSci 输出目录]
目标 collection：[集合名]
标签规则：[主题标签、access-status 标签、待核查标签]
要求：先给导入预览和查重结果；没有确认前不要写入 Zotero。
```

Expected route: `instsci-zotero`, import preview before any library write.

## Case: Target-Journal Full Manuscript Polish

Use when the user has a complete manuscript and wants journal-style adaptation.

Prompt:

```text
使用 civil-thesis-body-writing 做目标期刊润色修改。
目标期刊：[期刊名或期刊族]
稿件路径：[docx/md/latex 路径]
文章类型：[Article/Review/Technical note]
重点：[摘要、引言、结果讨论、结论、全文风格量化对比]
要求：先调研目标期刊和相似范文，再给全文改写蓝图；不要直接整篇重写。
```

Expected route: `target-journal-polish`, with exemplar/style research before rewrite.

## Case: Thesis Format And Final Audit

Use when the user wants a rule-based format review before supervisor handoff, defense, or submission.

Prompt:

```text
使用 civil-thesis-body-writing 审查论文格式与终稿 readiness。
论文材料：[LaTeX 项目 / DOCX / PDF 路径]
格式依据：[学校或期刊规范、模板、规则包路径和版本]
交付阶段：[导师审阅 / 答辩 / 预提交 / 最终提交]
要求：先确定事实源和审查维度；输出 PASS/WARN/BLOCK/UNAVAILABLE；把格式问题、终稿残留、统计符号、交叉引用和缺失验证证据分开；所有修复先预览，不直接改原文件。
```

Expected route: `thesis-audit`, calibrated format matrix, structured evidence, preview-first bounded fixes.

## Case: Scientific Figure Colour Selection Or Audit

Use when the user wants a restrained palette for thesis/journal figures or needs to check an existing figure for semantic and accessibility problems.

Prompt:

```text
使用 civil-thesis-body-writing 为科研图表选择/审查配色。
图表任务：[试验-有限元对比 / 参数分析 / ML模型比较 / SHAP / 云图 / 构造示意图]
变量类型与顺序：[名义分类、连续、递增参数、正负效应]
系列数量与基准组：[填写]
目标期刊或学校模板：[填写或“待确认”]
现有图或绘图代码：[路径；没有则写“暂无”]
要求：给出 Hex 色值和对象映射；颜色之外同时指定标记/线型；检查色觉、灰度、终稿尺寸和期刊边界；不要把示例色卡称为 Nature 官方配色。
```

Expected route: matching manuscript mode and section, then `references/style/scientific-figure-color.md` for palette and QA decisions.

## Case: Publication Figure Planning, Rendering, And Manuscript Reintegration

Use when the user wants an actual thesis/journal figure plus the corresponding caption or results text.

Prompt:

```text
使用 civil-thesis-body-writing 与 nature-figure 协作生成投稿图。
论文位置与图件任务：[章节、拟表达的核心结论]
数据/代码/现有图路径：[填写]
变量、单位、分组顺序和基准组：[填写]
目标期刊与输出：[单栏/双栏；SVG/PDF/TIFF/PNG；没有则写“待确认”]
拟定面板：[a/b/c 或“请根据证据规划”]
正文需求：[仅绘图 / 同时修改图题和结果段]
要求：先建立 figure brief；实际绘图、Python/R 后端选择、导出与视觉 QA 由 nature-figure 执行；不要编造缺失数据；最后报告真实生成的文件和正文再集成结果。
```

Expected route: `figure-support`; complete `nature-figure-cooperation.md`, invoke `nature-figure` for execution, then return to the civil-writing mode for caption/results reintegration.
