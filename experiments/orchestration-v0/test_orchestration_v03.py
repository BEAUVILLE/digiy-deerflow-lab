import unittest
from orchestration_reelle_v03 import executer

BASE = '''<section><details id="voix-adherents"><summary><strong>La voix</strong><small>Une idée</small></summary>
<div><a href="https://wa.me/220000000000?text=Bonjour" target="_blank" rel="noopener noreferrer">Idée</a>
<a href="https://wa.me/220000000000?text=Bonjour" target="_blank" rel="noopener noreferrer">Besoin</a>
<a href="https://wa.me/220000000000?text=Bonjour" target="_blank" rel="noopener noreferrer">Collaboration</a></div>
<p>Le message reste sous votre contrôle</p></details></section>'''

class TestOrchestrationV03(unittest.TestCase):
    def test_trois_travailleurs_executent(self):
        r = executer(BASE)
        self.assertEqual([x['role'] for x in r['travaux']], ['eclaireur', 'technique', 'langues'])
        self.assertEqual(r['controleur']['verdict'], 'a_corriger')
    def test_compte_lien(self):
        r = executer(BASE.replace('<a href="https://wa.me/220000000000?text=Bonjour" target="_blank" rel="noopener noreferrer">Collaboration</a>', '<span>Collaboration</span>'))
        self.assertIn('Nombre de liens != 3', r['travaux'][1]['anomalies'])
    def test_whatsapp_malveillant(self):
        r=executer(BASE.replace('https://wa.me/', 'https://evil.example/'))
        self.assertIn('Lien WhatsApp non conforme', r['travaux'][1]['anomalies'])
    def test_rel_protection(self):
        r=executer(BASE.replace('rel="noopener noreferrer"', 'rel=""'))
        self.assertIn('Lien nouvel onglet non protege',r['travaux'][1]['anomalies'])
    def test_no_phone_in_report(self):
        r=executer(BASE)
        self.assertNotIn('220000000000', str(r))
    def test_i18n_missing(self):
        self.assertIn('Libelles non raccordes au systeme de traduction', executer(BASE)['travaux'][2]['anomalies'])
    def test_translation_complete_does_not_auto_approve(self):
        s=BASE.replace('<strong>', '<strong data-i18n="one">').replace('<small>', '<small data-i18n="two">').replace('<a ', '<a data-i18n="three" ').replace('<p>', '<p data-i18n="four">')
        r=executer(s)
        self.assertEqual(r['travaux'][2]['anomalies'],[])
        self.assertEqual(r['controleur']['verdict'],'a_verifier')
        self.assertFalse(r['controleur']['preuve_independante_validee'])
    def test_missing_block_not_approved(self):
        r=executer('<html>vide</html>')
        self.assertEqual(r['controleur']['verdict'],'a_corriger')
    def test_immutable_input_deterministic(self):
        self.assertEqual(executer(BASE),executer(BASE))
    def test_empty_src_does_not_publish(self):
        r=executer('')
        self.assertTrue(all(r['interdictions'].values()))

if __name__ == '__main__': unittest.main()
