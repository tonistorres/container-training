import json
import colorama
from colorama import Fore, Back, Style

colorama.init()


def report_expense(Path):
    try:
        with open(Path, mode="r") as file:
            expense = json.load(file)
            list_expense = []
            for i in range(len(expense)):
                list_expense.append(expense[i]["WHO"])
                for j in range(len(expense)):
                    list_expense.append(expense[i]["WEEK"][j]["NUMBER"])
                    list_expense.append(expense[i]["WEEK"][j]["EXPENSE"])
            # print(type(list_expense))
            print(list_expense)
            # fazer um destructuring ou desmonte aqui no python

    except json.decoder.JSONDecodeError:
        print(Fore.RED + "File json corrupted")
    except FileNotFoundError:
        print(Fore.RED + "Path or File not found")
    except:
        print(
            """
         Tratamento Generico não recomendado.
         Se estourou aqui faça o tratamento
         adequadamente (especifico)
         """
        )
    finally:
        print(Back.RED + "Execução encerrada")


report_expense("data/data.json")
