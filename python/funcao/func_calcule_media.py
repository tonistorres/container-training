def calculo_media():

    somatorio_notas = 0

    for n in range(1, 5):
        value = float(input("digite a {}ª nota:".format(n)))
        somatorio_notas += value

    media = somatorio_notas / 4

    if media < 7:
        print("Você está reprovado.")
    else:
        print("Você foi aprovado")


calculo_media()
