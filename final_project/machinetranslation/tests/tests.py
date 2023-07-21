import unittest
import sys
sys.path.append("../")  # Add the parent directory to the sys.path

from translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):
    def test_english_to_french(self):
        english_text = "Hello"
        expected_french_text = "Bonjour"
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, expected_french_text)
        self.assertNotEqual(translated_text, "Hola")

    def test_french_to_english(self):
        french_text = "Bonjour"
        expected_english_text = "Hello"
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, expected_english_text)
        self.assertNotEqual(translated_text, "Hi")

if __name__ == '__main__':
    unittest.main()