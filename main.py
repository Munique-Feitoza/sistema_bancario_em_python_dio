from banco import Banco

def menu():
    print("""
=========== MENU ===========
[1] Criar cliente
[2] Criar conta
[3] Depositar
[4] Sacar
[5] Extrato
[6] Listar contas
[0] Sair
============================
""")
    return input("Escolha uma opção: ")


def selecionar_conta(cliente):
    if not cliente.contas:
        print("⚠️ Cliente não possui contas.")
        return None

    print("Contas disponíveis:")
    for i, conta in enumerate(cliente.contas, start=1):
        print(f"[{i}] Conta {conta.numero} - Agência {conta.agencia}")

    try:
        escolha = int(input("Selecione o número da conta: "))
        if 1 <= escolha <= len(cliente.contas):
            return cliente.contas[escolha - 1]
        else:
            print("❌ Opção inválida.")
    except ValueError:
        print("⚠️ Entrada inválida. Digite um número.")
    return None


def main():
    banco = Banco()

    while True:
        opcao = menu()

        if opcao == "1":
            nome = input("Nome completo: ")
            cpf = input("CPF (somente números): ")
            nascimento = input("Data de nascimento (dd-mm-aaaa): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            banco.criar_cliente(nome, cpf, nascimento, endereco)

        elif opcao == "2":
            cpf = input("CPF do cliente: ")
            banco.criar_conta(cpf)

        elif opcao == "3":
            cpf = input("CPF do titular: ")
            cliente = banco.buscar_cliente_por_cpf(cpf)
            if cliente:
                conta = selecionar_conta(cliente)
                if conta:
                    try:
                        valor = float(input("Valor do depósito: "))
                        conta.depositar(valor)
                    except ValueError:
                        print("⚠️ Valor inválido.")
            else:
                print("❌ Cliente não encontrado.")

        elif opcao == "4":
            cpf = input("CPF do titular: ")
            cliente = banco.buscar_cliente_por_cpf(cpf)
            if cliente:
                conta = selecionar_conta(cliente)
                if conta:
                    try:
                        valor = float(input("Valor do saque: "))
                        conta.sacar(valor)
                    except ValueError:
                        print("⚠️ Valor inválido.")
            else:
                print("❌ Cliente não encontrado.")

        elif opcao == "5":
            cpf = input("CPF do titular: ")
            cliente = banco.buscar_cliente_por_cpf(cpf)
            if cliente:
                conta = selecionar_conta(cliente)
                if conta:
                    conta.exibir_extrato()
            else:
                print("❌ Cliente não encontrado.")

        elif opcao == "6":
            banco.listar_contas()

        elif opcao == "0":
            print("✅ Saindo do sistema. Até mais!")
            break

        else:
            print("⚠️ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
