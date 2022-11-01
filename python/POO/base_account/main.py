from cell import Celular
from python.POO.base_account.client import Cliente
from python.POO.base_account.address import Endereco
from python.POO.base_account.account import Conta


class Main:

    # 1º Cadastrar Celular (Coposição)
    celular = Celular("Claro", 99, 984526378)
    # 2º Cadastrar Endereco (Composição)
    endereco = Endereco("Maranhão", "Alto Alegre", "Centro", "Dico Veiga")
    # 3º Vamos cadastrar um Cliente
    cliente = Cliente(
        "Tonis",
        "Ferreira",
        celular,
        endereco,
    )
    # 4º Preprando o cenário das Transações bancárias
    conta = Conta(cliente.get_first_name(), 239259)
    conta.deposita(1000)
    conta.sacar(10)
    conta.sacar(990)
    conta.sacar(1)
    print(conta)
