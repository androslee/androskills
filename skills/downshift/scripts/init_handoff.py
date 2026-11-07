#!/usr/bin/env python3
"""Create a portable, draft Downshift packet. No network, models or overwrites."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

TEMPLATES = Path(__file__).resolve().parents[1] / 'assets' / 'packet'


def initialize(destination: Path, mode: str) -> list[Path]:
    if mode not in {'files', 'direct'}:
        raise ValueError('mode must be files or direct')
    # Read all bundled inputs before creating anything, so missing templates do
    # not leave an apparently complete packet. Never resolve user content as code.
    templates = sorted(p for p in TEMPLATES.rglob('*') if p.is_file())
    if not templates:
        raise FileNotFoundError(f'Packet templates missing: {TEMPLATES}')
    prepared = [(p.relative_to(TEMPLATES), p.read_text(encoding='utf-8').replace('{{MODE}}', mode)) for p in templates]
    # Reject even existing empty directories/symlinks: resuming a packet is an
    # edit, not reinitialization. mkdir also protects against a concurrent creator.
    destination.mkdir(parents=True, exist_ok=False)
    written = []
    for relative, content in prepared:
        path = destination / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('x', encoding='utf-8') as output:
            output.write(content)
        written.append(path)
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path, help='New packet directory; must not already exist')
    parser.add_argument('--mode', choices=['files', 'direct'], default='files')
    args = parser.parse_args(argv)
    try:
        paths = initialize(args.destination, args.mode)
    except (OSError, ValueError) as error:
        print(f'Cannot initialize handoff: {error}', file=sys.stderr)
        print('No existing files are replaced. If creation was interrupted, inspect the partial new directory before retrying.', file=sys.stderr)
        return 1
    print(f'Created {len(paths)} draft files at {args.destination} (mode: {args.mode}).')
    print('Complete the contract and ready cards before giving this packet to a worker. No model was invoked.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
