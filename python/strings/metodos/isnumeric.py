"""
Definição e uso
O isnumeric()método retorna True se todos os caracteres forem numéricos (0-9), caso contrário, False.

Expoentes, como ² e ¾ também são considerados valores numéricos.

"-1"e "1.5"NÃO são considerados valores numéricos, pois todos os caracteres na string
 devem ser numéricos, e the -e the .não são.

"""

a = "\u0030"  # unicode for 0
b = "\u00B2"  # unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
