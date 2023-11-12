# primeira versão de um sistema bancário. possibilita ações como depósito, saque e extrato
# deposito: somente valores positivos
# saques: o valor deve ser igual ou menor que o saldo em conta. maximo 3 saques por dia, limite maximo de 
# 500 reais por saque
# extrato: listar todos os saques e depositos na ordem da ação, no final, exibir saldo atual da conta

from datetime import date,datetime
depositos_saques = []
data_hora = []
valores = []

saldo = 0
contador_saque_diario = 0


def primeiro_comando(comando=0):
    """
    função que define o comando a ser executado

    retorno:
    numero que define qual será a ação do gerenciador 
    """

    print('Bem-vindo ao menu. Escolha a opção desejada digitando o numero correspondente:')
    print('1- Realizar depósito')
    print('2- Realizar saque')
    print('3- Imprimir extrato')

    #variavel "comando" abriga a tarefa a ser executada
    comando = input('')                                                                    
    print('')

    try:
        comando = int(comando)
    except Exception:
        print('opção inválida, tente novamente.')
        return primeiro_comando
    
    if not (1 <= comando <= 3):
        print('opção inválida, tente novamente.')
        return primeiro_comando
                                         
    return comando



def escolha_valor(x=0):
    """
    função que permite o usuario escolher o valor a ser depositado/sacado
    retorna o valor (inteiro)
    existe uma função (def valor_unico) para a opção 5
    """

    print('Escolha o valor digitando o numero correspondente: ')
    print('1- 10')
    print('2- 20')
    print('3- 50')
    print('4- 100')
    print('5- Outro')

    valor = input('')                                                                    
    print('')

    try:
        valor = int(valor)
    except Exception:
        print('opção inválida, tente novamente.')
        print('')
        return escolha_valor()
    
    if not (1 <= valor <= 5):
        print('opção inválida, tente novamente.')
        print('')
        return escolha_valor()
    
    if valor == 1:
        valor = 10
        return valor
    
    elif valor == 2:
        valor = 20
        return valor
    
    elif valor == 3:
        valor = 50
        return valor
    
    elif valor == 4:
        valor = 100
        return valor
    
    else:
        valor = valor_unico()
        return valor



def valor_unico(x=0):
    """ 
    auxilia a função (escolha_valor), retorna um valor especificado pelo usuario 
    """

    valor_outro = input('digite o valor desejado, sem pontos ou virgulas:')

    try:
        valor_outro = int(valor_outro)
    except Exception:
        print('opção inválida, tente novamente.')
        print('')
        return valor_unico
       
    if (valor_outro <= 0):
        print('opção inválida, tente novamente.')
        print('')
        return valor_unico
    
    return valor_outro
    

def deposito(x=0):
    """ realiza o deposito na conta. armazena o tipo(deposito), data e hora da transação nas respectivas listas """
    a = escolha_valor()
    dia_e_hora = datetime.now()

    depositos_saques.append('Depósito')
    data_hora.append(dia_e_hora)
    valores.append(a)
    
    return a 
    
    
def saque(x=0):
    """ 
     realiza o saque. armazena o tipo(saque), data e hora da transação nas respectivas listas.
     verifica a contagem de saques, o saldo em conta e se o valor é igual ou menor que 500.
     """
    a = escolha_valor()
    dia_e_hora = datetime.now()

    if a > saldo:
        print('Valor inválido, escolha um valor igual ou menor que o saldo atual.')
        print('')
        return primeiro_comando()
    
    elif a > 500:
        print('Limite maximo de saldo é de R$500.00, tente novamente.')
        print('')
        return primeiro_comando()
    
    elif contador_saque_diario == 3:
        print('Limite maximo de saques atingido, tente novamente amanhã.')
        print('')
    
    depositos_saques.append('Saque')
    data_hora.append(dia_e_hora)
    valores.append(a)
    
    return a


def extrato(x=0):
    """
    acessa as listas depositos_saques e data_hora, retorna a impressão dos dados das ultimas transações
    """
    if len(depositos_saques)==0:
        print('Ainda não há movimentações na conta.')
        print('')
        return
    
    print('Segue o extrato das ultimas movimentações: ')
    print('')

    for i in range(len(valores)):
        print(data_hora[i],' ','R$',valores[i],'',depositos_saques[i])

    print('')
    return





# loop que garante que o processo funcione initerruptamente
while True:
    passo = primeiro_comando()

    if passo == 1:
        valor_deposito = deposito()
        saldo = saldo + valor_deposito
        print('Depósito realizado com sucesso')
        print('')
        

    elif passo == 2:
        valor_saque = saque()
        saldo = saldo - valor_saque
        print('Saque realizado com sucesso')
        print('')
        contador_saque_diario += 1

    else:
        extrato()
        print('Saldo atual: R$',saldo)
        print('')


