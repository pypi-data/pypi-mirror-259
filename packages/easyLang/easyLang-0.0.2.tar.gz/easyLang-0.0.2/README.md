# easyLang - Language Detection and Translation Module

## Overview

This module provides a simple and efficient solution for language detection and translation within your applications. Whether you need to identify the language of a given text or translate content from one language to another, easyLang has you covered.

## Features

1. **Language Detection:** Easily determine the language of a given text using advanced language detection algorithms.

2. **Language Translation:** Seamlessly translate text from one language to another with support for a wide range of language pairs.

3. **User-Friendly API:** A straightforward API design makes it easy to integrate language detection and translation into your applications.

## Installation

```bash
pip install easyLang
```

## Usage

```bash
from easyLang.Language_detection.via_detectlanguage import detect_language

file_path = "data/german.txt"
_, language = detect_language(file_path)
```

## Supported Languages
For language codes and supported language pairs, refer to the ISO 639-1 language codes and supported language pairs documentation.

## Contributing
If you find a bug, have a feature request, or want to contribute to the project, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](https://opensource.org/license/MIT).
