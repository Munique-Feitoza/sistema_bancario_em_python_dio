import textwrap

# Constantes do sistema
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500

# Listas para armazenar os dados dos usuários e contas
usuarios = []
contas = []

# Função para exibir o menu principal
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

# Cria um novo usuário com CPF único
def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        print("Usuário já cadastrado.")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")

# Verifica se um usuário com o CPF já existe
def filtrar_usuario(cpf):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

# Cria uma nova conta para um usuário já cadastrado
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
        "extrato": "",
        "saques": 0
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: 0001 Conta: {numero_conta:04d}")

# Permite localizar uma conta com base no CPF do titular
def selecionar_conta():
    cpf = input("Informe o CPF do titular da conta: ")
    conta = next((c for c in contas if c["usuario"]["cpf"] == cpf), None)
    if not conta:
        print("Conta não encontrada.")
    return conta

# Função de depósito: soma valor ao saldo e registra no extrato
def depositar():
    conta = selecionar_conta()
    if not conta:
        return

    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            conta["saldo"] += valor
            conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

# Função de saque: realiza diversas validações antes de subtrair do saldo
def sacar():
    conta = selecionar_conta()
    if not conta:
        return

    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        print("Entrada inválida.")
        return

    if valor <= 0:
        print("Valor inválido.")
    elif valor > conta["saldo"]:
        print("Saldo insuficiente.")
    elif valor > LIMITE_VALOR_SAQUE:
        print("Valor excede o limite de R$ 500.")
    elif conta["saques"] >= LIMITE_SAQUES:
        print("Número de saques diários excedido.")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["saques"] += 1
        print("Saque realizado com sucesso.")

# Mostra o extrato e o saldo da conta
def exibir_extrato():
    conta = selecionar_conta()
    if not conta:
        return

    print("\n========== EXTRATO ==========")
    print("Sem movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"Saldo: R$ {conta['saldo']:.2f}")
    print("=============================")

# Lista todas as contas cadastradas
def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print(f"\nAgência: {conta['agencia']}")
        print(f"Número da conta: {conta['numero']:04d}")
        print(f"Titular: {conta['usuario']['nome']}")

# Laço principal de execução do sistema bancário
while True:
    opcao = menu()

    if opcao == "1":
        criar_usuario()
    elif opcao == "2":
        criar_conta()
    elif opcao == "3":
        depositar()
    elif opcao == "4":
        sacar()
    elif opcao == "5":
        exibir_extrato()
    elif opcao == "6":
        listar_contas()
    elif opcao == "0":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
