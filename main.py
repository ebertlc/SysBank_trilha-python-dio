#3 projeto python D.I.O. Sistema bancário V1 operações básicas como Deposito, saque e extrato

#função para deposito
"""
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1
usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os
depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
"""
def deposito(valor, saldo):
    saldo += valor
    return saldo

#função para saque
"""
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha 
saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
"""
def saque(valor, saldo):
    if saldo >= valor:
        saldo -= valor
        return saldo
    else:
        print('Saldo insuficiente')
        return saldo

#função para extrato
"""
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo 
atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações. 

Os valores devem ser exibidos utilizando o formato R$ xxx.xx
exemplo: 
1500.45 = R$ 1500.45
"""

def extrato(saldo, depositos, saques):
    print('Extrato')
    if len(depositos) == 0 and len(saques) == 0:
        print('Não foram realizadas movimentações')
    else:
        for deposito in depositos:
            print(f'Depósito: R$ {deposito}')
        for saque in saques:
            print(f'Saque: R$ {saque}')
    print(f'Saldo atual: R$ {saldo}')

#função para menu
def menu():
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Extrato')
    print('4 - Sair')
    opcao = int(input('Escolha uma opção: '))
    return op

#função main
def main():
    saldo = 0
    depositos = []
    saques = []
    while True:
        opcao = menu()
        if opcao == 1:
            valor = float(input('Digite o valor do depósito: '))
            saldo = deposito(valor, saldo)
            depositos.append(valor)
        elif opcao == 2:
            valor = float(input('Digite o valor do saque: '))
            saldo = saque(valor, saldo)
            saques.append(valor)
        elif opcao == 3:
            extrato(saldo, depositos, saques)
        elif opcao == 4:
            break
        else:
            print('Opção inválida')


if __name__ == '__main__':
    main()
