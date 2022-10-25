"""
Definição e uso
O isidentifier()método retorna True se a string for um identificador válido, caso contrário, False.

Uma string é considerada um identificador válido se contiver apenas letras alfanuméricas (az)
e (0-9) ou sublinhados (_).
Um identificador válido não pode começar com um número nem conter espaços.

"""
txt = "Demo"

x = txt.isidentifier()

print(x)

# COMO SE FOSSEMOS USAR PARA IDENTIFICAR SE A VARIÁVEL É VÁLIDA COISA ASSIM
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
