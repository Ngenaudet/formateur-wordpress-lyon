# Cours Conception audio & vidéo

Ouvrir index.html dans un navigateur. La page fonctionne sans connexion et sans dépendances externes ; les liens de ressources nécessitent Internet.

## Contenu
- index.html : contenu du cours, modifiable dans un éditeur HTML.
- style.css : présentation et mise en page mobile/impression.
- app.js : recherche, navigation active, impression.
- assets/ : 77 diapositives originales en images.
- contenu-source.json : transcription du texte extractible, liens et numéros des 77 pages, pour de futures migrations. Les textes incorporés dans les images sont conservés visuellement et les principales infographies ont également une transcription dans la page.

Les doublons et intercalaires sont regroupés dans la lecture principale et tous conservés dans les originaux. Les corrections de mise en forme ne constituent pas une actualisation pédagogique. Les chiffres et exemples du PDF ne sont pas vérifiés. Les liens ne sont pas testés auprès des services externes.

## Intégration WordPress
Cette livraison est une page autonome préparatoire. Une protection par code partagé est ajoutée via PHP et `.htaccess`, sans compte étudiant. Pour l’intégration définitive, transférer le contenu dans une page WordPress ou un modèle de cours et charger style.css/app.js avec le thème ou une extension adaptée. Éviter de coller un document HTML complet dans le bloc HTML de WordPress.

Protéger la page ET les ressources du cours côté serveur avec le futur espace membres ; une image stockée dans les médias publics WordPress reste accessible par son URL même si la page est protégée. La balise noindex n’est pas un contrôle d’accès.

La page est ajoutée au dépôt dans cours/conception-audio-video/. Son URL après déploiement sera /cours/conception-audio-video/. La protection par code prendra effet après déploiement des fichiers PHP et du fichier caché `.htaccess`.
