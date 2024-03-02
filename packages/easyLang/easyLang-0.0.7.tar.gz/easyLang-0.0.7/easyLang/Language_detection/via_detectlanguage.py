#Documentation https://github.com/detectlanguage/detectlanguage-python
#Installation pip install detectlanguage

import detectlanguage

def detect_language(content):
    try:
        api_key = "cd0d7ee1c00134e594282fbb9fd12fdf" #Free

        detectlanguage.configuration.api_key = api_key
        result = detectlanguage.detect(content)
        print(result)
        language_detected = result[0]['language']
        return True, language_detected

    
    except Exception as e:
        print(f"Error in detecting langauge: {e}")
        return False, None
    