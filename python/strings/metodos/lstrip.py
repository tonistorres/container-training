"""
Definição e uso
O lstrip()método remove quaisquer caracteres iniciais
(espaço é o caractere inicial padrão a ser removido)

Sintaxe
string.lstrip(characters)


"""

# Remova os espaços à esquerda da string:

# txt = "     banana     "

# x = txt.lstrip()

# print("of all fruits", x, "is my favorite")


# Remova os caracteres principais:
txt2 = ",,,,,ssaaww.....banana"

xy = txt2.lstrip(",.asw")

print(xy)
