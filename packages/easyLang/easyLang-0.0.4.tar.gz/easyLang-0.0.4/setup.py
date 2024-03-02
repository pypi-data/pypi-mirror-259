import setuptools

setuptools.setup(
    name="easyLang",
    version="0.0.4",
    author="Fizahat",
    description="Language translations & detections module",
    packages=["easyLang", "easyLang.Language_detection", "easyLang.Language_translation"],
    install_requires=[
        'detectlanguage',
        'googletrans',
        'deep-translator']
)