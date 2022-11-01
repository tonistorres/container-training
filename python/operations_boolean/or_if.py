# bem para trabalharmos com operações booleanas é necessario passar rapidinho pelo
# pelo comando if para fazermos a brincadeira acontecer

# Enunciado: Dado um valor x=10 e y=5 e z=10 responda as seguintes questões:
# Se x ou y forem iguais: imprima na tela "sao iguais" caso contrario "xablau"
# Se x e z são iguais: imprima "somos iguais" caso contrário "xablau"
# Utilizando o operador NOT se x igual a 10: imprima "not é 10", ou seja, negue a operação


def enter_two_number(number_a, number_b):
    if number_a == number_b:
        print("são iguais")
    else:
        print("xablau")


enter_two_number(10, 5)
