# Conception audio & vidéo — version enrichie

53 slides en dix chapitres, dont 17 compléments. Les 77 diapositives originales sont conservées comme archives.

## Mettre à jour

Dans le dépôt, modifier `slides.json`, puis lancer `python3 scripts/build-course.py` depuis la racine. Ce script génère `index.html`. Les schémas sont éditables dans `scripts/course_visuals.py` ; les styles et interactions dans `style.css` et `app.js`.

`contenu-source.json` reste la transcription du PDF d’origine et ne doit pas être confondu avec le contenu révisé.

## Présenter

Le bouton « Lire en diaporama » affiche une slide à la fois. Les flèches gauche/droite et Page précédente/suivante changent de slide ; Début/Fin vont aux extrémités ; Échap ferme le diaporama. Sur petit écran, les slides longues restent défilables.

L’impression produit une version des slides sans la navigation et les archives.

## Déployer

Déployer tout le dossier, y compris le fichier caché `.htaccess`. PHP et les règles Apache protègent la page et ses ressources. Les JSON de travail et ce fichier ne sont pas servis par le contrôleur. Le code d’accès existant est conservé.

Voir l’audit complet dans `audits/audit-conception-audio-video-2026-10-27.md` à la racine du dépôt. Les points d’organisation dépendant de la classe restent à confirmer par le formateur.
