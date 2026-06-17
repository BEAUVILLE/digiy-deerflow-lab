# DIGIY DeerFlow Lab

**DIGIY DeerFlow Lab** est un atelier privé pour préparer, ranger, vérifier et améliorer les supports terrain de DIGIYLYFE.

Ce dépôt n’est pas la vitrine publique.
Ce dépôt n’est pas la production.
Ce dépôt n’est pas le cerveau qui décide à la place du terrain.

Il sert à préparer les cartouches proprement, avant validation humaine.

---

## Vision

DIGIYLYFE reste la route simple du terrain :

```txt
voix → intention → fiche → QR → contact direct → paiement direct
```

DeerFlow reste en arrière-atelier :

```txt
idée → brouillon → structuration → vérification → support terrain → validation humaine
```

La règle est claire :

> DeerFlow prépare dans l’atelier.
> DIGIY structure et valide.
> Le terrain décide.

---

## Doctrine centrale

Dans DIGIYLYFE, l’abonné ou le professionnel renseigne ses propres données.

Pourquoi ?

Parce que lui seul connaît réellement :

* son nom public ;
* son métier ;
* ses zones d’intervention ;
* ses services ;
* ses horaires ;
* son contact public ;
* ses photos ;
* ses limites ;
* ses disponibilités ;
* sa manière de travailler.

DeerFlow ne doit pas inventer une fiche à la place du pro.

DeerFlow peut seulement aider à :

* structurer les informations ;
* clarifier un texte ;
* repérer les oublis ;
* préparer un message WhatsApp ;
* préparer une phrase QR ;
* préparer un pitch court ;
* préparer une checklist ;
* mettre en forme un support terrain.

---

## Règle photos

Les photos doivent être renseignées uniquement sous forme d’URL.

Aucune photo ne doit être stockée directement dans le Lab.

Format recommandé :

```txt
photo_url: "https://..."
gallery_urls:
- "https://..."
- "https://..."
- "https://..."
```

Les URLs doivent être publiques, propres, accessibles et validées par le professionnel.

---

## Mission du Lab

Le Lab sert à produire rapidement :

```txt
modèles de fiches métiers
checklists de validation
pages HTML de démonstration
offres commerciales souples
messages WhatsApp
scripts terrain
packs QR
dossiers partenaires
textes de prospection
supports pour recruter des pros
```

Première cible :

# Club des Métiers du Terrain — Saly

Objectif : préparer un pack simple pour recruter 10 professionnels terrain à Saly.

---

## Ce que le Lab peut faire

### 1. Préparer un modèle de fiche métier

Exemples :

```txt
plombier à Saly
maçon à Mbour
chauffeur AIBD
coiffeuse à Saly
soins beauté à domicile
location appartement Petite Côte
```

Le Lab ne remplace pas la saisie du professionnel.

Sortie attendue :

```txt
structure de fiche
champs à remplir
règles de validation
message WhatsApp préparé
phrase QR
pitch oral
contrôle sécurité
```

### 2. Préparer une page HTML

Le Lab peut préparer une page statique simple, lisible sur téléphone, pour une porte ou une campagne.

Exemples :

```txt
club-metiers-saly.html
fiche-modele-artisan.html
qr-chauffeur-aibd.html
page-offre-terrain.html
```

### 3. Préparer un message WhatsApp

Exemple :

```txt
Bonjour, je viens depuis DIGIYLYFE.
Je cherche un plombier à Saly.
Besoin : petite intervention.
Moment : à préciser.
Merci de me répondre quand disponible.
```

### 4. Préparer un script terrain

Exemple :

```txt
Bonjour grand, je vous montre une chose simple.
Le client scanne le QR, il voit votre fiche, il vous écrit directement.
Pas de commission sur votre travail. Pas d’application compliquée. Vous gardez la main.
```

### 5. Préparer une checklist

Le Lab peut aider à vérifier :

```txt
données validées par le pro
contact public validé
photos en URL seulement
lien testé
QR testé
texte clair
pas de donnée sensible
pas de promesse excessive
```

