# Atividade 1
import numpy as np
import pandas as pd
import read_csv as r_csv
import module_head as r_preview

result_read_file = r_csv.read_file_csv("bike-sharing.csv")
# r_preview.head(
#     "*", "Contando todos os Valores de \n    diferentes colunas Method: count"
# )
# print(result_read_file.count())

# # https://acervolima.com/valores-de-contagem-no-dataframe-pandas/
# r_preview.head("*", "Printar anos 2011 \n    representado com valores 0(ZERO)")
# print(result_read_file[result_read_file["year"] == 0]["registered"].count())

# # https://acervolima.com/valores-de-contagem-no-dataframe-pandas/
# r_preview.head("/", "Printar anos 2012 \n    representado com valore 1(UM)")
# print(result_read_file[result_read_file["year"] == 1]["registered"].count())

# # https://www.youtube.com/watch?v=AxELwcccxyE
# r_preview.head("/", "Numeros de Locaçẽso Feitas 2011/2012")
# print(
#     "Nº Locações Feitas 2011:",
#     result_read_file[result_read_file["year"] == 0]["total_count"].sum(),
# )
# print(
#     "Nº Locaçẽos Feitas 2012:",
#     result_read_file[result_read_file["year"] == 1]["total_count"].sum(),
# )
# print("Nº Total de Bicicletas Alugadas:", result_read_file["total_count"].sum())
# r_preview.head(",", "Preview Lines Columns Metodh Shape")
# print(result_read_file.shape)

# r_preview.head(",", "Preview Column windspeed Method:mean")
# print(result_read_file["windspeed"].mean())

# r_preview.head(",", "Preview Column temp Method: mean")
# print(result_read_file["temp"].mean())

# r_preview.head("/", "Grupo de Média por\n    estação do ano ")

# result_read_file["nova_coluna"] = result_read_file.groupby(["season"])[
#     "total_count"
# ].mean()
# print(result_read_file["nova_coluna"].dropna(axis=0))

# r_preview.head("/", "Respondendo Questões 8 e 9")

# print(
#     "Estacao com MAIOR MÉDIA de Aluguéis: QUESTAO 8-->>",
#     result_read_file["nova_coluna"].max(),
# )
# print(
#     "Estacao com MENOR MÉDIA de Aluguéis QUESTAO 9-->>",
#     result_read_file["nova_coluna"].min(),
# )


# r_preview.head(",", "Grupo de registros MAIOR ")
# print(
#     "Nº ",
#     result_read_file.groupby(["season"])["total_count"].max(),
# )

# print(result_read_file["season"].value_counts(dropna=False).max())

# r_preview.head(",", "Época do Ano com MENOR Média de Contratação de Bicicleta")
# print(result_read_file["season"].value_counts(dropna=False).mean())
# print(result_read_file["season"].value_counts(dropna=False).min())
r_preview.head("/", "Horário do Dia \n    que tem maior média locação ")
result_read_file["nova_coluna"] = result_read_file.groupby(["hour"])[
    "total_count"
].mean()
print(result_read_file["nova_coluna"].dropna(axis=0))

print(
    " QUESTAO 10-->>",
    result_read_file["nova_coluna"].max(),
)

print(
    " QUESTAO 11-->>",
    result_read_file["nova_coluna"].min(),
)
