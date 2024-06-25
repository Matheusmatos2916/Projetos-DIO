opcao = 0
saldo = 0
contador_saldo = 0
historico_deposito = []
historico_saques = []

while opcao != 4:
    print("\n---- Selecione a Opção ----\n1-)Depósito\n2-)Saque\n3-)Extrato\n4-)Sair\n")
    opcao = int(input("Insira a opção desejada: "))

    if opcao == 1:
        deposito = float(input("Insira o valor do depósito (R$): "))
        if deposito > 0:
                saldo += deposito
                print("Saldo atual:", saldo)
                historico_deposito.append(deposito)
        else:
            print("Valor inválido")

    elif opcao == 2:
        if contador_saldo < 3:
            saque = float(input("Insira o valor do saque (R$): "))
            if saque > 0 and saque <= 500:
                if saldo >= saque:
                    saldo -= saque
                    print("Saldo atual: R$ ", saldo)
                    historico_saques.append(saque)
                    contador_saldo += 1
                else:
                    print("Erro: Saldo Insuficiente")
            else:
                print("Valor inválido ou saque máximo alcançado R$ 500.00)")
        else:
            print("Erro: Limite de saques alcançado")

    elif opcao == 3:
        print("\n---- Extrato ----\n")
        print("Ordem\tOperação\tValor")
        for i, deposito in enumerate(historico_deposito, 1):
            print(f"{i}\tDepósito\t R$ {deposito:.2f}")
        for i, saque in enumerate(historico_saques, 1):
            print(f"{i}\tSaque\t R$ {saque:.2f}")
        print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == 4:
        print("Obrigado por utilizar o nosso sistema")