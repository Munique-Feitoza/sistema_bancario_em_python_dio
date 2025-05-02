# 💰 Sistema Bancário em Python (Refatorado com Datas)

Este é um projeto desenvolvido durante o bootcamp da [DIO.me](https://www.dio.me/), baseado no desafio de construir um sistema bancário em Python. Nesta versão refatorada, o sistema utiliza **funções** e inclui **registro de datas** para todas as transações e cadastros de usuários, tornando o controle mais realista e organizado.

## ✅ Funcionalidades

- 📌 Criar usuários com CPF, nome, data de nascimento e endereço (com data de cadastro).
- 🏦 Criar contas bancárias associadas a usuários.
- 💵 Realizar **depósitos** (com registro de data e hora).
- 💸 Realizar **saques**, respeitando:
  - Limite de R$500 por saque
  - Máximo de 3 saques por dia
  - Saldo da conta
- 📄 Consultar extrato da conta, com data e hora das movimentações.
- 📚 Listar todas as contas cadastradas.

## 📁 Estrutura

O código está organizado em funções para facilitar manutenção e reutilização:

- `criar_usuario()`
- `criar_conta()`
- `depositar(conta)`
- `sacar(conta)`
- `exibir_extrato(conta)`
- `listar_contas()`

Além disso, utiliza `datetime.now()` para registrar as datas relevantes de ações no sistema.

## 📦 Como Executar

1. Certifique-se de ter Python instalado (versão 3.x).
2. . Clone este repositório ou copie o código:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario-python.git
   ```
3. Execute com Python 3:
   ```bash
   python sistema_bancario.py
   ```

## 📚 Tecnologias utilizadas

- Python 3
- Programação Procedural
- Listas e Dicionários
- Entrada e saída de dados com `input()` e `print()`

## 🧠 Aprendizados

- Estruturação de código limpo e modular
- Validação de regras de negócio
- Manipulação de dados em memória
- Interação com o usuário via terminal

## 🏁 Próximos passos

- Suporte a autenticação por senha
- Persistência de dados em arquivo ou banco de dados
- Interface gráfica com Tkinter ou interface web com Flask

---

Feito com 💻 para o bootcamp da [DIO.me](https://www.dio.me/)