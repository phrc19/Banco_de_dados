MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS = """Relatórios
1 - Relatorio de Servicos
2 - Relatorio de Clientes
3 - Relatorio de Ordem de servico
4 - Relatorio de Telefone
5 - Relatorio de Endereco
6 - Relatório de Clientes Completo
0 - Sair
"""

MENU_ENTIDADES = """Entidades
1 - SERVICOS
2 - CLIENTES
3 - ORDENSSERVICOS
4 - TELEFONE
5 - ENDERECOS
"""

# Consulta de contagem de registros por tabela
QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=3):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")
