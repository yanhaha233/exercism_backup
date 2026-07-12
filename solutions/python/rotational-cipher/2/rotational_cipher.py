"""实现凯撒旋转密码"""
import string

def rotate(text, key):
    """将文本中的英文字母向后移动指定的位数。"""
    result = ""
    
    for letter in text:
        if letter in string.ascii_lowercase:
            new_char = chr((ord(letter) - ord("a") + key) % 26 + ord("a"))
            result += new_char
        elif letter in string.ascii_uppercase:
            new_char = chr((ord(letter) - ord("A") + key) % 26 + ord("A"))
            result += new_char
        else:
            result += letter

    return result
