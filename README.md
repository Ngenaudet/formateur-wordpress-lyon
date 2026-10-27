# Maquette — Nicolas Genaudet, formateur digital

Maquette locale HTML/CSS/JavaScript : ouvrir `index.html` ou servir le dossier du dépôt. Aucun site existant modifié.

## Contenu confirmé

- Écoles mentionnées par Nicolas : INSEEC, ESDES, ESD, UCLy, NEXT-U et EDEN School. Les matières et périodes restent à préciser.
- Jury DWWM, CDA et CDUI depuis trois ans, selon Nicolas. Les compétences décrites sont celles des référentiels évalués ; cela ne représente pas des diplômes détenus.
- CDUI : référentiel historique RNCP35634, remplacé par RNCP42140 en juillet 2026. Le lien public principal pointe vers le référentiel actuel.
- 31 formations du catalogue public Pilot’in au 13 octobre 2026, toutes intégrées avec lien direct et durée en heures. Catégories éditoriales : Acquisition, Design, HubSpot, WordPress, IA et Stratégie.
- Les pages commerciales Pilot’in mentionnent aussi ActiveCampaign et un intitulé HubSpot combiné non listés séparément dans le catalogue officiel de l’organisme : ils ne sont pas présentés comme des inscriptions ouvertes.
- Certaines fiches détaillées étaient inaccessibles à l’outil de recherche : les liens et durées sont ceux affichés dans l’index officiel. Résumés éditoriaux courts, sans reproduction intégrale des programmes. Les modalités à jour et inscriptions sont accessibles via les liens Pilot’in.
- Nicolas est nommé pour la gestion de site WordPress sur la page https://www.pilot-in.com/formations/. Aucun autre formateur individuel n’est attribué sans preuve.

## Sources

https://pilot-in.catalogueformpro.com/
https://www.pilot-in.com/formations/
https://nicolas-genaudet.fr/
https://www.francecompetences.fr/recherche/rncp/37674/
https://www.francecompetences.fr/recherche/rncp/37873/
https://www.francecompetences.fr/recherche/rncp/35634/
https://www.francecompetences.fr/recherche/rncp/42140/

## Interactions

Recherche, filtres thématiques, fiches modales, liens de programme et contact Pilot’in. Animations CSS, apparitions au défilement, adaptation mobile et réduction des mouvements. Aucune demande n’est envoyée automatiquement.

## SEO et publication o2switch

Le dossier du dépôt doit être la racine web publiée : `index.html`, `.htaccess`, `robots.txt`, `sitemap.xml`, les scripts, le CSS et les images doivent être servis depuis https://formateur-wordpress-lyon.fr/. Le 14 octobre 2026, le domaine répondait avec une liste de répertoire vide : la publication effective reste à vérifier après mise à jour du checkout serveur.

Métadonnées : titre, description, canonical HTTPS, robots, Open Graph, Twitter Card, favicon et image de partage 1200 × 630. JSON-LD : Person, WebSite, WebPage, Organization Pilot’in et ItemList de Course avec Pilot’in comme fournisseur. Aucun avis, tarif ou diplôme personnel inventé. Les formations et liens officiels sont présents dans le HTML sans JavaScript.

Après modification de `pilot-data.js`, régénérer le HTML et le JSON-LD avec `node scripts/build-seo.mjs`. Le sitemap référence seulement la page d’accueil ; les ancres de sections ne sont pas des pages distinctes. Soumettre le sitemap dans Search Console une fois le domaine correctement publié. Aucun jeton de vérification n’est inventé.

### Redirections à venir

Remplir `plan-redirections.csv` avec les anciennes URL et la destination pertinente. Laisser chaque URL inconnue en attente de validation, puis ajouter les redirections 301 au `.htaccess`. Ne pas rediriger toutes les anciennes pages vers l’accueil. Vérifier le statut 301, la destination 200 et l’absence de chaîne ou boucle. Aucune redirection métier n’est activée avant réception des anciennes URL. La seule normalisation déjà configurée concerne `/index.html` vers `/`. Une page 404 réelle est configurée via Apache.

## Mentions légales, paiement et Analytics

Coordonnées fournies par Nicolas : Nicolas Genaudet EI, 1 rue de Montribloud, 69009 Lyon ; SIREN 892530064 ; TVA FR70892530064 ; NDA 84692278769 ; téléphone 0681909494 ; email genaudet.nicolas@gmail.com. Deux pages liées depuis le pied de page : mentions légales et confidentialité. Le médiateur reste à désigner ; les durées de conservation des contacts et des journaux restent à préciser, ainsi que les réglages de traitement du compte GA4. Ces rubriques ne sont pas déclarées entièrement finalisées.

