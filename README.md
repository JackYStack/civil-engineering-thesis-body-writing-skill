<div align="center">
  <img src="assets/readme-banner-cn.svg" alt="土木工程论文写作 Skill" width="100%">
  <p>
    <a href="https://github.com/JackYStack/civil-engineering-thesis-body-writing-skill/actions/workflows/validate.yml"><img alt="Validation" src="https://github.com/JackYStack/civil-engineering-thesis-body-writing-skill/actions/workflows/validate.yml/badge.svg"></a>
    <img alt="Platform Codex" src="https://img.shields.io/badge/platform-Codex-303942">
    <img alt="Claude Code 适配" src="https://img.shields.io/badge/adapter-Claude_Code-64746b">
    <img alt="WorkBuddy 适配" src="https://img.shields.io/badge/adapter-WorkBuddy-64746b">
    <a href="README.en.md"><img alt="中文与 English" src="https://img.shields.io/badge/language-中文%20%7C%20English-f4c542"></a>
  </p>
  <p>
    <a href="#快速使用">快速使用</a> ·
    <a href="#常用任务模板">任务模板</a> ·
    <a href="#安装">安装</a> ·
    <a href="#使用边界">使用边界</a> ·
    <a href="#验证">验证</a> ·
    <a href="#致谢与参考来源">致谢</a> ·
    <a href="README.en.md">English</a>
  </p>
</div>

`civil-thesis-body-writing` 是面向土木工程学位论文与工程期刊稿件的 Agent skill，覆盖文献阅读与中英翻译、证据组织、正文起草与润色、试验/有限元/机器学习报告、公式图表检查、审稿修订及 Word 交付。以 Codex 为默认安装平台，提供 Claude Code 和 WorkBuddy 安装/技能包适配；不同客户端的工具和权限分别配置，不随规则包自动迁移。

它将研究对象、数据、图表、公式与文献关联到具体论点，保留来源、条件和真实不确定性。日常文献讨论也区分原文、忠实译文与解释；修改结果后检查正文、摘要、结论、图表和审稿回复的一致性。语言修改沿用最小清理、常规润色和新稿写作三种强度，不以去防御为由删除必要反例或假设。

> 不编造数据、公式、试验结果或参考文献，不把预测精度写成规范设计安全。科学含义、数值、可编辑对象和页面显示分别核对；缺少材料或工具时明确说明，不冒称完成。

规则导航：[研究与证据](references/workflows/research-integrity-and-reproducibility.md) · [文献翻译](references/workflows/literature-translation-grounding.md) · [公式图表](references/workflows/equation-figure-table-integrity.md) · [一致性与交付](references/workflows/manuscript-consistency-and-delivery.md) · [整合范围与未迁移项](references/meta/systematic-integration-map.md)

## 快速使用

