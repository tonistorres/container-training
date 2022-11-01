# Doc: https://docs.python.org/pt-br/3/tutorial/introduction.html#numbers
# Divisão (/) sempre retorna ponto flutuante (float).
#  Para fazer uma divisão pelo piso e receber um inteiro
# como resultado (descartando a parte fracionária)
# você pode usar o operador //; para calcular o resto
#  você pode usar o %:


def division_in_python():
    result_01 = 17 / 3  # classic division returns a float
    result_02 = 17 // 3  # floor division discards the fractional part
    result_03 = 17 % 3  # the % operator returns the remainder of the division
    print("Resultado divisão 17 / 3 : {}".format(result_01))
    print("Resultado divisão 17 // 3 : {}".format(result_02))
    print("Resultado divisão 17 % 3 : {}".format(result_03))


division_in_python()
