from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Conta:
    def __init__(self, cliente, numero):
        self.agencia = "0001"
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0
        self.transacoes = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor <= 0:
            print("⚠️ Valor inválido para depósito.")
            return False

        self.saldo += valor
        transacao = Deposito(valor)
        self.transacoes.append(transacao)
        print("✅ Depósito realizado com sucesso.")
        return True

    def sacar(self, valor):
        if valor <= 0:
            print("⚠️ Valor inválido para saque.")
            return False

        if valor > self.saldo:
            print("❌ Saldo insuficiente.")
            return False

        if valor > 500:
            print("❌ O valor máximo por saque é R$ 500.00.")
            return False

        if self.saques_diarios >= 3:
            print("❌ Limite diário de saques atingido.")
            return False

        self.saldo -= valor
        self.saques_diarios += 1
        transacao = Saque(valor)
        self.transacoes.append(transacao)
        print("✅ Saque realizado com sucesso.")
        return True

    def exibir_extrato(self):
        print("\n========== EXTRATO ==========")
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for t in self.transacoes:
                print(f"{t.data.strftime('%d/%m/%Y %H:%M:%S')} - {t}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("=============================")


class Transacao(ABC):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    @abstractmethod
    def __str__(self):
        pass


class Deposito(Transacao):
    def __str__(self):
        return f"Depósito: R$ {self.valor:.2f}"


class Saque(Transacao):
    def __str__(self):
        return f"Saque: R$ {self.valor:.2f}"


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def buscar_cliente_por_cpf(self, cpf):
        return next((c for c in self.clientes if c.cpf == cpf), None)

    def criar_cliente(self, nome, cpf, nascimento, endereco):
        if self.buscar_cliente_por_cpf(cpf):
            print("⚠️ CPF já cadastrado.")
            return None
        cliente = Cliente(nome, cpf, nascimento, endereco)
        self.clientes.append(cliente)
        print("✅ Cliente cadastrado com sucesso.")
        return cliente

    def criar_conta(self, cpf):
        cliente = self.buscar_cliente_por_cpf(cpf)
        if not cliente:
            print("❌ Cliente não encontrado.")
            return None
        numero = len(self.contas) + 1
        conta = Conta(cliente, numero)
        cliente.adicionar_conta(conta)
        self.contas.append(conta)
        print(f"✅ Conta criada com sucesso: Agência {conta.agencia} Conta {conta.numero:04d}")
        return conta

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada.")
            return
        for conta in self.contas:
            print(f"\nAgência: {conta.agencia}")
            print(f"Número: {conta.numero:04d}")
            print(f"Titular: {conta.cliente.nome}")
