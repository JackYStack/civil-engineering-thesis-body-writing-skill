"""Isolated deployment tests; these do not invoke an agent or mutate user profiles."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import zipfile

import install_agent as installer


class AgentInstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = self.root / 'source'
        self.source.mkdir()
        for path, content in {
            'SKILL.md': '---\nname: civil-thesis-body-writing\ndescription: Write civil engineering prose.\n---\nRead references/workflows/agent-compatibility.md.\n',
            'manifest.yaml': 'name: civil-thesis-body-writing\n',
            'static/core/stance.md': 'Do not invent data.\n',
            'references/workflows/agent-compatibility.md': 'Keep host boundaries.\n',
            'references/style/example.md': 'Keep uncertainty.\n',
            'agents/openai.yaml': 'Codex only\n',
            '.git/config': 'do not export\n',
            'scripts/__pycache__/cached.pyc': 'do not export\n',
            'scripts/install.ps1': 'do not export\n',
            'scripts/tool.py': 'print("ok")\n',
            'private.md': 'not part of public skill\n',
            'LICENSE': 'Preserve distribution terms.\n',
        }.items():
            target = self.source / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding='utf-8')

    def test_claude_user_location(self):
        self.assertEqual(installer.destination('claude-code', 'user', None, self.root), self.root / '.claude/skills' / installer.NAME)

    def test_project_locations(self):
        for agent, folder in [('claude-code', '.claude'), ('workbuddy', '.codebuddy')]:
            self.assertEqual(installer.destination(agent, 'project', self.root), self.root / folder / 'skills' / installer.NAME)

    def test_project_requires_directory(self):
        for value in (None, self.root / 'missing'):
            with self.assertRaises(ValueError):
                installer.destination('workbuddy', 'project', value)

    def test_personal_workbuddy_is_explicitly_unsupported(self):
        with self.assertRaises(ValueError):
            installer.destination('workbuddy', 'user', None)

    def test_user_scope_rejects_project_argument(self):
        with self.assertRaises(ValueError):
            installer.destination('claude-code', 'user', self.root)

    def test_install_copies_references_and_static(self):
        target = self.root / 'project/.claude/skills' / installer.NAME
        installer.install(self.source, target, 'claude-code')
        for name in ('SKILL.md', 'manifest.yaml', 'static/core/stance.md', 'references/style/example.md'):
            self.assertEqual((target / name).read_bytes(), (self.source / name).read_bytes())
        self.assertFalse((target / 'agents').exists())

    def test_existing_install_preserved_without_replace(self):
        target = self.root / 'target'
        target.mkdir()
        (target / 'custom.txt').write_text('preserve me')
        with self.assertRaises(ValueError):
            installer.install(self.source, target, 'claude-code')
        self.assertEqual((target / 'custom.txt').read_text(), 'preserve me')

    def test_replace_retains_backup(self):
        target = self.root / 'target'
        target.mkdir()
        (target / 'custom.txt').write_text('preserve me')
        backup = installer.install(self.source, target, 'claude-code', replace=True)
        self.assertEqual((backup / 'custom.txt').read_text(), 'preserve me')
        self.assertTrue((target / 'SKILL.md').is_file())

    def test_overlap_refused(self):
        for target in (self.source, self.source / 'nested', self.root):
            with self.assertRaises(ValueError):
                installer.install(self.source, target, 'claude-code', replace=True)

    def test_workbuddy_metadata_does_not_change_source(self):
        original = (self.source / 'SKILL.md').read_bytes()
        exported = installer.payload(self.source, 'workbuddy')['SKILL.md'].decode()
        for key in ('display_name:', 'display_name_en:', 'description_zh:', 'description_en:', 'version:', 'author:'):
            self.assertIn(key, exported)
        self.assertEqual((self.source / 'SKILL.md').read_bytes(), original)
        self.assertEqual(exported.split('---', 2)[2], original.decode().replace('\r\n', '\n').split('---', 2)[2])

    def test_export_excludes_nonportable_and_unknown_files(self):
        names = installer.payload(self.source, 'workbuddy')
        self.assertNotIn('.git/config', names)
        self.assertNotIn('private.md', names)
        self.assertNotIn('agents/openai.yaml', names)
        self.assertNotIn('scripts/install.ps1', names)
        self.assertIn('scripts/tool.py', names)
        self.assertIn('LICENSE', names)

    def test_zip_structure_and_unicode_paths(self):
        output = self.root / '\u5bfc\u51fa' / 'skill.zip'
        installer.package(self.source, output, 'workbuddy')
        with zipfile.ZipFile(output) as archive:
            self.assertIsNone(archive.testzip())
            self.assertIn(installer.NAME + '/SKILL.md', archive.namelist())
            self.assertTrue(all(n.startswith(installer.NAME + '/') and '..' not in Path(n).parts for n in archive.namelist()))

    def test_existing_zip_not_overwritten(self):
        output = self.root / 'skill.zip'
        output.write_bytes(b'old archive')
        with self.assertRaises(FileExistsError):
            installer.package(self.source, output, 'workbuddy')
        self.assertEqual(output.read_bytes(), b'old archive')

    def test_missing_core_fails_before_install(self):
        (self.source / 'manifest.yaml').unlink()
        with self.assertRaises(ValueError):
            installer.install(self.source, self.root / 'target', 'claude-code')
        self.assertFalse((self.root / 'target').exists())

    def test_failed_replacement_restores_original(self):
        target = self.root / 'target'
        target.mkdir()
        (target / 'custom.txt').write_text('preserve me')
        original_rename = Path.rename

        def rename(path, destination):
            if path.name == installer.NAME:
                raise OSError('simulated final placement failure')
            return original_rename(path, destination)

        with mock.patch.object(Path, 'rename', rename):
            with self.assertRaises(OSError):
                installer.install(self.source, target, 'claude-code', replace=True)
        self.assertEqual((target / 'custom.txt').read_text(), 'preserve me')

    def test_linked_destination_is_refused(self):
        target = self.root / 'target'
        with mock.patch.object(installer, 'linked', side_effect=lambda p: p == target):
            with self.assertRaises(ValueError):
                installer.install(self.source, target, 'claude-code')

    def test_cli_project_install(self):
        result = subprocess.run([sys.executable, '-X', 'utf8', str(installer.SOURCE / 'scripts/install_agent.py'), 'install', '--agent', 'workbuddy', '--scope', 'project', '--project-root', str(self.root)], capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0, result.stderr)
        installed = self.root / '.codebuddy/skills' / installer.NAME
        self.assertTrue((installed / 'references/workflows/agent-compatibility.md').is_file())
        text = (installed / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('display_name_en:', text)


if __name__ == '__main__':
    unittest.main()
