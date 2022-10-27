"""
Definição e uso
O split()método divide uma string em uma lista.

Você pode especificar o separador, o separador padrão é qualquer espaço em branco.

Nota: Quando maxsplit for especificado, a lista conterá o número
especificado de elementos mais um .

"""

txt = "welcome to the jungle"

x = txt.split()

print(x)


# Divida a string, usando vírgula, seguida por um espaço, como separador:

txt2 = "hello, my name is Peter, I am 26 years old"

xy = txt2.split(", ")

print(xy)


# Divida a string em uma lista com no máximo 2 itens:

txt3 = "apple#banana#cherry#orange"

# definindo o parâmetro maxsplit para 1, retornará uma lista com 2 elementos!
xyz = txt3.split("#", 1)

print(xyz)
