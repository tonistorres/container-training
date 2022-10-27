"""
Percorrer um dicionário
Você pode percorrer um dicionário usando um forloop.

Ao percorrer um dicionário, o valor de
retorno são as chaves do dicionário, mas também
existem métodos para retornar os valores .


"""

# Imprima todos os nomes de chave no dicionário, um por um:

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

for x in thisdict:
    print(x)


# Imprima todos os valores no dicionário, um por um:

for element in thisdict:
    print(thisdict[element])
