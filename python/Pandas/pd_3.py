# Indexação Direta
import pandas as pd
import module_read_files as read_file
import module_head as hreport
import module_fotter as freport


data_file = read_file.read_file_excel_with_decimal_point_sep(
    "python/Pandas/temperature.xlsx", "."
)

# hreport.head("*", "Viewing Report Header")
print(data_file)
# freport.fotter("-", "End report successfully|!!!")

# hreport.head("*", "Indexação Direta")
df = pd.DataFrame(data_file["classification"])
print(df[2])
# freport.fotter("-", "extracted column")
