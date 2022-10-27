"""
orindex() método encontra a última ocorrência do valor especificado.

orindex() método gera uma exceção se o valor não for encontrado.

O rindex()método é quase o mesmo que o rfind() método. Veja exemplo abaixo.

Sintaxe
string.rindex(value, start, end)
"""

txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)
