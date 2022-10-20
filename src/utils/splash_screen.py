from conexion.oracle_queries import OracleQueries
from . import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_servicos = config.QUERY_COUNT.format(tabela="servicos")
        self.qry_total_clientes = config.QUERY_COUNT.format(tabela="clientes")
        self.qry_total_ordensservicos = config.QUERY_COUNT.format(tabela="ordensservicos")
        self.qry_total_enderecos = config.QUERY_COUNT.format(tabela="enderecos")
        self.qry_total_telefones = config.QUERY_COUNT.format(tabela="telefones")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Alexander Silva, Esdras dos Reis, Johannes Peter, Joaquim Lucas, Paulo Hugo Rothechedl Cavalieri, Pedro Henrique Xibili"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    def get_total_servicos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_servicos)["total_servicos"].values[0]

    def get_total_clientes(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_clientes)["total_clientes"].values[0]

    def get_total_ordensservicos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_ordensservicos)["total_ordensservicos"].values[0]

    def get_total_enderecos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_enderecos)["total_enderecos"].values[0]
    
    def get_total_telefones(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Retorna o total de registros computado pela query
        return oracle.sqlToDataFrame(self.qry_total_telefones)["total_telefones"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #            SISTEMA DE TELEFONIA/INTERNET                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - SERVICOS:         {str(self.get_total_servicos()).rjust(5)}
        #      2 - CLIENTES:         {str(self.get_total_clientes()).rjust(5)}
        #      3 - ORDEM DE SERVICO: {str(self.get_total_ordensservicos()).rjust(5)}
        #      4 - ENDERECOS:         {str(self.get_total_enderecos()).rjust(5)}
        #      5 - TELEFONES:         {str(self.get_total_telefones()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """
