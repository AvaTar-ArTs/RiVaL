#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["rich"]
# ///
"""Render a Claude Code session log (plus its subagent logs) as one Markdown transcript.

/export only covers the conversation after the last compaction; the session .jsonl keeps
everything. This reads it read-only and writes a new file; it never overwrites (an existing
output gets -v2, -v3 ...).

Usage:
  ./export-full-transcript.py SESSION.jsonl [-o OUT.md] [--dry-run] [--limit N] [--no-subagents]
"""
import argparse
import json
import sys
import time
from pathlib import Path

try:
    from rich.console import Console
    from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
    from rich.table import Table
    console = Console()
except ImportError:  # plain fallback when run without uv
    console = None

TOOL_RESULT_MAX = 4000  # chars kept per tool result; the full text stays in the .jsonl


def say(msg):
    console.print(msg) if console else print(msg)


def block_text(b, role):
    t = b.get('type')
    if t == 'text':
        return b.get('text', '').strip()
    if t == 'tool_use':
        args = json.dumps(b.get('input', {}), ensure_ascii=False, indent=2)
        return f"**Tool call: `{b.get('name')}`**\n\n```json\n{args}\n```"
    if t == 'tool_result':
        c = b.get('content')
        if isinstance(c, list):
            c = '\n'.join(x.get('text', '') for x in c if isinstance(x, dict) and x.get('type') == 'text')
        c = str(c or '')
        cut = f"\n… [{len(c) - TOOL_RESULT_MAX:,} more chars in the session log]" if len(c) > TOOL_RESULT_MAX else ''
        return f"**Tool result**\n\n```\n{c[:TOOL_RESULT_MAX]}{cut}\n```"
    return ''  # thinking blocks and other internals are left out


def render(path, title, limit=None):
    """Return (markdown, turn_count) for one .jsonl log."""
    out, n = [f"# {title}\n\nSource: `{path}`\n"], 0
    for line in path.open(encoding='utf-8'):
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        role = d.get('type')
        if role not in ('user', 'assistant'):
            continue
        m = d.get('message') or {}
        c = m.get('content')
        parts = [c.strip()] if isinstance(c, str) else [block_text(b, role) for b in (c or []) if isinstance(b, dict)]
        parts = [p for p in parts if p]
        if not parts:
            continue
        n += 1
        out.append(f"\n---\n\n## {role} · {d.get('timestamp', '')}\n\n" + '\n\n'.join(parts) + '\n')
        if limit and n >= limit:
            break
    return ''.join(out), n


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
    ap.add_argument('session', type=Path)
    ap.add_argument('-o', '--out', type=Path)
    ap.add_argument('--dry-run', action='store_true', help='show what would be written; write nothing')
    ap.add_argument('--limit', type=int, help='turns per log (trial runs)')
    ap.add_argument('--no-subagents', action='store_true')
    a = ap.parse_args()

    if not a.session.is_file():
        say(f"[red]failed[/red] session log not found: {a.session}" if console else f"failed: not found {a.session}")
        return 1
    logs = [(a.session, 'Main session')]
    sub = a.session.with_suffix('') / 'subagents'
    if not a.no_subagents and sub.is_dir():
        logs += [(p, f"Subagent {p.stem.split('-')[1]}") for p in sorted(sub.glob('agent-*.jsonl'))]
    out = free_path(a.out or a.session.with_name(a.session.stem + '-full-transcript.md'))

    start, sections, rows = time.time(), [], []
    try:
        if console:
            with Progress(SpinnerColumn(), TextColumn('{task.description}'), BarColumn(),
                          TextColumn('[{task.completed}/{task.total}]'), TimeElapsedColumn(),
                          console=console, transient=False) as prog:
                task = prog.add_task('rendering logs', total=len(logs))
                for p, title in logs:
                    md, n = render(p, title, a.limit)
                    sections.append(md); rows.append((title, n, p.stat().st_size))
                    prog.advance(task)
        else:
            for i, (p, title) in enumerate(logs, 1):
                md, n = render(p, title, a.limit)
                sections.append(md); rows.append((title, n, p.stat().st_size))
                print(f"[{i}/{len(logs)}] ok {title}: {n} turns")
    except KeyboardInterrupt:
        say('interrupted: nothing written')
        return 130

    text = '\n\n'.join(sections)
    if console:
        t = Table(title='Full transcript')
        for col in ('log', 'turns', 'source bytes'):
            t.add_column(col)
        for title, n, size in rows:
            t.add_row(title, str(n), f"{size:,}")
        console.print(t)
    else:
        for r in rows:
            print(*r)

    if a.dry_run:
        say(f"dry run: would write {len(text):,} chars to {out}")
        return 0
    part = out.with_name(out.name + '.part')
    part.write_text(text, encoding='utf-8')
    part.rename(out)
    ok = out.stat().st_size == len(text.encode('utf-8'))  # verify: bytes on disk match what was rendered
    say(f"{'ok' if ok else 'failed'}: wrote {out} ({out.stat().st_size:,} bytes, size check {'passed' if ok else 'FAILED'}) in {time.time() - start:.1f}s")
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
