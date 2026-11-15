# Relais de missions entre rôles — DIGIY V0.1

**Status : pilote documenté et logique de validation testée ; aucun agent IA autonome n'est branché.**

Cette couche complète le pilote V0 sans le remplacer. Elle **n'écrit rien** dans le site, dans Supabase ou ailleurs. Elle consomme uniquement des paquets JSON préparés séparément ; elle n'envoie aucun message, n'appelle aucune API IA et n'exécute aucune commande externe.

## Ordre de transmission

MAÎTRE (mission en lecture seule) → Éclaireur (faits GitHub) → Technique (structure) → Langues (traductions) → Contrôleur (verdict consolidé, **sans pouvoir de publication**).

Les sorties doivent identifier leur `recu_de`, leur rôle, leurs références de preuve, les inconnues, et déclarer zéro action et zéro dépense. Une preuve ne peut être attribuée au mauvais spécialiste. Les références sont issues d'un catalogue **manuel** ; leur présence ne prouve pas à elle seule la véracité d'une affirmation d'un modèle IA.

## Essais reproductibles (Node.js local, sans dépendance)

```sh
node run_relais.mjs mission_relais_001.json
node --test test_relais_agents.mjs
```

Le jeu d'essai porte sur la PR DIGIYLYFE #204. Ce sont des **faux paquets d'agents saisis pour le test de contrat**, pas des résultats d'agents autonomes. Une intégration à de véritables modèles exige ultérieurement des identités d'agent, une isolation des permissions, une validation indépendante des sources, une politique de coût et l'accord explicite du MAÎTRE.

## État actuel

- Le protocole détecte l'écart de langue, les éléments WhatsApp non testés et les comptes rendus incomplets.
- Tests de logique exécutés dans l'environnement de développement avant écriture GitHub ; tests Node enregistrés pour exécution dans un environnement Node disponible.
- La PR #1 reste **brouillon non fusionné**. Pas de push manuel supplémentaire requis : cette branche reçoit les nouveaux fichiers.
- **Ni CI GitHub ni vrais agents IA ni téléphone n'ont été vérifiés ici.**