---

## Ce que le Lab ne doit jamais faire

```txt
ne jamais toucher la production
ne jamais publier seul
ne jamais utiliser les clés Supabase privées
ne jamais stocker de données clients sensibles
ne jamais exposer les téléphones complets dans un fichier public non validé
ne jamais publier un contact sans accord du professionnel
ne jamais stocker les photos directement dans le dépôt
ne jamais inventer les données d’un pro
ne jamais remplacer la décision humaine
ne jamais complexifier la vitrine DIGIYLYFE
```

Si une idée rend la rue plus compliquée, elle sort du Lab.

---

## Structure du dépôt

```txt
digiy-deerflow-lab/
├── README.md
├── index.html
├── doctrine-digiy-deerflow.md
├── skills/
│   ├── fiche_metier_terrain.md
│   └── pack_qr_commercial.md
├── inputs/
│   ├── modules_digiy.json
│   └── exemples_terrain.md
├── outputs/
│   ├── fiches/
│   ├── pages/
│   ├── offres/
│   ├── flyers/
│   └── scripts_com/
└── tests/
    └── checklist_validation.md
```

---

## Doctrine d’écriture

DIGIYLYFE ne vend pas du rêve abstrait.
DIGIYLYFE donne une route visible aux professionnels du terrain.

Les mots doivent rester :

```txt
simples
humains
courts
locaux
utiles
vendables
compréhensibles au téléphone
```

Éviter :

```txt
jargon technique
grosses promesses
phrases trop longues
langage froid de machine
survente
copie des plateformes lourdes
données inventées
prix affichés trop tôt
```

---

## Modules DIGIYLYFE concernés

```txt
DIGIY POS       → Mon commerce
DIGIY DRIVER    → Chauffeurs et trajets
DIGIY LOC       → Locations
DIGIY PAY       → Argent et preuves
DIGIY MARKET    → Produits et boutiques
DIGIY BUILD     → Artisans et services
DIGIY JOBS      → Missions et travail
DIGIY RESA      → Rendez-vous et réservations
DIGIY EXPLORE   → Lieux et découvertes
DIGIY RÉSEAU    → Club et partenaires
```

---

## Premier challenge

# Recruter 10 pros à Saly

Livrables à produire :

```txt
1. une page HTML “Club des Métiers Saly”
2. une fiche modèle artisan
3. une fiche modèle chauffeur
4. un message WhatsApp de prospection
5. un texte QR autocollant
6. une offre terrain souple sans prix bloquant
7. un script oral de démonstration
8. un mini dossier partenaire
9. une checklist de validation pro
10. un modèle de données avec photo_url et gallery_urls
```

---

## Grille de validation terrain

Avant de publier ou d’utiliser une sortie, vérifier :

```txt
Est-ce compréhensible en 10 secondes ?
Est-ce lisible sur téléphone ?
Est-ce utile pour un pro local ?
Est-ce que le client sait quoi faire ?
Est-ce que le contact direct est clair ?
Est-ce que DIGIY garde le pro maître de son business ?
Est-ce que cela évite la commission ?
Est-ce que cela peut être imprimé en QR ?
Est-ce que les données viennent bien du pro ?
Est-ce que les photos sont en URL seulement ?
Est-ce que le lien fonctionne ?
Est-ce que le QR fonctionne sur téléphone ?
```

Si la réponse est non, on simplifie.

---

## Règle de publication

Aucune sortie ne part sur le terrain sans contrôle :

```txt
contrôle terrain
contrôle DIGIYLYFE
contrôle données pro
contrôle photos URL
contrôle sécurité
contrôle action
contrôle format
contrôle module
validation finale
```

---

## Phrase de route

> DIGIYLYFE transforme le sable du terrain en or digital.

Le Lab existe pour servir cette route, pas pour la remplacer.

---

## Règle finale

L’abonné fournit ses données.
DIGIY structure.
DeerFlow assiste.
Le pro valide.
Le terrain décide.
