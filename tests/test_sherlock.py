import contextlib
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/sherlock/scripts/sherlock.py'
spec = importlib.util.spec_from_file_location('sherlock', SCRIPT)
sherlock = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sherlock)


def skill(root, folder, header, body='Instructions are not inventory metadata.'):
    location = root / folder
    location.mkdir(parents=True)
    (location / 'SKILL.md').write_text('---\n' + header + '\n---\n' + body, encoding='utf-8')
    return location


class SkillTests(unittest.TestCase):
    def test_rank_local_metadata_and_abstain(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill(root, 'pdf', 'name: pdf\ndescription: Read PDF documents and extract pages')
            skill(root, 'dog', 'name: pets\ndescription: Handle animated virtual pets', 'PDF PDF PDF')
            skill(root, 'self', 'name: sherlock\ndescription: Find PDF skills')
            items = sherlock.inventory([root])
            result = sherlock.rank('extract PDF pages', items, 10)
            self.assertEqual([x['name'] for x in result], ['pdf'])
            self.assertEqual(sherlock.rank('zzzxxyy', items, 10), [])

    def test_skips_malformed_disabled_and_large_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill(root, 'disabled', 'name: disabled\ndescription: test\ndisable-model-invocation: true # disabled')
            explicit = skill(root, 'explicit', 'name: explicit\ndescription: test')
            (explicit / 'agents').mkdir()
            (explicit / 'agents' / 'openai.yaml').write_text('policy:\n  allow_implicit_invocation: false\n')
            skill(root, 'block', 'name: block\ndescription: >-\n  Handles diagrams\n  and SVG rendering')
            skill(root, 'large', 'name: large\ndescription: test', 'x' * (128 * 1024))
            skill(root, 'bad', 'name: bad\ndescription: "unclosed')
            found = sherlock.inventory([root, root])
            self.assertEqual([x['name'] for x in found], ['block'])
            self.assertEqual(found[0]['description'], 'Handles diagrams and SVG rendering')

    def test_system_subdirectory_and_missing_roots(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill(root, '.system/creator', 'name: creator\ndescription: Create skills')
            self.assertEqual([x['name'] for x in sherlock.inventory([root / 'missing', root])], ['creator'])

    def test_external_search_is_bounded_and_filters_untrusted_ids(self):
        seen = []
        payload = {'skills': [
            {'id': 'owner/repo/pdf', 'name': 'pdf', 'source': 'owner/repo', 'installs': 100},
            {'id': '../../evil', 'name': 'bad', 'source': 'bad', 'installs': 4},
            {'id': 'x/y/z', 'name': 'bad', 'source': 'x/y', 'installs': 'fake'},
        ]}
        class Response(io.BytesIO):
            pass
        def open_fake(request, timeout):
            seen.append((request.full_url, timeout))
            return Response(json.dumps(payload).encode())
        result = sherlock.search('pdf documents', 10, open_fake)
        self.assertEqual([r['id'] for r in result], ['owner/repo/pdf'])
        self.assertEqual(parse_qs(urlparse(seen[0][0]).query), {'q': ['pdf documents']})
        self.assertEqual(result[0]['url'], 'https://skills.sh/owner/repo/pdf')
        with self.assertRaises(ValueError): sherlock.search('x\nsecret', 10, open_fake)
        self.assertEqual(len(seen), 1)

    def test_cli_offline_and_root_override(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill(root, 'render', 'name: renderer\ndescription: Render SVG graphics')
            run = subprocess.run([sys.executable, str(SCRIPT), 'rank', 'SVG render', '--root', str(root)], text=True, capture_output=True, check=True)
            self.assertEqual(json.loads(run.stdout)['results'][0]['name'], 'renderer')
            self.assertNotIn('skills.sh/api', run.stdout)


if __name__ == '__main__': unittest.main()
