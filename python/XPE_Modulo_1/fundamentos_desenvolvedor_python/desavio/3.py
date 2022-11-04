# atividade 3 Enunciado

import math


def circle_area(radius):
    try:
        pi = math.pi
        if type(radius) == int or type(radius) == float:
            area = pi * (radius**2)
            print("Circle Area is: %.2f:" % area)
        else:
            print("Type data invalid")
    except TypeError:
        print("required positional argument")


circle_area(8)


def circle_area_two(radius, PI):
    try:
        if (type(radius) == int or type(radius) == float) and (
            type(PI) == int or type(PI) == float
        ):
            area = PI * (radius**2)
            print("Circle Area is: %.2f:" % area)
        else:
            print("Type data invalid")
    except TypeError:
        print("required positional argument")


circle_area_two(8, 3.14)
