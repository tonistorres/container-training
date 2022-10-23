"""
Percorrer os números de índice
Você também pode percorrer os itens da tupla consultando seu número de índice.

Use as funções range() e len() para criar um iterável adequado.
"""

thistuple = ("apple", "banana", "cherry")
for index in range(len(thistuple)):
    print(thistuple[index])
