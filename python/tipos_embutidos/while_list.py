"""

Usando um loop while
Você pode percorrer os itens da lista usando um loop while.

Use a função len() para determinar o comprimento da lista,
 então comece em 0 e faça um loop pelos itens da lista
 consultando seus índices.

Lembre-se de aumentar o índice em 1 após cada iteração.

"""

thislist = ["apple", "banana", "cherry"]
i = 0
# enquanto i for menor que o comprimento da lista faça
while i < len(thislist):
    # imprima cada elemento na posição i do indice da lista
    print(thislist[i])
    # agora pegue i e incremente em mais 1

    i = i + 1
