"""
Argumentos arbitrários, *args
Se você não souber quantos argumentos serão passados ​​para sua função,
adicione um *antes do nome do parâmetro na definição da função.

Dessa forma, a função receberá uma tupla de argumentos e poderá acessar os itens de acord
"""


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")
