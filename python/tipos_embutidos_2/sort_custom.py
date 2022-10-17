"""
Você também pode personalizar sua própria função usando o
argumento de palavra-chave key = function.
A função retornará um número que será usado para
ordenar a lista (o número mais baixo primeiro):
"""

# Classifique a lista com base em quão próximo o número está de 50:


def myfunc(n):
    # Retorna o valor absoluto de um número
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)


myfunc(100)
