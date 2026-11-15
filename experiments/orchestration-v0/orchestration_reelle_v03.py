#!/usr/bin/env python3
"""DIGIY V0.3: execution reelle de controles locaux sur du HTML fourni.
Aucun modele IA, reseau, sous-processus, publication ou ecriture dans la source.
"""
import argparse
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit


class VoiceParser(HTMLParser):
    """Extrait les elements du bloc voix sans executer le HTML."""
    LABELS = {"strong", "small", "a", "p"}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.found = False
        self.block_depth = 0
        self.elements = []
        self.links = []
        self.summary_count = 0
        self.labels = []
        self.label_stack = []

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if not self.block_depth:
            if tag == "details" and attrs.get("id") == "voix-adherents":
                self.block_depth = 1
                self.found = True
                self.elements.append(tag)
            return
        self.block_depth += 1
        self.elements.append(tag)
        if tag == "summary":
            self.summary_count += 1
        if tag == "a":
            self.links.append({"href": attrs.get("href", ""),
                               "target": attrs.get("target", ""),
                               "rel": attrs.get("rel", "")})
        if tag in self.LABELS:
            self.label_stack.append({"tag": tag, "i18n": bool(attrs.get("data-i18n")),
                                     "depth": self.block_depth, "visible": False})

    def handle_data(self, data):
        if self.block_depth and data.strip() and self.label_stack:
            self.label_stack[-1]["visible"] = True

    def handle_endtag(self, tag):
        if not self.block_depth:
            return
        if self.label_stack and self.label_stack[-1]["tag"] == tag:
            obj = self.label_stack.pop()
            if obj["visible"]:
                self.labels.append({"tag": obj["tag"], "i18n": obj["i18n"]})
        self.block_depth -= 1


def eclaireur(source: str):
    raw = source.encode("utf-8")
    return {"role": "eclaireur", "statut": "conforme", "preuves": [
        f"Lecture locale: {len(raw)} octets", f"SHA-256: {hashlib.sha256(raw).hexdigest()}"],
        "inconnues": ["Aucun test navigateur ni reseau effectue"]}


def technique(parsed):
    bad = []
    missing = []
    if not parsed.found:
        bad.append("Bloc voix-adherents absent")
    if parsed.summary_count != 1:
        bad.append("Nombre de summary != 1")
    if len(parsed.links) != 3:
        bad.append("Nombre de liens != 3")
    for link in parsed.links:
        url = urlsplit(link["href"])
        q = parse_qs(url.query)
        if url.scheme != "https" or url.hostname != "wa.me" or not url.path.strip("/").isdigit() or not q.get("text", [""])[0].strip():
            bad.append("Lien WhatsApp non conforme")
        if link["target"] == "_blank" and not {"noopener", "noreferrer"}.issubset(set(link["rel"].split())):
            bad.append("Lien nouvel onglet non protege")
    missing.append("Reception WhatsApp et affichage iPhone non testes")
    return {"role": "technique", "statut": "a_corriger" if bad else "impossible_a_verifier",
            "preuves": [f"{len(parsed.links)} liens trouves", f"{parsed.summary_count} summary trouve"],
            "anomalies": sorted(set(bad)), "inconnues": missing}


def langues(parsed):
    total = len(parsed.labels)
    missing = sum(1 for x in parsed.labels if not x["i18n"])
    return {"role": "langues",
            "statut": "a_corriger" if missing else "impossible_a_verifier",
            "preuves": [f"{total} elements de libelle audites", f"{missing} sans data-i18n"],
            "anomalies": ["Libelles non raccordes au systeme de traduction"] if missing else [],
            "inconnues": ["Traductions des dix langues etendu aux autres pages non auditees"]}


def executer(source):
    if not isinstance(source, str) or len(source) > 3_000_000:
        raise ValueError("Fichier absent ou trop volumineux")
    parsed = VoiceParser()
    parsed.feed(source)
    travaux = [eclaireur(source), technique(parsed), langues(parsed)]
    problem = any(x["statut"] == "a_corriger" for x in travaux)
    return {"version": "DIGIY-ORCH-V0.3", "mode": "lecture_seule",
            "moteur": "trois_travailleurs_locaux_deterministes_sans_IA_externe",
            "travaux": travaux,
            "controleur": {"verdict": "a_corriger" if problem else "a_verifier",
                            "preuve_independante_validee": False,
                            "demonstration_agents_IA_independants": False},
            "interdictions": {"fusion": True, "publication": True, "ecriture_source": True,
                             "contact_externe": True, "depense": True}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, required=True,
                    help="Fichier HTML fourni localement, jamais telecharge par cet outil")
    args = ap.parse_args()
    if not args.source.is_file():
        ap.error("Source inexistante")
    print(json.dumps(executer(args.source.read_text(encoding="utf-8")), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
