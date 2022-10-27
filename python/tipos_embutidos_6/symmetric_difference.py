# Retorna um conjunto que contém todos os itens de ambos os conjuntos,
# exceto os itens presentes em ambos:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
