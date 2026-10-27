"""Vérifie le contenu généré, ses liens locaux et sa correspondance aux sources."""
from pathlib import Path
from html.parser import HTMLParser
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
COURSE=ROOT/'cours/conception-audio-video'
class Structure(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.local=[];self.anchors=[];self.slides=0;self.images=0;self.labels=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.append(d['id'])
  if tag=='article' and 'lesson' in d.get('class','').split():self.slides+=1
  if tag=='img':self.images+=1;assert d.get('alt') or d.get('aria-hidden')=='true'
  if 'aria-labelledby' in d:self.labels.extend(d['aria-labelledby'].split())
  for k in ['href','src']:
   v=d.get(k,'')
   if v.startswith('#'):self.anchors.append(v[1:])
   elif v and ':' not in v:self.local.append(v)
data=json.loads((COURSE/'slides.json').read_text())
slides=[s for c in data['chapters'] for s in c['slides']]
assert len(slides)==57 and sum(s['added'] for s in slides)==17
assert len(data['chapters'])==10
for s in slides:
 assert s['title'] and s['lead'] and s['takeaway']
 assert s['items'] or s.get('table')
 assert all(1<=n<=77 for n in s['source_pages'])
check=Structure();check.feed((COURSE/'index.html').read_text())
assert check.slides==57 and check.images==78
assert len(check.ids)==len(set(check.ids))
assert all(x in check.ids for x in check.anchors+check.labels)
assert all((COURSE/f).is_file() for f in check.local)
before=hashlib.sha256((COURSE/'index.html').read_bytes()).hexdigest()
subprocess.run([sys.executable,str(ROOT/'scripts/build-course.py')],check=True)
assert before==hashlib.sha256((COURSE/'index.html').read_bytes()).hexdigest(), 'La génération doit être reproductible'
print('57 slides, 17 compléments, 77 originaux et portrait, liens, titres accessibles et génération reproductible vérifiés.')
