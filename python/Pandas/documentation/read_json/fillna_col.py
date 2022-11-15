# Substituir apenas para colunas especificadas
# O exemplo acima substitui todas as células vazias em todo o Data Frame.

# Para substituir apenas valores vazios de uma coluna, especifique o nome da coluna para o DataFrame:

# Exemplo
# Substitua os valores NULL nas colunas "Calorias" pelo número 130:

import pandas as pd
import module_head as rhead

df = pd.read_csv("data.csv")
# rhead.head("*", "Read CSV")
# print(df.to_string())
rhead.head("-", "Atualiza Col Calories")
df["Calories"].fillna("NULO", inplace=True)
print(df.to_string())
