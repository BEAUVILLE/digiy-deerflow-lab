import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from orchestrateur_v04 import executer

BASE = {
    'mission_id': 'DIGIY-ORCH-004', 'type': 'lecture_seule',
    'cout_supplementaire_autorise': 0, 'actions_autorisees': [],
    'validation_maitre': False,
    'cibles': [{'fichier': 'ok.py', 'controle': 'base'}]
}

class TestOrchV04(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.addCleanup(self.t.cleanup)
        self.r = Path(self.t.name)
        (self.r/'ok.py').write_text('x = 1\n', encoding='utf-8')
        self.m = copy.deepcopy(BASE)

    def test_simple_mission_is_never_approved(self):
        r = executer(self.m, self.r)
        self.assertEqual(r['controleur']['verdict'], 'a_verifier')
        self.assertEqual(r['fichiers'][0]['controles'][1]['indices']['syntaxe'], 'python_ok')
        self.assertTrue(r['verrous']['publication_interdite'])

    def test_python_syntax_error(self):
        (self.r/'ok.py').write_text('def x(\n', encoding='utf-8')
        self.assertEqual(executer(self.m, self.r)['controleur']['verdict'], 'a_corriger')

    def test_json_syntax_error(self):
        (self.r/'a.json').write_text('{', encoding='utf-8')
        self.m['cibles'] = [{'fichier': 'a.json', 'controle': 'base'}]
        self.assertEqual(executer(self.m, self.r)['fichiers'][0]['controles'][1]['indices']['syntaxe'], 'json_invalide')

    def test_javascript_syntax_error(self):
        (self.r/'a.mjs').write_text('export const x = ;', encoding='utf-8')
        self.m['cibles'] = [{'fichier': 'a.mjs', 'controle': 'base'}]
        self.assertEqual(executer(self.m, self.r)['controleur']['verdict'], 'a_corriger')

    def test_node_unavailable_not_false_success(self):
        (self.r/'a.mjs').write_text('export const x = 1;', encoding='utf-8')
        self.m['cibles'] = [{'fichier': 'a.mjs', 'controle': 'base'}]
        with patch('orchestrateur_v04.shutil.which', return_value=None):
            r = executer(self.m, self.r)
        self.assertEqual(r['fichiers'][0]['controles'][1]['statut'], 'a_verifier')

    def test_bad_html_link(self):
        (self.r/'a.html').write_text('<a href="https://a" target="_blank">A</a>', encoding='utf-8')
        self.m['cibles'] = [{'fichier': 'a.html', 'controle': 'base'}]
        self.assertEqual(executer(self.m, self.r)['controleur']['verdict'], 'a_corriger')

    def test_secret_flag_never_leaks_secret(self):
        secret = 'sk-proj-'+'supersecret_12345678'
        (self.r/'ok.py').write_text('s = "'+secret+'"', encoding='utf-8')
        r = executer(self.m, self.r)
        self.assertEqual(r['controleur']['verdict'], 'a_corriger')
        self.assertNotIn(secret, json.dumps(r))

    def test_escape_path_rejected(self):
        self.m['cibles'] = [{'fichier': '../outside.py', 'controle': 'base'}]
        with self.assertRaises(ValueError): executer(self.m, self.r)

    def test_symlink_to_outside_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            p = Path(outside)/'outside.py'
            p.write_text('x=1', encoding='utf-8')
            (self.r/'external.py').symlink_to(p)
            self.m['cibles'] = [{'fichier': 'external.py', 'controle': 'base'}]
            with self.assertRaises(ValueError): executer(self.m, self.r)

    def test_empty_actions_only(self):
        self.m['actions_autorisees'] = ['fusion']
        with self.assertRaises(ValueError): executer(self.m, self.r)

    def test_no_budget(self):
        self.m['cout_supplementaire_autorise'] = 1
        with self.assertRaises(ValueError): executer(self.m, self.r)

    def test_no_implicit_approval(self):
        self.m['validation_maitre'] = True
        with self.assertRaises(ValueError): executer(self.m, self.r)

    def test_missing_file_stays_unknown(self):
        self.m['cibles'] = [{'fichier': 'missing.py', 'controle': 'base'}]
        self.assertEqual(executer(self.m, self.r)['fichiers'][0]['statut'], 'a_verifier')

    def test_no_duplicate_targets(self):
        self.m['cibles'] *= 2
        with self.assertRaises(ValueError): executer(self.m, self.r)

    def test_too_many_files(self):
        self.m['cibles'] = [{'fichier': f'{i}.py', 'controle': 'base'} for i in range(21)]
        with self.assertRaises(ValueError): executer(self.m, self.r)

    def test_consistent_report_and_no_file_mutation(self):
        before = (self.r/'ok.py').read_bytes()
        a,b = executer(self.m, self.r), executer(self.m, self.r)
        self.assertEqual(a,b)
        self.assertEqual(before,(self.r/'ok.py').read_bytes())

    def test_voice_adapter_uses_existing_v03(self):
        markup = '''<details id="voix-adherents"><summary><strong>Voix</strong></summary>
        <a href="https://wa.me/221001234567?text=Bonjour">A</a>
        <a href="https://wa.me/221001234567?text=Bonjour">B</a>
        <a href="https://wa.me/221001234567?text=Bonjour">C</a></details>'''
        (self.r/'v.html').write_text(markup, encoding='utf-8')
        self.m['cibles'] = [{'fichier':'v.html', 'controle':'voix'}]
        r = executer(self.m, self.r)
        self.assertEqual(r['controleur']['verdict'],'a_corriger')
        self.assertEqual(r['fichiers'][0]['controles'][-1]['role'],'specialiste_voix')
        self.assertNotIn('221001234567',json.dumps(r))

    def test_broken_utf8_not_assumed_valid(self):
        (self.r/'bad.py').write_bytes(b'\xff\xfe')
        self.m['cibles'] = [{'fichier':'bad.py', 'controle':'base'}]
        self.assertEqual(executer(self.m,self.r)['fichiers'][0]['statut'],'a_verifier')

if __name__ == '__main__': unittest.main()
