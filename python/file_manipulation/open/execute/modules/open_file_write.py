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


def write_add_end_file(Path="file_default.tx", str="\n valeu argus default"):
    try:
        r = open(Path, mode="r")
        f = open(Path, mode="a")
        # método que verifica se o arquivo pode ser lido
        result = r.readable()
        if result:
            # adciona no final do arquivo
            f.write(str)
        r.close()
        f.close()
    except TypeError:
        print("Erro: Faltando passar uma argumento posicional.")
        print(
            "outra possibilidade é não ter passado strings\n como argumento para função"
        )
    except FileNotFoundError:
        print("Erro: Caminho passado como argumento é inválido")
