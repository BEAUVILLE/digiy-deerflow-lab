"""Tests offline, stdlib uniquement. python -m unittest discover -s . -p 'test_*.py'"""
import copy
import json
from pathlib import Path
import unittest

from orchestrateur import orchestrer

ROOT = Path(__file__).resolve().parent


class TestPilotage(unittest.TestCase):
    def setUp(self):
        self.mission = json.loads((ROOT / "mission_001.json").read_text(encoding="utf-8"))
        self.faits = json.loads((ROOT / "faits_001.json").read_text(encoding="utf-8"))

    def test_pilote_reel_signale_ecart_et_limites(self):
        r = orchestrer(self.mission, self.faits)
        self.assertEqual([p["role"] for p in r["postes"]], ["eclaireur", "technique", "langues"])
        self.assertEqual([p["statut"] for p in r["postes"]],
                         ["conforme", "impossible_a_verifier", "a_corriger"])
        self.assertEqual(r["controleur"]["statut"], "a_corriger")
        self.assertTrue(r["garde_fou"]["validation_humaine_requise"])
        self.assertFalse(r["garde_fou"]["mise_en_production"])
        self.assertFalse(r["garde_fou"]["message_externe"])

    def test_mutation_bloquee(self):
        mission = copy.deepcopy(self.mission)
        mission["actions_autorisees"] = ["envoyer_whatsapp"]
        with self.assertRaises(ValueError):
            orchestrer(mission, self.faits)

    def test_cout_bloque(self):
        mission = copy.deepcopy(self.mission)
        mission["cout_supplementaire_autorise"] = 1
        with self.assertRaises(ValueError):
            orchestrer(mission, self.faits)

    def test_preuve_manquante_non_inventee(self):
        faits = copy.deepcopy(self.faits)
        faits["pr"] = {}
        faits["composant"] = {}
        r = orchestrer(self.mission, faits)
        self.assertTrue(all(p["statut"] == "impossible_a_verifier" for p in r["postes"]))

    def test_execution_reproductible(self):
        a = orchestrer(self.mission, self.faits)
        b = orchestrer(self.mission, self.faits)
        self.assertEqual(a, b)

    def test_pas_de_confusion_avec_des_agents_autonomes(self):
        r = orchestrer(self.mission, self.faits)
        self.assertEqual(r["execution"], "locale_deterministe_sans_agents_ia")
        self.assertFalse(r["garde_fou"]["fusion"])


if __name__ == "__main__":
    unittest.main()
