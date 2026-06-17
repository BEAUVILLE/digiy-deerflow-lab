# Skill — Fiche Métier Terrain

## Mission

Préparer une fiche simple pour un professionnel du terrain à partir des informations fournies par le professionnel lui-même.

La fiche doit être claire, courte, lisible sur téléphone, utilisable avec un QR, et compatible avec la logique DIGIYLYFE :

**voix → intention → fiche → QR → contact direct**

---

## Doctrine

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
* sa disponibilité ;
* sa manière de travailler.

DeerFlow ne doit pas inventer une fiche à la place du pro.

DeerFlow peut seulement :

* structurer les informations ;
* clarifier le texte ;
* repérer les oublis ;
* préparer un message WhatsApp ;
* préparer une phrase QR ;
* préparer un pitch court ;
* vérifier que la fiche reste simple et sûre.

---

## Entrées

```txt
nom_public:
metier:
zone_principale:
zones_secondaires:
services:
telephone_public_ou_whatsapp:
horaires:
phrase_confiance:
module_digiy:
statut: partenaire | pro | test
lien_public:
photo_url:
gallery_urls:
```

---

## Règle photos

Les photos doivent être renseignées uniquement sous forme d’URL.

Aucune photo ne doit être stockée directement dans ce fichier.

Format attendu :

```txt
photo_url: "https://..."
gallery_urls:
- "https://..."
- "https://..."
- "https://..."
```

Les URLs doivent être publiques, propres, accessibles et validées par le professionnel.

---

## Sortie attendue

```txt
TITRE PUBLIC

Statut :
partenaire | pro | test

Module DIGIY :

Phrase courte :

Services :
- service 1
- service 2
- service 3

Zone principale :

Zones secondaires :

Contact :
uniquement si validé par le professionnel

Lien public :

Photos :
photo_url:
gallery_urls:

Message WhatsApp préparé :

Phrase QR :

Pitch oral 15 secondes :

Contrôle avant publication :
- données validées par le pro
- contact validé
- photos en URL seulement
- lien testé
- QR testé
```

---

## Règles d’écriture

```txt
phrases courtes
texte lisible sur téléphone
pas de promesse excessive
pas de jargon
pas de faux avis
pas de superlatifs gratuits
pas de coordonnées privées non validées
pas de numéro publié sans accord
pas de photo stockée dans le dépôt
pas de donnée inventée
pas de tarif inventé
```

---

## Contrôle obligatoire

Avant de considérer une fiche comme utilisable :

* [ ] Le nom public est validé par le professionnel.
* [ ] Le métier est validé par le professionnel.
* [ ] Les zones sont validées par le professionnel.
* [ ] Les services sont validés par le professionnel.
* [ ] Le contact public est validé par le professionnel.
* [ ] Le lien public fonctionne.
* [ ] Les photos sont uniquement en URL.
* [ ] Les URLs photos fonctionnent.
* [ ] Le message WhatsApp est clair.
* [ ] La phrase QR est simple.
* [ ] Le QR est testé sur téléphone.
* [ ] La fiche ne contient aucune donnée sensible.
* [ ] La fiche respecte la doctrine DIGIYLYFE.

---

## Exemple

Entrée :

```txt
nom_public: Helage Plombier
metier: plombier
zone_principale: Saly
zones_secondaires: Mbour, Ngaparou, Somone, Petite Côte
services: fuite, robinet, WC, petits travaux
telephone_public_ou_whatsapp: à compléter après validation du pro
horaires: à préciser par le pro
phrase_confiance: intervention locale simple
module_digiy: BUILD
statut: partenaire
lien_public: https://helage-plombier.digiylyfe.com/
photo_url: ""
gallery_urls:
- ""
- ""
- ""
```

Sortie :

```txt
HELAGE PLOMBIER — Saly

Statut :
partenaire

Module DIGIY :
BUILD

Phrase courte :
Plombier local pour les petites interventions à Saly.

Services :
- fuite d’eau
- robinetterie
- WC et évacuation
- petits travaux de plomberie

Zone principale :
Saly

Zones secondaires :
Mbour, Ngaparou, Somone, Petite Côte

Contact :
À publier uniquement après validation du professionnel.

Lien public :
https://helage-plombier.digiylyfe.com/

Photos :
photo_url:
À compléter avec une URL publique validée par le professionnel.

gallery_urls:
À compléter avec des URLs publiques validées par le professionnel.

Message WhatsApp préparé :
Bonjour, je viens depuis DIGIYLYFE.
Je cherche un plombier à Saly.
Besoin : petite intervention plomberie.
Moment : à préciser.
Merci de me répondre quand disponible.

Phrase QR :
Scannez pour contacter un plombier local à Saly.

Pitch oral 15 secondes :
Le client scanne le QR, voit la fiche et contacte directement le plombier.
Pas de commission sur le travail du pro, pas d’application compliquée.

Contrôle avant publication :
- données à valider par le professionnel
- contact à valider
- photos URL à compléter
- lien à tester
- QR à tester sur téléphone
```

---

## Règle finale

L’abonné fournit ses données.
DIGIY structure.
DeerFlow assiste.
Le pro valide.
Le terrain décide.

