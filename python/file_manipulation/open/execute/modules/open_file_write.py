"""
Arquivo Python aberto
O manuseio de arquivos é uma parte importante de qualquer aplicativo da web.

Python tem várias funções para criar, ler, atualizar e deletar arquivos.

Manipulação de arquivos
A função chave para trabalhar com arquivos em Python é a open()função.

A open()função recebe dois parâmetros; nome do arquivo e modo .

Existem quatro métodos (modos) diferentes para abrir um arquivo:

"r"- Leitura - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir

"a"- Append - Abre um arquivo para anexação, cria o arquivo se não existir

"w"- Write - Abre um arquivo para escrita, cria o arquivo caso não exista

"x"- Criar - Cria o arquivo especificado, retorna um erro se o arquivo existir

Além disso você pode especificar se o arquivo deve ser tratado como modo binário ou texto

"t"- Texto - Valor padrão. Modo de texto

"b"- Binário - Modo binário (por exemplo, imagens)


"""
import os
import colorama
from colorama import Fore, Back, Style

colorama.init()


def write_file(Path="default.txt"):
    # abrindo o arquivo
    f = open(Path, mode="w")
    # manipulando o arquivo
    f.write("testando file open_file.py\n")
    f.write("Se não existir a função open\n")
    f.write("irá criar esse arquivo raiz \n")
    f.write(" da pasta, e irá escrever \n")
    f.write("nele, caso exista irá escrever\n")
    f.write(" esse texto no mesmo.\n")
    # Importante: fechando o arquivo
    f.close()


def write_add_end_file(Path, File, str):
    try:

        if os.path.exists(Path):
            print(Fore.CYAN + "Path Successfully")
            if os.path.isfile(f"{Path}/{File}"):
                r = open(f"{Path}/{File}", mode="r")
                f = open(f"{Path}/{File}", mode="a")

                result = r.readable()
                if result:
                    f.write(str)
                    print("Content adding Successfully")
                r.close()
                f.close()

            else:
                print(Fore.RED + "File not exists")
                print(f"{Path}/{File}")
                f = open(f"{Path}/{File}", mode="a")
                create_file = open(f"{Path}/{File}", mode="w")
                create_file.write("")
                print(Fore.GREEN + "File Created.")
                f.write(str)
                print(Fore.BLUE + "Content adding Successfully")
                f.close()
                create_file.close()
                # exit(1)

        else:
            print(Fore.RED + "Path not Exists")
            exit(1)

    except FileNotFoundError:
        print(Fore.RED + "Null value path")
        exit(1)
    except IsADirectoryError:
        print(Fore.YELLOW + "Erro: Path Invalid")
    except ModuleNotFoundError:
        print("Need to install some external module")
        exit(1)
    except NameError:
        print("Problem with colorama module see declarations or reinstallation")
        exit(1)
    except TypeError:
        print("it is necessary to correctly pass all args (path, file.txt, content)")
