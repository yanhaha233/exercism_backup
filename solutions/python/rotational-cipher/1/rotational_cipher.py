import string

def rotate(text, key):
    result = ""
    
    for letter in text:
        if letter in string.ascii_lowercase:
            new_char = chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
            result += new_char
        elif letter in string.ascii_uppercase:
            new_char = chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
            result += new_char
        else:
            result += letter

    return result
