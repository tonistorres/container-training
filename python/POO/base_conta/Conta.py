from Cliente import Cliente


class Conta:
    def __init__(self, cliente: Cliente, numero_conta):
        self._Cliente = cliente
        self._numero_conta = numero_conta
        self.__saldo = 0

    def deposita(self, valor):
        try:
            if valor < 0:
                raise Exception()  # lanço a exceção
            else:
                self.__saldo += valor
        except:
            if valor < 0:
                print("Sistema não Aceita Deposito de Valores Negativo")
                exit(1)  # sair do sistema
        finally:
            print("Operação de Depósito")

    def sacar(self, valor):
        try:
            saldo_em_conta = self.__saldo - valor
            if saldo_em_conta < 0:
                raise Exception()  # lanço a exceção
            else:
                self.__saldo -= valor
        except:
            if saldo_em_conta < 0:  # trato a exceção
                print("Não tem Saldo Suficiente ")
            exit(1)  # sair do sistema
        finally:
            print("Operação de Saque")

    # sobrescrita do método mágico __str__
    def __str__(self):
        linha = f"----------------------------------"
        return f"\n{linha}\n Titular: {self._Cliente}\n Número Conta:{self._numero_conta}\n Saldo Conta:{self.__saldo}\n {linha}\n"
