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
