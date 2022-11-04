lista = [
    ["PI", 13],
    ["PI", 5],
    ["PI", 6],
    ["PI", 49],
    ["PI", 8],
]

# setando a posição das sub-lista no dado do tipo inteiro
def func(list_position):
    return list_position[1]


# por baixo dos panos o sort realiza um for ou while
# como cada item da lista é uma outra lista quando ele
# passa item por item o que acontece que eu defino a posição
# de qual elemento eu quero que ordene, em nosso caso eu
# defini a ordenação pelo dados di tipo inteiro e para
# que ocorra a execução da função passo ela como argumento
# para o método sort
lista.sort(key=func)
print(lista)
