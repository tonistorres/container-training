"""
Definição e uso
O join()método pega todos os itens em um iterável e os une em uma string.

Uma string deve ser especificada como separador.

Sintaxe
string.join(iterable)

"""

myTuple = ("John", "Peter", "Vicky")
myTupe_2 = ("123", "422", "623", "32")

x = "#".join(myTuple)
y = ".".join(myTupe_2)

print(x)
print(y)

# Junte todos os itens de um dicionário em uma string, usando a palavra "TEST" como separador:
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)


print(x)


#

list = ["a", "n", "a"]
unindo = "".join(list)
print(unindo)
