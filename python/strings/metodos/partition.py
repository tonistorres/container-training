"""
O partition()método procura uma string especificada e divide a
string em uma tupla contendo três elementos.

O primeiro elemento contém a parte antes da string especificada.

O segundo elemento contém a string especificada.

O terceiro elemento contém a parte após a string.

Nota: Este método procura a primeira ocorrência da string especificada.

"""

txt = "I could eat bananas all day"

x = txt.partition("bananas")

# print(x)


# Se o valor especificado não for encontrado, o método partition()
#  retornará uma tupla contendo: 1 - a string inteira, 2 - uma string vazia,
# 3 - uma string vazia:


txt2 = "I could eat bananas all day"

xy = txt2.partition("apples")

print(xy)
