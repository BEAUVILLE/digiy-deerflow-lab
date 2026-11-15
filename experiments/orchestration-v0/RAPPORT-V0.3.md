# DIGIY V0.3 — Notre système exécute une mission réelle en lecture seule

## Ce qui change

V0.2 comparait des paquets de test préremplis. **V0.3 reçoit un fichier HTML et calcule lui-même les observations**, grâce à trois travailleurs programmés :
- **Éclaireur** : lit les octets, produit l'empreinte SHA-256.
- **Technique** : reconnaît le bloc `voix-adherents`, vérifie le nombre de liens WhatsApp, leur forme, le texte prérempli et les protections des liens.
- **Langues** : repère les libellés visibles non raccordés à `data-i18n`.
- **Contrôleur** : rassemble les résultats et ne publie jamais.

Le test a utilisé **un extrait du HTML réel** de `BEAUVILLE/digiylyfe.com/index.html` lu via GitHub le 15 novembre 2026. L'extrait complet (qui comporte un numéro WhatsApp public) **n'a pas été ajouté au Lab**. Seul un rapport sans numéro a été enregistré.

## Résultat du passage sur le code existant

- 3 liens WhatsApp structurellement reconnus ;
- 1 `summary` ;
- 6 libellés visibles examinés, **6 sans `data-i18n`** ;
- réception WhatsApp / comportement iPhone **non testés** ;
- verdict contrôleur **À CORRIGER**, sans aucun changement de production.

Voir `rapport_v03_extrait.json`.

## Tests

```sh
cd experiments/orchestration-v0
python3 -m unittest -v test_orchestration_v03.py
# 10 tests réussis localement lors de la préparation
python3 orchestration_reelle_v03.py --source /chemin/vers/fichier.html
```

Le module utilise seulement la bibliothèque standard Python. Il n'effectue **aucune requête réseau**, n'installe rien, n'écrit pas dans le HTML et ne transmet pas les URL WhatsApp complètes dans son rapport.

## Limites et suite

Le travail a été véritablement exécuté sur du contenu du dépôt, mais les « travailleurs » sont des **fonctions déterministes**, pas des modèles IA indépendants. L'analyse statique ne prouve pas les traductions effectives, ni l'affichage navigateur, ni la réception WhatsApp.

Notre orchestrateur peut donc **avancer avec nos propres outils sans nouvel abonnement**. Une étape ultérieure pourra brancher un ou plusieurs modèles déjà accessibles, mais elle nécessitera une preuve explicite de leur exécution et un contrôle du coût.

Aucune fusion, publication, prise de contact ni dépense n'est autorisée par le présent pilote. La PR #1 reste en brouillon jusqu'au feu vert distinct du MAÎTRE.
