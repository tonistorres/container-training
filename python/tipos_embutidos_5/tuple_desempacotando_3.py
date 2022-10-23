"""
Se o asterisco for adicionado a outro nome de variável que não o último,
o Python atribuirá valores à variável até que o número de valores restantes
corresponda ao número de variáveis ​​restantes.
"""

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(primeiro_elemento, *segundo_elemento, restante) = fruits

print(primeiro_elemento)
print(segundo_elemento)
print(restante)
