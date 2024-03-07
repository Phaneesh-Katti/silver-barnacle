import nltk
from nltk.corpus import wordnet

common_words = set(nltk.corpus.words.words())

def perc_num_words(matched_words, total_words):
    return (matched_words / total_words) * 100 if total_words != 0 else 0

def shifter(inp_string, key):
    new_string = ""
    for ch in inp_string:
        if ch.isalpha():
            temp = ord(ch)
            temp -= key
            ch = chr(temp)
        new_string += ch
    return new_string

def num_common_words(inp_string):
    return [(word, word.lower() in common_words) for word in inp_string.split()]

def get_word_meaning(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return synsets[0].definition()
    return f"No definition found for '{word}'"

t1, t2, t3, s1, s2, s3, k1, k2, k3 = 0, 0, 0, "", "", "", 0, 0, 0
words_info1, words_info2, words_info3 = [], [], []  # Declare these variables globally

def get_top_guesses():
    global t1, t2, t3, s1, s2, s3, k1, k2, k3, words_info1, words_info2, words_info3
    for key in range(0, 26):
        s = shifter(inp, key)
        words_info = num_common_words(s)
        x = perc_num_words(sum(1 for _, is_common in words_info if is_common), num_inp_words)
        if x > t1:
            t1, s1, k1, words_info1 = x, s, key, words_info
        elif x > t2:
            t2, s2, k2, words_info2 = x, s, key, words_info
        elif x > t3:
            t3, s3, k3, words_info3 = x, s, key, words_info

def print_meanings(words_info, key):
    print(f"\nMeanings for Key: {key}")
    for word, is_common in words_info:
        if is_common:
            meaning = get_word_meaning(word.lower())
            print(f"{word}: {meaning}")

def print_top_guesses():
    global t1, t2, t3, s1, s2, s3, k1, k2, k3, words_info1, words_info2, words_info3
    print("Top 3 guesses:")
    if any((t1, t2, t3)):
        print("{:<5} {:<15} {:<10}".format("Key", "Plain Text", "Confidence"))
        if t1:
            print("{:<5} {:<15} {:<10}".format(k1, s1, t1))
            print_meanings(words_info1, k1)
        if t2:
            print("{:<5} {:<15} {:<10}".format(k2, s2, t2))
            print_meanings(words_info2, k2)
        if t3:
            print("{:<5} {:<15} {:<10}".format(k3, s3, t3))
            print_meanings(words_info3, k3)
    else:
        print("Sorry, could not crack the cipher.")

def print_shifted_strings():
    print("\nShifted Strings for All Keys:")
    for key in range(26):
        shifted_string = shifter(inp, key)
        print(f"Key {key}: {shifted_string}")

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
