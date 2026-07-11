def is_valid(isbn):
    if not isbn:
        return False

    if len(isbn.replace("-","")) != 10:
        return False

    if isbn[-1] != 'X' and not isbn[-1].isdigit():
        return False
    
    isbn_list = []
    for char in isbn:
        if char.isdigit():
            isbn_list.append(char)

    if isbn[-1] == 'X':
        isbn_list.append(10)

    result = 0
    total = 10
    for i in isbn_list:
        result += int(i) * total
        total -= 1

    return result % 11 == 0
