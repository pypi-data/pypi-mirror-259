#Documentation https://github.com/detectlanguage/detectlanguage-python
#Installation pip install detectlanguage

import detectlanguage

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
        api_key = "cd0d7ee1c00134e594282fbb9fd12fdf" #Free

        flag, content = load_text_file(file_path)
        if flag:
            print(content)
        
            detectlanguage.configuration.api_key = api_key
            result = detectlanguage.detect(content)
            print(result)
            language_detected = result[0]['language']
            return True, language_detected
        else:
            return False, None
    
    except Exception as e:
        print(f"Error in detecting langauge: {e}")
        return False, None
    
file_path = "data/german.txt"
flag, language = detect_language(file_path)
if flag:
    print(language)

