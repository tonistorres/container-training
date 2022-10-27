"""
O splitlines()método divide uma string em uma lista.
 A divisão é feita em quebras de linha.

Sintaxe
string.splitlines(keeplinebreaks)

"""


# Divida uma string em uma lista onde cada linha é um item de lista:

# txt = "Thank you for the music\nWelcome to the jungle"

# x = txt.splitlines()

# print(x)

# Divida a string, mas mantenha as quebras de linha:

txt2 = "Thank you for the music\nWelcome to the jungle"

x2 = txt2.splitlines(True)

print(x2)
