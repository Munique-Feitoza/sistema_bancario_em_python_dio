# Sistema Bancário em Python

Este projeto é um sistema bancário simples desenvolvido em Python, utilizando orientação a objetos. Ele permite o gerenciamento de clientes e contas bancárias com operações de depósito, saque e extrato.

## Funcionalidades

- ✅ Criação de clientes com CPF único.
- ✅ Abertura de contas bancárias associadas a clientes.
- ✅ Depósito de valores com registro em extrato.
- ✅ Saque com verificação de saldo, limite por saque e limite de saques diários.
- ✅ Visualização do extrato da conta.
- ✅ Listagem de contas cadastradas.

## Requisitos

- Python 3.8+

## Como executar

1. Clone o repositório ou baixe os arquivos `banco.py` e `main.py`.
2. Execute no terminal com:

```bash
python main.py
```

## Estrutura de Arquivos

- `banco.py` – Contém as classes `Cliente` e `ContaBancaria` com toda a lógica de negócios.
- `main.py` – Interface interativa em terminal para o usuário interagir com o sistema.
- `README.md` – Este arquivo.

## Melhorias Recentes

- Refatoração completa usando classes (orientação a objetos).
- Separação clara entre lógica de negócio (`banco.py`) e interface (`main.py`).
- Validação de dados e mensagens mais descritivas.