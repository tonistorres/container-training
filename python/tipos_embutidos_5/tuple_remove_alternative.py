"""
Remover itens
Nota: Você não pode remover itens em uma tupla.

As tuplas não podem ser alteradas, portanto, você não pode remover
itens dela, mas pode usar a mesma solução alternativa que usamos
para alterar e adicionar itens de tupla

"""
# tuple imutável
thistuple = ("apple", "banana", "cherry")
# convertendo em lista
y = list(thistuple)
# removendo da lista
y.remove("apple")
# convertendo em tupe novamente
thistuple = tuple(y)
# imprimindo resultado na tela
print(thistuple)
