# DIGIY — Pilote d'orchestration V0 (branche d'essai)

**Statut : expérimentation en lecture seule. Aucun déploiement.**

## Pourquoi ici ?
Réutiliser **DIGIY Master** (doctrine) et **DIGIY DeerFlow Lab** (atelier). Ne pas créer de produit autonome ni toucher au CORE, au site public, aux données des professionnels ou à Supabase.

## Comment ça marche ?
Le pilote reçoit une mission strictement en lecture seule et un **jeu de faits déjà vérifiés**. Il distribue ces faits à trois contrôles indépendants :

- Éclaireur : état de la PR et périmètre ;
- Technique : structure des liens et vérifications terrain manquantes ;
- Langues : présence de marqueurs de traduction ;
- Contrôleur : synthèse, sans outrepasser les statuts des spécialistes.

Le code est **déterministe**, sans appel IA, sans réseau, sans clé, sans installation de dépendance. Ce n'est **pas** un orchestrateur multi-agent autonome. C'est un contrat de délégation testable et un premier passage réel sur la PR #204.

## Essai local
Depuis ce dossier :

    python3 orchestrateur.py --mission mission_001.json --faits faits_001.json
    python3 -m unittest discover -v -s . -p 'test_*.py'

Le rapport attendu est enregistré dans rapport_001.json pour comparaison. La mission doit montrer **la traduction à corriger** et **la réception WhatsApp impossible à vérifier** sans téléphone.

## Restrictions de sécurité
- actions_autorisees doit être une liste vide ; type doit être lecture_seule ; budget supplémentaire zéro.
- Pas d'écriture sur GitHub, pas d'envoi WhatsApp, pas de fusion, pas de publication, pas d'appel réseau ni de données privées.
- Aucune décision du MAÎTRE n'est présumée. Les échecs et informations manquantes restent visibles.
- Les faits sont une photographie manuelle datée, pas une synchronisation temps réel.
- Le code n'a pas été branché sur un moteur d'agents IA. Une phase ultérieure nécessiterait une autorisation distincte et des tests d'isolation.

## Critère de réussite
Un seul rapport compréhensible rassemble des contrôles spécialisés, souligne un écart réel, conserve les inconnues et ne peut exécuter aucune mutation.

## Références
- [DIGIY Master — doctrine](https://github.com/BEAUVILLE/digiy-master/blob/main/AGENTS.md)
- [DeerFlow Lab — doctrine](https://github.com/BEAUVILLE/digiy-deerflow-lab/blob/main/doctrine-digiy-deerflow.md)
- [PR #204 — La Voix des adhérents](https://github.com/BEAUVILLE/digiylyfe.com/pull/204)
