"""
O que é um Módulo?
Considere um módulo como sendo o mesmo que uma biblioteca de código.
Um arquivo contendo um conjunto de funções que você deseja incluir em seu aplicativo.

Criar um módulo
Para criar um módulo basta salvar o código desejado em um arquivo com a extensão de arquivo .py:
"""


def greeting_system(name):
    return "Hello, " + name + " " + "Welcome System"


def greeting_work(name):
    str = ""
    str += "Olá!!, Tenha um bom serviço" + name
    return str


def greeting_product(first_name, last_name):
    str = ""
    str += (
        "Hello!!"
        + first_name
        + " "
        + last_name
        + " "
        + "Welcome to the Product Register."
    )
    return str
