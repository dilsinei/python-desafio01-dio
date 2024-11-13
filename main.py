menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_depositado = float(input("Digite o valor depositado: "))
        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f"Depósito: R${valor_depositado: .2f}\n"
        else:
            print("Valor inválido.")
    elif opcao == "s":
        valor_sacado = float(input("Digite o valor para saque: "))
        if saldo >= valor_sacado and numero_saques < LIMITE_SAQUES:
            if valor_sacado <= limite:
                saldo -= valor_sacado
                numero_saques += 1
            else:
                print("Limite máximo de saque por operação: R$500,00")
        else:
            if numero_saques >= LIMITE_SAQUES:
                print("Você atingiu o limite de saques diários.")
            else:
                print("Saldo insuficiente.")
        if valor_sacado > 0:
            extrato += f"Saque: R${valor_sacado:.2f}\n"

    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"Saldo: R${saldo: .2f}\n")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
