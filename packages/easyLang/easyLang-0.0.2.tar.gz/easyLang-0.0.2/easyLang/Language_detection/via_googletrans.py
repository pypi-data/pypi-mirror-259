#Documentation https://pypi.org/project/googletrans/
#Installation pip install googletrans

from googletrans import Translator

def load_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return True, content
    except Exception as e:
        print(f"Error loading the text file: {e}")
        return False, None

def detect_language(file_path):
    try:
        flag, content = load_text_file(file_path)
        if flag:
            print(content)
            
            translator = Translator() 
            language_detected = translator.detect(content)
            language = language_detected.lang 
            return True, language
        else:
            language = None
            return False, language
    
    except Exception as e:
        print(f"Error in detecting langauge: {e}")
        return False, None
    
file_path = "data/german.txt"

flag, language = detect_language(file_path)
if flag:
    print(language)

