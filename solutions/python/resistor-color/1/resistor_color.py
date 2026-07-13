"""根据颜色返回数值"""
COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]


def color_code(color):
    """返回单个颜色的数值"""

    return COLORS.index(color)


def colors():
    """返回全部颜色"""

    return COLORS
