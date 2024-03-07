import nltk
from nltk.corpus import wordnet

common_words = set(nltk.corpus.words.words())

def perc_num_words(matched_words, total_words):
    """
    Calculates percentage of words in a string that are in common_words
    
    Args:
        matched_words (int): Number of words in common_words in the string
        total_words (int): Total number of words in the string
    
    Returns:
        float: Percentage of words in common_words or 0 if total_words = 0
    """
    return (matched_words / total_words) * 100 if total_words != 0 else 0


def shifter(inp_string, key):
    """
    Shifts all alphabetic characters in a string by a given key

    Args:
        inp_string (str): String to shift
        key (int): Key to shift by

    Returns:
        str: Shifted string
    """
    new_string = ""
    for ch in inp_string:
        if ch.isalpha():
            temp = ord(ch)
            temp -= key
            ch = chr(temp)
        new_string += ch
    return new_string


def num_common_words(inp_string):
    """
    Returns a list of tuples where each tuple contains a word and a boolean indicating if
    the word is in common_words.

    Args:
        inp_string (str): String to check for common words

    Returns:
        list: List of tuples where each tuple contains a word and a boolean indicating if
            the word is in common_words
    """
    return [(word, word.lower() in common_words) for word in inp_string.split()]


def get_word_meaning(word):
    """
    Returns the definition of a word from WordNet.

    If the word has no definition, return a string indicating that.

    Args:
        word (str): Word to get the definition of

    Returns:
        str: Definition of the word
    """
    synsets = wordnet.synsets(word)
    if synsets:  # If the word has a synset (i.e. a group of words with similar meanings)
        definition = synsets[0].definition()  # Get the definition of the first synset
        return definition  # Return the definition
    return f"No definition found for '{word}'"  # If no synset found, return a string indicating that


t1, t2, t3, s1, s2, s3, k1, k2, k3 = 0, 0, 0, "", "", "", 0, 0, 0
words_info1, words_info2, words_info3 = [], [], []  # Declare these variables globally

def get_top_guesses():
    """
    Finds the top 3 decryptions of the ciphertext based on the number of common words.

    For each possible key (0-25), shifts the ciphertext by that key and calculates the
    percentage of common words in the resulting decryption. If the percentage is greater
    than the threshold for the lowest ranked decryption, the decryption is added to the list
    of top guesses.

    The top 3 decryptions are stored in the global variables t1, t2, and t3, along with their
    respective keys (k1, k2, k3) and word information (words_info1, words_info2, words_info3).
    """
    global t1, t2, t3, s1, s2, s3, k1, k2, k3, words_info1, words_info2, words_info3
    for key in range(0, 26):
        s = shifter(inp, key)  # Shift the ciphertext by the current key
        words_info = num_common_words(s)  # Get the word information of the decryption
        x = perc_num_words(  # Calculate the percentage of common words
            sum(1 for _, is_common in words_info if is_common), num_inp_words
        )
        if x > t1:  # If the percentage is greater than the threshold for the lowest ranked
            t1, s1, k1, words_info1 = x, s, key, words_info  # Add the decryption to the list of top guesses
        elif x > t2:
            t2, s2, k2, words_info2 = x, s, key, words_info
        elif x > t3:
            t3, s3, k3, words_info3 = x, s, key, words_info

def print_meanings(words_info, key):
    """
    Prints the meanings of the common words in the decryption of the ciphertext, given the key.

    Parameters:
        words_info (list): List of tuples containing the word and a boolean indicating if it is common
        key (int): Key of the decryption
    """
    print(f"\nMeanings for Key: {key}")  # Print the key
    for word, is_common in words_info:  # Iterate over the words and their common status
        if is_common:  # If the word is common, get its meaning
            meaning = get_word_meaning(word.lower())  # Get the meaning of the word
            print(f"{word}: {meaning}")  # Print the word and its meaning

def print_top_guesses():
    """
    Prints the top 3 guesses for the ciphertext, along with their keys, plain texts,
    and corresponding confidence percentages.

    If there are no valid decryptions, prints a message indicating this.
    """
    
    global t1, t2, t3, s1, s2, s3, k1, k2, k3, words_info1, words_info2, words_info3
    print("Top 3 guesses:")
    if any((t1, t2, t3)):  # If there are valid decryptions
        print("{:<5} {:<15} {:<10}".format("Key", "Plain Text", "Confidence"))
        if t1:  # If there is a top 1 guess
            print("{:<5} {:<15} {:<10}".format(k1, s1, t1))
            print_meanings(words_info1, k1)
        if t2:  # If there is a top 2 guess
            print("{:<5} {:<15} {:<10}".format(k2, s2, t2))
            print_meanings(words_info2, k2)
        if t3:  # If there is a top 3 guess
            print("{:<5} {:<15} {:<10}".format(k3, s3, t3))
            print_meanings(words_info3, k3)
    else:  # If there are no valid decryptions
        print("Sorry, could not crack the cipher.")

def print_shifted_strings():
    """
    Prints the shifted strings for all keys.

    This function prints the shifted strings for all 26 possible keys
    of the Caesar cipher. The input text is shifted by each key and the
    resulting string is printed along with the key.

    Parameters:
        None

    Returns:
        None
    """

    print("\nShifted Strings for All Keys:")
    for key in range(26):
        shifted_string = shifter(inp, key)  # Shift the text by the key
        print(f"Key {key}: {shifted_string}")  # Print the shifted string and key

if __name__ == "__main__":
    try:
        inp = input("Note: This program may not work well for very short input.\nEnter your encrypted (cipher) text: ")
        num_inp_words = len(inp.split())

        get_top_guesses()
        print_top_guesses()

        user_input = input("Are you satisfied with the top 3 guesses? (y/n): ").lower()
        if user_input == 'n':
            print_shifted_strings()

    except Exception as e:
        print(f"Error: {e}. Please enter a valid input.")
