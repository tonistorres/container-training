import json
import colorama
from colorama import Fore, Back, Style

colorama.init()


def read_file_json(Path):
    try:
        with open(Path, mode="r") as file:
            despesas = json.load(file)
            print(despesas[0])
    except json.decoder.JSONDecodeError:
        print(Fore.RED + "File json corrupted")


read_file_json("data/data.json")
