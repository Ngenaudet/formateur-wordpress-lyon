"""Visuels du cours : images, exemples photographiques et parcours illustrés."""
import html,struct
from pathlib import Path
from course_visuals import render_diagram
def e(s):return html.escape(str(s),quote=True)
def board(name,alt,caption):
 path='assets/visuel-'+name+'.png'
 width,height=struct.unpack('>II',(Path(__file__).resolve().parents[1]/'cours/conception-audio-video'/path).read_bytes()[16:24])
 return f'<figure class="visual-board"><button class="zoom-image" type="button" data-zoom-src="{path}" data-zoom-alt="{e(alt)}" aria-label="Agrandir : {e(alt)}"><img src="{path}" alt="{e(alt)}" loading="lazy" width="{width}" height="{height}"></button><figcaption>{e(caption)} · Cliquer pour agrandir</figcaption></figure>'
def crop(x,y,w,h,label,caption):
 return f'<div class="photo-example"><div class="photo-window" style="aspect-ratio:{w}/{h}"><img src="assets/visuel-histoire.png" alt="{e(label)}" loading="lazy" style="width:{1486/w*100:.3f}%;height:{988/h*100:.3f}%;left:{-x/w*100:.3f}%;top:{-y/h*100:.3f}%"></div><strong>{e(label)}</strong><small>{e(caption)}</small></div>'
def render_visual(kind,slide):
 if kind=='reference':return board('histoire','Avant de filmer : plans, émotion, composition, anticipation du montage et rythme','Infographie du support fournie par le formateur')
 if kind=='light':return board('lumiere','Comparaison : visage sombre à contre-jour et visage éclairé par une fenêtre de côté','Illustration pédagogique : modifier la position du sujet change la lumière sur le visage')
 if kind=='sound':return board('son','Trois étapes : lieu calme, micro bien placé et écoute du test ; saturation comparée à une prise propre','Illustration pédagogique : les formes d’onde sont schématiques')
 if kind=='storyboard':return board('storyboard','Quatre plans : situation de distraction, activation du minuteur, concentration et présentation de la lampe','Exemple pédagogique fictif : la situation, l’action, le bénéfice puis l’invitation')
 if kind=='framing-photo':
  specs=[(7,280,178,120,'Plan large','Situer le personnage.'),(197,280,178,120,'Plan moyen','Montrer son action.'),(386,280,178,120,'Plan rapproché','Créer la proximité.'),(575,280,178,120,'Gros plan','Montrer une émotion.'),(765,280,178,120,'Plan de détail','Isoler un élément.')]
  return '<figure class="photo-examples">'+''.join(crop(*s) for s in specs)+'<figcaption>Le même univers, cinq intentions de cadrage. Le plan américain, présenté dans les explications, coupe vers la mi-cuisse.</figcaption></figure>'
 if kind=='movements-photo':
  specs=[(7,581,143,102,'Plan fixe','Caméra immobile.'),(163,581,143,102,'Travelling','La caméra se déplace.'),(319,581,143,102,'Panoramique','La caméra pivote.'),(475,581,143,102,'Angle de vue','Changer le point de vue.'),(631,581,143,102,'Règle des tiers','Composer le cadre.')]
  return '<figure class="photo-examples">'+''.join(crop(*s) for s in specs)+'<figcaption>Échelle, angle et mouvement sont trois choix distincts.</figcaption></figure>'
 if kind in ['arc','steps','tracks','formats']:return render_diagram(kind)
 if kind=='timing':
  return '<div class="visual-timing" aria-label="Répartition indicative des 90 secondes">'+''.join(f'<div><strong>{a}</strong><span>{b}</span><small>{c}</small></div>' for a,b,c in [('0–10 s','Accroche','Se reconnaître'),('10–25 s','Problème','Comprendre'),('25–50 s','Solution','Découvrir'),('50–75 s','Preuve','Être convaincu'),('75–90 s','Action','Passer à la suite')])+'</div>'
 if kind=='grading':
  final='barème' in slide['title'].lower()
  values=[('6 / 20','Message'),('8 / 20','Créativité'),('6 / 20','Rendu')] if final else [('50 %','Suivi du projet'),('50 %','Présentation finale')]
  return '<div class="visual-grading">'+''.join(f'<div><strong>{a}</strong><span>{b}</span></div>' for a,b in values)+'</div>'
 if kind=='roadmap':
  return '<ol class="visual-flow">'+''.join(f'<li><span aria-hidden="true">{icon}</span><strong>{title}</strong><small>3 heures</small></li>' for icon,title in [('🎯','Stratégie'),('✏️','Scénario'),('📱','Premier essai'),('🎬','Tournage'),('✂️','Montage'),('📤','Livraison')])+'</ol>'
 if kind=='premiere':
  return '<figure class="visual-board"><img src="assets/diapo-65.jpg" alt="Capture du support : médias, timeline, moniteur, effets et options d’effets dans Premiere" loading="lazy"><figcaption>Capture du support d’origine ; l’interface dépend de la version.</figcaption></figure>'
 icons={'skills':['🎯','✏️','🎬','💬'],'content':['📖','🎥','🎙️'],'impact':['👁️','💡','🤝'],'formats-content':['📦','💬','🎤'],'brief':['🎯','💡','✅'],'deliverables':['🎬','📱','📁'],'production':['🎒','👥','🗓️'],'skeleton':['🎯','🧩','✅'],'script':['💬','🎥','🎵'],'smartphone':['📐','☀️','🔋'],'voiceover':['✏️','🎙️','⏺️','🎧'],'mix':['✂️','🎚️','🎧'],'folders':['📂','🏷️','💾'],'edit-workflow':['🗂️','✂️','🎨','✅'],'effects':['↔️','🎨','✨'],'export':['📂','⚙️','▶️'],'captions':['✍️','⏱️','💬'],'sharing':['▶️','📁','🔒'],'checklist':['🎯','🎧','📦'],'dossier':['🎯','✏️','📤']}
 if kind not in icons:return ''
 cards=[]
 for i,item in enumerate(slide['items']):
  text=item['text'].strip().rstrip('.')
  if len(text)>105:text=text[:102].rsplit(' ',1)[0]+'…'
  cards.append(f'<li><span class="visual-symbol" aria-hidden="true">{icons[kind][i%len(icons[kind])]}</span><strong>{e(item["title"])}</strong><span>{e(text)}</span></li>')
 result='<ol class="visual-flow cards-'+str(len(cards))+'">'+''.join(cards)+'</ol>'
 if slide.get('eeat'):
  result+='<section class="eeat-panel" aria-label="Le cadre E-E-A-T de Google"><h4>GOOGLE · E-E-A-T <span>Des contenus utiles et crédibles</span></h4><div class="eeat-grid">'
  for pillar in slide['eeat']:
   result+='<div class="eeat-pillar"><b>'+e(pillar['letter'])+'</b><strong>'+e(pillar['title'])+'</strong><small>'+e(pillar['english'])+'</small><p>'+e(pillar['example'])+'</p></div>'
  result+='</div><a href="'+e(slide['eeat_source'])+'" target="_blank" rel="noopener noreferrer">Source : Google Search Central ↗</a></section>'
 return result
