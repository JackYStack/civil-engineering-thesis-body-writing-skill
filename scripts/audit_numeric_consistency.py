#!/usr/bin/env python3
"""Read-only checks of explicitly mapped CSV values; not a scientific validator."""

from __future__ import annotations

import argparse
import csv
from decimal import Decimal, InvalidOperation, localcontext
import hashlib
import io
import json
from pathlib import Path
import re
import sys


class AuditError(ValueError):
    pass


def fields(obj: object, allowed: set[str], required: set[str], label: str) -> dict:
    if not isinstance(obj, dict):
        raise AuditError(f'{label}: expected an object')
    if set(obj) - allowed or required - set(obj):
        raise AuditError(f'{label}: unknown or missing fields')
    return obj


def name(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise AuditError(f'{label}: expected a nonempty string')
    return value


def number(value: object) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (str, int, float, Decimal)):
        raise AuditError('Expected a finite numeric value, not a boolean/null/object')
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise AuditError(f'Invalid numeric value: {value!r}') from exc
    if not result.is_finite():
        raise AuditError('Nonfinite numeric value')
    return result


class Data:
    def __init__(self, specs: object, base: Path):
        if not isinstance(specs, dict) or not specs:
            raise AuditError('datasets must be a nonempty object')
        self.tables = {}
        self.receipts = {}
        base = base.resolve()
        for key, spec in specs.items():
            name(key, 'dataset id')
            fields(spec, {'path', 'sha256'}, {'path'}, f'dataset {key}')
            relative = Path(name(spec['path'], 'dataset path'))
            path = (base / relative).resolve()
            if relative.is_absolute() or not path.is_relative_to(base):
                raise AuditError(f'{key}: dataset path must stay under the spec directory')
            raw = path.read_bytes()
            digest = hashlib.sha256(raw).hexdigest()
            if 'sha256' in spec:
                expected = spec['sha256']
                if not isinstance(expected, str) or not re.fullmatch('[0-9a-fA-F]{64}', expected):
                    raise AuditError(f'{key}: invalid SHA-256')
                if digest != expected.lower():
                    raise AuditError(f'{key}: source hash mismatch')
            try:
                reader = csv.DictReader(io.StringIO(raw.decode('utf-8-sig'), newline=''))
                headers = reader.fieldnames
                if not headers or any(not h.strip() for h in headers) or len(set(headers)) != len(headers):
                    raise AuditError(f'{key}: missing/blank/duplicate CSV headers')
                rows = list(reader)
                if not rows or any(None in row or any(v is None for v in row.values()) for row in rows):
                    raise AuditError(f'{key}: empty or ragged CSV')
            except (UnicodeError, csv.Error) as exc:
                raise AuditError(f'{key}: invalid UTF-8 CSV') from exc
            self.tables[key] = (set(headers), rows)
            self.receipts[key] = {'path': spec['path'], 'sha256': digest, 'rows': len(rows)}

    def column(self, dataset: object, column: object) -> list[str]:
        key, col = name(dataset, 'dataset'), name(column, 'column')
        if key not in self.tables or col not in self.tables[key][0]:
            raise AuditError(f'Unknown dataset/column: {key}/{col}')
        return [row[col] for row in self.tables[key][1]]

    def cell(self, locator: object) -> Decimal:
        keys = {'dataset', 'row_key', 'row_id', 'column'}
        item = fields(locator, keys, keys, 'cell locator')
        ids = self.column(item['dataset'], item['row_key'])
        values = self.column(item['dataset'], item['column'])
        row_id = name(item['row_id'], 'row_id')
        matches = [v for k, v in zip(ids, values) if k == row_id]
        if len(matches) != 1:
            raise AuditError('Cell locator must identify exactly one row')
        return number(matches[0])


