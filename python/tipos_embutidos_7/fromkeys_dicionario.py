"""
Definição e uso
O fromkeys()método retorna um dicionário com as chaves especificadas
e o valor especificado.

Sintaxe
dict.fromkeys(keys, value)
Crie um dicionário com 3 chaves, todas com o valor 0:
"""

x = ("key1", "key2", "key3")
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)


# x = ("key1", "key2", "key3")

# thisdict = dict.fromkeys(x)

# print(thisdict)
