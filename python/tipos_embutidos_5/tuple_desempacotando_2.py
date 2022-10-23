"""
Se o número de variáveis ​​for menor que o número de valores,
você pode adicionar um * ao nome da variável e os valores
serão atribuídos à variável como uma lista
"""

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(primeiro_elemento, segundo_elemento, *restante_dos_elementos_em_outra_lista) = fruits

print(primeiro_elemento)
print(segundo_elemento)
print(restante_dos_elementos_em_outra_lista)
