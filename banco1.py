def depositar(saldo, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito de R${saldo}")
        print(f"Depósito de R${valor} realizado com sucesso.")
    else:
        print("Valor inválido. O valor deve ser maior que zero.")
    return saldo

def sacar(saldo, saque):
    if saque > 0 and saldo >= saque:
        saldo -= saque
        extrato.append(f"Depósito de R${saldo}")
        print(f"Saque de R${saque} realizado com sucesso.")
    else:
        print("Valor inválido.")
    return saldo
def mostrarExtrato (extrato, saldo):
    print(f"\nExtrato Detalhado:")
    for operacao in extrato:
        print(operacao)
        print(f"\nSeu saldo atual é R${saldo}")

saldo = 0
extrato = []
sair = False
while sair != True:
    contaBancaria = int(input("Escolha a operação que deseja fazer? \n 1 - Depositar;\n 2 - Sacar; \n 3 - Extrato; \n 0 - Sair; \n"))
    if contaBancaria == 1:
        valor = float(input('Quanto você quer depositar: '))
        saldo = depositar(saldo, valor)
    elif contaBancaria == 2:
        saque = float(input('Quanto você quer sacar: '))
        saldo = sacar(saldo, saque)
    elif contaBancaria == 3:
        mostrarExtrato(extrato, saldo)
    elif contaBancaria == 0:
        sair = True