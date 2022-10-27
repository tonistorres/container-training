import mysql.connector

conexao = mysql.connector.connect(
    host="localhost", user="root", password="1020", database="bdyoutube"
)
cursor = conexao.cursor()
venda_id = 1
comando = f"DELETE FROM tb_vendas WHERE venda_id={venda_id}"
cursor.execute(comando)
conexao.commit()  # edita o banco de dados

cursor.close()
conexao.close()

# create
# produto_nome= "Desinfetante 1000ml"
# venda_valor=6.50
# comando = f'INSERT INTO tb_vendas(produto_nome, venda_valor) VALUES ("{produto_nome}",{venda_valor})'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# read
# cursor = conexao.cursor()
# comando= f'SELECT * FROM tb_vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() # ler o banco de dados
# print(resultado)
#
# cursor.close()
# conexao.close()

# update
# produto_nome = "Agua Sanitaria 500ml"
# venda_id = 1
# comando = (
#     f'UPDATE tb_vendas SET produto_nome="{produto_nome}" WHERE venda_id={venda_id}'
# )
# cursor.execute(comando)
# conexao.commit()  # edita o banco de dados