def compare(computed: Decimal, reported: object, check: dict) -> dict:
    actual = number(reported)
    absolute = number(check.get('abs_tol', '1e-9'))
    relative = number(check.get('rel_tol', 0))
    if absolute < 0 or relative < 0:
        raise AuditError('Tolerances must be nonnegative')
    tolerance = max(absolute, relative * abs(computed))
    difference = abs(actual - computed)
    return {'status': 'PASS' if difference <= tolerance else 'FAIL',
            'computed': str(computed), 'reported': str(actual),
            'absolute_difference': str(difference), 'tolerance': str(tolerance)}


def check_one(check: object, data: Data) -> dict:
    common = {'id', 'kind', 'abs_tol', 'rel_tol'}
    variants = {
        'aggregate': {'dataset', 'column', 'operation', 'reported', 'missing'},
        'relative_change': {'baseline', 'current', 'reported', 'scale'},
        'regression_metrics': {'dataset', 'actual', 'predicted', 'reported'},
        'split_disjoint': {'dataset', 'split_column', 'group_column'},
    }
    if not isinstance(check, dict) or check.get('kind') not in variants:
        raise AuditError('Unknown check kind')
    kind = check['kind']
    required = {
        'aggregate': {'dataset', 'column', 'operation', 'reported'},
        'relative_change': {'baseline', 'current', 'reported'},
        'regression_metrics': {'dataset', 'actual', 'predicted', 'reported'},
        'split_disjoint': {'dataset', 'split_column', 'group_column'},
    }[kind]
    fields(check, common | variants[kind], {'id', 'kind'} | required, 'check')
    name(check['id'], 'check id')
    for field in ('abs_tol', 'rel_tol'):
        if field in check and number(check[field]) < 0:
            raise AuditError('Tolerances must be nonnegative')

    if kind == 'aggregate':
        policy = check.get('missing', 'error')
        if policy not in ('error', 'exclude'):
            raise AuditError('missing must be error or exclude')
        source = data.column(check['dataset'], check['column'])
        missing = {'', 'na', 'n/a', 'null', 'none', 'nan'}
        values = [number(v) for v in source if v.strip().lower() not in missing]
        excluded = len(source) - len(values)
        if not values or (excluded and policy == 'error'):
            raise AuditError('Missing data or no usable observations')
        operation = check['operation']
        if operation == 'sum':
            result = sum(values, Decimal(0))
        elif operation == 'mean':
            result = sum(values, Decimal(0)) / len(values)
        elif operation == 'min':
            result = min(values)
        elif operation == 'max':
            result = max(values)
        else:
            raise AuditError('Unknown aggregate operation')
        return {**compare(result, check['reported'], check), 'used': len(values), 'excluded': excluded}

    if kind == 'relative_change':
        baseline, current = data.cell(check['baseline']), data.cell(check['current'])
        if baseline == 0:
            raise AuditError('Relative change undefined at a zero baseline')
        scale = check.get('scale', 'ratio')
        if scale not in ('ratio', 'percent'):
            raise AuditError('scale must be ratio or percent')
        result = (current - baseline) / baseline * (100 if scale == 'percent' else 1)
        return {**compare(result, check['reported'], check), 'scale': scale}

    if kind == 'regression_metrics':
        truth = [number(v) for v in data.column(check['dataset'], check['actual'])]
        predicted = [number(v) for v in data.column(check['dataset'], check['predicted'])]
        supported = {'mae', 'rmse', 'mbe', 'r2', 'mape'}
        reported = fields(check['reported'], supported, set(), 'reported metrics')
        if not reported:
            raise AuditError('At least one reported metric is required')
        errors = [p - y for p, y in zip(predicted, truth)]
        n = len(truth)
        squared = sum((v * v for v in errors), Decimal(0))
        computed = {'mae': sum(map(abs, errors), Decimal(0)) / n,
                    'mbe': sum(errors, Decimal(0)) / n,
                    'rmse': (squared / n).sqrt()}
        if 'r2' in reported:
            center = sum(truth, Decimal(0)) / n
            denominator = sum(((v - center) ** 2 for v in truth), Decimal(0))
            if n < 2 or denominator == 0:
                raise AuditError('R-squared undefined for fewer than two or constant observations')
            computed['r2'] = 1 - squared / denominator
        if 'mape' in reported:
            if any(v == 0 for v in truth):
                raise AuditError('MAPE undefined at zero observations')
            computed['mape'] = sum((abs(e / y) for e, y in zip(errors, truth)), Decimal(0)) / n
        comparisons = {key: compare(computed[key], value, check) for key, value in reported.items()}
        return {'status': 'PASS' if all(v['status'] == 'PASS' for v in comparisons.values()) else 'FAIL',
                'n': n, 'metrics': comparisons, 'mbe_convention': 'predicted - actual', 'mape_scale': 'ratio'}

    if check['split_column'] == check['group_column']:
        raise AuditError('Split and group columns must differ')
    splits = data.column(check['dataset'], check['split_column'])
    groups = data.column(check['dataset'], check['group_column'])
    partitions: dict[str, set[str]] = {}
    for split, group in zip(splits, groups):
        if not split.strip() or not group.strip():
            raise AuditError('Blank split/group labels')
        if split != split.strip() or group != group.strip():
            raise AuditError('Surrounding whitespace in split/group labels must be resolved explicitly')
        partitions.setdefault(group, set()).add(split)
    if len(set(splits)) < 2:
        raise AuditError('Need at least two partitions to check disjointness')
    overlap = {g: sorted(p) for g, p in partitions.items() if len(p) > 1}
    return {'status': 'FAIL' if overlap else 'PASS', 'overlap': overlap,
            'rows': len(groups), 'groups': len(partitions), 'partitions': sorted(set(splits))}


