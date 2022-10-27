"""
Definição e uso
O startswith()método retorna True se a string começar com
o valor especificado, caso contrário, False.

Sintaxe
string.startswith(value, start, end)

"""

# Verifique se a string começa com "Hello":

# txt = "Hello, welcome to my world."

# x = txt.startswith("Hello")

# print(x)

# Verifique se a posição 7 a 20 começa com os caracteres "wel":
txt2 = "Hello, welcome to my world."

x2 = txt2.startswith("wel", 7, 20)

print(x2)
