# Digite sua idade

idade = int(input("Digite sua idade"))

if idade >= 18:
    print("Você já é maior de idade ")
elif idade > 15 and idade < 18:
    print("Infanto Juvenil")
else:
    print("Menor de idade")
