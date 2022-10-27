# Adicione um novo item ao dicionário original e veja se a
# lista de chaves também é atualizada:

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change
