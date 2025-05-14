menu = "Por favor, selecione uma opção:\n[d] Depositar \n[s] Sacar \n[e] Extrato \n[q] Sair \n=> "

saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito R$ {valor: .2f}\n"
        else: 
            print("Operação falhou. O valor informado é inválido. ") 


    elif opcao == "s":
        print ("Saque")
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = num_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou. Você não tem saldo suficiente.") 

        elif excedeu_limite:
            print("Operação falhou. O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou. Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor: .2f}\n"
            print(f"Saque R$ {valor: .2f}\n")
            num_saques += 1
    
        else:
            print("Operação falou. O valor informado é inválido.")
    
    
    elif opcao == "e":

        print("\n=============== EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
            
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo: .2f}\n")

        print("==========================================")


    elif opcao == "q":
        print("Encerrando Sistema.")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada ") 