class Cliente:

    def __init__(self, codigo_cliente: int, nome: str):
        self.codigo_cliente = codigo_cliente
        self.nome = nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_nome(self) -> str:
        return self.nome

    def get_codigo_cliente(self) -> int:
        return self.codigo_cliente

    def __str__(self) -> str:
        return "Codigo do cliente: " + str(self.get_codigo_cliente()) + "\nNome do cliente: " + self.get_nome()
