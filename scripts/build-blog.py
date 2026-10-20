"""Build the static blog from the supplied Markdown, using Python's standard library."""
from pathlib import Path
import html
import json
import re
import unicodedata
from html.parser import HTMLParser
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://formateur-wordpress-lyon.fr/'
POSTS = [
    ('creer-site-wordpress-ia', 'Créer un site WordPress avec IA', 'WordPress', 'Brief, contenus, construction et recette : une méthode concrète pour créer un site WordPress avec l’IA sans perdre le contrôle.'),
    ('seo-avec-ia', 'SEO avec IA : la méthode', 'SEO', 'Une méthode en cinq étapes pour utiliser l’IA en SEO : mots-clés, analyse des SERP, rédaction, maillage et suivi.'),
    ('assistant-seo-ia-comparatif', 'Quel assistant SEO IA choisir ?', 'SEO', 'ChatSEO, Semrush, Surfer SEO, NeuronWriter et les assistants connectés à Search Console : usages, limites et budgets comparés.'),
    ('claude-code-wordpress', 'Claude Code & WordPress', 'Développement', 'Prompts, configuration et retours de terrain pour utiliser Claude Code sur un projet WordPress client.'),
    ('claude-design-wordpress', 'Claude Design & WordPress', 'UX/UI', 'Du brief à la maquette : une méthode pour préparer un site WordPress avec Claude Design, les patterns et ACF.'),
]
esc = html.escape

def inline(text):
    codes = []
    def code(m):
        codes.append('<code>' + esc(m[1]) + '</code>')
        return f'\x00{len(codes)-1}\x00'
    text = re.sub(r'`([^`]+)`', code, text)
    text = esc(text)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    text = re.sub(r'\x00(\d+)\x00', lambda m: codes[int(m[1])], text)
    return text

def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode().lower()).strip('-')

def markdown(source):
    lines = source.splitlines()
    out, headings = [], []
    anchors = {}
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith('```'):
            lang, block = line[3:], []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                block.append(lines[i]); i += 1
            out.append(f'<pre><code class="language-{esc(lang)}">{esc(chr(10).join(block))}</code></pre>')
        elif re.match(r'^#{2,3} ', line):
            level = len(line.split(' ')[0]); title = line[level+1:]; base_anchor = slug(title)
            anchors[base_anchor] = anchors.get(base_anchor, 0) + 1
            anchor = base_anchor if anchors[base_anchor] == 1 else f'{base_anchor}-{anchors[base_anchor]}'
            if level == 2: headings.append((anchor, title))
            out.append(f'<h{level} id="{anchor}">{inline(title)}</h{level}>')
        elif line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                row = [x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', x) for x in row): rows.append(row)
                i += 1
            out.append('<div class="table-scroll" tabindex="0" role="region" aria-label="Tableau comparatif"><table><thead><tr>' + ''.join('<th scope="col">'+inline(x)+'</th>' for x in rows[0]) + '</tr></thead><tbody>' + ''.join('<tr>'+''.join('<td>'+inline(x)+'</td>' for x in row)+'</tr>' for row in rows[1:]) + '</tbody></table></div>')
            continue
        elif re.match(r'^(?:-\s+|\d+\.\s+)', line):
            ordered = bool(re.match(r'^\d+\.', line)); tag = 'ol' if ordered else 'ul'; items = []
            pattern = r'^\d+\.\s+' if ordered else r'^-\s+'
            while i < len(lines):
                current = lines[i].strip()
                if not current:
                    i += 1; continue
                if not re.match(pattern, current): break
                items.append('<li>'+inline(re.sub(pattern, '', current))+'</li>'); i += 1
            out.append(f'<{tag}>'+''.join(items)+f'</{tag}>'); continue
        elif line.startswith('> '): out.append('<blockquote><p>'+inline(line[2:])+'</p></blockquote>')
        elif line == '* * *': out.append('<hr>')
        else:
            paragraph = [line]; i += 1
            while i < len(lines) and lines[i].strip():
                paragraph.append(lines[i].strip()); i += 1
            out.append('<p>'+inline(' '.join(paragraph))+'</p>'); continue
        i += 1
    return '\n'.join(out), headings

class TextContent(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, data):
        self.parts.append(data)
    def handle_endtag(self, tag):
        if tag in ('p', 'li', 'br'): self.parts.append(' ')

def plain(markup):
    parser = TextContent()
    parser.feed(markup)
    return re.sub(r'\s+', ' ', ''.join(parser.parts)).strip()

home = (ROOT / 'index.html').read_text()
header = re.search(r'<header class="site-header">[\s\S]*?</header>', home)[0]
header = header.replace('href="#"', 'href="index.html"')
header = re.sub(r'href="#([^\"]+)"', r'href="index.html#\1"', header)
header = header.replace('href="blog.html"', 'href="blog.html" aria-current="page"')
footer = '''<footer class="wrap"><a href="index.html">Accueil</a><a href="blog.html">Blog</a><a href="mentions-legales.html">Mentions légales</a><a href="confidentialite.html">Confidentialité</a><button data-cookie-settings>Gérer les cookies</button><p>© 2026 Nicolas Genaudet EI</p></footer>'''
banner = re.search(r'<aside id="cookie-banner"[\s\S]*?</aside>', home)[0]

def page(title, description, filename, body, graph, article=False):
    canonical = BASE + filename
    return f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} | Nicolas Genaudet</title><meta name="description" content="{esc(description)}"><meta name="author" content="Nicolas Genaudet"><meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="{canonical}">
