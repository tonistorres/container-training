# atividade 5

# lista contendo números inteiros
list_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, 0]

# E ncontra e retorna o maior número impar presente na lista
def maior_impar(lista):
    # criando uma lista vazia que conterá todos números ímpares contido na lista list_integer
    list_impar = []
    # fazendo um laço de repetição for que irá iterar sobre toda lista list_integer
    for i in list_integer:
        # estrutura condicional simples que irá separar da lista list_integer todos os números impares
        if i % 2 != 0:
            # adicionando os números ímpares contidos em list_integer na lista vazia list_impar
            list_impar.append(i)
    # utilizando a função nativa do python max para filtrar o maior número interio impar de list_impar
    return max(list_impar)


# imprimindo o resultado do maior número inteiro ímpar contido em list_integer
print(maior_impar(list_integer))

# E ncontra e retorna o menor número impar presente na lista
# bem essa função segue a mesma dinâmica da primeira
def menor_impar(lista):
    list_impar = []
    for i in list_integer:
        if i % 2 != 0:
            list_impar.append(i)
    return min(list_impar)


print(menor_impar(list_integer))

# E ncontra e retorna o maior e o menor número ímpar presentes na lista
# nesse última função eu só faço a reutilização de código e o que tem
# diferente é que coloco o resultado em uma tupla
def menor_maior_impar(lista):
    result_max = maior_impar(list_integer)
    result_min = menor_impar(list_integer)
    tuple = (result_max, result_min)
    return tuple


print(menor_maior_impar(list_integer))