def audit(spec: object, base: Path) -> dict:
    report = {'schema_version': 1, 'status': 'FAIL', 'datasets': {}, 'checks': [], 'errors': [],
              'scope': 'Declared numeric/ID checks only; not scientific, semantic, leakage, or visual certification.'}
    try:
        fields(spec, {'schema_version', 'datasets', 'checks'}, {'schema_version', 'datasets', 'checks'}, 'spec')
        if type(spec['schema_version']) is not int or spec['schema_version'] != 1:
            raise AuditError('Unsupported schema_version')
        checks = spec['checks']
        if not isinstance(checks, list) or not checks:
            raise AuditError('checks must be a nonempty list')
        ids = [name(c.get('id'), 'check id') if isinstance(c, dict) else '' for c in checks]
        if not all(ids) or len(set(ids)) != len(ids):
            raise AuditError('Check IDs must be nonempty and unique')
        data = Data(spec['datasets'], base)
        report['datasets'] = data.receipts
        for check in checks:
            try:
                with localcontext() as ctx:
                    ctx.prec = 40
                    result = check_one(check, data)
            except (AuditError, ArithmeticError, TypeError, KeyError) as exc:
                result = {'status': 'FAIL', 'error': str(exc)}
            report['checks'].append({'id': check['id'], 'kind': check.get('kind'), **result})
        if all(c['status'] == 'PASS' for c in report['checks']):
            report['status'] = 'PASS'
    except (AuditError, OSError, TypeError, KeyError, ArithmeticError) as exc:
        report['errors'].append(str(exc))
    return report


def unique_pairs(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise AuditError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def reject_constant(value: str):
    raise AuditError(f'Nonfinite JSON constant: {value}')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('spec', type=Path)
    args = parser.parse_args()
    try:
        spec = json.loads(args.spec.read_text(encoding='utf-8-sig'), parse_float=Decimal,
                          object_pairs_hook=unique_pairs, parse_constant=reject_constant)
        report = audit(spec, args.spec.resolve().parent)
    except (OSError, UnicodeError, ValueError) as exc:
        report = {'status': 'FAIL', 'errors': [str(exc)]}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report['status'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
