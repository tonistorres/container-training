# Você pode alterar o número máximo de linhas com a
#  mesma instrução.

# Exemplo
# Aumente o número máximo de linhas para exibir
# todo o DataFrame:

import pandas as pd
import module_head as rhead

pd.options.display.max_rows = 100

df = pd.read_csv("data.csv")
rhead.head("*", "Preview Report Max Rows")
print(df)
