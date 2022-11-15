# Ler arquivos CSV
# Uma maneira simples de armazenar grandes
# conjuntos de dados é usar arquivos
#  CSV (arquivos separados por vírgula).

# Os arquivos CSV contêm texto simples
# e é um formato bem conhecido que pode
#  ser lido por todos, incluindo Pandas.

# Em nossos exemplos, usaremos um arquivo
# CSV chamado 'data.csv'.

# Baixe data.csv . ou Abra data.csv

# Exemplo
# Carregue o CSV em um DataFrame:

import pandas as pd
import module_head as r_read


df = pd.read_csv("./data.csv")
# Dica: use to_string()para imprimir todo o DataFrame.
# Se você tiver um DataFrame grande com muitas linhas,
# o Pandas retornará apenas as 5 primeiras linhas
# e as últimas 5 linhas:
r_read.head(",", "Imprimindo com to_string DataFrame Full")
print(df.to_string())

r_read.head(",", "Imprimindo sem to_string DF Not Full")
print(df.to_string())
