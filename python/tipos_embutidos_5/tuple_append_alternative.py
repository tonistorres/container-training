"""
Adicionar itens
Como as tuplas são imutáveis, elas não possuem um método append()
embutido, mas existem outras maneiras de adicionar itens a uma tupla.

Converter em uma lista: Assim como a solução alternativa para alterar uma tupla,
você pode convertê-la em uma lista, adicionar seu(s) item(ns) e convertê-la novamente
em uma tupla.
"""
# tuple
thistuple = ("apple", "banana", "cherry")
# convertendo tuple em lista por meio do método contructor
y = list(thistuple)
# adicionando elemento a lista
y.append("orange")
# convertendo de volta lista em tuple por meio do método construtor
thistuple = tuple(y)
print(thistuple)
