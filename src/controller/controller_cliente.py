from model.cliente import Cliente
from conexion.oracle_queries import OracleQueries

class ControllerCliente:

    def __init__(self):
        pass

    def inserir_cliente(self) -> Cliente:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente: "))

        if self.verifica_existencia_cliente(oracle, codigo_cliente):
            nome = str(input("Insira o nome do cliente: "))
            oracle.write(f"insert into clientes values ('{codigo_cliente}', '{nome}')")
            df_cliente = oracle.sqlToDataFrame(f"select codcliente, nome from clientes where codcliente = '{codigo_cliente}'")
            novo_cliente = Cliente(df_cliente.codcliente.values[0], df_cliente.nome.values[0])
            print(novo_cliente)
            return novo_cliente
        else:
            print("Nao e possivel fazer a insercao com os dados fornecidos")
            return None

    def atualizar_cliente(self) -> Cliente:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente: "))

        if not self.verifica_existencia_cliente(oracle, codigo_cliente):
            novo_nome = str(input("Insira o nome do cliente: "))
            oracle.write(f"update clientes set nome = '{novo_nome}' where codcliente = '{codigo_cliente}'")
            df_cliente = oracle.sqlToDataFrame(f"select codcliente, nome from clientes where codcliente = '{codigo_cliente}'")
            cliente_atualizado = Cliente(df_cliente.codcliente.values[0], df_cliente.nome.values[0])
            print(cliente_atualizado)
            return cliente_atualizado
        else:
            print("Nao e possivel fazer a atualizacao com os dados fornecidos")
            return None

    def excluir_cliente(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente: "))

        if not self.verifica_existencia_cliente(oracle, codigo_cliente):
            df_cliente = oracle.sqlToDataFrame(f"select codcliente, nome from clientes where codcliente = '{codigo_cliente}'")
            oracle.write(f"delete from telefones where codcliente = '{codigo_cliente}'")
            oracle.write(f"delete from enderecos where codcliente = '{codigo_cliente}'")
            oracle.write(f"delete from servicos where codcliente = '{codigo_cliente}'")
            oracle.write(f"delete from ordensservicos where codcliente = '{codigo_cliente}'")
            oracle.write(f"delete from clientes where codcliente = '{codigo_cliente}'")
            cliente_excluido = Cliente(df_cliente.codcliente.values[0], df_cliente.nome.values[0])
            print("Cliente removido com sucesso")
            print(cliente_excluido)
        else:
            print("Nao e possivel fazer a exclusao com os dados fornecidos")

    def verifica_existencia_cliente(self, oracle: OracleQueries, codigo_cliente: int = None) -> bool:
        df_cliente = oracle.sqlToDataFrame(f"select codcliente, nome from clientes where codcliente = '{codigo_cliente}'")
        return df_cliente.empty
