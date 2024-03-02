#Documentation https://pypi.org/project/deep-translator/
#Installationpip install deep-translator

from deep_translator import GoogleTranslator

def translate_file(content):
    try:
        #target is language you want to translate your text into
        translated_text = GoogleTranslator(source='auto', target='en').translate(content)
        return True, translated_text
    
    except Exception as e:
        print(f"Error in detecting langauge: {e}")
        return False, None