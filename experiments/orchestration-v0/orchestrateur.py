#!/usr/bin/env python3
"""DIGIY V0: coordination déterministe de contrôles, sans agent IA ni réseau."""
import argparse
import json
from pathlib import Path

ROLES = ("eclaireur", "technique", "langues")
STATES = ("conforme", "a_corriger", "impossible_a_verifier")


def check_mission(mission):
    """Aucune instruction externe, dépense ou mutation n'est admise."""
    if not isinstance(mission, dict):
        raise ValueError("Mission invalide")
    if mission.get("type") != "lecture_seule":
        raise ValueError("Seules les missions en lecture_seule sont admises")
    if mission.get("actions_autorisees") != []:
        raise ValueError("Les actions externes sont interdites")
    if mission.get("cout_supplementaire_autorise") != 0:
        raise ValueError("Aucun cout supplementaire autorise")
    if mission.get("validation_maitre") is not False:
        raise ValueError("Aucune validation du MAITRE ne doit etre anticipee")
    if mission.get("mission_id") != "DIGIY-ORCH-001":
        raise ValueError("Seul le pilote 001 est admis en V0")


def report(role, status, facts, missing=()):
    return {"role": role, "statut": status, "preuves": facts, "points_a_verifier": list(missing)}


def eclaireur(faits):
    pr = faits.get("pr") or {}
    if pr.get("merged") is True and pr.get("url") and pr.get("changed_files") == ["index.html"]:
        return report("eclaireur", "conforme", ["PR #204 fusionnee", "Un seul fichier modifie : index.html", pr["url"]])
    return report("eclaireur", "impossible_a_verifier", [], ["Etat et perimetre de la PR non etablis"])


def technique(faits):
    dom = faits.get("composant") or {}
    if not isinstance(dom.get("liens_whatsapp"), int) or not isinstance(dom.get("details_natif"), bool):
        return report("technique", "impossible_a_verifier", [], ["Code source non documente"])
    if dom["liens_whatsapp"] != 3 or not dom["details_natif"]:
        return report("technique", "a_corriger", ["Structure observee non conforme au contrat du pilote"])
    if dom.get("destination_whatsapp_verifiee") is True and dom.get("test_reception_sur_telephone") is True:
        return report("technique", "conforme", ["Trois liens et test telephone attestes"])
    return report("technique", "impossible_a_verifier", ["HTML details natif et trois liens WhatsApp dans le code"], ["Destination WhatsApp metier", "Reception et parcours sur telephone"])


def langues(faits):
    com = faits.get("composant") or {}
    if not isinstance(com.get("libelles_traduits_dans_le_bloc"), bool):
        return report("langues", "impossible_a_verifier", [], ["Analyse linguistique absente"])
    if com["libelles_traduits_dans_le_bloc"]:
        return report("langues", "conforme", ["Balises linguistiques presentes selon les preuves fournies"])
    return report("langues", "a_corriger", ["Libelles francais sans data-i18n dans le bloc"], ["Examiner les 10 langues et le parcours utilisateur avant correctif"])


SPECIALISTES = {"eclaireur": eclaireur, "technique": technique, "langues": langues}


def orchestrer(mission, faits):
    check_mission(mission)
    if not isinstance(faits, dict):
        raise ValueError("Faits invalides")
    travaux = [SPECIALISTES[role](faits) for role in ROLES]
    etats = [r["statut"] for r in travaux]
    if any(x not in STATES for x in etats):
        raise RuntimeError("Statut de rapport inconnu")
    verdict = "a_corriger" if "a_corriger" in etats else ("impossible_a_verifier" if "impossible_a_verifier" in etats else "conforme")
    return {
        "mission_id": mission["mission_id"],
        "execution": "locale_deterministe_sans_agents_ia",
        "postes": travaux,
        "controleur": {"statut": verdict, "motif": "Synthese des trois controles; les elements non verifies restent ouverts"},
        "garde_fou": {"mise_en_production": False, "publication": False, "fusion": False,
                      "message_externe": False, "depense": False,
                      "validation_humaine_requise": True},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mission", required=True, type=Path)
    parser.add_argument("--faits", required=True, type=Path)
    args = parser.parse_args()
    mission = json.loads(args.mission.read_text(encoding="utf-8"))
    faits = json.loads(args.faits.read_text(encoding="utf-8"))
    print(json.dumps(orchestrer(mission, faits), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
