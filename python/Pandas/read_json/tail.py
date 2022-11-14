# Há também um tail()método para visualizar as últimas
#  linhas do DataFrame.

# O tail()método retorna os cabeçalhos e um número
# especificado de linhas, começando na parte inferior.

# Exemplo
# Imprima as últimas 5 linhas do DataFrame:

import pandas as pd

df = pd.read_csv("./data.csv")

print(df.tail())
