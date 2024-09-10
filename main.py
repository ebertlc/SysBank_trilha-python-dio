###3 projeto python D.I.O. Sistema bancário V1 operações básicas como Deposito, saque e extrato###

import time
import sys

#função pra verificar se o numero é positivo
def numero_valido(numero):
    if numero > 0:
        return True
    else:
        return False

#função para deposito

#Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1
#usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os
#depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

def deposito(valor, saldo):
    saldo += valor
    print('\n' + f'Depósito de R$ {valor:.2f} realizado com sucesso!'.center(80, "_"))
    return saldo

def depositar(saldo, movimentacoes):
    while True:
        try:
            valor = float(input('Digite o valor do depósito: '))
            if numero_valido(numero=valor):
                saldo_atualizado = deposito(valor=valor, saldo=saldo)
                movimentacoes.append('Depósito: R$' + f'{valor:.2f}'.rjust(68, "_"))
                return saldo_atualizado
            else:
                print('\n' + 'O valor para depósito deve ser maior que zero'.center(80, "_"))
                continue
        except ValueError:
            print('\n' + 'Digite um valor válido'.center(80, "#"))
            continue

#função para saque

#O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha
#saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
#Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

def saque(valor, saldo):
        saldo_corrigido = saldo - valor
        print('\n' + f'Saque de R$ {valor:.2f} realizado com sucesso!'.center(80, "_"))
        return saldo_corrigido

def sacar(saldo, movimentacoes, limite):
    while True:
        try:
            valor = float(input('Digite o valor do saque: '))

            if numero_valido(numero=valor):
                valor_a_sacar = valor
            else:
                valor_a_sacar = valor * -1

            if valor_a_sacar <= limite:
                if saldo >= valor_a_sacar:
                    saldo_atualizado = saque(valor=valor_a_sacar, saldo=saldo)
                    movimentacoes.append('Saque: R$' + f'{valor_a_sacar:.2f}'.rjust(71, "_"))
                    return saldo_atualizado
                else:
                    print('\n' + 'Saldo insuficiente, operação não realizada'.center(80, "_"))
                    opcao = input('Deseja continuar? [s] Sim [n]Não\n =>')
                    if opcao == 's':
                        continue
                    elif opcao == 'n':
                        break
                    else:
                        print('\n' + 'Digite uma opção válida'.center(80, "_"))
                        break
            else:
                print('\n' + f'O valor máximo permitido para saque é de R$ {limite:.2f}'.center(80, "_"))
                continue
        except ValueError:
            print('Digite um valor válido'.center(80, "#"))
            continue

#função para extrato

#Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo
#atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.

#Os valores devem ser exibidos utilizando o formato R$ xxx.xx
#exemplo:
#1500.45 = R$ 1500.45

def extrato(saldo, movimentacoes):
    print('\n')
    print('Extrato'.center(80, "_"))
    print('\n')
    if len(movimentacoes) == 0:
        print('Não foram realizadas movimentações'.center(80, "_"))
    else:
        for movimentacao in movimentacoes:
            print(movimentacao)
    print('\n\nSaldo atual: R$' + f'{saldo:.2f}'.rjust(65, "_"))

#funçoes para carregamento e cabeçalho

def carregamento():
    for i in range(3):
        print("_".center(80, "_"))
        time.sleep(0.5)

def barra_loading():
    for i in range(101):
        mensagem = f'Carregando {i}%'
        barra = mensagem.center(80, '_')
        sys.stdout.write(f'\r{barra}')
        sys.stdout.flush()
        time.sleep(0.05)

def cabecalho():
    carregamento()
    print('Bem Vindo(a) ao SysBank'.center(80,"_"))
    time.sleep(0.5)
    carregamento()
    print('\n')
    barra_loading()
    print('\n\n')
    print('Escolha uma opção para começar'.center(80, "_"))

#função para menu

def menu():
    opcao = input(
    '\n[d]' + 'Depositar\n'.rjust(78, '_') +
    '[s]' + 'Sacar\n'.rjust(78, '_')+
    '[e]' + 'Extrato\n'.rjust(78, '_') +
    '[q]' + 'Sair\n'.rjust(78, '_') +
    '[ ]====>')
    return opcao

#função main

def main():
    saldo = 0
    limite = 500
    movimentacoes = []
    __saque_diario__ = 3
    saques_realizados = 0

    cabecalho()
    while True:
        opcao = menu()
        if opcao == 'd':
            saldo = depositar(saldo=saldo, movimentacoes=movimentacoes)
            print('\n'+'Selecione uma Operação para Continuar'.center(80, "_"))
        elif opcao == 's':
            if saques_realizados < __saque_diario__:
                saldo = sacar(saldo=saldo, limite=limite, movimentacoes=movimentacoes)
                saques_realizados += 1
            else:
                print('Limite de saques diários atingido'.center(80, "_"))
            print('\n' + 'Selecione uma Operação para Continuar'.center(80, "_"))
        elif opcao == 'e':
            extrato(saldo, movimentacoes)
        elif opcao == 'q':
            break
        else:
            print('Selecione uma opção válida'.center(80, "_"))

if __name__ == '__main__':
    main()
