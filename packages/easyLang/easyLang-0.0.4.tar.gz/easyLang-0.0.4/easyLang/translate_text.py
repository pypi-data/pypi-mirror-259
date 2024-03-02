from Language_translation import via_deeptranslator
from Language_translation import via_googletrans 

def load_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return True, content
    except Exception as e:
        print(f"Error loading the text file: {e}")
        return False, None
    
def translate_txt(file_path,module='googletrans'):
    try:
        flag, content = load_text_file(file_path)
        if flag:
            print("File loaded")

            if module == 'googletrans':
                _, language = via_googletrans.translate_file(content)
             
            elif module == 'deeptrans':
                _, language =  via_deeptranslator.translate_file(content)
        
            else:
                return False, None
                          
            return _, language

        else:
            print("Could not load file")
            return False, None

    except:
        print("Exception in translate_text", e)
        return False, None
