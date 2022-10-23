"""
A palavra-chave del pode excluir a tupla completamente:
"""

thistuple = ("apple", "banana", "cherry")
del thistuple
# da um erro na hora da impressão porque não existe mais tuple para imprimir
print(thistuple)  # this will raise an error because the tuple no longer exists
