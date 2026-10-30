#!/usr/bin/env python3
"""Render each Arcana-*.html beside it as a 3000x3000 PNG with headless Chrome. Skips PNGs that exist.

Usage: python3 -I render.py
"""
import struct
import subprocess
from pathlib import Path

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
HERE = Path(__file__).resolve().parent
PROFILE = HERE.parent / '.tmp' / 'chrome'  # scratch profile inside the project, gitignored

PROFILE.mkdir(parents=True, exist_ok=True)
pages = sorted(HERE.glob('Arcana-*.html'))
for i, html in enumerate(pages, 1):
    png = html.with_name(html.stem + '-3000.png')
    if png.exists():
        print(f'[{i}/{len(pages)}] skipped (exists) {png.name}')
        continue
    r = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--user-data-dir={PROFILE}',
                        '--window-size=1080,1080', '--force-device-scale-factor=2.7777778', '--virtual-time-budget=8000',
                        f'--screenshot={png}', html.as_uri()], capture_output=True)
    size = struct.unpack('>II', png.read_bytes()[16:24]) if png.exists() else None
    ok = r.returncode == 0 and size == (3000, 3000)  # verify: exit status and pixel size
    print(f"[{i}/{len(pages)}] {'ok' if ok else 'failed'} {png.name} {size}")
