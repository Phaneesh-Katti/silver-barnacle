# silver-barnacle
## Automated Caesar-Cipher Decryption Tool
<br>

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Description

The Caesar Cipher Decryption Tool is a Python-based utility that helps decrypt text encrypted using the Caesar Cipher. It provides both a command-line interface (CLI) and a graphical user interface (GUI) for easy and efficient decryption.

## Features

- Decrypts text using the Caesar Cipher.
- Top 3 guesses for the decrypted text based on English word recognition.
- Shows all 26 combinations for in-depth analysis.
- Modern GUI design for user-friendly interaction.

## Installation



1. Clone the repository:

    ```bash
    git clone https://github.com/Phaneesh-Katti/silver-barnacle.git
    cd silver-barnacle
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements_gui.txt
    ```
3. Download 'words' and 'wordnet' from nltk:

    ```bash
    python
    ```
    ```bash
    import nltk
    ```
    ```bash
    nltk.download('words')
    ```
    ```bash
    nltk.download('wordnet')
    ```

## Usage


## Screenshots

### GUI Version
```bash
python caesar_cipher_gui.py
```

<div align="center">
  <img src="screenshots/gui-screenshot-window.png" alt="GUI Window" width="400">
  <p><em>GUI Window</em></p>
</div>
<br><br>
<div align="center">
  <img src="screenshots/gui-screenshot-info.png" alt="General info" width="400">
  <p><em>General info</em></p>
</div>
<br><br>
<div align="center">
  <img src="screenshots/gui-screenshot-decrypt.png" alt="Automatic Decryption Top Results" width="400">
  <p><em>Automatic Decryption Top Results</em></p>
</div>
<br><br>
<div align="center">
  <img src="screenshots/gui-screenshot-all-combos.png" alt="View All Decrypted Combinations" width="400">
  <p><em>View All Decrypted Combinations</em></p>
</div>

