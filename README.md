# Sistema Bancário V1

### Projeto Python - DIO

Este é um projeto básico de sistema bancário desenvolvido em Python para o bootcamp da DIO (Digital Innovation One). Ele implementa operações simples como **depósito**, **saque** e **consulta de extrato**. Esta é a versão 1 do sistema, que trabalha apenas com um usuário, sem a necessidade de gerenciar múltiplas contas.

## Funcionalidades

1. **Depósito**
   - Permite ao usuário realizar depósitos de valores positivos.
   - Todos os depósitos são armazenados e exibidos no extrato.

2. **Saque**
   - Permite realizar até 3 saques diários, com limite máximo de R$ 500,00 por saque.
   - Verifica se há saldo suficiente antes de permitir o saque.
   - Todos os saques são registrados e exibidos no extrato.

3. **Extrato**
   - Exibe todas as movimentações (depósitos e saques) realizadas pelo usuário.
   - Exibe o saldo atual da conta.
   - Se não houver movimentações, uma mensagem é exibida informando que não foram realizadas operações.

## Requisitos

- Python 3.6 ou superior.

## Como usar

1. Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com/ebertlc/SysBank_trilha-python-dio
   ```

2. Execute o arquivo `main.py` para iniciar o sistema:
   ```bash
   python main.py
   ```

3. Siga as instruções no terminal para realizar operações de depósito, saque ou extrato.

## Operações disponíveis

- **[d] Depositar**: Permite ao usuário realizar um depósito.
- **[s] Sacar**: Permite realizar um saque, respeitando o limite diário e o saldo disponível.
- **[e] Extrato**: Exibe todas as movimentações e o saldo atual.
- **[q] Sair**: Encerra o programa.

## Exemplo de Execução

```bash
______________________________________________________
______________________________________________________
Bem Vindo(a) ao SysBank
______________________________________________________
Escolha uma opção para começar
[d]______________________Depositar
[s]______________________Sacar
[e]______________________Extrato
[q]______________________Sair
[ ]====>
```

---