def read_full_file(path):
    r = open(path, mode="r")
    # Esse arquivo pode ser lido?
    result = r.readable()
    if result:
        # lendo o arquivo todo
        print(r.read())
    r.close()


def read_first_line(path):
    # fazendo leitura do arquivo
    r = open(path, mode="r")
    # método que verifica se o arquivo pode ser lido
    result = r.readable()
    if result:

        print(r.readline())

    r.close()


def read_file_convert_list_manipulation(Path):
    # fazendo leitura do arquivo
    r = open(Path, mode="r")
    # método que verifica se o arquivo pode ser lido
    result = r.readable()
    if result:
        list_content = r.readlines()
        print(list_content)
        # list_convert_string = str(list_content)
        # print(Back.GREEN + list_convert_string)
    r.close()


def capture_by_index_in_list(Path, position_list):

    try:
        if type(position_list) != int:
            print("\nposition_list deve ser um número inteiro positivo")
            return
        else:
            # fazendo leitura do arquivo
            r = open(Path, mode="r")
            # método que verifica se o arquivo pode ser lido
            result = r.readable()
            if result:
                list_content = r.readlines()
                print(list_content[int(position_list)])
                list_convert_string = str(list_content[int(position_list)])
                print(list_convert_string)
            r.close()
    except IndexError:
        print("\nÍndice inexistente na Lista. Fora do range!!!")


def read_file_txt_rt(Path):

    r = open(Path, mode="rt")
    result = r.readable()
    if result:
        print("--------------------------")
        print("Efetuando Leitura Arquivo")
        print("--------------------------")
        print(r.read())
    r.close()
