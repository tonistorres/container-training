import pandas as pd

# separador decimal ponto
def read_file_excel_with_decimal_point_sep(Path, sep):
    number_initial_lines = 3
    number_final_lines = 3
    excel_file = pd.ExcelFile(Path)
    df2 = pd.read_excel(excel_file, sheet_name="Sheet1", decimal=sep)

    linha = "*************************************"

    return f"{df2}"


#     print(
#         f"""-----------------------------------------------
#    Analysis  Report Data Set Pandas
# -----------------------------------------------
# 1- Print the first 3 lines of the report:\n{df2.head(number_initial_lines)}\n{linha}
# 2- Print the final 3 lines of the report:\n{df2.tail(number_final_lines)}\n{linha}
# 3- Print type data inferred by pandas:\n{df2.dtypes}
# 4- Print info basic about the data frame:\n{df2.columns}
# """
#     )


# read_file_excel_with_decimal_point_sep("python/Pandas/temperature.xlsx", ".")

# separador decimal vírgula
def read_file_xlsx_sep_decimalread_file_excel_with_decimal_comma_sep(Path, sep):
    excel_file = pd.ExcelFile(Path)
    df2 = pd.read_excel(excel_file, sheet_name="Sheet2", decimal=sep)
    linha = "*************************************"

    return f"{linha}\nReading Report Excel:\n{linha}{df2}\n{linha}\n End of the read file Excel(xlsx)"


#     print(
#         f"""-----------------------------------------------
#    Analysis  Report Data Set Pandas
# -----------------------------------------------
# 1- Print the first 3 lines of the report:\n{df2.head(2)}\n{linha}
# 2- Print the final 3 lines of the report:\n{df2.tail(2)}\n{linha}
# 3- Print type data inferred by pandas:\n{df2.dtypes}
# 4- Print info basic about the data frame:\n{df2.columns}
# """
#     )


# read_file_xlsx_sep_decimalread_file_excel_with_decimal_comma_sep(
#     "python/Pandas/temperature.xlsx", ","
# )
