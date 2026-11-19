#!/usr/bin/env python3
"""Numeric invariants, invalid-input behavior and CLI read-only regression tests."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from audit_numeric_consistency import audit


class NumericChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.csv = self.base / 'data.csv'
        self.csv.write_text('id,y,pred,split,group\na,10,12,train,g1\nb,20,18,val,g2\nc,30,36,test,g3\n', encoding='utf-8')
        self.spec = {'schema_version': 1, 'datasets': {'d': {'path': 'data.csv'}}, 'checks': []}

    def run_check(self, kind='aggregate', **extra):
        self.spec['checks'] = [{'id': 'check', 'kind': kind, **extra}]
        return audit(self.spec, self.base)

    def aggregate(self, **extra):
        options = {'dataset': 'd', 'column': 'y', 'operation': 'mean', 'reported': 20}
        options.update(extra)
        return self.run_check(**options)

    def cell(self, row):
        return {'dataset': 'd', 'row_key': 'id', 'row_id': row, 'column': 'y'}

    def metrics(self, reported, **extra):
        return self.run_check('regression_metrics', dataset='d', actual='y', predicted='pred', reported=reported, **extra)

    def test_aggregate_operations(self):
        for operation, value in [('mean', 20), ('sum', 60), ('min', 10), ('max', 30)]:
            with self.subTest(operation=operation):
                self.assertEqual(self.aggregate(operation=operation, reported=value)['status'], 'PASS')

    def test_wrong_reported_value_is_failure(self):
        self.assertEqual(self.aggregate(reported=21)['status'], 'FAIL')

    def test_explicit_absolute_rounding_tolerance(self):
        self.assertEqual(self.aggregate(reported='20.04', abs_tol='.05')['status'], 'PASS')
        self.assertEqual(self.aggregate(reported='20.06', abs_tol='.05')['status'], 'FAIL')

    def test_relative_tolerance(self):
        self.assertEqual(self.aggregate(reported='20.1', abs_tol=0, rel_tol='.01')['status'], 'PASS')
        self.assertEqual(self.aggregate(reported='20.3', abs_tol=0, rel_tol='.01')['status'], 'FAIL')

    def test_negative_and_nonfinite_tolerance(self):
        for value in ['-1', 'NaN', 'Infinity']:
            with self.subTest(value=value):
                self.assertEqual(self.aggregate(abs_tol=value)['status'], 'FAIL')

    def test_missing_defaults_to_error(self):
        self.csv.write_text('id,y\na,10\nb,\nc,30\n', encoding='utf-8')
        self.assertEqual(self.aggregate()['status'], 'FAIL')

    def test_exclusion_is_explicit_and_counted(self):
        self.csv.write_text('id,y\na,10\nb,NA\nc,30\n', encoding='utf-8')
        report = self.aggregate(missing='exclude')
        self.assertEqual(report['status'], 'PASS')
        self.assertEqual(report['checks'][0]['excluded'], 1)
        self.assertEqual(report['checks'][0]['used'], 2)

    def test_all_missing_never_passes(self):
        self.csv.write_text('y\nNA\nnull\n', encoding='utf-8')
        self.assertEqual(self.aggregate(missing='exclude')['status'], 'FAIL')

    def test_unknown_field_cannot_silently_change_policy(self):
        self.assertEqual(self.aggregate(missng='exclude')['status'], 'FAIL')
        self.assertEqual(self.aggregate(missing='ignore')['status'], 'FAIL')

    def test_no_code_evaluation(self):
        self.assertEqual(self.aggregate(reported="__import__('os').getcwd()")['status'], 'FAIL')

    def test_relative_change_ratio_and_percent_are_not_interchangeable(self):
        args = {'baseline': self.cell('a'), 'current': self.cell('b')}
        self.assertEqual(self.run_check('relative_change', reported=1, **args)['status'], 'PASS')
        self.assertEqual(self.run_check('relative_change', reported=100, **args)['status'], 'FAIL')
        self.assertEqual(self.run_check('relative_change', reported=100, scale='percent', **args)['status'], 'PASS')

    def test_negative_relative_change(self):
        report = self.run_check('relative_change', baseline=self.cell('b'), current=self.cell('a'), reported='-.5')
        self.assertEqual(report['status'], 'PASS')

    def test_zero_baseline_is_undefined(self):
        self.csv.write_text('id,y\na,0\nb,10\n', encoding='utf-8')
        self.assertEqual(self.run_check('relative_change', baseline=self.cell('a'), current=self.cell('b'), reported=0)['status'], 'FAIL')

    def test_duplicate_or_missing_cell_identity_fails(self):
        self.csv.write_text('id,y\na,10\na,20\n', encoding='utf-8')
        for row in ['a', 'missing']:
            with self.subTest(row=row):
                report = self.run_check('relative_change', baseline=self.cell(row), current=self.cell(row), reported=0)
                self.assertEqual(report['status'], 'FAIL')

    def test_metrics_against_independent_arithmetic(self):
        report = self.metrics({'mae': 10 / 3, 'mbe': 2, 'rmse': (44 / 3) ** .5, 'r2': .78, 'mape': 1 / 6})
        self.assertEqual(report['status'], 'PASS')

    def test_signed_bias_is_not_absolute_error(self):
        self.assertEqual(self.metrics({'mbe': 10 / 3})['status'], 'FAIL')

    def test_negative_r2_is_valid(self):
        self.csv.write_text('y,pred\n1,10\n2,10\n3,10\n', encoding='utf-8')
        self.assertEqual(self.metrics({'r2': -96})['status'], 'PASS')

    def test_undefined_metrics_do_not_silently_become_zero(self):
        for contents, metric in [('y,pred\n1,1\n1,1\n', 'r2'), ('y,pred\n0,1\n1,1\n', 'mape'), ('y,pred\n1,1\n', 'r2')]:
            with self.subTest(metric=metric, contents=contents):
                self.csv.write_text(contents, encoding='utf-8')
                self.assertEqual(self.metrics({metric: 0})['status'], 'FAIL')

    def test_constant_truth_still_allows_defined_mae(self):
        self.csv.write_text('y,pred\n1,2\n1,2\n', encoding='utf-8')
        self.assertEqual(self.metrics({'mae': 1})['status'], 'PASS')

    def test_empty_or_unknown_metrics_fail(self):
        for metrics in [{}, {'accuracy': 1}]:
            self.assertEqual(self.metrics(metrics)['status'], 'FAIL')

    def test_nonfinite_and_missing_pairs_fail(self):
        for value in ['NaN', 'Infinity', '', 'N/A']:
            self.csv.write_text(f'y,pred\n1,{value}\n2,2\n', encoding='utf-8')
            self.assertEqual(self.metrics({'mae': 0})['status'], 'FAIL')

    def test_metric_scaling_and_row_order_invariants(self):
        self.csv.write_text('y,pred\n300,360\n100,120\n200,180\n', encoding='utf-8')
        self.assertEqual(self.metrics({'mae': 100 / 3, 'rmse': ((44 / 3) ** .5) * 10, 'mbe': 20, 'r2': .78, 'mape': 1 / 6})['status'], 'PASS')

    def test_disjoint_groups_pass(self):
        self.assertEqual(self.run_check('split_disjoint', dataset='d', split_column='split', group_column='group')['status'], 'PASS')

    def test_shared_group_across_partitions_fails(self):
        self.csv.write_text('split,group\ntrain,g1\ntest,g1\n', encoding='utf-8')
        report = self.run_check('split_disjoint', dataset='d', split_column='split', group_column='group')
        self.assertEqual(report['status'], 'FAIL')
        self.assertEqual(report['checks'][0]['overlap'], {'g1': ['test', 'train']})

    def test_degenerate_or_blank_group_checks_fail(self):
        for contents in ['split,group\ntrain,g1\ntrain,g2\n', 'split,group\ntrain,g1\ntest,\n', 'split,group\ntrain,g1\ntest, g1\n']:
            self.csv.write_text(contents, encoding='utf-8')
            self.assertEqual(self.run_check('split_disjoint', dataset='d', split_column='split', group_column='group')['status'], 'FAIL')

    def test_empty_check_list_or_duplicate_ids_fail(self):
        self.assertEqual(audit(self.spec, self.base)['status'], 'FAIL')
        self.aggregate()
        self.spec['checks'] *= 2
        self.assertEqual(audit(self.spec, self.base)['status'], 'FAIL')

    def test_no_sources_or_unknown_dataset_column_fail(self):
        self.assertEqual(self.aggregate(column='unknown')['status'], 'FAIL')
        self.assertEqual(self.aggregate(dataset='unknown')['status'], 'FAIL')
        self.spec['datasets'] = {}
        self.assertEqual(audit(self.spec, self.base)['status'], 'FAIL')

    def test_hash_identity_and_changed_source(self):
        digest = hashlib.sha256(self.csv.read_bytes()).hexdigest()
        self.spec['datasets']['d']['sha256'] = digest
        report = self.aggregate()
        self.assertEqual(report['status'], 'PASS')
        self.assertEqual(report['datasets']['d']['sha256'], digest)
        self.csv.write_text('y\n20\n', encoding='utf-8')
        self.assertEqual(self.aggregate()['status'], 'FAIL')

    def test_bad_hash_and_paths_fail(self):
        for path in ['../data.csv', str(self.csv.resolve())]:
            self.spec['datasets']['d']['path'] = path
            self.assertEqual(self.aggregate()['status'], 'FAIL')
        self.spec['datasets']['d'] = {'path': 'data.csv', 'sha256': 'wrong'}
        self.assertEqual(self.aggregate()['status'], 'FAIL')

    def test_ambiguous_csv_structure_fails(self):
        for contents in ['y,y\n1,2\n', 'y,pred\n1\n', 'y\n1,2\n', 'y\n', ',y\na,1\n']:
            self.csv.write_text(contents, encoding='utf-8')
            self.assertEqual(self.aggregate()['status'], 'FAIL')

    def test_boolean_unknown_schema_and_wrong_types_fail(self):
        self.assertEqual(self.aggregate(reported=True)['status'], 'FAIL')
        self.aggregate()
        for value in [True, 2, '1']:
            spec = copy.deepcopy(self.spec)
            spec['schema_version'] = value
            self.assertEqual(audit(spec, self.base)['status'], 'FAIL')
        for value in [None, [], {'schema_version': 1}]:
            self.assertEqual(audit(value, self.base)['status'], 'FAIL')

    def cli(self, contents):
        spec = self.base / 'checks.json'
        spec.write_text(contents, encoding='utf-8')
        return subprocess.run([sys.executable, '-X', 'utf8', str(Path(__file__).with_name('audit_numeric_consistency.py')), str(spec)], capture_output=True, text=True)

    def test_cli_rejects_duplicate_json_and_nonfinite_constants(self):
        for contents in ['{"schema_version":1,"schema_version":1}', '{"value":NaN}', 'not-json']:
            result = self.cli(contents)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(json.loads(result.stdout)['status'], 'FAIL')

    def test_cli_status_and_input_bytes_are_preserved(self):
        self.aggregate()
        before = self.csv.read_bytes()
        result = self.cli(json.dumps(self.spec))
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(json.loads(result.stdout)['status'], 'PASS')
        self.assertEqual(self.csv.read_bytes(), before)
        self.assertEqual(sorted(p.name for p in self.base.iterdir()), ['checks.json', 'data.csv'])
        self.spec['checks'][0]['reported'] = 999
        self.assertEqual(self.cli(json.dumps(self.spec)).returncode, 1)


if __name__ == '__main__':
    unittest.main()
