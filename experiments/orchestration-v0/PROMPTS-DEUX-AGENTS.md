# DIGIY V0.2 — Deux analyses IA distinctes : protocole d'essai manuel (non exécuté)

**Important :** ce document ne lance aucun agent, ne crée aucun compte, ne dépense rien et n'envoie aucune donnée. Il prépare une comparaison future à budget zéro.

## Entrée commune aux deux agents
- Mission : DIGIY-ORCH-001, lecture seule.
- Périmètre : [PR #204, La Voix des adhérents](https://github.com/BEAUVILLE/digiylyfe.com/pull/204) et [index.html du site](https://github.com/BEAUVILLE/digiylyfe.com/blob/main/index.html).
- Faits initiaux datés du 15 novembre 2026 : PR #204 fusionnée ; un seul fichier modifié, `index.html` ; ajout d'un élément `<details id="voix-adherents">` ; trois liens WhatsApp ; libellés du bloc ajoutés en français sans attribut `data-i18n` ; test de réception WhatsApp sur téléphone non confirmé.
- **Les sources ci-dessus sont des références de consultation, pas des preuves indépendantes des affirmations fournies.** Chaque agent doit signaler ses limites d'accès et la vérification restant à faire.
- Exclusions : pas de clé API, PIN, accès propriétaire, numéro privé, données Supabase, contact externe ni modification GitHub.
- But : déterminer si le bloc respecte les parcours multilingues et la promesse WhatsApp, sans inventer de test mobile.

## Agent A — analyseur
Instruction à fournir dans une session indépendante :

> Tu es l'analyseur de DIGIYLYFE. N'exécute aucune action. Examine uniquement le périmètre et les faits fournis. Donne un état pour I18N_VOIX et WHATSAPP_RECEPTION parmi "conforme", "a_corriger", "inconnu". Pour chaque état, indique les références du catalogue VOIX_HTML ou PR204 et une note factuelle. Ne prétends pas avoir testé un téléphone, WhatsApp ou une langue si tu ne l'as pas réellement fait. Retourne uniquement les champs attendus pour une entrée de `sorties` dans `deux_sorties_SYNTHETIQUES.json`, en remplaçant l'agent_id par "analyseur", le run_id par un identifiant d'exécution réel distinct, `type_execution` par "modele_externe_non_verifie", `modele` par ton nom exact vérifié, `actions_demandees` par [], et `cout_demande` par 0. Si tu ne peux pas garantir ton nom ou le coût, ne remplis pas le rapport : indique l'incertitude.

## Agent B — contre-auditeur
Instruction à fournir **dans une autre session sans consulter la réponse d'A** :

> Tu es le contre-auditeur indépendant de DIGIYLYFE. Tu reçois les mêmes faits qu'un premier analyseur, sans accès à ses conclusions. Cherche d'abord ce qui manque pour prouver les affirmations, notamment la traduction réelle, le comportement WhatsApp et les validations sur téléphone. Pour I18N_VOIX et WHATSAPP_RECEPTION, réponds avec "conforme", "a_corriger" ou "inconnu" et des références VOIX_HTML ou PR204. Ne présente jamais une supposition comme un test effectué. Retourne uniquement les champs attendus pour une entrée de `sorties` dans `deux_sorties_SYNTHETIQUES.json`, avec `agent_id` "contre_auditeur", ton véritable run_id distinct, `type_execution` "modele_externe_non_verifie", `modele` authentiquement connu, `actions_demandees` [], `cout_demande` 0. Si le coût ou la provenance ne peuvent pas être garantis, stoppe.

## Contrôle après réception
1. Conserver le même catalogue des sources et le même périmètre pour les deux analyses.
2. Remplacer le fichier de fixture par un nouveau JSON d'essai local, jamais le fichier intitulé `SYNTHETIQUES`.
3. Exécuter `node lancer_confrontation.mjs <nouveau_fichier.json>`.
4. Tout désaccord devient `a_arbitrer`. Une inconnue reste ouverte. Une concordance n'autorise jamais une publication.
5. Faire une relecture humaine indépendante des références : deux run_id différents ne prouvent pas l'indépendance réelle des modèles.
6. Conserver les résultats **hors production**, aucun merge sans feu vert.

**Aucun essai réel avec deux fournisseurs/modèles n'a été effectué dans cette PR.**
