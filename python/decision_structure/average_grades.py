# Dado as notas de um aluno criar um algoritmo que calcule se esse aluno foi
# aprovado ou reprovado

nota_1 = float(input("Digite a media do 1° Bimestre:"))
nota_2 = float(input("Digite a media do 2° Bimestre:"))
nota_3 = float(input("Digite a media do 3° Bimestre:"))
nota_4 = float(input("Digite a media do 4° Bimestre:"))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media < 7:
    print("infelizmente sua média foi baixa %.2f" % media, "Você esta reprovado")
else:
    print("Parabéns você foi aprovado no seletivo da EMBRAER")
