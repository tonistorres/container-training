from cell import Celular
from python.POO.base_account.address import Endereco


class Cliente:
    def __init__(self, first_name, last_name, celular: Celular, endereco: Endereco):
        self._first_name = first_name
        self._last_name = last_name
        self._Celular = celular
        self._Endereco = endereco

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_Endereco(self):
        return self._Endereco

    def set_Endereco(self, Endereco):
        self._Endereco = Endereco

    def __str__(self):
        linha = f"----------------------------------"
        return f"\n{linha}\n First Name:{self._first_name}\n Last Name: {self._last_name}\n Celular: {self._Celular}\n Estado: {self._Endereco}\n{linha}\n"
