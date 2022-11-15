# max_rows
# O número de linhas retornadas é definido nas configurações de opção do Pandas.

# Você pode verificar o número máximo de linhas do seu sistema com a pd.options.display.max_rowsinstrução.

# Exemplo
# Verifique o número máximo de linhas retornadas:

import pandas as pd

print(pd.options.display.max_rows)

# No meu sistema o número é 60, o que significa que se
#  o DataFrame contiver mais de 60 linhas, a
# print(df)instrução retornará apenas os
# cabeçalhos e as primeiras e últimas 5 linhas.

# Você pode alterar o
#  número máximo de linhas com a mesma instrução.
