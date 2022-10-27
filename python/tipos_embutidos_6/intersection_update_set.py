"""
Mantenha APENAS as duplicatas
O intersection_update()método manterá apenas os itens
 presentes em ambos os conjuntos.
"""

# Mantenha os itens que existem em ambos set x, e set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

# O intersection()método retornará um novo conjunto, que
# contém apenas os itens presentes em ambos os conjuntos.
