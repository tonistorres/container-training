# Você pode obter o tipo de dados de qualquer objeto
#  usando a função type():
str = "hello world"
num_int = 20
num_float = 20.5
num_complex = 1j
list_python = ["apple", "banana", "cherry"]
estrutura_dados_tupla = ("apple", "banana", "cherry")
range_default = range(6)
estrutura_dicionario = {"name": "John", "age": 36}
estrutura_set = {"apple", "banana", "cherry"}
estutura_frozenset = frozenset({"apple", "banana", "cherry"})
tip_boleano = True
tip_byte = b"Hello"
tip_byte_array = bytearray(5)
tip_memory_view = memoryview(bytes(5))
tip_None = None


def func_types(x):
    print(type(x))


func_types(str)
func_types(num_int)
func_types(num_float)
func_types(num_complex)
func_types(list_python)
func_types(estrutura_dados_tupla)
func_types(range_default)
func_types(estrutura_dicionario)
func_types(estrutura_set)
func_types(estutura_frozenset)
func_types(tip_boleano)
func_types(tip_byte)
func_types(tip_byte_array)
func_types(tip_memory_view)
func_types(tip_None)
