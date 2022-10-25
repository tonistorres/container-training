"""
Definição e uso
O isdigit()método retorna True se todos os caracteres forem dígitos, caso contrário, False.
Expoentes, como ², também são considerados um dígito.
"""

txt = "50800"

x = txt.isdigit()

print(x)

a = "\u0030"  # unicode for 0
b = "\u00B2"  # unicode for ²

print(a.isdigit())
print(b.isdigit())
