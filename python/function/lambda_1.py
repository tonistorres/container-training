"""
Python Lambda
Uma função lambda é uma pequena função anônima.

Uma função lambda pode receber qualquer número de argumentos, mas pode ter apenas uma expressão.

Sintaxe
lambda arguments : expression
A expressão é executada e o resultado é retornado:
"""


x = lambda a: a + 10
print(x(5))

# Multiplique argumento apor argumento be retorne o resultado:

y = lambda a, b: a * b
print(y(5, 6))

# Resuma argument a, b, and ce retorne o resultado:
xy = lambda a, b, c: a + b + c
print(xy(5, 6, 2))
