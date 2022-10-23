"""
Python - Atualizar Tuplas
As tuplas são imutáveis, o que significa que você não pode alterar,
 adicionar ou remover itens depois que a tupla for criada.
Mas existem algumas soluções alternativas.
Você pode converter a tupla em uma lista, alterar a lista e
convertê-la novamente em uma tupla.
"""
# tupla
x = ("apple", "banana", "cherry")
# convertendo em lista utilizando o contrutor para coverter tupla em lista
y = list(x)
# alterando a lista
y[1] = "kiwi"
# converttendo novamente em tupla utiliza o construtor para converter lista em tupla
x = tuple(y)
# imprimindo tupla alterada
print(x)
