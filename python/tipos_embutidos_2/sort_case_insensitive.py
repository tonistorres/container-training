"""
Por padrão, o método sort() diferencia maiúsculas
 de minúsculas, resultando em todas as letras maiúsculas
 classificadas antes das minúsculas:
"""

# A classificação com distinção entre maiúsculas e minúsculas
#  pode fornecer um resultado inesperado

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


"""
Felizmente, podemos usar funções internas como funções-chave
 ao classificar uma lista.

Portanto, se você deseja uma função de classificação que
não diferencia maiúsculas de minúsculas, use str.lower
como uma função de chave:
"""

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)
