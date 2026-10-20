# Claude Code WordPress : ce que ça change vraiment sur un projet client

**Par Nicolas Genaudet**, formateur WordPress, UX-UI et SEO à Lyon · Mis à jour le 20 octobre 2026 · 9 min de lecture

!\[Photo de l'auteur à insérer : portrait de Nicolas Genaudet devant son écran, en situation de formation\]

## En bref

Claude Code WordPress, c'est utiliser un agent qui vit dans ton terminal : il lit ton dépôt, écrit les fichiers, lance `wp` et `composer lint`, puis te montre un `git diff`. Sur un projet client réel (thème enfant + plugin sur mesure + audit d'un site hérité), ça m'a fait gagner environ un tiers du temps de production PHP - et zéro minute sur la partie design.

Ce qu'il ne fait pas : il ne connaît pas ton client, il n'ouvre pas ton navigateur à ta place, et il oublie régulièrement les `current_user_can()`. Trois garde-fous non négociables : revue humaine ligne par ligne, PHPCS + Query Monitor, et aucun push en prod sans passage par un staging.

Voilà le détail, avec les prompts et les blocs de code que j'ai réellement utilisés.

## Ce que Claude Code change (et ne change pas) pour un dev WordPress

La bascule n'est pas « de l'autocomplétion en mieux ». Elle est ailleurs.

Un assistant classique complète la ligne que tu es en train d'écrire. Claude Code prend une **tâche** : « ajoute un CPT `témoignage` avec une taxonomie, une page d'admin et les templates associés ». Il ouvre les fichiers concernés, crée ce qui manque, enregistre les hooks, lance `wp rewrite flush --hard`, et te rend la main avec une liste de changements.

Concrètement, ce qui change dans mon quotidien de développement WordPress :

-   **La cartographie d'un codebase inconnu.** Il lit 40 fichiers PHP en deux minutes et me sort l'arbre des hooks. Avant, c'était une demi-journée de `grep`.
    
-   **Les tâches répétitives multi-fichiers.** Déclarer un CPT, son bloc d'admin, ses colonnes de liste, ses capabilities : le genre de chose où je fais une faute de frappe toutes les trois lignes.
    
-   **Le contexte persistant.** Un fichier `CLAUDE.md` bien écrit remplace trois paragraphes de rappel à chaque conversation. Ça, c'est le vrai gain.
    
-   **Les scripts jetables.** Migrer 600 meta `_prix` en `_bf_prix` ? Il écrit le script WP-CLI, je le relis, je le lance en local.
    

Et ce qu'il ne change pas - c'est la partie que les vidéos YouTube oublient :

-   **La sécurité reste ton problème.** Il produit du code plausible qui *a l'air* sûr. Un nonce manquant reste un nonce manquant, même quand il est écrit dans un joli fichier bien indenté.
    
-   **Le contexte exotique.** ACF Pro, un thème premium qui fait des choses bizarres, un plugin métier des années 2015 : il ne les connaît pas. Il invente une API crédible.
    
-   **Le goût.** La hiérarchie visuelle, le choix d'une typo, la pertinence d'un parcours d'inscription : rien de tout ça ne sort d'un terminal.
    
-   **Le debug infra.** OPcache, WAF, timeout PHP, un certificat intermédiaire manquant. Là, tu es seul.
    

Une nuance importante : la qualité de sortie dépend directement de la qualité de ton brief. « Fais-moi un plugin de réservation » donne du code générique. Un brief avec la version de PHP, le text domain, les capabilities et le format de réponse attendu donne du code utilisable. C'est un changement de métier : on passe de tapeur de code à rédacteur de spécifications.

## Installer et configurer Claude Code pour un projet WordPress

La configuration, c'est le vrai tutoriel Claude Code : tout se joue là. Un agent mal cadré produit du code hors sujet pendant que tu brûles des jetons.

**Installation.** Sur macOS, Linux ou WSL, l'installeur natif se met à jour tout seul :

```bash
curl -fsSL https://claude.ai/install.sh | bash
# ou : brew install --cask claude-code
claude --version
```

**Le répertoire de travail.** Erreur n°1 : lancer `claude` à la racine de WordPress. Tu traînes 2 000 fichiers de core dans le contexte et tu doubles le bruit. Je me place dans le dossier que je modifie : `cd wp-content/plugins/bf-annuaire`.

**Le** `CLAUDE.md`**.** Lance `/init` une fois, puis réécris le fichier à la main. Le mien ressemble à ça :

