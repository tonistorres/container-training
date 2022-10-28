"""
A declaração de pausa
Com a instrução break podemos parar o loop
 mesmo se a condição while for verdadeira:

"""

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
