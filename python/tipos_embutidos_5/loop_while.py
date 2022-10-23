"""

Usando um loop while
Você pode percorrer os itens da lista usando um loop while.

Use a função len() para determinar o comprimento da tupla,
então comece em 0 e faça um loop pelos itens da tupla consultando seus índices.

Lembre-se de aumentar o índice em 1 após cada iteração.
"""
# tupla
thistuple = ("apple", "banana", "cherry")
# contador
count = 0
# enquando count for menor que o comprimento da tupla
while count < len(thistuple):
    # print o elemento na posição do index
    print(thistuple[count])
    # incremente em 1 o contando para evitar loop infinito
    count += 1
