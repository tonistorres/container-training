"""
Valor do parâmetro padrão
O exemplo a seguir mostra como usar um valor de parâmetro padrão.

Se chamarmos a função sem argumento, ela usará o valor padrão:

"""


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
