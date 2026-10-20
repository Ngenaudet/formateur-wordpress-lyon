import fs from 'node:fs';
import vm from 'node:vm';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const base='https://formateur-wordpress-lyon.fr/';
const courses=vm.runInNewContext(fs.readFileSync(path.join(root,'pilot-data.js'),'utf8')+';pilotCourses');
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
let html=fs.readFileSync(path.join(root,'index.html'),'utf8');
const graph=[
{'@type':'Person','@id':base+'#nicolas',name:'Nicolas Genaudet',url:'https://nicolas-genaudet.fr/',sameAs:['https://nicolas-genaudet.fr/'],jobTitle:'Formateur WordPress, designer UX/UI et consultant SEO',knowsAbout:['WordPress','UX/UI','Figma','SEO','Référentiels DWWM, CDA et CDUI'],description:'Formateur à Lyon et à distance. Jury des titres professionnels DWWM, CDA et CDUI depuis trois ans.'},
{'@type':'Organization','@id':'https://www.pilot-in.com/#organization',name:'Pilot’in',url:'https://www.pilot-in.com/'},
{'@type':'WebSite','@id':base+'#website',url:base,name:'Nicolas Genaudet — Formateur WordPress à Lyon',inLanguage:'fr-FR',publisher:{'@id':base+'#nicolas'}},
{'@type':'WebPage','@id':base+'#webpage',url:base,name:'Formateur WordPress à Lyon | Nicolas Genaudet',description:'Formations WordPress, UX/UI et SEO avec Nicolas Genaudet à Lyon et à distance. Découvrez le catalogue des formations Pilot’in.',inLanguage:'fr-FR',isPartOf:{'@id':base+'#website'},about:{'@id':base+'#nicolas'},mainEntity:{'@id':base+'#catalogue'}},
{'@type':'ItemList','@id':base+'#catalogue',name:'Catalogue des formations Pilot’in',numberOfItems:courses.length,itemListElement:courses.map((c,i)=>({'@type':'ListItem',position:i+1,item:{'@type':'Course','@id':c.source+'#course',url:c.source,name:c.title,description:c.desc,inLanguage:'fr-FR',provider:{'@id':'https://www.pilot-in.com/#organization'}}}))}
];
const title='Formateur WordPress à Lyon | Nicolas Genaudet';
const description='Formations WordPress, UX/UI et SEO avec Nicolas Genaudet à Lyon et à distance. Découvrez le catalogue des formations Pilot’in.';
const head=`<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title}</title>
<meta name="description" content="${description}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="author" content="Nicolas Genaudet">
<meta name="theme-color" content="#3844ef">
<link rel="canonical" href="${base}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Nicolas Genaudet — Formateur WordPress">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${description}">
<meta property="og:url" content="${base}">
<meta property="og:image" content="${base}social-preview.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png">
<meta property="og:image:alt" content="Nicolas Genaudet — Formateur WordPress à Lyon. Le digital, en pratique.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${title}">
<meta name="twitter:description" content="${description}">
<meta name="twitter:image" content="${base}social-preview.png">
<meta name="twitter:image:alt" content="Nicolas Genaudet — Formateur WordPress à Lyon">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="style.css">
<script type="application/ld+json">${JSON.stringify({'@context':'https://schema.org','@graph':graph}).replaceAll('<','\\u003c')}</script>
<script src="pilot-data.js" defer></script>
<script src="app.js" defer></script>
</head>`;
html=html.replace(/<head>[\s\S]*?<\/head>/,head);
const cards=courses.map((c,i)=>`<article class="course"><div class="course-visual" aria-hidden="true"><span>${esc(c.icon)}</span></div><div class="course-body"><div class="course-meta"><span>${esc(c.domain)}</span><span>${c.hours.toLocaleString('fr')} h · Pilot’in</span></div><h3>${esc(c.title)}</h3><p>${esc(c.desc)}${c.nicolas?'<br><strong>Avec Nicolas Genaudet</strong>':''}</p><a class="course-link" href="${esc(c.source)}" target="_blank" rel="noopener">Voir le programme chez Pilot’in <span>↗</span></a><button data-index="${i}">Découvrir la formation <span>↗</span></button></div></article>`).join('\n');
html=html.replace(/<div class="course-grid" id="courses">[\s\S]*?<\/div><p id="result-count"/,`<div class="course-grid" id="courses">${cards}</div><p id="result-count"`);
html=html.replace(/(<p id="result-count"[^>]*>)[\s\S]*?<\/p>/,'$131 formations Pilot’in</p>');
html=html.replace('<p id="catalogue-note" class="catalogue-note"></p>','<p id="catalogue-note" class="catalogue-note">Formations proposées par Pilot’in. Consultez les programmes officiels pour les modalités et inscriptions.</p>');
fs.writeFileSync(path.join(root,'index.html'),html);
fs.writeFileSync(path.join(root,'sitemap.xml'),`<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>${base}</loc></url><url><loc>${base}mentions-legales.html</loc></url><url><loc>${base}confidentialite.html</loc></url><url><loc>${base}blog.html</loc></url>${fs.readdirSync(path.join(root,'content/blog')).filter(f=>f.endsWith('.md')).map(f=>`<url><loc>${base}${f.slice(0,-3)}.html</loc></url>`).join('')}</urlset>\n`);
fs.writeFileSync(path.join(root,'robots.txt'),`User-agent: *\nAllow: /\n\nSitemap: ${base}sitemap.xml\n`);
console.log(`SEO généré : ${courses.length} formations, métadonnées, JSON-LD, sitemap et robots.txt.`);
