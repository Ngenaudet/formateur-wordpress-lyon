# SEO avec IA : ma méthode en 5 étapes (et ce qui ne marche pas)

**Par Nicolas Genaudet**, formateur SEO et WordPress à Lyon - [profil LinkedIn](https://www.linkedin.com/in/nicolas-genaudet)

Ma règle de départ n'a pas bougé depuis deux ans : **l'IA ne touche jamais un sujet que je ne maîtrise pas.** Pas par principe, par rendement. La première fois que je l'ai lâchée sur un thème que je connaissais mal, j'ai obtenu 1 200 mots impeccables, bien titrés, sans une seule faute - et sans un seul fait vérifiable. J'ai tout réécrit.

Le débat sur le « SEO avec IA » tourne souvent autour de la question « est-ce que Google pénalise ? ». C'est la mauvaise question. La bonne : est-ce que la page apporte quelque chose que le top 10 n'apporte pas déjà ? L'IA change la vitesse d'exécution, pas la valeur ajoutée. C'est là que tout se joue, et c'est ce que je forme en atelier à Lyon depuis deux ans, auprès de plus de 600 professionnels et étudiants.

## En bref

-   **L'IA accélère l'exécution**, elle ne choisit pas la stratégie. Le brief, l'angle et les preuves restent humains.
    
-   **Les cinq étapes du workflow** où le gain est réel : mots-clés, SERP, brief/rédaction, maillage, audit et suivi.
    
-   **En France, « seo avec ia » ne fait que 20 recherches par mois** - mais à 9,08 € de CPC. Faible volume, forte intention d'achat.
    
-   **Le garde-fou numéro un** : aucun chiffre publié sans source primaire vérifiée à la main. Aucun.
    

## L'IA ne remplace pas la stratégie : elle accélère l'exécution

Ce que l'IA fait très bien : trier, regrouper, résumer, reformuler, générer des variantes, écrire du regex, produire un plan à partir de dix concurrents, mettre en forme un tableau. Ce qu'elle fait mal, structurellement : décider à qui l'on parle, choisir un angle, assumer une position, et fournir une expérience de première main.

Google le formule sans détour dans sa [documentation sur le contenu génératif](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) : la qualité ne dépend pas de l'outil, mais de l'utilité et de l'originalité. Sa politique anti-spam vise le *scaled content abuse*, c'est-à-dire « de grandes quantités de contenu non original, sans valeur pour les utilisateurs, peu importe la façon dont il est créé ». Autrement dit : produire 200 pages parce qu'on peut le faire, c'est le vrai risque - pas le fait d'utiliser ChatGPT.

Les chiffres aident à sortir du fantasme. Dans son étude de juillet 2025 portant sur 600 000 pages et 100 000 mots-clés, Ahrefs a trouvé que [86,5 % des pages du top 20 de Google contenaient du texte assisté par IA](https://ahrefs.com/blog/ai-generated-content-does-not-hurt-your-google-rankings/), dont seulement 4,6 % entièrement générées. La masse du classement est hybride. Ce qui départage les pages, ce n'est pas le taux d'IA, c'est ce qu'il y a dedans.

## Étape 1 : recherche et priorisation des mots-clés

Je ne commence jamais par demander une liste de mots-clés à un modèle. Il invente des volumes, et il les invente avec un aplomb remarquable. Je commence par trois sources de données réelles : les exports de Search Console des 16 derniers mois, les questions que les clients posent en formation, et une base type DataForSEO ou Semrush.

Là, un **outil SEO IA** devient utile. Le [Keyword Strategy Builder de Semrush](https://www.semrush.com/kb/1058-keyword-strategy-builder) regroupe des milliers de requêtes en clusters et en piliers ; je m'en sers comme d'un premier jet à corriger, jamais comme d'un livrable.

Sur le terrain français, la lecture des volumes évite les erreurs de casting. Un relevé DataForSEO récent donne :

| Requête | Recherches/mois | CPC |
| --- | --- | --- |
| ia seo | 140 | \- |
| seo chatgpt | 50 | \- |
| chatgpt seo | 30 | \- |
| seo avec ia | 20 | 9,08 € |
| outil seo ia | 20 | \- |
| chatgpt pour le seo / ia rédaction seo | 10 chacun | \- |

Un mot-clé à 20 recherches par mois et 9 € de CPC, c'est du B2B à forte intention : peu de monde, mais des gens qui cherchent une méthode, pas une définition. Ce genre de requête se travaille en page pilier, pas en post de blog jetable. Et « ia seo » à 140 recherches sert de variante naturelle dans le corps du texte.

Mon prompt de qualification, quand j'ai déjà les données :

```
Rôle : stratège SEO B2B francophone.
Contexte : j'ai joint un export de 340 requêtes (volume, CPC, intention estimée).
Tâche : regroupe-les en clusters d'intention, propose 1 page par cluster,
et signale les requêtes que je devrais fusionner avec une page existante.
Contraintes : ne crée aucun chiffre. Si une donnée manque, écris "à vérifier".
Sortie : tableau markdown, 3 colonnes (cluster, requêtes, page cible).
```

La priorisation se fait ensuite à la main, sur une matrice simple : intention × difficulté × ma capacité à apporter une preuve. Une page sans preuve à apporter ne passe pas.

## Étape 2 : analyse des SERP et des concurrents

L'analyse SERP est le domaine où l'IA fait gagner le plus de temps - à condition de lui donner les vrais résultats, pas de lui demander de les deviner. Je lui colle les cinq premières positions, titres et plans Hn inclus.

Ce que dit la SERP française sur « seo avec ia », en date d'octobre 2026 : lemon-interactive en 2, burguindigital en 4, digital-passengers en 5, semrush.fr en 9, hubspot.fr en 10, webrankinfo en 11. **Aucun forum, aucune vidéo YouTube.** C'est une information stratégique : Google considère cette requête comme une demande de méthode ou de guide, pas comme un débat d'opinion. Donc pas de billet d'humeur, pas de « l'IA va-t-elle tuer le SEO ». Une procédure, des étapes, des exemples.

Le prompt que j'utilise pour repérer les angles morts :

```
Voici les plans Hn des 5 pages en top 5 pour "seo avec ia" (collés ci-dessous).
1) Liste les sous-sujets traités par au moins 4 pages sur 5 (le socle obligatoire).
2) Liste ce qu'aucune page ne traite.
3) Repère les affirmations non sourcées ou contradictoires entre pages.
Ne rédige pas l'article. Ne paraphrase pas les titres.
```

Deux règles que j'applique systématiquement :

-   **Ne jamais demander un résumé des concurrents.** Un modèle qui résume cinq textes produit un sixième texte qui ressemble aux cinq autres. On paie ensuite en duplicate.
    
-   **Vérifier chaque affirmation « sourcée »** par le modèle lui-même. Il cite volontiers des études qui n'existent pas, avec un titre crédible et une année plausible.
    

Dernier point de méthode : Ahrefs montre que [76,1 % des pages citées dans les AI Overviews de Google viennent du top 10 organique](https://ahrefs.com/blog/search-rankings-ai-citations/). La conclusion est banale et implacable : on ne cite pas une page invisible. Le travail de classement reste le préalable à toute visibilité dans les réponses IA.

## Étape 3 : brief et rédaction

C'est l'étape où l'**ia rédaction seo** fait le plus de dégâts, et c'est aussi celle où je l'utilise le plus. La différence tient à une chose : ce que je mets dans le brief.

Un brief que l'IA produit seule à partir d'une SERP donne un article encyclopédique et interchangeable. Un brief qui contient mes données terrain - une capture d'écran de GSC, un chiffre daté, un verbatim de client, un test raté - donne un article que personne d'autre ne peut écrire.

Ma séquence, concrètement :

1.  Je rédige le plan et les **preuves** à la main : 5 à 8 puces de faits vécus, datés, chiffrés.
    
2.  L'IA développe chaque section à partir de ces puces, jamais à partir de rien.
    
3.  Je réécris moi-même les 150 premiers mots. Toujours. C'est là que se joue la voix.
    
4.  Je relis chaque phrase contenant un chiffre, une date, un nom d'outil ou une citation.
    

Le prompt de rédaction, avec les contraintes qui comptent :

```
Tu écris en français pour un lecteur qui gère un site WordPress en PME.
Plan imposé (ne pas modifier) + faits fournis ci-dessous (ne pas en inventer d'autres).
Interdits : statistiques non fournies, "à l'ère du numérique", "dans un monde où",
"il est crucial de", énumérations à rallonge, adjectifs creux.
Style : phrases courtes, verbes concrets, un exemple chiffré par section.
Si une information manque, laisse [À COMPLÉTER] au lieu d'inventer.
```

Le `[À COMPLÉTER]` est le détail qui change tout. Sans cette consigne, le modèle comble les trous avec du plausible. Avec elle, il me signale exactement où je dois travailler - et ça m'arrive encore 5 à 10 fois par article.

Sur la transparence, Google recommande d'expliquer l'usage de l'automatisation quand le lecteur peut se poser la question. Une ligne en fin d'article suffit, et ça ne coûte rien.

## Étape 4 : maillage interne et optimisation on-page

Un modèle ne connaît pas votre arborescence. Si vous ne lui donnez pas la liste de vos URL, il inventera des liens - et vous publierez des 404. Je commence donc par un export du sitemap et des titres, collé dans le prompt.

```
Voici mes 120 URL (URL + titre + cluster). Pour la page ci-dessous,
propose 3 liens internes sortants maximum, avec 3 ancres différentes chacune,
et 2 pages qui devraient pointer vers elle.
Règle : jamais d'ancre "cliquez ici" ni de titre exact répété. Justifie en 6 mots.
```

Ce que je vérifie ensuite, à la main : que la page cible existe vraiment, que l'ancre n'est pas déjà utilisée ailleurs, et qu'il n'y a pas de cannibalisation entre deux pages du même cluster. L'IA ne voit pas la cannibalisation, parce qu'elle ne voit pas vos positions réelles.

Côté on-page, les titres et les meta descriptions générés ont un défaut récurrent : ils se ressemblent tous, avec la même promesse et la même structure « X : le guide complet pour… ». J'en garde environ 70 % et je réécris le reste. Les balises alt, en revanche, sont un cas d'usage idéal : 40 images à décrire, c'est fastidieux et sans ego.

## Étape 5 : audit technique et suivi

Un crawl reste un crawl. Screaming Frog avec une clé API (OpenAI ou Gemini) permet de passer des prompts sur les données collectées : classer 3 000 titres par intention, repérer les pages trop courtes, rédiger des alt textes en série. Ce n'est pas un audit magique, c'est du post-traitement - mais sur 5 000 URL, ça remplace trois jours de tableur.

Le vrai terrain où l'**ia générative seo** me fait gagner des heures, c'est le code. Regex pour filtrer les requêtes de marque dans GSC, requêtes SQL sur l'export BigQuery, formules Looker Studio : je décris le besoin, je teste, je corrige. Je ne publie jamais un regex sans l'avoir fait tourner sur un échantillon et vérifié le compte de lignes retournées.

Pour le suivi, un chiffre à garder en tête : selon [Pew Research](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/) (900 adultes américains, mars 2025), un lien classique est cliqué dans 8 % des visites quand un résumé IA s'affiche, contre 15 % sans résumé. Le pattern à surveiller dans Search Console n'est donc plus « je baisse », mais **« impressions en hausse, clics stables »** - typique d'une requête captée par un AI Overview. Ça se mesure, ça ne se devine pas : je compare les segments de requêtes informationnelles et transactionnelles mois par mois, et je regarde les conversions assistées dans GA4 plutôt que le seul trafic.

## Les 5 erreurs qui plombent un SEO fait avec l'IA

1.  **Déléguer la stratégie à l'outil.** Une liste de 400 mots-clés sans intention ni page cible, c'est du bruit. L'outil propose, l'humain arbitre.
    
2.  **Confondre volume et autorité.** 200 pages générées en un week-end, c'est exactement le *scaled content abuse* décrit par Google. Dans l'étude Ahrefs, les pages 100 % IA sont 4,6 % du top 20, contre 81,9 % de pages hybrides : le modèle gagnant, c'est l'humain qui se sert de l'IA.
    
3.  **Laisser inventer des sources.** Une étude citée sans lien vérifiable est un risque juridique et un signal E-E-A-T négatif. Je clique sur chaque lien avant publication.
    
4.  **Uniformiser la voix.** Quand 30 articles commencent par « Dans le paysage numérique actuel », le lecteur comprend qu'il n'y a personne derrière. Une expérience de première main ne se génère pas.
    
5.  **Produire page par page.** Sans vue d'ensemble, on crée de la cannibalisation et on oublie le maillage. Chaque nouvel article doit renforcer une page existante.
    

## Mon stack IA pour le SEO

| Étape | Outil | Ce que je lui confie | Ce que je garde |
| --- | --- | --- | --- |
| Données mots-clés | DataForSEO, Semrush | Volumes, CPC, clusters | Priorisation, intentions |
| Analyse SERP | Chat classique + résultats collés | Angles morts, socle commun | Lecture du type de requête |
| Brief | Claude, ChatGPT | Structuration, questions à traiter | Preuves et angle |
| Rédaction | ChatGPT | Première version, reformulation | 150 premiers mots, faits, ton |
| Maillage | Screaming Frog + ChatGPT | Propositions d'ancres | Vérification URL et cannibalisation |
| Technique | Screaming Frog API, regex, SQL | Classification, requêtes | Tests et contrôles |
| Suivi | GSC, GA4, Looker Studio | Formules, commentaires de tendance | Diagnostic et décisions |

Un **chatgpt pour le seo** bien réglé, c'est un assistant qui exécute vite. Un **chatgpt seo** mal réglé, c'est une machine à produire du texte que personne ne cite. La différence ne tient pas au modèle choisi, elle tient au brief, aux données qu'on y met et au temps de relecture qu'on s'accorde.

## FAQ

**Faut-il déclarer qu'on utilise l'IA sur un article ?** Oui dès que le lecteur peut légitimement se poser la question, comme le recommande Google. Une phrase en bas de page sur la méthode de production suffit. Ce qui compte pour l'évaluation, c'est qui est responsable du contenu.

**Google pénalise-t-il les contenus écrits avec l'IA ?** Non. Google vise le contenu produit à grande échelle sans valeur ajoutée, quelle que soit la méthode. Une page utile, vérifiée, signée et sourcée se classe, même si un modèle a participé à sa rédaction.

**ChatGPT peut-il remplacer un rédacteur SEO ?** Il remplace la mise en forme et le premier jet, pas le jugement. Ce qui se vend aujourd'hui, ce n'est pas la production de texte - c'est la capacité à apporter une expérience, des données et un angle que le concurrent n'a pas.

**Quel outil SEO IA choisir pour commencer ?** Celui que vous avez déjà, plus un accès API. Un Semrush ou un DataForSEO pour les données, un chat pour la structuration, Screaming Frog pour le crawl : le reste est du confort. Le temps gagné vient du prompt, pas de l'abonnement.

## Sources utiles

-   Google Search Central - [Guidance on generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
    
-   Google Search Central - [Spam policies, scaled content abuse](https://developers.google.com/search/docs/essentials/spam-policies)
    
-   Google Search Central - [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
    
-   Google - [Search Quality Rater Guidelines (PDF)](https://services.google.com/fh/files/misc/hsw-sqrg.pdf)
    
-   Ahrefs - [AI-generated content and Google rankings](https://ahrefs.com/blog/ai-generated-content-does-not-hurt-your-google-rankings/)
    
-   Ahrefs - [76 % of AI Overview citations come from the top 10](https://ahrefs.com/blog/search-rankings-ai-citations/)
    
-   Pew Research Center - [Clicks when an AI summary appears](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/)
    

## Pour aller plus loin

Cette méthode, je l'enseigne en atelier à Lyon, sur des sites réels et des cas clients : le pilier comprendre le référencement naturel pose les fondations, et les prochaines dates de formation SEO et WordPress permettent de travailler votre propre workflow. Un audit SEO de 7 h suffit généralement à identifier les trois chantiers prioritaires ; la formation GA4 (3,5 h) sert ensuite à mesurer ce qui compte vraiment. Tout part de l'accueil du site, en présentiel à Lyon ou à distance.

## Spécifications de balisage

Bloc destiné à l'intégration technique - le JSON-LD complet est généré à la publication.

**Article**

-   `@type` : Article ; `headline` = titre H1 ; `description` = meta description ; `inLanguage` : fr-FR ; `datePublished` / `dateModified` au format ISO 8601.
    
-   `author` : référence `@id` vers le nœud Person ; `publisher` : Organization (nom, logo, URL).
    
-   `mainEntityOfPage` : URL canonique de l'article ; `image` : visuel principal 1200 × 630.
    

**Person (Nicolas Genaudet)**

-   `name`, `jobTitle` (« Formateur SEO et WordPress »), `url` (page profil auteur), `sameAs` (LinkedIn, site), `address` (Lyon, FR), `knowsAbout` (SEO, WordPress, Google Analytics 4, IA générative).
    

**FAQPage**

-   Un `Question` par interrogation de la section FAQ (4), avec `acceptedAnswer.text` reprenant la réponse visible, mot pour mot.
    
-   Aucune question ne doit apparaître dans le balisage sans être présente à l'écran.