import colorama
from colorama import Fore, Back, Style
import pandas as pd

colorama.init()


def read_file_csv(Path):
    try:
        df = pd.read_csv(Path)
        return df
    except FileNotFoundError:
        print(Fore.RED + "Directory or File Invalid!!")
    except:
        print(
            """
         Tratamento Generico não recomendado.
         Se estourou aqui faça o tratamento
         adequadamente (especifico)
         """
        )
    finally:
        print(
            f"""
          ------------------------
          Return Content File CSV
          ------------------------
          """
        )
