from model.endereco import Endereco
from conexion.oracle_queries import OracleQueries

class ControllerEndereco:

    def __init__(self):
        pass

    def inserir_endereco(self) -> Endereco:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente referente ao qual deseja cadastrar o endereco: "))

        if self.verifica_existencia_endereco(oracle, codigo_cliente):
            cep = str(input("Insira o cep que deseja inserir: "))
            logradouro = str(input("Insira o nome da rua: "))
            municipio = str(input("Insira o municipio: "))
            uf = str(input("Insira a sigla do estado: "))
            numero = str(input("Insira o numero: "))
            complemento = str(input("Caso queira, insira o complemento: )"))
            oracle.write(f"insert into enderecos values ('{codigo_cliente}', '{cep}', '{logradouro}', '{municipio}', '{uf}', '{numero}', '{complemento}')")
            df_endereco = oracle.sqlToDataFrame(f"select codcliente, cep, logradouro, municipio, uf, numero, complemento from enderecos where codcliente = '{codigo_cliente}'")
            novo_endereco = Endereco(df_endereco.codcliente.values[0], df_endereco.cep.values[0],
                                     df_endereco.logradouro.values[0], df_endereco.municipio.values[0],
                                     df_endereco.uf.values[0], df_endereco.numero.values[0],
                                     df_endereco.complemento.values[0])
            print(novo_endereco)
            return novo_endereco
        else:
            print("Nao e possivel fazer a insercao com os dados fornecidos")
            return None

    def atualizar_endereco(self) -> Endereco:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente referente ao qual deseja atualizar o endereco: "))
        cep = str(input("Insira o cep do endereco anterior: "))

        if not self.verifica_existencia_endereco(oracle, codigo_cliente):
            novo_cep = str(input("insira o cep atualizado: "))
            novo_logradouro = str(input("Insira nome da rua atualizado: "))
            novo_municipio = str(input("Insira o municipio atualizado: "))
            novo_uf = str(input("Insira a sigla do estado atualizada: "))
            novo_numero = str(input("Insira o numero atualizado: "))
            novo_complemento = str(input("Caso queira, insira o complemento atualizado: )"))
            oracle.write(f"update enderecos set cep = '{novo_cep}', logradouro = '{novo_logradouro}', municipio = '{novo_municipio}', uf = '{novo_uf}', numero = '{novo_numero}', complemento = '{novo_complemento}' where codcliente = '{codigo_cliente}'")
            df_endereco = oracle.sqlToDataFrame(f"select codcliente, cep, logradouro, municipio, uf, numero, complemento from enderecos where codcliente = '{codigo_cliente}'")
            endereco_atualizado = Endereco(df_endereco.codcliente.values[0], df_endereco.cep.values[0],
                                           df_endereco.logradouro.values[0], df_endereco.municipio.values[0],
                                           df_endereco.uf.values[0], df_endereco.numero.values[0],
                                           df_endereco.complemento.values[0])
            print(endereco_atualizado)
            return endereco_atualizado
        else:
            print("Nao e possivel fazer a atualizacao com os dados fornecidos")
            return None

    def excluir_endereco(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente referente ao qual deseja excluir o endereco: "))

        if not self.verifica_existencia_endereco(oracle, codigo_cliente):
            df_endereco = oracle.sqlToDataFrame(f"select codcliente, cep, logradouro, municipio, uf, numero, complemento from enderecos where codcliente = '{codigo_cliente}'")
            oracle.write(f"delete from enderecos where codcliente = '{codigo_cliente}'")
            endereco_excluido = Endereco(df_endereco.codcliente.values[0], df_endereco.cep.values[0],
                                         df_endereco.logradouro.values[0], df_endereco.municipio.values[0],
                                         df_endereco.uf.values[0], df_endereco.numero.values[0],
                                         df_endereco.complemento.values[0])
            print("Endereco removido com sucesso")
            print(endereco_excluido)
        else:
            print("Nao e possivel fazer a exclusao com os dados fornecidos")

    def verifica_existencia_endereco(self, oracle: OracleQueries, codigo_cliente: int):
        df_endereco = oracle.sqlToDataFrame(f"select codcliente, cep, logradouro, municipio, uf, numero, complemento from enderecos where codcliente = '{codigo_cliente}'")
        return df_endereco.empty
