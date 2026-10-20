# Créer un site WordPress avec IA : ce que ça change vraiment (et ce que ça ne remplace pas)

*Par Nicolas Genaudet, formateur WordPress à Lyon - mis à jour le 20 octobre 2026*

## En bref

On peut **créer un site WordPress avec IA** plus vite. Pas deux fois plus vite. Environ 40 % plus vite sur un site vitrine de cinq pages, et 0 % plus vite sur la recette et la mise en ligne.

Chiffres mesurés sur mes deux derniers projets comparables - même typologie, même nombre de pages, clients aussi exigeants : **42 heures sans IA, 25 h 30 avec**. Le reste de l'article explique où partent ces 16 h 30 et où l'IA ne sert strictement à rien.

Trois choses avant de lire la suite :

-   **L'IA excelle en amont.** Brief, arborescence, plan de page, premier jet de texte, bouts de CSS : c'est du travail de structuration, et elle le fait mieux que la page blanche.
    
-   **Elle échoue sur la preuve.** Vos chiffres, vos photos, vos clients, votre quartier, votre façon de refuser un devis. Tout ce qui rend un site crédible vient de vous.
    
-   **Le facteur limitant reste humain.** Validation client, arbitrage de périmètre, conformité RGPD, dernier kilomètre de recette.
    

Les pages « ia création site web wordpress » promettent toutes un site en dix minutes. J'en forme depuis huit ans à Lyon, et je n'ai jamais vu un site pro sortir en dix minutes. Voici le workflow réaliste, avec un verdict par étape.

!\[Capture - éditeur de site WordPress avec un thème bloc ouvert, annotations sur les réglages de styles globaux\]

## Ce que l'IA fait bien (et ce qu'elle ne fait pas) sur un site WordPress

Je sépare le débat utile du débat stérile. La question n'est pas « IA ou pas » : c'est « quel type de tâche ».

**Ce qu'elle fait bien, vraiment :**

-   Transformer trois pages de notes clients en brief structuré et en arborescence cohérente.
    
-   Proposer dix variantes de titres d'accroche en trente secondes - dont deux utilisables.
    
-   Rédiger le premier jet d'une page « Services », d'une FAQ, de mentions légales à trous.
    
-   Générer des méta-descriptions, des balises alt, des textes de boutons.
    
-   Écrire du CSS ciblé et des fonctions PHP courtes (filtres, custom post types) que je relis ensuite.
    
-   Expliquer un message d'erreur ou une erreur fatale PHP en langage clair.
    
-   Produire des scripts WP-CLI et des requêtes SQL pour du diagnostic.
    

**Ce qu'elle ne fait pas, malgré les promesses :**

-   Vérifier ses propres faits. Elle invente des tarifs, des noms, des dates avec un aplomb remarquable.
    
-   Connaître votre client. Le brief réel est dans un mail, un café, un coup de fil - pas dans un prompt.
    
-   Fournir des photos. Et un site vitrine sans photo réelle reste un site générique.
    
-   Choisir un plugin maintenu plutôt qu'un plugin abandonné en 2023.
    
-   Porter la responsabilité légale : RGPD, cookies, CGV, accessibilité. Cette responsabilité est la vôtre.
    
-   Assumer un parti pris graphique cohérent d'une page à l'autre.
    

Sur le référencement, la situation est plus simple qu'on ne le dit. Google est explicite depuis février 2023 : [le mode de production du contenu n'est pas le sujet](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content), ce qui compte est l'utilité réelle et l'originalité. La limite est ailleurs, dans la [politique sur les contenus produits à grande échelle](https://developers.google.com/search/blog/2024/03/core-update-spam-policies) mise à jour en mars 2024 : publier cinquante pages creuses sur cinquante variantes de requêtes, c'est du spam, avec ou sans IA.

**Verdict de cette partie :** l'IA WordPress est un accélérateur de production. Ce n'est ni un rédacteur, ni un chef de projet, ni un photographe.

## Étape 1 : cadrer le projet avec l'IA

C'est la partie où le gain est le plus net, et où personne ne l'attend.

Mon prompt de cadrage tient en huit lignes. Je le colle à chaque nouveau projet, avec les notes brutes de l'entretien client :

> « Tu es chef de projet web. Voici mes notes d'entretien avec un menuisier à Villeurbanne : \[notes\]. Produis : 1) trois personas avec leurs objections d'achat, 2) une arborescence de 5 pages maximum justifiée page par page, 3) pour chaque page, l'objectif, l'action attendue et les preuves à collecter, 4) les dix questions que je dois encore poser au client. »

