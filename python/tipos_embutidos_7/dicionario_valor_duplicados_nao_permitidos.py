"""
Valores duplicados substituirão os valores existentes:


"""

# neste caso o year 2020 sobrescreve o year: 1964
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print(thisdict)
# Para determinar quantos itens um dicionário possui, use a len()função:
print(len(thisdict))
