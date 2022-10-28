def area_square(lado):
    area = lado**2
    return area


# utilizando sintaxe lambada
def area_square_lambda():
    return lambda lado: lado**2


def area_triangle(base, height):
    area = (base * height) / 2
    return area


def area_triangle_lambda(default=2):
    return lambda base, height: (base * height) / default


def area_rectangle(base, height):
    return base * height
