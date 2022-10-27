"""

Definição e uso
O maketrans()método retorna uma tabela de mapeamento que pode
ser usada com o método para substituir caracteres especificados.
translate()
Sintaxe
string.maketrans(x, y, z)
"""
# txt = "Hello Sam!"
# mytable = txt.maketrans("S", "P")
# print(txt.translate(mytable))


# Use uma tabela de mapeamento para substituir muitos caracteres:

# txt2 = "Hi Sam!"
# x = "mSa"
# y = "eJo"
# mytable = txt2.maketrans(x, y)
# print(txt2.translate(mytable))


# O terceiro parâmetro na tabela de mapeamento descreve os caracteres
# que você deseja remover da string:

# txt = "Good night Sam!"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# mytable = txt.maketrans(x, y, z)
# print(txt.translate(mytable))


# O maketrans()próprio método retorna um dicionário descrevendo
#  cada substituição, em unicode:

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z))
