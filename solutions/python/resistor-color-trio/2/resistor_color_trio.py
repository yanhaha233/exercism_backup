"""根据三个颜色来写欧姆数，前两个转为数字，第三个转为欧姆"""
UNITS = ["ohms","kiloohms","megaohms","gigaohms"]

COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

def label(colors):
    first_color,second_color,third_color, *_ = colors

    first = COLORS.index(first_color)
    second = COLORS.index(second_color)
    third = COLORS.index(third_color)

    value = (first * 10 + second) * 10 ** third

    unit_index = 0

    while value >= 1000:
        value = value // 1000
        unit_index += 1

    return str(value) + " " + UNITS[unit_index]