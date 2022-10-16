"""
Percorrer os números de índice
Você também pode percorrer os itens da lista consultando
seu número de índice.
Use as funções range() e len() para criar um iterável adequado.
"""

thislist = ["apple", "banana", "cherry"]
# traduzindo: Percorrer a lista em todo seu tamanho(comprimento)
for i in range(len(thislist)):
    print(thislist[i])
