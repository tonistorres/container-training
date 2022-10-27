"""
Definição e uso
O setdefault()método retorna o valor do item com a chave especificada.

Se a chave não existir, insira a chave, com o valor especificado, veja o exemplo abaixo

Sintaxe
dictionary.setdefault(keyname, value)

"""
# Obtenha o valor do item "modelo":

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

x = car.setdefault("model", "Bronco")

print(x)
