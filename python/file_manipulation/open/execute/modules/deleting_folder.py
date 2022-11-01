from genericpath import isfile
import os
import colorama
from colorama import Fore, Back, Style

colorama.init()


def check_folder_delete(Path):
    try:
        if os.path.exists(Path):
            print(Fore.CYAN + "Path Successfully")
            os.rmdir(Path)
            print(Fore.RED + "Empty folders, deleted")
        else:
            print(Fore.YELLOW + "Path not Exists")
            exit(1)
    except OSError:
        print(Fore.YELLOW + "Folder not empty")
