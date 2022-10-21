conjunto = [4, 42, 52, 88, 3, 9, 11, 15, 5, 65]
numero = 0
i = 0

while i < len(conjunto):
    if conjunto[i] > numero:
        numero = conjunto[i]
    i += 1
    print(numero)
