# A delpalavra-chave excluirá o conjunto completamente:


def del_exclude():
    try:
        thisset = {"apple", "banana", "cherry"}
        del thisset
        print(thisset)
    except NameError:
        print("Não existe mais conjunto foi excluído completamente")


del_exclude()
