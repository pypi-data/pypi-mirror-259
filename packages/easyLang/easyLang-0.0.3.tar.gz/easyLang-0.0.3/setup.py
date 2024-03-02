import setuptools
from setuptools import find_packages

setuptools.setup(
    name="easyLang",
    version="0.0.3",
    author="Fizahat",
    description="Language translations & detections module",
    packages=find_packages(),
    install_requires=[
        'detectlanguage',
        'googletrans',
        'deep-translator']
)