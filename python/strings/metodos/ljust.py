"""
Definição e uso
O ljust()método alinhará a string à esquerda, usando um caractere
especificado (o espaço é o padrão) como o caractere de preenchimento.

Sintaxe
string.ljust(length, character)

"""

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")


# Usando a letra "O" como caractere de preenchimento:

txt2 = "banana"

xy = txt2.ljust(20, "O")

print(xy)
