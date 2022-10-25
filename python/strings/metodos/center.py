"""
Método Python String center()

Exemplo
Imprima a palavra "banana", ocupando o espaço de 20 caracteres, com "banana" no meio:
Definição e uso
O center()método irá centralizar a string, usando um caractere especificado
(o espaço é o padrão) como o caractere de preenchimento.

"""

txt = "banana"

x = txt.center(20)

print(x)


"""
Usando a letra "O" como caractere de preenchimento:
"""
txt_2 = "banana"

x1 = txt_2.center(20, "O")

print(x1)
