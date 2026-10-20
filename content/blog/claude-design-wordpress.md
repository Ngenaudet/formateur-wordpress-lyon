# Claude Design tuto : produire une maquette de site WordPress

**Par Nicolas Genaudet**, formateur WordPress et UX/UI à Lyon.

*\[PHOTO - portrait de Nicolas Genaudet, à insérer en haut de l'article. Format 4:5, lumière naturelle, écran de maquette en arrière-plan flou.\]*

Ce tuto fait une seule chose : vous emmener d'un brief de site WordPress à une maquette validée, puis à un handoff réellement utilisable. Comptez deux heures pour une page d'accueil complète. Je l'ai chronométré la semaine dernière sur un site de cabinet d'architectes à Villeurbanne : 1 h 50, brief inclus, cinq sections, deux allers-retours client.

Pas de vitrine théorique ici. Vous trouverez les prompts que j'utilise, les réglages qui changent vraiment le résultat, et ce que je refuse de laisser faire à l'IA.

## En bref

-   **Claude Design** génère une maquette éditable sur un canevas, à partir d'une conversation : vous décrivez, il construit, vous corrigez au chat, au commentaire ou à la souris.
    
-   L'étape qui décide de tout n'est pas le prompt, c'est le **brief + le design system importé** (couleurs, typo, composants). Bâclé, vous refaites tout à la main.
    
-   On itère **section par section** : hero, preuve sociale, tarifs, FAQ. Jamais « refais toute la page ».
    
-   Le handoff vers WordPress passe par **theme.json** (les design tokens), des **patterns** et **ACF** pour ce que le client doit éditer.
    
-   Aucun export Figma natif à ce jour : le pont se fait par **HTML autonome**, ou en important votre fichier Figma comme *système de design* en amont.
    

* * *

## À quoi sert Claude Design quand on construit un site WordPress

Claude Design est un mode de Claude qui associe une conversation à un canevas. Vous le lancez depuis n'importe quelle conversation, depuis l'onglet **Artifacts**, depuis **Claude Code** avec `/design`, ou sur mobile. Il est inclus dans les plans Free, Pro, Max, Team et Enterprise. Point d'attention : la version autonome sur `claude.ai/design` ferme le **14 décembre 2026**, il faut donc basculer vos projets dans Claude avant cette date.

En pratique, sur un projet WordPress, il sert à quatre choses.

**Trouver la direction visuelle sans ouvrir Photoshop.** Trois variantes de hero en dix minutes, comparables côte à côte. Sur un site vitrine, c'est souvent là que se joue la validation client.

**Produire du contenu structuré, pas du faux texte.** C'est le gain que je n'attendais pas. Un hero avec un vrai titre, un vrai sous-titre, une vraie accroche de preuve sociale : on discute de la formulation avant de discuter de pixels.

**Vérifier la hiérarchie avant Gutenberg.** Une page qui tient debout en maquette tiendra debout en blocs. Une page qui dépend de trois colonnes imbriquées et d'un dégradé vous coûtera deux jours de `theme.json`.

**Aligner le client sur du concret.** Un canevas partageable vaut mieux que trois réunions.

Ce qu'il ne fait pas, et c'est important de le dire : il ne produit pas de HTML WordPress, pas de blocs Gutenberg natifs, pas de champs personnalisés, et il n'a **pas encore d'historique de versions**. Ce dernier point a des conséquences concrètes que je détaille plus bas.

**Claude design exemple** : la page d'accueil d'un artisan électricien, 6 sections, palette reprise de son camion, un seul appel à l'action « Demander un devis ». Un brief de 12 lignes a suffi.

## Préparer le brief : ce qui fait la différence

La documentation Anthropic est claire : une bonne invite contient l'**objectif**, la **mise en page**, le **contenu** et l'**audience**. Sur un site WordPress, j'y ajoute une couche : les contraintes de production. Voilà mes quatre blocs.

### Le contexte

Huit lignes, pas plus. Activité, zone géographique, objectif unique de la page, nombre de pages prévues, ce qui existe déjà (URL, logo, photos), qui éditera le site après livraison, hébergeur et type de thème visé.

### Les personas

Deux maximum. Pour chacun : une phrase de douleur, un critère de décision, un canal d'arrivée (Google, recommandation, Instagram). Si vous en mettez cinq, la maquette devient tiède. La règle « un persona principal, un secondaire » m'a jamais trahi.

### Les contraintes

Techniques d'abord : thème bloc, six couleurs maximum, typographies auto-hébergées, pas de police Google en direct (RGPD), images en 16:9, cible 90+ sur Lighthouse mobile. Éditoriales ensuite : longueur des textes, preuve sociale réellement disponible (avis Google ? nombre de chantiers ?), langues.

### Le design system

C'est le levier le plus sous-estimé. Claude Design accepte un système de design créé à partir de **fichiers Figma**, d'une base de code, d'un deck ou de logos et palettes. En bêta sur Pro, Max, Team et Enterprise. Si votre design system vit dans du code React, `/design-sync` depuis Claude Code lit directement vos tokens et vos composants.

Conseil de terrain : ne demandez pas « des couleurs sobres ». Donnez `#1F3A5F`, `#E8E2D9`, une échelle d'espacement en 4 px. Et nommez les composants comme en production (« Bouton principal », « Carte témoignage »), parce que vous les retrouverez dans le code.

> **Prompt de brief (à copier tel quel)** « Tu conçois la page d'accueil d'un site WordPress pour un cabinet d'architectes à Lyon. Objectif unique : générer une demande de rendez-vous. Audience : particuliers propriétaires d'appartements haussmanniens, 40-60 ans, sensibles à la lumière et au patrimoine. Sections imposées : hero, 3 réalisations, méthode en 4 étapes, 2 témoignages, FAQ (4 questions), bloc prise de rendez-vous. Contraintes : thème bloc, 6 couleurs max (palette ci-jointe), typo serif pour les titres, sans-serif pour le corps, mobile 390 px et desktop 1440 px. Style : sobre, éditorial, beaucoup de blanc, photos plein cadre. Pas de dégradés, pas d'ombres portées, pas d'illustrations 3D. »

## Étape 1 : générer la première maquette

1.  **Créez un projet** et vérifiez que le design system de l'organisation est bien actif. Un projet hérite automatiquement des couleurs, polices et composants.
    
2.  **Joignez les ressources** : logo, captures de l'existant, deux ou trois sites de référence, photos disponibles.
    
3.  **Collez le brief** ci-dessus, en une seule fois.
    
4.  **Demandez desktop d'abord**, 1440 px, plan de travail par section, nommés « 01 - Hero », « 02 - Réalisations »…
    
5.  **Demandez deux variantes** de la section hero avant de valider quoi que ce soit. « Montre-moi deux directions différentes pour le hero, pas deux ajustements. »
    
6.  **Demandez les plans de travail mobile** seulement après validation du desktop. Sinon vous itérez deux fois.
    

*\[CAPTURE 1 - Le canevas Claude Design après la première génération : plans de travail numérotés à gauche, panneau Propriétés à droite. Capture personnelle, projet cabinet d'architectes.\]*

Premier constat systématique : la structure est bonne, le détail typographique est approximatif. C'est normal. Ne corrigez pas le détail ici, ça vient à l'étape 2.

## Étape 2 : itérer sur les sections

La règle : **le chat pour la structure, les commentaires en ligne pour le micro-réglage, le canevas pour le visuel**. Et une section à la fois. « Refais toute la page en plus moderne » produit une régression garantie sur les sections qui marchaient.

### Le hero

Ce que je demande : un titre de moins de 9 mots, un sous-titre qui dit à qui ça s'adresse, un CTA principal unique, une image qui prouve le métier. Puis je fais vérifier le contraste : Claude peut auditer l'accessibilité et les rapports de contraste de sa propre sortie.

> « Réduis le titre à 7 mots maximum. Supprime le bouton secondaire. Agrandis la photo pour qu'elle occupe la moitié droite, bord à bord. Le CTA garde la couleur d'accent. »

### La preuve sociale

Deux formats suffisent : trois logos ou trois témoignages courts avec prénom, ville et un chiffre. Demandez des citations ancrées, pas des « Super travail ! ». Un bon témoignage contient un avant/après mesurable.

### Les tarifs

Le piège classique : trois colonnes identiques avec une seule pastille « Populaire ». Demandez plutôt deux formules et une ligne « sur devis », avec le prix en gros et les inclusions en liste à sept items maximum. Sur WordPress, ça se traduit par un pattern avec une grille, pas par un tableau.

### La FAQ

Quatre questions maximum, formulées avec les mots du client, pas ceux du métier. Demandez à Claude de générer les questions à partir du brief, puis relisez : il invente des objections que personne ne se pose.

*\[CAPTURE 2 - Vue commentaires en ligne : une note ancrée sur le bouton du hero, panneau de discussion ouvert à gauche. Capture personnelle.\]*

Astuce : si vos commentaires n'apparaissent pas sur le canevas, collez-les dans le chat. C'est un bug intermittent connu, et c'est le workaround officiel.

## Étape 3 : passer de la maquette à WordPress

C'est là que 80 % des tutos s'arrêtent. Voilà ma chaîne, dans l'ordre.

### Passer par Figma ou pas

Soyons précis sur **Claude Design Figma** : il n'existe **aucun export** `.fig` **natif** aujourd'hui. Les exports disponibles sont le `.zip`, le PDF, le PPTX, Google Slides, le HTML autonome, plus l'envoi vers Canva, Wix, Netlify, Vercel, v0, Lovable, HubSpot ou Miro, et le transfert vers Claude Code.

Deux options, donc :

-   **Import HTML** vers Figma via un outil type html.to.design ou Anima. Rapide, mais vous récupérez des calques à nettoyer : prévoyez une heure par page et ne comptez pas sur des auto-layouts propres.
    
-   **Reconstruction dans Figma** si le client exige un fichier source exploitable par son équipe. Dans ce cas, ne repartez pas de zéro : importez votre fichier Figma existant comme système de design dans Claude Design, la maquette sortira déjà alignée sur la bibliothèque.
    

Mon avis : pour un site vitrine WordPress, Figma ne sert que si quelqu'un d'autre doit reprendre le fichier. Sinon, c'est un détour.

### Le thème bloc et les tokens

Le vrai handoff, c'est `theme.json`. Chaque couleur de la maquette devient un preset, chaque taille de titre une entrée `fontSizes`, chaque espacement une `spacingSizes`. Vous nommez, le client hérite, et vous ne touchez plus au CSS.

```json
{
  "settings": {
    "color": { "palette": [
      { "slug": "encre", "color": "#1F3A5F", "name": "Encre" },
      { "slug": "sable", "color": "#E8E2D9", "name": "Sable" }
    ]},
    "typography": { "fluid": true, "fontSizes": [
      { "slug": "display", "size": "clamp(2.5rem, 5vw, 4rem)", "name": "Display" }
    ]}
  }
}
```

La typographie fluide (`fluid: true` + `clamp()`) règle 90 % du responsive sans media query. C'est aussi le meilleur moyen de tenir la promesse d'une maquette mobile fidèle à ce qui sortira en production.

### Les patterns

Une maquette validée = une bibliothèque de patterns. Un fichier par section dans `/patterns/`, avec un en-tête qui déclare le titre et les catégories. Les blocs synchronisés pour les éléments répétés (bandeau CTA, carte contact). Résultat : le client insère « Hero - Cabinet », pas 40 blocs à remonter.

*\[CAPTURE 3 - Éditeur WordPress, écran d'insertion de patterns : la catégorie « Accueil » affiche les cinq patterns issus de la maquette. Capture personnelle, thème bloc.\]*

### Les champs avec ACF

Tout ce qui change souvent sort dans ACF : titre et sous-titre du hero, réglages du CTA, réitérateur de témoignages, lignes de tarifs, questions de FAQ. Pour les sections complexes, j'utilise **ACF Blocks** : le gabarit PHP reprend le markup de la maquette, les champs deviennent des contrôles dans l'éditeur. Un client qui change son hero sans appeler personne, c'est ça, le handoff réussi.

## Claude Design vs Figma : ce que je garde de chacun

| Critère | Claude Design | Figma |
| --- | --- | --- |
| Première piste exploitable | 15-20 min, brief en langage naturel | Plusieurs heures, tout à la main |
| Bibliothèque de composants | Système de design importé (bêta), moins strict | Référence du marché : instances, variantes, variables |
| Design tokens | Extrait et applique ; pas de fichier de tokens propre | Variables, modes, export via plugins |
| Responsive | À demander explicitement, approximatif | Auto-layout et contraintes, précis au pixel |
| Handoff développeur | HTML autonome, `.zip`, transfert vers Claude Code | Dev Mode, inspection, specs |
| Collaboration client | Partage, commentaires ; édition multi-personnes basique | Robuste, historique de versions |
| Coût | Inclus dans l'abonnement Claude | Sièges payants, à partir d'une quinzaine d'euros par éditeur |

Ce que je garde : **Claude Design pour explorer, Figma pour figer.** Exploration = trois directions, du contenu réel, un client qui réagit vite. Figement = composants, tokens, versions, une équipe qui travaille dessus pendant six mois.

## Les erreurs à éviter

-   **Partir sans design system.** La maquette sera jolie et impossible à reproduire en `theme.json`. Deux heures perdues, à chaque fois.
    
-   **Compter sur l'historique de versions.** Il n'existe pas encore. Dupliquez le projet avant chaque changement de direction, ou dites : « Sauvegarde ce que nous avons et essaie une approche complètement différente. »
    
-   **Demander du code WordPress directement.** Vous obtiendrez du HTML statique, pas des blocs. Le passage par patterns + ACF reste votre travail.
    
-   **Valider une maquette sans les vrais textes.** Un titre de 4 mots en `lorem ipsum` devient un pavé illisible une fois le contenu client livré.
    
-   **Oublier le mobile jusqu'à la fin.** Demandez les plans de travail 390 px avant la validation, pas après.
    
-   **Confondre rapidité et finition.** La sortie de Claude n'est pas accessible par défaut : contrastes, tailles de cible, ordre des titres. Faites-lui auditer, puis vérifiez vous-même.
    

## FAQ

### Claude Design peut-il générer un thème WordPress complet ?

Non. Il produit une maquette et du HTML statique. Le thème bloc (templates, `theme.json`, patterns) s'écrit ensuite, à la main ou avec Claude Code. La maquette fait gagner la phase de conception, pas le développement.

### Comment passer une maquette Claude Design vers Figma ?

Il n'y a pas d'export `.fig`. Exportez en HTML autonome puis importez via html.to.design ou Anima, en prévoyant un nettoyage des calques. L'inverse fonctionne nativement : un fichier Figma peut servir à créer votre système de design dans Claude Design.

### Faut-il un abonnement payant pour utiliser Claude Design ?

Claude Design est disponible dès le plan Free, avec les mêmes limites d'usage que le reste de Claude. En pratique, un projet complet avec plusieurs itérations consomme vite le quota : les plans Pro ou Max sont plus confortables. Les systèmes de design sont en bêta sur Pro, Max, Team et Enterprise.

### Claude Design remplace-t-il un designer UX/UI ?

Il remplace la phase de production de pistes, pas le jugement. Hiérarchie de l'information, accessibilité, cohérence du design system, choix de ce qu'on met dans un pattern ou dans ACF : c'est là que se joue la qualité. L'outil accélère, il ne tranche pas.

## Sources utiles

-   [Commencer avec Claude Design - Centre d'aide Anthropic](https://support.claude.com/fr/articles/14604416-commencer-avec-claude-design)
    
-   [Configurer votre système de design dans Claude Design](https://support.claude.com/fr/articles/14604397-configurez-votre-systeme-de-design-dans-claude-design)
    
-   [Claude Design - page produit](https://claude.com/fr/product/design)
    
-   [Introduction à theme.json - WordPress Developer Resources](https://developer.wordpress.org/themes/global-settings-and-styles/introduction-to-theme-json/)
    
-   [Theme.json Reference - Block Editor Handbook](https://developer.wordpress.org/block-editor/reference-guides/theme-json-reference/)
    
-   [ACF - documentation officielle](https://www.advancedcustomfields.com/resources/)
    

* * *

## Spécifications de balisage (à implémenter au publish)

**Article** - `headline` = H1 ci-dessus ; `description` = méta description ; `datePublished` / `dateModified` au format ISO 8601 ; `author` → référence au nœud `Person` ; `image` = photo de l'auteur (1200×1200) ; `inLanguage` = `fr-FR` ; `articleSection` = « Tutoriels WordPress ».

**Person** - `name` = « Nicolas Genaudet » ; `jobTitle` = « Formateur WordPress et UX/UI » ; `address` (Lyon, FR) ; `knowsAbout` = WordPress, thème bloc, UX/UI, Figma, accessibilité ; `sameAs` = profil LinkedIn + page profil du site ; `image` = portrait.

**HowTo** - `name` = « Produire une maquette de site WordPress avec Claude Design » ; `totalTime` = `PT2H` ; 4 `HowToStep` alignés sur les H2 « Préparer le brief », « Étape 1 », « Étape 2 », « Étape 3 » (chaque `url` pointe vers l'ancre de section) ; `tool` = Claude Design, WordPress, ACF ; `supply` = brief, design system, palette.

**FAQPage** - 4 `Question` / `Answer` reprenant exactement les 4 H3 de la section FAQ. Note : depuis août 2023, Google n'affiche plus d'étoiles FAQ pour la plupart des sites ; gardez le balisage pour la sémantique et les moteurs génératifs, pas pour le SERP.

**Maillage** : les liens internes vers l'accueil, la page formations UX/UI et la page formations WordPress se posent sur les ancres « formateur WordPress et UX/UI à Lyon », « formations UX/UI » et « formations WordPress ». Ne pas imbriquer `HowTo` et `FAQPage` deux fois sur la même URL.

**CTA de fin d'article** : *Envie de construire la chaîne complète - maquette, thème bloc, patterns, ACF - plutôt que de bricoler seul ? Mes formations WordPress et UX/UI se donnent à Lyon et à distance, en petit groupe.*