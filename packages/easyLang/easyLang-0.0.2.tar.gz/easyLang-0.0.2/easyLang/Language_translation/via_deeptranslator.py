#Documentation https://pypi.org/project/deep-translator/
#Installationpip install deep-translator

import os 
from deep_translator import GoogleTranslator

PATH = os.get
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
        #target is language you want to translate your text into

        flag, content = load_text_file(file_path)
        if flag:
            print(content)
        translated_text = GoogleTranslator(source='auto', target='en').translate(content)
        return True, translated_text
    
    except Exception as e:
        print(f"Error in detecting langauge: {e}")
        return False, None
    
file_path = "data/german.txt"
flag, translated_content = translate_file(file_path)
if flag:
    print(translated_content)

