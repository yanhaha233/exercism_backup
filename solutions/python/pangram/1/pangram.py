import string

def is_pangram(sentence):
    # string.ascii_lowercase == "abcdefghijklmnopqrstuvwxyz"
    for letter in string.ascii_lowercase:
        if letter not in sentence.lower():
            return False

    return True
