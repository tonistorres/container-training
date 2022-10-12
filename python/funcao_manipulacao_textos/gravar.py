"""
Modo	Descrição
r	Abre o arquivo somente para leitura.
O arquivo deve já existir.
r+	Abre o arquivo para leitura e escrita. O arquivo deve já existir.
A escrita começa a partir da primeira linha e, caso exista algo escrito no arquivo, as linhas serão reescritas, conforme formos escrevendo.
w	Abre o arquivo somente para escrita, no início do arquivo.
Apagará o conteúdo do arquivo se ele já existir. Criará um arquivo novo se não existir.
w+	Abre o arquivo para escrita e leitura, apagando o conteúdo preexistente.
a	Abre o arquivo para escrita no final do arquivo.
Não apaga o conteúdo preexistente.
a+	Abre o arquivo para escrita no final do arquivo e leitura.
"""


arquivo = open("./data.txt", "w")
arquivo.write("Curso Python \n")
arquivo.write("Aula Prática Fundação Bradesco")
arquivo.close()
