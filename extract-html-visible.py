from pathlib import Path
from html.parser import HTMLParser
import collections
import hashlib
import json

source = Path('/Users/steven/Downloads/making-of-RiVaL (1).html')
out = Path(__file__).resolve().parent / 'rival-source-review'

class Reader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.item_depth = None
        self.content_depth = None
        self.current = None
        self.records = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cl = (a.get('class') or '').split()
        if tag == 'div':
            self.depth += 1
            if 'conversation-item' in cl:
                assert self.current is None
                self.item_depth = self.depth
                self.current = {'ordinal': len(self.records)+1, 'role': None, 'parts': []}
            if self.current is not None and 'author' in cl:
                self.current['role'] = 'user' if 'user' in cl else 'assistant' if 'assistant' in cl else 'unknown'
            if self.current is not None and 'conversation-content' in cl:
                self.content_depth = self.depth
        if self.content_depth is not None and tag in ('p','br','li','pre','tr','h1','h2','h3','blockquote'):
            self.current['parts'].append('\n')

    def handle_endtag(self, tag):
        if self.content_depth is not None and tag in ('p','li','pre','tr','h1','h2','h3','blockquote'):
            self.current['parts'].append('\n')
        if tag == 'div':
            if self.content_depth == self.depth:
                self.content_depth = None
            if self.item_depth == self.depth:
                self.current['text'] = ''.join(self.current.pop('parts')).strip()
                self.records.append(self.current)
                self.current = None
                self.item_depth = None
            self.depth -= 1

    def handle_data(self, text):
        if self.current is not None and self.content_depth is not None:
            self.current['parts'].append(text)

r = Reader()
r.feed(source.read_text())
assert r.current is None and len(r.records) == 77
(out / 'html-visible-records.json').write_text(json.dumps(r.records, indent=2, ensure_ascii=False)+'\n')
(out / 'html-visible-dialogue.md').write_text('\n\n'.join('## HTML item {ordinal} | {role}\n\n{text}'.format(**x) for x in r.records)+'\n')
print(json.dumps({'source': str(source), 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                  'items': len(r.records), 'roles': dict(collections.Counter(x['role'] for x in r.records)),
                  'note': 'Static text extraction with layout normalization; no HTML scripts/assets executed.'}))
