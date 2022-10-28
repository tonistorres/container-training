"""
Ou use a mesma definição de função para fazer as duas funções, no mesmo programa:
"""


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
