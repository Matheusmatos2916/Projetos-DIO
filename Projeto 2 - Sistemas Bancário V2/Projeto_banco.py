class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    numero_conta = 1

    def __init__(self, usuario):
        self.agencia = "0001"
        self.numero = Conta.numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.contador_deposito = 0
        self.contador_saque = 0
        self.historico_deposito = []
        self.historico_saques = []
        Conta.numero_conta += 1

usuarios = []
contas = []

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = input("Digite o endereço do usuário (logradouro, nro - bairro - cidade/estado): ")

    # Verificar se o CPF já existe na lista de usuários
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Erro: CPF já cadastrado.")
            return None

    # Criar um novo usuário e adicioná-lo à lista de usuários
    novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso.")

def listar_usuarios():
    print("\n---- Usuários Cadastrados ----")
    for usuario in usuarios:
        print(f"Nome: {usuario.nome}\tCPF: {usuario.cpf}")

def deposito(valor, saldo, conta):
    if valor > 0:
        saldo += valor
        print("Saldo atual:", saldo)
        conta.historico_deposito.append(valor)
        return saldo
    else:
        print("Valor inválido")
        return saldo

def saque(valor, saldo, contador_saldo, conta):
    if contador_saldo < 3:
        if valor > 0 and valor <= 500:
            if saldo >= valor:
                saldo -= valor
                print("Saldo atual: R$ ", saldo)
                conta.historico_saques.append(valor)
                return saldo
            else:
                print("Erro: Saldo Insuficiente")
        else:
            print("Valor inválido ou saque máximo alcançado R$ 500.00)")
    else:
        print("Erro: Limite de saques alcançado")
    return saldo

while True:
    print("\n---- Selecione a Opção ----")
    print("1-)Cadastrar Usuário\n2-)Depósito\n3-)Saque\n4-)Extrato\n5-)Listar Usuários\n6-)Sair\n")
    opcao = int(input("Insira a opção desejada: "))

    if opcao == 1:
        cadastrar_usuario()

    elif opcao == 2:
        cpf = input("Digite o CPF do usuário: ")
        usuario_encontrado = False
        for usuario in usuarios:
            if usuario.cpf == cpf:
                valor_deposito = float(input("Insira o valor do depósito (R$): "))
                for conta in contas:
                    if conta.usuario == usuario:
                        conta.saldo = deposito(valor_deposito, conta.saldo, conta)
                        conta.contador_deposito += 1
                        usuario_encontrado = True
                if not usuario_encontrado:
                    nova_conta = Conta(usuario)
                    nova_conta.saldo = deposito(valor_deposito, nova_conta.saldo, nova_conta)
                    nova_conta.contador_deposito += 1
                    contas.append(nova_conta)
                    usuario_encontrado = True
                break
        if not usuario_encontrado:
            print("Usuário não encontrado.")

    elif opcao == 3:
        cpf = input("Digite o CPF do usuário: ")
        usuario_encontrado = False
        for usuario in usuarios:
            if usuario.cpf == cpf:
                for conta in contas:
                    if conta.usuario == usuario:
                        valor_saque = float(input("Insira o valor do saque (R$): "))
                        conta.saldo = saque(valor_saque, conta.saldo, conta.contador_saque, conta)
                        conta.contador_saque += 1
                        usuario_encontrado = True
                        break
                break
        if not usuario_encontrado:
            print("Usuário não encontrado.")

    elif opcao == 4:
        cpf = input("Digite o CPF do usuário: ")
        usuario_encontrado = False
        for usuario in usuarios:
            if usuario.cpf == cpf:
                for conta in contas:
                    if conta.usuario == usuario:
                        print("\n---- Extrato ----\n")
                        print("Ordem\tOperação\tValor")
                        for i, valor in enumerate(conta.historico_deposito, 1):
                            print(f"{i}\tDepósito\t R$ {valor:.2f}")
                        for i, valor in enumerate(conta.historico_saques, 1):
                            print(f"{i}\tSaque\t R$ {valor:.2f}")
                        print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
                        usuario_encontrado = True
                if not usuario_encontrado:
                    print("Usuário não possui conta.")
                break
        if not usuario_encontrado:
            print("Usuário não encontrado.")

    elif opcao == 5:
        listar_usuarios()

    elif opcao == 6:
        print("Obrigado por utilizar o nosso sistema")
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida.")
