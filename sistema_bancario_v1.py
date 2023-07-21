menu = """
        === MENU ===

    Insira a opcao valida
    para realizar a operacao!

    [d] Realizar Depósito

    [s] Realizar Saque

    [e] Realizar Extrato

    [q] Sair do Sistema

"""
LIMITE_SAQUE = 500
LIMITE_DIARIO = 3
saques_realizados = 0
saldo = 0
mensagem_extrato = ""

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Iniciando operação de Depósito")
        valor_para_deposito = float(input("Insira um valor para ser depositado: "))
        if valor_para_deposito > 0:
            print(f"R${valor_para_deposito:.2f} será depositado na sua conta!")
            saldo += valor_para_deposito
            mensagem_extrato += (f"Deposito no valor de +R${valor_para_deposito:.2f} \n\n")
        else: print("Insira um valor de deposito valido!!")

    elif opcao == "s":
        if(saques_realizados < LIMITE_DIARIO):
            print("Iniciando operacao de Saque")
            valor_para_saque = float(input("Insira um valor para ser sacado: "))
            if valor_para_saque <= LIMITE_SAQUE and valor_para_saque > 0 and valor_para_saque <= saldo:
                print(f"{valor_para_saque:.2f} sera sacado da sua conta!")
                saldo -= valor_para_saque
                saques_realizados += 1
                mensagem_extrato += (f"Saque no valor de -R${valor_para_saque:.2f} \n\n")

            elif valor_para_saque <= 0: 
                print("Insira um valor de saque valido!!")
                
            elif valor_para_saque > LIMITE_SAQUE:
                print("Seu valor para saque esta acima do nosso limite de R$500.00")

            else: print("Voce nao possui esse valor disponivel em sua conta")
        
        else: print("Seu limite de 3 saques diários foi alcançado! Operacao de saque finalizada")

    elif opcao == "e":
        print("\n------------EXTRATO------------\n")
        if mensagem_extrato != "":
            print(mensagem_extrato)
            print("-------------------------------\n")
            print(f"Saldo em conta: R${saldo:.2f}\n")
            print("-------------------------------\n")
        else: 
            print("Não foram realizadas movimentações\n")
            print("-------------------------------\n")
            print(f"Saldo em conta: R${saldo:.2f}\n")
            print("-------------------------------\n")


    elif opcao == "q":
        print("Saindo do sistema. Volte sempre!")
        break

    else: 
        print("Insira uma opcao valida!!")