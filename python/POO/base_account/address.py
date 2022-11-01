class Endereco:
    def __init__(self, estado, cidade, bairro, rua):
        self._estado = estado
        self._cidade = cidade
        self._bairro = bairro
        self._rua = rua

    def get_estado(self):
        return self._estado

    def set_estado(self, estado):
        self._estado = estado

    def get_cidade(self):
        return self._cidade

    def set_cidade(self, cidade):
        self._cidade = cidade

    def get_bairro(self):
        return self._bairro

    def set_bairro(self, bairro):
        self._bairro = bairro

    def get_rua(self):
        return self._rua

    def set_rua(self, rua):
        self._rua = rua

    def __str__(self):
        linha = "-----------------------------------"
        return f"\n{linha}\n Estado: {self._estado}\n Cidade: {self._cidade}\n Bairro: {self._bairro}\n Rua: {self._rua}"
