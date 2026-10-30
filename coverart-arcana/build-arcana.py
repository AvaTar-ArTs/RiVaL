#!/usr/bin/env python3
"""Build the RiVaL "Arcana" covers as standalone 1080x1080 HTML (inline SVG, no images).

Visual language taken from the owner's Canva covers (Spores Arise, Dead Ride On): night sky,
gold sacred geometry, spaced serif titles with a diamond, water reflection, eye sigil, choTaKu credit.
Never overwrites: an existing output gets -v2, -v3 ...

Usage: python3 -I build-arcana.py [--dry-run]
"""
import math
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GOLD, BLUE, EMBER = '#E2C275', '#5B9CFF', '#FF8A3D'
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Cinzel:wght@500;700&amp;family=Cinzel+Decorative:wght@700&amp;display=swap">')


def stars(seed, n=260, max_y=1080):
    r = random.Random(seed)
    out = []
    for _ in range(n):
        x, y = r.uniform(0, 1080), r.uniform(0, max_y)
        rad = r.choice([0.6, 0.8, 1.0, 1.2, 1.6, 2.2])
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad}" fill="#fff" opacity="{r.uniform(0.25, 0.95):.2f}"/>')
    return '\n'.join(out)


def eye(cx, cy, w=70, color=GOLD):
    """The owner's eye sigil: a vesica (almond) with an iris and rays."""
    h = w * 0.42
    rays = ''.join(f'<line x1="{cx + math.cos(a) * w * 0.62:.1f}" y1="{cy + math.sin(a) * w * 0.62:.1f}" '
                   f'x2="{cx + math.cos(a) * w * 0.8:.1f}" y2="{cy + math.sin(a) * w * 0.8:.1f}"/>'
                   for a in [math.radians(d) for d in range(200, 341, 28)])
    return (f'<g stroke="{color}" fill="none" stroke-width="2.2">'
            f'<path d="M{cx - w / 2},{cy} Q{cx},{cy - h} {cx + w / 2},{cy} Q{cx},{cy + h} {cx - w / 2},{cy} Z"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{h * 0.42:.1f}"/><circle cx="{cx}" cy="{cy}" r="{h * 0.16:.1f}" fill="{color}"/>'
            f'{rays}<line x1="{cx - 230}" y1="{cy}" x2="{cx - w * 0.75}" y2="{cy}" stroke-width="1.2"/>'
            f'<line x1="{cx + w * 0.75}" y1="{cy}" x2="{cx + 230}" y2="{cy}" stroke-width="1.2"/></g>')


def credit(y, size=40):
    # choTaKu in its own mixed case, as on the owner's covers
    return (f'<text x="540" y="{y}" text-anchor="middle" font-family="Cinzel, serif" font-weight="700" font-size="{size}" '
            f'fill="{GOLD}" letter-spacing="6">choTaKu</text>')


