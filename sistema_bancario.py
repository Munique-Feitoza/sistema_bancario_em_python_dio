import textwrap
from datetime import datetime

# Constantes
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500

# Dados em memória
usuarios = []
contas = []

# Funções do sistema

def menu():
    menu_text = """
    ======== MENU ========
    [1] Criar usuário
    [2] Criar conta
    [3] Depositar
    [4] Sacar
    [5] Extrato
    [6] Listar contas
    [0] Sair
    ======================
    => """
    return input(textwrap.dedent(menu_text))

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf):
        print("Usuário já cadastrado.")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "data_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    })
    print("✅ Usuário criado com sucesso!")

def filtrar_usuario(cpf):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_conta():
    cpf = input("Informe o CPF do titular: ")
    usuario = filtrar_usuario(cpf)

    if not usuario:
        print("Usuário não encontrado. Cadastre-o primeiro.")
        return

    numero_conta = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": [],
        "saques": 0
    }
    contas.append(conta)
    print(f"✅ Conta criada com sucesso! Agência: 0001 Conta: {numero_conta:04d}")

def selecionar_conta():
    cpf = input("Informe o CPF do titular da conta: ")
    conta = next((c for c in contas if c["usuario"]["cpf"] == cpf), None)
    if not conta:
        print("Conta não encontrada.")
    return conta

def depositar(conta):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            conta["saldo"] += valor
            data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            conta["extrato"].append(f"{data} - Depósito: R$ {valor:.2f}")
            print("✅ Depósito realizado com sucesso.")
        else:
            print("⚠️ Valor inválido.")
    except ValueError:
        print("⚠️ Entrada inválida. Tente novamente.")

def sacar(conta):
    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        print("⚠️ Entrada inválida.")
        return

    if valor <= 0:
        print("⚠️ Valor inválido.")
    elif valor > conta["saldo"]:
        print("❌ Saldo insuficiente.")
    elif valor > LIMITE_VALOR_SAQUE:
        print("❌ Valor excede o limite de R$ 500.")
    elif conta["saques"] >= LIMITE_SAQUES:
        print("❌ Número de saques diários excedido.")
    else:
        conta["saldo"] -= valor
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        conta["extrato"].append(f"{data} - Saque: R$ {valor:.2f}")
        conta["saques"] += 1
        print("✅ Saque realizado com sucesso.")

def exibir_extrato(conta):
    print("\n========== EXTRATO ===========")
    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        for item in conta["extrato"]:
            print(item)
    print(f"Saldo: R$ {conta['saldo']:.2f}")
    print("================================")

def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print(f"\nAgência: {conta['agencia']}")
        print(f"Número da conta: {conta['numero']:04d}")
        print(f"Titular: {conta['usuario']['nome']}")
        print(f"Cadastro: {conta['usuario'].get('data_cadastro', 'Data não disponível')}")

# Loop principal
def main():
    while True:
        opcao = menu()

        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            criar_conta()
        elif opcao == "3":
            conta = selecionar_conta()
            if conta:
                depositar(conta)
        elif opcao == "4":
            conta = selecionar_conta()
            if conta:
                sacar(conta)
        elif opcao == "5":
            conta = selecionar_conta()
            if conta:
                exibir_extrato(conta)
        elif opcao == "6":
            listar_contas()
        elif opcao == "0":
            print("Saindo do sistema.")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