Ce qui sort n'est pas parfait. Mais ce qui sort fait apparaître **les trous dans mon propre brief**, et ça, aucune méthode de mon classeur ne le faisait aussi vite. La liste « questions à poser » est systématiquement la plus rentable.

Deux garde-fous que j'ai appris à la dure :

-   **Ne jamais envoyer le brief généré au client tel quel.** Il contient des invraisemblances (délais, périmètres techniques) qu'un client un peu technique repérera.
    
-   **Garder l'arbitrage.** L'IA propose cinq pages ; c'est moi qui décide qu'on jette la page « Équipe » parce qu'elle sera vide.
    

**Verdict :** excellent. C'est là que se joue la moitié du gain de temps total. Comptez 2 heures au lieu de 5.

## Étape 2 : générer la structure et les contenus

Pour créer un site WordPress de A à Z, la structure se pose avant le design. L'IA y est bonne : plan de page, hiérarchie Hn, ordre des sections, liste des preuves à afficher.

Le contenu, c'est autre chose. Ma règle, après avoir testé les deux extrêmes : **60/40**. L'IA produit 60 % du texte - les paragraphes explicatifs, les transitions, les réponses aux objections courantes. J'écris les 40 % restants, qui sont exactement ceux qu'aucun modèle ne peut inventer : un chantier livré en mars, un devis type, deux avis clients recopiés, un délai réel, une contrainte de quartier.

Le symptôme du contenu 100 % IA, je l'entends en formation : « Nous sommes passionnés par notre métier et attachés à la satisfaction de nos clients. » Vrai pour tout le monde, donc utile à personne. Sur trois sites clients l'an dernier, les pages que j'ai le plus retravaillées étaient celles que le client avait générées seul avant de m'appeler.

À faire par l'IA sans état d'âme : méta-descriptions, balises alt, libellés de formulaire, textes de boutons, FAQ structurées, versions courtes pour les réseaux.

À ne jamais déléguer : les témoignages, les chiffres, les mentions légales définitives, les tarifs. Un tarif inventé par un modèle et publié, c'est une réclamation client la semaine suivante.

!\[Capture - page WordPress avec paragraphes surlignés en deux couleurs : généré par IA en bleu, réécrit à la main en orange\]

**Verdict :** bon pour la structure et le squelette rédactionnel, moyen pour le texte final, nul pour la preuve.

## Étape 3 : construire le site

Trois familles d'outils, trois usages très différents.

**Les thèmes blocs (recommandé).** Avec un thème bloc type Twenty Twenty-Five, tout passe par l'éditeur de site : en-tête, pied de page, gabarits. La [documentation officielle sur les thèmes blocs](https://wordpress.org/documentation/article/block-themes/) est claire et suffisante. Le plugin officiel [Create Block Theme](https://learn.wordpress.org/lesson/use-the-create-block-theme-plugin-for-exports-and-theme-variations/) permet de figer vos réglages dans des fichiers de thème et d'exporter un ZIP : c'est le pont entre « je bricole dans l'éditeur » et « je livre un thème propre au client ».

**Les builders.** Elementor AI et Divi AI génèrent des sections entières à partir d'une phrase. Le résultat est visuellement correct et alourdit sérieusement la page. Sur un site de cinq pages destiné à du référencement local, je reste sur des blocs natifs. Sur une landing page jetable, un builder généré fait le travail.

**Le plugin IA WordPress.** Le bon choix dépend de l'usage, pas du classement :

-   **Rank Math Content AI** pour la production SEO dans le flux éditorial (titres, méta, suggestions).
    
