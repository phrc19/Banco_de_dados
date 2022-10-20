from model.ordem_servico import OrdemServico
from conexion.oracle_queries import OracleQueries

class ControllerOrdemServico:

    def __init__(self):
        pass

    def inserir_ordem_servico(self) -> OrdemServico:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente: "))
        codigo_ordem = str(input("Insira o codigo de ordem de servico: "))

        if self.verifica_existencia_ordem_servico(oracle, codigo_cliente, codigo_ordem):
            dt_abertura = str(input("Insira a data de abertura da ordem de servico: "))
            dt_prevista = str(input("Insira a data prevista da ordem de servico: "))
            dt_efetiva = str(input("insira a data efetiva da ordem de servico: "))
            oracle.write(f"insert into ordensservicos values ('{codigo_cliente}', '{codigo_ordem}', '{dt_abertura}', '{dt_prevista}', '{dt_efetiva}')")
            df_ordem_servico = oracle.sqlToDataFrame(f"select codcliente, cod_ordemservico, dt_abertura, dt_prev_atendimento, dt_efet_atendimento from ordensservicos where codcliente = '{codigo_cliente}' and cod_ordemservico = '{codigo_ordem}'")
            novo_ordem_servico = OrdemServico(df_ordem_servico.codcliente.values[0],
                                              df_ordem_servico.cod_ordemservico.values[0],
                                              df_ordem_servico.dt_abertura.values[0],
                                              df_ordem_servico.dt_prev_atendimento.values[0],
                                              df_ordem_servico.dt_efet_atendimento.values[0])
            print(novo_ordem_servico)
            return novo_ordem_servico
        else:
            print("Nao e possivel fazer a insercao com os dados fornecidos")
            return None

    def atualizar_ordem_servico(self) -> OrdemServico:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente: "))
        codigo_ordem = str(input("Insira o codigo de ordem de servico: "))

        if not self.verifica_existencia_ordem_servico(oracle, codigo_cliente, codigo_ordem):
            novo_codigo_ordem = str(input("Insira o codigo de ordem atualizado: "))
            if self.verifica_existencia_ordem_servico(oracle, codigo_cliente, novo_codigo_ordem):
                novo_dt_abertura = str(input("Insira a data de abertura da ordem de servico atualizada: "))
                novo_dt_prevista = str(input("Insira a data prevista da ordem de servico atualizada: "))
                novo_dt_efetiva = str(input("insira a data efetiva da ordem de servico atualizada: "))
                oracle.write(f"update servicos set cod_ordemservico = '{novo_codigo_ordem}' where cod_ordemservico = '{codigo_ordem}'")
                oracle.write(f"update ordensservicos set cod_ordemservico = '{novo_codigo_ordem}', dt_abertura = '{novo_dt_abertura}', dt_prev_atendimento = '{novo_dt_prevista}', dt_efet_atendimento = '{novo_dt_efetiva}' where codcliente = '{codigo_cliente}' and cod_ordemservico = '{codigo_ordem}'")
                df_ordem_servico = oracle.sqlToDataFrame(f"select codcliente, cod_ordemservico, dt_abertura, dt_prev_atendimento, dt_efet_atendimento from ordensservicos where codcliente = '{codigo_cliente}' and cod_ordemservico = '{novo_codigo_ordem}'")
                ordem_servico_atualizado = OrdemServico(df_ordem_servico.codcliente.values[0],
                                                        df_ordem_servico.cod_ordemservico.values[0],
                                                        df_ordem_servico.dt_abertura.values[0],
                                                        df_ordem_servico.dt_prev_atendimento.values[0],
                                                        df_ordem_servico.dt_efet_atendimento.values[0])
                print(ordem_servico_atualizado)
                return ordem_servico_atualizado
            else:
                print("Nao e possivel fazer a atualizacao com os dados fornecidos")
                return None
        else:
            print("Nao e possivel fazer a atualizacao com os dados fornecidos")
            return None

    def excluir_ordem_servico(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        codigo_cliente = int(input("Insira o codigo do cliente da ordem de servico a ser excluida: "))
        codigo_ordem = str(input("Insira o codigo da ordem de servico a ser excluida: "))

        if not self.verifica_existencia_ordem_servico(oracle, codigo_cliente, codigo_ordem):
            df_ordem_servico = oracle.sqlToDataFrame(f"select codcliente, cod_ordemservico, dt_abertura, dt_prev_atendimento, dt_efet_atendimento from ordensservicos where codcliente = '{codigo_cliente}' and cod_ordemservico = '{codigo_ordem}'")
            oracle.write(f"delete from servicos where codcliente = '{codigo_cliente}' and cod_ordemservico = '{codigo_ordem}'")
            oracle.write(f"delete from ordensservicos where codcliente = '{codigo_cliente}' and cod_ordemservico = '{codigo_ordem}'")
            ordem_servico_excluido = OrdemServico(df_ordem_servico.codcliente.values[0],
                                                  df_ordem_servico.cod_ordemservico.values[0],
                                                  df_ordem_servico.dt_abertura.values[0],
                                                  df_ordem_servico.dt_prev_atendimento.values[0],
                                                  df_ordem_servico.dt_efet_atendimento.values[0])
            print("Ordem de servico excluida com sucesso")
            print(ordem_servico_excluido)
        else:
            print("Nao e possivel fazer a exclusao com os dados fornecidos")

    def verifica_existencia_ordem_servico(self, oracle: OracleQueries, codigo_cliente: int, codigo_ordem: str):
        df_ordem_servico = oracle.sqlToDataFrame(f"select codcliente, cod_ordemservico, dt_abertura, dt_prev_atendimento, dt_efet_atendimento from ordensservicos where codcliente = '{codigo_cliente}' and cod_ordemservico = '{codigo_ordem}'")
        return df_ordem_servico.empty
