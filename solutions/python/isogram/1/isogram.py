def is_isogram(phrase):
    seen = set()

    for char in phrase:
        if not char.isalpha():
            continue

        if char.lower() in seen:
            return False

        seen.add(char.lower())

    return True