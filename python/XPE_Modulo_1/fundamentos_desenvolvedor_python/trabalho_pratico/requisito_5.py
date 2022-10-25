"""
5. Crie um código que realize o somatório de todos os caracteres da seguinte string:
numero = '127957'
Para resolver este problema, considere as seguintes dicas:
• A soma deverá ser 1 + 2 + 7 + 9 + 5 + 7 = 𝟑𝟏;
• Utilize o laço de repetição for … in ; para percorrer cada caractere da string;
• Utilize a conversão do tipo string para o tipo inteiro ( int(caractere) ) para converter os
caracteres em valores numéricos;
•
Utilize uma variável auxiliar, soma , para acumular o somatório dos valores.
"""

numero = "127957"


def somatorio():
    soma = 0
    for caracter in numero:
        soma += int(caracter)
    print(f"O valor do Somatório é:", soma)


somatorio()