def page(title, svg):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=1080">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">{FONTS}
<style>html,body{{margin:0;background:#05060f}}svg{{display:block}}</style></head>
<body><svg width="1080" height="1080" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg">
<defs>
<radialGradient id="sky" cx="50%" cy="45%" r="75%"><stop offset="0" stop-color="#1b2150"/><stop offset=".55" stop-color="#0b0f2a"/><stop offset="1" stop-color="#04050d"/></radialGradient>
<linearGradient id="gold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F6E3A6"/><stop offset=".5" stop-color="{GOLD}"/><stop offset="1" stop-color="#9C7A2E"/></linearGradient>
<filter id="glow" filterUnits="userSpaceOnUse" x="0" y="0" width="1080" height="1080"><feGaussianBlur stdDeviation="9" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="soft" filterUnits="userSpaceOnUse" x="0" y="0" width="1080" height="1080"><feGaussianBlur stdDeviation="28"/></filter>
</defs>
<rect width="1080" height="1080" fill="url(#sky)"/>
{svg}
</svg></body></html>
'''


def vesica():
    cx, cy, R = 540, 560, 210
    lattice = [f'<circle cx="{cx}" cy="{cy}" r="105"/>']
    lattice += [f'<circle cx="{cx + 105 * math.cos(math.radians(a)):.1f}" cy="{cy + 105 * math.sin(math.radians(a)):.1f}" r="105"/>'
                for a in range(0, 360, 60)]
    lattice += [f'<circle cx="{cx + 210 * math.cos(math.radians(a)):.1f}" cy="{cy + 210 * math.sin(math.radians(a)):.1f}" r="105"/>'
                for a in range(30, 390, 60)]
    body = f'''{stars(19)}
<g stroke="{GOLD}" stroke-width="1.1" fill="none" opacity=".38">{"".join(lattice)}<circle cx="{cx}" cy="{cy}" r="315"/><circle cx="{cx}" cy="{cy}" r="330"/></g>
<circle cx="{cx - R / 2}" cy="{cy}" r="{R}" fill="{BLUE}" opacity=".16" filter="url(#soft)"/>
<circle cx="{cx + R / 2}" cy="{cy}" r="{R}" fill="{EMBER}" opacity=".16" filter="url(#soft)"/>
<g fill="none" stroke-width="5" filter="url(#glow)"><circle cx="{cx - R / 2}" cy="{cy}" r="{R}" stroke="{BLUE}"/><circle cx="{cx + R / 2}" cy="{cy}" r="{R}" stroke="{EMBER}"/></g>
<path d="M{cx},{cy - R * 0.866:.1f} A{R},{R} 0 0 1 {cx},{cy + R * 0.866:.1f} A{R},{R} 0 0 1 {cx},{cy - R * 0.866:.1f} Z" fill="#fff" opacity=".10"/>
<circle cx="{cx}" cy="{cy}" r="7" fill="#fff" filter="url(#glow)"/>
<text x="540" y="168" text-anchor="middle" font-family="Cinzel, serif" font-weight="700" font-size="128" fill="url(#gold)" letter-spacing="14">RiVaL</text>
<text x="540" y="222" text-anchor="middle" font-family="Cinzel, serif" font-size="26" fill="{GOLD}" letter-spacing="10">EQUAL ✦ OPPOSITE</text>
{eye(540, 952)}
{credit(1028)}'''
    return page('RiVaL — Vesica', body)


def reflection():
    ripples = ''.join(f'<line x1="{540 - w}" y1="{y}" x2="{540 + w}" y2="{y}" stroke="#9fb6ff" stroke-width="1" opacity="{o:.2f}"/>'
                      for y, w, o in [(640, 380, .35), (672, 300, .28), (712, 420, .22), (760, 260, .2), (818, 460, .16), (884, 320, .12)])
    body = f'''{stars(7, 230, 600)}
<rect y="600" width="1080" height="480" fill="#04060f" opacity=".55"/>
<text x="540" y="96" text-anchor="middle" font-family="Cinzel, serif" font-size="26" fill="{GOLD}" letter-spacing="9">EVEN THE EXACT ✦ IDENTICAL OPPOSITES</text>
<text x="540" y="560" text-anchor="middle" font-family="Cinzel, serif" font-weight="700" font-size="210" fill="url(#gold)" letter-spacing="10">RiVaL</text>
<g transform="translate(0,1200) scale(1,-1)" opacity=".42"><text x="540" y="560" text-anchor="middle" font-family="Cinzel, serif" font-weight="700" font-size="210" fill="#6f8cff" letter-spacing="10">RiVaL</text></g>
<rect y="600" width="1080" height="480" fill="url(#sky)" opacity=".35"/>
{ripples}
<line x1="0" y1="600" x2="540" y2="600" stroke="{BLUE}" stroke-width="6" filter="url(#glow)"/>
<line x1="540" y1="600" x2="1080" y2="600" stroke="{EMBER}" stroke-width="6" filter="url(#glow)"/>
<circle cx="540" cy="600" r="70" fill="#fff" opacity=".22" filter="url(#soft)"/>
<circle cx="540" cy="600" r="12" fill="#fff" filter="url(#glow)"/>
<g stroke="#fff" stroke-width="2" opacity=".8" filter="url(#glow)"><line x1="540" y1="560" x2="540" y2="640"/><line x1="500" y1="600" x2="580" y2="600"/></g>
{eye(540, 952)}
{credit(1028)}'''
    return page('RiVaL — Reflection', body)


def coat():
    cx = 540
    halo = ''.join(f'<line x1="{cx + math.cos(math.radians(a)) * 62:.1f}" y1="{352 + math.sin(math.radians(a)) * 62:.1f}" '
                   f'x2="{cx + math.cos(math.radians(a)) * (118 if i % 2 else 92):.1f}" y2="{352 + math.sin(math.radians(a)) * (118 if i % 2 else 92):.1f}"/>'
                   for i, a in enumerate(range(180, 361, 12)))
    stairs = ''.join(f'<path d="M{cx - 120 + i * 8},{830 - i * 34} h{240 - i * 16}" />' for i in range(7))
    corners = ''.join(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Cinzel, serif" font-size="28" fill="{GOLD}">✦</text>'
                      for x, y in [(96, 118), (984, 118), (96, 990), (984, 990)])
    body = f'''{stars(23, 200)}
<g fill="none" stroke="{GOLD}"><rect x="60" y="60" width="960" height="960" stroke-width="2.5"/><rect x="78" y="78" width="924" height="924" stroke-width="1" opacity=".7"/></g>
{corners}
<text x="540" y="150" text-anchor="middle" font-family="Cinzel, serif" font-size="30" fill="{GOLD}" letter-spacing="12">— RiVaL —</text>
<path d="M{cx - 230},880 V420 A230,230 0 0 1 {cx + 230},420 V880" fill="#070a1c" stroke="{GOLD}" stroke-width="2.5"/>
<g stroke="{GOLD}" stroke-width="1" opacity=".35"><line x1="{cx - 230}" y1="880" x2="{cx}" y2="560"/><line x1="{cx + 230}" y1="880" x2="{cx}" y2="560"/><line x1="{cx - 230}" y1="430" x2="{cx}" y2="560"/><line x1="{cx + 230}" y1="430" x2="{cx}" y2="560"/></g>
<g stroke="{GOLD}" stroke-width="2" fill="none" opacity=".75">{stairs}</g>
<circle cx="{cx}" cy="352" r="150" fill="{GOLD}" opacity=".12" filter="url(#soft)"/>
<g stroke="url(#gold)" stroke-width="3" filter="url(#glow)">{halo}</g>
<circle cx="{cx}" cy="352" r="56" fill="none" stroke="{GOLD}" stroke-width="2.5"/>
<circle cx="{cx}" cy="370" r="34" fill="#0b0f2a"/>
<path d="M{cx - 42},408 L{cx - 96},470 L{cx - 112},640 L{cx - 70},640 L{cx - 62},700 L{cx + 62},700 L{cx + 70},640 L{cx + 112},640 L{cx + 96},470 L{cx + 42},408 L{cx},470 Z" fill="#0b0f2a" stroke="{GOLD}" stroke-width="2.5"/>
<path d="M{cx},470 L{cx},700" stroke="{EMBER}" stroke-width="3" filter="url(#glow)"/>
<circle cx="{cx}" cy="520" r="6" fill="{BLUE}" filter="url(#glow)"/>
<text x="540" y="912" text-anchor="middle" font-family="Cinzel, serif" font-size="34" fill="url(#gold)" letter-spacing="8">THE ONE IN THE COAT</text>
<text x="540" y="950" text-anchor="middle" font-family="Cinzel, serif" font-size="19" fill="{GOLD}" opacity=".85" letter-spacing="3">“the reason why the coat is the thing it is”</text>
{credit(998)}'''
    return page('RiVaL — The One in the Coat', body)


def free(p):
    if not p.exists():
        return p
    v = 2
    while (q := p.with_name(f"{p.stem}-v{v}{p.suffix}")).exists():
        v += 1
    return q


if __name__ == '__main__':
    dry = '--dry-run' in sys.argv
    for name, fn in [('Arcana-1-vesica', vesica), ('Arcana-2-reflection', reflection), ('Arcana-3-coat', coat)]:
        out = free(HERE / f'{name}.html')
        html = fn()
        if dry:
            print(f'would write {out.name} ({len(html):,} chars)')
            continue
        out.write_text(html, encoding='utf-8')
        print(f'ok {out.name} ({out.stat().st_size:,} bytes)')
