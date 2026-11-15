#!/usr/bin/env python3
"""DIGIY ORCH V0.4 : orchestration multi-fichiers, locale, sans API ni écriture.

Rôles effectifs : Éclaireur (inventaire), Technicien (syntaxe), Gardien
(sécurité statique), Contrôleur (synthèse). Python stdlib et Node local
pour la seule option `node --check` (ne lance pas le code contrôlé).
"""
import argparse
import ast
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess

MAX_FILES = 20
MAX_BYTES = 2_000_000
EXTENSIONS = {'.py', '.json', '.js', '.mjs', '.html'}
SECRET_PATTERNS = {
    'cle_privee': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    'jeton_api': re.compile(r'\b(?:sk-proj-|sk_test_secret_|sb_secret_)[A-Za-z0-9_-]{12,}'),
}


class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.unsafe_blank = 0
        self.links = 0

    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        a = dict(attrs)
        self.links += 1
        if a.get('target') == '_blank' and not {'noopener', 'noreferrer'}.issubset(set(a.get('rel', '').split())):
            self.unsafe_blank += 1


def mission_valide(mission):
    if not isinstance(mission, dict) or set(mission) != {'mission_id', 'type', 'cout_supplementaire_autorise', 'actions_autorisees', 'validation_maitre', 'cibles'}:
        raise ValueError('Contrat de mission invalide')
    if not isinstance(mission['mission_id'], str) or not re.fullmatch(r'DIGIY-[A-Z0-9-]{4,40}', mission['mission_id']):
        raise ValueError('ID de mission invalide')
    if mission['type'] != 'lecture_seule' or mission['actions_autorisees'] != [] or type(mission['cout_supplementaire_autorise']) is not int or mission['cout_supplementaire_autorise'] != 0 or mission['validation_maitre'] is not False:
        raise ValueError('Dépense, action ou validation implicite interdite')
    targets = mission['cibles']
    if not isinstance(targets, list) or not 1 <= len(targets) <= MAX_FILES:
        raise ValueError('Nombre de fichiers interdit')
    names = set()
    for item in targets:
        if not isinstance(item, dict) or set(item) != {'fichier', 'controle'}:
            raise ValueError('Cible invalide')
        name, control = item['fichier'], item['controle']
        if not isinstance(name, str) or not name or '\x00' in name or Path(name).is_absolute() or name in names:
            raise ValueError('Chemin interdit ou dupliqué')
        if any(segment in ('.', '..') for segment in Path(name).parts):
            raise ValueError('Chemin traversant interdit')
        if not isinstance(control, str) or control not in ('base', 'voix'):
            raise ValueError('Contrôle inconnu')
        if Path(name).suffix.lower() not in EXTENSIONS or (control == 'voix' and Path(name).suffix.lower() != '.html'):
            raise ValueError('Extension ou contrôle interdit')
        names.add(name)


def statut(role, resultat, indices, inconnues=None):
    return {'role': role, 'statut': resultat, 'indices': indices, 'inconnues': inconnues or []}


def eclaireur(filename, data):
    return statut('eclaireur', 'conforme', {'chemin': filename, 'octets': len(data), 'sha256': hashlib.sha256(data).hexdigest()})


