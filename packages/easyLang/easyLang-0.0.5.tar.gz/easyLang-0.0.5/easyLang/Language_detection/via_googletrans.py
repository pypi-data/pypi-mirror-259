#Documentation https://pypi.org/project/googletrans/
#Installation pip install googletrans

from googletrans import Translator


def detect_language(content):
    try: 
        translator = Translator() 
        language_detected = translator.detect(content)
        language = language_detected.lang 
        return True, language
    
    except Exception as e:
        print(f"Error in detecting langauge: {e}")
        return False, None
    