count = 1
somatorio = 0

while count <= 4:
    nota = int(input(f"Entre com a {count}ª nota:"))
    if nota < 0 or nota > 10:
        while nota < 0 or nota > 10:
            nota = int(input("Nota inválida. Entre com uma nota entre 0 à 10:"))
    count += 1
    somatorio += nota


media = float(somatorio / 4)
if media >= 7:
    print("Aprovado 😀😀😀😀😀")
else:
    print("Reprovado 🥲🥲🥲🥲🥲")
