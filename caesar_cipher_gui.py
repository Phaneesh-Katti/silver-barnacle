import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QScrollArea, QTextBrowser, QDialog
from PyQt5.QtGui import QFont
from nltk.corpus import words
from nltk.corpus import wordnet
common_words = set(words.words())

"""
    This class definition creates a GUI for decrypting Caesar Cipher encrypted text. Here's what each method does:

    __init__: Initializes the GUI and calls the init_ui method to set up the user interface.
    init_ui: Sets up the layout and UI elements for the GUI, including labels, text entry, buttons, and their respective actions.
    decrypt: Retrieves the input text, strips any whitespace, and calls the get_top_guesses method to decrypt the input.
    show_shifted_strings: Retrieves the input text, strips any whitespace, and calls the print_shifted_strings method to display all 26 shifted strings.
    clear_input: Clears the input text and result label.
    show_info: Displays information about how the tool works and provides notes on its usage.
    perc_num_words: Calculates the percentage of recognized English words in the decrypted text.
    shifter: Shifts the input string using a given key to decrypt the text.
    num_common_words: Returns a list of tuples containing words from the input text and a boolean indicating if the word is a common English word.
    get_word_meaning: Retrieves the definition of a given word using WordNet.
    get_top_guesses: Finds the top decrypted guesses and calls the print_top_guesses method to display the results.
    print_top_guesses: Formats and displays the top decrypted guesses along with their confidence levels and meanings.
    get_meanings: Retrieves the meanings of common English words in the decrypted text using the get_word_meaning method.
    print_shifted_strings: Generates all 26 shifted strings for the input text and calls the show_shifted_strings_popup method to display them.
    show_shifted_strings_popup: Displays the shifted strings in a popup window.
"""

class CaesarCipherGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Caesar Cipher Decryption')
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel('Enter your encrypted (cipher) text:', self)
        self.label.setFont(QFont('Arial', 12))

        self.text_entry = QTextEdit(self)
        self.text_entry.setFont(QFont('Arial', 10))

        self.decrypt_button = QPushButton('Decrypt', self)
        self.decrypt_button.clicked.connect(self.decrypt)
        self.decrypt_button.setFont(QFont('Arial', 12, QFont.Bold))
        self.decrypt_button.setStyleSheet('QPushButton {background-color: #4CAF50; color: white;}')

        self.result_label = QLabel(self)
        self.result_label.setFont(QFont('Arial', 12))

        self.show_shifted_strings_button = QPushButton('Show All 26 Combinations', self)
        self.show_shifted_strings_button.clicked.connect(self.show_shifted_strings)
        self.show_shifted_strings_button.setFont(QFont('Arial', 12))
        self.show_shifted_strings_button.setStyleSheet('QPushButton {background-color: #007BFF; color: white;}')

        self.clear_button = QPushButton('Clear Input', self)
        self.clear_button.clicked.connect(self.clear_input)
        self.clear_button.setFont(QFont('Arial', 12))
        self.clear_button.setStyleSheet('QPushButton {background-color: #FFC107; color: white;}')

        self.info_button = QPushButton('Info', self)
        self.info_button.clicked.connect(self.show_info)
        self.info_button.setFont(QFont('Arial', 12))
        self.info_button.setStyleSheet('QPushButton {background-color: #6C757D; color: white;}')

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.text_entry)
        vbox.addWidget(self.decrypt_button)
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.show_shifted_strings_button)
        vbox.addWidget(self.clear_button)
        vbox.addWidget(self.info_button)
        vbox.addStretch(1)

        self.setLayout(vbox)

    def decrypt(self):
        inp = self.text_entry.toPlainText().strip()
        if inp:
            self.get_top_guesses(inp)

    def show_shifted_strings(self):
        inp = self.text_entry.toPlainText().strip()
        if inp:
            self.print_shifted_strings(inp)

    def clear_input(self):
        self.text_entry.clear()
        self.result_label.clear()

    def show_info(self):
        info_text = (
            "This tool attempts to decrypt a Caesar Cipher encrypted text.\n\n"
            "How it works:\n"
            "1. Enter your encrypted text in the provided text box.\n"
            "2. Click 'Decrypt' to view the top guesses based on English word recognition.\n"
            "3. Click 'Show All 26 Combinations' to see the shifted strings for all keys.\n\n"
            "Note:\n"
            "- This tool may not work well for very short input or texts with uncommon words.\n"
            "- The 'Show All 26 Combinations' button provides a list of possible decrypted texts.\n"
            "- The confidence level indicates the percentage of recognized English words in the decrypted text."
        )
        info_dialog = QMessageBox()
        info_dialog.setWindowTitle('Information')
        info_dialog.setText(info_text)
        info_dialog.setFont(QFont('Arial', 12))
        info_dialog.exec_()

    def perc_num_words(self, matched_words, total_words):
        return (matched_words / total_words) * 100 if total_words != 0 else 0

    def shifter(self, inp_string, key):
        new_string = ""
        for ch in inp_string:
            if ch.isalpha():
                temp = ord(ch)
                temp -= key
                ch = chr(temp)
            new_string += ch
        return new_string

    def num_common_words(self, inp_string):
        return [(word, word.lower() in common_words) for word in inp_string.split()]

    def get_word_meaning(self, word):
        synsets = wordnet.synsets(word)
        if synsets:
            return synsets[0].definition()
        return f"No definition found for '{word}'"

    def get_top_guesses(self, inp):
        t1, t2, t3, s1, s2, s3, k1, k2, k3 = 0, 0, 0, "", "", "", 0, 0, 0
        words_info1, words_info2, words_info3 = [], [], []

        for key in range(0, 26):
            s = self.shifter(inp, key)
            words_info = self.num_common_words(s)
            x = self.perc_num_words(sum(1 for _, is_common in words_info if is_common), len(inp.split()))
            if x > t1:
                t1, s1, k1, words_info1 = x, s, key, words_info
            elif x > t2:
                t2, s2, k2, words_info2 = x, s, key, words_info
            elif x > t3:
                t3, s3, k3, words_info3 = x, s, key, words_info

        self.top_guesses = {'t1': t1, 's1': s1, 'k1': k1, 'words_info1': words_info1,
                            't2': t2, 's2': s2, 'k2': k2, 'words_info2': words_info2,
                            't3': t3, 's3': s3, 'k3': k3, 'words_info3': words_info3}
        self.print_top_guesses()

    def print_top_guesses(self):
        result = "top guesses:\n"
        if any((self.top_guesses['t1'], self.top_guesses['t2'], self.top_guesses['t3'])):
            result += "{:<5} {:<15} {:<10}\n".format("Key", "Plain Text", "Confidence")
            if self.top_guesses['t1']:
                result += "{:<5} {:<15} {:<10}\n".format(self.top_guesses['k1'], self.top_guesses['s1'], self.top_guesses['t1'])
                result += self.get_meanings(self.top_guesses['words_info1'], self.top_guesses['k1'])
            if self.top_guesses['t2']:
                result += "{:<5} {:<15} {:<10}\n".format(self.top_guesses['k2'], self.top_guesses['s2'], self.top_guesses['t2'])
                result += self.get_meanings(self.top_guesses['words_info2'], self.top_guesses['k2'])
            if self.top_guesses['t3']:
                result += "{:<5} {:<15} {:<10}\n".format(self.top_guesses['k3'], self.top_guesses['s3'], self.top_guesses['t3'])
                result += self.get_meanings(self.top_guesses['words_info3'], self.top_guesses['k3'])
        else:
            result += "Sorry, could not crack the cipher."
        self.result_label.setText(result)

    def get_meanings(self, words_info, key):
        meanings = f"\nMeanings for Key: {key}\n"
        for word, is_common in words_info:
            if is_common:
                meaning = self.get_word_meaning(word.lower())
                meanings += f"{word}: {meaning}\n"
        return meanings

    def print_shifted_strings(self, inp):
        shifted_strings = []
        for key in range(26):
            shifted_string = self.shifter(inp, key)
            shifted_strings.append(f"Key {key}: {shifted_string}")
        self.show_shifted_strings_popup(shifted_strings)

    def show_shifted_strings_popup(self, shifted_strings):
        popup = QDialog(self)
        popup.setWindowTitle("Shifted Strings")
        popup.setGeometry(200, 200, 600, 400)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_content = QTextBrowser()
        scroll_content.setFont(QFont('Arial', 10))

        for shifted_string in shifted_strings:
            scroll_content.append(shifted_string)

        scroll_area.setWidget(scroll_content)

        layout = QVBoxLayout(popup)
        layout.addWidget(scroll_area)
        popup.setLayout(layout)

        popup.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CaesarCipherGUI()
    window.show()
    sys.exit(app.exec_())
