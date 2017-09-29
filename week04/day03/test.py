import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('u'))

    def test_is_vovel_b(self):
        self.assertFalse(extend.is_vovel('b'))

    def test_is_vovel_U(self):
        self.assertTrue(extend.is_vovel('U'))


    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

    def test_translate_bbb(self):
        self.assertEqual(extend.translate("bbb"), "bbb")

    def test_translate_ae(self):
        self.assertEqual(extend.translate("ae"), "avaeve")
    
    def test_translate_aa(self):
       self.assertEqual(extend.translate("aa"), "avaava")

    def test_translate_aaee(self):
       self.assertEqual(extend.translate("aaee"), "avaavaeveeve")

    def test_translate_aaaa(self):
       self.assertEqual(extend.translate("aaaa"), "avaavaavaava")


if __name__ == '__main__':
    unittest.main()