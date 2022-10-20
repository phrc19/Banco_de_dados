from model.servico import Servico
from conexion.oracle_queries import OracleQueries

class ControllerServico:

    def __init__(self):
        pass

    def inserir_servico(self) -> Servico:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente referente ao servico que sera incluido: "))
        ordem_servico = str(input("Insira a ordem de servico referente ao servico que sera incluido: "))
        codigo_servico = str(input("Insira o codigo do servico que sera incluido: "))

        if self.verifica_existencia_servico(oracle, codigo_cliente, ordem_servico, codigo_servico):
            nome = str(input("Insira o nome do servico: "))
            cat = str(input("Insira o categoria do servico: "))
            valor_unitario = str(input("Insira o valor untario: "))
            tempo_execucao = str(input("insira o tempo de execucao: "))
            garantia = str(input("Insira a garantia do servico: "))
            oracle.write(f"insert into servicos values ('{codigo_cliente}', '{ordem_servico}', '{codigo_servico}', '{nome}', '{cat}', '{valor_unitario}', '{tempo_execucao}', '{garantia}')")
            df_servicos = oracle.sqlToDataFrame(f"select codcliente, cod_ordemservico, cod_servico, nome, cat, vlr_unitario, tempo_execuo, garantia from servicos where codcliente = '{codigo_cliente}' and cod_ordemservico = '{ordem_servico}' and cod_servico = '{codigo_servico}'")
            novo_servico = Servico(df_servicos.codcliente.values[0], df_servicos.cod_ordemservico.values[0],
                                   df_servicos.cod_servico.values[0], df_servicos.nome.values[0],
                                   df_servicos.cat.values[0], df_servicos.vlr_unitario.values[0],
                                   df_servicos.tempo_execuo.values[0], df_servicos.garantia.values[0])
            print(novo_servico)
            return novo_servico
        else:
            print("Nao e possivel fazer a insercao com os dados fornecidos")
            return None

    def atualizar_servico(self) -> Servico:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente do servico que deseja atualizar: "))
        ordem_servico = str(input("Insira a ordem de servico que deseja atualizar: "))
        codigo_servico = str(input("Insira o codigo do servico que deseja atualizar: "))

        if not self.verifica_existencia_servico(oracle, codigo_cliente, ordem_servico, codigo_servico):
            novo_codigo_servico = str(input("Insira o codigo do servico atualizado: "))
            if self.verifica_existencia_servico(oracle, codigo_cliente, ordem_servico, novo_codigo_servico):
                novo_nome = str(input("Insira o nome do servico atualizado: "))
                novo_cat = str(input("Insira o categoria do servico atualizado: "))
                novo_valor_unitario = str(input("Insira o valor untario atualizado: "))
                novo_tempo_execucao = str(input("insira o tempo de execucao atualizado: "))
                novo_garantia = str(input("Insira a garantia do servico atualizado: "))
                oracle.write(f"update servicos set cod_servico = '{novo_codigo_servico}', nome = '{novo_nome}', cat = '{novo_cat}', vlr_unitario = '{novo_valor_unitario}', tempo_execuo = '{novo_tempo_execucao}', garantia = '{novo_garantia}' where codclientes = '{codigo_cliente}' and ordensservicos = '{ordem_servico}' and codcliente = '{codigo_servico}'")
                df_servicos = oracle.sqlToDataFrame(f"select codcliente, cod_ordemservico, cod_servico, nome, cat, vlr_unitario, tempo_execuo, garantia from servicos where codcliente = '{codigo_cliente}' and cod_ordemservico = '{ordem_servico}' and cod_servico = '{novo_codigo_servico}'")
                servico_atualizado = Servico(df_servicos.codcliente.values[0], df_servicos.cod_ordemservico.values[0],
                                             df_servicos.cod_servico.values[0], df_servicos.nome.values[0],
                                             df_servicos.cat.values[0], df_servicos.vlr_unitario.values[0],
                                             df_servicos.tempo_execuo.values[0], df_servicos.garantia.values[0])
                print(servico_atualizado)
                return servico_atualizado
            else:
                print("Nao e possivel fazer a atualizacao com os dados fornecidos")
                return None
        else:
            print("Nao e possivel fazer a atualizacao com os dados fornecidos")
            return None

    def excluir_servico(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente do servico que deseja atualizar: "))
        ordem_servico = str(input("Insira a ordem de servico que deseja atualizar: "))
        cod_servico = str(input("Insira o codigo do servico que deseja atualizar: "))

        if not self.verifica_existencia_servico(oracle, codigo_cliente, ordem_servico, cod_servico):
            df_servicos = oracle.sqlToDataFrame(f"select codcliente, cod_ordemservico, cod_servico, nome, cat, vlr_unitario, tempo_execuo, garantia from servicos where codcliente = '{codigo_cliente}' and cod_ordemservico = '{ordem_servico}' and cod_servico = '{cod_servico}'")
            oracle.write(f"delete from servicos where codcliente = '{codigo_cliente}' and cod_ordemservico = '{ordem_servico}' and cod_servico = '{cod_servico}'")
            servico_excluido = Servico(df_servicos.codcliente.values[0], df_servicos.cod_ordemservico.values[0],
                                       df_servicos.cod_servico.values[0], df_servicos.nome.values[0],
                                       df_servicos.cat.values[0], df_servicos.vlr_unitario.values[0],
                                       df_servicos.tempo_execuo.values[0], df_servicos.garantia.values[0])
            print("O servico foi removido com sucesso")
            print(servico_excluido)
        else:
            print("Nao e possivel fazer a exclusao com os dados fornecidos")


    def verifica_existencia_servico(self, oracle: OracleQueries, codigo_cliente: int, ordem_servico: str, codigo_servico: str):
        df_servico = oracle.sqlToDataFrame(f"select codcliente, cod_ordemservico, cod_servico, nome, cat, vlr_unitario, tempo_execuo, garantia from servicos where codcliente = '{codigo_cliente}' and cod_ordemservico = '{ordem_servico}' and cod_servico = '{codigo_servico}'")
        return df_servico.empty
