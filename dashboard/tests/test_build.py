"""Production state regressions: different workflows and delivery scopes."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('dashboard_build', Path(__file__).parents[1] / 'src/build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads(build.read(build.ROOT / 'dashboard/clips.json'))

    def rows(self, entries, batches=None):
        data = copy.deepcopy(self.manifest)
        by_key = {(e['파트'], e['클립']): e for e in data['클립']}
        for key, values in entries.items():
            by_key[key].update(values)
        if batches is not None:
            data['납품차수'] = batches
        original = build.read
        with patch.object(build, 'read', side_effect=lambda p: json.dumps(data) if p == build.ROOT / 'dashboard/clips.json' else original(p)):
            rows, warnings, nearest = build.build_rows()
        self.assertFalse(warnings)
        return {(r['파트번호'], r['클립']): r for r in rows}, nearest

    def test_practice_material_done_schedules_recording_without_script(self):
        rows, _ = self.rows({(3, 'Ch02-01'): {'실습자료': '완료', '촬영': '시작전'}})
        r = rows[(3, 'Ch02-01')]
        self.assertEqual((r['제작'], r['대본'], r['촬영']), ('완료', '해당없음', '예정'))

    def test_recorded_does_not_imply_material_done(self):
        rows, _ = self.rows({(3, 'Ch02-01'): {'실습자료': '시작전', '촬영': '완료'}})
        self.assertEqual(rows[(3, 'Ch02-01')]['제작'], '시작전')
        self.assertEqual(rows[(3, 'Ch02-01')]['촬영'], '완료')

    def test_active_recording_not_overwritten_by_material_preparation(self):
        rows, _ = self.rows({(3, 'Ch02-01'): {'실습자료': '작업중', '촬영': '작업중'}})
        self.assertEqual(rows[(3, 'Ch02-01')]['제작'], '작업중')
        self.assertEqual(rows[(3, 'Ch02-01')]['촬영'], '작업중')

    def test_all_clips_have_correct_delivery(self):
        rows, _ = self.rows({})
        self.assertEqual(len(rows), 72)
        for (part, _), r in rows.items():
            self.assertEqual(r['차수'], 1 if part <= 4 else 2 if part <= 7 else 3)
        self.assertEqual(len(build.stage_scope(list(rows.values()), '제작')), 72)
        self.assertEqual(len(build.stage_scope(list(rows.values()), '대본')), 30)

    def test_earliest_unfinished_delivery_stays_current(self):
        batches = copy.deepcopy(self.manifest['납품차수'])
        for b in batches:
            b['납기'] = f"2026-{9 + b['차수']:02}-15"
        rows, nearest = self.rows({}, batches)
        self.assertEqual(nearest, '2026-10-15')
        self.assertEqual(rows[(5, 'Ch01-01')]['제작'], '시작전')

    def test_duplicate_part_assignment_rejected(self):
        with self.assertRaises(SystemExit):
            build.delivery_config({'납품차수': [{'차수': 1, '파트': [1]}, {'차수': 2, '파트': [1]}]})

    def test_invalid_calendar_date_rejected(self):
        with self.assertRaises(SystemExit):
            build.delivery_config({'납품차수': [{'차수': 1, '파트': [1], '납기': '2026-02-30'}]})

    def test_optional_material_is_excluded_from_production_scope(self):
        rows, _ = self.rows({(3, 'Ch02-01'): {'실습자료': '해당없음', '촬영': '작업중'}})
        r = rows[(3, 'Ch02-01')]
        self.assertEqual((r['제작'], r['대본'], r['촬영']), ('해당없음', '해당없음', '작업중'))
        self.assertEqual(len(build.stage_scope(list(rows.values()), '제작')), 71)
        self.assertEqual(len(build.stage_scope(list(rows.values()), '촬영')), 72)

    def test_completed_recording_cannot_hold_up_next_delivery(self):
        by_part = {
            1: [{'촬영': '완료', '제작': '시작전', '대본': '해당없음'}],
            2: [{'촬영': '작업중', '제작': '완료', '대본': '완료'}],
        }
        parts, deadline = build.due_parts({'1': '2026-09-01', '2': '2026-10-01'}, by_part)
        self.assertEqual((parts, deadline), ({2}, '2026-10-01'))

    def test_completed_theory_is_preserved(self):
        rows, _ = self.rows({})
        r = rows[(4, 'Ch01-01')]
        self.assertEqual((r['제작'], r['대본'], r['촬영']), ('완료', '완료', '완료'))


if __name__ == '__main__':
    unittest.main()