Les formations personnelles sont facturées par Nicolas et payables en trois virements, selon le contrat. Aucun nombre de mensualités, partage en tiers égaux ou frais de financement n’a été inventé. Pour un particulier finançant lui-même une formation professionnelle, établir un contrat conforme, notamment sur le délai de rétractation, l’absence de paiement avant son expiration, le premier versement plafonné et l’échelonnement au fur et à mesure du déroulement de la formation. Les conditions Pilot’in restent distinctes.

GA4 G-NWBTJB68HL : mode de consentement basique, chargement uniquement après acceptation, refus équivalent, retrait au pied de page. Préférence conservée six mois, cookies GA configurés pour treize mois sans renouvellement de l’échéance. Publicité et Google Signals désactivés par la configuration locale. Aucun chargement Analytics dans les aperçus locaux. Vérifier aussi les paramètres GA4 (durée de conservation, partage, mesure améliorée et éventuels usages supplémentaires).

Vérification : `node tests/consent.mjs`. Références : https://developers.google.com/tag-platform/security/concepts/consent-mode et https://entreprendre.service-public.gouv.fr/vosdroits/F33338.

## Blog statique

La rubrique est accessible dans `blog.html`. Les cinq articles sont conservés en Markdown dans `content/blog/` et générés en HTML pour être lisibles et indexables sans JavaScript.

Après une modification des contenus, lancer :

```sh
python3 scripts/build-blog.py
```

Le script reprend le menu de l’accueil et génère les articles, le sommaire, les métadonnées et les données structurées Article, Person et FAQPage (HowTo pour le tutoriel Claude Design). Les consignes de visuels et de balisage fournies dans les textes restent dans les sources, sans être affichées aux lecteurs. Les portraits et captures n’ont pas encore été fournis. Les affirmations et retours d’expérience des textes ChatSEO doivent être relus par l’auteur avant mise en ligne.

Pour ajouter un article, créer sa source Markdown et compléter `POSTS` dans `scripts/build-blog.py`. Le générateur ajoute les URL au sitemap, et `scripts/build-seo.mjs` reprend automatiquement les sources du blog. Les FAQ sont reconnues sous forme de titres H3 ou de questions en gras ; les réponses du balisage reprennent le texte visible. Le comparatif des assistants SEO comprend aussi une liste structurée des cinq outils.


## Supports de cours

Le cours INSEEC « Conception audio & vidéo » (18 heures, MSc2 MCSC) est accessible à `/cours/conception-audio-video/` après déploiement du dépôt. Le dossier contient une page autonome avec styles et scripts locaux, les 77 diapositives originales et une transcription source JSON. Aucun outil de compilation n’est nécessaire.

Le cours reste absent du menu public et du sitemap. La balise `noindex,nofollow` limite son indexation ; l’accès est désormais contrôlé côté serveur par `access.php` et les règles Apache locales. Le même contrôle protège les images, les styles et les scripts. Les sources JSON et la documentation ne sont pas servies.

### Accès au cours

Code partagé à quatre chiffres : empreinte configurée dans `cours/conception-audio-video/access-config.php`. La session dure quatre heures, avec cookies Secure, HttpOnly et SameSite=Lax. Après cinq échecs par adresse IP, les tentatives sont suspendues cinq minutes. Le compteur est conservé dans le dossier temporaire PHP, hors de la racine web. Une modification de l’empreinte invalide les sessions précédentes.

Nécessite PHP 7.4+ et Apache avec mod_rewrite/AllowOverride sur l’hébergement. Déployer aussi le fichier caché `.htaccess` du cours. La protection du site ne modifie pas la visibilité du dépôt GitHub.

Test local : lancer le serveur PHP avec `php -S 127.0.0.1:8766 cours/conception-audio-video/access.php`, puis exécuter `python3 tests/course-access.py http://127.0.0.1:8766/cours/conception-audio-video/` et saisir le code sur l’entrée standard. Le test finit par déclencher la limite de tentatives locale ; attendre cinq minutes avant de le relancer. Le routage Apache doit également être vérifié après déploiement.

### Version pédagogique enrichie du 27 octobre 2026

57 slides révisées réparties en dix chapitres, dont 17 compléments pédagogiques. Palette inspirée du support original (bleu, lavande, corail), ateliers dédiés, cinq schémas éditables, recherche et diaporama avec flèches clavier / Échap. Les 77 images originales restent dans les archives du cours.

Modifier `cours/conception-audio-video/slides.json`, puis lancer `python3 scripts/build-course.py`. Les schémas se trouvent dans `scripts/course_visuals.py`. Vérifier avec `python3 tests/course-content.py` et `node --check cours/conception-audio-video/app.js`.

L’audit détaillé est dans `audits/audit-conception-audio-video-2026-10-27.md`. Il distingue les corrections effectuées et les points à confirmer par le formateur. La protection par code existante est conservée.
