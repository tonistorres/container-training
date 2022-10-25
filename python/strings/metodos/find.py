"""
O find()método encontra a primeira ocorrência do valor especificado.

O find()método retorna -1 se o valor não for encontrado.

O find()método é quase o mesmo que o index() método, a única diferença é que o index()
 método gera uma exceção se o valor não for encontrado. (Veja exemplo abaixo)

"""

txt = "Hello, welcome to my world."

x = txt.find("to")

print(x)


# se o valor não for encontrado

t = "Hello, welcome to my world."

print(t.find("q"))
# print(t.index("q"))
