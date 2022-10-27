"""
Definição e uso
O isprintable()método retorna True se todos os caracteres forem imprimíveis,
caso contrário, False.

Exemplo de nenhum caractere imprimível pode ser retorno de carro e alimentação de linha.

Sintaxe
string.isprintable()

"""
txt = "Hello!\nAre you #1?"

x = txt.isprintable()

print(x)
