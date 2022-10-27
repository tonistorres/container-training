"""
Você também pode usar o pop()método para remover um item,
mas esse método removerá o último item. Lembre-se de que os
conjuntos não são ordenados, então você não saberá qual item será removido.

O valor de retorno do pop()método é o item removido.
Nota: Os conjuntos não são ordenados , portanto, ao usar o pop()método,
você não sabe qual item será removido.

"""

# PARA SER SINCERO NÃO É UMA BOA PRÁTICA USAR O POP EM CONJUNTOS JÁ QUE NUNCA SABEMOS
# QUAL SERÁ O ÚLTIMO DA VEZ, OU SEJA, OS CONJUNTOS NÃO TEM ORDENAÇÃO SÁO ALEATORIOS.
# Remova o último item usando o pop() método:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
