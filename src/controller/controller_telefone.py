from model.telefone import Telefone
from conexion.oracle_queries import OracleQueries

class ControllerTelefone:

    def __init__(self):
        pass

    def inserir_telefone(self) -> Telefone:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente: "))

        if self.verifica_existencia_telefone(oracle, codigo_cliente):
            numero = str(input("Insira o numero que deseja inserir: "))
            tipo_telefone = str(input("Insira o tipo no numero: "))
            oracle.write(f"insert into telefones values ('{codigo_cliente}', '{numero}', '{tipo_telefone}')")
            df_telefone = oracle.sqlToDataFrame(f"select codcliente, numero, tipo_telefone from telefones where codcliente = '{codigo_cliente}'")
            novo_telefone = Telefone(df_telefone.codcliente.values[0], df_telefone.numero.values[0],
                                     df_telefone.tipo_telefone.values[0])
            print(novo_telefone)
            return novo_telefone
        else:
            print("Nao e possivel fazer a insercao com os dados fornecidos")
            return None

    def atualizar_telefone(self) -> Telefone:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente do telefone que deseja atualizar: "))

        if not self.verifica_existencia_telefone(oracle, codigo_cliente):
            novo_numero = str(input("Insira o numero atualizado: "))
            novo_tipo_telefone = str(input("Insira o tipo do numero atualizado: "))
            oracle.write(f"update telefones set numero = '{novo_numero}', tipo_telefone = '{novo_tipo_telefone}' where codcliente = '{codigo_cliente}'")
            df_telefone = oracle.sqlToDataFrame(f"select codcliente, numero, tipo_telefone from telefones where codcliente = '{codigo_cliente}'")
            telefone_atualizado = Telefone(df_telefone.codcliente.values[0], df_telefone.numero.values[0],
                                           df_telefone.tipo_telefone.values[0])
            print(telefone_atualizado)
            return telefone_atualizado
        else:
            print("Nao e possivel fazer a atualizacao com os dados fornecidos")
            return None

    def excluir_telefone(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente do telefone que deseja atualizar: "))

        if not self.verifica_existencia_telefone(oracle, codigo_cliente):
            df_telefone = oracle.sqlToDataFrame(f"select codcliente, numero, tipo_telefone from telefones where codcliente = '{codigo_cliente}'")
            oracle.write(f"delete from telefones where codcliente = '{codigo_cliente}'")
            telefone_excluido = Telefone(df_telefone.codcliente.values[0], df_telefone.numero.values[0],
                                         df_telefone.tipo_telefone.values[0])
            print("O telefone foi excluido")
            print(telefone_excluido)
        else:
            print("Nao e possivel fazer a exclusao com os dados fornecidos")

    def verifica_existencia_telefone(self, oracle: OracleQueries, codigo_cliente: int = None) -> bool:
        df_telefone = oracle.sqlToDataFrame(f"select codcliente, numero, tipo_telefone from telefones where codcliente = '{codigo_cliente}'")
        return df_telefone.empty
