#!/usr/bin/env python3
"""Mutation tests for the public distribution validator."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = Path("scripts/validate_distribution.py")
UNISOLATED_VALIDATION_COMMANDS = (
    "python -m pip install -r requirements-validation.txt\n"
    "python -X utf8 scripts/validate_all.py ."
)
ISOLATED_VALIDATION_COMMANDS = (
    "python -m venv .venv-validation\n"
    ".\\.venv-validation\\Scripts\\python.exe -m pip install -r requirements-validation.txt\n"
    ".\\.venv-validation\\Scripts\\python.exe -X utf8 scripts\\validate_all.py .\n"
    "python3 -m venv .venv-validation\n"
    "./.venv-validation/bin/python -m pip install -r requirements-validation.txt\n"
    "./.venv-validation/bin/python -X utf8 scripts/validate_all.py ."
)


class DistributionMutationTests(unittest.TestCase):
    maxDiff = None

    def fixture(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        fixture_root = Path(temporary.name) / "repository"
        shutil.copytree(
            ROOT,
            fixture_root,
            ignore=shutil.ignore_patterns(
                ".git",
                ".superpowers",
                ".venv-validation",
                "__pycache__",
                ".pytest_cache",
                "*.pyc",
            ),
        )
        return temporary, fixture_root

    def run_validator(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-X", "utf8", str(root / VALIDATOR), str(root)],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )

    def assert_mutation_rejected(
        self,
        mutate: Callable[[Path], None],
        expected_error: str,
    ) -> None:
        temporary, root = self.fixture()
        self.addCleanup(temporary.cleanup)
        mutate(root)

        completed = self.run_validator(root)
        output = completed.stdout + completed.stderr
        self.assertNotEqual(completed.returncode, 0, output)
        self.assertIn(expected_error, output)

    def ensure_validation_venv_contract(self, root: Path) -> None:
        for readme_name in ("README.md", "README.en.md"):
            path = root / readme_name
            text = path.read_text(encoding="utf-8")
            if UNISOLATED_VALIDATION_COMMANDS in text:
                text = text.replace(UNISOLATED_VALIDATION_COMMANDS, ISOLATED_VALIDATION_COMMANDS, 1)
            path.write_text(text, encoding="utf-8")

        gitignore = root / ".gitignore"
        text = gitignore.read_text(encoding="utf-8")
        if ".venv-validation/" not in text.splitlines():
            text += ".venv-validation/\n"
        gitignore.write_text(text, encoding="utf-8")

    def test_unmodified_distribution_passes(self) -> None:
        temporary, root = self.fixture()
        self.addCleanup(temporary.cleanup)

        completed = self.run_validator(root)

        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_missing_dependency_instructions_use_validation_venv(self) -> None:
        temporary, root = self.fixture()
        self.addCleanup(temporary.cleanup)

        completed = subprocess.run(
            [sys.executable, "-S", "-X", "utf8", str(root / VALIDATOR), str(root)],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        output = completed.stdout + completed.stderr

        self.assertNotEqual(completed.returncode, 0, output)
        self.assertIn(
            ".\\.venv-validation\\Scripts\\python.exe -m pip install -r requirements-validation.txt",
            output,
        )
        self.assertIn(
            "./.venv-validation/bin/python -m pip install -r requirements-validation.txt",
            output,
        )

    def test_malformed_issue_form_yaml_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / ".github/ISSUE_TEMPLATE/bug-report.yml"
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("name: Bug report", "name: [", 1), encoding="utf-8")

        self.assert_mutation_rejected(mutate, "cannot parse YAML")

    def test_missing_issue_form_top_level_key_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / ".github/ISSUE_TEMPLATE/bug-report.yml"
            text = path.read_text(encoding="utf-8")
            text = re.sub(r"(?m)^description:.*\n", "", text, count=1)
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "missing top-level key: description")

    def test_duplicate_issue_form_id_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / ".github/ISSUE_TEMPLATE/bug-report.yml"
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("id: observed", "id: expected", 1), encoding="utf-8")

        self.assert_mutation_rejected(mutate, "duplicate issue-form id: expected")

    def test_wrong_issue_form_field_type_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / ".github/ISSUE_TEMPLATE/bug-report.yml"
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("  - type: input", "  - type: textarea", 1), encoding="utf-8")

        self.assert_mutation_rejected(mutate, "field `environment` must have type `input`")

    def test_invalid_issue_form_id_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / ".github/ISSUE_TEMPLATE/bug-report.yml"
            text = path.read_text(encoding="utf-8")
            extra_field = (
                "  - type: input\n"
                "    id: invalid.id\n"
                "    attributes:\n"
                "      label: Extra context\n"
            )
            text = text.replace("  - type: checkboxes\n    id: privacy", extra_field + "  - type: checkboxes\n    id: privacy", 1)
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "issue-form id `invalid.id` must match")

    def test_duplicate_dropdown_options_are_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / ".github/ISSUE_TEMPLATE/bug-report.yml"
            text = path.read_text(encoding="utf-8")
            text = text.replace("        - Paper or SCI writing", "        - Thesis body writing", 1)
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "dropdown `task_mode` options must be unique")

    def test_checkbox_option_label_must_be_a_non_empty_string(self) -> None:
        def mutate(root: Path) -> None:
            path = root / ".github/ISSUE_TEMPLATE/workflow-request.yml"
            text = path.read_text(encoding="utf-8")
            extra_field = (
                "  - type: checkboxes\n"
                "    id: acknowledgement\n"
                "    attributes:\n"
                "      label: Acknowledgement\n"
                "      options:\n"
                "        - label: 42\n"
                "          required: true\n"
            )
            text = text.replace("  - type: checkboxes\n    id: privacy", extra_field + "  - type: checkboxes\n    id: privacy", 1)
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "checkboxes `acknowledgement` option 1 label must be a non-empty string")

    def test_checkbox_option_required_must_be_boolean(self) -> None:
        def mutate(root: Path) -> None:
            path = root / ".github/ISSUE_TEMPLATE/workflow-request.yml"
            text = path.read_text(encoding="utf-8")
            extra_field = (
                "  - type: checkboxes\n"
                "    id: acknowledgement\n"
                "    attributes:\n"
                "      label: Acknowledgement\n"
                "      options:\n"
                "        - label: I understand.\n"
                "          required: \"true\"\n"
            )
            text = text.replace("  - type: checkboxes\n    id: privacy", extra_field + "  - type: checkboxes\n    id: privacy", 1)
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "checkboxes `acknowledgement` option 1 required must be boolean")

    def test_checkbox_option_labels_must_be_unique(self) -> None:
        def mutate(root: Path) -> None:
            path = root / ".github/ISSUE_TEMPLATE/workflow-request.yml"
            text = path.read_text(encoding="utf-8")
            extra_field = (
                "  - type: checkboxes\n"
                "    id: acknowledgement\n"
                "    attributes:\n"
                "      label: Acknowledgement\n"
                "      options:\n"
                "        - label: I agree\n"
                "        - label: I agree\n"
            )
            text = text.replace("  - type: checkboxes\n    id: privacy", extra_field + "  - type: checkboxes\n    id: privacy", 1)
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "checkboxes `acknowledgement` option labels must be unique")

    def test_changed_privacy_confirmation_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / ".github/ISSUE_TEMPLATE/workflow-request.yml"
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("I removed", "I reviewed", 1), encoding="utf-8")

        self.assert_mutation_rejected(mutate, "privacy confirmation does not match the required structure")

    def test_missing_privacy_confirmation_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / ".github/ISSUE_TEMPLATE/workflow-request.yml"
            text = path.read_text(encoding="utf-8")
            text = text.split("  - type: checkboxes", maxsplit=1)[0]
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "privacy confirmation does not match the required structure")

    def test_issue_config_false_must_be_a_boolean(self) -> None:
        def mutate(root: Path) -> None:
            path = root / ".github/ISSUE_TEMPLATE/config.yml"
            text = path.read_text(encoding="utf-8")
            path.write_text(
                text.replace("blank_issues_enabled: false", 'blank_issues_enabled: "false"', 1),
                encoding="utf-8",
            )

        self.assert_mutation_rejected(mutate, "blank_issues_enabled must be boolean false")

    def test_windows_user_path_detector_is_isolated(self) -> None:
        def mutate(root: Path) -> None:
            windows_path = "C:" + "\\Users\\researcher\\private\\notes.txt"
            (root / "leak.ps1").write_text("# " + windows_path + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in leak.ps1")

    def test_posix_user_path_detector_is_isolated(self) -> None:
        def mutate(root: Path) -> None:
            home_path = "/" + "home" + "/researcher/private/notes.txt"
            (root / "leak.sh").write_text("#!/usr/bin/env bash\n# " + home_path + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in leak.sh")

    def test_bearer_token_detector_is_isolated(self) -> None:
        def mutate(root: Path) -> None:
            bearer = "Bear" + "er " + ("A" * 32)
            (root / "leak.txt").write_text("Authorization: " + bearer + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in leak.txt")

    def test_github_token_prefix_detector_is_isolated(self) -> None:
        def mutate(root: Path) -> None:
            github_token = "gh" + "p_" + ("A" * 36)
            (root / "leak.txt").write_text("value: " + github_token + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in leak.txt")

    def test_openai_token_prefix_detector_is_isolated(self) -> None:
        def mutate(root: Path) -> None:
            openai_token = "s" + "k-proj-" + ("A" * 32)
            (root / "leak.txt").write_text("value: " + openai_token + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in leak.txt")

    def test_database_password_in_env_local_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            name = "DATABASE_" + "PASSWORD"
            value = "database-credential-value-12345"
            (root / ".env.local").write_text(name + "=" + value + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in .env.local")

    def test_aws_secret_access_key_assignment_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            name = "AWS_" + "SECRET_ACCESS_KEY"
            value = "aws-credential-value-123456789"
            (root / ".env").write_text(name + "=" + value + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in .env")

    def test_prefixed_api_token_assignment_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            name = "SERVICE_" + "API_TOKEN"
            value = "service-credential-value-12345"
            (root / "settings.toml").write_text(name + " = \"" + value + "\"\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in settings.toml")

    def test_json_password_assignment_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            key = "pass" + "word"
            value = "json-credential-value-12345"
            content = "{\"" + key + "\": \"" + value + "\"}\n"
            (root / "credentials.json").write_text(content, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in credentials.json")

    def test_real_secret_value_starting_with_dollar_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            name = "TO" + "KEN"
            value = "$" + "real-credential-value-12345"
            (root / ".env").write_text(name + "=" + value + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in .env")

    def test_secret_value_starting_with_re_compile_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            name = "DATABASE_" + "PASSWORD"
            value = "re." + "compile-real-credential-12345"
            (root / ".env").write_text(name + "=" + value + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in .env")

    def test_macos_user_path_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            home_path = "/" + "Users" + "/researcher/private/notes.txt"
            (root / "leak.cfg").write_text("source=" + home_path + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in leak.cfg")

    def test_pem_private_key_file_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            header = "-----BEGIN " + "PRIVATE KEY-----"
            (root / "private.pem").write_text(header + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in private.pem")

    def test_key_private_key_file_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            header = "-----BEGIN " + "PRIVATE KEY-----"
            (root / "private.key").write_text(header + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in private.key")

    def test_authentic_dsa_private_key_header_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            header = "-----BEGIN " + "DSA PRIVATE KEY-----"
            (root / "id_dsa").write_text(header + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in id_dsa")

    def test_encrypted_pkcs8_private_key_header_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            header = "-----BEGIN " + "ENCRYPTED PRIVATE KEY-----"
            (root / "encrypted.pem").write_text(header + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, "possible private/disallowed token in encrypted.pem")

    def test_standard_extensionless_private_key_filenames_are_rejected(self) -> None:
        for filename in ("id_rsa", "id_dsa", "id_ecdsa", "id_ed25519"):
            with self.subTest(filename=filename):
                def mutate(root: Path, key_filename: str = filename) -> None:
                    header = "-----BEGIN " + "PRIVATE KEY-----"
                    (root / key_filename).write_text(header + "\n", encoding="utf-8")

                self.assert_mutation_rejected(mutate, f"possible private/disallowed token in {filename}")

    def test_documented_placeholders_are_allowed(self) -> None:
        temporary, root = self.fixture()
        self.addCleanup(temporary.cleanup)
        placeholder_path = "C:" + "\\Users\\<user>\\.codex\\skills"
        placeholder_lines = [
            "OPENAI_" + "API_KEY=" + "YOUR_OPENAI_API_KEY",
            "PASS" + "WORD=" + "[password]",
            "SERVICE_" + "TOKEN=" + "<token>",
            "CLIENT_" + "SECRET=" + "{secret}",
            "DATABASE_" + "PASSWORD=" + "$HOME",
            "AUTH_" + "TOKEN=" + "${CODEX_HOME}",
            "PRIVATE_" + "KEY=" + "%USERPROFILE%",
            "SKILLS_ROOT=$HOME/.codex/skills",
            "CODEX_SKILLS=${CODEX_HOME:-$HOME/.codex}/skills",
            "WINDOWS_SKILLS=" + placeholder_path,
        ]
        content = "\n".join(placeholder_lines) + "\n"
        (root / "placeholders.env").write_text(content, encoding="utf-8")

        completed = self.run_validator(root)

        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_missing_validation_venv_command_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            self.ensure_validation_venv_contract(root)
            path = root / "README.en.md"
            text = path.read_text(encoding="utf-8")
            text = text.replace(
                ".\\.venv-validation\\Scripts\\python.exe -m pip install -r requirements-validation.txt\n",
                "",
                1,
            )
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "README.en.md validation instructions missing isolated command")

    def test_unisolated_local_pip_instruction_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            self.ensure_validation_venv_contract(root)
            path = root / "README.md"
            text = path.read_text(encoding="utf-8")
            text = text.replace(
                "python -m venv .venv-validation",
                "python -m pip install -r requirements-validation.txt\npython -m venv .venv-validation",
                1,
            )
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "README.md must not recommend unisolated validation pip")

    def test_missing_acknowledgement_index_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "README.md"
            text = path.read_text(encoding="utf-8")
            text = text.replace("references/meta/external-skill-sources.md", "references/index.md", 1)
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "README.md missing interface element: references/meta/external-skill-sources.md")

    def test_release_link_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "README.en.md"
            text = path.read_text(encoding="utf-8")
            text += "\nhttps://github.com/example/project/releases/latest\n"
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "README.en.md contains removed Release guidance: /releases/")

    def test_chinese_repository_install_route_is_validated(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "README.md"
            text = path.read_text(encoding="utf-8")
            text = text.replace("### 从仓库安装（推荐）", "### 仓库获取")
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "README.md installation route `### 从仓库安装（推荐）` missing")

    def test_stale_private_repository_guidance_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "README.en.md"
            text = path.read_text(encoding="utf-8")
            if "In this private repository" not in text:
                text += "\nIn this private repository, issue forms are private.\n"
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "README.en.md contains stale private-repository guidance")

    def test_validation_venv_must_be_ignored(self) -> None:
        def mutate(root: Path) -> None:
            self.ensure_validation_venv_contract(root)
            path = root / ".gitignore"
            lines = [line for line in path.read_text(encoding="utf-8").splitlines() if line != ".venv-validation/"]
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")

        self.assert_mutation_rejected(mutate, ".gitignore must ignore .venv-validation/")

    def test_validation_venv_is_excluded_from_distribution_scan(self) -> None:
        temporary, root = self.fixture()
        self.addCleanup(temporary.cleanup)
        package = root / ".venv-validation/Lib/site-packages/example.py"
        package.parent.mkdir(parents=True)
        name = "DATABASE_" + "PASSWORD"
        package.write_text(name + "=third-party-example-value\n", encoding="utf-8")

        completed = self.run_validator(root)

        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def test_accidental_separator_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "README.en.md"
            text = path.read_text(encoding="utf-8")
            bad_separator = "\u74ba\u75d0"
            for separator in ("\u00b7", "\u8def"):
                if separator in text:
                    text = text.replace(separator, bad_separator, 1)
                    break
            else:
                self.fail("README.en.md has no navigation separator to mutate")
            path.write_text(text, encoding="utf-8")

        self.assert_mutation_rejected(mutate, "forbidden separator")

    def test_oversized_english_banner_title_is_rejected(self) -> None:
        def mutate(root: Path) -> None:
            path = root / "assets/readme-banner-en.svg"
            tree = ET.parse(path)
            title = next(
                element
                for element in tree.getroot().iter()
                if element.text == "Civil Engineering Academic Writing Skill"
                and element.tag.endswith("text")
            )
            title.set("font-size", "53")
            tree.write(path, encoding="utf-8", xml_declaration=False)

        self.assert_mutation_rejected(mutate, "English banner title font-size must be at most 52px")


if __name__ == "__main__":
    unittest.main(verbosity=2)
