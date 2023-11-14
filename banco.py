contaBancaria = int(input("Escolha a operação que deseja fazer? \n 1 - Depositar;\n 2 - Sacar; \n 3 - Extrato; \n 0 - Sair; \n"))

# Saldo inicial
saldo = 0
extrato = []

while contaBancaria != 0:
    if contaBancaria == 1:
        valor = float(input("Quanto deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito de R${valor}")
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("Valor inválido. O valor deve ser maior que zero.")

    elif contaBancaria == 2:
        valor = float(input("Quanto deseja sacar: "))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            extrato.append(f"Saque de R${valor}")
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Valor inválido ou saldo insuficiente.")

    elif contaBancaria == 3:
        print(f"\nExtrato Detalhado:")
        for operacao in extrato:
            print(operacao)
        print(f"\nSeu saldo atual é R${saldo}")

    # Solicita uma nova operação
    contaBancaria = int(input("\nEscolha a operação que deseja fazer? \n 1 - Depositar;\n 2 - Sacar; \n 3 - Extrato; \n 0 - Sair; \n"))

print("\nExtrato Final:")
for operacao in extrato:
    print(operacao)
print(f"\nSaldo final é R${saldo}")
print("Obrigado por utilizar nosso sistema. Até mais!")