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

def translate_file(file_path):
    try:

        flag, content = load_text_file(file_path)
        if flag:
            print(content)

            translator = Translator() 
            result = translator.translate(content, dest='en') 
            return True, result.text
        else:
            return False, None
    
    except Exception as e:
        print(f"Error in detecting langauge: {e}")
        return False, None
    
file_path = "data/german.txt"
flag, translated_content = translate_file(file_path)
if flag:
    print(translated_content)

