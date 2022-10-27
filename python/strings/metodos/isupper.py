"""
Definição e uso
O isupper()método retorna True se todos os caracteres
 estiverem em maiúsculas, caso contrário, False.

Números, símbolos e espaços não são verificados, apenas caracteres alfabéticos.

Sintaxe
string.isupper()

"""

txt = "THIS IS NOW!"

x = txt.isupper()

print(x)


a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print("Resultado a: ", a.isupper())
print("Resultado b:", b.isupper())
print("Resultado c: ", c.isupper())
