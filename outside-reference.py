#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["rich"]
# ///
"""Reference, without copying, the parts of a checkout that git does not hold.

Reads ROOT read-only and writes a manifest of every file there: relative path, bytes, mtime,
SHA-256, and whether this branch tracks it. Untracked files stay where they are; the manifest
is the outside reference to them. Never overwrites: an existing output gets -v2, -v3 ...

Usage:
  ./outside-reference.py ROOT [-o reference/outside-manifest.json] [--dry-run] [--limit N]
"""
import argparse
import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from rich.console import Console
    from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
    from rich.table import Table
    console = Console()
except ImportError:  # plain fallback when run without uv
    console = None

SKIP_DIRS = {'.git', '.claude', '.tmp', '__pycache__'}  # VCS, worktrees, scratch, caches


def say(msg):
    console.print(msg) if console else print(msg)


def sha256(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def free_path(p):
    """Never overwrite: return p, or p-v2, p-v3 ... that does not exist yet."""
    if not p.exists():
        return p
    v = 2
    while (q := p.with_name(f"{p.stem}-v{v}{p.suffix}")).exists():
        v += 1
    return q


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('root', type=Path)
    ap.add_argument('-o', '--out', type=Path, default=Path('reference/outside-manifest.json'))
    ap.add_argument('--dry-run', action='store_true', help='list counts; write nothing')
    ap.add_argument('--limit', type=int, help='files to hash (trial runs)')
    a = ap.parse_args()

    root = a.root.resolve()
    if not root.is_dir():
        say(f"failed: not a directory: {root}")
        return 1
    tracked = set(subprocess.run(['git', 'ls-files'], capture_output=True, text=True, check=True).stdout.splitlines())
    files = sorted(p for p in root.rglob('*') if p.is_file() and not SKIP_DIRS & set(p.relative_to(root).parts))
    if a.limit:
        files = files[:a.limit]

    start, rows, failed = time.time(), [], 0
    try:
        if console:
            with Progress(SpinnerColumn(), TextColumn('{task.description}'), BarColumn(),
                          TextColumn('[{task.completed}/{task.total}]'), TimeElapsedColumn(), console=console) as prog:
                task = prog.add_task('hashing', total=len(files))
                for p in files:
                    try:
                        rows.append(entry(p, root, tracked))
                    except OSError as e:
                        failed += 1
                        say(f"[red]failed[/red] {p.relative_to(root)}: {e}")
                    prog.advance(task)
        else:
            for i, p in enumerate(files, 1):
                try:
                    rows.append(entry(p, root, tracked))
                except OSError as e:
                    failed += 1
                    print(f"failed {p.relative_to(root)}: {e}")
                print(f"[{i}/{len(files)}] {p.relative_to(root)}")
    except KeyboardInterrupt:
        say('interrupted: nothing written')
        return 130

    groups = {}
    for r in rows:
        top = r['path'].split('/')[0] if '/' in r['path'] else '(root files)'
        g = groups.setdefault(top, {'files': 0, 'bytes': 0, 'tracked': 0})
        g['files'] += 1; g['bytes'] += r['bytes']; g['tracked'] += r['tracked']
    if console:
        t = Table(title=f'Outside reference · {root.name}')
        for col in ('group', 'files', 'bytes', 'tracked here'):
            t.add_column(col)
        for k, g in sorted(groups.items()):
            t.add_row(k, str(g['files']), f"{g['bytes']:,}", str(g['tracked']))
        console.print(t)
    say(f"{len(rows)} ok, {failed} failed, {sum(r['bytes'] for r in rows):,} bytes, {time.time() - start:.1f}s")

    if a.dry_run:
        say(f"dry run: would write {a.out}")
        return 1 if failed else 0
    doc = {'root': root.name, 'generated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
           'skipped_dirs': sorted(SKIP_DIRS), 'groups': groups, 'files': rows}
    out = free_path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    part = out.with_name(out.name + '.part')
    part.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    part.rename(out)
    ok = json.loads(out.read_text(encoding='utf-8'))['files'] == rows  # verify: written manifest reads back identical
    say(f"{'ok' if ok else 'failed'}: wrote {out} (read-back check {'passed' if ok else 'FAILED'})")
    return 0 if ok and not failed else 1


def entry(p, root, tracked):
    rel = p.relative_to(root).as_posix()
    st = p.stat()
    return {'path': rel, 'bytes': st.st_size,
            'mtime': datetime.fromtimestamp(st.st_mtime, timezone.utc).isoformat(timespec='seconds'),
            'sha256': sha256(p), 'tracked': rel in tracked}


if __name__ == '__main__':
    sys.exit(main())
