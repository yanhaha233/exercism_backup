"""根据颜色返回数字，只返回前两个的颜色数字就行"""
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

def value(colors):
    return int(str(COLORS.index(colors[0])) + str(COLORS.index(colors[1])))
