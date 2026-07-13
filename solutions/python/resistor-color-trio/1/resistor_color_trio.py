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
    colorone,colortwo,om = colors[0],colors[1],colors[2]

    first = COLORS.index(colorone)
    second = COLORS.index(colortwo)
    manyzero = COLORS.index(om)

    value = (first * 10 + second) * 10 ** manyzero

    unit_index = 0

    while value >= 1000:
        value = value // 1000
        unit_index += 1

    return str(value) + " " + UNITS[unit_index]