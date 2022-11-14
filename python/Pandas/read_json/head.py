# Visualizando os dados
# Um dos métodos mais usados ​​para obter uma visão geral
# rápida do DataFrame, é o head()método.

# O head()método retorna os cabeçalhos e um número
#  especificado de linhas, começando do topo.

# Exemplo
# Obtenha uma visão geral rápida imprimindo as primeiras 10
#  linhas do DataFrame:

# Nota: se o número de linhas não for especificado, o head()
# método retornará as 5 primeiras linhas.

import pandas as pd

df = pd.read_csv("./data.csv")

print(df.head(10))
