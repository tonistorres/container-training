""""
Operação	Símbolo
Adição	+
Subtração	-
Multiplicação	*
Divisão Real	/
Divisão Inteiro	//
Exponenciação	**
Resto da Divisão	%

"""


from unittest import result


def soma(a, b):
    result = a + b
    print("O resultado da soma é: %d" % result)


soma(10, 20)


def subtracao(a, b):
    result = a - b
    print("O resultado da subtração é: %d" % result)


subtracao(20, 5)


def multiplicacao(a, b):
    result = a * b
    print("O resultado da multiplicação é:%d" % result)


multiplicacao(4, 5)


def divisao_real(a, b):
    result = a / b
    print("O resultado da divisão real é %.2f" % result)


divisao_real(20.4, 2)


def divisao_inteiros(a, b):
    result = a // b
    print("O resultado de inteiros é %d" % result)


divisao_inteiros(5, 4)


def exponeciacao(a):
    result = a**a
    print("O resultado é: %.2f" % result)


exponeciacao(8)


def resto_divisao(a, b):
    result = a % b
    print("O resto da divisao é %d" % result)


resto_divisao(5, 4)
