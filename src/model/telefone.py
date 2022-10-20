class Telefone:

    def __init__(self, codigo_cliente: int, numero: str, tipo_numero: str):
        self.codigo_cliente = codigo_cliente
        self.numero = numero
        self.tipo_numero = tipo_numero

    def set_numero(self, numero: str):
        self.numero = numero

    def set_tipo_numero(self, tipo_numero):
        self.tipo_numero = tipo_numero

    def get_codigo_cliente(self) -> int:
        return self.codigo_cliente

    def get_numero(self) -> str:
        return self.numero

    def get_tipo_numero(self) -> str:
        return self.tipo_numero

    def __str__(self) -> str:
        return "Codigo do cliente: " + str(self.get_codigo_cliente()) + "\nNumero de contato: " + self.get_numero() + "\nTipo do numero: " + self.get_tipo_numero()