1. 使用 `git clone https://github.com/JackYStack/civil-engineering-thesis-body-writing-skill.git` 获取仓库，或在 GitHub 仓库页面选择 `Code -> Download ZIP` 并完整解压。
2. Codex 安装：Windows PowerShell 使用 `.\scripts\install.ps1`，Linux/macOS Bash 使用 `bash scripts/install.sh`；其他平台见 [Claude Code 与 WorkBuddy](#claude-code-与-workbuddy)。
3. 在目标客户端加载技能后发送：`使用 civil-thesis-body-writing 修改这段土木工程论文正文，保留数据、术语、公式和引用，不补写没有证据的结论。` Codex 安装后需重启；其他平台按下方适配步骤启用。

## 常用任务模板

| 想完成的任务 | 可直接使用的提示词 |
| --- | --- |
| 修改学位论文小节 | `使用 civil-thesis-body-writing 修改这一小节。保留图表、公式、参数和引用，删除空泛判断，并列出缺少的证据。` |
| 定稿最小清理 | `使用 civil-thesis-body-writing 对这段定稿做最小清理，只改可定位的套话或表达缺陷。其余文字、段落结构、术语、数字、公式和引用不动，保留真实不确定性。` |
| 按审稿意见微修 | `使用 civil-thesis-body-writing 回应这条审稿意见，只修改相关段落，保留原文风格。给出可检索的插入或替换位置、修改稿和简短说明，不编造页码或行号。` |
| 梳理论证与贡献 | `使用 civil-thesis-body-writing 围绕最有证据支持的贡献梳理本节论证，删除冗余自辩，不隐瞒影响结论的不利发现、必要假设或适用条件。` |
| 核查或精简引用 | `使用 civil-thesis-body-writing 核查这些引用分别支持哪一句话，按强支持、部分支持、背景支持和不建议引用分级。` |
| 翻译并解释文献 | `使用 civil-thesis-body-writing 翻译并解释这段文献，注明实际来源和读取范围，保留否定、数值归属和工况；将忠实译文、你的解释及能支持的正文论点分开。` |
| 检查试验、有限元或机器学习报告 | `使用 civil-thesis-body-writing 检查这段方法与结果的证据链、样本单位、标定/验证、数据划分和指标定义；只修改表述，不新增试验或启动计算。` |
| 核对公式与图表 | `使用 civil-thesis-body-writing 核查公式来源、符号、单位、假设和适用域，以及图表的数据、变换、误差与正文对应关系。排版和科学内容分开检查，无法确认处不要猜。` |
| 复核表格数值 | `使用 civil-thesis-body-writing 按明确口径只读复核这个 CSV 的均值、变化率、回归误差及组间重叠。先确认列和指标映射，不改原始数据，报告实际执行的检查。` |
| 更新摘要、结论和回复引用 | `使用 civil-thesis-body-writing 根据这次结果变更检查受影响的正文、图表、摘要、结论和审稿回复；区分建议修改与当前文件中已确认的修改，不虚构页码。` |
| 创建、转换或安全修改 Word 稿件 | `使用 civil-thesis-body-writing 处理这个 Word 任务。先区分新建、Markdown 转换或已有 DOCX 修订，再按学校/期刊模板生成新文件并校核公式、编号、域和兼容性。` |
| 整理 InstSci/Zotero 文献 | `使用 civil-thesis-body-writing 整理这些检索结果，先给 Zotero 导入预览和查重结果，不直接写入文库。` |
| 按目标期刊润色 | `使用 civil-thesis-body-writing 调研目标期刊与同方向范文，先给出结构和深度差异，再制定整篇修改方案。` |
| 规划或生成科研图表 | `使用 civil-thesis-body-writing 先建立图件论点、数据和面板 brief，再调用 nature-figure 绘图、导出和 QA，最后补写图题与结果段。` |

## 工作方式

```mermaid
flowchart TD
    A[文稿、数据、图表、公式与文献] --> B[来源定位、证据库与术语台账]
    B --> C[按体裁、章节和任务加载规则]
    C --> D[起草、翻译、润色、引用或文档修订]
    D --> E[科学含义、数值及跨章节一致性核对]
    E --> F[正文、译文、审查意见或文件交付]
    D -. 按需且获得授权 .-> G[专项绘图、计算与文档工具]
    G --> H[核对实际产物、原生对象和渲染]
    H --> F
```

普通小段修改只加载相关规则，不强制运行整套流程。只读数值工具可复算显式映射的 CSV；绘图、符号/统计计算、FE 求解和 Word/PDF 渲染由可用专项工具执行，未执行的步骤不计为通过。

## 主要能力

| 工作流 | 直接产物 | 关键边界 |
| --- | --- | --- |
| 学位论文正文 | 按章节任务组织的中文正文 | 以用户图表、公式和数据为主要证据 |
| 独立期刊稿件/SCI | 摘要、引言、结果讨论、结论与亮点的写作或润色 | 不提供“大论文改 SCI”或从学位论文章节抽取、压缩成期刊稿件的功能 |
| 学术表达清理 | 按最小清理、常规润色或新稿写作强度处理的正文与修改说明 | 不机械禁词或强制句式变化；核对数字、术语、引用及其对应关系 |
| 审稿局部修订 | 对应审稿问题的插入/替换位置、修改段落及回复交接信息 | 保留有效原文；区分建议修改与实际完成；仅在需要时协作 `nature-response` 组装回复包 |
| 贡献组织与反防御性写作 | 以证据组织的中心主张、实验职责与章节论证 | 删除冗余自辩而非必要披露，不把局部优势写成全面领先 |
| 引用核查 | 临时引用、候选清单与支持等级 | 检索命中或题名相似不等于全文支持 |
| 文献阅读与中英翻译 | 有出处和读取范围的译文、解释与正文使用建议 | 日常讨论也保留否定、数值归属和条件；译文与推论分开，不拿摘要补全文 |
| 研究与公式图表完整性 | 试验/有限元/机器学习报告检查、公式来源与适用域、图表数据核对 | 科学含义、数值、原生对象和页面显示分别检查；不以排版或量纲通过保证模型有效 |
| 只读数值核对 | 声明口径的 CSV 聚合、变化率、回归误差和组间重叠报告 | 只检查显式映射，不自动理解论文、证明无泄漏或修改原始数据 |
| 跨章节与交付一致性 | 摘要/结论/图表及审稿回复的联动检查 | 数据或措辞修改后核对受影响位置；声明与访问权限必须有实际依据 |
| DOCX 创建与修改 | 新建、Markdown 转换或保留格式的修订版本 | 模板优先；默认不覆盖原文件；检查原生 Word 对象和渲染结果 |
| InstSci/Zotero | 检索整理、导入预览与查重结果 | 写入文库前确认，访问成功不等于可引用 |
| 目标期刊润色 | 期刊要求、范文差异与全文修改蓝图 | 先调研后重写，不机械模仿范文句式 |
| 格式与终稿审查 | 规则依据、格式问题台账、Readiness Gate 与修复预览 | 通用规则不等于学校合规；跳过的检查不能记为通过 |
| 科研图表协作 | 图件 brief、语义化配色、nature-figure 绘图交接、产物 QA 与正文再集成 | 正文 Skill 不绕过 Python/R 后端门；没有数据或产物时不声称已生成 |

具体规则见[学术表达清理指南](references/style/academic-prose-cleanup.md)、[审稿局部修订流程](references/workflows/reviewer-driven-revision.md)和[反防御性写作指南](references/architecture/evidence-led-narrative-and-defensive-writing.md)。三种语言处理强度沿用现有起草/修订操作，不是额外安装的独立 skill。

全流程覆盖、已审来源、采用/协作/排除理由及未迁移功能见[系统整合映射](references/meta/systematic-integration-map.md)。专业绘图、符号计算、统计、FE 求解、Word/PDF 渲染按任务和实际环境协作，不因整合规则而自动安装或运行。

## 安装

### Claude Code 与 WorkBuddy

以下命令在仓库根目录执行，需要 Python 3.10+；Codex 用户继续使用下方原有安装方式。

```shell
python -X utf8 scripts/install_agent.py install --agent claude-code --scope user
python -X utf8 scripts/install_agent.py install --agent workbuddy --scope project --project-root "/path/to/project"
python -X utf8 scripts/install_agent.py package --agent workbuddy --output "/path/to/output/civil-thesis-body-writing-workbuddy.zip"
```

Claude Code 安装后使用 `/civil-thesis-body-writing`。WorkBuddy 可在支持本地 `.codebuddy/` 配置的项目中使用，或通过技能页上传导出包并完成安全确认；不猜测全局目录，不自动部署到云端。已有安装默认不覆盖，确认更新后加 `--replace`，先备份再安装。

三平台共享写作规则，不共享 MCP、权限、凭据或其他技能。缺少外部连接、Word/PDF 渲染或 `nature-figure` 等能力时，跳过对应动作并说明，不能用普通文字冒充已执行产物。安装/打包适配不代表客户端已经完成实际发现和调用。完整步骤与跳过清单见[Agent 适配指南](references/workflows/agent-compatibility.md)。

### 从仓库安装（推荐）

- **前提条件：** 已安装 Codex，可访问 GitHub 仓库，并具备 Git 或浏览器，以及 PowerShell 或 Bash。
- **操作：** 运行 `git clone https://github.com/JackYStack/civil-engineering-thesis-body-writing-skill.git`，或在仓库页面选择 `Code -> Download ZIP` 并完整解压；随后在仓库目录运行 Windows 的 `.\scripts\install.ps1` 或 Linux/macOS 的 `bash scripts/install.sh`。
- **默认目标：** Windows 为 `$HOME\.codex\skills\civil-thesis-body-writing`；Linux/macOS 为 `${CODEX_HOME:-$HOME/.codex}/skills/civil-thesis-body-writing`。
- **已有安装：** 安装脚本先把已有目录重命名为同级的 `civil-thesis-body-writing.bak-YYYYMMDD-HHMMSS`，再复制当前仓库内容。
- **重启：** 安装完成后重启 Codex。
- **验证：** 运行[共享验证提示词](#安装验证)。

### Windows

- **前提条件：** 已安装 Codex 和 PowerShell，并已取得包含 `SKILL.md`、`manifest.yaml`、`static/`、`references/`、`scripts/` 与 `agents/` 的完整仓库目录。
- **操作：** 在该目录运行：

```powershell
.\scripts\install.ps1
```

- **默认目标：** `$HOME\.codex\skills\civil-thesis-body-writing`。
- **已有安装：** 脚本先把已有目录重命名为同级的 `civil-thesis-body-writing.bak-YYYYMMDD-HHMMSS`。
- **重启：** 安装完成后重启 Codex。
- **验证：** 运行[共享验证提示词](#安装验证)。

### Linux/macOS

- **前提条件：** 已安装 Codex 和 Bash，并已取得完整仓库目录。
- **操作：** 在该目录运行：

```bash
bash scripts/install.sh
```

- **默认目标：** `${CODEX_HOME:-$HOME/.codex}/skills/civil-thesis-body-writing`。
- **已有安装：** 脚本先把已有目录重命名为同级的 `civil-thesis-body-writing.bak-YYYYMMDD-HHMMSS`。
- **重启：** 安装完成后重启 Codex。
- **验证：** 运行[共享验证提示词](#安装验证)。

该脚本已纳入仓库内容校验；当前仓库不声明已在维护者机器完成 Linux/macOS 执行冒烟测试。

### 手动安装

- **前提条件：** 已安装 Codex，已取得完整 `civil-thesis-body-writing` 文件夹，并可写入 Codex skills 目录。
- **操作：** 先按下述备份规则处理已有目录，再把完整文件夹复制到默认目标，确认目标文件夹内直接包含 `SKILL.md`；也可在 Codex 自定义 skills 根目录执行同等复制操作。
- **默认目标：** Windows 为 `$HOME\.codex\skills\civil-thesis-body-writing`；Linux/macOS 为 `${CODEX_HOME:-$HOME/.codex}/skills/civil-thesis-body-writing`。
- **已有安装：** 手动安装不会自动备份；复制前把已有目录重命名为 `civil-thesis-body-writing.bak-YYYYMMDD-HHMMSS`。
- **重启：** 复制完成后重启 Codex。
- **验证：** 运行[共享验证提示词](#安装验证)。

### 安装验证

所有安装路线使用同一验证提示词：

```text
使用 civil-thesis-body-writing 检查这段土木工程论文正文是否存在空泛结论，并说明缺少哪些证据。
```

## 使用边界

- 已移除“大论文改 SCI”功能，不将学位论文或章节抽取、压缩、重组成期刊稿件。独立期刊稿件写作/润色、中英翻译和 Word 格式转换仍保留；这些任务不自动改变文稿类型。

- 本文试验、有限元、机器学习和 GUI 结论优先由本文图表、公式、模型输出及参数范围支持。
- 外部文献用于背景、方法来源、机理解释和横向比较，不替代本文结果。
- Zotero 元数据、摘要和下载状态不能单独作为句子级引用证据。
- 设计值、承载力和规范性结论必须保留适用工况、参数范围和标准依据。
- 公式的来源、变量、量纲、数学关系和力学假设分别检查；量纲一致或数值代入正确，不代表模型有效或可直接用于工程设计。
- 定量图表必须追溯实际数据与处理过程；生成式概念图不能伪装成试验照片、有限元云图、实测曲线或统计证据。
- 数值工具只核查声明的 CSV 运算和分组关系，不自动理解论文、补齐缺失值或证明数据完全无泄漏。
- DOCX 任务先区分新建、转换和修订；学校/期刊模板高于通用格式，已有文件默认不覆盖，公式、域、批注、修订和编号需按对象校核。
- 最小清理不授权结构重写；常规润色不擅自补充事实。修改既核对字面值，也核对数值对应的模型、指标、工况以及引用支持的主张。
- 反防御性写作不等于删除负面结果。保留影响解释的重要不利发现、建模假设、适用条件和真实不确定性，不默认添加泛化的局限性段落。
- 表达清理以清楚、准确和专业语域为目标，不承诺 AI 检测分数，也不删除学校或期刊要求的 AI 辅助使用声明。

## 示例与模板

- [公开使用配方](references/examples/public-usage-recipes.md)
- [分场景任务模板](references/examples/use-case-templates.md)
- [完整参考索引](references/index.md)

## 验证

<details>
<summary>运行完整验证</summary>

本地验证使用仓库专用的 `.venv-validation`，不把 PyYAML 安装到 skill 运行环境或共享 Python 环境。

Windows PowerShell：

```powershell
python -m venv .venv-validation
.\.venv-validation\Scripts\python.exe -m pip install -r requirements-validation.txt
.\.venv-validation\Scripts\python.exe -X utf8 scripts\validate_all.py .
```

Linux/macOS Bash：

```bash
python3 -m venv .venv-validation
./.venv-validation/bin/python -m pip install -r requirements-validation.txt
./.venv-validation/bin/python -X utf8 scripts/validate_all.py .
```

安装依赖和运行验证都直接调用该虚拟环境的 Python，无需激活环境。PyYAML 仅用于仓库验证，skill 运行时不依赖它。完整入口检查 router、manifest、输出契约、压力测试、前向测试、写作风格、引用工作流、公开分发和隐私规则。GitHub Actions 在推送到 main、pull request 和手动触发时运行同一入口。
</details>

## 项目结构

<details>
<summary>查看目录职责</summary>

```text
civil-thesis-body-writing/
  SKILL.md                 # 轻量 router
  manifest.yaml            # 模式、章节、来源和操作映射
  static/                  # 核心规则与任务碎片
  references/              # 按需加载的工作流、风格与案例
  scripts/                 # 安装脚本和确定性验证器
  agents/openai.yaml       # Codex UI 元数据
  .github/                 # CI 与问题反馈表单
```
</details>

## 仓库分发与隐私

仓库提交与对外分发内容不应包含本地私人路径、Zotero storage key、真实论文清单、访问凭据、未公开数据或用户稿件。维护者在推送或合并前运行完整验证；使用者通过克隆仓库或 `Code -> Download ZIP` 获取当前内容。

## 问题反馈

- [提交可复现问题](https://github.com/JackYStack/civil-engineering-thesis-body-writing-skill/issues/new?template=bug-report.yml)
- [提出可复用工作流需求](https://github.com/JackYStack/civil-engineering-thesis-body-writing-skill/issues/new?template=workflow-request.yml)

提交前删除稿件原文、私人路径、凭据和未公开研究数据。

本仓库为公开仓库。Issue Form 的 `required` 设置仅作为结构化确认；Issue 内容可能被任何人查看，表单本身不能阻止敏感信息披露。请勿提交稿件、私人路径、凭据、Zotero storage key 或未公开数据。

## 致谢与参考来源

本 Skill 的架构和部分通用工作流受以下公开项目启发。感谢这些项目的作者与维护者：

- [Gostyan/docx-skill-4-cn-paper](https://github.com/Gostyan/docx-skill-4-cn-paper)：DOCX 新建、转换、修订分支及格式验证思路。
- [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)：router/manifest 架构、学术写作方法和 `nature-figure` 协作边界。
- [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine)：论证主线、证据库、写作理由矩阵和逻辑迁移审查。
- [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills)：外部工具调用、来源状态和证据边界规则。
- [Rimagination/instsci](https://github.com/Rimagination/instsci)：论文获取、访问状态记录和 Zotero 交接流程。
- [quzhiii/thesis-skills](https://github.com/quzhiii/thesis-skills)：论文格式、终稿 readiness 和确定性审查方法。
- [zsyggg/paper-craft-skills](https://github.com/zsyggg/paper-craft-skills)：论文阅读与展示工作流参考。
- [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)：以证据组织主张、明确实验职责和精简防御性表述的写作规则。
- [matsuikentaro1/humanizer_academic](https://github.com/matsuikentaro1/humanizer_academic)：清楚优先于压缩，明确比较对象、条件与指代，保留有内容的学术表达。
- [AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer)：主张强度与证据匹配、作者风格校准及学术语气保护。
- [junbolian/Academic-Humanizer](https://github.com/junbolian/Academic-Humanizer)：分级编辑强度、可定位的修改理由，以及数据、引用与限定语的对照核查。
- [taehyeonglim/academic-humanizer](https://github.com/taehyeonglim/academic-humanizer)：学术语域保护，保留真实不确定性、方法被动语态、专业词汇和范围符号。

各项目的审阅版本、许可证、迁移状态、保留内容、未迁移内容及本 Skill 内部落点，见[外部 Skill 来源与迁移索引](references/meta/external-skill-sources.md)。本项目仅以重新表述的规则或显式协作接口吸收通用方法，不默认复制上游脚本、数据、示例或品牌规范；具体许可证仍以各上游仓库为准。
