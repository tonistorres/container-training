# criando arquivo inicial
# bem se o arquivo não existir ele será criado/aberto caso exista será aberto
"""
A função open é a responsável por abrir um arquivo,
tornando possível sua manipulação. Seu único parâmetro
obrigatório é o nome do arquivo. Por padrão, arquivos
são abertos somente para leitura, mas podemos modificar
isto passando o modo com que vamos abrir o arquivo.
No exemplo abaixo, estamos utilizando mode="w", ou seja,
estamos abrindo o arquivo para escrita:
"""
programming_languages = open("languages.txt", mode="w")

# vamos escrever no arquivo aberto
# Para escrevermos um conteúdo em um arquivo utilizamos a função write
# Só é possível escrever em um arquivo após abri-lo em um modo que permita escrita.
programming_languages.write("Java\n")
programming_languages.write("C++\n")
programming_languages.write("C#\n")
programming_languages.write("JavaScript\n")

# agora vou escrever mais alguns elementos numa lista
list_leguages = ["TypeScript\n", "Python\n", "Vba\n"]

# o comando writelines pega todos elementos de uma lista e imprime num arquivo especificado
"""
Para escrever múltiplas linhas podemos utilizar a função writelines.
Repare que a função espera que cada linha tenha seu próprio caractere de separação (\n):
"""
programming_languages.writelines(list_leguages)

# bem podemos escrever em arquivos de várias formas até mesmo com o método print
"""
Assim como podemos redirecionar a saída do nosso programa para a saída de erros,
podemos redirecionar o conteúdo digitado dentro de print para um arquivo.
Ou seja, também podemos escrever em um arquivo através do print.
"""
print(file=programming_languages)

# importantíssimo após terminar as manipulações devidas no arquivo devemos fechá-los
"""
Outro motivo importante para se fechar os arquivos é que normalmente a manipulação
de arquivos é feita através de buffers. Ou seja, a escrita em disco pode não ser imediata.
Quando fechamos o arquivo, garantimos que tudo aquilo que ainda não está escrito seja persistido.
"""
programming_languages.close()
