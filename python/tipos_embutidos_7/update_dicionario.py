"""
Atualizar dicionário
O update()método atualizará o dicionário com os itens do argumento fornecido.

O argumento deve ser um dicionário ou um objeto iterável com pares chave:valor.

"""

# Atualize o "ano" do carro usando o update() método:

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"year": 2020})
print(thisdict)
