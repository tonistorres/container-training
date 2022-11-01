class Celular:
    def __init__(self, operadora, ddd, numero):
        self._operadora = operadora
        self._ddd = ddd
        self._numero = numero

    def get_operadora(self):
        return self._operadora

    def set_nome(self, operadora):
        self._operadora = operadora

    def get_ddd(self):
        return self._ddd

    def set_ddd(self, ddd):
        self._ddd = ddd

    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero

    def __str__(self):
        linha = "--------------------------------"
        return f"\n{linha}\n Operadora: {self._operadora}\n DDD: {self._ddd}\n Celular: {self._numero}"
