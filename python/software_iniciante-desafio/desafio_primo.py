# Bootcamp: Programador(a) de Software Iniciante
# Desafio Final
# Módulo 1: Fundamentos Programador de Software Iniciante
# Objetivos de Ensino
# Exercitar os seguintes conceitos trabalhados no Módulo:
# 1. Lógica de programação em Portugol no VisuAlg.
# Enunciado
# O aluno deverá criar um programa para informar se determinado número é primo ou não.
# Atividades
# O aluno deverá criar um programa que informará se determinado número é primo ou não. Esse
# número deve ser informado pelo usuário.
# Um número primo é aquele que só é divisível por 1 e por ele mesmo. O número 1 não é
# considerado um número primo.
# Dizer que um número X é divisível por um número Y quer dizer que o resto da divisão de X
# por Y é igual a zero. Por exemplo, podemos dizer que 6 é divisível por 3, pois 6 dividido por 3
# é igual a 2 e resto 0. Já o número 7 não é divisível por 3, pois 7 dividido por 3 é 2 e sobra 1
# como resto.
# Um exemplo de número primo é o número 13, pois ele é divisível somente por 1 e por 13.
# Ao rodar o programa, ele deve imprimir se o número informado pelo usuário é primo ou não.
# Exemplo de saída considerando o número informado como 10:
# O número 10 não é primo.
# Exemplo de saída considerando o número informado como 13:
# 1O número 13 é primo.
# Durante o questionário, será perguntado se alguns números são primos ou não. Para descobrir
# isso, você deve executar o seu código passando o número da pergunta como entrada para seu
# programa.
# Respostas Finais
# Os alunos deverão desenvolver a prática e, depois, responder às seguintes questões objetivas:
# 2

# bem temos uma função quer recebe ao ser invocada ou executada, exige que o usuário entre com um
# numero inteiro. Depois fazemos um for percorrendo todo o range de 1 ate o numero +1 fazendo uma
# verificação se cores, onde, os numero do range que dividem esse número ficaram colorido no terminal
# na cor azul caso contrario ou seja quando eles não forem divisiveis permaneceram na cor branca no
# terminal. Em seguida criei um contado que irá contar quantas vezes um número é divisível dado o range
# percorrido pelo laço de repetiação for
# https://www.youtube.com/watch?v=Er5Hyd4LyVw


def prime_number(number):
    count_divisible = 0
    for c in range(1, number + 1):
        if number % c == 0:
            count_divisible += 1
            print("\033[34m", end="")
        else:
            print("\033[m", end="")
        print("{}".format(c), end="")
    print(
        "\n\033[31mO numero {} foi divisível {} vezes".format(number, count_divisible)
    )
    if count_divisible == 2:
        print("IS PRIME")
    else:
        print("NOT PRIME")


prime_number(int(input("Digite um número inteiro:")))
