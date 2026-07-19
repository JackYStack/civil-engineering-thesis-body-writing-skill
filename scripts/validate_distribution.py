#!/usr/bin/env python3
"""Validate public distribution readiness for civil-thesis-body-writing."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError:
    print(
        "Validation dependency missing. Install it in .venv-validation:\n"
        "PowerShell: python -m venv .venv-validation; "
        ".\\.venv-validation\\Scripts\\python.exe -m pip install -r requirements-validation.txt\n"
        "Bash: python3 -m venv .venv-validation && "
        "./.venv-validation/bin/python -m pip install -r requirements-validation.txt"
    )
    raise SystemExit(2)


VALIDATION_REQUIREMENT = "PyYAML>=6.0.3,<7.0"

REQUIRED_FILES = [
    ".github/workflows/validate.yml",
    ".gitignore",
    "README.md",
    "README.en.md",
    "agents/openai.yaml",
    "requirements-validation.txt",
    "scripts/install.ps1",
    "scripts/install.sh",
    "scripts/test_validate_distribution.py",
    "references/examples/public-usage-recipes.md",
    "references/meta/regression-test-checklist.md",
    "references/meta/real-task-regression-results.md",
    "assets/readme-banner-cn.svg",
    "assets/readme-banner-en.svg",
    ".github/ISSUE_TEMPLATE/bug-report.yml",
    ".github/ISSUE_TEMPLATE/workflow-request.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
]

README_REQUIRED_SNIPPETS = [
    "## 安装",
    "## 快速使用",
    "## 常用任务模板",
    "## 验证",
    "## 仓库分发与隐私",
]

README_INTERFACE_SNIPPETS = {
    "README.md": [
        "assets/readme-banner-cn.svg",
        "## 工作方式",
        "## 主要能力",
        "## 使用边界",
        "## 示例与模板",
        "## 项目结构",
        "## 问题反馈",
        "使用 civil-thesis-body-writing",
        "/actions/workflows/validate.yml",
        "README.en.md",
        "仅作为结构化确认",
        "## 致谢与参考来源",
        "references/meta/external-skill-sources.md",
    ],
    "README.en.md": [
        "assets/readme-banner-en.svg",
        "## How It Works",
        "## Capabilities",
        "## Evidence and Safety Boundaries",
        "## Examples and Recipes",
        "## Repository Structure",
        "## Support",
        "Use civil-thesis-body-writing",
        "/actions/workflows/validate.yml",
        "README.md",
        "structured confirmation only",
        "## Acknowledgements And Upstream Skills",
        "references/meta/external-skill-sources.md",
    ],
}

ACKNOWLEDGED_SKILL_SOURCES = [
    "https://github.com/Gostyan/docx-skill-4-cn-paper",
    "https://github.com/Yuan1z0825/nature-skills",
    "https://github.com/WUBING2023/PaperSpine",
    "https://github.com/google-deepmind/science-skills",
    "https://github.com/Rimagination/instsci",
    "https://github.com/quzhiii/thesis-skills",
    "https://github.com/zsyggg/paper-craft-skills",
]

FORBIDDEN_INTERFACE_SNIPPETS = [
    "license-",
    "License</a>",
]

FORBIDDEN_RELEASE_GUIDANCE = [
    "/releases/",
    "/releases/latest",
    "Release v0.",
    "### 从 Release 安装",
    "### Install from a Release",
    "## Release Gate",
    "release archive",
    "release page",
    "prepared the next release tag",
    "当前稳定发布",
    "v0.4.0",
    "v0.3.0",
]

RELEASE_GUIDANCE_FILES = [
    "README.md",
    "README.en.md",
    "references/index.md",
    "references/meta/regression-test-checklist.md",
    "references/meta/update-log.md",
]

INSTALLATION_ROUTES = {
    "README.md": {
        "headings": [
            "### 从仓库安装（推荐）",
            "### Windows",
            "### Linux/macOS",
            "### 手动安装",
        ],
        "labels": ["前提条件：", "操作：", "默认目标：", "已有安装：", "重启：", "验证："],
        "quick_start_commands": [r".\scripts\install.ps1", "bash scripts/install.sh"],
    },
    "README.en.md": {
        "headings": [
            "### Install from the repository (recommended)",
            "### Windows",
            "### Linux/macOS",
            "### Manual installation",
        ],
        "labels": ["Prerequisite:", "Action:", "Default destination:", "Existing installation:", "Restart:", "Verify:"],
        "quick_start_commands": [r".\scripts\install.ps1", "bash scripts/install.sh"],
    },
}

README_VALIDATION_VENV_SNIPPETS = [
    "python -m venv .venv-validation",
    r".\.venv-validation\Scripts\python.exe -m pip install -r requirements-validation.txt",
    r".\.venv-validation\Scripts\python.exe -X utf8 scripts\validate_all.py .",
    "python3 -m venv .venv-validation",
    "./.venv-validation/bin/python -m pip install -r requirements-validation.txt",
    "./.venv-validation/bin/python -X utf8 scripts/validate_all.py .",
]
UNISOLATED_VALIDATION_PIP = re.compile(
    r"(?m)^python(?:3)? -m pip install -r requirements-validation\.txt\s*$"
)

FORBIDDEN_SEPARATOR = "\u74ba\u75d0"
WRONG_SEPARATOR_GLYPH = "\u8def"
MIDDLE_DOT = "\u00b7"
EXPECTED_NAVIGATION_SEPARATORS = 6
EXPECTED_BANNER_FOOTER = f"OBJECT {MIDDLE_DOT} EVIDENCE {MIDDLE_DOT} MECHANISM {MIDDLE_DOT} BOUNDARY"
ENGLISH_BANNER_TITLE = "Civil Engineering Academic Writing Skill"
MAX_ENGLISH_TITLE_SIZE = 52.0

PRIVACY_CONFIRMATION_LABEL = (
    "I understand this is a structured confirmation only, and I removed manuscript text, "
    "private paths, credentials, Zotero storage keys, access tokens, and unpublished research data."
)

ISSUE_SUPPORT_NOTES = [
    "This is a public repository. Issue Form required settings provide a structured confirmation only; "
    "issue content may be visible to anyone, and the form cannot prevent disclosure of sensitive information.",
    "本仓库为公开仓库。Issue Form 的 required 设置仅用于结构化确认；Issue 内容可能被任何人查看，"
    "表单本身不能阻止敏感信息披露。",
]

STALE_PRIVATE_GUIDANCE = [
    "In this private repository",
    "当前仓库为私有仓库",
]

VISIBILITY_GUIDANCE_FILES = [
    "README.md",
    "README.en.md",
    ".github/ISSUE_TEMPLATE/bug-report.yml",
    ".github/ISSUE_TEMPLATE/workflow-request.yml",
]

ISSUE_FORM_REQUIREMENTS = {
    ".github/ISSUE_TEMPLATE/bug-report.yml": {
        "name": "Bug report",
        "fields": {
            "task_mode": ("dropdown", True),
            "environment": ("input", True),
            "reproduction": ("textarea", True),
            "expected": ("textarea", True),
            "observed": ("textarea", True),
            "validation": ("textarea", False),
            "privacy": ("checkboxes", None),
        },
    },
    ".github/ISSUE_TEMPLATE/workflow-request.yml": {
        "name": "Workflow request",
        "fields": {
            "scenario": ("textarea", True),
            "deliverable": ("textarea", True),
            "evidence": ("textarea", True),
            "constraints": ("textarea", True),
            "reusable_value": ("textarea", True),
            "privacy": ("checkboxes", None),
        },
    },
}

ALLOWED_ISSUE_ITEM_TYPES = {"markdown", "input", "textarea", "dropdown", "checkboxes"}
ISSUE_FORM_ID = re.compile(r"^[A-Za-z0-9_-]+$")
ISSUE_CONFIG_USAGE_URL = (
    "https://github.com/JackYStack/civil-engineering-thesis-body-writing-skill/blob/main/"
    "references/examples/public-usage-recipes.md"
)

EXAMPLE_MIN_CASES = 6
REGRESSION_MIN_CASES = 7

LEGACY_PRIVATE_PATTERNS = [
    re.compile(r"[A-Za-z]:[\\/](?:我的文件|Downloads[\\/]Documents[\\/]我的文库)(?:[\\/]|$)"),
    re.compile(r"Zotero[\\/]storage[\\/][A-Z0-9]{8}", re.IGNORECASE),
    re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE),
]

WINDOWS_USER_PATH = re.compile(
    r"\b[A-Za-z]:[\\/]+Users[\\/]+(?P<user>[^\\/\s]+)(?:[\\/][^\s'\"`<>|]*)?",
    re.IGNORECASE,
)
POSIX_USER_PATH = re.compile(r"(?<![A-Za-z0-9_])/(?:home|Users)/(?P<user>[^/\s]+)(?:/[^\s'\"`]*)?")
KEY_HEADER_PATTERN = re.compile(
    r"-----BEGIN[ \t]+(?:(?:RSA|DSA|EC|OPENSSH|ENCRYPTED)[ \t]+)?PRIVATE[ \t]+KEY-----"
)
BEARER_CREDENTIAL_PATTERN = re.compile(r"\bBearer[ \t]+[A-Za-z0-9._~+/=-]{12,}", re.IGNORECASE)
CREDENTIAL_PREFIX_PATTERNS = [
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
]
SECRET_NAME = (
    r"(?:[A-Za-z0-9]+[_-])*(?:api[_-]?key|access[_-]?key|auth[_-]?token|password|passwd|secret|"
    r"token|private[_-]?key|cookie)(?:[_-][A-Za-z0-9]+)*"
)
CREDENTIAL_ASSIGNMENT = re.compile(
    rf"""(?imx)
    (?:^|[\s,{{;])
    ["']?(?:\$env:)?{SECRET_NAME}["']?\s*[:=]\s*
    (?:
        "(?P<double>[^"\r\n]+)"
        |'(?P<single>[^'\r\n]+)'
        |(?P<bare>[^\s,;#]+)
    )
    """
)

EXPLICIT_PLACEHOLDER = re.compile(
    r"(?i)(?:"
    r"(?:YOUR|EXAMPLE|REPLACE|REPLACE_ME)[_-][A-Z0-9_-]+"
    r"|\[(?:password|passwd|secret|token|api[_-]?key|access[_-]?key|private[_-]?key)\]"
    r"|<(?:password|passwd|secret|token|api[_-]?key|access[_-]?key|private[_-]?key)>"
    r"|\{(?:password|passwd|secret|token|api[_-]?key|access[_-]?key|private[_-]?key)\}"
    r")"
)
ENVIRONMENT_REFERENCE = re.compile(
    r"(?i)(?:\$(?:HOME|CODEX_HOME)|\$\{(?:HOME|CODEX_HOME)\}|%(?:HOME|USERPROFILE|CODEX_HOME)%|"
    r"\$env:(?:HOME|USERPROFILE|CODEX_HOME))"
)
PLACEHOLDER_USERS = {
    "user",
    "username",
    "<user>",
    "<username>",
    "<用户名>",
    "[user]",
    "[username]",
    "$user",
    "${user}",
    "%username%",
}

SCAN_SUFFIXES = {
    ".md",
    ".yaml",
    ".yml",
    ".py",
    ".txt",
    ".svg",
    ".ps1",
    ".sh",
    ".json",
    ".toml",
    ".ini",
    ".cfg",
    ".env",
    ".pem",
    ".key",
}
SCAN_FILENAMES = {".env", "id_rsa", "id_dsa", "id_ecdsa", "id_ed25519"}
SCAN_SKIP_DIRS = {
    ".git",
    ".superpowers",
    ".venv-validation",
    "__pycache__",
    "dist",
    "build",
    ".pytest_cache",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def iter_scanned_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel_parts = set(path.relative_to(root).parts)
        if rel_parts & SCAN_SKIP_DIRS:
            continue
        filename = path.name.lower()
        if (
            path.suffix.lower() in SCAN_SUFFIXES
            or filename in SCAN_FILENAMES
            or filename.startswith(".env.")
        ):
            yield path


def markdown_section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    match = re.search(r"(?m)^#{2,3} ", text[start + len(heading) :])
    if match is None:
        return text[start:]
    return text[start : start + len(heading) + match.start()]


def load_yaml_mapping(path: Path, rel: str, errors: list[str]) -> dict[str, Any] | None:
    try:
        data = yaml.safe_load(read(path))
    except yaml.YAMLError as exc:
        detail = getattr(exc, "problem", None) or exc.__class__.__name__
        errors.append(f"{rel} cannot parse YAML: {detail}")
        return None
    if not isinstance(data, dict):
        errors.append(f"{rel} top level must be a mapping")
        return None
    return data


def validate_issue_form(
    path: Path,
    rel: str,
    requirements: dict[str, Any],
    errors: list[str],
) -> None:
    data = load_yaml_mapping(path, rel, errors)
    if data is None:
        return

    for key in ("name", "description", "title", "body"):
        if key not in data:
            errors.append(f"{rel} missing top-level key: {key}")

    if data.get("name") != requirements["name"]:
        errors.append(f"{rel} name must be `{requirements['name']}`")
    for key in ("description", "title"):
        if key in data and not isinstance(data[key], str):
            errors.append(f"{rel} top-level `{key}` must be a string")

    body = data.get("body")
    if not isinstance(body, list):
        if "body" in data:
            errors.append(f"{rel} body must be a list")
        return

    items_by_id: dict[str, dict[str, Any]] = {}
    markdown_values: list[str] = []
    for index, item in enumerate(body):
        location = f"{rel} body item {index + 1}"
        if not isinstance(item, dict):
            errors.append(f"{location} must be a mapping")
            continue

        item_type = item.get("type")
        if item_type not in ALLOWED_ISSUE_ITEM_TYPES:
            errors.append(f"{location} has unsupported type: {item_type}")

        attributes = item.get("attributes")
        if not isinstance(attributes, dict):
            errors.append(f"{location} attributes must be a mapping")
            attributes = {}

        if item_type == "markdown":
            value = attributes.get("value")
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{location} markdown value must be a non-empty string")
            else:
                markdown_values.append(value)
            continue

        field_id = item.get("id")
        if not isinstance(field_id, str) or not field_id:
            errors.append(f"{location} must have a non-empty string id")
            continue
        if not ISSUE_FORM_ID.fullmatch(field_id):
            errors.append(f"{rel} issue-form id `{field_id}` must match `[A-Za-z0-9_-]+`")
        if field_id in items_by_id:
            errors.append(f"{rel} duplicate issue-form id: {field_id}")
        else:
            items_by_id[field_id] = item

        label = attributes.get("label")
        if not isinstance(label, str) or not label.strip():
            errors.append(f"{rel} field `{field_id}` attributes.label must be a non-empty string")

        if item_type in {"dropdown", "checkboxes"}:
            options = attributes.get("options")
            if not isinstance(options, list) or not options:
                errors.append(f"{rel} field `{field_id}` attributes.options must be a non-empty list")
            elif item_type == "dropdown":
                if not all(isinstance(option, str) and option.strip() for option in options):
                    errors.append(f"{rel} dropdown `{field_id}` options must be non-empty strings")
                elif len(options) != len(set(options)):
                    errors.append(f"{rel} dropdown `{field_id}` options must be unique")
            elif item_type == "checkboxes":
                checkbox_labels: list[str] = []
                for option_index, option in enumerate(options, start=1):
                    if not isinstance(option, dict):
                        errors.append(f"{rel} checkboxes `{field_id}` option {option_index} must be a mapping")
                        continue
                    if not isinstance(option.get("label"), str) or not option["label"].strip():
                        errors.append(
                            f"{rel} checkboxes `{field_id}` option {option_index} "
                            "label must be a non-empty string"
                        )
                    else:
                        checkbox_labels.append(option["label"])
                    if "required" in option and type(option["required"]) is not bool:
                        errors.append(
                            f"{rel} checkboxes `{field_id}` option {option_index} required must be boolean"
                        )
                if len(checkbox_labels) != len(set(checkbox_labels)):
                    errors.append(f"{rel} checkboxes `{field_id}` option labels must be unique")

        validations = item.get("validations", {})
        if not isinstance(validations, dict):
            errors.append(f"{rel} field `{field_id}` validations must be a mapping")
        elif "required" in validations and type(validations["required"]) is not bool:
            errors.append(f"{rel} field `{field_id}` validations.required must be boolean")

    notes = "\n".join(markdown_values)
    for note in ISSUE_SUPPORT_NOTES:
        if note not in notes:
            errors.append(f"{rel} missing private-repository support note: {note}")

    for field_id, (expected_type, expected_required) in requirements["fields"].items():
        item = items_by_id.get(field_id)
        if item is None:
            errors.append(f"{rel} missing issue-form field: id: {field_id}")
            continue
        if item.get("type") != expected_type:
            errors.append(f"{rel} field `{field_id}` must have type `{expected_type}`")
        if expected_required is not None:
            validations = item.get("validations")
            actual_required = validations.get("required") if isinstance(validations, dict) else None
            if type(actual_required) is not bool or actual_required is not expected_required:
                errors.append(
                    f"{rel} field `{field_id}` validations.required must be boolean "
                    f"{str(expected_required).lower()}"
                )

    expected_privacy = {
        "type": "checkboxes",
        "id": "privacy",
        "attributes": {
            "label": "Privacy confirmation",
            "options": [{"label": PRIVACY_CONFIRMATION_LABEL, "required": True}],
        },
    }
    if items_by_id.get("privacy") != expected_privacy:
        errors.append(f"{rel} privacy confirmation does not match the required structure")


def validate_issue_config(path: Path, rel: str, errors: list[str]) -> None:
    data = load_yaml_mapping(path, rel, errors)
    if data is None:
        return
    if data.get("blank_issues_enabled") is not False:
        errors.append(f"{rel} blank_issues_enabled must be boolean false")

    links = data.get("contact_links")
    if not isinstance(links, list):
        errors.append(f"{rel} contact_links must be a list")
        return

    usage_link_found = False
    for index, link in enumerate(links):
        if not isinstance(link, dict):
            errors.append(f"{rel} contact link {index + 1} must be a mapping")
            continue
        for key in ("name", "url", "about"):
            if not isinstance(link.get(key), str) or not link[key].strip():
                errors.append(f"{rel} contact link {index + 1} `{key}` must be a non-empty string")
        if link.get("url") == ISSUE_CONFIG_USAGE_URL:
            usage_link_found = True
    if not usage_link_found:
        errors.append(f"{rel} must contain the usage-recipes contact link")


def is_placeholder_user(value: str) -> bool:
    return value.strip().lower() in PLACEHOLDER_USERS


def is_placeholder_secret(value: str) -> bool:
    normalized = value.strip().strip("'\"")
    return bool(
        EXPLICIT_PLACEHOLDER.fullmatch(normalized)
        or ENVIRONMENT_REFERENCE.fullmatch(normalized)
    )


def privacy_matches(text: str):
    for pattern in LEGACY_PRIVATE_PATTERNS:
        yield from pattern.finditer(text)
    for pattern in (WINDOWS_USER_PATH, POSIX_USER_PATH):
        for match in pattern.finditer(text):
            if not is_placeholder_user(match.group("user")):
                yield match
    yield from KEY_HEADER_PATTERN.finditer(text)
    yield from BEARER_CREDENTIAL_PATTERN.finditer(text)
    for pattern in CREDENTIAL_PREFIX_PATTERNS:
        yield from pattern.finditer(text)
    for match in CREDENTIAL_ASSIGNMENT.finditer(text):
        value = match.group("double") or match.group("single") or match.group("bare")
        if len(value) < 8:
            continue
        if not is_placeholder_secret(value):
            yield match


def validate_navigation_and_banners(root: Path, errors: list[str]) -> None:
    for rel in ("README.md", "README.en.md"):
        path = root / rel
        if not path.exists():
            continue
        text = read(path)
        wrong_navigation_separator = rf"</a>\s+{re.escape(WRONG_SEPARATOR_GLYPH)}\s*"
        if FORBIDDEN_SEPARATOR in text or re.search(wrong_navigation_separator, text):
            errors.append(f"{rel} contains a forbidden separator")
        navigation_lines = [line for line in text.splitlines() if '<a href="#' in line]
        if sum(line.count(MIDDLE_DOT) for line in navigation_lines) != EXPECTED_NAVIGATION_SEPARATORS:
            errors.append(
                f"{rel} navigation must use exactly "
                f"{EXPECTED_NAVIGATION_SEPARATORS} middle-dot separators"
            )

    for rel in ("assets/readme-banner-cn.svg", "assets/readme-banner-en.svg"):
        path = root / rel
        if not path.exists():
            continue
        try:
            tree = ET.parse(path)
        except ET.ParseError as exc:
            errors.append(f"{rel} is not valid XML: {exc}")
            continue
        texts = [element for element in tree.getroot().iter() if element.tag.endswith("text")]
        if not any(element.text == EXPECTED_BANNER_FOOTER for element in texts):
            errors.append(f"{rel} footer must use middle-dot separators")
        if any(element.text and FORBIDDEN_SEPARATOR in element.text for element in texts):
            errors.append(f"{rel} contains a forbidden separator")

        if rel.endswith("-en.svg"):
            title = next((element for element in texts if element.text == ENGLISH_BANNER_TITLE), None)
            if title is None:
                errors.append(f"{rel} is missing the English banner title")
                continue
            try:
                font_size = float(title.attrib.get("font-size", ""))
            except ValueError:
                errors.append(f"{rel} English banner title font-size must be numeric")
                continue
            if font_size > MAX_ENGLISH_TITLE_SIZE:
                errors.append(f"{rel} English banner title font-size must be at most 52px")


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            errors.append(f"missing distribution file: {rel}")

    requirements = root / "requirements-validation.txt"
    if requirements.exists() and VALIDATION_REQUIREMENT not in read(requirements).splitlines():
        errors.append(f"requirements-validation.txt must contain `{VALIDATION_REQUIREMENT}`")

    workflow = root / ".github/workflows/validate.yml"
    if workflow.exists():
        workflow_text = read(workflow)
        if "scripts/validate_all.py" not in workflow_text:
            errors.append("GitHub Actions workflow does not run scripts/validate_all.py")
        if "python -X utf8" not in workflow_text:
            errors.append("GitHub Actions workflow does not force UTF-8 Python mode")
        if "python -m pip install -r requirements-validation.txt" not in workflow_text:
            errors.append("GitHub Actions workflow does not install validation dependencies")

    readme = root / "README.md"
    if readme.exists():
        readme_text = read(readme)
        for snippet in README_REQUIRED_SNIPPETS:
            if snippet not in readme_text:
                errors.append(f"README.md missing section: {snippet}")
        if "\ufffd" in readme_text:
            errors.append("README.md contains replacement characters")

    readme_en = root / "README.en.md"
    if readme_en.exists():
        readme_en_text = read(readme_en)
        for snippet in ["## Installation", "## Quick Start", "## Common Workflows", "## Validation", "## Repository Distribution And Privacy"]:
            if snippet not in readme_en_text:
                errors.append(f"README.en.md missing section: {snippet}")
        if "\ufffd" in readme_en_text:
            errors.append("README.en.md contains replacement characters")

    for readme_name, snippets in README_INTERFACE_SNIPPETS.items():
        readme_path = root / readme_name
        if not readme_path.exists():
            continue
        readme_text = read(readme_path)
        for snippet in snippets:
            if snippet not in readme_text:
                errors.append(f"{readme_name} missing interface element: {snippet}")
        for snippet in FORBIDDEN_INTERFACE_SNIPPETS:
            if snippet in readme_text:
                errors.append(f"{readme_name} shows unsupported interface element: {snippet}")
        for source_url in ACKNOWLEDGED_SKILL_SOURCES:
            if source_url not in readme_text:
                errors.append(f"{readme_name} missing acknowledged upstream skill: {source_url}")

        route_contract = INSTALLATION_ROUTES[readme_name]
        quick_start = markdown_section(
            readme_text,
            "## 快速使用" if readme_name == "README.md" else "## Quick Start",
        )
        for command in route_contract["quick_start_commands"]:
            if command not in quick_start:
                errors.append(f"{readme_name} quick start missing platform command: {command}")
        for heading in route_contract["headings"]:
            section = markdown_section(readme_text, heading)
            for label in route_contract["labels"]:
                if label not in section:
                    errors.append(f"{readme_name} installation route `{heading}` missing: {label}")

        validation_section = markdown_section(
            readme_text,
            "## 验证" if readme_name == "README.md" else "## Validation",
        )
        for command in README_VALIDATION_VENV_SNIPPETS:
            if command not in validation_section:
                errors.append(f"{readme_name} validation instructions missing isolated command: {command}")
        if UNISOLATED_VALIDATION_PIP.search(validation_section):
            errors.append(f"{readme_name} must not recommend unisolated validation pip")

    for rel in RELEASE_GUIDANCE_FILES:
        path = root / rel
        if not path.exists():
            continue
        text = read(path)
        for snippet in FORBIDDEN_RELEASE_GUIDANCE:
            if snippet in text:
                errors.append(f"{rel} contains removed Release guidance: {snippet}")

    for rel in VISIBILITY_GUIDANCE_FILES:
        path = root / rel
        if not path.exists():
            continue
        text = read(path)
        for snippet in STALE_PRIVATE_GUIDANCE:
            if snippet in text:
                errors.append(f"{rel} contains stale private-repository guidance: {snippet}")

    gitignore = root / ".gitignore"
    if gitignore.exists() and ".venv-validation/" not in read(gitignore).splitlines():
        errors.append(".gitignore must ignore .venv-validation/")

    validate_navigation_and_banners(root, errors)

    openai_yaml = root / "agents/openai.yaml"
    if openai_yaml.exists():
        openai_text = read(openai_yaml)
        for snippet in ["display_name:", "short_description:", "default_prompt:", "$civil-thesis-body-writing"]:
            if snippet not in openai_text:
                errors.append(f"agents/openai.yaml missing: {snippet}")
        if "\ufffd" in openai_text:
            errors.append("agents/openai.yaml contains replacement characters")

    for installer in ["scripts/install.ps1", "scripts/install.sh"]:
        installer_path = root / installer
        if installer_path.exists():
            installer_text = read(installer_path)
            for snippet in ["civil-thesis-body-writing", "Restart Codex"]:
                if snippet not in installer_text:
                    errors.append(f"{installer} missing installation message: {snippet}")

    examples = root / "references/examples/public-usage-recipes.md"
    if examples.exists():
        examples_text = read(examples)
        case_count = len(re.findall(r"^## Case:", examples_text, flags=re.MULTILINE))
        if case_count < EXAMPLE_MIN_CASES:
            errors.append(f"public usage recipes too thin: {case_count} cases")
        for required in ["DOCX", "InstSci", "Citation", "SCI"]:
            if required.lower() not in examples_text.lower():
                errors.append(f"public usage recipes missing topic: {required}")

    checklist = root / "references/meta/regression-test-checklist.md"
    if checklist.exists():
        checklist_text = read(checklist)
        for snippet in ["Phase 8D Regression Cases", "Repository Distribution Gate", "Privacy And Distribution Gate"]:
            if snippet not in checklist_text:
                errors.append(f"regression checklist missing: {snippet}")

    regression_results = root / "references/meta/real-task-regression-results.md"
    if regression_results.exists():
        regression_text = read(regression_results)
        pass_count = len(re.findall(r"\bPASS\b", regression_text))
        if pass_count < REGRESSION_MIN_CASES:
            errors.append(f"real-task regression results too thin: {pass_count} PASS rows")
        for snippet in ["Anti-vague", "PCSP", "Citation", "DOCX", "InstSci", "SCI", "Target-journal"]:
            if snippet.lower() not in regression_text.lower():
                errors.append(f"real-task regression results missing topic: {snippet}")

    references_index = root / "references/index.md"
    if references_index.exists():
        index_text = read(references_index)
        for expected in ["examples/public-usage-recipes.md", "meta/regression-test-checklist.md", "meta/real-task-regression-results.md"]:
            if expected not in index_text:
                errors.append(f"references/index.md does not mention {expected}")
    else:
        errors.append("missing references/index.md")

    manifest = root / "manifest.yaml"
    if manifest.exists():
        manifest_text = read(manifest)
        for validator in ["scripts/validate_distribution.py", "scripts/test_validate_distribution.py"]:
            if validator not in manifest_text:
                errors.append(f"manifest.yaml does not list {validator}")
    else:
        errors.append("missing manifest.yaml")

    validate_all = root / "scripts/validate_all.py"
    if validate_all.exists():
        validate_all_text = read(validate_all)
        for validator in ["validate_distribution.py", "test_validate_distribution.py"]:
            if validator not in validate_all_text:
                errors.append(f"validate_all.py does not run {validator}")
    else:
        errors.append("missing scripts/validate_all.py")

    for rel, requirements_contract in ISSUE_FORM_REQUIREMENTS.items():
        issue_path = root / rel
        if issue_path.exists():
            validate_issue_form(issue_path, rel, requirements_contract, errors)

    config_rel = ".github/ISSUE_TEMPLATE/config.yml"
    config_path = root / config_rel
    if config_path.exists():
        validate_issue_config(config_path, config_rel, errors)

    for path in iter_scanned_files(root):
        text = read(path)
        if "\ufffd" in text:
            errors.append(f"replacement character found in {path.relative_to(root)}")
        for match in privacy_matches(text):
            errors.append(
                f"possible private/disallowed token in {path.relative_to(root)}: "
                f"{match.group(0)[:80]}"
            )

    if errors:
        print("Distribution validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Distribution validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
