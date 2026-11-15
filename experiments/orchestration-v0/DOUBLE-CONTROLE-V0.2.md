# DIGIY V0.2 — Double contre-examen des sorties IA (interface prête)

Ce dossier complète V0/V0.1 dans la **même PR brouillon**, sans changement de production.

## Objectif
Deux agents IA distincts doivent pouvoir recevoir **le même sujet**, remettre des avis structurés indépendants, puis passer devant un contrôleur qui détecte contradictions, preuves absentes, demandes d'action et dépenses non autorisées. La provenance d'une sortie doit rester explicitement **non vérifiée** tant qu'aucune attestation externe n'existe.

## État démontré
- Code `confrontation_agents.mjs` pour comparer **deux sorties structurées**.
- Données `deux_sorties_SYNTHETIQUES.json` : **fictives, uniquement pour des tests de contrat**.
- Contrôles de cohérence exécutés en JavaScript : 16 assertions passées lors de la préparation ; code de tests Node joint pour la reproduction.
- **Aucun appel réel à un deuxième modèle IA ; aucune exécution d'agents IA indépendants prouvée.**

## Usage hors réseau
```sh
node lancer_confrontation.mjs deux_sorties_SYNTHETIQUES.json
node --test test_confrontation_agents.mjs
```

## Étape suivante (NON autorisée automatiquement)
Quand deux accès IA compatibles avec le budget zéro seront disponibles, remplacer la fixture par leurs réponses structurées : préciser `type_execution: modele_externe_non_verifie`, un `run_id` distinct, un `modele` déclaré, et les `preuve_ids` issus de sources authentifiées. **Attention** : un nom de modèle et deux IDs ne suffisent pas à prouver l'indépendance réelle ; cette validation exige un contrôle du contexte d'exécution ou une attestation du fournisseur.

Ne jamais exposer clés, données clients privées, WhatsApp personnels, PIN ou permissions de production aux modèles. Le laboratoire ne publie et ne contacte personne. Fusion uniquement après nouvelle validation expresse du MAÎTRE.
