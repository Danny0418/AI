"""import MyMemory Translator library"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """function translate English to French"""
    french_text = MyMemoryTranslator(source='en-SG', target='fr-FR').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """function translate French to English"""
    english_text = MyMemoryTranslator(source='fr-FR', target='en-SG').translate(french_text)
    print(english_text)
    return english_text
