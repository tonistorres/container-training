"""
Adicionar qualquer iterável
O objeto no update()método não precisa ser um conjunto, pode ser qualquer objeto
iterável (tuplas, listas, dicionários etc.).
"""

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
