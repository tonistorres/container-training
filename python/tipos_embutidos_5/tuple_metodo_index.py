"""
Definição e uso
O método index() encontra a primeira ocorrência do valor especificado.

O método index() gera uma exceção se o valor não for encontrado.
"""

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
try:
    x = thistuple.index(10)
    print(x)
except ValueError:
    print("Variável x não foi encontrada na tuple")
