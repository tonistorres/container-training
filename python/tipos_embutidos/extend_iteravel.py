"""
Adicionar qualquer iterável
O método extend() não precisa anexar listas,
você pode adicionar qualquer objeto iterável
(tuplas, conjuntos, dicionários etc.).
"""

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
