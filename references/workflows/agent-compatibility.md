# Agent 适配与能力降级

本指南适用于 Claude Code、WorkBuddy，以及安装/打包维护。保留同一份写作规则，不复刻为三份独立正文指南。相对路径均以当前加载的 `SKILL.md` 所在目录为根，不以论文工作目录或 Codex 安装位置为根。

## 安装与调用

需要 Python 3.10+。在完整仓库根目录执行以下命令；此 Python 安装器不会修改 MCP、权限、全局提示词或 agent 配置文件。原 Codex PowerShell/Bash 安装命令保持可用。

### Claude Code

个人安装到 `~/.claude/skills/civil-thesis-body-writing/`：

```shell
python -X utf8 scripts/install_agent.py install --agent claude-code --scope user
```

项目安装必须指定实际项目目录：

```shell
python -X utf8 scripts/install_agent.py install --agent claude-code --scope project --project-root "/path/to/project"
```

调用 `/civil-thesis-body-writing`，或在自然语言请求中点名。若当前会话尚未识别新技能，重新打开该项目会话。不要将 Codex 的 `$skill-name` 当作所有平台通用命令。

### WorkBuddy

项目级本地安装仅针对支持 `.codebuddy/` 项目配置的客户端/代码开发场景：

```shell
python -X utf8 scripts/install_agent.py install --agent workbuddy --scope project --project-root "/path/to/project"
```

安装到项目的 `.codebuddy/skills/civil-thesis-body-writing/`。在对应工作目录启动任务，并请求“使用 civil-thesis-body-writing 修改这段正文”。客户端版本和项目类型可能影响本地配置加载；未识别时不应声称已启用。

个人技能推荐走官方界面导入，不推测用户级目录：

```shell
python -X utf8 scripts/install_agent.py package --agent workbuddy --output "/path/to/output/civil-thesis-body-writing-workbuddy.zip"
```

在 WorkBuddy 的技能页选择添加/上传本地技能包，按客户端安全审查完成确认，再启用技能。ZIP只有一个技能顶层目录，保留 `manifest.yaml`、`static/` 和按需参考文件；WorkBuddy 导出副本补充平台展示字段，原始 `SKILL.md` 不变。`version: 0.1.0` 表示导出适配格式版本，不是论文或模型版本；`author` 标记来源仓库的维护者，不声明上游规则为原创。

本地项目安装不是云端技能部署；桌面个人库、云端个人库和团队项目库不得视为自动同步。若导入时丢失 `static/` 或参考文件，停止正式写作并报告缺失路径，不退回无依据的通用回答。

### 安装保护与导出范围

已有同名目录默认拒绝覆盖；确认更新后加 `--replace`，旧目录会先备份到同级唯一的 `.bak-...` 目录。不删除备份、不自动重装其他技能。安装目录不能是源目录、源的上级或下级；检测到链接或冲突即拒绝。

导出只选取技能入口、manifest、说明、验证依赖声明及 `static/`、`references/`、`scripts/`、`assets/` 中的受支持文件。排除 `.git`、`.github`、Codex 专属 `agents/openai.yaml`、缓存、旧安装器、运行产物及其他文件。部署包不等于完整开发仓库；维护时的分发验证应在原仓库执行，不能以部署包缺少仓库元数据判断写作规则失效。

## 运行前能力门

只检查当前任务所需能力，不要求纯文本润色配置全部外部服务。能力必须来自当前宿主实际提供的工具、权限或已读取文件，不从平台名称推断。不要运行猜测的 MCP 方法名，不复制其他客户端的凭据或会话。

| 能力 | 可迁移部分 | 缺失时的处理 |
|---|---|---|
| 正文起草、清理、审稿微修、术语/证据规则 | 共享 Markdown 核心 | 必需参考文件不可读则停止该正式流程；短段落可仅在已读规则和用户材料内处理，并说明范围 |
| 文件读取、目录搜索、shell | 映射到当前宿主的等价工具 | 只读权限不写文件；无 shell 就人工对照，不声称运行脚本或验证器 |
| Zotero / InstSci / 网络检索 | 证据流程和确认规则 | MCP/连接器未配置或未授权则跳过外部调用，使用已提供文件；不能访问的引用标为未核实，不自动安装服务 |
| DOCX / PDF / OCR / 公式 / 渲染 | 模板、对象保护和核对要求 | 依赖或字体缺失时，仅交付明确标注的文字修改稿；不生成伪兼容文件，不把未渲染页面判为通过 |
| `nature-figure` / `nature-response` | brief、正文交接和局部修改 | 先确认宿主可加载这些独立技能；缺失时交付 brief 或修改段落，跳过实际绘图/回复包组装，不用普通写作输出冒充产物 |
| 子 agent、浏览器/桌面控制、Codex 专属工具 | 抽象任务目的 | 无等价工具则顺序人工核对或跳过，并报告少了哪项独立检查；不调用 Codex 内部命名接口 |
| Codex UI 元数据、自动调用策略 | 核心任务不依赖它们 | 在非 Codex 导出包中省略，不承诺宿主执行 `agents/openai.yaml` 的策略 |

所有宿主均保留：不编数据/引用、技术披露优先、真实不确定性、库写入前确认和原文件保护。降级仅改变可执行动作，不降低证据要求。必要能力缺失时输出“已完成部分 / 跳过项目及原因 / 需提供材料”，不让维护性检查清单淹没实际正文。

## 适配状态与非目标

安装与包结构可在隔离目录验证，但这不证明客户端已成功发现或调用技能。正式声称宿主可用前，应在相应客户端确认技能可见、能读取本指南与任一按需参考文件，并完成一个不含私有数据的局部请求。当前不自动部署用户的 Claude Code 或 WorkBuddy 个人配置，不申请额外权限，不启动付费模型调用，也不发布到技能市场。

官方依据（核对日期：2026-11-19）：

- [Claude Code Skills](https://code.claude.com/docs/en/skills)：个人与项目技能目录、支持文件和斜杠调用。
- [WorkBuddy Skills](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills)：本地技能包上传、启用及安全确认。
- [WorkBuddy 项目配置](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Project)：代码开发场景的 `.codebuddy/skills/`；客户端与云端库的区别。
- [WorkBuddy 开放平台技能格式](https://open.workbuddy.cn/en/docs/skill)：技能目录及展示字段。生成这些字段不等于已取得市场发布资格。
