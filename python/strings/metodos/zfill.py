"""

Definição e uso
O zfill()método adiciona zeros (0) no início da string, até atingir o
 comprimento especificado.

Se o valor do parâmetro len for menor que o comprimento da string,
 nenhum preenchimento será feito.

Sintaxe
string.zfill(len)

"""

# Preencha a string com zeros até que tenha 10 caracteres:

txt = "50"

x = txt.zfill(10)

print(x)


# Preencha as strings com zeros até que tenham 10 caracteres:

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
