# Exercício 1: No terminal, inicialize duas variáveis a e b,
# sendo a = 10 e b = 5. Mostre o resultado das 7 operações
#  básicas (soma, subtração, multiplicação, divisão, divisão inteira,
#  potenciação e módulo) envolvendo essas variáveis.


def result_operations(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao_real = a / b
    divisao_inteira = a // b
    potenciacao = a**b
    modulo = a % b
    print("Soma: {}".format(soma))
    print("Subtração: {}".format(subtracao))
    print("Multiplicação: {}".format(multiplicacao))
    print("Divisão Real: {}".format(divisao_real))
    print("Divisão Inteira: {}".format(divisao_inteira))
    print("Potenciação: {}".format(potenciacao))
    print("Modulo: {}".format(modulo))


result_operations(20, 4)
