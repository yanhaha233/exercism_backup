def equilateral(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a and len(set(sides)) == 1


def isosceles(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a and len(set(sides)) <= 2


def scalene(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a and len(set(sides)) == 3
