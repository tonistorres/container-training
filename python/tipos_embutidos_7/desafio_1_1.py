back_dict = dict()

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
# https://www.w3schools.com/python/ref_dictionary_items.asp
car_tuple = tuple(car.items())
print("Convertido em Tupla:", car_tuple)
# print(type(car_tuple)) # sim o dado é do tipo tuple

for i in car_tuple:
    back_dict[i[0]] = i[1]  # nesse ponto ele monta o dicionário chave:valor
    # print(back_dict)

print("Dicionário montado:", back_dict)
