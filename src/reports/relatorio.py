from conexion.oracle_queries import OracleQueries

class Relatorio:

    def __init__(self):

        with open("//home/labdatabase/Downloads/TrabalhoDow/src/sql_consulta/relatorio_cliente_endereco_telefone.sql") as f:
            self.query_relatorio_cliente_endereco_telefone = f.read()

        with open("//home/labdatabase/Downloads/TrabalhoDow/src/sql_consulta/relatorio_cliente.sql") as f:
            self.query_relatorio_cliente = f.read()

        with open("//home/labdatabase/Downloads/TrabalhoDow/src/sql_consulta/relatorio_codcliente_x_ordemdeservico.sql") as f:
            self.query_relatorio_codcliente_x_ordemdeservico = f.read()

        with open("//home/labdatabase/Downloads/TrabalhoDow/src/sql_consulta/relatorio_servico_x_codcliente.sql") as f:
            self.query_relatorio_servico_x_codcliente = f.read()

        with open("//home/labdatabase/Downloads/TrabalhoDow/src/sql_consulta/relatorio_servicos_realizados.sql") as f:
            self.query_relatorio_servicos_realizados = f.read()

    
    def get_relatorio_endereco(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(f"select * from enderecos"))
        input("Pressione Enter para sair do relatorio")

    def get_relatorio_ordem_servico(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(f"select * from ordensservicos"))
        input("Pressione Enter para sair do relatorio")

    def get_relatorio_servico(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(f"select * from servicos"))
        input("Pressione Enter para sair do relatorio")

    def get_relatorio_telefone(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(f"select * from telefones"))
        input("Pressione Enter para sair do relatorio")

    
    def get_relatorio_cliente_endereco_telefone(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_cliente_endereco_telefone))
        input("Pressione Enter para sair do relatorio")

    def get_relatorio_cliente(self):
        oracle = OracleQueries()
        oracle.connect()
        print(self.query_relatorio_cliente)
        print(oracle.sqlToDataFrame(self.query_relatorio_cliente))
        input("Pressione Enter para sair do relatorio")

    def get_relatorio_codcliente_ordemdeservico(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_codcliente_x_ordemdeservico))
        input("Pressione Enter para sair do relatorio")

    def get_relatorio_servico_codcliente(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_servico_x_codcliente))
        input("Pressione Enter para sair do relatorio")

    def get_relatorio_servicos_realizados(self):
        oracle = OracleQueries()
        oracle.connect()

        print(oracle.sqlToDataFrame(self.query_relatorio_servicos_realizados))
        input("Pressione Enter para sair do relatorio")

        
