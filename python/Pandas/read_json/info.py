# Informações sobre os dados
# O objeto DataFrames possui um método chamado info(), que fornece mais informações sobre o conjunto de dados.

# Exemplo
# Imprimir informações sobre os dados:

import pandas as pd

df = pd.read_csv("./data.csv")
print(df.info())