```markdown
# Projet : plugin « Annuaire Clients » - client Bouchon & Fils

## Environnement
- WordPress 6.8, PHP 8.2, MySQL 8, local via wp-env
- Thème parent : Blocksy 2.x + ACF Pro 6.x (ne jamais remplacer par des meta natives)
- Préfixe global : `bf_` - namespace `Bouchon\Annuaire` - text domain `bf-annuaire`

## Règles de code
- WordPress Coding Standards obligatoires (PHPCS, ruleset WordPress)
- Tabs, jamais d'espaces. `array()` long, jamais `[]`.
- Une classe par fichier, nommage `class-bf-<nom>.php`
- Chaque lecture/écriture de données passe par une capability check explicite
- Sortie toujours échappée : esc_html, esc_attr, esc_url, wp_kses_post
- Entrée toujours `wp_unslash()` + sanitize. Aucun `$_POST` brut.

## Commandes utiles
- `composer lint` → PHPCS
- `wp plugin list --status=active` → état réel des plugins
- `wp rewrite flush --hard` après tout changement de rewrite

## Interdits
- Ne jamais modifier `wp-config.php`, `.htaccess`, `wp-content/uploads`
- Ne jamais toucher au thème parent
- Pas de `git push`, pas de `wp db` sauf `wp db export` en local
```

**Les permissions.** Dans `.claude/settings.json`, j'autorise les lectures et j'interdis les gestes irréversibles :

```json
{
  "permissions": {
    "allow": ["Bash(wp plugin list:*)", "Bash(composer lint:*)", "Bash(git diff:*)"],
    "deny": ["Bash(git push:*)", "Bash(wp db reset:*)", "Bash(rm -rf:*)"]
  }
}
```

**Le Plan Mode.** `Shift+Tab` jusqu'à « plan », ou `claude --permission-mode plan`. Il explore, propose un plan, n'écrit rien. Tu valides, ou tu édites le plan avec `Ctrl+G`. Pour tout ce qui touche plus de trois fichiers, je ne travaille plus autrement.

**Les commandes maison.** Un fichier par tâche dans `.claude/commands/` : `/audit-secu`, `/maj-pot`, `/revue-diff`. Trois lignes de Markdown qui te font gagner dix minutes par jour.

!\[Capture à insérer : terminal Claude Code en Plan Mode, avec un plan de refactoring affiché et le curseur sur « Accept plan »\]

## Cas d'usage 1 : créer un plugin WordPress sur mesure

Claude Code plugin WordPress personnalisé : c'est le premier test que j'ai fait, et celui qui m'a convaincu.

Le projet : un endpoint REST qui expose les fiches clients du CPT `client`, pour un back-office React maison. Avant de lancer quoi que ce soit, `wp scaffold plugin bf-annuaire --plugin_author="Nicolas Genaudet"` pour avoir une base propre, puis ce prompt :

```text
Contexte : ./wp-content/plugins/bf-annuaire
Tâche : ajouter un endpoint REST GET /bf/v1/clients qui renvoie la liste paginée du CPT "client".
Contraintes :
- permission_callback obligatoire, capability "edit_posts"
- args validés via validate_callback + sanitize_callback
- réponse via WP_REST_Response, pagination exposée dans X-WP-Total
- aucune requête SQL directe, uniquement WP_Query
- code conforme WPCS, tabs, text domain bf-annuaire
Avant d'écrire : propose un plan (fichiers touchés + signatures), attends mon OK.
```

Il m'a rendu quatre fichiers et un diff propre. J'ai corrigé trois choses, et elles sont instructives :

1.  `permission_callback` **en** `__return_true`**.** Il savait que je voulais `edit_posts`, il a mis la version qui « fonctionne quand on teste ».
    
2.  `sanitize_text_field()` **sur un tableau.** Un tableau de meta, passé dans une fonction qui attend une chaîne.
    
3.  `'posts_per_page' => -1`**.** La valeur par défaut de tout ce qui ressemble à une liste, et l'assurance de faire exploser la mémoire dans six mois.
    

Le squelette final, celui que je garde comme gabarit :

