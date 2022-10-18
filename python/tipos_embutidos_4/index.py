"""

Definição e uso
O método index() retorna a posição na primeira ocorrência do
 valor especificado.

Sintaxe
list.index(elmnt)

Qual é a posição do valor 32:
Nota: O método index() retorna apenas a primeira ocorrência do valor.
"""

fruits = ["apple", "banana", "cherry"]

x = fruits.index("cherry")

print(f"Retorna a posição do índice onde encontra o elemento:{x}")


fruits = [4, 55, 64, 32, 16, 32]

y = fruits.index(32)

print(f"Retorna o primeiro indice em que se encontra 32 --> {y}")
