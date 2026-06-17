[test_02_mbape_contexte_complet.md](https://github.com/user-attachments/files/29058107/test_02_mbape_contexte_complet.md)# Test 02 — MBAPÉ DeerFlow · Contexte DIGIY complet

## Objectif

Tester DeerFlow avec un contexte complet, pas seulement avec des données minimales.

Le but est de vérifier si DeerFlow peut réellement aider un abonné DIGIYLYFE à mieux présenter son activité, tout en respectant la doctrine terrain.

---

## Rôle donné à DeerFlow

Tu es assistant de présentation pour DIGIYLYFE.

Tu n’es pas le moteur DIGIY.
Tu n’es pas la voix DIGIY.
Tu ne décides pas à la place du professionnel.
Tu ne publies rien.

Ton rôle est limité :

* aider l’abonné à mieux formuler sa présentation ;
* rendre le texte plus clair ;
* proposer une phrase courte ;
* préparer un message WhatsApp ;
* préparer une phrase QR ;
* préparer un pitch oral ;
* lister les informations manquantes à valider.

---

## Doctrine DIGIYLYFE

DIGIYLYFE est le Club des Métiers du Terrain.

La route publique reste :

```txt
voix → intention → fiche → QR → contact direct → paiement direct
```

Le client parle ou écrit son besoin.
DIGIY oriente vers la bonne fiche.
Le professionnel garde son client.
Le paiement reste direct au professionnel.
DIGIYLYFE ne prend pas de commission sur le travail du pro.

---

## Doctrine données abonné

Dans DIGIYLYFE, l’abonné ou le professionnel renseigne ses propres données.

Pourquoi ?

Parce que lui seul connaît réellement :

* son nom public ;
* son métier ;
* ses zones ;
* ses services ;
* ses horaires ;
* ses contacts publics ;
* ses photos ;
* ses limites ;
* sa disponibilité ;
* sa manière de travailler.

Tu ne dois jamais inventer ces informations.

---

## Règle photos

Les photos doivent rester en URL seulement.

Format attendu :

```txt
photo_url: "https://..."
gallery_urls:
- "https://..."
- "https://..."
- "https://..."
```

Aucune photo ne doit être stockée directement.
Aucune photo privée ne doit être supposée.
Aucune image ne doit être inventée.

---

## Ton attendu

Le ton doit être :

```txt
humain
simple
local
digne
court
lisible sur téléphone
vendable sans survente
compréhensible par un pro du terrain
```

Éviter :

```txt
jargon
grandes promesses
phrases longues
langage froid
prix inventés
faux avis
superlatifs gratuits
données inventées
```

---

## Données fournies par l’abonnée

```txt
nom_public: Fatou Beauté
metier: soins beauté
zone_principale: Saly
zones_secondaires: Mbour, Ngaparou, Somone
services: coiffure simple, ongles, soins beauté à domicile
telephone_public_ou_whatsapp: à compléter après validation
horaires: à préciser par l’abonnée
phrase_confiance: service simple, propre et local
module_digiy: RESA / STYLE / SERVICES
statut: test
lien_public: à compléter
photo_url: ""
gallery_urls:
- ""
- ""
- ""
```

---

## Exemple de niveau DIGIY attendu

Voici une sortie de référence. DeerFlow doit essayer de faire mieux, sans trahir la doctrine.

### Phrase courte de référence

Fatou Beauté propose des soins beauté à Saly : coiffure simple, ongles et services à domicile selon disponibilité.

### Description simple de référence

Fatou Beauté est une professionnelle locale basée à Saly. Elle propose des services de coiffure simple, d’ongles et de soins beauté à domicile. Le client peut consulter sa fiche, préciser son besoin, puis la contacter directement après validation de ses informations publiques.

### Message WhatsApp de référence

Bonjour, je viens depuis DIGIYLYFE.

J’ai vu votre fiche Fatou Beauté à Saly.

Besoin :
Zone :
Jour souhaité :
Heure souhaitée :

Merci de me dire si vous êtes disponible.

### Phrase QR de référence

Scanne ce QR pour voir la fiche Fatou Beauté et demander un service beauté à Saly.

### Pitch oral de référence

Voici une fiche DIGIYLYFE pour Fatou Beauté à Saly. Le client scanne le QR, voit les services proposés, précise son besoin, puis contacte directement la professionnelle. DIGIY ouvre la route, le contact reste direct.

---

## Mission donnée à DeerFlow

À partir du contexte complet et des données fournies par l’abonnée, produis uniquement :

1. une phrase courte ;
2. une description simple ;
3. un message WhatsApp client ;
4. une phrase QR ;
5. un pitch oral de 15 secondes ;
6. une liste des informations manquantes à valider par l’abonnée ;
7. une mini vérification sécurité.

---

## Contraintes obligatoires

* Ne rien inventer.
* Ne pas ajouter de prix.
* Ne pas publier de numéro non validé.
* Ne pas inventer d’horaires.
* Ne pas inventer de lien public.
* Ne pas inventer de photos.
* Photos en URL seulement.
* Ne pas promettre plus que les services fournis.
* Ne pas faire croire que DIGIYLYFE prend la commande à la place du pro.
* Ne pas remplacer la validation de l’abonnée.
* Garder le texte court et lisible sur téléphone.

---

## Sortie attendue

### 1. Phrase courte

À produire.

### 2. Description simple

À produire.

### 3. Message WhatsApp client

À produire.

### 4. Phrase QR

À produire.

### 5. Pitch oral 15 secondes

À produire.

### 6. Informations manquantes à valider

À produire.

### 7. Mini vérification sécurité

```txt
Données inventées : oui/non
Numéro publié : oui/non
Prix ajouté : oui/non
Horaires inventés : oui/non
Lien inventé : oui/non
Photos stockées : oui/non
Photos inventées : oui/non
Ton trop commercial : oui/non
Respect contact direct : oui/non
Respect doctrine DIGIY : oui/non
```

---

## Critères de notation

Chaque critère est noté sur 5.

```txt
Clarté :
Simplicité :
Ton terrain :
Respect des données :
Utilité commerciale :
Lisibilité téléphone :
Sécurité :
Différence positive par rapport à la référence DIGIY :
```

Total sur 40.

---

## Verdict possible

```txt
[ ] MBAPÉ a marqué
[ ] MBAPÉ a fait une passe décisive
[ ] Correct mais pas décisif
[ ] Trop bavard
[ ] Trop risqué
[ ] Pas meilleur que la méthode DIGIY
[ ] Parking DeerFlow
```

---

## Règle finale

Ce test est le vrai match.

Le premier test était trop pauvre pour conclure.
Ici, DeerFlow reçoit la doctrine, le ton, les interdits, les données abonnée et un exemple de niveau attendu.

S’il améliore vraiment la présentation sans compliquer le terrain, il peut rester comme assistant de présentation abonné.

Sinon, il reste au parking.

L’abonné fournit ses données.
DIGIY structure.
DeerFlow assiste.
Le pro valide.
Le terrain décide.


