"""
4. Crie um código declarando as seguintes variáveis do tipo string:

Em seguida, realize as seguintes transformações nas variáveis:
• Transforme todos os caracteres das variáveis em maiúsculo;
• Transforme todos os caracteres das variáveis em minúsculo;
• Exiba a posição do caractere ã, se presente, em cada uma das variáveis;
• Exiba o número de caracteres de cada variável;
• Remova os pontos (.) e o hífen (–) da variável cpf .

"""


# variáveis do tipo string
nome = "João da Silva"
cidade = "São Paulo"
cpf = "123.456.789-00"

# Transforme todos os caracteres das variáveis em maiúsculo;
# print(f"MAIÚSCULO:{nome.upper()}")

# Transforme todos os caracteres das variáveis em minúsculo
# print(f"minúsculo:{nome.lower()}")

# O find()método encontra a primeira ocorrência do valor especificado.
# Exiba a posição do caractere ã, se presente, em cada uma das variáveis;

print("Posição em nome: ", nome.find("ã"))
# print("Posição em cidade: ", cidade.find("ã"))

# Exiba o número de caracteres de cada variável;
# print("Numero de caracter: ", len(nome))
# print("Numero de caracter: ", len(cidade))
# print("Numero de caracter: ", len(cpf))

#


# def remove():
#     string = cpf
#     str_remove_hifen = ""
#     str_remove_ponto = ""
#     for caracter in string:
#         if caracter == "-":
#             str_remove_hifen = string.replace("-", "")
#     for caracter_ponto in str_remove_hifen:
#         if caracter_ponto == ".":
#             str_remove_ponto = str_remove_hifen.replace(".", "")
#     print(str_remove_ponto)


# remove()