def technicien(file, path, text):
    suffix = path.suffix.lower()
    if suffix == '.py':
        try:
            ast.parse(text, filename=file)
        except SyntaxError as exc:
            return statut('technicien', 'a_corriger', {'syntaxe': 'python_invalide', 'ligne': exc.lineno})
        return statut('technicien', 'conforme', {'syntaxe': 'python_ok'})
    if suffix == '.json':
        try:
            json.loads(text)
        except json.JSONDecodeError as exc:
            return statut('technicien', 'a_corriger', {'syntaxe': 'json_invalide', 'ligne': exc.lineno})
        return statut('technicien', 'conforme', {'syntaxe': 'json_ok'})
    if suffix in ('.js', '.mjs'):
        node = shutil.which('node')
        if not node:
            return statut('technicien', 'a_verifier', {'syntaxe': 'node_absent'}, ['Installer Node n’est pas autorisé automatiquement'])
        try:
            p = subprocess.run([node, '--check', str(path)], capture_output=True, timeout=10, check=False)
        except (OSError, subprocess.TimeoutExpired):
            return statut('technicien', 'a_verifier', {'syntaxe': 'check_indisponible'})
        return statut('technicien', 'conforme' if p.returncode == 0 else 'a_corriger', {'syntaxe': 'javascript_ok' if p.returncode == 0 else 'javascript_invalide'})
    if suffix == '.html':
        p = Links()
        p.feed(text)
        return statut('technicien', 'a_corriger' if p.unsafe_blank else 'conforme', {'liens': p.links, 'nouvel_onglet_non_protege': p.unsafe_blank})
    raise ValueError('Type non pris en charge')


def gardien(text):
    # Aucune valeur trouvée n'est copiée dans le rapport, seules les catégories.
    alertes = sorted([name for name, pattern in SECRET_PATTERNS.items() if pattern.search(text)])
    return statut('gardien', 'a_corriger' if alertes else 'conforme', {'alertes_securite': alertes})


def specialiste_voix(text):
    from orchestration_reelle_v03 import executer
    original = executer(text)
    t = original['travaux'][1]
    l = original['travaux'][2]
    return statut('specialiste_voix', 'a_corriger' if any(x['statut'] == 'a_corriger' for x in (t, l)) else 'a_verifier',
                  {'structure_liens': t['preuves'], 'traduction': l['preuves']},
                  ['Test téléphone et réception WhatsApp encore nécessaires'])


def executer(mission, root):
    mission_valide(mission)
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError('Racine invalide')
    results = []
    for target in mission['cibles']:
        name = target['fichier']
        try:
            path = (root / name).resolve(strict=True)
        except (OSError, RuntimeError):
            results.append({'fichier': name, 'statut': 'a_verifier', 'controles': [], 'inconnues': ['Fichier absent ou inaccessible']})
            continue
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError('Sortie de racine ou cible non régulière interdite')
        if path.stat().st_size > MAX_BYTES:
            raise ValueError('Fichier trop volumineux')
        data = path.read_bytes()
        if len(data) > MAX_BYTES:
            raise ValueError('Fichier trop volumineux')
        try:
            text = data.decode('utf-8')
        except UnicodeDecodeError:
            results.append({'fichier': name, 'statut': 'a_verifier', 'controles': [eclaireur(name, data)], 'inconnues': ['Encodage non UTF-8']})
            continue
        workers = [eclaireur(name, data), technicien(name, path, text), gardien(text)]
        if target['controle'] == 'voix':
            workers.append(specialiste_voix(text))
        # Une conformité des travailleurs ne remplace jamais le contrôle humain.
        verdict = 'a_corriger' if any(x['statut'] == 'a_corriger' for x in workers) else 'a_verifier'
        results.append({'fichier': name, 'statut': verdict, 'controles': workers})
    final = 'a_corriger' if any(x['statut'] == 'a_corriger' for x in results) else 'a_verifier'
    return {
        'mission_id': mission['mission_id'], 'version': 'DIGIY-ORCH-V0.4',
        'mode': 'execution_locale_sans_modele_IA', 'fichiers': results,
        'controleur': {'verdict': final, 'preuves_independantes_verifiees': False,
                        'validation_maitre_requise': True},
        'actions_effectuees': [],
        'verrous': {'fusion_interdite': True, 'publication_interdite': True,
                   'contact_externe_interdit': True, 'cout_supplementaire_interdit': True},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mission', required=True, type=Path)
    parser.add_argument('--racine', type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    print(json.dumps(executer(json.loads(args.mission.read_text(encoding='utf-8')), args.racine), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
