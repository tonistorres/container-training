"""
Obter valores
O values()método retornará uma lista de todos os valores do dicionário.

"""


# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# x = thisdict.values()
# print(x)

# Faça uma alteração no dicionário original e veja se a lista de valores também é atualizada:

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.values()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change
