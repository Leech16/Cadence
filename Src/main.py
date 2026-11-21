#===============================
# INTERFACE USUÁRIO 
#===============================

def exibir_menu():
    print("="*30)
    print("          CADENCE           ")
    print("="*30)
    print(
        " [1] Registrar sessão de estudo \n "
        "[2] Consultar histórico \n "
        "[3] Listar disciplinas \n "
        "[4] Consultar estatísticas \n "
        "[5] Sair"
        )

def ler_opcao():
    entrada = input("Escolha uma opção:").strip()
    if not entrada.isdigit():
        print("Entrada inválida! Digite um número de 1 a 5!")
        return None
    return int(entrada)

def executar_opcao(opcao: int):
    if opcao == 1:
        print("opção 1 selecionada - registro será implementado futuramente.") 
    elif opcao == 2:
        print("opção 2 selecionada - Consultar histórico será implementado futuramente.")
    elif opcao == 3:
        print("opção 3 selecionada - Listar disciplinas será implementado futuramente.")
    elif opcao == 4:
        print("opção 4 selecionada - Consultar estatísticas será implementado futuramente.")
    elif opcao == 5:
        print("Encerrando o programa!")
    else:
        print("Opção Inexistente! Escolha um número entre 1 e 5.")

def main():
    opcao = 0
    while opcao != 5:
        exibir_menu()
        opcao_lida = ler_opcao()

        if opcao_lida is None:
            continue

        opcao = opcao_lida
        executar_opcao(opcao)

if __name__=="__main__":
    main()