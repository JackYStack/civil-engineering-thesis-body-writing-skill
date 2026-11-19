#!/usr/bin/env python3
"""Export/install shared writing rules without editing host configuration."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import stat
import tempfile
import uuid
import zipfile

NAME = 'civil-thesis-body-writing'
SOURCE = Path(__file__).resolve().parents[1]
ROOT_FILES = {'SKILL.md', 'manifest.yaml', 'README.md', 'README.en.md', 'requirements-validation.txt', 'LICENSE', 'LICENSE.txt', 'NOTICE', 'NOTICE.txt'}
DIRECTORIES = {'static', 'references', 'scripts', 'assets'}
SUFFIXES = {'.md', '.yaml', '.yml', '.py', '.svg', '.png', '.jpg', '.jpeg', '.json', '.txt'}


def linked(path: Path) -> bool:
    try:
        attrs = getattr(path.lstat(), 'st_file_attributes', 0)
    except FileNotFoundError:
        return False
    return path.is_symlink() or bool(attrs & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0))


def payload(source: Path, agent: str) -> dict[str, bytes]:
    result = {}
    for path in sorted(source.rglob('*')):
        rel = path.relative_to(source)
        if any(p.startswith('.') or p == '__pycache__' for p in rel.parts):
            continue
        if not (str(rel) in ROOT_FILES or rel.parts[0] in DIRECTORIES):
            continue
        if linked(path) or source.resolve() not in path.resolve().parents:
            raise ValueError(f'Linked resource is not exportable: {rel}')
        if not path.is_file() or (str(rel) not in ROOT_FILES and path.suffix.lower() not in SUFFIXES):
            continue
        result[rel.as_posix()] = path.read_bytes()
    for required in ('SKILL.md', 'manifest.yaml', 'static/core/stance.md', 'references/workflows/agent-compatibility.md'):
        if required not in result:
            raise ValueError(f'Missing required resource: {required}')
    if agent == 'workbuddy':
        text = result['SKILL.md'].decode('utf-8-sig').replace('\r\n', '\n')
        if not text.startswith('---\n'):
            raise ValueError('Invalid SKILL.md frontmatter')
        _, metadata, body = text.split('---', 2)
        if 'display_name:' in metadata:
            raise ValueError('Unexpected existing platform metadata')
        metadata += ('display_name: 土木论文写作\ndisplay_name_en: Civil Engineering Thesis Writing\n'
                     'description_zh: 土木工程论文起草、润色、引用核查与审稿局部修订。\n'
                     'description_en: Civil-engineering drafting, polishing, citation support, and reviewer revision.\n'
                     'version: "0.1.0"\nauthor: "JackYStack repository maintainers"\n')
        result['SKILL.md'] = ('---' + metadata + '---' + body).encode('utf-8')
    return result


def destination(agent: str, scope: str, project: Path | None, home: Path | None = None) -> Path:
    if scope == 'project':
        if project is None or not project.is_dir():
            raise ValueError('Project scope requires an existing --project-root directory')
        root = project.resolve()
    else:
        if project is not None:
            raise ValueError('--project-root is valid only with --scope project')
        if agent == 'workbuddy':
            raise ValueError('Use WorkBuddy local-package upload for personal skills; no global directory is assumed')
        root = home or Path.home()
    return root / ('.claude' if agent == 'claude-code' else '.codebuddy') / 'skills' / NAME


def check_location(source: Path, target: Path):
    source, resolved = source.resolve(), target.resolve()
    if source == resolved or source in resolved.parents or resolved in source.parents:
        raise ValueError('Source and destination must not contain each other')
    for path in (target, *target.parents):
        if linked(path):
            raise ValueError('Linked destination or parent is not supported')


def install(source: Path, target: Path, agent: str, replace: bool = False) -> Path | None:
    check_location(source, target)
    files = payload(source, agent)
    if target.exists() and (not target.is_dir() or not replace):
        raise ValueError('Destination exists; inspect it and use --replace to back it up before updating')
    target.parent.mkdir(parents=True, exist_ok=True)
    backup = None
    with tempfile.TemporaryDirectory(prefix='.skill-stage-', dir=target.parent) as staging:
        staged = Path(staging) / NAME
        for name, content in files.items():
            path = staged / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        if target.exists():
            stamp = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')
            backup = target.with_name(f'{NAME}.bak-{stamp}-{uuid.uuid4().hex[:8]}')
            target.rename(backup)
        try:
            staged.rename(target)
        except OSError:
            if backup is not None and not target.exists():
                backup.rename(target)
            raise
    return backup


def package(source: Path, output: Path, agent: str):
    if output.suffix.lower() != '.zip':
        raise ValueError('Package output must end in .zip')
    check_location(source, output)
    files = payload(source, agent)
    output.parent.mkdir(parents=True, exist_ok=True)
    created = False
    try:
        with output.open('xb') as stream:
            created = True
            with zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
                for name, content in files.items():
                    archive.writestr(f'{NAME}/{name}', content)
    except Exception:
        if created:
            output.unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='operation', required=True)
    setup = commands.add_parser('install')
    setup.add_argument('--agent', choices=('claude-code', 'workbuddy'), required=True)
    setup.add_argument('--scope', choices=('user', 'project'), required=True)
    setup.add_argument('--project-root', type=Path)
    setup.add_argument('--replace', action='store_true')
    export = commands.add_parser('package')
    export.add_argument('--agent', choices=('claude-code', 'workbuddy'), required=True)
    export.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.operation == 'install':
            target = destination(args.agent, args.scope, args.project_root)
            backup = install(SOURCE, target, args.agent, args.replace)
            print(f'Installed for {args.agent}: {target}')
            if backup:
                print(f'Previous installation retained: {backup}')
            print('Open the intended project/session and confirm skill discovery; no host settings were changed.')
        else:
            package(SOURCE, args.output, args.agent)
            print(f'Package created for {args.agent}: {args.output.resolve()}')
            print('Import and enable it in the host; package creation does not prove host acceptance.')
    except (ValueError, OSError) as error:
        parser.exit(1, f'Not installed/exported: {error}\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