-   [**AI Engine**](https://wordpress.org/plugins/ai-engine/) pour tout le reste : chatbot, résumés, génération d'images, connexion à votre propre clé API.
    
-   **Fluent Forms + un peu de JS** pour les formulaires : l'IA n'apporte rien ici.
    

Pour un **chatbot IA WordPress**, AI Engine est le point de départ le plus sain : le plugin est gratuit, vous branchez votre clé OpenAI et vous payez à l'usage, sans marge du plugin. La version Pro démarre autour de 59 $/an. Deux précautions : fixez un plafond de dépense côté fournisseur, et limitez la longueur de contexte, sinon la facture grimpe sur un site à fort trafic. Un comparatif utile existe chez [WPFormation](https://wpformation.com/plugins-ia-wordpress-2026/).

### Ce que les promesses d'IA création de site web WordPress ne disent pas

Les générateurs intégrés (WordPress.com, Hostinger, SeedProd) produisent un site **présentable** en quelques minutes. Présentable n'est pas publiable. Ce qui manque au bout de dix minutes : les vraies photos, les bons numéros de téléphone, un choix de plugins assumé, la conformité cookies, et surtout une structure pensée pour une intention de recherche. C'est un bon point de départ pour un client pressé, pas un livrable.

**Verdict :** moyen. L'IA aide sur le CSS, les variations de styles et les gabarits. Elle ne décide pas de l'architecture, et c'est l'architecture qui fait la différence entre un site qui vieillit bien et un site à refaire dans dix-huit mois. 16 heures → 11 heures.

## Étape 4 : SEO et performance

L'IA propose des clusters de mots-clés et un maillage interne cohérent en quelques secondes. Sur ce point, elle est meilleure que la plupart des tableurs que j'ai vus circuler.

Elle ne sait pas juger l'intention. Exemple concret : le terme « créer un site wordpress avec ia » ne pèse que 20 recherches mensuelles en France, quand « wordpress ia » en fait 210. Un outil IA va vous recommander de tout miser sur le second. Mauvaise lecture : le premier attire des gens qui vont acheter une formation ou un accompagnement, le second attire des curieux. Le volume n'est pas la valeur.

Sur la performance, aucune surprise. Les seuils des [Core Web Vitals](https://developers.google.com/speed/docs/insights/v5/about) n'ont pas bougé : **LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1**, évalués au 75ᵉ percentile des visites réelles, mobile et ordinateur séparément. Ce que l'IA ne fera pas à votre place :

-   Désactiver les scripts des extensions inutiles, dont les plugins IA chargés de widgets.
    
-   Compresser et mettre en cache correctement. Pour ça, [WP Rocket](https://wp-rocket.me/google-core-web-vitals-wordpress/) fait le travail.
    
-   Choisir un hébergement qui ne plombe pas le temps de réponse serveur.
    

Ce que l'IA fait bien : lire un rapport PageSpeed et proposer un ordre de priorité. C'est déjà beaucoup.

**Verdict :** moyen. Bonne pour la liste de contrôle et la structure de contenu, inutile pour l'arbitrage et pour les serveurs. 5 heures → 3 heures.

## Étape 5 : ce qui doit rester humain

Le dernier kilomètre. C'est 10 % du temps et 90 % de la valeur perçue :

-   **La recette client.** Cliquer chaque lien, tester le formulaire sur un vrai téléphone, vérifier que le mail de contact arrive. L'IA ne reçoit pas les mails.
    
-   **L'accessibilité.** Contrastes réels, navigation au clavier, alternatives textuelles justes. Un modèle produit des alt plausibles, pas des alt exacts.
    
-   **Le RGPD et les cookies.** Finalités, durées, registre, bandeau conforme. C'est de la responsabilité, pas de la génération.
    
-   **Les photos.** Une demi-journée de prises de vue transforme un site correct en site crédible.
    
-   **La formation du client.** Une heure à montrer l'admin, les sauvegardes et la mise à jour des extensions évite six mois de dépendance.
    
-   **Les décisions de périmètre.** Dire non poliment à « juste une page en plus » - ça reste mon métier.
    

**Verdict :** 100 % humain. Et c'est tant mieux : c'est ce que le client paie réellement.

!\[Capture - liste de contrôle de mise en ligne sur deux colonnes, avec cases cochées à la main\]

## Combien de temps ça fait vraiment gagner ?

Site vitrine de 5 pages, accompagnement client compris :

| Étape | Sans IA | Avec IA | Gain | Verdict |
| --- | --- | --- | --- | --- |
| 1\. Cadrage, brief, arborescence | 5 h | 2 h | −3 h | Excellent |
| 2\. Rédaction des 5 pages | 12 h | 6 h | −6 h | Bon, sous conditions |
| 3\. Design et build (thème bloc) | 16 h | 11 h | −5 h | Moyen |
| 4\. SEO technique et performance | 5 h | 3 h | −2 h | Moyen |
| 5\. Mise en ligne, recette, RGPD | 4 h | 3 h 30 | −30 min | Nul |
| **Total** | **42 h** | **25 h 30** | **−16 h 30 (−39 %)** |  |

39 %, pas 80 %. Et ce chiffre dépend d'une condition unique : **vous devez déjà savoir ce que vous faites**. L'IA accélère un professionnel et noie un débutant, parce qu'elle produit du plausible - pas du correct. En formation, les stagiaires qui gagnent le plus de temps sont ceux qui avaient déjà construit dix sites à la main.

Pour aller plus loin, je forme sur ces sujets à Lyon : la formation « Créer un site WordPress » (21 heures, du brief à la mise en ligne) et la formation « Gérer un site WordPress » (7 heures) pour la maintenance et la sécurité. Le catalogue Pilot'in propose des modules IA de 7 à 35 heures pour ceux qui veulent aller sur les usages avancés. Et pour le reste de mon approche, voir la page formateur WordPress à Lyon.

## FAQ

### Peut-on créer un site WordPress avec IA sans savoir coder ?

Oui, pour un site vitrine simple. Blocks natifs, thème bloc, un formulaire, un plugin SEO : ça se fait sans une ligne de code. Dès qu'il y a un besoin métier spécifique (réservation, extranet, catalogue filtré), il faut soit du code, soit une extension payante bien choisie - et cette décision-là demande de l'expérience.

### L'IA nuit-elle au référencement d'un site WordPress ?

Non, pas en soi. Google évalue l'utilité et l'originalité, pas la méthode de production. Ce qui pénalise, c'est de publier en masse des pages creuses sur des variantes de requêtes, ou d'empiler trente pages génériques avec un plugin IA WordPress sans relecture. Une page utile, même assistée par IA, se classe très bien.

### Quel plugin IA WordPress choisir pour un site professionnel ?

Un seul au départ, et celui qui correspond à votre usage : Rank Math Content AI pour l'optimisation SEO dans l'éditeur, AI Engine pour un chatbot ou des usages sur mesure avec votre propre clé API. Empiler trois extensions IA est le meilleur moyen d'ajouter du JavaScript inutile et 400 ms de LCP.

### Combien coûte un chatbot IA WordPress en fonctionnement ?

Le plugin peut être gratuit, l'IA jamais tout à fait. Vous payez les tokens à votre fournisseur, à l'usage. Pour un chatbot de support sur un site de PME, la facture mensuelle reste souvent sous les 10 à 15 €, à condition de plafonner la longueur des réponses et d'activer une limite de dépense. Le coût réel, c'est le temps de rédaction de la base de connaissances.

## Sources utiles

-   [Google Search's guidance about AI-generated content](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content) - février 2023
    
-   [Google core update et politique sur les contenus à grande échelle](https://developers.google.com/search/blog/2024/03/core-update-spam-policies) - mars 2024
    
-   [Thèmes blocs - documentation WordPress.org](https://wordpress.org/documentation/article/block-themes/)
    
-   [Create Block Theme : exporter un thème bloc](https://learn.wordpress.org/lesson/use-the-create-block-theme-plugin-for-exports-and-theme-variations/)
    
-   [AI Engine - plugin WordPress.org](https://wordpress.org/plugins/ai-engine/)
    
-   [Plugins IA WordPress : comparatif WPFormation](https://wpformation.com/plugins-ia-wordpress-2026/)
    
-   [PageSpeed Insights et données de terrain](https://developers.google.com/speed/docs/insights/v5/about)
    
-   [Core Web Vitals pour WordPress - WP Rocket](https://wp-rocket.me/google-core-web-vitals-wordpress/)
    

## Spécifications de balisage (à implémenter au gabarit)

Bloc de spécifications pour l'intégration, sans JSON-LD complet :

**1\.** `Article` **(ou** `BlogPosting`**)**

-   `headline` : titre H1 exact
    
-   `description` : méta-description
    
-   `datePublished` / `dateModified` : 20 octobre 2026
    
-   `inLanguage` : `fr-FR`
    
-   `author` : `@id` → `#nicolas-genaudet`
    
-   `publisher` : `@id` → `#organisation`
    
-   `mainEntityOfPage` : URL canonique de l'article
    
-   `image` : capture d'écran principale, 1200 × 630
    
-   `articleSection` : « WordPress »
    
-   `keywords` : créer un site wordpress avec ia, ia wordpress, plugin ia wordpress, chatbot ia wordpress, créer un site wordpress de a à z
    

**2\.** `Person` (id `#nicolas-genaudet`)

-   `name` : Nicolas Genaudet
    
-   `jobTitle` : Formateur WordPress
    
-   `description` : formateur WordPress à Lyon, 8 ans de pratique
    
-   `address` → `PostalAddress` : Lyon, FR
    
-   `worksFor` : `@id` → `#organisation`
    
-   `sameAs` : LinkedIn, profil public
    
-   `knowsAbout` : WordPress, thèmes blocs, SEO local, accessibilité
    

**3\.** `FAQPage`

-   4 entités `Question` / `Answer`, alignées mot pour mot sur la section FAQ
    
-   `acceptedAnswer.text` : réponse complète, texte brut, sans lien
    

**4\. Cohérence à vérifier avant publication :** une seule entité `FAQPage` par page, `Person` référencée par `@id` et non dupliquée, `Organization` déclarée une seule fois sur le site.