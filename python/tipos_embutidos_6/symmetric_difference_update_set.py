"""
Mantenha tudo, mas não as duplicatas
O symmetric_difference_update()método manterá apenas os elementos
 que NÃO estão presentes em ambos os conjuntos.

"""

# Guarde os itens que não estão presentes em ambos os conjuntos:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

# O symmetric_difference()método retornará um novo conjunto,
#  que contém apenas os elementos que NÃO estão presentes em ambos os conjuntos.
