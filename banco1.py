import textwrap

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito de R${saldo}")
        print(f"Depósito de R${valor} realizado com sucesso.")
    else:
        print("Valor inválido. O valor deve ser maior que zero.")
    return saldo, extrato

def sacar(saldo, saque, extrato):
    if saque > 0 and saldo >= saque and saque <= 1000:
        saldo -= saque
        extrato.append(f"Depósito de R${saldo}")
        print(f"Saque de R${saque} realizado com sucesso.")
    else:
        print("Valor não autorizado.")
    return saldo

def mostrarExtrato (extrato, saldo):
    print(f"\nExtrato Detalhado:")
    for operacao in extrato:
        print(operacao)
        print(f"\nSeu saldo atual é R${saldo}")

def criar_usuario(usuarios):
    cpf = input("informe o CPF (somente números): ")
    usuario = filtrar_Usuario(cpf,usuarios)
    if usuario: 
        print("\n @@@ Já existe usuário com esse CPF! @@@ ")
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado: ")
    
    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário Criado com Sucesso")

def filtrar_Usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuarios in usuarios if usuario["cpf"] = cpf]
    return usuarios_filtrados [0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF (somente números): ")
    usuario = filtrar_Usuario(cpf,usuarios)
    if usuario: 
        print ("\n Conta Criada com Sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("n\ Usuario não encontrado")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        agencia = \t{conta["agencia"]}
        c/c: \t\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

agencia = "0001"
saldo = 0
extrato = []
endereço = {}
usuarios = []
contas = []
sair = False
while sair != True:
    contaBancaria = int(input("Escolha a operação que deseja fazer? \n 1 - Depositar; \n 2 - Sacar; \n 3 - Extrato; \n 4 - Novo Usuário; \n 5 - Listar Contas; \n 6 - Nova Conta; \n 0 - Sair; \n"))
    if contaBancaria == 1:
        valor = float(input('Quanto você quer depositar: '))
        saldo = depositar(saldo, valor, extrato)
    
    elif contaBancaria == 2:
        saque = float(input('Quanto você quer sacar: '))
        saldo = sacar(saldo, saque)
    

    elif contaBancaria == 3:
        print("\n****************EXTRATO**************")
        print("Não foram realizadas mais movimentações")
        mostrarExtrato(extrato, saldo)
        print("***************************************")
    
    elif contaBancaria == 4:
        criar_usuario(usuarios)
    
    elif contaBancaria == 5:
        listar_contas(contas)

    elif contaBancaria == 6:
        numero_conta = len(contas) + 1
        conta = criar_conta(agencia, numero_conta, usuarios)
        if conta: 
            conta.append(conta)
    elif contaBancaria == 0:
        sair = True