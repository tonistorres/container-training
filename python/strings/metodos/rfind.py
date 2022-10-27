"""
Definição e uso
O rfind()método encontra a última ocorrência do valor especificado.

O rfind()método retorna -1 se o valor não for encontrado.

O rfind()método é quase o mesmo que o rindex() método. Veja exemplo abaixo.

Sintaxe
string.rfind(value, start, end)
"""

# Onde no texto está a última ocorrência da string "casa"?:


# txt = "Mi casa, su casa."

# x = txt.rfind("casa")

# print(x)

# Onde no texto está a última ocorrência da letra "e"?:
# txt2 = "Hello, welcome to my world."

# x2 = txt2.rfind("e")

# print(x2)

# Onde no texto está a última ocorrência da letra "e" quando você pesquisa apenas
# entre a posição 5 e 10?:

# txt4 = "Hello, welcome to my world."

# x4 = txt4.rfind("e", 5, 10)

# print(x4)

# Se o valor não for encontrado, o método rfind()
#  retornará -1, mas o método rindex() irá gerar uma exceção:
txt5 = "Hello, welcome to my world."

print(txt5.rfind("q"))
print(txt5.rindex("q"))
