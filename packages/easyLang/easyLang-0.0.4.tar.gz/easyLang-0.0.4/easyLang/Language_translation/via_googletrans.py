#Documentation https://pypi.org/project/googletrans/
#Installation pip install googletrans

from googletrans import Translator

def translate_file(content):
    try:

        translator = Translator() 
        result = translator.translate(content, dest='en') 
        return True, result.text
    
    except Exception as e:
        print(f"Error in detecting langauge: {e}")
        return False, None