<meta property="og:type" content="{'article' if article else 'website'}"><meta property="og:locale" content="fr_FR"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{BASE}social-preview.png"><meta property="og:image:alt" content="Nicolas Genaudet — Formateur WordPress à Lyon"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="blog.css">
<script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@graph':graph}, ensure_ascii=False).replace('<', chr(92)+'u003c')}</script><script src="navigation.js" defer></script><script src="consent.js" defer></script></head>
<body><a class="skip" href="#main">Aller au contenu</a>{header}<main id="main">{body}</main>{footer}{banner}</body></html>'''

person = {'@type':'Person','@id':BASE+'#nicolas','name':'Nicolas Genaudet','url':'https://nicolas-genaudet.fr/','jobTitle':'Formateur WordPress, UX/UI et SEO','address':{'@type':'PostalAddress','addressLocality':'Lyon','addressCountry':'FR'}}
cards = []
for key, short, category, description in POSTS:
    source = (ROOT / 'content/blog' / (key+'.md')).read_text()
    title = source.splitlines()[0][2:]
    content = source.split('## Spécifications de balisage')[0]
    # Production notes are retained in Markdown, never rendered as broken images.
    content = '\n'.join(line for line in content.splitlines() if not re.match(r'^(?:!\\\[|\*\\\[(?:PHOTO|CAPTURE))', line))
    content = '\n'.join(content.splitlines()[1:]).strip()
    content = re.sub(r'^\*{1,2}Par Nicolas Genaudet[^\n]*(?:\n|$)', '', content).strip()
    rendered, headings = markdown(content)
    toc = '<details class="article-toc" open><summary>Dans cet article</summary><ol>'+''.join(f'<li><a href="#{anchor}">{esc(label)}</a></li>' for anchor,label in headings)+'</ol></details>'
    minutes = round(len(content.split()) / 220)
    filename = key+'.html'
    cta = '<aside class="article-cta"><span class="eyebrow">PASSER À LA PRATIQUE</span><h2>Votre prochain projet commence ici.</h2><p>Progressez en WordPress et en UX/UI avec Nicolas Genaudet, à Lyon ou à distance.</p><a class="button coral" href="index.html#formations">Explorer les formations ↗</a> <a class="course-link" href="https://nicolas-genaudet.fr/#contact">Parlons de votre projet ↗</a></aside>'
    others = sorted((p for p in POSTS if p[0] != key), key=lambda p: p[2] != category)[:2]
    related = '<aside class="related"><h2>À lire aussi</h2><ul>' + ''.join(f'<li><a href="{p[0]}.html">{esc(p[1])} ↗</a></li>' for p in others) + '</ul></aside>'
    body = f'<div class="wrap article-shell"><nav class="breadcrumbs" aria-label="Fil d’Ariane"><a href="index.html">Accueil</a><span aria-hidden="true">/</span><a href="blog.html">Blog</a></nav><article><div class="article-heading"><span class="eyebrow">{esc(category.upper())} · OUTILS IA</span><h1>{esc(title)}</h1><p class="article-meta">Par <a href="index.html#parcours">Nicolas Genaudet</a>, formateur à Lyon · <time datetime="2026-10-20">20 octobre 2026</time> · {minutes} min de lecture</p></div><div class="article-layout"><div class="article-content">{rendered}{cta}{related}</div>{toc}</div></article></div>'
    graph = [person, {'@type':'Article','headline':title,'description':description,'datePublished':'2026-10-20','dateModified':'2026-10-20','author':{'@id':BASE+'#nicolas'},'publisher':{'@id':BASE+'#nicolas'},'mainEntityOfPage':BASE+filename,'inLanguage':'fr-FR','articleSection':category}]
    faq_match = re.search(r'^## FAQ\s*\n([\s\S]*?)(?=^## |\Z)', content, re.M)
    if faq_match:
        faq = faq_match[1].strip()
        pairs = re.findall(r'^### (.+)\n+([\s\S]+?)(?=\n### |\Z)', faq, re.M)
        if not pairs:
            pairs = re.findall(r'^\*\*(.+?)\*\* (.+)', faq, re.M)
        if pairs:
            graph.append({'@type':'FAQPage','mainEntity':[{'@type':'Question','name':plain(inline(q.strip())),'acceptedAnswer':{'@type':'Answer','text':plain(markdown(a.strip())[0])}} for q,a in pairs]})
    if key == 'assistant-seo-ia-comparatif':
        tools = [
            ('ChatSEO', 'https://chatseo.app/', 'Assistant conversationnel connecté à Google Search Console.'),
            ('Semrush', 'https://www.semrush.com/', 'Suite de recherche de mots-clés, audit et suivi de positions.'),
            ('Surfer SEO', 'https://surferseo.com/', 'Briefs éditoriaux et optimisation on-page.'),
            ('NeuronWriter', 'https://neuronwriter.com/', 'Optimisation sémantique et rédaction assistée.'),
            ('ChatGPT + Search Console', 'https://chatgpt.com/', 'Assistant généraliste associé à un connecteur Search Console.'),
        ]
        graph.append({'@type':'ItemList','name':'Les cinq assistants SEO IA comparés','itemListElement':[{'@type':'ListItem','position':i,'name':name,'url':url,'description':desc} for i,(name,url,desc) in enumerate(tools, 1)]})
    if key == 'claude-design-wordpress':
        steps = [(a,t) for a,t in headings if t.startswith(('Préparer le brief','Étape '))]
        graph.append({'@type':'HowTo','name':'Produire une maquette de site WordPress avec Claude Design','totalTime':'PT2H','step':[{'@type':'HowToStep','name':t,'url':BASE+filename+'#'+a} for a,t in steps]})
    (ROOT / filename).write_text(page(title, description, filename, body, graph, True))
    cards.append(f'<article class="blog-card"><a class="blog-cover" href="{filename}" aria-label="{esc(title)}"><span class="eyebrow">{esc(category.upper())}</span><span class="cover-title">{esc(short).replace(" &amp; ", "<br>&amp; ")}</span><span aria-hidden="true">↗</span></a><div class="blog-card-body"><p class="article-meta"><time datetime="2026-10-20">20 octobre 2026</time> · {minutes} min</p><h2><a href="{filename}">{esc(title)}</a></h2><p>{esc(description)}</p><a class="course-link" href="{filename}">Lire l’article <span>↗</span></a></div></article>')
body = '<section class="wrap blog-intro"><span class="eyebrow">LE BLOG DE NICOLAS GENAUDET</span><h1>Le web en pratique.<br><em>Les idées en partage.</em></h1><p>WordPress, UX/UI et outils IA : des tutoriels et des retours de terrain pour faire avancer vos projets, à Lyon et partout ailleurs.</p></section><section class="wrap blog-list" aria-label="Les derniers articles">'+''.join(cards)+'</section>'
(ROOT / 'blog.html').write_text(page('Blog WordPress, UX/UI et IA', 'Tutoriels WordPress, UX/UI et retours de terrain sur les outils IA par Nicolas Genaudet, formateur à Lyon et à distance.', 'blog.html', body, [{'@type':'Blog','name':'Le blog de Nicolas Genaudet','url':BASE+'blog.html','inLanguage':'fr-FR','author':person}]))
# Keep the sitemap in sync without dropping the existing site pages.
ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
sitemap = ET.parse(ROOT / 'sitemap.xml')
ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
locations = {node.text for node in sitemap.iter(ns+'loc')}
for filename in ['blog.html'] + [p[0]+'.html' for p in POSTS]:
    if BASE+filename not in locations:
        ET.SubElement(ET.SubElement(sitemap.getroot(), ns+'url'), ns+'loc').text = BASE+filename
sitemap.write(ROOT / 'sitemap.xml', encoding='UTF-8', xml_declaration=True)
print(f'Blog et {len(POSTS)} articles générés.')
