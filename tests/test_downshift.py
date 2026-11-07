"""Downshift packet creation invariants; no models, credentials or network."""
import csv
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/downshift/scripts/init_handoff.py'
spec = importlib.util.spec_from_file_location('downshift_init', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class HandoffTests(unittest.TestCase):
    def test_both_modes_produce_portable_draft_packets(self):
        with tempfile.TemporaryDirectory() as temp:
            for mode in ('files', 'direct'):
                target = Path(temp) / mode / 'project with spaces' / '.downshift'
                written = module.initialize(target, mode)
                self.assertEqual(len(written), 7)
                self.assertTrue(all(p.is_relative_to(target) for p in written))
                self.assertTrue((target / 'tasks/T001.md').is_file())
                self.assertIn(f'Mode: {mode}', (target / 'START_HERE.md').read_text())
                self.assertIn('State: Draft', (target / 'tasks/T001.md').read_text())
                with (target / 'COSTS.csv').open(newline='') as stream:
                    ledger = list(csv.reader(stream))
                self.assertEqual(len(ledger), 1)  # No invented cost measurements.
                self.assertEqual(len(ledger[0]), len(set(ledger[0])))

    def test_existing_packet_and_empty_destination_are_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / 'existing'
            module.initialize(target, 'files')
            (target / 'tasks/T001.md').write_text('Actual worker progress, do not lose.')
            before = {p.relative_to(target): p.read_bytes() for p in target.rglob('*') if p.is_file()}
            with self.assertRaises(FileExistsError):
                module.initialize(target, 'direct')
            after = {p.relative_to(target): p.read_bytes() for p in target.rglob('*') if p.is_file()}
            self.assertEqual(before, after)
            empty = Path(temp) / 'empty'
            empty.mkdir()
            with self.assertRaises(FileExistsError):
                module.initialize(empty, 'files')
            self.assertEqual(list(empty.iterdir()), [])

    def test_invalid_mode_and_symlink_do_not_touch_other_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with self.assertRaises(ValueError):
                module.initialize(root / 'invalid', 'automatic')
            self.assertFalse((root / 'invalid').exists())
            elsewhere = root / 'elsewhere'
            elsewhere.mkdir()
            marker = elsewhere / 'user-file'
            marker.write_text('preserve')
            link = root / 'link'
            link.symlink_to(elsewhere, target_is_directory=True)
            with self.assertRaises(FileExistsError):
                module.initialize(link, 'files')
            self.assertEqual(marker.read_text(), 'preserve')
            self.assertEqual(len(list(elsewhere.iterdir())), 1)

    def test_cli_failure_has_nonzero_status_and_never_reinitializes(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / 'packet'
            args = [sys.executable, str(SCRIPT), str(target), '--mode', 'direct']
            first = subprocess.run(args, text=True, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            second = subprocess.run(args, text=True, capture_output=True)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual((target / 'START_HERE.md').read_text().count('Mode: direct'), 1)


if __name__ == '__main__':
    unittest.main()
