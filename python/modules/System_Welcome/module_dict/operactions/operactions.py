# função cria um dicionário


def screen_dict():
    linha = "**************************************************"
    print(f"\n{linha}\n")
    print(f"Se o Valor for um NÚMERO INTEIRO digite i")
    print(f"Se o Valor for um NÚMERO FLOAT digite f")
    print(f"Se o Valor for um NÚMERO BOLEAN digite b")
    print(f"Se o Valor for uma STRING digite s:")
    print(f"\n{linha}\n")


def creator_dict():
    value_inteiro = 0
    value_float = 0.0
    value_boolean = False
    value_string = ""

    name_dict = input("Informe o nome do dicionário:")
    num_key_value = int(
        input("Informe a quantidade de elementos dentro do dicionário:")
    )
    name_dict = {}

    for item in range(num_key_value):
        key = input("Digite nome chave:")
        screen_dict()
        options = input("Qual Tipagem do Valor:")
        if options == "i":
            value_inteiro = int(input("Digite um Valor do Tipo Inteiro:"))
            name_dict.update({key: value_inteiro})
        elif options == "f":
            value_float = float(input("Digite um Valor do Tipo Float:"))
            name_dict.update({key: value_float})
        elif options == "b":
            value_boolean = bool(
                input("Digite um Valordo Tipo Boleano'True ou False':")
            )
            name_dict.update({key: value_boolean})
        elif options == "s":
            value_string = input("Digite um Valor do Tipo Strng:")
            name_dict.update({key: value_string})
        else:
            print(" Erro valor desconhecido!!")
