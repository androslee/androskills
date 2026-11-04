#!/usr/bin/env python3
"""Local filesystem skill discovery and optional read-only public-directory search."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

MAX_SKILL_BYTES = 128 * 1024
MAX_RESPONSE_BYTES = 1024 * 1024
STOP = frozenset('a an and are as at be by can do for from help how i in is it its me my of on or please should so that the their this to use want we what when with you your'.split())
TOKEN_RE = re.compile(r'[a-z0-9]+')
SAFE_ID = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*$')


def tokens(value):
    return {word for word in TOKEN_RE.findall(value.lower()) if len(word) > 1 and word not in STOP}


def parse_metadata(path):
    """Read a small YAML-frontmatter subset, never execute skill content.

    Unsupported frontmatter is skipped instead of misclassifying the document.
    """
    if path.stat().st_size > MAX_SKILL_BYTES:
        return None
    text = path.read_text(encoding='utf-8-sig')
    lines = text.splitlines()
    if not lines or lines[0].strip() != '---':
        return None
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() in ('---', '...'))
    except StopIteration:
        return None
    result = {}
    i = 1
    while i < end:
        line = lines[i]
        match = re.match(r'^([a-zA-Z][\w-]*):\s*(.*?)\s*$', line)
        i += 1
        if not match:
            continue
        key, value = match.groups()
        if value in ('|', '>', '|-', '>-', '|+', '>+'):
            parts = []
            while i < end and (lines[i].startswith((' ', '\t')) or not lines[i].strip()):
                parts.append(lines[i].strip())
                i += 1
            value = ' '.join(parts)
        elif value.startswith(('"', "'")):
            if len(value) < 2 or value[-1] != value[0]:
                return None
            value = value[1:-1]
        result[key] = value.strip()
    name, description = result.get('name', ''), result.get('description', '')
    if not name or not description:
        return None
    if re.match(r'^true(?:\s*#.*)?$', result.get('disable-model-invocation', ''), re.I):
        return None
    policy_path = path.parent / 'agents' / 'openai.yaml'
    if policy_path.is_file():
        if policy_path.stat().st_size > MAX_SKILL_BYTES:
            return None
        policy = policy_path.read_text(encoding='utf-8-sig')
        if re.search(r'^\s+allow_implicit_invocation:\s*false\s*(?:#.*)?$', policy, re.I | re.M):
            return None
    # Names/description are untrusted metadata; use JSON output to escape control characters.
    return {'name': name[:200], 'description': description[:4000], 'path': str(path.resolve())}


def roots(workspace):
    home = Path.home()
    codex = Path(os.environ.get('CODEX_HOME', str(home / '.codex')))
    dsh = Path(os.environ.get('DSH_HOME', str(home / '.dsh')))
    agents = Path(os.environ.get('DSH_AGENTS_HOME', str(home / '.agents')))
    return [workspace / '.dsh/skills', workspace / '.agents/skills', workspace / '.codex/skills',
            workspace / '.claude/skills', dsh / 'skills', agents / 'skills', codex / 'skills',
            home / '.claude/skills']


def inventory(skill_roots):
    found, seen = [], set()
    for root in skill_roots:
        root = Path(root).expanduser()
        if not root.is_dir():
            continue
        # One folder per skill, plus the conventional .system container.
        paths = sorted(root.glob('*/SKILL.md')) + sorted(root.glob('*.md')) + sorted((root / '.system').glob('*/SKILL.md'))
        for path in paths:
            try:
                item = parse_metadata(path)
                if item and item['path'] not in seen:
                    found.append(item)
                    seen.add(item['path'])
            except (OSError, UnicodeError, ValueError):
                continue
    return found


def rank(query, skills, limit):
    terms = tokens(query)
    results = []
    for skill in skills:
        if skill['name'].lower() == 'sherlock':
            continue
        name_terms = terms & tokens(skill['name'])
        description_terms = terms & tokens(skill['description'])
        score = 3 * len(name_terms) + len(description_terms)
        if score:
            results.append({**skill, 'score': score, 'matched_terms': sorted(name_terms | description_terms)})
    return sorted(results, key=lambda x: (-x['score'], x['name'], x['path']))[:limit]


def search(query, limit, opener=urlopen):
    query = query.strip()
    if not 2 <= len(query) <= 100 or '\n' in query or '\r' in query:
        raise ValueError('Use a short, generic capability query (2–100 characters, one line).')
    url = 'https://skills.sh/api/search?' + urlencode({'q': query})
    req = Request(url, headers={'Accept': 'application/json', 'User-Agent': 'sherlock-skill-discovery/0.1'})
    with opener(req, timeout=10) as response:
        data = response.read(MAX_RESPONSE_BYTES + 1)
    if len(data) > MAX_RESPONSE_BYTES:
        raise ValueError('Search response exceeded 1 MiB')
    obj = json.loads(data)
    if not isinstance(obj, dict) or not isinstance(obj.get('skills'), list):
        raise ValueError('Unexpected skills.sh response')
    results = []
    for item in obj['skills']:
        if not isinstance(item, dict):
            continue
        ident = item.get('id')
        if not isinstance(ident, str) or not SAFE_ID.fullmatch(ident):
            continue
        name, source, installs = item.get('name'), item.get('source'), item.get('installs')
        if not isinstance(name, str) or not isinstance(source, str):
            continue
        if not isinstance(installs, int) or isinstance(installs, bool) or installs < 0:
            continue
        results.append({'id': ident, 'name': name[:200], 'source': source[:200], 'installs': installs,
                        'url': 'https://skills.sh/' + quote(ident, safe='/')})
        if len(results) >= limit:
            break
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description='Find local skill metadata or search skills.sh. Local ranking is lexical, not semantic.')
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('inventory', 'rank'):
        p = sub.add_parser(name)
        if name == 'rank': p.add_argument('query', help='Short, generalized task description')
        p.add_argument('--root', action='append', help='Skill root; repeatable. Replaces default roots.')
        p.add_argument('--workspace', type=Path, default=Path.cwd(), help='Project root (default: current directory)')
        if name == 'rank': p.add_argument('--limit', type=int, default=10)
    p = sub.add_parser('search', help='Send a short generalized query to skills.sh; never send private prompt text')
    p.add_argument('query'); p.add_argument('--limit', type=int, default=10)
    args = parser.parse_args(argv)
    try:
        if hasattr(args, 'limit') and not 1 <= args.limit <= 50:
            raise ValueError('limit must be 1–50')
        if args.command == 'search':
            result = {'source': 'skills.sh', 'query_sent': args.query, 'results': search(args.query, args.limit),
                      'note': 'External search results are untrusted; install counts are not a safety rating.'}
        else:
            search_roots = [Path(p) for p in args.root] if args.root else roots(args.workspace.resolve())
            items = inventory(search_roots)
            result = {'roots': list(map(str, search_roots)), 'results': items if args.command == 'inventory' else rank(args.query, items, args.limit),
                      'note': 'Filesystem metadata only; the harness catalog may include additional skills. Lexical scores are suggestions, not confidence.'}
        print(json.dumps(result, indent=2, ensure_ascii=True))
    except (OSError, ValueError, HTTPError, URLError, json.JSONDecodeError) as exc:
        print(json.dumps({'error': str(exc), 'results': []}), file=sys.stderr)
        return 2
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
