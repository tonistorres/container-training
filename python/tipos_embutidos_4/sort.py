"""
Definição e uso
O método sort() classifica a lista em ordem
 crescente por padrão.

Você também pode criar uma função para decidir o(s)
critério(s) de classificação.

Sintaxe
list.sort(reverse=True|False, key=myFunc)


"""

cars = ["Ford", "BMW", "Volvo"]

cars.sort(reverse=True)


print(f" Lista reversa(Maior para menor):{cars}")

# A function that returns the 'year' value:
def myFunc(e):
    return e["year"]


cars_f = [
    {"car": "Ford", "year": 2005},
    {"car": "Mitsubishi", "year": 2000},
    {"car": "BMW", "year": 2019},
    {"car": "VW", "year": 2011},
]

cars_f.sort(key=myFunc)

print(cars_f)
