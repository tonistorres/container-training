"""
Definição e uso
O método count() retorna o número de elementos com o valor especificado.

Sintaxe
list.count(valor)
"""

from typing import Counter


fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(f"Impressão cherry {x}")

# Retorna o número de vezes que o valor 9 aparece na lista

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)

print("O numero de vezes que aparece na lista é: {}".format(x))
