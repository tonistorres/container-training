"""
Por que usar funções do Lambda?
O poder do lambda é melhor mostrado quando você os usa como uma função anônima dentro de outra função.

Digamos que você tenha uma definição de função que recebe um argumento e esse argumento
será multiplicado por um número desconhecido:

"""


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
