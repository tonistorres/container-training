"""
Passando uma lista como um argumento
Você pode enviar qualquer tipo de dado de argumento para uma
função (string, número, lista, dicionário etc.), e ele será
tratado como o mesmo tipo de dado dentro da função.

Por exemplo, se você enviar uma lista como argumento,
ela ainda será uma lista quando chegar à função:

"""


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)