```php
add_action( 'admin_post_bf_save_client', 'bf_save_client' );

function bf_save_client() {
	if ( ! current_user_can( 'edit_posts' ) ) {
		wp_die( esc_html__( 'Action non autorisée.', 'bf-annuaire' ) );
	}

	check_admin_referer( 'bf_save_client', 'bf_nonce' );

	$name = isset( $_POST['bf_name'] )
		? sanitize_text_field( wp_unslash( $_POST['bf_name'] ) )
		: '';

	update_post_meta( absint( $_POST['post_id'] ), '_bf_name', $name );

	wp_safe_redirect( add_query_arg( 'bf_saved', '1', wp_get_referer() ) );
	exit;
}
```

Résultat : 2 h 30 au lieu de 5 h estimées, 280 lignes livrées, dont 40 % que j'ai réécrites. Les règles de sécurité et de validation viennent toujours de la doc officielle du Plugin Handbook - [Common issues](https://developer.wordpress.org/plugins/wordpress-org/common-issues/) est la page que je fais lire à l'agent en début de session.

## Cas d'usage 2 : refactoriser un thème enfant

Le contexte : un thème enfant de 2019, un `functions.php` de 912 lignes, quatorze fonctions préfixées `my_`, et un CSS chargé deux fois. Le client voulait ajouter un module de blog ; j'ai refusé de poser une brique dessus.

J'ai demandé une cartographie avant tout refactoring, en lecture seule : « liste chaque fonction de functions.php, son hook, et ce qu'elle modifie ». Puis j'ai attaqué par lots, un objectif par commit.

Ce qu'il a produit de vraiment bon : l'extraction en quatre fichiers `inc/` avec un autoload manuel, et cette version de l'enqueue - là où le thème enfant chargeait son CSS sans dépendance, donc dans le désordre :

```php
add_action( 'wp_enqueue_scripts', 'bf_enqueue_child_styles' );

function bf_enqueue_child_styles() {
	$parent_handle = 'parent-theme-style'; // handle réel du thème parent
	$path          = get_stylesheet_directory() . '/style.css';

	wp_enqueue_style(
		'bf-child',
		get_stylesheet_uri(),
		array( $parent_handle ),
		(string) filemtime( $path ) // cache-busting à chaque déploiement
	);
}
```

