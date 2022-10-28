"""
Loops aninhados
Um loop aninhado é um loop dentro de um loop.
O "loop interno" será executado uma vez para
cada iteração do "loop externo":

"""
# Imprima cada adjetivo para cada fruta:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
