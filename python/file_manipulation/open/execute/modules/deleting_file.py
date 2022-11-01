from genericpath import isfile
import os
import colorama
from colorama import Fore, Back, Style

colorama.init()


def check_before_delete(Path, File):
    try:
        if os.path.exists(Path):
            print(Fore.CYAN + "Path Successfully")
            print(f"{Path}/{File}")
            if os.path.isfile(f"{Path}/{File}"):
                print(Fore.BLUE + "The path {} exist".format(Path))
                os.remove(f"{Path}/{File}")
                print(Fore.RED + "remove with successfully!!")
            else:
                print("File not exists")
                exit(1)
        else:
            print(Fore.RED + "Path not Exists")
            exit(1)
    except FileNotFoundError:
        print(Fore.RED + "Erro Exception")
    except IsADirectoryError:
        print(Fore.RED + "File was not passed as a function argument")
