import utils.config as config
from utils.splash_screen import SplashScreen
from reports.relatorio import Relatorio
from controller.controller_servico import ControllerServico
from controller.controller_cliente import ControllerCliente
from controller.controller_ordem_servico import ControllerOrdemServico
from controller.controller_endereco import ControllerEndereco
from controller.controller_telefone import ControllerTelefone

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_servico = ControllerServico()
ctrl_cliente = ControllerCliente()
ctrl_ordem_servico = ControllerOrdemServico()
ctrl_telefone = ControllerTelefone()
ctrl_endereco = ControllerEndereco()

def reports(opcao_relatorio: int = 0):
    if opcao_relatorio == 1:
        relatorio.get_relatorio_servico()
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_cliente()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_ordem_servico()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_telefone()
    elif opcao_relatorio == 5:
        relatorio.get_relatorio_endereco()
    elif opcao_relatorio == 6:
        relatorio.get_relatorio_cliente_endereco_telefone()
    else:
        return

def inserir(opcao_inserir: int = 0):
    if opcao_inserir == 1:
        relatorio.get_relatorio_ordem_servico()
        relatorio.get_relatorio_cliente()
        novo_servico = ctrl_servico.inserir_servico()
    elif opcao_inserir == 2:
        relatorio.get_relatorio_cliente()
        novo_cliente = ctrl_cliente.inserir_cliente()
    elif opcao_inserir == 3:
        relatorio.get_relatorio_cliente()
        relatorio.get_relatorio_ordem_servico()
        relatorio.get_relatorio_servico()
        novo_ordem_servico = ctrl_ordem_servico.inserir_ordem_servico()
    elif opcao_inserir == 4:
        relatorio.get_relatorio_cliente()
        novo_telefone = ctrl_telefone.inserir_telefone()
    elif opcao_inserir == 5:
        relatorio.get_relatorio_cliente()
        novo_endereco = ctrl_endereco.inserir_endereco()


def atualizar(opcao_atualizar: int = 0):
    if opcao_atualizar == 1:
        relatorio.get_relatorio_servico()
        servico_atualizado = ctrl_servico.atualizar_servico()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_cliente()
        cliente_atualizado = ctrl_cliente.atualizar_cliente()
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_ordem_servico()
        ordem_servico_atualizado = ctrl_ordem_servico.atualizar_ordem_servico()
    elif opcao_atualizar == 4:
        relatorio.get_relatorio_telefone()
        telefone_atualizado = ctrl_telefone.atualizar_telefone()
    elif opcao_atualizar == 5:
        relatorio.get_relatorio_endereco()
        endereco_atualizado = ctrl_endereco.atualizar_endereco()


def excluir(opcao_excluir: int = 0):
    if opcao_excluir == 1:
        relatorio.get_relatorio_servico()
        ctrl_servico.excluir_servico()
    elif opcao_excluir == 2:
        relatorio.get_relatorio_cliente()
        ctrl_cliente.excluir_cliente()
    elif opcao_excluir == 3:
        relatorio.get_relatorio_ordem_servico()
        ctrl_ordem_servico.excluir_ordem_servico()
    elif opcao_excluir == 4:
        relatorio.get_relatorio_telefone()
        ctrl_telefone.excluir_telefone()
    elif opcao_excluir == 5:
        relatorio.get_relatorio_endereco()
        ctrl_endereco.excluir_endereco()


def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)

        if opcao == 1:  # Relatórios

            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [1-9]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2:  # Inserir Novos Registros

            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3:  # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)


if __name__ == "__main__":
    run()