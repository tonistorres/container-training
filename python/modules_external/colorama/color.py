import colorama
from colorama import Fore, Back, Style

colorama.init()

print(Fore.RED + "some red text")
print(Back.GREEN + "and with a green background")
print(Style.DIM + "and in dim text")
print(Style.RESET_ALL)
print("back to normal now")
