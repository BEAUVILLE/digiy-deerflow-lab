# DIGIY Orchestration V0.4 — atelier interne réutilisable

**Doctrine : pas d'API IA externe, pas de dépense, pas de publication automatique, lecture seule.**

## Nouvel apport réel
Le pilote analyse maintenant **plusieurs fichiers d'une même mission**, sans être limité au bloc WhatsApp :
- **Éclaireur** : inventaire, taille et empreinte SHA-256 du fichier réellement lu.
- **Technicien** : syntaxe Python (AST), JSON, JavaScript (Node `--check`, sans exécution du programme), ou sécurité basique des liens HTML.
- **Gardien** : signale certaines signatures de secrets, sans afficher les secrets dans le rapport ; ce contrôle n'est pas une certification de sécurité.
- **Spécialiste Voix** : réutilise le moteur V0.3 lorsqu'une cible HTML déclare explicitement `controle: voix`.
- **Contrôleur** : rassemble les constats, mais son verdict reste **« à vérifier »** même si tous les contrôles passent.

Le moteur ne fait ni appel réseau, ni écriture de source, ni paiement, ni envoi de message. Il refuse les demandes d'action, les missions payantes, les chemins sortant de la racine, les fichiers trop volumineux et les formats non pris en charge.

## Une mission réellement exécutée
La mission `mission_v04.json` a analysé **quatre fichiers réels du Lab** (Python, JS, JSON et le moteur V0.4 lui-même) : syntaxe valide et aucune signature de secret détectée sur ces fichiers. Il ne s'agit **pas** d'un audit de sécurité exhaustif.

Consulter `rapport_v04_resume.json`, construit à partir du rapport d'exécution locale. Les SHA des sources GitHub utilisées ont été comparés aux copies locales afin d'éviter une fausse validation.

## Reproduire sur un ordinateur disposant de Python 3 et Node
Depuis `experiments/orchestration-v0/` :

```sh
python3 orchestrateur_v04.py --mission mission_v04.json --racine .
python3 -m unittest -v test_orchestrateur_v04.py
python3 -m unittest discover -v -p 'test_*.py'
node --test test_*.mjs
```

Sans Node installé, un contrôle de syntaxe JavaScript est marqué `a_verifier`, jamais « conforme ». L'orchestrateur n'installe rien. Il ne lance pas le JavaScript analysé : Node ne fait qu'en vérifier la syntaxe.

## Résultats locaux du 15 novembre 2026
- V0.4 : **18/18 tests Python réussis**.
- V0.3 + V0.4 : **28/28 tests Python réussis**.
- Socle V0 : **6/6 tests Python réussis**.
- Relais et double contrôle V0.1–V0.2.1 : **22/22 tests Node réussis**.
- Tous ces tests ont été lancés localement, **pas dans la CI GitHub**.
- Aucune exécution de deux agents IA autonomes n'a été prouvée.

## Suite utile
Étendre les règles de contrôle aux contrats réels du projet et faire relire le rapport avant de corriger quoi que ce soit. Ne pas multiplier les frameworks. Ne pas fusionner cette PR brouillon sans feu vert explicite du MAÎTRE.

**Le terrain et le fondateur gardent la main.**
