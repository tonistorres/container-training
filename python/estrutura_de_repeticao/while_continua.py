"""
A declaração continua
Com a instrução continue podemos parar a iteração
atual e continuar com a próxima:
"""

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # Continue para a próxima iteração se i for 3:
    print(i)
