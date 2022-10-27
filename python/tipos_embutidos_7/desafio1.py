"""
Alguém conhece um método que resolva isso de forma mais fácil de uma pancada só:
Tipo eu tenho um dicionário chamado car então quero converter esse dicionário em
tuplas chave e valor e depois quero retornar ele para uma novo dicionário com os
mesmas chaves e valores.

Obs: Sei que parece não fazer sentido mais poderia por exemplo fazer alterações
enquanto era lista e depois retoná-lo como um novo dicionário é mais questão didática.

"""
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

list_keys = []
list_values = []

# 1º convertendo dicionarios em tuplas
for element in car.keys():
    list_keys.append(element)
inputTuple_1 = tuple(list_keys)

for value in car.values():
    list_values.append(value)
inputTuple_2 = tuple(list_values)

# 2º convertendo de tupla para dicionario
if len(inputTuple_1) == len(inputTuple_2):
    resultDictionary = {
        inputTuple_1[i]: inputTuple_2[i] for i, _ in enumerate(inputTuple_2)
    }

print(resultDictionary)