La [doc officielle des thèmes enfants](https://developer.wordpress.org/themes/advanced-topics/child-themes/) insiste d'ailleurs sur ce point : vérifie d'abord comment le parent charge ses styles, chaque thème fait différemment.

Ce qu'il a raté : il a supprimé `my_redirect_after_login()`. Elle n'était appelée nulle part dans le thème… mais un plugin de fidélisation la rappelait par `function_exists()`. Deux heures de perte sur un staging. Depuis, j'ajoute systématiquement dans le prompt : « avant de supprimer une fonction, cherche son nom dans tout `wp-content`, y compris les plugins ».

Bilan : `functions.php` passé de 912 à 178 lignes, quatre fichiers dans `inc/`, aucune régression fonctionnelle détectée en recette.

!\[Capture à insérer : git diff avant/après du functions.php, avec le compteur de lignes -912/+178 visible\]

## Cas d'usage 3 : audit et revue de code d'un site existant

C'est l'usage le plus sous-estimé. Le site d'un client, repris d'une agence, avec un plugin custom de 12 fichiers PHP que personne n'avait relu depuis trois ans.

Le prompt, en lecture seule :

```text
Mode lecture seule. Ne modifie aucun fichier.
Périmètre : ./wp-content/plugins/accroche-custom (12 fichiers PHP).
Pour chaque fichier, signale :
1. entrées non validées (superglobales)
2. sorties non échappées
3. requêtes SQL non préparées (hors $wpdb->prepare)
4. absence de current_user_can / check_admin_referer sur les actions
5. points de performance : WP_Query en -1, meta_query non indexée, absence de cache
Sortie : tableau markdown trié par sévérité (critique / majeur / mineur),
avec fichier:ligne et correctif en une phrase.
```

Sortie : 3 critiques, 9 majeurs, 14 mineurs. Les trois critiques étaient réels - un `$_GET` passé directement dans une requête, une action AJAX sans nonce, un `echo` d'une option non échappée. Le genre de chose qu'un audit manuel laisse filer après deux heures de lecture.

Ce qu'il ne voit pas, en revanche : une faille dans un plugin tiers, un XSS stocké alimenté par une option enregistrée ailleurs dans le site, une mauvaise configuration serveur. L'agent ne regarde que ce que tu lui donnes.

D'où la combinaison que j'impose maintenant sur tout audit :

-   **PHPCS avec le ruleset WordPress Coding Standards** - la référence est la page [PHP Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/), et l'outillage officiel est sur [WordPress-Coding-Standards](https://github.com/WordPress/WordPress-Coding-Standards).
    
-   [**Query Monitor**](https://wordpress.org/plugins/query-monitor/) pour les requêtes lentes, les doublons et les hooks réellement déclenchés. Un agent ne peut pas te dire qu'une requête met 800 ms ; Query Monitor, si.
    
-   `git diff` **relu ligne par ligne.** Pas de « ça a l'air bon ». 22 lignes sur un audit de cette taille cachent facilement une régression.
    

## Claude Code vs Cursor : lequel pour WordPress ?

C'est la question la plus tapée des deux en France - 480 recherches mensuelles pour « claude code vs cursor », contre 70 pour « claude code wordpress » (données DataForSEO, octobre 2026). Et la réponse courte est : ce ne sont pas les mêmes outils, donc pas les mêmes moments.

|  | Claude Code | Cursor |
| --- | --- | --- |
| **Interface** | Terminal | Éditeur (fork de VS Code) |
| **Où il travaille** | Tout le dépôt, exécute des commandes | Les fichiers ouverts, plus un contexte projet |
| **Point fort sur WordPress** | Multi-fichiers, WP-CLI, scripts de migration, audits | CSS, templates, retouche visuelle, diff côte à côte |
| **Validation des changements** | `git diff` en terminal | Accepter / refuser bloc par bloc |
| **Boucle test-réflexion** | Lance PHPUnit ou PHPCS et corrige seul | Possible, moins naturel |
| **Mon usage réel** | Plugin custom, refactoring, audit | Intégration d'une maquette, ajustements de design |

En pratique, je vis dans les deux. Claude Code pour tout ce qui dépasse un fichier et touche au PHP métier ; Cursor quand je dois voir le rendu d'une grille CSS et arbitrer à l'œil. Rien n'empêche de lancer Claude Code dans le terminal intégré de Cursor, c'est même ce que je fais la moitié du temps. La comparaison médiatisée autour de « l'un va tuer l'autre » ne résiste pas à une journée de vrai travail.

Un point que personne ne mesure dans ces comparatifs : le coût cognitif. Déléguer à un agent en terminal demande une discipline de brief. Rester dans un éditeur qui propose demande une discipline de refus. Ce n'est pas la même fatigue en fin de journée.

## Les pièges que j'ai rencontrés

Sept, dans l'ordre de gravité décroissante.

1.  **La confiance sur la sécurité.** Il oublie `current_user_can()`, il met `__return_true` dans un `permission_callback`, il échappe une sortie HTML avec `esc_html()` au lieu de `wp_kses_post()`. À chaque session. La checklist de revue, c'est moi qui la porte, pas lui.
    
2.  **La fonction inventée.** `wp_get_post_terms_by()` n'existe pas. Ça compile visuellement, ça casse à l'exécution. Réflexe : vérifier chaque fonction inconnue sur [developer.wordpress.org](https://developer.wordpress.org/).
    
3.  **Le contexte pollué.** Laisse-le lire tout `wp-content`, et il te proposera des solutions basées sur un plugin que tu as désactivé en 2023. Périmètre serré, toujours.
    
4.  **Le refactor trop large.** « Nettoie ce plugin » donne 40 fichiers modifiés et un diff illisible. Règle : un commit, un objectif, un diff relisible en trois minutes.
    
5.  **Le CSS qui marche mais casse la DA.** Il produit du CSS valide et générique. Le rendu est propre, et complètement à côté de la charte.
    
6.  **Le secret dans le contexte.** Un `wp-config.php` dans le répertoire de travail, et les identifiants de base partent dans la conversation. Je sors le fichier, systématiquement.
    
7.  **La prod.** Jamais. `git`, staging, sauvegarde, et un humain qui appuie sur le bouton. C'est le garde-fou que je refuse de déléguer, même pour un fix d'une ligne.
    

**Passer à la pratique.** Si tu veux apprendre à cadrer ce genre d'outil sur un vrai projet, plutôt que de collectionner des démos, notre formation **« Créer un site WordPress »** (21 h, Lyon ou à distance) couvre la chaîne complète : environnement local, thème enfant, plugin maison, mise en ligne. Les bases de PHP et de sécurité qu'on y pose sont exactement celles qui manquent à l'agent. Toutes nos formations WordPress à Lyon sont en petit groupe, avec un vrai site de A à Z - c'est le format le plus efficace pour prendre les bons réflexes de revue.

!\[Capture à insérer : session de formation WordPress à Lyon, participants devant un terminal et un back-office\]

## FAQ

**Claude Code peut-il créer un plugin WordPress complet de A à Z ?** Oui pour le squelette, non pour la livraison. Il génère la structure, les hooks, l'admin, les endpoints en quelques minutes. Il rate systématiquement une partie des contrôles de capacité, de nonce et de validation, et il invente parfois des fonctions. Un plugin publiable demande encore une relecture humaine complète.

**Claude Code remplace-t-il un développeur WordPress ?** Non. Il déplace le travail : moins de frappe, plus de spécification et de revue. Sur mon projet, le temps de production PHP a baissé d'environ un tiers, mais le temps d'analyse et de test n'a pas bougé - c'est lui qui garantit que le code est juste.

**Ça fonctionne avec ACF, WooCommerce ou un thème premium ?** Partiellement. Il connaît les API publiques les plus courantes, pas les hooks spécifiques d'un thème commercial ni les versions exactes installées chez toi. La parade : pointer les fichiers du plugin dans le prompt, coller les signatures de fonctions concernées, et lui interdire explicitement de remplacer une meta ACF par du `post_meta` brut.

**Faut-il savoir coder pour l'utiliser sur WordPress ?** Pour du prototypage, non. Pour de la production, oui. Un agent qui produit du code plausible est plus dangereux pour quelqu'un qui ne peut pas l'évaluer que pas d'agent du tout. C'est précisément pour ça que je commence toujours mes formations WordPress par les bases de PHP et la logique de sécurisation.

## Sources utiles

-   [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) - la boucle explorer / planifier / implémenter / vérifier
    
-   [How Claude remembers your project](https://code.claude.com/docs/en/memory) - `CLAUDE.md`, auto-mémoire, `/memory`, `/context`
    
-   [Configure permissions](https://code.claude.com/docs/en/permissions) - allow / deny, hooks `PreToolUse`
    
-   [Quickstart Claude Code](https://code.claude.com/docs/en/quickstart) - installation et `/init`
    
-   [WordPress PHP Coding Standards](https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/) - le ruleset PHPCS de référence
    
-   [Common issues - Plugin Handbook](https://developer.wordpress.org/plugins/wordpress-org/common-issues/) - nonces, sanitize, escape
    
-   [Child Themes - Theme Handbook](https://developer.wordpress.org/themes/advanced-topics/child-themes/) - chargement des styles du parent
    
-   [wp scaffold plugin - WP-CLI](https://developer.wordpress.org/cli/commands/scaffold/plugin/) - base de plugin propre
    
-   [Query Monitor](https://wordpress.org/plugins/query-monitor/) - requêtes, hooks, erreurs PHP
    

## Spécifications de balisage (intégration)

*Bloc de specs à destination de l'intégrateur. Le JSON-LD complet est généré au publish.*

`Article` - `headline` = titre H1 · `description` = meta description · `datePublished` = 2026-10-20 · `dateModified` = 2026-10-20 · `inLanguage` = `fr-FR` · `author` → référence `#person` · `publisher` → Organization du site · `mainEntityOfPage` → URL canonique · `image` → image d'en-tête 1200 × 630 · `about` → `SoftwareApplication` (Claude Code), `WordPress` · `keywords` = claude code wordpress, claude code plugin wordpress, claude code tutoriel, claude code vs cursor, développement wordpress.

`Person` (`@id` = `#person`) - `name` = Nicolas Genaudet · `jobTitle` = Formateur WordPress, UX-UI et SEO · `address` → Lyon, France · `worksFor` → site formateur · `image` → portrait de l'auteur · `sameAs` → LinkedIn + GitHub · `knowsAbout` = WordPress, PHP, UX-UI, SEO, Claude Code.

`FAQPage` - `mainEntity` avec 4 `Question` / `Answer`, en reprenant mot pour mot les 4 questions de la section FAQ. Chaque réponse limitée au premier paragraphe.

**À ne pas baliser** : pas de `HowTo` (les cas d'usage sont des retours d'expérience, pas un protocole unique), pas d'`AggregateRating`, pas de `SoftwareApplication` en entité principale - Claude Code est cité comme sujet, pas comme produit évalué. Validation finale dans le Rich Results Test avant mise en ligne.