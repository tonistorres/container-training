back_dict = dict()
car_tuple = dict()
car_dict = dict()

# bem criou uma 1ª função que recebe como parâmetro um dicionário qualquer
# e tipou como retorno uma tupla
def dict_to_tuple(dict_to_convert: dict) -> tuple:
    # utilizou a palavra reservada return para que a condição da tipagem seja
    # verdadeira e possa retornar a tupla, em seguida utilizou o método item()
    # que converte o dicionário em tuplas no formato de chave valor
    return tuple(dict_to_convert.items())


# criou uma função que recebe agora como parâmetro uma tupla e retorna um dicionáro
def tuple_to_dict(tuple_to_convert: tuple) -> dict:
    # criou uma estrutura de uma dicionario vazia para que possa ser preenchida pelo
    # laço de repetção for
    convert_dict = {}
    # percorre todos os elementos da tupla neste caso em especial de par em par
    # ((a,b),(c,d) e monta o dicionario acima declarado vazio pegando os itens
    # da primiera posição do par de tuplas e da segunda representada pelos indices
    # 0 e 1
    for _ in tuple_to_convert:
        convert_dict[_[0]] = _[1]  # montando o novo dicionário
    # como a função foi tipada com retorno utilizou a palavra reservada
    # return retornando um dicionário que é o que o requisto pede
    return convert_dict


# o dicionário do requisito
car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# invocando a primeira função e passando o dicionário como parâmetro
# para ser convertido em tupla
car_tuple = dict_to_tuple(car)

# invocando a segunda função e passando uma tupla que retornará um dicionário
car_dict = tuple_to_dict(car_tuple)
