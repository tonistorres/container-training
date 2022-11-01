# Criar um função que calcule a soma de dois números
def sum(x, y):
    result = x + y
    print("O Resultado da Operação é:{}".format(result))


sum(10, 20)


def calculator_01():
    result = 50 - 5 * 6
    if result <= 20:
        print("O valor é um numero menor igual a 20")
    else:
        print("xablau")


calculator_01()


def calculator_02():
    result = (50 - 5 * 6) / 4
    if result == 5.0:
        print("Resultado igual a 5:{}".format(result))
    else:
        print("xablau")


calculator_02()
