import modules.open_file_read as read_operations
import modules.open_file_write as write_fake

# escrevendo arquivo
# write_fake.write_file("modules/open.txt")
# fazendo a leitura completa do arquvio
# read_operations.read_full_file("modules/open.txt")
# fazendo a leitura da primeira linha do arquivo
# read_operations.read_first_line("modules/open.txt")
# convertendo conteudo do arquivo em lista para manipulação por índice entre outros
# read_operations.read_file_convert_list_manipulation("modules/open.txt")
# pegando um índice da lista
# read_operations.capture_by_index_in_list("modules/open.txt", 5)

# abrindo arquivo txt utilizando mode=rt (r-leitura t- arquivo texto)
# read_operations.read_file_txt_rt("modules/open.txt")
# adicionando nova tecnologia
write_fake.write_add_end_file("modules/open.txt", "-----------------------\n")
write_fake.write_add_end_file("modules/open.txt", "Adicionando Tecnologias\n")
write_fake.write_add_end_file("modules/open.txt", "-----------------------\n")
write_fake.write_add_end_file("modules/open.txt", "JavaScript\n")
write_fake.write_add_end_file("modules/open.txt", "Java desktop\n")
write_fake.write_add_end_file("modules/open.txt", "Python\n")
write_fake.write_add_end_file("modules/open.txt", "Sql-Server\n")
write_fake.write_add_end_file("modules/open.txt", "No-SQL\n")
write_fake.write_add_end_file("modules/open.txt", "Mongo DB\n")
write_fake.write_add_end_file("modules/open.txt", "Node\n")
write_fake.write_add_end_file("modules/open.txt", "Ract\n")
read_operations.read_file_txt_rt("modules/open.txt")
# write_fake.write_file()
